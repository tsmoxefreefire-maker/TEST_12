"""🆕 batch 41 (Hareth: «الفعاليات بتشتغل لحالها… بتضل شغالة زي الفيديو… لازم تكون للطالب، هو اللي يتفاعل معها») in a real browser, FAKE CLOCK:
(1) the video left alone (nobody touches) in every stage: it plays the story and the big picture, then STOPS at the first activity —
    nothing in it moves or gets solved (minutes later: same scene, same caption, nothing placed / chosen), no countdown, no ▶ on it,
    and «🖐️ دورك!» tells him how to play;
(2) EVERY activity scene of the 12 books opens «closed»: «🖐️ دورك», no ▶, no video running on it, nothing solved by itself;
(3) the student plays it and wins (the puzzle by dragging, the tower, the switches, the journey) → «ليش؟» opens → the countdown →
    the next scene, and the video plays again there; «✓ خلصت» does the same for an activity with no win (the sliders);
    «🔁 العب كمان» → the activity is closed again (his again);
(4) the phone: the page never scrolls sideways, and «🖐️ دورك» fits;
(5) 🌳 NOTHING STANDS WHERE IT DOES NOT BELONG (Hareth: «الدودة طالعة بالسما والحجر طالع بالسما»): every place and little world, at every
    size the page uses — no worm or stone above the soil, no sun under the ground, nothing cut off, an owl sits on something (place_audit.py).
python tests_browser/test_batch41.py"""
import json, pathlib, re, sys
from playwright.sync_api import sync_playwright
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import place_audit  # noqa: E402
PAGE = HERE.parent / "player" / "explain.html"; URL = PAGE.as_uri()
data = json.loads(PAGE.read_text(encoding="utf-8").split("const DATA = ", 1)[1].split(";\nconst $", 1)[0])
res, errs = [], []
def ok(n, c, x=""): res.append(("✅" if c else "❌") + " " + n + ("" if c else " " + str(x)[:400]))
ACTS = {"assemble", "recipe", "connect", "compare", "teach", "slider", "lens", "flip", "ladder", "throw", "tower", "magnet", "machine", "power", "journey", "what_if", "before_after",
        "build_up", "missing", "who_am_i", "sentence"}   # 🆕 batch 42: the two new «parts» games are the student's too · 🆕 batch 43: 🕵️ + 🧩 too
STEPS = lambda s: 1 if s["kind"] == "meet" else len(s["steps"])
clean = lambda t: re.sub(r"\s+", " ", str(t).replace("«", "").replace("»", "")).strip()
# what can change when somebody plays: the caption, the progress dots, the pieces placed, the bricks set, the switches on, the slider values, the win
SIG = """(()=>{const q=s=>document.querySelectorAll(s).length;return JSON.stringify([(document.getElementById('cap')||{}).textContent,q('.gx-pips i.on'),q('.gx-mission.gx-done'),
  q('#xs .xnode.placed'),q('#xs .g4-set'),q('[aria-pressed="true"].g4-sw'),q('.gx-end'),[...document.querySelectorAll('#q input[type=range]')].map(i=>i.value).join(',')]);})()"""
ST = """({turn:!!document.getElementById('turn'),how:((document.querySelector('#turn .yt-t')||{}).textContent||''),go:!!document.getElementById('goNext'),
  play:!(document.getElementById('play')||{hidden:true}).hidden,pressed:(document.getElementById('play')||{getAttribute:()=>''}).getAttribute('aria-pressed'),
  where:(document.querySelector('#prog .where')||{}).textContent||'',why:!(document.getElementById('why')||{hidden:true}).hidden,gt:(document.querySelector('#goNext .gn-t')||{}).textContent||''})"""


def new(b, **kw):
    ctx = b.new_context(viewport=kw.pop("viewport", {"width": 1150, "height": 1000}), **kw); pg = ctx.new_page(); pg.route("**/fonts.*/**", lambda r: r.abort())
    pg.on("pageerror", lambda e: errs.append(str(e)[:200])); pg.clock.install(); pg.goto(URL + "?q=hi"); pg.clock.run_for(600); return ctx, pg


