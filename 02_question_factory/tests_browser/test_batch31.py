"""🆕 batch 31 (Hareth) in a real browser, with a FAKE CLOCK (minutes of video in seconds):
(1) the video goes on BY ITSELF from scene to scene (a countdown between scenes), no «skip» needed;
(2) the countdown: ⏸ stops it · ▶ now goes at once · a touch on the scene stops it (the student is playing);
(3) 🆕 batch 41 (Hareth: «الفعاليات… الطالب هو اللي بيلعب فيها مو أوتوماتيك»): an ACTIVITY is never played by the video — it stops there,
    «🖐️ دورك», and goes on only after HE finishes (the puzzle dragged piece by piece → the countdown → the next scene);
(4) slower for the little ones; (5) the last scene → a lesson summary card (never jumps into the next lesson by itself);
(6) when the student takes control (manual «التالي»), nothing moves by itself;
(7) ONE page that knows phone / computer: body[data-dev] + quality hi/lo + the button + ?device= / ?q= in the link.
python tests_browser/test_batch31.py"""
import json, pathlib, urllib.parse, urllib.request
from playwright.sync_api import sync_playwright
HERE = pathlib.Path(__file__).resolve().parent
URL = (HERE.parent / "player" / "explain.html").as_uri()
html = open(urllib.request.url2pathname(urllib.parse.urlparse(URL).path), encoding="utf-8").read()
data = json.loads(html.split("const DATA = ")[1].split(";\nconst $")[0])
res, errs = [], []
def ok(n, c, x=""): res.append(("✅" if c else "❌") + " " + n + ("" if c else " " + str(x)[:300]))
ST = """({scene:(document.getElementById('xs')||{getAttribute:()=>null}).getAttribute('aria-label'),go:!!document.getElementById('goNext'),
  gn:(document.getElementById('gnSec')||{}).textContent||null,gt:(document.querySelector('#goNext .gn-t')||{}).textContent||'',ls:!!document.getElementById('lsum'),
  les:(document.querySelector('#side .les[aria-current="true"]')||{dataset:{}}).dataset.l,dot:[...document.querySelectorAll('.dots i')].findIndex(i=>i.classList.contains('on')),
  next:(document.getElementById('next')||{}).textContent,turn:!!document.getElementById('turn')})"""


def new(b, vp=None, url=URL, touch=False):
    ctx = b.new_context(viewport=vp or {"width": 1250, "height": 950}, has_touch=touch, is_mobile=touch)
    pg = ctx.new_page(); pg.route("**/fonts.*/**", lambda r: r.abort()); pg.on("pageerror", lambda e: errs.append(str(e)[:160]))
    pg.clock.install(); pg.goto(url); pg.clock.run_for(800)
    pg.click('#prog .pstop[data-c="-1"]', force=True); pg.clock.run_for(300)   # batch 32: a lesson starts with its story; these checks start at the big picture
    return ctx, pg


def run_until(pg, cond, limit_ms, step=250):
    t = 0
    while t < limit_ms:
        pg.clock.run_for(step); t += step
        s = pg.evaluate(ST)
        if cond(s):
            return s, t
    return pg.evaluate(ST), None


def open_lesson(pg, g, l):
    pg.click(f'#side .les[data-g="{g}"][data-l="{l}"]', force=True); pg.clock.run_for(400)


# 🆕 batch 42: the «parts» scene takes turns from lesson to lesson → the plants lesson whose parts scene is the puzzle (and no little world before it)
_L0 = data["graphs"][0]["lessons"]
PUZ = next((i for i, l in enumerate(_L0) if (l.get("assemble") or {}).get("kind") == "assemble" and not l.get("world")),
           next(i for i, l in enumerate(_L0) if (l.get("assemble") or {}).get("kind") == "assemble"))


def puzzle_lesson(pg):
    if PUZ:
        open_lesson(pg, 0, PUZ); pg.click('#prog .pstop[data-c="-1"]', force=True); pg.clock.run_for(300)


