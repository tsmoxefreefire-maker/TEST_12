"""🔊 batch 44 — the voice in a real browser (the page served by the real service; a FAKE voice: no key, no internet; FAKE clock).
The browser's Audio is replaced by a recorder (the test decides when a clip «ends»), so «the line waits for the voice» is checked exactly.
Checks: the 🔊 button appears only when the server has a voice · the narrator's line is sent to /tts (stage + the same text) · the line does
NOT move on while the voice speaks, and moves on after it ends (+ a short breath) · 🔇 → back to reading at its own speed, no more voice ·
the story's subtitle is read and the story WAITS for the voice · no voice on the server → no button, no request, the page as before ·
/tts gives a real sound file, made once. Run:  python tests_browser/test_tts_page.py      (from 05_explanation_api)"""
import json
import os
import sys
import tempfile
import urllib.parse

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.environ["EXPLAIN_DATA_DIR"] = tempfile.mkdtemp(prefix="explain_tts_test_")
os.environ["EMBED_PROVIDER"] = "none"
os.environ["TTS_PROVIDER"] = "fake"
sys.path.insert(0, HERE)
from playwright.sync_api import sync_playwright  # noqa: E402

from core import service, tts  # noqa: E402

ORIGIN = "https://ie.test"
SHOTS = os.environ.get("TTS_SHOTS")
res, errs, tts_hits = [], [], []
VOICE_ON = {"on": True}


def ok(n, c, x=""):
    res.append(("✅" if c else "❌") + " " + n + ("" if c else " " + str(x)[:300]))


def handle(route):
    u = urllib.parse.urlparse(route.request.url)
    q = urllib.parse.parse_qs(u.query)
    try:
        if u.path.startswith("/explain"):
            book = u.path.split("/")[2] if u.path.count("/") >= 2 else None
            return route.fulfill(status=200, content_type="text/html; charset=utf-8", body=service.page_html([book] if book else None))
        if u.path == "/tts/status":
            st = service.tts_status() if VOICE_ON["on"] else dict(service.tts_status(), on=False, provider="none")
            return route.fulfill(status=200, content_type="application/json", body=json.dumps(st))
        if u.path == "/tts":
            tts_hits.append(q)
            data, mime = service.tts_audio(q.get("text", [""])[0], q.get("stage", ["kids"])[0])
            return route.fulfill(status=200, content_type=mime, body=data)
        return route.fulfill(status=404, body="not here")
    except Exception as e:   # noqa: BLE001
        return route.fulfill(status=400, body=str(e))


FAKE_AUDIO = """(()=>{window.__aud=[];window.Audio=class{constructor(src){this.src=src;this.l={};window.__aud.push(this);}
  addEventListener(n,f){(this.l[n]=this.l[n]||[]).push(f);} play(){return Promise.resolve();} pause(){} removeAttribute(){} load(){}
  fire(n){(this.l[n]||[]).forEach(f=>f());}};})()"""
STEP = "[...document.querySelectorAll('.stepper .dots i')].findIndex(i=>i.classList.contains('on'))"
LAST = "(()=>{const a=window.__aud[window.__aud.length-1];return a?decodeURIComponent(a.src):'';})()"


def new(b, **kw):
    ctx = b.new_context(viewport=kw.pop("viewport", {"width": 1150, "height": 950}))
    pg = ctx.new_page(); pg.on("pageerror", lambda e: errs.append(str(e)[:200]))
    pg.route("**/fonts.*/**", lambda r: r.abort()); pg.route(ORIGIN + "/**", handle)
    pg.add_init_script(FAKE_AUDIO); pg.clock.install()
    return ctx, pg


