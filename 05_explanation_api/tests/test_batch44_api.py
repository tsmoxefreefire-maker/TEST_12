"""🔊 batch 44: the voice (core/tts.py) — who speaks, what is read, made once, the two real providers' requests (checked against their
docs, with the network replaced: no key, no internet here), the endpoints, and the page reads slower (Hareth: «الطالب ما بيلحق يقرا»)."""
import base64
import json
import os
import tempfile
import unittest
from unittest import mock

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("EXPLAIN_SEED", "0")
os.environ.setdefault("EXPLAIN_DATA_DIR", tempfile.mkdtemp())
import sys  # noqa: E402
sys.path.insert(0, HERE)
from core import service, tts  # noqa: E402
try:
    from fastapi.testclient import TestClient
    from main import app
    HAVE = True
except ImportError:
    HAVE = False

TEMPLATE = os.path.join(os.path.dirname(HERE), "02_question_factory", "player", "explain_template.html")


class _Answer:
    def __init__(self, body: bytes):
        self.body = body

    def read(self):
        return self.body

    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False


class TestWhoSpeaks(unittest.TestCase):
    def test_no_key_no_voice(self):
        with mock.patch.dict(os.environ, {"TTS_PROVIDER": "", "AZURE_SPEECH_KEY": "", "AZURE_SPEECH_REGION": ""}):
            self.assertEqual(tts.provider(), "none")
            self.assertFalse(tts.status()["on"])
            with self.assertRaises(service.NotFound):
                service.tts_audio("مرحبا")

    def test_an_azure_key_turns_it_on_and_gemini_only_when_asked(self):
        with mock.patch.dict(os.environ, {"TTS_PROVIDER": "", "AZURE_SPEECH_KEY": "k", "AZURE_SPEECH_REGION": "westeurope"}):
            self.assertEqual(tts.provider(), "azure")
        with mock.patch.dict(os.environ, {"TTS_PROVIDER": "", "AZURE_SPEECH_KEY": "", "GEMINI_API_KEY": "g"}):
            self.assertEqual(tts.provider(), "none")                 # the team's Gemini key never starts spending on voice by itself
        with mock.patch.dict(os.environ, {"TTS_PROVIDER": "gemini", "GEMINI_API_KEY": "g"}):
            self.assertEqual(tts.provider(), "gemini")

    def test_what_is_read(self):
        self.assertEqual(tts.clean("🎉 «الجذر» بيمتص الماء! 👇"), "الجذر بيمتص الماء!")
        self.assertEqual(tts.clean("• 🖐️ دورك!"), "دورك!")


class TestMadeOnce(unittest.TestCase):
    def setUp(self):
        self.env = mock.patch.dict(os.environ, {"TTS_PROVIDER": "fake", "TTS_DIR": tempfile.mkdtemp()})
        self.env.start()

    def tearDown(self):
        self.env.stop()

    def test_the_same_line_is_made_once_and_kept(self):
        n = tts.CALLS["n"]
        a, mime = service.tts_audio("«الساق» بتحمل الماء", "kids")
        b, _ = service.tts_audio("الساق بتحمل الماء", "kids")       # the same words (the marks are not read)
        self.assertEqual(a, b); self.assertEqual(mime, "audio/wav"); self.assertEqual(tts.CALLS["n"], n + 1)
        self.assertEqual(tts.status()["clips"], 1)
        c, _ = service.tts_audio("الساق بتحمل الماء", "senior")       # another age = another speed = another clip
        self.assertNotEqual(a, c); self.assertEqual(tts.status()["clips"], 2)

    def test_bad_lines(self):
        with self.assertRaises(service.BadInput):
            service.tts_audio("   🎉  ")
        with self.assertRaises(service.BadInput):
            service.tts_audio("ا" * (tts.MAX_CHARS + 1))


