"""🔊 batch 44 · THE VOICE THAT READS THE EXPLANATION (Hareth: «لما الكلام يمشي هو يحكي… موديل كويس وفي نفس الوقت رخيص، إحنا بس نجربه»).
Every line the page shows (the narrator's line under the scene, the story's subtitles) can be read aloud. The page asks
GET /tts?text=…&stage=… → this file makes the sound ONCE (a model), keeps it in data/tts/ (and in the database with the other files),
and every next student gets the same file at once, for free. The page waits for the voice to finish before the next line.

Who speaks (environment variable TTS_PROVIDER, or: an Azure key → azure, else none):
    azure  → AZURE_SPEECH_KEY + AZURE_SPEECH_REGION   (a Jordanian voice: ar-JO-SanaNeural · 0.5M characters free every month)
    gemini → GEMINI_API_KEY (the same key as the rest)  (gemini-3.8-flash-lite-tts, style «speaking slowly…»; only when TTS_PROVIDER=gemini,
                                                         so the team's Gemini key never starts spending on voice by itself)
    elevenlabs → ELEVENLABS_API_KEY + ELEVENLABS_VOICE_ID (🆕 a TRIAL, Hareth: «بدي إليفن لابس… صوت عربي حلو سعودي… تجربة بس»;
                 only when TTS_PROVIDER=elevenlabs · the voice = any Arabic voice from ElevenLabs' Voice Library, by its ID ·
                 model ELEVENLABS_MODEL, default eleven_multilingual_v2 · slower for the little ones: voice_settings.speed)
    fake   → a short tone as long as the text (for the tests: no key, no internet)
    none   → no voice: the page reads at its own (slower) speed, as before
The keys: environment variables on the server (Render dashboard) or 02_question_factory/api_key.txt — NEVER in GitHub."""
import base64
import hashlib
import io
import json
import math
import os
import re
import sys
import urllib.error
import urllib.request
import wave

from core import settings

MAX_CHARS = 400                                                   # one line of the page (a longer text is not a line: refused)
TIMEOUT = 25
STAGES = ("kids", "junior", "teen", "senior")
# slower for the little ones (Azure: SSML prosody · Gemini: the style line)
RATE = {"kids": "-20%", "junior": "-12%", "teen": "-5%", "senior": "0%"}
STYLE = {"kids": "speaking slowly, warm and friendly, for a young child",
         "junior": "speaking a little slowly, clear and friendly, for a curious student",
         "teen": "speaking clearly at a calm pace, like a confident classmate",
         "senior": "speaking clearly and calmly, like a teacher"}
VOICE = {"azure": os.environ.get("TTS_VOICE_AZURE", "ar-JO-SanaNeural"),
         "gemini": os.environ.get("TTS_VOICE_GEMINI", "Sulafat")}
MODEL_GEMINI = os.environ.get("TTS_MODEL_GEMINI", "gemini-3.8-flash-lite-tts")
# 🆕 ElevenLabs (trial): the speed by age (1.0 = normal; ElevenLabs takes about 0.7–1.2) · the voice and the model are read at each call
SPEED_ELEVEN = {"kids": 0.85, "junior": 0.9, "teen": 0.95, "senior": 1.0}
ELEVEN_DEFAULT_VOICE = "EXAVITQu4vr4xnSDxMaL"                    # a ready voice of every account (NOT Arabic-born): set ELEVENLABS_VOICE_ID to a Saudi one
_el_voice = lambda: os.environ.get("ELEVENLABS_VOICE_ID", "").strip() or ELEVEN_DEFAULT_VOICE
_el_model = lambda: os.environ.get("ELEVENLABS_MODEL", "").strip() or "eleven_multilingual_v2"
CALLS = {"n": 0}                                                  # how many times we called a model (the tests check it)
_EMOJI = re.compile("[\U0001F000-\U0001FAFF←-⇿⌀-⏿①-➿⬀-⯿️‍]")


class TTSError(Exception):
    pass


def _keys() -> dict:
    sys.path.insert(0, settings.FACTORY_DIR)
    import llm_gateway                                            # the same keys as the rest of the project (env or api_key.txt)
    try:
        return llm_gateway.read_settings()["keys"]
    except Exception:
        return {}


