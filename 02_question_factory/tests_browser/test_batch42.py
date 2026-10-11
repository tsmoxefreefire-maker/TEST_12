"""🆕 batch 42 (Hareth: «التكرار») in a real browser, FAKE CLOCK:
(1) 🎨 THE SAME GAME, ANOTHER LOOK: the journey (road · river · rail · space), the tower (blocks · castle · books), compare (circles ·
    baskets · houses) and the puzzle (shadows · frames · sky) — every look draws, the game still works in it, and the look follows the
    book / lesson / concept (the next lesson gets the next look); across the 12 books every kind shows more than one look;
(2) 🌱 «ابنيها من تحت»: opens closed («🖐️ دورك», no ▶) · a part whose base is not there yet shakes and says what it needs ·
    from the base up → the win → «ليش؟» + the countdown (the video goes on);
(3) ❓ «شو ناقص؟»: the hole, the sad parts · a wrong card says «it is in the picture» · the right one comes back, the next round, the win;
(4) 🎥 «جولة الكاميرا»: a film, not a game: the video plays it by itself, one part per step, the camera close on it;
(5) 🔗 a link opens the page RIGHT AT a scene (?lesson=…&concept=…&at=…&kind=…): the answer of «ask a question»;
(6) 📱 the phone: the new scenes and the looks fit (no sideways scroll) · no JS error.
python tests_browser/test_batch42.py"""
import json, pathlib, re, sys, urllib.parse
from playwright.sync_api import sync_playwright
HERE = pathlib.Path(__file__).resolve().parent
PAGE = HERE.parent / "player" / "explain.html"; URL = PAGE.as_uri()
data = json.loads(PAGE.read_text(encoding="utf-8").split("const DATA = ", 1)[1].split(";\nconst $", 1)[0])
res, errs = [], []
def ok(n, c, x=""): res.append(("✅" if c else "❌") + " " + n + ("" if c else " " + str(x)[:400]))
LOOKS = {"journey": ["road", "river", "rail", "space"], "tower": ["blocks", "castle", "books"], "compare": ["venn", "baskets", "houses"], "assemble": ["shadows", "frames", "sky"]}
DECO = {"river": ".sk-water", "rail": ".sk-rails", "space": ".sk-stars", "castle": ".sk-battle", "books": ".sk-shelf", "baskets": ".sk-cmp", "houses": ".sk-cmp", "frames": ".sk-asm", "sky": ".sk-asm"}
ST = """({turn:!!document.getElementById('turn'),go:!!document.getElementById('goNext'),play:!(document.getElementById('play')||{hidden:true}).hidden,
  pressed:(document.getElementById('play')||{getAttribute:()=>''}).getAttribute('aria-pressed'),cap:(document.getElementById('cap')||{}).textContent||'',
  why:!(document.getElementById('why')||{hidden:true}).hidden,skin:(document.getElementById('xs')||{dataset:{}}).dataset.skin||'',kind:(document.getElementById('xs')||{getAttribute:()=>''}).getAttribute('class')||''})"""


def lesson_scene(kind):
    """(book index, lesson, the lesson-level scene) for a «parts» kind"""
    for gi, g in enumerate(data["graphs"]):
        for l in g["lessons"]:
            a = l.get("assemble") or {}
            if a.get("kind") == kind:
                return gi, l, a, [k for k in ("overview", "world", "assemble") if l.get(k)].index("assemble")


def concept_scene(kind):
    for gi, g in enumerate(data["graphs"]):
        for l in g["lessons"]:
            for c in l["concepts"]:
                ks = [s["kind"] for s in c["scenes"]]
                if kind in ks:
                    return gi, l, c, ks.index(kind)


def link(gi, l, at, kind, concept=None, **kw):
    q = {"q": "hi", "book": gi, "lesson": l["lesson_id"], "at": at, "kind": kind}
    if concept:
        q["concept"] = concept
    q.update(kw)
    return URL + "?" + urllib.parse.urlencode(q)


def new(b, **kw):
    ctx = b.new_context(viewport=kw.pop("viewport", {"width": 1150, "height": 1000}), **kw); pg = ctx.new_page(); pg.route("**/fonts.*/**", lambda r: r.abort())
    pg.on("pageerror", lambda e: errs.append(str(e)[:200])); pg.clock.install(); return ctx, pg


