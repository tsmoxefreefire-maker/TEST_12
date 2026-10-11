"""🆕 batch 39 (Hareth's ideas) in a real browser:
(1) 🐰 THE THIEF of the twist (the little ones and the explorers): a character of the place grabs the one everybody needs, the story STAYS on
    what happens without it (grey, sad, «بدون…»), somebody calls «we need it», the thief brings it back — the idea gets across, not a chase;
(2) 🖐️ THE BOARD AND THE DIAGRAM ANSWER THE STUDENT: when the student plays the story himself it stops and asks (the right one + wrong
    ones from the graph, each wrong one explained), the auto video never stops; a tap on a card / a node tells about it;
(3) 🏞️ A PLACE FOR EVERY LESSON, A WORLD FOR EVERY CONCEPT, and places made from pieces (data) are drawn from the same pieces.
python tests_browser/test_batch39.py"""
import json, pathlib, sys, tempfile
from playwright.sync_api import sync_playwright
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import place_library  # noqa: E402
PAGE = HERE.parent / "player" / "explain.html"; URL = PAGE.as_uri()
data = json.loads(PAGE.read_text(encoding="utf-8").split("const DATA = ")[1].split(";\nconst $")[0])
res, errs = [], []
def ok(n, c, x=""): res.append(("✅" if c else "❌") + " " + n + ("" if c else " " + str(x)[:400]))
OPEN = "([gi,li])=>{window.stCtl&&window.stCtl.pause();document.querySelector(`#side .les[data-g=\"${gi}\"][data-l=\"${li}\"]`).click();}"
gi_of = lambda st, sj: next(i for i, g in enumerate(data["graphs"]) if g["audience"]["stage"] == st and g["subject"] == sj)
POS = "id=>{const g=document.querySelector(`#xs .sa[data-id=\"${id}\"]`)||document.querySelector('#xs .st-thief');const m=/translate\\(([-\\d.]+) ([-\\d.]+)/.exec(g.getAttribute('transform'));return [+m[1],+m[2]];}"

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1150, "height": 950}); pg.route("**/fonts.*/**", lambda r: r.abort()); pg.on("pageerror", lambda e: errs.append(str(e)[:200]))
    pg.goto(URL + "?q=hi"); pg.wait_for_timeout(500)
    # ---------- (1) the thief ----------
    gk = gi_of("kids", "science")
    pg.evaluate(OPEN, [gk, 2]); pg.wait_for_timeout(200)          # 🆕 batch 40: «البذرة» can be carried (the soil of lesson 0 is pulled down by a mole now)
    T = pg.evaluate("JSON.parse(document.querySelector('.st-screen').dataset.chap).find(c=>c[1]==='المفاجأة')[0]")
    tl = pg.evaluate("""T=>{const c=window.stCtl;c.pause();const W=+document.getElementById('xs').viewBox.baseVal.width,th=document.querySelector('#xs .st-thief');const out=[];
      for(let t=T;t<T+28&&t<c.DUR;t+=0.25){c.seek(t);const m=/translate\\(([-\\d.]+) ([-\\d.]+)/.exec(th.getAttribute('transform'));out.push({t:+t.toFixed(2),tx:+m[1],
        sub:(document.getElementById('stSub')||{}).textContent||'',grey:document.querySelectorAll('#xs .sa.st-gray').length,gone:[...document.querySelectorAll('#xs .sa')].filter(g=>g.style.opacity==='0').length,
        bub:[...document.querySelectorAll('#xs .st-bub')].map(g=>g.textContent).join('|')});}return {W,out};}""", T)
    W, out = tl["W"], tl["out"]
    inside = [o for o in out if 0 < o["tx"] < W]
    ok("🐰 kids: a thief (a rabbit of the garden, never a concept) comes into the picture at the twist", pg.locator("#xs .st-thief").count() == 1 and len(inside) > 4
       and pg.evaluate("document.querySelector('#xs .st-thief').dataset.k") == "rabbit", (len(inside), out[:2]))
    i_kid = next((i for i, o in enumerate(out) if "خطف" in o["sub"]), None)
    i_wo = next((i for i, o in enumerate(out) if "بدون" in o["sub"]), None)
    i_call = next((i for i, o in enumerate(out) if "نادى" in o["sub"] or "نادت" in o["sub"]), None)
    i_back = next((i for i, o in enumerate(out) if "رجع" in o["sub"] and i_call is not None and out.index(o) > i_call), None)
    ok("🐰 the order of the idea: «خطف» → «بدون … ما بيقدروا» → somebody calls «إحنا بنحتاجها» → it comes back", None not in (i_kid, i_wo, i_call, i_back) and i_kid < i_wo < i_call < i_back,
       (i_kid, i_wo, i_call, i_back))
    wo = [o for o in out if "بدون" in o["sub"]]
    ok("🐰 the story STAYS on what happens without it: the ones who need it are grey for seconds, they miss it («وين…؟»), the one taken is away",
       len(wo) * 0.25 >= 3 and max(o["grey"] for o in wo) >= 2 and any("وين" in o["bub"] for o in out) and max(o["gone"] for o in wo) == 1, (len(wo), [o["grey"] for o in wo][:6]))
    end = out[-1]
    ok("🐰 at the end it is back: nobody grey, nobody missing, the thief gone again (it said sorry)", any("آسف" in o["bub"] for o in out) and end["grey"] == 0 and end["gone"] == 0 and not (0 < end["tx"] < W), end)
    gj = gi_of("junior", "chemistry")                              # 🆕 batch 40: the robot carries «الذرة» (a force cannot be carried: «💭 تخيّلوا…»)
    pg.evaluate(OPEN, [gj, 0]); pg.wait_for_timeout(200)
    js = pg.evaluate("""()=>{const c=window.stCtl;c.pause();const s=new Set();for(let t=0;t<c.DUR;t+=0.3){c.seek(t);s.add(document.getElementById('stSub').textContent);}return [...s];}""")
    ok("🧭 junior: the thief too, said the explorers' way («⚡ فجأة خطف… وهرب!»)", any("⚡ فجأة خطف" in x for x in js) and pg.locator("#xs .st-thief").count() == 1, [x for x in js if "خطف" in x][:2])
    missing = []
    for gi, g in enumerate(data["graphs"]):
        st = g["audience"]["stage"]
        for li, l in enumerate(g["lessons"]):
            pg.evaluate(OPEN, [gi, li]); pg.wait_for_timeout(40)
            chap = [c[1] for c in json.loads(pg.evaluate("document.querySelector('.st-screen').dataset.chap"))]
            thief = pg.locator("#xs .st-thief").count()
            if st in ("kids", "junior") and "المفاجأة" in chap and not thief: missing.append((g["title"], l["lesson_title"]))
            if st in ("teen", "senior") and thief: missing.append(("thief in a grown-up story", l["lesson_title"]))
    ok("🐰 every twist of the little ones and the explorers has its thief; the board and the diagram keep the «test» / «hypothesis»", not missing, missing[:4])
    # ---------- (2) the board and the diagram answer the student ----------
    pg.close()
    ctx = b.new_context(viewport={"width": 1150, "height": 950}); pg = ctx.new_page(); pg.route("**/fonts.*/**", lambda r: r.abort()); pg.on("pageerror", lambda e: errs.append(str(e)[:200]))
    pg.clock.install(); pg.goto(URL + "?q=hi"); pg.clock.run_for(600)
    for st, sj, word in (("teen", "science", "دورك يا محقق"), ("senior", "physics", "توقّع")):
        gi = gi_of(st, sj)
        pg.evaluate(OPEN, [gi, 0]); pg.clock.run_for(300)
        # the auto video: it never stops to ask
        pg.evaluate("window.stCtl.seek(0)"); pg.evaluate("window.stCtl.play()"); pg.clock.run_for(15000)
        ok(f"{st}: in the auto video it never stops to ask (it shows the answer like an example)", pg.locator(".st-ask").count() == 0 and pg.evaluate("window.stCtl.t") > 10, pg.evaluate("window.stCtl.t"))
        # the student plays it himself
        pg.locator("#xs").dispatch_event("pointerdown"); pg.evaluate("window.stCtl.pause();window.stCtl.seek(0)"); pg.click("#stPP")
        for _ in range(120):
            pg.clock.run_for(250)
            if pg.locator(".st-ask").count(): break
        q = pg.inner_text(".st-ask .sa-q") if pg.locator(".st-ask").count() else ""
        sub = pg.inner_text("#stSub")
        n_opts = pg.locator(".st-ask .sa-opt").count()
        ok(f"{st}: when the student plays it, it stops and asks «{word}…» with 2–3 choices, and the line that tells the answer is not on yet",
           word in q and 2 <= n_opts <= 3 and "«" not in q and not any(x in sub for x in ("الدليل الأول", "بتعتمد على", "بيعتمد على")), (q, n_opts, sub))
        # try the choices one by one until the right one
        whys, done = [], False
        for i in range(n_opts):
            if not pg.locator(f".st-ask .sa-opt >> nth={i}").is_enabled(): continue
            pg.click(f".st-ask .sa-opt >> nth={i}"); pg.clock.run_for(300)
            whys.append(pg.inner_text(".st-ask .sa-why"))
            if pg.locator(".st-ask.sa-done").count(): done = True; break
        ok(f"{st}: every wrong choice is explained («مش العكس» / «ما إله علاقة مباشرة»), the right one says why it is right",
           done and whys[-1].startswith("✔") and all(w.startswith("✗") for w in whys[:-1]) and all("«" not in w for w in whys), whys)
        t_ask = pg.evaluate("window.stCtl.t"); pg.clock.run_for(5000)
        ok(f"{st}: then the window goes and the story goes on", pg.locator(".st-ask").count() == 0 and pg.evaluate("window.stCtl.t") > t_ask + 1, pg.evaluate("window.stCtl.t"))
        # a tap on a card / a node that is on the board → it tells about itself; one not shown yet → nothing
        pg.evaluate("window.stCtl.pause();window.stCtl.seek(window.stCtl.DUR-0.5)")
        pg.evaluate("(()=>{const g=[...document.querySelectorAll('#xs .st-tap')].find(x=>+getComputedStyle(x).opacity>0.5);g.dispatchEvent(new MouseEvent('click',{bubbles:true}));})()"); pg.clock.run_for(200)
        info = pg.inner_text(".st-info") if pg.locator(".st-info").count() else ""
        ok(f"{st}: a tap on a card / a node → what it is, and what it needs / who needs it", info and any(x in info for x in ("بيعتمد", "بتعتمد", "مبني")), info)
        if pg.locator(".st-info").count(): pg.click(".st-info .si-x")
        pg.evaluate("window.stCtl.seek(0.3)")
        pg.evaluate("(()=>{const g=[...document.querySelectorAll('#xs .st-tap')].find(x=>+getComputedStyle(x).opacity<0.5);if(g)g.dispatchEvent(new MouseEvent('click',{bubbles:true}));})()"); pg.clock.run_for(200)
        ok(f"{st}: a card / a node not on the board yet does not answer", pg.locator(".st-info").count() == 0)
        pg.evaluate("window.stCtl&&window.stCtl.pause()")
    ctx.close()
    # ---------- (3) places and zones ----------
    pg = b.new_page(viewport={"width": 1150, "height": 950}); pg.route("**/fonts.*/**", lambda r: r.abort()); pg.on("pageerror", lambda e: errs.append(str(e)[:200]))
    pg.goto(URL + "?q=hi"); pg.wait_for_timeout(400)
    places = {l["lesson_title"]: l.get("place") for g in data["graphs"] for l in g["lessons"]}
    ok("🏞️ every lesson has a place that fits its words (plants → garden, cells → lab, energy → workshop, the Nile → desert, numbers → class)",
       places["أجزاء النبات"] == "garden" and places["مكوّنات الخلية"] == "lab" and places["الطاقة والكهرباء"] == "machine" and places["الحياة حول النيل"] == "desert" and places["الجمع والطرح"] == "classroom", places)
    wrong_zone, n_z = [], 0
    for gi, g in enumerate(data["graphs"]):
        for li, l in enumerate(g["lessons"]):
            zs = l.get("zones") or {}
            for ci, c in enumerate(l["concepts"]):
                if c["concept_id"] not in zs: continue
                n_z += 1
                pg.evaluate(OPEN, [gi, li]); pg.wait_for_timeout(40)
                pg.evaluate(f"window.stCtl&&window.stCtl.pause();document.querySelector('#prog .pstop[data-c=\"{ci}\"]').click()"); pg.wait_for_timeout(60)
                got = pg.evaluate("[(document.querySelector('.st-screen')||{dataset:{}}).dataset.place,!!document.querySelector('#xs .pl.pl-full')]")
                if got[0] != zs[c["concept_id"]] or not got[1]: wrong_zone.append((c["title"], zs[c["concept_id"]], got))
    ok(f"🌍 every concept with a world of its own ({n_z}) has it behind its cartoon (the root under the ground, the nucleus in the cell, the atom…)", n_z >= 40 and not wrong_zone, wrong_zone[:4])
    pg.evaluate(OPEN, [gk, 0]); pg.wait_for_timeout(100)
    root_ci = next(ci for ci, c in enumerate(data["graphs"][gk]["lessons"][0]["concepts"]) if c["title"] == "الجذر")
    pg.evaluate(f"window.stCtl&&window.stCtl.pause();document.querySelector('#prog .pstop[data-c=\"{root_ci}\"]').click()"); pg.wait_for_timeout(200)
    pieces = pg.evaluate("[...new Set([...document.querySelectorAll('#xs .pl [data-pl]')].map(e=>e.dataset.pl))]")
    ok("🌍 «الجذر»: under the ground — roots, pebbles, a worm (the pieces move and answer a tap like every place)", {"roots", "pebble", "worm"} <= set(pieces), pieces)
    # the pieces the factory may use exist in the page: a copy of the page whose first lesson lives in a place made from ALL the pieces (a recipe = data)
    rec = {"id": "test_place", "label": "تجربة", "words": ["تجربة"], "sky": ["#FFF6EC", "#FDEBD8"], "ground": ["#E9D3B6", "#D9BE98"], "far": "tiles", "skyItems": ["sun"],
           "props": [[pc, 0.03 + (i % 16) * 0.06, 0, 0.5] for i, pc in enumerate(place_library.PIECES)], "extras": [[x, 0.1, 0, 0.8] for x in place_library.EXTRAS[:2]]}
    d2 = json.loads(json.dumps(data)); d2["graphs"][gk]["places"] = {"test_place": rec}; d2["graphs"][gk]["lessons"][0]["place"] = "test_place"; d2["graphs"][gk]["lessons"][0]["zones"] = {}
    html = PAGE.read_text(encoding="utf-8"); head, rest = html.split("const DATA = ", 1); tail = rest.split(";\nconst $", 1)[1]
    tmp = pathlib.Path(tempfile.mkdtemp()) / "recipe.html"; tmp.write_text(head + "const DATA = " + json.dumps(d2, ensure_ascii=False).replace("</", "<\\/") + ";\nconst $" + tail, encoding="utf-8")
    pg.goto(tmp.as_uri() + "?q=hi"); pg.wait_for_timeout(400)
    pg.evaluate(OPEN, [gk, 0]); pg.wait_for_timeout(100)
    pg.evaluate("window.stCtl&&window.stCtl.pause();document.querySelector('#prog .pstop[data-c=\"1\"]').click()"); pg.wait_for_timeout(200)
    got = pg.evaluate("[(document.querySelector('.st-screen')||{dataset:{}}).dataset.place,[...new Set([...document.querySelectorAll('#xs .pl [data-pl]')].map(e=>e.dataset.pl))]]")
    lost = [pc for pc in place_library.PIECES if pc not in got[1]]
    ok(f"🧱 a place made from pieces (a recipe, data) is drawn by the page — and every one of the {len(place_library.PIECES)} pieces the factory may use exists", got[0] == "test_place" and not lost, (got[0], lost))
    pg.close()
    # ---------- 📱 phone ----------
    ctx = b.new_context(viewport={"width": 390, "height": 844}, has_touch=True, is_mobile=True); pg = ctx.new_page(); pg.route("**/fonts.*/**", lambda r: r.abort()); pg.on("pageerror", lambda e: errs.append(str(e)[:200]))
    pg.clock.install(); pg.goto(URL); pg.clock.run_for(800)
    pg.evaluate(OPEN, [gi_of("teen", "science"), 0]); pg.clock.run_for(300)
    pg.locator("#xs").dispatch_event("pointerdown"); pg.evaluate("window.stCtl.pause();window.stCtl.seek(0)"); pg.click("#stPP")
    for _ in range(120):
        pg.clock.run_for(250)
        if pg.locator(".st-ask").count(): break
    fit = pg.evaluate("(()=>{const a=document.querySelector('.st-ask');if(!a)return null;const r=a.getBoundingClientRect();return [r.left>=0,r.right<=390,document.documentElement.scrollWidth];})()")
    ok("📱 the phone: the «دورك» window fits (no sideways scroll)", fit and fit[0] and fit[1] and fit[2] <= 391, fit)
    ctx.close()
    b.close()
print("\n".join(r for r in res if r.startswith("❌")) or "")
print(f"✅ {sum(r.startswith('✅') for r in res)} checks passed · ❌ {sum(r.startswith('❌') for r in res)} failed")
print("JS errors:", errs or "none")
