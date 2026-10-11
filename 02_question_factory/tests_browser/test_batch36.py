"""🆕 batch 36 (Hareth's notes) in a real browser:
(1) CHARACTERS 2.0: depth on every drawing (gradients, the outline in the body's own colour), the glossy eyes, little shoes and a breath
    for the younger stages (none for the older ones), the arms come out of the body's real edge;
(2) the PLACES LIVE: birds / butterflies / falling leaves / bubbles come and go; a tap = the thing's own show (leaves + an apple fall,
    the cloud rains, the sun shines, the rocket takes off); the far and near layers move apart with the pointer; the ground has details;
    the place feels the game (a right answer → the sun laughs); the light quality: nothing moves;
(3) the GAME LAYER on every activity: a mission with progress dots, a gentle shake on a mistake, stars by the tries (+ a badge and
    confetti for the little ones, none for the older ones), «🔁 العب كمان» starts it again;
(4) the six remade activities: recipe (wrong food → «يع!» + why; take one back → hungry again) · compare (one card at a time) ·
    teach (❓ → 💡) · ladder (a choice on every rung) · journey (hidden stations, choose the next) · what if (guess, then check);
    power starts at night and lighting it brings the day;
(5) 🆕 batch 41: the video never plays the new choices for him (they wait for him) · the phone: nothing sideways.
python tests_browser/test_batch36.py"""
import json, pathlib, re, sys
from playwright.sync_api import sync_playwright
HERE = pathlib.Path(__file__).resolve().parent
PAGE = HERE.parent / "player" / "explain.html"; URL = PAGE.as_uri()
data = json.loads(PAGE.read_text(encoding="utf-8").split("const DATA = ")[1].split(";\nconst $")[0])
res, errs = [], []
def ok(n, c, x=""): res.append(("✅" if c else "❌") + " " + n + ("" if c else " " + str(x)[:300]))
STEPS = lambda s: 1 if s["kind"] == "meet" else len(s["steps"])


def find(kind, stage="kids"):
    for gi, g in enumerate(data["graphs"]):
        if g["audience"]["stage"] != stage: continue
        for li, l in enumerate(g["lessons"]):
            for ci, c in enumerate(l["concepts"]):
                for si, s in enumerate(c["scenes"]):
                    if s["kind"] == kind: return gi, li, ci, sum(STEPS(x) for x in c["scenes"][:si]), s


def page(b, q="hi", **kw):
    ctx = b.new_context(viewport=kw.pop("viewport", {"width": 1150, "height": 1000}), **kw); pg = ctx.new_page(); pg.route("**/fonts.*/**", lambda r: r.abort())
    pg.on("pageerror", lambda e: errs.append(str(e)[:200])); pg.goto(URL + (f"?q={q}" if q else "")); pg.wait_for_timeout(500); return ctx, pg


def open_scene(pg, f, video=False):
    gi, li, ci, n, s = f
    for _ in range(3):
        pg.evaluate("window.stCtl&&window.stCtl.pause()")
        pg.evaluate(f"document.querySelector('#side .les[data-g=\"{gi}\"][data-l=\"{li}\"]').click()"); pg.wait_for_timeout(150)
        pg.evaluate("window.stCtl&&window.stCtl.pause()")
        pg.evaluate(f"document.querySelector('#prog .pstop[data-c=\"{ci}\"]').click()"); pg.wait_for_timeout(150)
        pg.evaluate("document.getElementById('play').textContent.includes('وقّف')&&document.getElementById('play').click()")
        for _ in range(n): pg.evaluate("document.getElementById('next').click()")
        pg.wait_for_timeout(250)
        if not video: pg.evaluate("document.getElementById('play').textContent.includes('وقّف')&&document.getElementById('play').click()")
        pg.wait_for_timeout(350)
        if pg.evaluate("!!document.querySelector('.gx-mission')") or s["kind"] not in ("recipe",): break
    return s


