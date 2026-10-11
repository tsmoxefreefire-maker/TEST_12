"""🆕 batch 34 (Hareth's notes) in a real browser:
(1) ALIVE ARROWS: they sway up and down (their ends stay on the characters), the word pill follows, pointing at one lights it up
    and says what it means; still with the light quality and «reduce motion»;
(2) GRAPHICS: a shadow under each character + a «sticker» shine for the younger stages, a quiet shadow for the older ones, names with a halo;
(3) the lesson's STORY is a real story: its chapters follow the age (a tale … an investigation), the hero is the one that needs the most,
    the journey walks back along the chain, and it ends with its lesson (العبرة);
(4) the FIVE GAMES (🪃 throw · 🏗️ tower · 🧲 magnet · ⚙️ machine · ⚡ power): every one of them opens with no error in every book,
    and each one is played for real: right → the reason, wrong → why, the end → the win; 🆕 batch 41: the video never plays it for him;
(5) the phone: no sideways scroll in the games.
python tests_browser/test_batch34.py"""
import json, pathlib, urllib.parse, urllib.request
from playwright.sync_api import sync_playwright
HERE = pathlib.Path(__file__).resolve().parent
URL = (HERE.parent / "player" / "explain.html").as_uri()
html = open(urllib.request.url2pathname(urllib.parse.urlparse(URL).path), encoding="utf-8").read()
data = json.loads(html.split("const DATA = ")[1].split(";\nconst $")[0])
res, errs = [], []
def ok(n, c, x=""): res.append(("✅" if c else "❌") + " " + n + ("" if c else " " + str(x)[:300]))
STEPS = lambda s: 1 if s["kind"] == "meet" else len(s["steps"])
GAMES = ("throw", "tower", "magnet", "machine", "power")
ARR = "[...document.querySelectorAll('#xs path.xarrow')].map(p=>p.getAttribute('d'))"


def find(kind, stage=None):
    for gi, g in enumerate(data["graphs"]):
        if stage and g["audience"]["stage"] != stage:
            continue
        for li, l in enumerate(g["lessons"]):
            for ci, c in enumerate(l["concepts"]):
                for si, s in enumerate(c["scenes"]):
                    if s["kind"] == kind:
                        return gi, li, ci, sum(STEPS(x) for x in c["scenes"][:si]), s
    return None


def open_scene(pg, f):
    gi, li, ci, n, s = f
    pg.evaluate(f"document.querySelector('#side .les[data-g=\"{gi}\"][data-l=\"{li}\"]').click()"); pg.wait_for_timeout(200)
    pg.evaluate(f"document.querySelector('#prog .pstop[data-c=\"{ci}\"]').click()"); pg.wait_for_timeout(200)
    for _ in range(n):
        pg.evaluate("document.getElementById('next').click()")
    pg.wait_for_timeout(250)
    pg.evaluate("document.getElementById('play').textContent.includes('وقّف')&&document.getElementById('play').click()")
    pg.wait_for_timeout(400)
    return s


def click(pg, sel):
    return pg.evaluate(f"(()=>{{const e=document.querySelector('{sel}');if(!e)return false;e.dispatchEvent(new MouseEvent('click',{{bubbles:true}}));return true;}})()")


def new_page(b, q="hi", **kw):
    pg = b.new_page(viewport=kw.pop("viewport", {"width": 1150, "height": 1000}), **kw); pg.route("**/fonts.*/**", lambda r: r.abort())
    pg.on("pageerror", lambda e: errs.append(str(e)[:160])); pg.goto(URL + ("?q=" + q if q else "")); pg.wait_for_timeout(600)
    return pg


