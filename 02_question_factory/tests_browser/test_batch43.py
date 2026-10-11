"""🆕 batch 43 (Hareth: «ممكن تزيد لي فعالية فعاليتين جداد») in a real browser, FAKE CLOCK — the two new activities of the concepts
with few scenes:
(1) 🕵️ «مين أنا؟»: opens closed («🖐️ دورك», no ▶) · the «؟» hides the character, two clues show · a wrong card is crossed out, says what
    THAT one is and opens one more clue · the right card: the «؟» opens, the character jumps out, the win, «ليش؟» + the countdown;
(2) 🧩 «ركّب الجملة»: opens closed · a wrong first piece shakes and says «look for the start» (nothing is placed) · the pieces in order
    fill the line → the whole sentence, the win and the countdown;
(3) 📱 the phone: both fit (no sideways scroll) · no JS error. Screenshots: SHOTS (computer + phone).
python tests_browser/test_batch43.py [shots folder]"""
import json, pathlib, sys, urllib.parse
from playwright.sync_api import sync_playwright
HERE = pathlib.Path(__file__).resolve().parent
PAGE = HERE.parent / "player" / "explain.html"; URL = PAGE.as_uri()
SHOTS = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else None
data = json.loads(PAGE.read_text(encoding="utf-8").split("const DATA = ", 1)[1].split(";\nconst $", 1)[0])
res, errs = [], []
def ok(n, c, x=""): res.append(("✅" if c else "❌") + " " + n + ("" if c else " " + str(x)[:400]))
ST = """({turn:!!document.getElementById('turn'),go:!!document.getElementById('goNext'),play:!(document.getElementById('play')||{hidden:true}).hidden,
  cap:(document.getElementById('cap')||{}).textContent||'',why:!(document.getElementById('why')||{hidden:true}).hidden,
  kind:(document.getElementById('xs')||{getAttribute:()=>''}).getAttribute('class')||''})"""


def concept_scene(kind, pick=0):
    found = []
    for gi, g in enumerate(data["graphs"]):
        for l in g["lessons"]:
            for c in l["concepts"]:
                ks = [s["kind"] for s in c["scenes"]]
                if kind in ks:
                    found.append((gi, l, c, ks.index(kind)))
    return found[pick % len(found)] if found else None


def link(gi, l, at, kind, concept):
    return URL + "?" + urllib.parse.urlencode({"q": "hi", "book": gi, "lesson": l["lesson_id"], "at": at, "kind": kind, "concept": concept})


def new(b, **kw):
    ctx = b.new_context(viewport=kw.pop("viewport", {"width": 1150, "height": 1000}), **kw); pg = ctx.new_page(); pg.route("**/fonts.*/**", lambda r: r.abort())
    pg.on("pageerror", lambda e: errs.append(str(e)[:200])); pg.clock.install(); return ctx, pg


def go(pg, url):
    pg.goto(url); pg.clock.run_for(800)


def shot(pg, name):
    if SHOTS:
        SHOTS.mkdir(parents=True, exist_ok=True); pg.screenshot(path=str(SHOTS / name), full_page=True)


def wait_go(pg):
    for _ in range(25):
        pg.clock.run_for(300)
        if pg.evaluate(ST)["go"]:
            break