def provider() -> str:
    """who speaks now: azure · gemini · fake · none"""
    p = os.environ.get("TTS_PROVIDER", "").strip().lower()
    if p in ("fake", "none"):
        return p
    if p == "elevenlabs":
        return "elevenlabs" if os.environ.get("ELEVENLABS_API_KEY", "").strip() else "none"
    if p == "gemini":
        return "gemini" if (os.environ.get("GEMINI_API_KEY") or _keys().get("gemini")) else "none"
    if p in ("azure", ""):
        return "azure" if os.environ.get("AZURE_SPEECH_KEY") and os.environ.get("AZURE_SPEECH_REGION") else "none"
    return "none"


def clean(text: str) -> str:
    """What is READ: the line without emoji, «» marks and bullets (the same text the student reads, said cleanly)."""
    t = _EMOJI.sub(" ", str(text or ""))
    t = re.sub(r"[«»•·|]", " ", t)
    t = re.sub(r"\s+", " ", t).strip(" -–—:")
    return t


def _ext(p: str) -> str:
    return "mp3" if p in ("azure", "elevenlabs") else "wav"


def _name(p: str, text: str, stage: str) -> str:
    """the clip's file name = a fingerprint of everything that changes the sound (the same line → the same file, forever)"""
    voice = _el_voice() if p == "elevenlabs" else VOICE.get(p, p)
    model = MODEL_GEMINI if p == "gemini" else _el_model() if p == "elevenlabs" else ""
    h = hashlib.sha1(f"{p}|{voice}|{model}|{RATE[stage]}|{text}".encode("utf-8")).hexdigest()[:24]
    return f"{h}.{_ext(p)}"


def _dir() -> str:
    return os.environ.get("TTS_DIR") or os.path.join(settings.DATA_DIR, "tts")   # (TTS_DIR: only the tests move it)


def folder() -> str:
    d = _dir()
    os.makedirs(d, exist_ok=True)
    return d


def status() -> dict:
    p = provider()
    d = _dir()
    n = len([x for x in os.listdir(d) if x.endswith((".mp3", ".wav"))]) if os.path.isdir(d) else 0
    return {"on": p != "none", "provider": p, "voice": _el_voice() if p == "elevenlabs" else VOICE.get(p, ""),
            "model": MODEL_GEMINI if p == "gemini" else _el_model() if p == "elevenlabs" else "",
            "clips": n, "max_chars": MAX_CHARS}


def speak(text: str, stage: str = "kids"):
    """(bytes, media type, made_now) for one line. Made once, then always from the file. Raises TTSError (no voice / bad text / model failed)."""
    p = provider()
    if p == "none":
        raise TTSError("off")
    t = clean(text)
    if not t:
        raise TTSError("empty")
    if len(t) > MAX_CHARS:
        raise TTSError("too long")
    stage = stage if stage in STAGES else "kids"
    path = os.path.join(folder(), _name(p, t, stage))
    mime = "audio/mpeg" if path.endswith(".mp3") else "audio/wav"
    if os.path.exists(path) and os.path.getsize(path) > 0:
        with open(path, "rb") as f:
            return f.read(), mime, False
    data = {"azure": _azure, "gemini": _gemini, "elevenlabs": _eleven, "fake": _fake}[p](t, stage)
    if not data:
        raise TTSError("no sound")
    tmp = path + ".tmp"
    with open(tmp, "wb") as f:
        f.write(data)
    os.replace(tmp, path)
    return data, mime, True


# ---------- the providers ----------
def _azure(text: str, stage: str) -> bytes:
    key, region = os.environ.get("AZURE_SPEECH_KEY", ""), os.environ.get("AZURE_SPEECH_REGION", "")
    voice = VOICE["azure"]
    lang = "-".join(voice.split("-")[:2]) or "ar-JO"
    esc = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    ssml = (f"<speak version='1.0' xml:lang='{lang}'><voice xml:lang='{lang}' name='{voice}'>"
            f"<prosody rate='{RATE[stage]}'>{esc}</prosody></voice></speak>")
    req = urllib.request.Request(f"https://{region}.tts.speech.microsoft.com/cognitiveservices/v1", data=ssml.encode("utf-8"), method="POST",
                                 headers={"Ocp-Apim-Subscription-Key": key, "Content-Type": "application/ssml+xml",
                                          "X-Microsoft-OutputFormat": "audio-24khz-48kbitrate-mono-mp3", "User-Agent": "interactive-explanation"})
    CALLS["n"] += 1
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            return r.read()
    except Exception as e:                                        # (the key never goes into the message)
        raise TTSError(f"azure: {type(e).__name__}")


