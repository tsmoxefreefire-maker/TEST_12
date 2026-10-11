"""🆕 batch 35 (Hareth's notes) in a real browser:
(1) PLACES: every lesson has its place (by the subject, or the JSON's "place" on the book / a lesson), behind every scene
    (softly, at the edges only) and fully behind the cartoons — and the story says where it happens;
(2) the places LIVE: the props move, a tap makes a prop wiggle with a sound, the background extras chat by themselves
    (the little ones' stages) and hop when tapped — never a fact; still with the light quality;
(3) the CHARACTERS have little arms (the younger stages), none for the older ones;
(4) the FACT BUDGET shows: a concept is the cartoon + a few scenes (≤ 4 + a film / slider).
python tests_browser/test_batch35.py"""
import json, os, pathlib, sys, tempfile, urllib.parse, urllib.request
from playwright.sync_api import sync_playwright
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parent / "player"))
URL = (HERE.parent / "player" / "explain.html").as_uri()
html = open(urllib.request.url2pathname(urllib.parse.urlparse(URL).path), encoding="utf-8").read()
data = json.loads(html.split("const DATA = ")[1].split(";\nconst $")[0])
res, errs = [], []
def ok(n, c, x=""): res.append(("✅" if c else "❌") + " " + n + ("" if c else " " + str(x)[:300]))
WANT = {"science": "garden", "math": "classroom", "physics": "space", "chemistry": "lab", "geography": "map", "history": "desert", "language": "notebook", "general": "room"}
PROPS = "(()=>{const vb=document.getElementById('xs').viewBox.baseVal;return [...document.querySelectorAll('#xs .pl-soft .pl-prop, #xs .pl-soft .pl-x')].map(g=>{const m=/translate\\(([-\\d.]+) ([-\\d.]+)/.exec(g.getAttribute('transform'));return {t:g.dataset.pl,x:+m[1]/vb.width,y:+m[2]/vb.height};});})()"


def json_place_page(tmp):
    """The computer book with "place": "kitchen" on the book and "sea" on its first lesson."""
    import explain_main, build_explain_player as bep, lego
    lego.set_store(os.path.join(tmp, "lego.json"))
    g = json.load(open(HERE.parent / "examples" / "new_subject_computer_g7.json", encoding="utf-8"))
    g["book"]["place"] = "kitchen"
    first = next(n for n in g["nodes"] if n["level"] == "lesson"); first["place"] = "sea"
    gp = os.path.join(tmp, "cs_place.json"); json.dump(g, open(gp, "w", encoding="utf-8"), ensure_ascii=False)
    od = os.path.join(tmp, "out_cs"); explain_main.run(gp, od)
    packed = bep.pack(gp, od)
    out = os.path.join(tmp, "cs_place.html"); open(out, "w", encoding="utf-8").write(bep.page_html([packed]))
    return pathlib.Path(out).as_uri(), packed, first["id"]


def page(b, url, **kw):
    ctx = b.new_context(viewport=kw.pop("viewport", {"width": 1150, "height": 1000}), **kw); pg = ctx.new_page(); pg.route("**/fonts.*/**", lambda r: r.abort())
    pg.on("pageerror", lambda e: errs.append(str(e)[:160])); return ctx, pg


def big_picture(pg, gi, li=0):
    pg.evaluate(f"window.stCtl&&window.stCtl.pause();document.querySelector('#side .les[data-g=\"{gi}\"][data-l=\"{li}\"]').click()"); pg.wait_for_timeout(250)
    pg.evaluate("window.stCtl&&window.stCtl.pause();document.querySelector('#prog .pstop[data-c=\"-1\"]').click()"); pg.wait_for_timeout(250)
    pg.evaluate("document.getElementById('play').textContent.includes('وقّف')&&document.getElementById('play').click()"); pg.wait_for_timeout(500)