click = lambda pg, sel: pg.evaluate("s=>{const e=document.querySelector(s);if(!e)return false;e.dispatchEvent(new MouseEvent('click',{bubbles:true}));return true;}", sel)
tap = lambda pg, sel: pg.evaluate("s=>{const e=document.querySelector(s);if(!e)return false;const r=e.getBoundingClientRect();['pointerdown','pointerup'].forEach(t=>e.dispatchEvent(new PointerEvent(t,{bubbles:true,clientX:r.left+r.width/2,clientY:r.top+r.height/2,pointerId:1})));return true;}", sel)
pips = lambda pg: pg.evaluate("[document.querySelectorAll('.gx-pips i.on').length,document.querySelectorAll('.gx-pips i').length]")
cap = lambda pg: pg.inner_text("#cap")

with sync_playwright() as p:
    b = p.chromium.launch()
    # ---------- (1) characters ----------
    ctx, pg = page(b); f = find("throw"); open_scene(pg, f); pg.wait_for_timeout(300)
    ch = pg.evaluate("""(()=>{const sv=[...document.querySelectorAll('#xs .xnode.g4-x .xbody>svg.ch')][0];
      const shapes=[...sv.querySelectorAll('path,circle,ellipse,rect')].filter(x=>!x.closest('.sface,.ch-arms,.ch-feet'));
      return {grad:shapes.filter(x=>/url\\(#c36g/.test(x.getAttribute('fill')||'')).length,ink:shapes.filter(x=>/^#3b2a1[ae]$/i.test(x.getAttribute('stroke')||'')).length,
        feet:!!sv.querySelector('.ch-feet'),breathe:!!sv.querySelector(':scope > .ch-breathe'),iris:!!sv.querySelector('.spupil circle[fill^="url(#c36iris)"]'),lid:!!sv.querySelector('.slid'),
        anim:getComputedStyle(sv.querySelector('.ch-breathe')).animationName,irisDef:!!document.getElementById('c36iris')};})()""")
    ok("🎨 the drawing has depth (its colours are gradients now)", ch["grad"] >= 1, ch)
    ok("🎨 the outline takes the body's own colour (no dark brown line on the body)", ch["ink"] == 0, ch)
    ok("👀 the new glossy eyes (a warm iris + the lid line)", ch["iris"] and ch["lid"] and ch["irisDef"], ch)
    ok("👟 little shoes + 🫁 it breathes (kids)", ch["feet"] and ch["breathe"] and ch["anim"] == "chBreathe", ch)
    ok("🪃 a ball in your hand: no shoes, no breathing (it stays still)", pg.evaluate("[...document.querySelectorAll('#xs .g4-ball svg.ch')].every(s=>!s.querySelector('.ch-feet')&&!s.querySelector('.ch-breathe'))"))
    arms = pg.evaluate("""(()=>{const out=[];document.querySelectorAll('#xs .xnode:not(.g4-ball) .xbody>svg.ch').forEach(sv=>{const a=sv.querySelector('.ch-arms .ch-arm.r path');if(!a)return;
      const m=/M([\\d.]+) ([\\d.]+)/.exec(a.getAttribute('d'));const x=+m[1],y=+m[2];const body=[...sv.querySelectorAll('path,circle,ellipse,rect')].filter(e=>!e.closest('.sface,.ch-arms,.ch-feet')&&e.getAttribute('fill')!=='none');
      const S=sv.getScreenCTM();const hit=body.some(e=>{try{const p=new DOMPoint(x-3,y).matrixTransform(e.getScreenCTM().inverse().multiply(S));return e.isPointInFill(p);}catch(_){return false;}});out.push(hit);});return out;})()""")
    ok("🙌 the arms start at the body's real edge (just inside the body, not in the air)", arms and sum(arms) >= len(arms) - 1, arms)
    sen = find("throw", "senior") or find("magnet", "senior") or find("compare", "senior")
    open_scene(pg, sen); pg.wait_for_timeout(300)
    ok("🧑‍🎓 the older stages: no shoes, a milder shade, no bounce", pg.evaluate("!document.querySelector('#xs .ch-feet')&&!!document.querySelector('#xs svg.ch [fill^=\"url(#c36m\"]')&&!document.querySelector('#xs svg.ch [fill^=\"url(#c36g\"]')"))
    ctx.close()
    # ---------- (2) the places live ----------
    ctx, pg = page(b)
    gs = next(i for i, g in enumerate(data["graphs"]) if g["subject"] == "science" and g["audience"]["stage"] == "kids")
    pg.evaluate(f"window.stCtl&&window.stCtl.pause();document.querySelector('#side .les[data-g=\"{gs}\"][data-l=\"0\"]').click()"); pg.wait_for_timeout(400)
    life = pg.evaluate("[document.querySelectorAll('#xs .pl-flyer').length,document.querySelectorAll('#xs .pl-flutter').length,document.querySelectorAll('#xs .pl-fall').length,!!document.querySelector('#xs .pl-grounddeco path,#xs .pl-grounddeco circle'),!!document.querySelector('#xs .pl-tufts')]")
    ok("🐦 the garden (cartoon): birds fly, butterflies flutter, leaves fall; the ground has grass and flowers", life[0] >= 1 and life[1] >= 1 and life[2] >= 1 and life[3] and life[4], life)
    ok("🐦 the birds really fly (CSS) and flap their wings", pg.evaluate("getComputedStyle(document.querySelector('#xs .pl-flyer .pl-cross')).animationName.startsWith('plCross')&&getComputedStyle(document.querySelector('#xs .pl-wing')).animationName==='plFlap'"))
    ok("☀️ the sun has a face (it blinks and follows you)", pg.evaluate("!!document.querySelector('#xs [data-pl=\"sun\"] .pl-sunface .seye')"))
    ok("🎨 the props have depth too (gradients)", pg.evaluate("document.querySelectorAll('#xs .pl-near [fill^=\"url(#c36\"]').length>5"))
    # the big picture (soft place) for the taps
    pg.evaluate("window.stCtl&&window.stCtl.pause();document.querySelector('#prog .pstop[data-c=\"-1\"]').click()"); pg.wait_for_timeout(300)
    pg.evaluate("document.getElementById('play').textContent.includes('وقّف')&&document.getElementById('play').click()"); pg.wait_for_timeout(400)
    tap(pg, '#xs .pl [data-pl="tree"]'); pg.wait_for_timeout(200)
    ok("🌳 tap a tree → leaves fall and an apple drops", pg.evaluate("document.querySelectorAll('#xs .pl-fx .pl-drop').length>=3&&!!document.querySelector('#xs .pl-fx .pl-apple')"))
    tap(pg, '#xs .pl [data-pl="cloud"]'); pg.wait_for_timeout(150)
    ok("☁️ tap the cloud → it rains", pg.evaluate("document.querySelectorAll('#xs .pl-fx .pl-rain').length>=6"))
    tap(pg, '#xs .pl [data-pl="sun"]'); pg.wait_for_timeout(150)
    ok("☀️ tap the sun → it shines and laughs", pg.evaluate("(()=>{const s=document.querySelector('#xs [data-pl=\"sun\"]');return s.classList.contains('pl-shine')&&s.querySelector('.pl-sunface').dataset.mood==='laugh';})()"))
    pg.mouse.move(200, 300); pg.wait_for_timeout(120); pg.mouse.move(900, 500, steps=5); pg.wait_for_timeout(200)
    ok("🫧 depth with the pointer: the far and near layers move apart", pg.evaluate("parseFloat(getComputedStyle(document.querySelector('#xs .pl')).getPropertyValue('--px'))>0.2"))
    pg.evaluate("document.dispatchEvent(new CustomEvent('gx',{detail:{type:'good'}}))"); pg.wait_for_timeout(100)
    ok("🎉 the place feels the game: a right answer → the sun laughs", pg.evaluate("document.querySelector('#xs [data-pl=\"sun\"] .pl-sunface').dataset.mood==='laugh'"))
    ctx.close()
    ctx, pg = page(b)
    gp = next(i for i, g in enumerate(data["graphs"]) if g["subject"] == "physics")
    pg.evaluate(f"window.stCtl&&window.stCtl.pause();document.querySelector('#side .les[data-g=\"{gp}\"][data-l=\"0\"]').click()"); pg.wait_for_timeout(400)
    ok("🌠 space: shooting stars and craters on the ground", pg.evaluate("!!document.querySelector('#xs .pl-shooting')&&!!document.querySelector('#xs .pl-grounddeco ellipse')"))
    tap(pg, '#xs .pl [data-pl="rocket"]'); pg.wait_for_timeout(150)
    ok("🚀 tap the rocket → it takes off (and comes back)", pg.evaluate("document.querySelector('#xs [data-pl=\"rocket\"] .pl-a').classList.contains('pl-launch')"))
    ctx.close()
    ctx, pg = page(b, q="lo"); pg.evaluate(f"window.stCtl&&window.stCtl.pause();document.querySelector('#side .les[data-g=\"{gs}\"][data-l=\"0\"]').click()"); pg.wait_for_timeout(400)
    ok("🐢 the light quality: no living things moving, the ground details stay", pg.evaluate("!document.querySelector('#xs .pl-life')&&!!document.querySelector('#xs .pl-grounddeco')"))
    ctx.close()
    # ---------- (3)+(4) the game layer and the six remade activities ----------
    ctx, pg = page(b)
    # 🍽️ recipe
    s = open_scene(pg, find("recipe")); order = pg.evaluate("[...document.querySelectorAll('#xs .na-ing')].map(e=>[+e.dataset.i,e.dataset.id])")
    need = {x["id"] for x in s["needs"]}; good = [i for i, d in order if d in need]; bad = [i for i, d in order if d not in need]
    ok("🎯 a mission with its progress dots", "أطعم" in pg.inner_text(".gx-mission") and pips(pg) == [0, len(s["needs"])], (pg.inner_text(".gx-mission"), pips(pg)))
    ok("🍽️ the table has food that is NOT his (decoys from the factory)", len(bad) >= 1 and len(order) == len(s["needs"]) + len(s.get("decoys", [])), order)
    tap(pg, f'#xs .na-ing[data-i="{bad[0]}"]'); pg.wait_for_timeout(1300)
    ok("😝 wrong food → «يع!», the reason, and it goes back (grey)", "ما " in cap(pg) and pg.evaluate(f"document.querySelector('#xs .na-ing[data-i=\"{bad[0]}\"]').classList.contains('g4-no')") and pg.evaluate("document.querySelector('.gx-mission').classList.contains('gx-shake')"), cap(pg))
    for i in good: tap(pg, f'#xs .na-ing[data-i="{i}"]'); pg.wait_for_timeout(1250)
    ok("😋 the right food: he eats it, an arrow joins it, the dots fill", pg.locator("#xs .na-ing.na-eaten").count() == len(good) and pg.locator("#xs #naArr .g4-arr").count() == len(good) and pips(pg)[0] == len(good))
    pg.wait_for_timeout(900)
    ok("⭐ the end: 2 stars (one mistake) + a badge + confetti", pg.locator(".gx-end .gx-stars i.on").count() == 2 and "طبّاخ" in pg.inner_text(".gx-end") and pg.locator(".gx-conf").count() > 5, pg.inner_text(".gx-end") if pg.locator(".gx-end").count() else "no end")
    tap(pg, f'#xs .na-ing[data-i="{good[0]}"]'); pg.wait_for_timeout(700)
    ok("⛔ take one back → he is missing it again (he needs ALL of them)", "شلت" in cap(pg) and pg.locator("#xs .na-ready").count() == 0, cap(pg))
    click(pg, ".gx-again"); pg.wait_for_timeout(500)
    ok("🔁 «العب كمان» starts it again (no dots, no stars)", pips(pg)[0] == 0 and pg.locator(".gx-end").count() == 0 and pg.locator("#xs .na-eaten").count() == 0)
    # ⚖️ compare
    s = open_scene(pg, find("compare"))
    ok("⚖️ one card at a time (it falls from the top)", pg.locator("#naTray .na-card").count() == 1 and pg.evaluate("getComputedStyle(document.querySelector('#naTray .na-card')).animationName.includes('g36Fall')"))
    for f_ in s["facts"]: click(pg, f'.na-zone[data-side="{f_["side"]}"]'); pg.wait_for_timeout(1150)
    pg.wait_for_timeout(1300)
    ok("⚖️ all sent home → 3 stars (no mistake)", pg.locator(".na-placed").count() == len(s["facts"]) and pg.locator(".gx-end .gx-stars i.on").count() == 3)
    # 💡 teach
    s = open_scene(pg, find("teach"))
    ok("❓ the friend's head is full of ❓", pg.locator("#xs .g36-q").count() == len(s["rounds"]) and pg.locator("#xs .g36-q.g36-got").count() == 0)
    r0 = s["rounds"][0]; kw = next(j for j, o in enumerate(r0["options"]) if not o["ok"]); kk = next(j for j, o in enumerate(r0["options"]) if o["ok"])
    click(pg, f'.na-opt[data-k="{kw}"]'); pg.wait_for_timeout(300)
    ok("🤔 a wrong answer makes the ❓ bigger", pg.locator("#xs .g36-q.g36-big").count() == 1)
    click(pg, f'.na-opt[data-k="{kk}"]'); pg.wait_for_timeout(300)
    ok("💡 a right answer turns one ❓ into 💡", pg.locator("#xs .g36-q.g36-got").count() == 1 and "💡" in pg.evaluate("(document.querySelector('#xs .g36-q.g36-got')||{}).textContent||''"))
    # 🪜 ladder (a rung with a choice)
    f = next((x for x in (find("ladder", st) for st in ("kids", "junior", "teen", "senior")) if x and any(r.get("wrong") for r in x[4]["rungs"])), None)
    ctx2, pg2 = page(b); s = open_scene(pg2, f)
    for r in s["rungs"]:
        if r.get("wrong"):
            ok("🪜 a rung is a choice (the right one + wrong ones, with pictures)", pg2.locator("#naOpts .na-opt").count() == 1 + len(r["wrong"]) and pg2.locator("#naOpts .g36-oart svg").count() >= 1)
            click(pg2, f'#naOpts .na-opt[data-id="{r["wrong"][0]["id"]}"]'); pg2.wait_for_timeout(250)
            ok("🪜 a wrong rung: it says why, and that card is off", ("ما" in pg2.inner_text("#cap")) and pg2.locator(f'#naOpts .na-opt[data-id="{r["wrong"][0]["id"]}"][disabled]').count() == 1, pg2.inner_text("#cap"))
            break
        click(pg2, "#naAsk"); pg2.wait_for_timeout(1300)
    for r in s["rungs"]:
        if not click(pg2, f'#naOpts .na-opt[data-id="{r["id"]}"]'): click(pg2, "#naAsk")
        pg2.wait_for_timeout(1500)
    pg2.wait_for_timeout(1000)
    ok("🪜 down to the end: every rung open, the stars", pg2.locator("#xs .xnode.na-hid").count() == 0 and pg2.locator(".gx-end").count() == 1)
    ctx2.close()
    # 🧭 journey
    s = open_scene(pg, find("journey"))
    ok("🧭 the stations ahead are hidden («؟»)", pg.locator("#xs .xnode.g36-hidden").count() == len(s["route"]) - 1 and pg.locator("#xs .g36-hole").count() == len(s["route"]) - 1)
    w = s["stops"][1].get("wrong", [])
    if w:
        click(pg, f'#naOpts .na-opt[data-id="{w[0]["id"]}"]'); pg.wait_for_timeout(500)
        ok("🧭 a wrong station: it says why, and nothing moves", pg.locator("#xs .xnode.g36-hidden").count() == len(s["route"]) - 1 and "ما " in cap(pg), cap(pg))
    for x in s["route"][1:]: click(pg, f'#naOpts .na-opt[data-id="{x}"]'); pg.wait_for_timeout(1600)
    pg.wait_for_timeout(800)
    ok("🧭 to the last station: all awake, the stars", pg.locator("#xs .xnode.g36-hidden").count() == 0 and pg.locator(".gx-end").count() == 1)
    # 🔮 what if
    s = open_scene(pg, find("what_if"))
    for x in s["affected"]: click(pg, f'#xs .xnode[data-id="{x}"]'); pg.wait_for_timeout(150)
    ok("🔮 guessing first: the guessed ones are marked", pg.locator("#xs .g36-mark.g36-pmark").count() == len(s["affected"]))
    click(pg, "#sw"); pg.wait_for_timeout(700 * len(s["affected"]) + 1500)
    ok("🔮 then switch off: every guess is checked (✅) → 3 stars", pg.locator("#xs .g36-mark.g36-ok").count() == len(s["affected"]) + len(s.get("calm", [])) and pg.locator(".gx-end .gx-stars i.on").count() == 3, cap(pg))
    # ⚡ power
    s = open_scene(pg, find("power"))
    ok("🌙 power starts at night", pg.evaluate("parseFloat(getComputedStyle(document.querySelector('#xs .g36-night')).opacity)>0.4"))
    for x in [y for y in s["sources"] if y != s["decoy"]]: click(pg, f'.g4-sw[data-id="{x}"]'); pg.wait_for_timeout(700)
    pg.wait_for_timeout(3400)
    ok("☀️ lighting it brings the day (and the stars)", pg.evaluate("document.getElementById('xs').classList.contains('g36-day')") and pg.locator(".gx-end").count() == 1)
    ctx.close()
    # the older stages: the same frame, no badge, no confetti
    ctx, pg = page(b); f = find("compare", "senior") or find("throw", "senior")
    s = open_scene(pg, f)
    for f_ in s["facts"]: click(pg, f'.na-zone[data-side="{f_["side"]}"]'); pg.wait_for_timeout(1150)
    pg.wait_for_timeout(1300)
    ok("🧑‍🎓 the older stages: stars, no badge, no confetti", pg.locator(".gx-end").count() == 1 and pg.locator(".gx-end b").count() == 0 and pg.locator(".gx-conf").count() == 0)
    ctx.close()
    # ---------- (5) 🆕 batch 41 (Hareth: «الفعاليات… الطالب هو اللي بيلعب فيها مو أوتوماتيك»): the video never plays the choices for him ----------
    for kind in ("journey", "what_if"):
        ctx, pg = page(b); pg.clock.install(); f = find(kind); open_scene(pg, f, video=True)
        pg.clock.run_for(90000)
        ok(f"🎬 the video never plays «{kind}» for him: 90 s later nothing chosen, no win, «🖐️ دورك» waits",
           pg.locator(".gx-mission.gx-done").count() == 0 and pips(pg)[0] == 0 and pg.locator("#turn").count() == 1, pips(pg))
        ctx.close()
    # the phone
    ctx, pg = page(b, viewport={"width": 390, "height": 844}, has_touch=True, is_mobile=True)
    wide = []
    for kind in ("recipe", "compare", "teach", "ladder", "journey", "what_if", "power"):
        f = find(kind) or find(kind, "junior")
        if not f: continue
        open_scene(pg, f); pg.wait_for_timeout(200)
        if pg.evaluate("document.documentElement.scrollWidth") > 391 or pg.evaluate("(()=>{const m=document.querySelector('.gx-mission');if(!m)return true;const r=m.getBoundingClientRect();return r.left<0||r.right>390;})()"):
            wide.append(kind)
    ok("📱 the phone: every remade activity fits (no sideways scroll, the mission inside)", not wide, wide)
    ctx.close()
    b.close()
print("\n".join(r for r in res if r.startswith("❌")) or "")
print(f"✅ {sum(r.startswith('✅') for r in res)} checks passed · ❌ {sum(r.startswith('❌') for r in res)} failed")
print("JS errors:", errs or "none")