with sync_playwright() as p:
    b = p.chromium.launch()
    kinds = {k: sum(1 for g in data["graphs"] for l in g["lessons"] for c in l["concepts"] for s in c["scenes"] if s["kind"] == k) for k in ("who_am_i", "sentence")}
    ok(f"🆕 both new activities are in the 12 books (🕵️ {kinds['who_am_i']} · 🧩 {kinds['sentence']})", all(kinds.values()), kinds)
    # ---------- (1) 🕵️ who am I ----------
    gi, l, c, at = concept_scene("who_am_i"); s = c["scenes"][at]; cid = c["concept_id"]
    ctx, pg = new(b); go(pg, link(gi, l, at, "who_am_i", cid)); st = pg.evaluate(ST)
    ok("🕵️ «مين أنا؟» opens closed: «🖐️ دورك», no ▶", st["turn"] and not st["play"] and "w43-who" in st["kind"], st)
    hidden = pg.evaluate(f"getComputedStyle(document.querySelector('#xs .xnode[data-id=\"{cid}\"]')).visibility")
    ok(f"🕵️ the «؟» hides the character, {s['start']} clues show", hidden == "hidden" and pg.locator("#xs .w43-mys").count() == 1
       and pg.locator(".w43-clue.on").count() == min(s["start"], len(s["clues"])), (hidden, pg.locator(".w43-clue.on").count()))
    name = data["graphs"][gi]["names"][cid]
    ok("🕵️ the top bar does not give the answer away (its name and picture wait behind «؟»)",
       name not in pg.inner_text("#prog .where") and pg.locator("#prog .pstop.on.w43-mask").count() == 1, pg.inner_text("#prog .where"))
    shot(pg, "who_1_start.png")
    wrong = next(o for o in s["options"] if not o["ok"])
    pg.click(f'#w43Opts .na-opt[data-id="{wrong["id"]}"]'); pg.clock.run_for(400); st = pg.evaluate(ST)
    more = len(s["clues"]) > s["start"]
    ok("🕵️ a wrong card: crossed out, says what THAT one is" + (" and opens one more clue" if more else ""),
       pg.locator(f'#w43Opts .na-opt.na-wrong[data-id="{wrong["id"]}"]').count() == 1 and data["graphs"][gi]["names"][wrong["id"]] in st["cap"]
       and pg.locator(".w43-clue.on").count() == min(len(s["clues"]), s["start"] + (1 if more else 0)), st["cap"])
    shot(pg, "who_2_wrong.png")
    pg.click(f'#w43Opts .na-opt[data-id="{cid}"]'); wait_go(pg); st = pg.evaluate(ST)
    vis = pg.evaluate(f"getComputedStyle(document.querySelector('#xs .xnode[data-id=\"{cid}\"]')).visibility")
    ok("🕵️ the right card: the «؟» opens, the character jumps out, every clue shows, the win, «ليش؟» and the countdown",
       vis == "visible" and pg.locator("#xs .w43-mys.w43-gone").count() == 1 and pg.locator(".w43-clue.on").count() == len(s["clues"])
       and pg.locator(".gx-end").count() == 1 and st["why"] and st["go"], (vis, st))
    ok("🕵️ found: the top bar shows its name again", name in pg.inner_text("#prog .where") and pg.locator("#prog .w43-mask").count() == 0, pg.inner_text("#prog .where"))
    shot(pg, "who_3_win.png")
    ctx.close()
    # ---------- (2) 🧩 build the sentence ----------
    gi, l, c, at = concept_scene("sentence"); s = c["scenes"][at]; cid = c["concept_id"]
    ctx, pg = new(b); go(pg, link(gi, l, at, "sentence", cid)); st = pg.evaluate(ST)
    ok("🧩 «ركّب الجملة» opens closed: «🖐️ دورك», no ▶", st["turn"] and not st["play"] and "s43-sen" in st["kind"], st)
    first_idx = [int(x) for x in pg.eval_on_selector_all("#s43Tray .s43-chunk", "bs=>bs.map(b=>b.dataset.i)")]
    ok(f"🧩 {len(s['chunks'])} pieces, mixed up (not already in order)", sorted(first_idx) == list(range(len(s["chunks"]))) and first_idx != sorted(first_idx), first_idx)
    shot(pg, "sentence_1_start.png")
    bad = next(i for i, ch in enumerate(s["chunks"]) if ch != s["chunks"][0])
    pg.click(f'#s43Tray .s43-chunk[data-i="{bad}"]'); pg.clock.run_for(300); st = pg.evaluate(ST)
    ok("🧩 a wrong first piece: it shakes, «look for the start», nothing is placed", "بداية" in st["cap"] and pg.locator(".s43-slot.on").count() == 0, st["cap"])
    for i in range(len(s["chunks"])):
        pg.click(f'#s43Tray .s43-chunk[data-i="{i}"]'); pg.clock.run_for(400)
    wait_go(pg); st = pg.evaluate(ST)
    line = pg.inner_text("#s43Line")
    ok("🧩 the pieces in order: the whole sentence, the win, «ليش؟» and the countdown",
       pg.locator(".s43-slot.on").count() == len(s["chunks"]) and " ".join(line.split()) == " ".join(s["sentence"].split())
       and pg.locator(".gx-end").count() == 1 and st["why"] and st["go"], (line, st))
    shot(pg, "sentence_2_win.png")
    ctx.close()
    # ---------- (3) the phone ----------
    ctx, pg = new(b, viewport={"width": 390, "height": 844}, has_touch=True, is_mobile=True); wide = []
    for kind in ("who_am_i", "sentence"):
        for k in range(3):
            gi, l, c, at = concept_scene(kind, k); go(pg, link(gi, l, at, kind, c["concept_id"]))
            w = pg.evaluate("[document.documentElement.scrollWidth, innerWidth]")
            if w[0] > w[1] + 1:
                wide.append((kind, c["title"], w))
            if k == 0:
                shot(pg, f"phone_{kind}.png")
    ok("📱 the phone: both new activities fit (no sideways scroll)", not wide, wide)
    ctx.close()
    b.close()

ok("no JS error", not errs, errs[:3])
print("\n".join(res))
print(f"✅ {sum(r.startswith('✅') for r in res)} checks passed · ❌ {sum(r.startswith('❌') for r in res)} failed")
print("JS errors:", errs[:5] or "none")
