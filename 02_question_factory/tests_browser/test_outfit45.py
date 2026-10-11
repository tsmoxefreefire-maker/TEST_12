"""👗 batch 45 · the clothes (a TRIAL, Hareth: «بدي أغيّر ملابس الزهرة… الزهرة والجذر والثمرة… ثلاث ملابس لكل واحد») in a real browser:
the corner button is there only in the plants book · 3 outfits + «بلا» for each of the three · the outfit is ON the character in the scene on
screen at once (the story keeps its moment) and in the other scenes too · a new choice replaces the old one everywhere · «بلا» takes it off ·
kept after a reload · the drawing itself is untouched · another book: no button, nobody dressed · the phone · no JS error.
python tests_browser/test_outfit45.py [folder for pictures]"""
import json, pathlib, sys
from playwright.sync_api import sync_playwright
HERE = pathlib.Path(__file__).resolve().parent
PAGE = HERE.parent / "player" / "explain.html"; URL = PAGE.as_uri()
SHOTS = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else None
res, errs = [], []
def ok(n, c, x=""): res.append(("✅" if c else "❌") + " " + n + ("" if c else " " + str(x)[:400]))
OPEN = "([gi,li])=>{window.stCtl&&window.stCtl.pause();document.querySelector(`#side .les[data-g=\"${gi}\"][data-l=\"${li}\"]`).click();}"
WORN = "()=>Object.fromEntries([...document.querySelectorAll('#xs .ow45')].map(g=>g.dataset.ow.split(':')))"
PICK = "([id,k])=>document.querySelector(`#ow45p [data-ow=\"${id}:${k}\"]`).click()"