class TestTheRealProviders(unittest.TestCase):
    def setUp(self):
        self.env = mock.patch.dict(os.environ, {"TTS_DIR": tempfile.mkdtemp()})
        self.env.start()

    def tearDown(self):
        self.env.stop()

    def test_azure_request_jordanian_voice_slower_for_kids(self):
        seen = {}

        def fake_open(req, timeout=None):
            seen["url"], seen["headers"], seen["body"] = req.full_url, dict(req.header_items()), req.data.decode("utf-8")
            return _Answer(b"ID3fake-mp3")
        with mock.patch.dict(os.environ, {"TTS_PROVIDER": "azure", "AZURE_SPEECH_KEY": "secret-key", "AZURE_SPEECH_REGION": "westeurope"}), \
                mock.patch("urllib.request.urlopen", fake_open):
            data, mime, new = tts.speak("الجذر بيمتص الماء", "kids")
        self.assertEqual((data, mime, new), (b"ID3fake-mp3", "audio/mpeg", True))
        self.assertEqual(seen["url"], "https://westeurope.tts.speech.microsoft.com/cognitiveservices/v1")
        h = {k.lower(): v for k, v in seen["headers"].items()}
        self.assertEqual(h["content-type"], "application/ssml+xml"); self.assertEqual(h["x-microsoft-outputformat"], "audio-24khz-48kbitrate-mono-mp3")
        self.assertEqual(h["ocp-apim-subscription-key"], "secret-key"); self.assertTrue(h["user-agent"])
        self.assertIn("name='ar-JO-SanaNeural'", seen["body"]); self.assertIn("rate='-20%'", seen["body"]); self.assertIn("الجذر بيمتص الماء", seen["body"])

    def test_azure_failure_never_shows_the_key(self):
        def boom(req, timeout=None):
            raise OSError("401 for key secret-key")
        with mock.patch.dict(os.environ, {"TTS_PROVIDER": "azure", "AZURE_SPEECH_KEY": "secret-key", "AZURE_SPEECH_REGION": "x"}), \
                mock.patch("urllib.request.urlopen", boom):
            with self.assertRaises(service.BadInput) as cm:
                service.tts_audio("نص جديد للتجربة")
        self.assertNotIn("secret-key", str(cm.exception))

    def test_cartesia_request_voice_model_speed_and_no_key_leak(self):
        seen = {}

        def fake_open(req, timeout=None):
            seen["url"], seen["headers"], seen["body"] = req.full_url, dict(req.header_items()), json.loads(req.data.decode("utf-8"))
            return _Answer(b"ID3cartesia-mp3")
        env = {"TTS_PROVIDER": "cartesia", "CARTESIA_API_KEY": "sk_car_secret", "CARTESIA_VOICE_ID": "voice-123"}
        with mock.patch.dict(os.environ, env), mock.patch("urllib.request.urlopen", fake_open):
            data, mime, new = tts.speak("الجذر بيمتص الماء", "kids")
        self.assertEqual((data, mime, new), (b"ID3cartesia-mp3", "audio/mpeg", True))
        self.assertEqual(seen["url"], "https://api.cartesia.ai/tts/bytes")
        h = {k.lower(): v for k, v in seen["headers"].items()}
        self.assertEqual(h["x-api-key"], "sk_car_secret"); self.assertEqual(h["cartesia-version"], "2025-04-16")
        b = seen["body"]
        self.assertEqual((b["model_id"], b["language"], b["voice"]), ("sonic-3", "ar", {"mode": "id", "id": "voice-123"}))
        self.assertEqual(b["output_format"]["container"], "mp3"); self.assertEqual(b["generation_config"]["speed"], 0.85)
        self.assertEqual(b["transcript"], "الجذر بيمتص الماء")

        def boom(req, timeout=None):
            raise OSError("401 for key sk_car_secret")
        with mock.patch.dict(os.environ, env), mock.patch("urllib.request.urlopen", boom):
            with self.assertRaises(service.BadInput) as cm:
                service.tts_audio("نص جديد للتجربة كارتيزيا")
        self.assertNotIn("sk_car_secret", str(cm.exception))

    def test_cartesia_needs_key_and_voice(self):
        with mock.patch.dict(os.environ, {"TTS_PROVIDER": "cartesia", "CARTESIA_API_KEY": ""}):
            self.assertEqual(tts.provider(), "none")
        with mock.patch.dict(os.environ, {"TTS_PROVIDER": "cartesia", "CARTESIA_API_KEY": "k", "CARTESIA_VOICE_ID": ""}):
            self.assertEqual(tts.provider(), "cartesia")
            with self.assertRaises(tts.TTSError):
                tts.speak("نص بلا صوت محدد", "kids")

    def test_gemini_request_and_both_answer_shapes(self):
        wav = tts._wav(b"\x00\x00" * 2400)
        answers = [{"steps": [{"content": [{"type": "audio", "mime_type": "audio/wav", "data": base64.b64encode(wav).decode()}]}]},
                   {"candidates": [{"content": {"parts": [{"inlineData": {"mimeType": "audio/L16;rate=24000", "data": base64.b64encode(b"\x01\x00" * 3000).decode()}}]}}]}]
        seen = []

        def fake_open(req, timeout=None):
            seen.append((req.full_url, dict(req.header_items()), json.loads(req.data.decode("utf-8"))))
            return _Answer(json.dumps(answers[len(seen) - 1]).encode())
        with mock.patch.dict(os.environ, {"TTS_PROVIDER": "gemini", "GEMINI_API_KEY": "g-key"}), mock.patch("urllib.request.urlopen", fake_open):
            a, mime, _ = tts.speak("أول جملة", "kids")
            b, _, _ = tts.speak("ثاني جملة", "teen")
        url, headers, body = seen[0]
        self.assertEqual(url, "https://generativelanguage.googleapis.com/v1beta/interactions")
        self.assertEqual({k.lower(): v for k, v in headers.items()}["x-goog-api-key"], "g-key")
        self.assertEqual(body["model"], tts.MODEL_GEMINI); self.assertEqual(body["response_format"], {"type": "audio"})
        self.assertEqual(body["generation_config"]["speech_config"][0]["voice"], tts.VOICE["gemini"])
        part = body["input"][0]["content"][0]
        self.assertEqual(part["text"], "أول جملة"); self.assertIn("slowly", part["annotations"][0]["style"])   # the style is NOT in the text (read verbatim)
        self.assertEqual(mime, "audio/wav"); self.assertEqual(a[:4], b"RIFF"); self.assertEqual(b[:4], b"RIFF")   # headerless PCM → WAV