def go(pg, url):
    pg.goto(url); pg.clock.run_for(800)


with sync_playwright() as p:
    b = p.chromium.launch()
    # ---------- (1) the looks ----------
    ctx, pg = new(b)
    for kind, looks in LOOKS.items():
        if kind == "assemble":
            gi, l, s, at = lesson_scene("assemble"); cid = None
        else:
            gi, l, c, at = concept_scene(kind); cid = c["concept_id"]
        drawn = []
        for lk in looks:
            go(pg, link(gi, l, at, kind, cid, skin=lk)); st = pg.evaluate(ST)
            deco = pg.locator(f"#xs {DECO[lk]}").count() if lk in DECO else 1
            drawn.append((lk, st["skin"] == lk and deco > 0))
        ok(f"🎨 {kind}: every look draws ({' · '.join(looks)})", all(d for _, d in drawn), drawn)
    # the look follows the book / lesson / concept, and changes between lessons
    seen = {k: set() for k in LOOKS}
    for gi, g in enumerate(data["graphs"]):
        for l in g["lessons"]:
            a = l.get("assemble") or {}
            if a.get("kind") == "assemble":
                go(pg, link(gi, l, [k for k in ("overview", "world", "assemble") if l.get(k)].index("assemble"), "assemble")); seen["assemble"].add(pg.evaluate(ST)["skin"])
            for c in l["concepts"]:
                for i, s in enumerate(c["scenes"]):
                    if s["kind"] in ("journey", "tower", "compare") and len(seen[s["kind"]]) < 3:
                        go(pg, link(gi, l, i, s["kind"], c["concept_id"])); seen[s["kind"]].add(pg.evaluate(ST)["skin"])
    ok("🎨 across the 12 books every one of the four games shows more than one look (lesson after lesson)", all(len(v) >= 2 for v in seen.values()), seen)
    # the game still works in a look: the journey on the river, the tower as a castle
    gi, l, c, at = concept_scene("journey"); s = c["scenes"][at]
    go(pg, link(gi, l, at, "journey", c["concept_id"], skin="river"))
    for k in range(len(s["route"]) - 1):
        pg.click(f'.na-opt[data-id="{s["route"][k + 1]}"]'); pg.clock.run_for(1900)
    pg.clock.run_for(1500)
    ok("🎨 the journey on the river: the boat sails to the last station and he wins (the game is the same)", pg.locator(".gx-end").count() == 1 and pg.locator("#trav .sk-trav").count() == 1)
    gi, l, c, at = concept_scene("tower"); s = c["scenes"][at]
    go(pg, link(gi, l, at, "tower", c["concept_id"], skin="castle"))
    for k in range(len(s["blocks"])):
        pg.click(f'#xs .g4-brick[data-i="{k}"]'); pg.clock.run_for(1600)
    pg.clock.run_for(800)
    flag = pg.evaluate("getComputedStyle(document.querySelector('#xs .sk-flag')).opacity")
    ok("🎨 the castle: built from the base up → the flag goes up", pg.locator(".gx-end").count() == 1 and float(flag) > 0.5, flag)
    ctx.close()
    # ---------- (2) 🌱 build it from the ground up ----------
    gi, l, s, at = lesson_scene("build_up")
    ctx, pg = new(b); go(pg, link(gi, l, at, "build_up")); st = pg.evaluate(ST)
    ok("🌱 «ابنيها من تحت» opens closed: «🖐️ دورك», no ▶", st["turn"] and not st["play"] and "p42-build" in st["kind"], st)
    top = s["order"][-1]
    pg.click(f'#xs .p42-piece[data-id="{top}"]'); pg.clock.run_for(700); st = pg.evaluate(ST)
    ok("🌱 a part whose base is not there yet: it shakes and says what it needs under it", "تحته أول" in st["cap"] and pg.locator("#xs .p42-piece.placed").count() == 0, st["cap"])
    for cid in s["order"]:
        pg.click(f'#xs .p42-piece[data-id="{cid}"]'); pg.clock.run_for(900)
    for _ in range(20):
        pg.clock.run_for(300)
        if pg.evaluate(ST)["go"]: break
    st = pg.evaluate(ST)
    ok(f"🌱 from the base up ({len(s['order'])} parts) → the win, «ليش؟», the countdown (the video goes on)", pg.locator("#xs .p42-piece.placed").count() == len(s["order"]) and pg.locator(".gx-end").count() == 1 and st["why"] and st["go"], st)
    ok("🌱 the arrows of the whole lesson are lit at the end", pg.locator("#p42Edges .xedge.lit").count() == len(s["edges"]))
    ctx.close()
    # ---------- (3) ❓ what's missing ----------
    gi, l, s, at = lesson_scene("missing")
    ctx, pg = new(b); go(pg, link(gi, l, at, "missing")); st = pg.evaluate(ST)
    R = s["rounds"][0]
    ok("❓ «شو ناقص؟» opens closed, with the hole and the part hidden", st["turn"] and not st["play"] and pg.locator("#xs .p42-hole").count() == 1
       and pg.locator(f'#xs .xnode[data-id="{R["id"]}"].g36-hidden').count() == 1, st)
    wrong = next(o for o in R["options"] if o != R["id"])
    pg.click(f'#p42Opts .na-opt[data-id="{wrong}"]'); pg.clock.run_for(300); st = pg.evaluate(ST)
    ok("❓ a wrong card: «it is in the picture», look for the empty place", "بالصورة" in st["cap"], st["cap"])
    for r in s["rounds"]:
        pg.click(f'#p42Opts .na-opt[data-id="{r["id"]}"]'); pg.clock.run_for(2000)
    for _ in range(20):
        pg.clock.run_for(300)
        if pg.evaluate(ST)["go"]: break
    st = pg.evaluate(ST)
    ok(f"❓ every round ({len(s['rounds'])}): the part comes back, nobody is sad, the win and the countdown",
       pg.locator("#xs .g36-hidden").count() == 0 and pg.locator("#xs .xnode.tired").count() == 0 and pg.locator(".gx-end").count() == 1 and st["go"], st)
    ctx.close()
    # ---------- (4) 🎥 the camera tour ----------
    gi, l, s, at = lesson_scene("tour")
    ctx, pg = new(b); go(pg, link(gi, l, at, "tour")); st = pg.evaluate(ST)
    ok("🎥 «جولة الكاميرا» is a film: the video plays it (▶ there, no «🖐️ دورك»)", st["play"] and st["pressed"] == "true" and not st["turn"], st)
    caps = set()
    for _ in range(60):
        pg.clock.run_for(1000); c = pg.evaluate(ST)["cap"]
        if c.startswith("📍"): caps.add(c[:30])
        if pg.evaluate(ST)["go"]: break
    ok(f"🎥 it walks up the parts by itself, one per step ({len(caps)} of {len(s['order'])})", len(caps) >= len(s["order"]) - 1, caps)
    ctx.close()
    # ---------- (5) the link to a scene ----------
    gi, l, c, at = concept_scene("what_if")
    ctx, pg = new(b); go(pg, link(gi, l, at, "what_if", c["concept_id"]))
    ok("🔗 ?lesson=…&concept=…&at=…&kind=… opens the page right at that scene", pg.locator("#xs .xswitch, .xswitch").count() >= 1 or "شو لو" in pg.inner_text("#prog"), pg.evaluate(ST))
    ctx.close()
    # ---------- (6) the phone ----------
    ctx, pg = new(b, viewport={"width": 390, "height": 844}, has_touch=True, is_mobile=True); wide = []
    for kind in ("build_up", "missing", "tour"):
        gi, l, s, at = lesson_scene(kind); go(pg, link(gi, l, at, kind))
        w = pg.evaluate("[document.documentElement.scrollWidth, innerWidth]")
        if w[0] > w[1] + 1: wide.append((kind, w))
    for kind, looks in LOOKS.items():
        if kind == "assemble":
            gi, l, s, at = lesson_scene("assemble"); cid = None
        else:
            gi, l, c, at = concept_scene(kind); cid = c["concept_id"]
        for lk in looks:
            go(pg, link(gi, l, at, kind, cid, skin=lk)); w = pg.evaluate("[document.documentElement.scrollWidth, innerWidth]")
            if w[0] > w[1] + 1: wide.append((kind, lk, w))
    ok("📱 the phone: the three new scenes and every look fit (no sideways scroll)", not wide, wide)
    ctx.close()
    b.close()

print("\n".join(res))
print(f"✅ {sum(r.startswith('✅') for r in res)} checks passed · ❌ {sum(r.startswith('❌') for r in res)} failed")
print("JS errors:", errs[:5] or "none")
