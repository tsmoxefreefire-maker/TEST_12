"""🆕 batch 32 (Hareth: «المشهد كأنه فيديو: SVG animation، الشخصيات بتتحرك وبتتفاعل مع بعض») in a real browser:
(1) EVERY lesson of the 12 books starts with its story (🎬 an SVG cartoon) and draws with no error;
(2) it plays by itself like a video: the time runs, the characters WALK (their place changes), a glowing ball is GIVEN, the arrow is drawn;
(3) the truth: every arrow in the story is a real «needs» of the graph (the overview's arrows or a «meet» prerequisite);
(4) the video controls: ⏸ stops the time · dragging the timeline jumps to the right chapter + subtitle;
(5) «what if…?»: the one everybody needs walks out (gone) and the ones who need it turn grey; it comes back;
(6) at the end the video goes on to the next scene by itself (batch 31); «reduce motion» = no autoplay, a big ▶;
(7) the age words (the secondary says «بيعتمد على»), the phone (no sideways scroll), a backdrop per subject.
python tests_browser/test_batch32.py"""
import json, pathlib, urllib.parse, urllib.request
from playwright.sync_api import sync_playwright
HERE = pathlib.Path(__file__).resolve().parent
URL = (HERE.parent / "player" / "explain.html").as_uri()
html = open(urllib.request.url2pathname(urllib.parse.urlparse(URL).path), encoding="utf-8").read()
data = json.loads(html.split("const DATA = ")[1].split(";\nconst $")[0])
res, errs = [], []
def ok(n, c, x=""): res.append(("✅" if c else "❌") + " " + n + ("" if c else " " + str(x)[:300]))
SCENE = "(document.getElementById('xs')||{getAttribute:()=>null}).getAttribute('aria-label')"
JOURNEY = ("الرحلة", "المغامرة", "الأدلة")          # batch 34: the story is TOLD by age — the journey chapter (where they give)
TWIST = ("المفاجأة", "الاختبار", "الفرضية")         # …and the twist chapter («what if…?»)
SEEK = "t=>{const s=document.getElementById('stSeek');s.value=String(Math.round(t*10));s.dispatchEvent(new Event('input'));s.dispatchEvent(new Event('change'));}"


def real_needs(lesson):
    """Every real «b needs a» of the lesson: the overview's arrows + every meet scene's prerequisites."""
    out = {tuple(e) for e in (lesson.get("overview") or {}).get("edges", [])}
    for c in lesson["concepts"]:
        for sc in c["scenes"]:
            if sc["kind"] == "meet":
                out |= {(a, c["concept_id"]) for a in sc.get("ins", [])}
    return out