with sync_playwright() as p:
    b = p.chromium.launch()
    ctx = b.new_context(viewport={"width": 1150, "height": 950})
    pg = ctx.new_page(); pg.route("**/fonts.*/**", lambda r: r.abort()); pg.on("pageerror", lambda e: errs.append(str(e)[:200]))
    pg.goto(URL + "?q=hi"); pg.wait_for_timeout(700)
    ok("👗 the corner button is there (the plants book), next to «الصوت» and «الجودة»", pg.locator(".modebar #ow45b").count() == 1)
    ok("🎨 its style is a style (never shown as text on the page)", "ow45-panel{" not in pg.inner_text("body"))
    pg.evaluate("window.stCtl.pause();window.stCtl.seek(window.stCtl.DUR-1)"); pg.wait_for_timeout(150)
    plain = pg.evaluate("[...document.querySelectorAll('#xs .sa')].map(g=>g.querySelector('svg.ch').outerHTML.length)")
    if SHOTS: pg.screenshot(path=str(SHOTS / "outfit_before.png"))
    ok("nobody is dressed before a choice", pg.evaluate(WORN) == {})
    pg.click("#ow45b"); pg.wait_for_timeout(150)
    rows = pg.evaluate("[...document.querySelectorAll('#ow45p .ow45-row')].map(r=>r.querySelectorAll('.ow45-o').length)")
    ok("📋 the panel: the flower, the root and the fruit, each with «بلا» + 3 outfits", rows == [4, 4, 4], rows)
    t0 = pg.evaluate("window.stCtl.t")
    pg.evaluate(PICK, ["flower", 0]); pg.evaluate(PICK, ["root", 0]); pg.evaluate(PICK, ["fruit", 0]); pg.wait_for_timeout(200)
    w1 = pg.evaluate(WORN)
    ok("👑🎩🎓 the three wear their outfit in the scene on screen, at once", w1 == {"flower": "0", "root": "0", "fruit": "0"}, w1)
    ok("⏱️ the story stays at the same moment (drawn again, not started again)", abs(pg.evaluate("window.stCtl.t") - t0) < 1.0, (t0, pg.evaluate("window.stCtl.t")))
    if SHOTS: pg.screenshot(path=str(SHOTS / "outfit_after.png"))
    pg.evaluate(PICK, ["flower", 1]); pg.evaluate(PICK, ["fruit", 2]); pg.wait_for_timeout(200)
    w2 = pg.evaluate(WORN)
    ok("🔁 a new choice REPLACES the old one (one outfit at a time, never two)", w2 == {"flower": "1", "root": "0", "fruit": "2"} and pg.locator('#xs .sa[data-id="flower"] .ow45').count() == 1, w2)
    pg.evaluate(PICK, ["root", "-"]); pg.wait_for_timeout(200)
    w3 = pg.evaluate(WORN)
    ok("«بلا» takes it off", w3 == {"flower": "1", "fruit": "2"}, w3)
    if SHOTS: pg.screenshot(path=str(SHOTS / "outfit_changed.png"))
    # moves with the character: the outfit is INSIDE the character's group
    ok("🚶 the outfit is inside the character (it walks, hops and talks with it)", pg.evaluate("[...document.querySelectorAll('#xs .ow45')].every(o=>o.closest('.sa')&&o.closest('svg.ch'))"))
    # another scene of the same book: the flower's own scene
    pg.click("#ow45b"); pg.wait_for_timeout(100)
    stops = pg.evaluate("[...document.querySelectorAll('#prog .pstop')].map(s=>s.textContent.trim())")
    fi = next((i for i, s in enumerate(stops) if "الزهرة" in s), None)
    if fi is not None:
        pg.locator("#prog .pstop").nth(fi).click(force=True); pg.wait_for_timeout(500)
        ok("🌸 in the flower's own scene she still wears her glasses", pg.evaluate("[...document.querySelectorAll('.ow45')].some(o=>o.dataset.ow==='flower:1')"), stops)
    # kept after a reload
    pg.reload(); pg.wait_for_timeout(700); pg.evaluate("window.stCtl&&(window.stCtl.pause(),window.stCtl.seek(window.stCtl.DUR-1))"); pg.wait_for_timeout(150)
    ok("💾 after a reload the choice is still there (kept on this device)", pg.evaluate(WORN) == {"flower": "1", "fruit": "2"}, pg.evaluate(WORN))
    ok("🎨 the drawing itself is untouched (without the outfit it is exactly the same)", pg.evaluate("[...document.querySelectorAll('#xs .sa')].map(g=>{const s=g.querySelector('svg.ch').cloneNode(true);s.querySelectorAll('.ow45').forEach(o=>o.remove());return s.outerHTML.length;})") == plain)
    # another book: no button, nobody dressed
    data = json.loads(PAGE.read_text(encoding="utf-8").split("const DATA = ")[1].split(";\nconst $")[0])
    gm = next(i for i, g in enumerate(data["graphs"]) if g["subject"] == "math")
    pg.evaluate(OPEN, [gm, 0]); pg.wait_for_timeout(300)
    ok("📐 another book (maths): no button, nobody dressed", pg.locator("#ow45b").count() == 0 and pg.locator(".ow45").count() == 0)
    ctx.close()
    # the phone
    ctx = b.new_context(viewport={"width": 390, "height": 844}, has_touch=True, is_mobile=True)
    pg = ctx.new_page(); pg.route("**/fonts.*/**", lambda r: r.abort()); pg.on("pageerror", lambda e: errs.append(str(e)[:200]))
    pg.goto(URL + "?q=hi"); pg.wait_for_timeout(700); pg.click("#ow45b"); pg.wait_for_timeout(150)
    pg.evaluate(PICK, ["flower", 2]); pg.wait_for_timeout(200)
    w = pg.evaluate("[document.documentElement.scrollWidth, innerWidth]")
    box = pg.evaluate("(()=>{const r=document.getElementById('ow45p').getBoundingClientRect();return [r.left,r.right,innerWidth];})()")
    ok("📱 the phone: the panel fits the screen, the bow tie is on, no sideways scroll", w[0] <= w[1] + 1 and box[0] >= 0 and box[1] <= box[2] and pg.evaluate(WORN).get("flower") == "2", (w, box))
    if SHOTS: pg.screenshot(path=str(SHOTS / "outfit_phone.png"))
    ctx.close(); b.close()
ok("no JS error", not errs, errs[:3])
print("\n".join(res))
print(f"✅ {sum(r.startswith('✅') for r in res)} checks passed · ❌ {sum(r.startswith('❌') for r in res)} failed")