def open_lesson(pg, gi, li):
    pg.evaluate(f"document.querySelector('#side .les[data-g=\"{gi}\"][data-l=\"{li}\"]').click()"); pg.clock.run_for(300)


def find(kind, stage="kids"):
    for gi, g in enumerate(data["graphs"]):
        if stage and g["audience"]["stage"] != stage: continue
        for li, l in enumerate(g["lessons"]):
            for ci, c in enumerate(l["concepts"]):
                for si, s in enumerate(c["scenes"]):
                    if s["kind"] == kind: return gi, li, ci, sum(STEPS(x) for x in c["scenes"][:si]), s


def open_scene(pg, f):
    gi, li, ci, n, s = f
    open_lesson(pg, gi, li)
    pg.evaluate("window.stCtl&&window.stCtl.pause()")
    pg.evaluate(f"document.querySelector('#prog .pstop[data-c=\"{ci}\"]').click()"); pg.clock.run_for(200)
    for _ in range(n): pg.evaluate("document.getElementById('next').click()")
    pg.clock.run_for(400)
    return s


def drag(pg, a, b):
    ra = pg.evaluate("s=>{const r=document.querySelector(s).getBoundingClientRect();return [r.left+r.width/2,r.top+r.height/2]}", a)
    rb = pg.evaluate("s=>{const r=document.querySelector(s).getBoundingClientRect();return [r.left+r.width/2,r.top+r.height/2]}", b)
    pg.mouse.move(*ra); pg.mouse.down(); pg.clock.run_for(50)
    for k in range(1, 9): pg.mouse.move(ra[0] + (rb[0] - ra[0]) * k / 8, ra[1] + (rb[1] - ra[1]) * k / 8); pg.clock.run_for(20)
    pg.mouse.up(); pg.clock.run_for(300)


click = lambda pg, sel: pg.evaluate("s=>{const e=document.querySelector(s);if(!e)return false;e.dispatchEvent(new MouseEvent('click',{bubbles:true}));return true;}", sel)


def then_the_video_goes_on(pg, name):
    """after he finishes: «ليش؟» opens, the countdown, the next scene — and the video plays there again"""
    here = pg.evaluate(ST)["where"]
    for _ in range(40):
        pg.clock.run_for(250)
        if pg.evaluate(ST)["go"]: break
    s = pg.evaluate(ST)
    last = "ملخّص الدرس" in s["gt"]                                # the lesson's last scene: the summary comes next (not a scene)
    ok(f"{name}: he finished → «🖐️ دورك» goes away, «ليش؟» opens, and the countdown to the next scene (or to the lesson's summary)", not s["turn"] and s["why"] and s["go"] and ("المشهد الجاي" in s["gt"] or last), s)
    for _ in range(80):
        pg.clock.run_for(500)
        if pg.evaluate(ST)["where"] != here or pg.locator("#lsum").count(): break
    s = pg.evaluate(ST)
    if last:
        ok(f"{name}: …then the lesson's summary card (it never jumps into the next lesson by itself)", pg.locator("#lsum").count() == 1, s)
        return
    nxt_act = any(k in s["where"] for k in ("ركّب", "أطعم", "الشروط", "الوصفة", "قارن", "علّم", "الشريط", "السلّم", "ارمي", "البرج", "المغناطيس", "الآلة", "وصّل", "الرحلة", "شو بيصير", "قبل وبعد", "ارسم"))
    ok(f"{name}: …then the next scene, and the video plays there again (or it is the next activity: closed)", s["where"] != here and ((s["play"] and s["pressed"] == "true") or (nxt_act and s["turn"])), (here, s))