with sync_playwright() as p:
    b = p.chromium.launch()
    # ---------- (1) + (3) every lesson ----------
    pg = b.new_page(viewport={"width": 1250, "height": 950}); pg.route("**/fonts.*/**", lambda r: r.abort()); pg.on("pageerror", lambda e: errs.append(str(e)[:160]))
    pg.goto(URL); pg.wait_for_timeout(500)
    bad_first, bad_truth, n_les, n_links, short = [], [], 0, 0, []
    for gi, g in enumerate(data["graphs"]):
        for li, l in enumerate(g["lessons"]):
            pg.click(f'#side .les[data-g="{gi}"][data-l="{li}"]', force=True); pg.wait_for_timeout(120); n_les += 1
            if pg.evaluate(SCENE) != "حكاية الدرس":
                bad_first.append((g["title"], l["lesson_title"]))
                continue
            links = pg.evaluate("[...document.querySelectorAll('#xs .st-link')].map(p=>[p.dataset.a,p.dataset.b])")
            n_links += len(links)
            real = real_needs(l)
            bad_truth += [(l["lesson_title"], a, bb) for a, bb in links if (a, bb) not in real]
            actors = pg.evaluate("document.querySelectorAll('#xs .sa').length")
            if actors < len(l["concepts"]) or float(pg.evaluate("document.querySelector('.st-screen').dataset.dur")) < 15:
                short.append((l["lesson_title"], actors))
    ok(f"every lesson ({n_les}) starts with its story 🎬", not bad_first, bad_first[:4])
    ok(f"every arrow in the stories ({n_links}) is a real «needs» of the graph", n_links > 30 and not bad_truth, bad_truth[:4])
    ok("every story has all its characters and a real length", not short, short[:4])
    pg.close()
    # ---------- (2) + (4) + (5) + (6) the plants lesson, with a fake clock ----------
    ctx = b.new_context(viewport={"width": 1250, "height": 950}); pg = ctx.new_page(); pg.route("**/fonts.*/**", lambda r: r.abort()); pg.on("pageerror", lambda e: errs.append(str(e)[:160]))
    pg.clock.install(); pg.goto(URL); pg.clock.run_for(400)
    t0 = pg.inner_text("#stTime"); pos0 = pg.evaluate("[...document.querySelectorAll('#xs .sa')].map(g=>g.getAttribute('transform'))")
    pg.clock.run_for(6000)
    ok("it plays by itself: the time runs", pg.inner_text("#stTime") != t0, (t0, pg.inner_text("#stTime")))
    pos1 = pg.evaluate("[...document.querySelectorAll('#xs .sa')].map(g=>g.getAttribute('transform'))")
    ok("🆕 batch 38: the hero walks in ALONE first (the others wait outside until someone needs them)", sum(a != c for a, c in zip(pos0, pos1)) == 1, (pos0[:3], pos1[:3]))
    chap = json.loads(pg.evaluate("document.querySelector('.st-screen').dataset.chap"))
    give = next(t for t, name in chap if name in JOURNEY)
    seen_orb = seen_link = False
    for _ in range(int((give + 6) * 4)):                 # play on (by the clock) until a little after the first «give» chapter
        pg.clock.run_for(250)
        if pg.evaluate("[...document.querySelectorAll('#xs .st-orb')].some(o=>o.getAttribute('opacity')==='1')"):
            seen_orb = True
        if pg.evaluate("[...document.querySelectorAll('#xs .st-link')].some(p=>p.getAttribute('marker-end')&&+p.getAttribute('stroke-dashoffset')<0.05)"):
            seen_link = True
        if seen_orb and seen_link:
            break
    pos2 = pg.evaluate("[...document.querySelectorAll('#xs .sa')].map(g=>g.getAttribute('transform'))")
    ok("…then the others come in, one by one", sum(a != c for a, c in zip(pos0, pos2)) >= 2, pos2[:3])
    ok("a glowing ball is GIVEN from one character to the other", seen_orb)
    ok("…and then the arrow between them is drawn (with its head)", seen_link)
    sub = pg.inner_text("#stSub")
    ok("the subtitles show the names (🆕 batch 37: in yellow bold, without «» marks)", "«" not in sub and pg.evaluate("document.querySelectorAll('#stSub b').length") >= 1, sub)
    pg.click("#stPP"); here = pg.inner_text("#stTime"); pg.clock.run_for(5000)
    ok("⏸ stops the time", pg.inner_text("#stTime") == here, (here, pg.inner_text("#stTime")))
    wi = next((t for t, name in chap if name in TWIST), None)
    if wi is not None:
        gone = grey = 0                                   # 🆕 batch 39: the thief takes it first, so we look along the twist (not one moment)
        for k in range(1, 48):
            pg.evaluate(SEEK, wi + 0.5 * k); pg.clock.run_for(60)
            if k > 2 and pg.inner_text("#stChap") not in TWIST: break
            gone = pg.evaluate("[...document.querySelectorAll('#xs .sa')].filter(g=>g.style.opacity==='0').length")
            grey = pg.evaluate("document.querySelectorAll('#xs .sa.st-gray').length")
            if gone == 1 and grey >= 1: break
        pg.evaluate(SEEK, wi + 1.0); pg.clock.run_for(60)
        ok("«what if…?»: the one everybody needs is gone and the ones who need it turn grey", gone == 1 and grey >= 1, (gone, grey))
        ok("…the chapter name follows the timeline", pg.inner_text("#stChap") in TWIST, pg.inner_text("#stChap"))
    dur = float(pg.evaluate("document.querySelector('.st-screen').dataset.dur"))
    pg.evaluate(SEEK, 2.0); pg.clock.run_for(100)
    ok("dragging the timeline back jumps to the start chapter", pg.inner_text("#stChap") in ("البداية", "المهمة", "السؤال"), pg.inner_text("#stChap"))
    pg.click("#stPP"); pg.clock.run_for(int((dur + 2) * 1000))
    for _ in range(40):
        if pg.evaluate("!!document.getElementById('goNext')") or pg.evaluate(SCENE) != "حكاية الدرس":
            break
        pg.clock.run_for(500)
    ok("at the end the video goes on by itself (the countdown / the next scene)", pg.evaluate("!!document.getElementById('goNext')") or pg.evaluate(SCENE) != "حكاية الدرس", pg.evaluate(SCENE))
    ctx.close()
    # ---------- reduce motion: no autoplay, a big ▶ ----------
    ctx = b.new_context(viewport={"width": 1250, "height": 950}, reduced_motion="reduce"); pg = ctx.new_page(); pg.route("**/fonts.*/**", lambda r: r.abort()); pg.on("pageerror", lambda e: errs.append(str(e)[:160]))
    pg.clock.install(); pg.goto(URL); pg.clock.run_for(3000)
    ok("«reduce motion» → it waits, with a big ▶", pg.inner_text("#stTime").startswith("0:00") and pg.is_visible("#stBig"), pg.inner_text("#stTime"))
    pg.click("#stBig"); pg.clock.run_for(3000)
    ok("…▶ plays it", not pg.inner_text("#stTime").startswith("0:00"), pg.inner_text("#stTime"))
    ctx.close()
    # ---------- (7) age words · phone · backdrops ----------
    pg = b.new_page(viewport={"width": 1250, "height": 950}); pg.route("**/fonts.*/**", lambda r: r.abort()); pg.on("pageerror", lambda e: errs.append(str(e)[:160]))
    pg.goto(URL); pg.wait_for_timeout(400)
    gs = next(i for i, g in enumerate(data["graphs"]) if g["audience"]["stage"] == "senior")
    pg.click(f'#side .les[data-g="{gs}"][data-l="0"]', force=True); pg.wait_for_timeout(300); pg.click("#stPP")
    subs = pg.evaluate("""()=>{const c=window.stCtl;c.pause();const out=new Set();for(let t=0;t<=c.DUR;t+=0.4){c.seek(t);const x=(document.getElementById('stSub')||{}).textContent||'';if(x.trim())out.add(x.trim());}return [...out];}""")
    ok("the secondary's story says «بيعتمد على» (its age words), never «بيحتاج»", any(("بيعتمد" in x or "بتعتمد" in x) for x in subs) and not any(("بيحتاج" in x or "بتحتاج" in x) for x in subs), subs[:6])
    themes = set()
    for gi in range(len(data["graphs"])):
        pg.click(f'#side .les[data-g="{gi}"][data-l="0"]', force=True); pg.wait_for_timeout(100)
        themes.add(pg.evaluate("document.querySelector('.st-screen').dataset.theme"))
    ok(f"a backdrop for every subject ({len(themes)}: {sorted(themes)})", len(themes) >= 7, themes)
    pg.close()
    ctx = b.new_context(viewport={"width": 390, "height": 844}, has_touch=True, is_mobile=True); pg = ctx.new_page(); pg.route("**/fonts.*/**", lambda r: r.abort()); pg.on("pageerror", lambda e: errs.append(str(e)[:160]))
    pg.goto(URL); pg.wait_for_timeout(1500)
    ok("📱 the story on the phone: no sideways scroll", pg.evaluate("document.documentElement.scrollWidth") <= 390, pg.evaluate("document.documentElement.scrollWidth"))
    box = pg.locator(".st-screen").bounding_box(); sb = pg.locator("#stSub").bounding_box()
    ok("📱 the subtitles stay inside the picture", sb is None or (sb["x"] >= box["x"] - 1 and sb["x"] + sb["width"] <= box["x"] + box["width"] + 1), (box, sb))
    ctx.close()
    b.close()
print("\n".join(r for r in res if r.startswith("❌")) or "")
print(f"✅ {sum(r.startswith('✅') for r in res)} checks passed · ❌ {sum(r.startswith('❌') for r in res)} failed")
print("JS errors:", errs or "none")
