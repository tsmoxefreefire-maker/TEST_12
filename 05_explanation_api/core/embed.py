"""🆕 batch 42 · MEANING-NUMBERS (embeddings) for the search by meaning — OPTIONAL (Hareth: «حطه، وأنا بعدين بحط المفتاح»).

A text → a list of numbers; two texts that MEAN the same get close numbers («ليش النبتة بتعطش؟» ≈ «النبات يحتاج الماء»),
even with no word in common. The scene descriptions are turned into numbers ONCE (when a book is made, before any student),
and only the student's question at the moment he asks (and a question asked before is remembered: no second call).

Who makes the numbers (the environment variable EMBED_PROVIDER, or the first key found):
    gemini  → GEMINI_API_KEY   (gemini-embedding-2, 768 numbers)
    openai  → OPENAI_API_KEY   (text-embedding-3-small, 768 numbers)
    fake    → a pretend model for the tests (no internet, no key, no cost): same words → same numbers
    none    → no search by meaning (the search by name and by spelling still works)
The keys: environment variables on the server (Render dashboard) or 02_question_factory/api_key.txt — NEVER in GitHub."""
import hashlib
import json
import math
import os
import re
import sys
import urllib.request

from core import settings

DIM = 768
TIMEOUT = 20
MODELS = {"gemini": os.environ.get("EMBED_MODEL_GEMINI", "gemini-embedding-2"),
          "openai": os.environ.get("EMBED_MODEL_OPENAI", "text-embedding-3-small")}
MIN_SCORE = {"gemini": 0.62, "openai": 0.45, "fake": 0.35}      # below this the closest scene is not close enough (tuned on real questions later)
_CACHE = {}                                                      # question → numbers (a question asked again costs nothing)
CALLS = {"n": 0}                                                 # how many times we called the model (the tests check it)


def _keys() -> dict:
    sys.path.insert(0, settings.FACTORY_DIR)
    import llm_gateway                                           # the same keys as the rest of the project (env or api_key.txt)
    return llm_gateway.read_settings()["keys"]


def provider() -> str:
    """which provider makes the numbers now ('none' = no search by meaning)."""
    p = os.environ.get("EMBED_PROVIDER", "").strip().lower()
    if p in ("fake", "none"):
        return p
    try:
        keys = _keys()
    except Exception:
        keys = {}
    if p in ("gemini", "openai"):
        return p if keys.get(p) else "none"
    return next((x for x in ("gemini", "openai") if keys.get(x)), "none")


def model_name() -> str:
    p = provider()
    return {"fake": "fake-768", "none": ""}.get(p, f"{p}:{MODELS.get(p, '')}:{DIM}")


def _unit(v):
    n = math.sqrt(sum(x * x for x in v)) or 1.0
    return [x / n for x in v]


# ---------- the pretend model (tests) ----------
def _fake(text: str):
    """same words → same numbers; shared words → close numbers. Not a real meaning model: it only proves the wiring."""
    sys.path.insert(0, settings.FACTORY_DIR)
    import scene_questions as sq
    v = [0.0] * DIM
    for w in sq.words(text):
        for k in range(2):
            h = int(hashlib.md5(f"{k}:{w}".encode()).hexdigest(), 16)
            v[h % DIM] += 1.0 if (h >> 12) & 1 else -1.0
    return _unit(v)


# ---------- the real providers ----------
def _post(url, body, headers):
    req = urllib.request.Request(url, data=json.dumps(body).encode(), headers=dict({"Content-Type": "application/json"}, **headers))
    with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
        return json.loads(r.read().decode())


def _gemini(texts, kind):
    key, m = _keys()["gemini"], MODELS["gemini"]
    pre = "task: search result | query: " if kind == "query" else "title: none | text: "      # the model's own way to say query / document
    body = {"requests": [{"model": f"models/{m}", "content": {"parts": [{"text": pre + t}]}, "output_dimensionality": DIM} for t in texts]}
    data = _post(f"https://generativelanguage.googleapis.com/v1beta/models/{m}:batchEmbedContents", body, {"x-goog-api-key": key})
    return [_unit(e["values"]) for e in data["embeddings"]]


def _openai(texts, kind):
    data = _post("https://api.openai.com/v1/embeddings", {"model": MODELS["openai"], "input": list(texts), "dimensions": DIM},
                 {"Authorization": "Bearer " + _keys()["openai"]})
    return [_unit(d["embedding"]) for d in sorted(data["data"], key=lambda d: d["index"])]


def embed(texts, kind: str = "document"):
    """texts → their numbers (kind: 'document' for the scenes, 'query' for a student's question). None if no provider."""
    p = provider()
    if p == "none" or not texts:
        return None
    texts = [re.sub(r"\s+", " ", t)[:6000] for t in texts]
    if p == "fake":
        CALLS["n"] += 1
        return [_fake(t) for t in texts]
    out = []
    for i in range(0, len(texts), 64):                                 # a few at a time (the providers limit one request)
        CALLS["n"] += 1
        out += (_gemini if p == "gemini" else _openai)(texts[i:i + 64], kind)
    return out


def query(text: str):
    """the numbers of ONE question (remembered: the same question again → no call)."""
    k = (model_name(), text.strip())
    if k not in _CACHE:
        v = embed([text], "query")
        if v is None:
            return None
        if len(_CACHE) > 5000:
            _CACHE.clear()
        _CACHE[k] = v[0]
    return _CACHE[k]


def min_score() -> float:
    return MIN_SCORE.get(provider(), 0.6)