service.seed_samples()
book = next(m["book_id"] for m in service.list_books() if m.get("title", "").startswith("العلوم"))   # the plants book (grade 4)
lesson = service.list_lessons(book)[0]["lesson_id"]
with sync_playwright() as p:
    b = p.chromium.launch()
    # ---------- (1) the narrator's line waits for the voice ----------
    ctx, pg = new(b)
    pg.goto(f"{ORIGIN}/explain/{book}?q=hi&lesson={lesson}&at=0&kind=overview"); pg.clock.run_for(1500)
    ok("🔊 the voice button is there (the server has a voice)", pg.locator("#ttsb").count() == 1 and "الصوت" in pg.inner_text("#ttsb"), pg.locator("#ttsb").count())
    first = pg.evaluate(LAST); cap = pg.inner_text("#cap")
    ok("🗣️ the narrator's line is sent to the voice (/tts, the stage, the same words)", "/tts?stage=kids&text=" in first and cap.split()[0].strip("«»") in first, (first[:120], cap[:60]))
    s0 = pg.evaluate(STEP); pg.clock.run_for(25000); s1 = pg.evaluate(STEP)
    ok("⏳ while the voice speaks (25 s), the line does NOT move on", s0 == 0 and s1 == 0, (s0, s1))
    if SHOTS:
        pg.screenshot(path=os.path.join(SHOTS, "tts_button.png"))
    pg.evaluate("window.__aud[window.__aud.length-1].fire('ended')"); pg.clock.run_for(2500)
    s2 = pg.evaluate(STEP); second = pg.evaluate(LAST)
    ok("➡️ the voice ended → a short breath → the next line, and the voice reads it", s2 == 1 and second != first and "/tts?" in second, (s2, second[:80]))
    # ---------- (2) 🔇 off → the page reads at its own speed ----------
    n = pg.evaluate("window.__aud.length")
    pg.click("#ttsb"); pg.clock.run_for(300)
    ok("🔇 the button turns the voice off", pg.get_attribute("#ttsb", "aria-pressed") == "false" and "🔇" in pg.inner_text("#ttsb"))
    cap1 = pg.inner_text("#cap"); pg.clock.run_for(30000)
    ok("🔇 off: the lines move on by themselves again (the next line / the next scene), and no new voice is asked for",
       pg.inner_text("#cap") != cap1 and pg.evaluate("window.__aud.length") == n, (cap1[:40], pg.inner_text("#cap")[:40], n))
    ctx.close()
    # ---------- (3) the story's subtitle is read, and the story waits ----------
    ctx, pg = new(b)
    pg.goto(f"{ORIGIN}/explain/{book}?q=hi"); pg.clock.run_for(1200)
    big = pg.locator("#stBig")
    if big.count() and big.is_visible():
        big.click()
    seen = ""
    for _ in range(60):
        pg.clock.run_for(500)
        seen = pg.evaluate(LAST)
        if seen:
            break
    sub = pg.inner_text("#stSub") if pg.locator("#stSub").count() else ""
    ok("🎬 the story's subtitle is read aloud", "/tts?" in seen and sub and sub.split()[0] in seen, (seen[:80], sub[:60]))
    pg.clock.run_for(20000); t1 = pg.inner_text("#stTime"); pg.clock.run_for(20000); t2 = pg.inner_text("#stTime")   # (the subtitle's own time first)
    ok("⏳ the story WAITS at the end of the subtitle while the voice still speaks (the time stands still)", t1 == t2 and sub in pg.inner_text("#stSub"), (t1, t2))
    pg.evaluate("window.__aud[window.__aud.length-1].fire('ended')"); pg.clock.run_for(3000); t3 = pg.inner_text("#stTime")
    ok("➡️ the voice ended → the story goes on", t3 != t2, (t2, t3))
    ctx.close()
    # ---------- (4) no voice on the server → the page exactly as before ----------
    VOICE_ON["on"] = False
    ctx, pg = new(b)
    pg.goto(f"{ORIGIN}/explain/{book}?q=hi&lesson={lesson}&at=0&kind=overview"); pg.clock.run_for(1500)
    s0 = pg.evaluate(STEP); pg.clock.run_for(30000)
    ok("🚫 no voice: no button, no voice asked for, the lines move on at their own speed",
       pg.locator("#ttsb").count() == 0 and pg.evaluate("window.__aud.length") == 0 and pg.evaluate(STEP) > s0, (pg.evaluate(STEP), pg.evaluate("window.__aud.length")))
    ctx.close()
    VOICE_ON["on"] = True
    # ---------- (5) the phone ----------
    ctx, pg = new(b, viewport={"width": 390, "height": 844})
    pg.goto(f"{ORIGIN}/explain/{book}?q=hi&lesson={lesson}&at=0&kind=overview"); pg.clock.run_for(1500)
    w = pg.evaluate("[document.documentElement.scrollWidth, innerWidth]")
    ok("📱 the phone: the button fits (no sideways scroll)", pg.locator("#ttsb").count() == 1 and w[0] <= w[1] + 1, w)
    if SHOTS:
        pg.screenshot(path=os.path.join(SHOTS, "tts_phone.png"))
    ctx.close()
    b.close()

# ---------- (6) the sound file itself, made once ----------
before = tts.CALLS["n"]
d1, m1 = service.tts_audio("الجذر بيمتص الماء من التربة", "kids")
d2, m2 = service.tts_audio("الجذر بيمتص الماء من التربة", "kids")
ok("🎵 /tts gives a real sound file (WAV) and makes it ONCE (the second time: from the saved file)", d1[:4] == b"RIFF" and d1 == d2 and tts.CALLS["n"] == before + 1, (d1[:4], tts.CALLS["n"] - before))
ok("🔒 the requests were only to our server's /tts (never a key in the page)", all("key" not in json.dumps(h).lower() for h in tts_hits), tts_hits[:1])
ok("no JS error", not errs, errs[:3])
print("\n".join(res))
print(f"✅ {sum(r.startswith('✅') for r in res)} checks passed · ❌ {sum(r.startswith('❌') for r in res)} failed")