with sync_playwright() as p:
    b = p.chromium.launch()
    # ---------- (1) the video left alone, in every stage ----------
    for st in ("kids", "junior", "teen", "senior"):
        gi = next(i for i, g in enumerate(data["graphs"]) if g["audience"]["stage"] == st)
        ctx, pg = new(b); open_lesson(pg, gi, 0)
        countdowns, s = 0, pg.evaluate(ST)
        for _ in range(240):                                       # up to 20 minutes of video, nobody touches anything
            pg.clock.run_for(5000); s = pg.evaluate(ST)
            countdowns += s["go"]
            if s["turn"]: break
        ok(f"{st}: the video plays by itself (story, big picture…) and STOPS at the first activity ({s['where']})", s["turn"] and countdowns >= 1, (countdowns, s))
        sig0, here = pg.evaluate(SIG), s["where"]
        pg.clock.run_for(180000)                                   # three more minutes
        s = pg.evaluate(ST)
        ok(f"{st}: …3 minutes later nothing in it moved or got solved, no countdown, the same scene", pg.evaluate(SIG) == sig0 and not s["go"] and s["where"] == here, (sig0, pg.evaluate(SIG), s))
        ok(f"{st}: no ▶ on the activity (nothing can make it play by itself), and «🖐️ دورك» says how to play", not s["play"] and "دورك" in s["how"] and len(clean(s["how"])) > 15, s)
        ctx.close()
    # ---------- (2) EVERY activity scene of the 12 books opens closed ----------
    ctx, pg = new(b); bad, n_act = [], 0
    for gi, g in enumerate(data["graphs"]):
        for li, l in enumerate(g["lessons"]):
            for ci, c in enumerate(l["concepts"]):
                for si, sc in enumerate(c["scenes"]):
                    if sc["kind"] not in ACTS: continue
                    n_act += 1
                    open_scene(pg, (gi, li, ci, sum(STEPS(x) for x in c["scenes"][:si]), sc))
                    s0, sig0 = pg.evaluate(ST), pg.evaluate(SIG)
                    pg.clock.run_for(20000)
                    s1 = pg.evaluate(ST)
                    want_how = clean(sc["steps"][1]) if len(sc["steps"]) >= 3 else ""
                    if not (s0["turn"] and not s0["play"] and pg.evaluate(SIG) == sig0 and not s1["go"] and s1["where"] == s0["where"] and (not want_how or want_how[:20] in clean(s0["how"]))):
                        bad.append((g["title"][:14], l["lesson_title"][:14], sc["kind"], s0["turn"], s0["play"], s1["go"]))
    total = sum(1 for g in data["graphs"] for l in g["lessons"] for c in l["concepts"] for sc in c["scenes"] if sc["kind"] in ACTS)
    ok(f"every activity of the 12 books ({n_act}) opens closed: «🖐️ دورك» with how to play, no ▶, nothing moves by itself in 20 s", not bad and n_act == total and n_act > 150, bad[:6])
    ctx.close()
    # ---------- (3) the student plays and wins → the video goes on ----------
    # 🧩 the puzzle, reached by the video itself (kids): he drags every piece to its shadow
    gi = next(i for i, g in enumerate(data["graphs"]) if g["audience"]["stage"] == "kids" and g["subject"] == "science")
    li = next(i for i, l in enumerate(data["graphs"][gi]["lessons"]) if (l.get("assemble") or {}).get("kind") == "assemble")   # (batch 42: the parts scene takes turns)
    ctx, pg = new(b); open_lesson(pg, gi, li)
    for _ in range(120):
        pg.clock.run_for(5000)
        if pg.evaluate(ST)["turn"]: break
    ids = pg.evaluate("[...document.querySelectorAll('#xs .xnode.piece')].map(n=>n.dataset.id)")
    ok("🧩 the video stopped at the puzzle, nothing placed", "ركّب" in pg.evaluate(ST)["where"] and ids and pg.evaluate("document.querySelectorAll('#xs .xnode.placed').length") == 0)
    for i in ids: drag(pg, f'#xs .xnode.piece[data-id="{i}"]', f'#xs .shadow[data-id="{i}"]')
    ok(f"🧩 he built it himself ({len(ids)} pieces dragged to their shadows)", pg.evaluate("document.querySelectorAll('#xs .xnode.placed').length") == len(ids))
    then_the_video_goes_on(pg, "🧩 the puzzle")
    ctx.close()
    # 🏗️ the tower · ⚡ the switches · 🧭 the journey (he plays them the student's way: taps)
    for kind in ("tower", "power", "journey"):
        f = find(kind); ctx, pg = new(b); s = open_scene(pg, f)
        if kind == "tower":
            for k in range(len(s["blocks"])):
                click(pg, f'#xs .g4-brick[data-i="{k}"]'); pg.clock.run_for(1600)
        elif kind == "power":
            for i in [x for x in s["sources"] if x != s["decoy"]]:
                click(pg, f'.g4-sw[data-id="{i}"]'); pg.clock.run_for(1600)
        else:
            for at in range(len(s["route"]) - 1):
                click(pg, f'.na-opt[data-id="{s["route"][at + 1]}"]'); pg.clock.run_for(1900)
        for _ in range(20):                                        # the stars come after the last move's little show (the light runs through the wires…)
            pg.clock.run_for(300)
            if pg.locator(".gx-end").count(): break
        ok(f"{kind}: he won it himself (the stars)", pg.locator(".gx-mission.gx-done").count() == 1 and pg.locator(".gx-end").count() == 1)
        then_the_video_goes_on(pg, kind)
        ctx.close()
    # «🔁 العب كمان»: after a win the activity is closed again
    f = find("tower"); ctx, pg = new(b); s = open_scene(pg, f)
    for k in range(len(s["blocks"])):
        click(pg, f'#xs .g4-brick[data-i="{k}"]'); pg.clock.run_for(1600)
    pg.clock.run_for(900); click(pg, ".gx-again"); pg.clock.run_for(600)
    sig0 = pg.evaluate(SIG); pg.clock.run_for(30000); s1 = pg.evaluate(ST)
    ok("🔁 «العب كمان» → the tower is empty and closed again: «🖐️ دورك», no countdown, nothing builds itself", s1["turn"] and not s1["go"] and pg.evaluate(SIG) == sig0
       and pg.locator("#xs .g4-set").count() == 0, (s1, pg.evaluate(SIG)))
    ctx.close()
    # ✓ «خلصت» for an activity with no win (the magic sliders)
    f = find("slider", None); ctx, pg = new(b); open_scene(pg, f)
    pg.evaluate("(()=>{const a=document.getElementById('a');a.value=+a.value+1;a.dispatchEvent(new Event('input',{bubbles:true}));})()"); pg.clock.run_for(300)
    pg.click("#turnDone"); then_the_video_goes_on(pg, "🎚️ the sliders («✓ خلصت»)")
    ctx.close()
    # ---------- (4) the phone ----------
    ctx, pg = new(b, viewport={"width": 390, "height": 844}, has_touch=True, is_mobile=True); open_scene(pg, find("recipe"))
    fit = pg.evaluate("(()=>{const t=document.getElementById('turn');if(!t)return null;const r=t.getBoundingClientRect();return [r.left>=0,r.right<=window.innerWidth+1,document.documentElement.scrollWidth];})()")
    ok("📱 the phone: «🖐️ دورك» fits (no sideways scroll)", fit and fit[0] and fit[1] and fit[2] <= 391, fit)
    ctx.close()
    ctx, pg = new(b, viewport={"width": 390, "height": 844}, has_touch=True, is_mobile=True)
    w = pg.evaluate("[document.documentElement.scrollWidth, window.scrollX]")
    ok("📱 the phone: the page itself never scrolls sideways (it did once, with a style file left without <style>)", w[0] <= 391 and w[1] == 0, w)
    ctx.close()
    # ---------- (5) nothing stands where it does not belong ----------
    ctx, pg = new(b); probs = place_audit.audit(pg)
    ok(f"🌳 every place and little world × {len(place_audit.SIZES)} sizes: no worm or stone in the sky, no sun under the ground, nothing cut off, the owls sit on something", not probs, probs[:6])
    ctx.close()
    b.close()

print("\n".join(res))
print(f"✅ {sum(r.startswith('✅') for r in res)} checks passed · ❌ {sum(r.startswith('❌') for r in res)} failed")
print("JS errors:", errs[:5] or "none")