with sync_playwright() as p:
    b = p.chromium.launch()
    # ---------- (1) + (3): plants · the lesson starts: overview → (countdown) → puzzle (HIS) → … by itself ----------
    ctx, pg = new(b); puzzle_lesson(pg)
    first = pg.evaluate(ST)["scene"]
    s, t = run_until(pg, lambda s: s["go"], 60000)
    ok("the end of a scene → a countdown appears by itself", t is not None and "المشهد الجاي" in s["gt"], s)
    secs = []
    for _ in range(3):
        secs.append(pg.evaluate(ST)["gn"]); pg.clock.run_for(1000)
    ok("the countdown counts down (seconds)", len({x for x in secs if x}) >= 2 and int(secs[0]) > int(secs[-1]), secs)
    s, t = run_until(pg, lambda s: s["scene"] != first, 20000)
    ok(f"…then the NEXT scene plays by itself ({first} → {s['scene']})", t is not None, s)
    ok("the next scene is the puzzle", s["scene"] == "ركّب المشهد", s)
    ids = pg.evaluate("[...document.querySelectorAll('#xs .xnode.piece')].map(n=>n.dataset.id)")
    s, t = run_until(pg, lambda s: s["go"] or pg.evaluate("document.querySelectorAll('#xs .xnode.placed').length") > 0, 90000)
    ok(f"🧩 🆕 the video STOPS at the puzzle: 90 s later not one of the {len(ids)} pieces placed by itself, no countdown, «🖐️ دورك»", t is None and s["turn"], s)
    for i in ids:                                                  # HE builds it: each piece dragged to its shadow
        a = pg.evaluate("s=>{const r=document.querySelector(s).getBoundingClientRect();return [r.left+r.width/2,r.top+r.height/2]}", f'#xs .xnode.piece[data-id="{i}"]')
        z = pg.evaluate("s=>{const r=document.querySelector(s).getBoundingClientRect();return [r.left+r.width/2,r.top+r.height/2]}", f'#xs .shadow[data-id="{i}"]')
        pg.mouse.move(*a); pg.mouse.down(); pg.clock.run_for(40)
        for k in range(1, 9): pg.mouse.move(a[0] + (z[0] - a[0]) * k / 8, a[1] + (z[1] - a[1]) * k / 8); pg.clock.run_for(20)
        pg.mouse.up(); pg.clock.run_for(300)
    s, t = run_until(pg, lambda s: s["go"], 20000)
    ok("…HE built it → the countdown to the next scene", t is not None and pg.evaluate("document.querySelectorAll('#xs .xnode.placed').length") == len(ids), s)
    # (2) ⏸ stops it
    pg.click("#gnStop"); pg.clock.run_for(300); here = pg.evaluate(ST)
    pg.clock.run_for(30000)
    ok("⏸ «وقّف» in the countdown → nothing moves (30 s later: same scene)", not pg.evaluate(ST)["go"] and pg.evaluate(ST)["scene"] == here["scene"], pg.evaluate(ST))
    ctx.close()
    # (2) ▶ now · a touch stops
    ctx, pg = new(b); puzzle_lesson(pg)
    s, t = run_until(pg, lambda s: s["go"], 60000)
    before = s["scene"]; pg.click("#gnGo"); pg.clock.run_for(500)
    ok("▶ «هلأ» → the next scene at once", pg.evaluate(ST)["scene"] != before, pg.evaluate(ST))
    s, t = run_until(pg, lambda s: s["go"] or pg.evaluate("document.querySelectorAll('#xs .xnode.placed').length") > 0, 90000)
    box = pg.locator("#xs").bounding_box(); pg.mouse.click(box["x"] + box["width"] - 20, box["y"] + 20); pg.clock.run_for(400)
    placed = pg.evaluate("document.querySelectorAll('#xs .xnode.placed').length"); pg.clock.run_for(20000)
    ok("the activity waits for him, and a touch on it moves nothing by itself (the student is playing)", not pg.evaluate(ST)["go"] and pg.evaluate("document.querySelectorAll('#xs .xnode.placed').length") == placed and pg.evaluate(ST)["scene"] == "ركّب المشهد", (placed, pg.evaluate(ST)))
    ctx.close()
    # ---------- (3) 🆕 batch 41: the video never feeds the recipe for him · «🖐️ دورك» stays (never a countdown past an activity) ----------
    gi, li = next((gi, li) for gi, g in enumerate(data["graphs"]) for li, l in enumerate(g["lessons"]) if any(sc["kind"] == "recipe" for c in l["concepts"] for sc in c["scenes"]))
    ctx, pg = new(b); open_lesson(pg, gi, li)
    RECIPE = ("الشروط", "الوصفة", "أطعم")                          # 🆕 batch 36: «🍽️ أطعم» for the little ones
    for _ in range(12):                                            # walk to the recipe (the video stops at every activity: «✓ خلصت» moves on)
        s, t = run_until(pg, lambda s: s["scene"] in RECIPE or s["turn"], 400000, 500)
        if s["scene"] in RECIPE: break
        pg.click("#turnDone"); pg.clock.run_for(300); s, t = run_until(pg, lambda s: s["go"], 20000); pg.click("#gnGo"); pg.clock.run_for(400)
    n = pg.evaluate("document.querySelectorAll('#xs .na-ing').length")
    s2, t2 = run_until(pg, lambda s: pg.evaluate("!!document.querySelector('#xs .na-tgt.na-ready')") or s["go"], 120000)
    ok(f"🍽️ the video never feeds him: 2 minutes later nothing eaten ({n} on the table), no countdown, «🖐️ دورك» waits", s["scene"] in RECIPE and n and t2 is None and pg.evaluate(ST)["turn"], s2)
    ctx.close()
    # ---------- (4) slower for the little ones ----------
    def first_step_ms(stage):
        g = next(i for i, x in enumerate(data["graphs"]) if x["audience"]["stage"] == stage)
        c2, q = new(b); open_lesson(q, g, 0); q.click('#prog .pstop[data-c="-1"]', force=True); q.clock.run_for(200)   # the big picture (not the story)
        q.click('#play'); q.clock.run_for(100)                       # stop
        q.click('#play'); q.clock.run_for(50)                        # play again from step 0
        s, t = run_until(q, lambda s: s["dot"] >= 1, 20000, 100)
        c2.close(); return t
    kms, sms = first_step_ms("kids"), first_step_ms("senior")
    ok(f"the little ones get more time per step ({kms} ms) than the secondary ({sms} ms)", kms and sms and kms > sms, (kms, sms))
    # ---------- (5) the last scene → a summary card · (6) manual control = nothing moves ----------
    gi = next(i for i, g in enumerate(data["graphs"]) if len(g["lessons"]) > 1)
    ctx, pg = new(b); open_lesson(pg, gi, 0)
    for _ in range(400):
        if "خلصت الدرس" in (pg.evaluate(ST)["next"] or ""):
            break
        pg.click("#next", force=True); pg.clock.run_for(60)
    pg.clock.run_for(25000)
    ok("manual control (the student pressed «التالي») → no countdown, nothing moves by itself", not pg.evaluate(ST)["go"] and not pg.evaluate(ST)["ls"], pg.evaluate(ST))
    if pg.locator("#play").is_visible(): pg.click("#play")      # 🆕 batch 41: the last scene can be an activity (no ▶): HE says «✓ خلصت»
    else: pg.click("#turnDone")
    s, t = run_until(pg, lambda s: s["ls"], 120000)
    ok("the last scene (video) → a lesson summary card", t is not None, s)
    chips = pg.evaluate("[...document.querySelectorAll('#lsum .ls-chip')].map(c=>c.textContent)")
    ok("the summary lists what he met (the lesson's concepts)", len(chips) == len(data["graphs"][gi]["lessons"][0]["concepts"]), chips)
    pg.clock.run_for(30000)
    ok("…and it never jumps into the next lesson by itself", pg.evaluate(ST)["les"] == "0", pg.evaluate(ST))
    pg.click("#lsNext"); pg.clock.run_for(600)
    ok("«الدرس الجاي ←» opens the next lesson, and its video plays", pg.evaluate(ST)["les"] == "1" and pg.evaluate("document.getElementById('play').textContent.includes('وقّف')"), pg.evaluate(ST))
    ctx.close()
    # ---------- (7) phone or computer: one page ----------
    ctx, pg = new(b)
    d = pg.evaluate("[document.body.dataset.dev,document.body.dataset.q]")
    ok("🖥️ a computer (mouse, big screen) → data-dev=desktop", d[0] == "desktop", d)
    ctx.close()
    ctx, pg = new(b, {"width": 390, "height": 844}, touch=True)
    d = pg.evaluate("[document.body.dataset.dev,document.body.dataset.q,(document.querySelector('#qBtn .q37-on')||{}).textContent]")   # 🆕 batch 37: the switch shows both, the ON one filled
    ok("📱 a phone (finger, small screen) → data-dev=phone and the lighter quality", d[0] == "phone" and d[1] == "lo" and "خفيفة" in (d[2] or ""), d)
    f = pg.evaluate("getComputedStyle(document.querySelector('#xs .xbody')).filter")
    ok("📱 lighter = no heavy glow/shadow filters on the characters", f in ("none", ""), f)
    pg.click('#qBtn .q37-o[data-q="hi"]'); pg.clock.run_for(200)
    ok("the «✨ جودة» button switches it by hand", pg.evaluate("document.body.dataset.q") == "hi", pg.evaluate("document.body.dataset.q"))
    pg.reload(); pg.clock.run_for(800)
    ok("…and the choice is remembered in this browser", pg.evaluate("document.body.dataset.q") == "hi", pg.evaluate("document.body.dataset.q"))
    ctx.close()
    ctx, pg = new(b, url=URL + "?device=phone&q=hi")
    d = pg.evaluate("[document.body.dataset.dev,document.body.dataset.q]")
    ok("the platform can force it in the link (?device=phone&q=hi)", d == ["phone", "hi"], d)
    ctx.close()
    b.close()
print("\n".join(r for r in res if r.startswith("❌")) or "")
print(f"✅ {sum(r.startswith('✅') for r in res)} checks passed · ❌ {sum(r.startswith('❌') for r in res)} failed")
print("JS errors:", errs or "none")