with sync_playwright() as p:
    b = p.chromium.launch()
    # ---------- (1) places by subject, behind the cartoon and behind every other scene ----------
    ctx, pg = page(b, URL); pg.goto(URL + "?q=hi"); pg.wait_for_timeout(600)
    wrong, soft_mid = [], []
    for gi, g in enumerate(data["graphs"]):
        want = g["lessons"][0].get("place") or g.get("place") or WANT.get(g["subject"], "room")   # 🆕 batch 39: the lesson's own place first (cells → lab)
        pg.evaluate(f"window.stCtl&&window.stCtl.pause();document.querySelector('#side .les[data-g=\"{gi}\"][data-l=\"0\"]').click()"); pg.wait_for_timeout(250)
        full = pg.evaluate("(()=>{const s=document.querySelector('.st-screen');return [s&&s.dataset.place,!!document.querySelector('#xs .pl.pl-full')];})()")
        big_picture(pg, gi)
        soft = pg.evaluate("(document.querySelector('#xs .pl.pl-soft')||{dataset:{}}).dataset.place||null")
        cast = g["audience"]["stage"] in ("kids", "junior")   # 🆕 batch 38: the teen story is a board, the secondary story a diagram (not the place)
        if (cast and (full[0] != want or not full[1])) or (not cast and full[0] not in ("board", "doc")) or soft != want:
            wrong.append((g["title"], want, full, soft))
        soft_mid += [(g["title"], q) for q in pg.evaluate(PROPS) if q["y"] > 0.6 and 0.15 < q["x"] < 0.85 and q["t"] not in ("waves", "car")]
    ok("every lesson has its place (its own words, else its subject's): in the cartoon (full, the little ones and the explorers) and behind the scenes (soft)", not wrong, wrong[:3])
    ok("behind a scene the place keeps to the edges (the middle belongs to the characters)", not soft_mid, soft_mid[:4])
    gs = next(i for i, g in enumerate(data["graphs"]) if g["subject"] == "science" and g["audience"]["stage"] == "kids")
    pg.evaluate(f"window.stCtl&&window.stCtl.pause();document.querySelector('#side .les[data-g=\"{gs}\"][data-l=\"0\"]').click()"); pg.wait_for_timeout(300)
    first = pg.evaluate("(()=>{const c=window.stCtl;c.pause();for(let t=0;t<6;t+=0.3){c.seek(t);const s=document.getElementById('stSub').textContent.trim();if(s)return s;}return '';})()")
    ok("the story happens in the place («كان يا ما كان، بحديقة خضرا…»)", "حديقة" in first, first)
    # ---------- (2) the place lives: a tap, the extras ----------
    big_picture(pg, gs)
    n0 = pg.evaluate("window.__SOUND.log.length")
    pg.evaluate("(()=>{const t=document.querySelector('#xs .pl [data-pl]:not([data-x])');t.dispatchEvent(new PointerEvent('pointerdown',{bubbles:true}));})()"); pg.wait_for_timeout(120)
    ok("tapping a prop makes it wiggle, with its sound", pg.locator("#xs .pl .pl-a.pl-poke").count() == 1 and pg.evaluate("window.__SOUND.log.length") > n0)
    pg.evaluate("(()=>{const t=document.querySelector('#xs .pl .pl-x');t.dispatchEvent(new PointerEvent('pointerdown',{bubbles:true}));})()"); pg.wait_for_timeout(150)
    say = pg.evaluate("(document.querySelector('#xs .pl-say text')||{}).textContent||''")
    names = set(data["graphs"][gs]["names"].values())
    ok("tapping an extra: it hops and says a little word (never a concept of the lesson)", say and not any(n in say for n in names), say)
    ok("the props move (a tree sways)", pg.evaluate("getComputedStyle(document.querySelector('#xs .pl .pl-sway')).animationName") == "plSway")
    ok("🙌 the characters have little arms (kids)", pg.locator("#xs .xnode .ch-arms").count() >= pg.locator("#xs .xnode").count() - 1 and pg.locator("#xs .xnode").count() > 0,
       (pg.locator("#xs .xnode .ch-arms").count(), pg.locator("#xs .xnode").count()))
    sen = next(i for i, g in enumerate(data["graphs"]) if g["audience"]["stage"] == "senior")
    big_picture(pg, sen)
    ok("the older stages: no arms (serious)", pg.locator("#xs .ch-arms").count() == 0)
    ctx.close()
    # the extras chat by themselves (the little ones), not the older ones (fake clock)
    for st_gi, label, want_chat in ((gs, "kids", True), (sen, "senior", False)):
        ctx, pg = page(b, URL); pg.clock.install(); pg.goto(URL + "?q=hi"); pg.clock.run_for(800)
        pg.evaluate(f"window.stCtl&&window.stCtl.pause();document.querySelector('#side .les[data-g=\"{st_gi}\"][data-l=\"0\"]').click()"); pg.clock.run_for(300)
        pg.evaluate("window.stCtl&&window.stCtl.pause();document.querySelector('#prog .pstop[data-c=\"-1\"]').click()"); pg.clock.run_for(300)
        pg.evaluate("document.getElementById('play').textContent.includes('وقّف')&&document.getElementById('play').click()")
        chatted = False
        for _ in range(30):
            pg.clock.run_for(1000)
            if pg.locator("#xs .pl-say").count():
                chatted = True; break
        ok(f"{label}: the background extras {'chat now and then' if want_chat else 'stay quiet'}", chatted == want_chat)
        ctx.close()
    # light quality: still
    ctx, pg = page(b, URL); pg.goto(URL + "?q=lo"); pg.wait_for_timeout(600); big_picture(pg, gs)
    ok("the light quality: the place stands still", pg.evaluate("getComputedStyle(document.querySelector('#xs .pl .pl-sway')).animationName") == "none")
    ctx.close()
    # ---------- (1b) the JSON chooses the place ----------
    with tempfile.TemporaryDirectory() as tmp:
        url, packed, lid = json_place_page(tmp)
        ctx, pg = page(b, url); pg.goto(url + "?q=hi"); pg.wait_for_timeout(600)
        got = []
        for li, l in enumerate(packed["lessons"]):
            big_picture(pg, 0, li)
            got.append((l["lesson_id"], pg.evaluate("(document.querySelector('#xs .pl')||{dataset:{}}).dataset.place||null")))
        want = [(l["lesson_id"], "sea" if l["lesson_id"] == lid else "kitchen") for l in packed["lessons"]]
        ok("the JSON's place wins: \"sea\" on one lesson, \"kitchen\" on the book for the others", got == want, (got, want))
        ctx.close()
    # ---------- (4) the fact budget, as the student sees it ----------
    too_long = [(g["title"], c["concept_id"], len(c["scenes"])) for g in data["graphs"] for l in g["lessons"] for c in l["concepts"]
                if len([s for s in c["scenes"] if s["kind"] not in ("play", "slider")]) > 4]
    ok("every concept: the cartoon + at most 3 more (+ a film / slider)", not too_long, too_long[:3])
    ok("every concept opens with its cartoon", all(c["scenes"][0]["kind"] == "meet" for g in data["graphs"] for l in g["lessons"] for c in l["concepts"]))
    # ---------- the phone ----------
    ctx, pg = page(b, URL, viewport={"width": 390, "height": 844}, has_touch=True, is_mobile=True); pg.goto(URL + "?q=hi"); pg.wait_for_timeout(600)
    big_picture(pg, gs)
    ok("📱 the place fits the phone (no sideways scroll)", pg.evaluate("document.documentElement.scrollWidth") <= 390 and pg.locator("#xs .pl").count() == 1)
    ctx.close()
    b.close()
print("\n".join(r for r in res if r.startswith("❌")) or "")
print(f"✅ {sum(r.startswith('✅') for r in res)} checks passed · ❌ {sum(r.startswith('❌') for r in res)} failed")
print("JS errors:", errs or "none")
