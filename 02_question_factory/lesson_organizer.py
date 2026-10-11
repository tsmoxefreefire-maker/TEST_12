# -*- coding: utf-8 -*-
"""🆕 batch 46 · THE MODEL ORGANIZES THE LESSON'S TEXT (the engineer: «الـ LLM هو اللي بينسّق»; the plan: the LLM decides how to explain,
it is NOT the source of truth — RAG is — and it never invents what the content does not say).

ONE call per lesson: the lesson's concepts (from the graph) + the lesson's own text (lesson_input.cut_lesson_text) → for each concept:
    name      a short name for the character (1–4 words)
    explain   one simple sentence that explains it, from the text
    examples  up to 3 short examples, from the text (e.g. «10 و20 و50»)
    problem   the book's own problem about it, or ""
Then THE CODE CHECKS every field (check()): only the graph's concepts · every number must be in the text · the explanation must share
words with the text or the concept · short lengths. A field that fails is dropped; a concept with nothing left keeps the team's description.
The answer is kept (made ONCE per lesson + text: the same request again costs nothing). No key / a broken answer → the graph alone."""
import hashlib
import json
import os
import re

_AR_DIGITS = str.maketrans("٠١٢٣٤٥٦٧٨٩", "0123456789")
_TASHKEEL = re.compile("[ؐ-ًؚ-ٰٟۖ-ۭ]")
_STOP = set("في من على الى إلى عن مع هو هي هذا هذه ذلك التي الذي ثم او أو كل بين حتى عند لكل كما لأن الا إلا ما لا ان أن".split())
SYSTEM = "You answer with ONE JSON object only. You organize a school lesson for children from its OWN text: never add a fact, a number or an example the text does not have."


def _norm(s: str) -> str:
    s = _TASHKEEL.sub("", str(s or "")).translate(_AR_DIGITS)
    return s.replace("أ", "ا").replace("إ", "ا").replace("آ", "ا").replace("ة", "ه").replace("ى", "ي")


def _words(s: str) -> set:
    return {w for w in re.findall(r"[ء-ي]{3,}", _norm(s)) if w not in _STOP and w[2:] not in _STOP}


def _numbers(s: str) -> set:
    return set(re.findall(r"\d+", _norm(s)))


def prompt(entities: list, text: str, subject: str = "", grade=None) -> str:
    ents = [{"id": str(e.get("id")), "name": e.get("text"), "graph_description": e.get("description") or (e.get("metadata") or {}).get("description", "")}
            for e in entities]
    return ("درس من كتاب مدرسي" + (f" (المادة: {subject}" + (f"، الصف: {grade}" if grade else "") + ")" if subject else "") + ".\n"
            "المفاهيم (من الجراف):\n" + json.dumps(ents, ensure_ascii=False) + "\n\n"
            "نص الدرس من الكتاب:\n<<<\n" + text[:6000] + "\n>>>\n\n"
            "رتّب لكل مفهوم من النص فقط، بعربي بسيط لطالب بهذا الصف:\n"
            '{"concepts": [{"id": "...", "name": "اسم قصير من 1 إلى 4 كلمات", "explain": "جملة واحدة بسيطة تشرح المفهوم (أقل من 20 كلمة)", '
            '"examples": ["مثال قصير من النص", "..."], "problem": "مسألة الكتاب عن هذا المفهوم كما هي، أو فاضي"}]}\n'
            "قواعد: لا تضف أي رقم أو مثال أو معلومة مش موجودة بالنص · examples أقصاها 3 · إذا النص ما فيه شي عن مفهوم خلّي explain فاضي · "
            "نفس الـ id بالضبط.")


def _parse(raw: str) -> dict:
    raw = str(raw or "")
    i, j = raw.find("{"), raw.rfind("}")
    if i < 0 or j <= i:
        return {}
    try:
        return json.loads(raw[i:j + 1])
    except Exception:
        return {}