with sync_playwright() as p:
    b = p.chromium.launch()
    # ---------- (1) alive arrows ----------
    pg = new_page(b)
    pg.evaluate("document.querySelector('#prog .pstop[data-c=\"-1\"]').click()"); pg.wait_for_timeout(300)
    pg.evaluate("document.getElementById('play').textContent.includes('وقّف')&&document.getElementById('play').click()"); pg.wait_for_timeout(900)
    d1 = pg.evaluate(ARR); pg.wait_for_timeout(700); d2 = pg.evaluate(ARR)
    ends = lambda d: (d.split(" Q")[0], d.split(" ")[-2:])
    ok("arrows sway: their middle moves with time", d1 != d2 and len(d1) > 0, (d1[:1], d2[:1]))
    ok("…but their two ends stay on the characters", all(ends(a) == ends(c) for a, c in zip(d1, d2)), (d1[:1], d2[:1]))
    ok("every arrow has a fat see-through twin to point at", pg.locator("#xs .arw-hit").count() == pg.locator("#xs .xarrow").count())
    mid = pg.evaluate("(()=>{const p=document.querySelector('#xs .xarrow');const m=p.getPointAtLength(p.getTotalLength()*0.3);const pt=p.ownerSVGElement.createSVGPoint();pt.x=m.x;pt.y=m.y;const s=pt.matrixTransform(p.getScreenCTM());return [s.x,s.y];})()")
    pg.mouse.move(mid[0], mid[1]); pg.wait_for_timeout(300)
    tip = pg.evaluate("(document.querySelector('#xs .arw-tip')||{}).textContent||''")
    e0 = pg.evaluate("(()=>{const e=document.querySelector('#xs .xedge');return [e.dataset.a,e.dataset.b];})()")
    names = data["graphs"][0]["names"]
    ok("pointing at an arrow lights it up", pg.locator("#xs .xedge.arw-hot").count() == 1)
    ok("…and says what it means (B بيحتاج A, from the graph; 🆕 batch 37: no «» marks)", tip == f"{names[e0[1]]} بيحتاج {names[e0[0]]}", (tip, e0))
    pg.mouse.move(5, 5); pg.wait_for_timeout(200)
    ok("…moving away: the sentence goes", pg.locator("#xs .arw-tip").count() == 0)
    pg.close()
    for q, kw, label in (("lo", {}, "the light quality"), ("hi", {"reduced_motion": "reduce"}, "«reduce motion»")):
        ctx = b.new_context(viewport={"width": 1150, "height": 1000}, **kw); pg = ctx.new_page(); pg.route("**/fonts.*/**", lambda r: r.abort())
        pg.on("pageerror", lambda e: errs.append(str(e)[:160])); pg.goto(URL + "?q=" + q); pg.wait_for_timeout(600)
        pg.evaluate("document.querySelector('#prog .pstop[data-c=\"-1\"]').click()"); pg.wait_for_timeout(800)
        a1 = pg.evaluate(ARR); pg.wait_for_timeout(700)
        ok(f"arrows stay still with {label}", a1 == pg.evaluate(ARR))
        ctx.close()
    # ---------- (2) graphics ----------
    pg = new_page(b)
    pg.evaluate("document.querySelector('#prog .pstop[data-c=\"-1\"]').click()"); pg.wait_for_timeout(500)
    ok("kids: a soft shadow under every character", pg.locator("#xs .xnode .xshadow").count() == pg.locator("#xs .xnode").count()
       and pg.evaluate("getComputedStyle(document.querySelector('#xs .xshadow')).display") != "none")
    ok("kids: the «sticker» shine on the drawings", "xgloss" in pg.evaluate("getComputedStyle(document.querySelector('#xs .xnode .xbody>svg.ch')).filter"))
    ok("names have a clean halo (readable on arrows)", pg.evaluate("getComputedStyle(document.querySelector('#xs .xname')).paintOrder").startswith("stroke"))
    gs = next(i for i, g in enumerate(data["graphs"]) if g["audience"]["stage"] == "senior")
    pg.evaluate(f"document.querySelector('#side .les[data-g=\"{gs}\"][data-l=\"0\"]').click()"); pg.wait_for_timeout(300)
    pg.evaluate("document.querySelector('#prog .pstop[data-c=\"-1\"]').click()"); pg.wait_for_timeout(500)
    ok("secondary: no ground shadow, a quiet drop shadow instead (no shine)", pg.evaluate("getComputedStyle(document.querySelector('#xs .xshadow')).display") == "none"
       and "xsoft" in pg.evaluate("getComputedStyle(document.querySelector('#xs .xnode .xbody>svg.ch')).filter"))
    ok("the shared drawing tools live once in the page", pg.locator("#b34defs filter#xgloss").count() == 1 and pg.locator("#b34defs filter#xsoft").count() == 1)
    pg.close()
    # ---------- (3) the story is a STORY ----------
    pg = new_page(b, q=None)
    want = {"kids": ["البداية", "المشكلة", "الرحلة", "المفاجأة", "النهاية السعيدة"], "junior": ["البداية", "المهمة", "المغامرة", "المفاجأة", "النهاية"],
            "teen": ["القضية", "الأدلة", "الاختبار", "الحل"], "senior": ["السؤال", "التتبّع", "الفرضية", "الاستنتاج"]}   # 🆕 batch 38: the board (an investigation) · the diagram (tracing back)
    SUBS = """()=>{const c=window.stCtl;c.pause();const out=[];let last='';for(let t=0;t<=c.DUR;t+=0.3){c.seek(t);const s=(document.getElementById('stSub')||{}).textContent||'';if(s.trim()&&s.trim()!==last){last=s.trim();out.push(last);}}return out;}"""
    for st, names_ch in want.items():
        gi = next(i for i, g in enumerate(data["graphs"]) if g["audience"]["stage"] == st and any(c for l in g["lessons"] for c in l["concepts"]))
        pg.evaluate(f"document.querySelector('#side .les[data-g=\"{gi}\"][data-l=\"0\"]').click()"); pg.wait_for_timeout(300)
        chap = [c[1] for c in json.loads(pg.evaluate("document.querySelector('.st-screen').dataset.chap"))]
        ok(f"{st}: the story is told its age's way {chap}", all(c in names_ch for c in chap) and chap[0] == names_ch[0] and chap[-1] == names_ch[-1], chap)
    pg.evaluate("document.querySelector('#side .les[data-g=\"0\"][data-l=\"0\"]').click()"); pg.wait_for_timeout(300)
    subs = pg.evaluate(SUBS)
    ok("kids: «كان يا ما كان…» → a problem → the journey → the twist → «العبرة»", subs[0].startswith("📖 كان يا ما كان") and any("بيوم من الأيام" in x for x in subs)
       and any("فجأة" in x for x in subs) and subs[-1].startswith("💡 العبرة"), subs)
    chap0 = json.loads(pg.evaluate("document.querySelector('.st-screen').dataset.chap"))
    pg.evaluate(f"window.stCtl.seek({chap0[1][0] + 0.15})")                      # everyone standing still (no walk, no jump)
    hero = pg.evaluate("(()=>{let best=null,sc=0;document.querySelectorAll('#xs .sa').forEach(g=>{const m=/scale\\(([\\d.]+)/.exec(g.querySelector('.sa-b').getAttribute('transform')||'');const s=m?+m[1]:1;if(s>sc){sc=s;best=g.dataset.id;}});return best;})()")
    first_go = next((x for x in subs if "بيوم من الأيام" in x), "")
    ok("the hero (the biggest) starts the journey (🆕 batch 38: it is the one that misses something first)", hero and data["graphs"][0]["names"][hero] in first_go, (hero, first_go))
    pg.close()
    # ---------- (4) the five games: open every one of them in every book ----------
    pg = new_page(b, q=None)
    opened, broken = 0, []
    for gi, g in enumerate(data["graphs"]):
        for li, l in enumerate(g["lessons"]):
            for ci, c in enumerate(l["concepts"]):
                for si, s in enumerate(c["scenes"]):
                    if s["kind"] in GAMES:
                        open_scene(pg, (gi, li, ci, sum(STEPS(x) for x in c["scenes"][:si]), s)); opened += 1
                        cls = pg.evaluate("document.getElementById('xs').getAttribute('class')")
                        if f"g4-{s['kind']}" not in cls:
                            broken.append((g["title"], s["kind"], cls))
    ok(f"every game opens in every book ({opened})", opened >= 50 and not broken, broken[:3])
    pg.close()
    pg = new_page(b)
    cap = lambda: pg.inner_text("#cap")
    # 🪃 throw: a tap = a perfect throw; a real fling aimed at X gets there; a fling the other way falls back
    s = open_scene(pg, find("throw", "kids")); need = sum(x["ok"] for x in s["balls"])
    wrong = next(i for i, x in enumerate(s["balls"]) if not x["ok"]); right = [i for i, x in enumerate(s["balls"]) if x["ok"]]
    def ball(i):
        el = pg.locator(f'#xs .g4-ball[data-i="{i}"]'); el.scroll_into_view_if_needed(); bx = el.bounding_box(); return bx["x"] + bx["width"] / 2, bx["y"] + bx["height"] / 3
    x0, y0 = ball(right[0]); X = pg.locator("#xs .g4-x").bounding_box(); tx, ty = X["x"] + X["width"] / 2, X["y"] + X["height"] / 2
    pg.mouse.move(x0, y0); pg.mouse.down(); pg.mouse.move(x0 - (tx - x0) * 0.04, y0 - (ty - y0) * 0.04, steps=2); pg.mouse.move(x0 + (tx - x0) * 0.35, y0 + (ty - y0) * 0.35, steps=4); pg.mouse.up(); pg.wait_for_timeout(1500)
    ok("🪃 a real fling aimed at «X» flies there and is caught (+ the reason)", pg.locator("#xs .g4-ball.g4-in").count() == 1 and cap().startswith("✅"), cap())
    x1, y1 = ball(right[1]) if len(right) > 1 else ball(wrong)
    pg.mouse.move(x1, y1); pg.mouse.down(); pg.mouse.move(x1 - 40, y1 + 30, steps=3); pg.mouse.move(x1 - 140, y1 + 90, steps=3); pg.mouse.up(); pg.wait_for_timeout(1700)
    ok("🪃 a fling the other way falls and comes back («صوّب»)", "صوّب" in cap(), cap())
    x2, y2 = ball(wrong); pg.mouse.move(x2, y2); pg.mouse.down(); pg.mouse.up(); pg.wait_for_timeout(1600)
    ok("🪃 a wrong ball is bounced back with why («ما بتحتاج… فرجعت»)", pg.locator(f'#xs .g4-ball.g4-no[data-i="{wrong}"]').count() == 1 and "↩️" in cap(), cap())
    for i in right[1:]:
        xi, yi = ball(i); pg.mouse.move(xi, yi); pg.mouse.down(); pg.mouse.up(); pg.wait_for_timeout(1600)
    ok("🪃 all the right ones caught → the win, an arrow for each", s["win"].replace("«", "").replace("»", "")[:12] in cap() and pg.locator("#xs .g4-arr").count() == need, (cap(), pg.locator("#xs .g4-arr").count()))
    # 🏗️ tower
    s = open_scene(pg, find("tower", "kids")); n = len(s["blocks"])
    click(pg, f'#xs .g4-brick[data-i="{n - 1}"]'); pg.wait_for_timeout(1800)
    ok("🏗️ the top block first: it wobbles, falls back, and says why", "🙃" in cap() and pg.locator("#xs .g4-brick.g4-set").count() == 0, cap())
    for k in range(n):
        click(pg, f'#xs .g4-brick[data-i="{k}"]'); pg.wait_for_timeout(1000)
    ok("🏗️ the right order builds the tower → the win", pg.locator("#xs .g4-brick.g4-set").count() == n and s["win"].replace("«", "").replace("»", "")[:10] in cap(), cap())
    # 🧲 magnet: one that does not need it stays; drag the magnet near one who needs it → pulled in
    s = open_scene(pg, find("magnet", "kids")); i_ok = next(i for i, x in enumerate(s["items"]) if x["ok"]); i_no = next(i for i, x in enumerate(s["items"]) if not x["ok"])
    click(pg, f'#xs .g4-it[data-i="{i_no}"]'); pg.wait_for_timeout(1300)
    ok("🧲 one that does not need it stays (😐 + why)", pg.locator(f'#xs .g4-it.g4-no[data-i="{i_no}"]').count() == 1 and "😐" in cap(), cap())
    m = pg.locator("#xs #g4Mag").bounding_box(); it = pg.locator(f'#xs .g4-it[data-i="{i_ok}"]').bounding_box()
    pg.mouse.move(m["x"] + m["width"] / 2, m["y"] + m["height"] / 2); pg.mouse.down(); pg.mouse.move(it["x"] + it["width"] / 2, it["y"] + it["height"] / 2, steps=10); pg.mouse.up(); pg.wait_for_timeout(1200)
    ok("🧲 dragging the magnet near one that needs it → it is pulled in and sticks (+ the reason)", pg.locator(f'#xs .g4-it.g4-in[data-i="{i_ok}"]').count() == 1, cap())
    for i, x in enumerate(s["items"]):
        if x["ok"] and i != i_ok:
            click(pg, f'#xs .g4-it[data-i="{i}"]'); pg.wait_for_timeout(1500)
    pg.wait_for_timeout(400)
    ok("🧲 all pulled in → the win", pg.locator("#xs .g4-it.g4-in").count() == sum(x["ok"] for x in s["items"]) and s["win"].replace("«", "").replace("»", "")[:10] in cap(), cap())
    # ⚙️ machine
    s = open_scene(pg, find("machine", "kids")); bad = next(i for i, o in enumerate(s["options"]) if not o["ok"]); good = next(i for i, o in enumerate(s["options"]) if o["ok"])
    click(pg, f'#xs .g4-opt[data-i="{bad}"]'); pg.wait_for_timeout(1300)
    ok("⚙️ a wrong gear clunks out (🔩 + why), the machine stays stuck", "🔩" in cap() and "g4-run" not in pg.evaluate("document.getElementById('xs').getAttribute('class')"), cap())
    tr0 = pg.evaluate("[...document.querySelectorAll('#xs .g4-teeth')].map(g=>g.getAttribute('transform'))")
    click(pg, f'#xs .g4-opt[data-i="{good}"]'); pg.wait_for_timeout(1200)
    tr1 = pg.evaluate("[...document.querySelectorAll('#xs .g4-teeth')].map(g=>g.getAttribute('transform'))")
    ok("⚙️ the right gear fits: every gear turns (+ both links said)", "g4-run" in pg.evaluate("document.getElementById('xs').getAttribute('class')") and tr0 != tr1 and cap().startswith("⚙️"), cap())
    pg.wait_for_timeout(1800)
    ok("⚙️ …then the win", s["win"].replace("«", "").replace("»", "")[:10] in cap(), cap())
    # ⚡ power
    s = open_scene(pg, find("power", "kids"))
    if s["decoy"]:
        pg.evaluate(f"document.querySelector('.g4-sw[data-id=\"{s['decoy']}\"]').click()"); pg.wait_for_timeout(700)
        ok("⚡ the decoy switch lights only itself, and says it helps nobody", "🔌" in cap() and pg.locator(f'#xs .g4-bulb.g4-lit[data-id="{s["target"]}"]').count() == 0, cap())
    real = [x for x in s["sources"] if x != s["decoy"]]
    for x in real[:-1]:
        pg.evaluate(f"document.querySelector('.g4-sw[data-id=\"{x}\"]').click()"); pg.wait_for_timeout(500)
    ok("⚡ not all the sources yet → «X» stays dark", pg.locator(f'#xs .g4-bulb.g4-lit[data-id="{s["target"]}"]').count() == 0 or len(real) == 1)
    pg.evaluate(f"document.querySelector('.g4-sw[data-id=\"{real[-1]}\"]').click()"); pg.wait_for_timeout(600)
    ok("⚡ all of them → the light runs through the wires and «X» lights up (+ why)", pg.locator(f'#xs .g4-bulb.g4-lit[data-id="{s["target"]}"]').count() == 1
       and pg.locator("#xs .g4-wire.g4-live").count() >= 1 and "💡" in cap(), cap())
    pg.wait_for_timeout(2000)
    ok("⚡ …then the win", s["win"].replace("«", "").replace("»", "")[:8] in cap(), cap())
    pg.close()
    # ---------- 🆕 batch 41 (Hareth: «الفعاليات… الطالب هو اللي بيلعب فيها مو أوتوماتيك»): the video NEVER builds it for him (fake clock) ----------
    ctx = b.new_context(viewport={"width": 1150, "height": 1000}); pg = ctx.new_page(); pg.route("**/fonts.*/**", lambda r: r.abort()); pg.on("pageerror", lambda e: errs.append(str(e)[:160]))
    pg.clock.install(); pg.goto(URL); pg.clock.run_for(600)
    gi, li, ci, n, s = find("tower", "kids")
    pg.evaluate(f"document.querySelector('#side .les[data-g=\"{gi}\"][data-l=\"{li}\"]').click()"); pg.clock.run_for(200)
    pg.evaluate(f"document.querySelector('#prog .pstop[data-c=\"{ci}\"]').click()"); pg.clock.run_for(200)
    for _ in range(n):
        pg.evaluate("document.getElementById('next').click()")
    pg.clock.run_for(80000)                                                          # 80 seconds of nobody touching anything
    ok("🎬 the video never builds the tower for him: no ▶ on it, «🖐️ دورك», not one brick set by itself",
       pg.locator("#xs .g4-brick.g4-set").count() == 0 and not pg.locator("#play").is_visible() and pg.locator("#turn").count() == 1, pg.locator("#xs .g4-brick.g4-set").count())
    ctx.close()
    # ---------- (5) the phone ----------
    ctx = b.new_context(viewport={"width": 390, "height": 844}, has_touch=True, is_mobile=True); pg = ctx.new_page(); pg.route("**/fonts.*/**", lambda r: r.abort()); pg.on("pageerror", lambda e: errs.append(str(e)[:160]))
    pg.goto(URL); pg.wait_for_timeout(600)
    wide = []
    for k in GAMES:
        f = find(k)
        open_scene(pg, f)
        if pg.evaluate("document.documentElement.scrollWidth") > 390:
            wide.append(k)
    ok("📱 every game fits the phone (no sideways scroll)", not wide, wide)
    s = open_scene(pg, find("throw")); el = pg.locator('#xs .g4-ball[data-i="0"]'); el.scroll_into_view_if_needed(); el.tap(); pg.wait_for_timeout(1600)
    ok("📱 a tap throws the ball", pg.locator('#xs .g4-ball.g4-in, #xs .g4-ball.g4-no').count() == 1, pg.inner_text("#cap"))
    ctx.close()
    b.close()
print("\n".join(r for r in res if r.startswith("❌")) or "")
print(f"✅ {sum(r.startswith('✅') for r in res)} checks passed · ❌ {sum(r.startswith('❌') for r in res)} failed")
print("JS errors:", errs or "none")