def _find_audio(o):
    """the first base64 audio in a Gemini answer (the Interactions API: steps[].content[].data · the older one: inlineData.data)"""
    if isinstance(o, dict):
        if isinstance(o.get("inlineData"), dict) and o["inlineData"].get("data"):
            return o["inlineData"]["data"], o["inlineData"].get("mimeType", "")
        if isinstance(o.get("data"), str) and len(o["data"]) > 100 and "audio" in str(o.get("mime_type") or o.get("mimeType") or o.get("type") or "audio"):
            return o["data"], str(o.get("mime_type") or o.get("mimeType") or "")
        for v in o.values():
            r = _find_audio(v)
            if r:
                return r
    elif isinstance(o, list):
        for v in o:
            r = _find_audio(v)
            if r:
                return r
    return None


def _wav(pcm: bytes, rate: int = 24000) -> bytes:
    b = io.BytesIO()
    with wave.open(b, "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(rate)
        w.writeframes(pcm)
    return b.getvalue()


def _gemini(text: str, stage: str) -> bytes:
    key = os.environ.get("GEMINI_API_KEY") or _keys().get("gemini", "")
    body = {"model": MODEL_GEMINI,
            "input": [{"type": "user_input", "content": [{"type": "text", "text": text,
                                                          "annotations": [{"type": "speech_metadata", "style": STYLE[stage]}]}]}],
            "response_format": {"type": "audio"},
            "generation_config": {"speech_config": [{"voice": VOICE["gemini"]}]}}
    req = urllib.request.Request("https://generativelanguage.googleapis.com/v1beta/interactions", data=json.dumps(body).encode("utf-8"),
                                 method="POST", headers={"x-goog-api-key": key, "Content-Type": "application/json"})
    CALLS["n"] += 1
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            ans = json.loads(r.read().decode("utf-8"))
    except Exception as e:
        raise TTSError(f"gemini: {type(e).__name__}")
    found = _find_audio(ans)
    if not found:
        raise TTSError("gemini: no audio in the answer")
    raw, mime = base64.b64decode(found[0]), found[1].lower()
    return raw if raw[:4] == b"RIFF" else _wav(raw)              # headerless PCM (audio/l16) → a WAV file


def _eleven(text: str, stage: str) -> bytes:
    """🆕 ElevenLabs (trial): POST /v1/text-to-speech/{voice_id} · header xi-api-key · the answer IS the mp3 file"""
    key = os.environ.get("ELEVENLABS_API_KEY", "").strip()
    body = {"text": text, "model_id": _el_model(),
            "voice_settings": {"stability": 0.5, "similarity_boost": 0.75, "style": 0, "use_speaker_boost": True, "speed": SPEED_ELEVEN[stage]}}
    req = urllib.request.Request(f"https://api.elevenlabs.io/v1/text-to-speech/{_el_voice()}?output_format=mp3_44100_128",
                                 data=json.dumps(body).encode("utf-8"), method="POST",
                                 headers={"xi-api-key": key, "Content-Type": "application/json", "Accept": "audio/mpeg"})
    CALLS["n"] += 1
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            return r.read()
    except urllib.error.HTTPError as e:                           # 🆕 say WHY (ElevenLabs' own reason: a wrong key, the plan, the voice…) — never the key
        why = ""
        try:
            d = json.loads(e.read().decode("utf-8", "replace") or "{}").get("detail")
            why = (d.get("status", "") + " " + str(d.get("message", ""))) if isinstance(d, dict) else str(d or "")
        except Exception:
            pass
        why = re.sub(r"\s+", " ", why.replace(key, "***") if key else why).strip()[:160]
        raise TTSError(f"elevenlabs {e.code}: {why or e.reason}")
    except Exception as e:                                        # (the key never goes into the message)
        raise TTSError(f"elevenlabs: {type(e).__name__}")


def _fake(text: str, stage: str) -> bytes:
    """a soft tone, 60 ms per letter (slower for the little ones): the page can test «wait for the voice» with no key and no internet"""
    CALLS["n"] += 1
    secs = max(0.6, min(20.0, len(text) * 0.06 * {"kids": 1.25, "junior": 1.12}.get(stage, 1.0)))
    rate = 8000
    n = int(secs * rate)
    pcm = bytearray()
    for i in range(n):
        v = int(1800 * math.sin(2 * math.pi * 330 * i / rate) * min(1, i / 400, (n - i) / 400))
        pcm += int(v).to_bytes(2, "little", signed=True)
    return _wav(bytes(pcm), rate)