def check(answer: dict, entities: list, text: str) -> dict:
    """{entity_id: {"name", "explain", "examples", "problem"}} — only what passes; the reasons of what did not are in "_dropped" """
    ids = {str(e.get("id")): e for e in entities}
    tnum, twords, out, dropped = _numbers(text), _words(text), {}, []
    for c in (answer or {}).get("concepts", []) if isinstance(answer, dict) else []:
        cid = str(c.get("id", ""))
        if cid not in ids:
            dropped.append(f"{cid}: مش من الجراف"); continue
        e, keep = ids[cid], {}
        own = _words(e.get("text", "")) | _words(e.get("description", ""))
        name = re.sub(r"\s+", " ", str(c.get("name") or "")).strip(" .،")
        if 1 <= len(name.split()) <= 4 and re.search(r"[ء-ي]", name) and not (_numbers(name) - tnum):
            keep["name"] = name
        ex = re.sub(r"\s+", " ", str(c.get("explain") or "")).strip()
        if ex and len(ex.split()) <= 25 and not (_numbers(ex) - tnum) and (_words(ex) & (twords | own)):
            keep["explain"] = ex.rstrip(".")
        elif ex:
            dropped.append(f"{cid}: الشرح فيه إشي مش بالنص")
        exs = []
        for x in (c.get("examples") or [])[:3]:
            x = re.sub(r"\s+", " ", str(x or "")).strip(" .،")
            if x and len(x.split()) <= 12 and not (_numbers(x) - tnum) and (_numbers(x) or (_words(x) & twords)):
                exs.append(x)
            elif x:
                dropped.append(f"{cid}: مثال مش من النص ({x[:30]})")
        if exs:
            keep["examples"] = exs
        pb = re.sub(r"\s+", " ", str(c.get("problem") or "")).strip()
        if pb and len(pb.split()) <= 40 and not (_numbers(pb) - tnum) and len(_words(pb) & twords) >= max(2, len(_words(pb)) // 2):
            keep["problem"] = re.sub(r"^\d{1,2}\s+(?=\D)", "", pb)          # (without the exercise's own number)
        elif pb:
            dropped.append(f"{cid}: المسألة مش من الكتاب")
        if keep:
            out[cid] = keep
    out["_dropped"] = dropped
    return out


def description(org: dict, original: str = "") -> str:
    """The text the factory reads for a concept (its pieces are split at «؛»): the explanation · the examples · the book's problem.
    Nothing usable → the team's description."""
    parts = []
    if org.get("explain"):
        parts.append(org["explain"])
    if org.get("examples"):
        parts.append("أمثلة: " + " و".join(org["examples"]))
    if org.get("problem"):
        parts.append(org["problem"].replace("؛", "،"))
    if original and not org.get("explain"):
        parts.insert(0, original.strip(" ."))
    return "؛ ".join(p.strip(" .؛") for p in parts if p) or (original or "")


def _cache_dir() -> str:
    return os.environ.get("ORGANIZED_DIR") or os.path.join(os.environ.get("EXPLAIN_DATA_DIR", os.path.join(os.path.dirname(__file__), "data")), "organized")


def organize(entities: list, text: str, llm, subject: str = "", grade=None, cache_dir: str = None) -> dict:
    """{entity_id: {...}} checked, plus "_dropped" and "_source" ("model" · "kept" · "none"). Made once per (concepts + text)."""
    if not entities or not (text or "").strip():
        return {"_dropped": [], "_source": "none"}
    key = hashlib.sha1(json.dumps([[str(e.get("id")), e.get("text")] for e in entities], ensure_ascii=False).encode("utf-8") + text.encode("utf-8")).hexdigest()[:20]
    path = os.path.join(cache_dir or _cache_dir(), key + ".json")
    if os.path.exists(path):
        try:
            with open(path, encoding="utf-8") as f:
                return dict(json.load(f), _source="kept")
        except Exception:
            pass
    if not llm:
        return {"_dropped": [], "_source": "none"}
    try:
        raw = llm(SYSTEM, prompt(entities, text, subject, grade))
    except Exception as e:                                       # (no credit, no network…): the graph alone, the page still works
        return {"_dropped": [f"الموديل ما رد: {type(e).__name__}"], "_source": "none"}
    res = check(_parse(raw), entities, text)
    if any(k for k in res if not k.startswith("_")):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(res, f, ensure_ascii=False)
    return dict(res, _source="model")