@unittest.skipUnless(HAVE, "fastapi not installed")
class TestEndpoints(unittest.TestCase):
    def test_status_and_a_line(self):
        c = TestClient(app)
        with mock.patch.dict(os.environ, {"TTS_PROVIDER": "fake", "TTS_DIR": tempfile.mkdtemp()}):
            st = c.get("/tts/status").json()
            self.assertTrue(st["on"]); self.assertEqual(st["provider"], "fake")
            r = c.get("/tts", params={"text": "الورقة بتصنع الغذاء", "stage": "junior"})
            self.assertEqual(r.status_code, 200); self.assertTrue(r.headers["content-type"].startswith("audio/")); raw = r.content if hasattr(r, "content") else r.text   # (the real TestClient · the sandbox's stand-in)
            self.assertEqual(raw[:4], b"RIFF")
            self.assertEqual(c.get("/tts", params={"text": "ا" * 900}).status_code, 400)
        with mock.patch.dict(os.environ, {"TTS_PROVIDER": "none"}):
            self.assertEqual(c.get("/tts", params={"text": "مرحبا"}).status_code, 404)


class TestThePageReadsSlower(unittest.TestCase):
    def test_reading_time_by_age_is_longer(self):
        with open(TEMPLATE, encoding="utf-8") as f:
            page = f.read()
        self.assertIn("const AUTO_SPEED={kids:1.7,junior:1.4,teen:1.2,senior:1.05}", page)   # was 1.3 · 1.12 · 1 · 0.9
        self.assertIn("ttsSay(VOICE(s.steps[STEP]", page)                                  # the line is read, and waits for the voice
        self.assertIn('fetch("/tts/status")', page)


if __name__ == "__main__":
    unittest.main()
