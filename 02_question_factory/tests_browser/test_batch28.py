"""🆕 batch 28 in a real browser: (1) on the PHONE the concepts of one row go right → left (number 1 on the right),
(2) turning the phone keeps what the student did, (3) the arrow word by subject (batch 33: in the concept cartoon's subtitles), (4) each concept its own drawing.
python tests_browser/test_batch28.py"""
import json, pathlib, urllib.parse, urllib.request
from playwright.sync_api import sync_playwright
HERE = pathlib.Path(__file__).resolve().parent
URL = (HERE.parent / "player" / "explain.html").as_uri()
html = open(urllib.request.url2pathname(urllib.parse.urlparse(URL).path), encoding="utf-8").read()
data = json.loads(html.split("const DATA = ")[1].split(";\nconst $")[0])
res, errs = [], []
def ok(n, c, x=""): res.append(("✅" if c else "❌") + " " + n + ("" if c else " " + str(x)))
POS = """(sel)=>[...document.querySelectorAll(sel)].map(n=>{const t=(n.getAttribute('transform')||'').match(/translate\\(([-\\d.]+)[ ,]+([-\\d.]+)/);return t?{id:n.dataset.id||'',x:+t[1],y:+t[2]}:null;}).filter(Boolean)"""
NUMS = """()=>[...document.querySelectorAll('#xs .xnum')].map(g=>{const t=g.getAttribute('transform').match(/translate\\(([-\\d.]+) ([-\\d.]+)/);return {n:+g.textContent,x:+t[1],y:+t[2]};})"""
def gi(title):
    return next(i for i, g in enumerate(data["graphs"]) if title in g["title"])
def open_lesson(pg, g, l, c=-1):
    pg.click(f'#side .les[data-g="{g}"][data-l="{l}"]', force=True); pg.wait_for_timeout(250)
    pg.click(f'#prog .pstop[data-c="{c}"]', force=True); pg.wait_for_timeout(450)
with sync_playwright() as p:
    b = p.chromium.launch()
    # ---------- (1) phone: number 1 on the RIGHT in every row of the big picture ----------
    pg = b.new_page(viewport={"width": 390, "height": 844}); pg.route("**/fonts.*/**", lambda r: r.abort()); pg.on("pageerror", lambda e: errs.append(str(e)[:150]))
    pg.goto(URL); pg.wait_for_timeout(500)
    rows_checked = 0
    for g, gr in enumerate(data["graphs"]):
        for l in range(len(gr["lessons"])):
            open_lesson(pg, g, l)
            nums = pg.evaluate(NUMS); rows = {}
            for m in nums: rows.setdefault(round(m["y"]), []).append(m)
            for y, ms in rows.items():
                if len(ms) > 1:
                    rows_checked += 1
                    ms.sort(key=lambda m: m["n"])
                    ok(f"phone big picture {gr['title']} lesson {l+1}: numbers go right → left", all(ms[i]["x"] > ms[i + 1]["x"] for i in range(len(ms) - 1)), [(m["n"], m["x"]) for m in ms])
    ok(f"phone: rows with 2+ concepts checked ({rows_checked})", rows_checked >= 5, rows_checked)
    # the same on the computer stays as it was (columns right → left, top → bottom)
    pc = b.new_page(viewport={"width": 1250, "height": 1000}); pc.route("**/fonts.*/**", lambda r: r.abort()); pc.on("pageerror", lambda e: errs.append(str(e)[:150]))
    pc.goto(URL); pc.wait_for_timeout(500); open_lesson(pc, 0, 0)
    n = sorted(pc.evaluate(NUMS), key=lambda m: m["n"])
    ok("computer big picture unchanged: number 1 is the rightmost column", n[0]["x"] == max(m["x"] for m in n))
    # ---------- (2) turning the phone ----------
    open_lesson(pg, 0, 0)
    pg.evaluate("document.getElementById('xs').setAttribute('data-mark','1')")
    pg.set_viewport_size({"width": 844, "height": 390}); pg.wait_for_timeout(700)
    ok("turned BEFORE doing anything → drawn again in the new layout", pg.locator("#xs[data-mark]").count() == 0 and float(pg.evaluate("document.getElementById('xs').viewBox.baseVal.width")) > 400)
    pg.set_viewport_size({"width": 390, "height": 844}); pg.wait_for_timeout(700)
    pg.evaluate("document.getElementById('xs').setAttribute('data-mark','1')")
    pg.locator("#xs .xnode").first.click(force=True); pg.wait_for_timeout(300)       # the student does something
    pg.set_viewport_size({"width": 844, "height": 390}); pg.wait_for_timeout(700)
    ok("turned AFTER doing something → the work stays (same drawing)", pg.locator("#xs[data-mark]").count() == 1)
    ok("…and the tall layout is kept at a good size", pg.locator(".xwrap.laykeep").count() == 1 and pg.evaluate("document.getElementById('xs').getBoundingClientRect().width") <= 445)
    pg.set_viewport_size({"width": 390, "height": 844}); pg.wait_for_timeout(700)
    ok("turned back → normal again, still the same work", pg.locator("#xs[data-mark]").count() == 1 and pg.locator(".xwrap.laykeep").count() == 0)
    pg.click("#next", force=True); pg.wait_for_timeout(500)
    # ---------- (3) the arrow word by subject ----------
    for title, word in (("الرياضيات · الصف الرابع", "مبني على"), ("التاريخ", "بسبب"), ("العلوم", "بيحتاج")):
        try:
            g = gi(title)
        except StopIteration:
            ok(f"book {title} exists", False); continue
        spot = next(((li, ci) for li, l in enumerate(data["graphs"][g]["lessons"]) for ci, c in enumerate(l["concepts"])
                     if c["scenes"][0]["kind"] == "meet" and c["scenes"][0].get("ins")), None)
        open_lesson(pc, g, *spot)
        # batch 33: «تعرّف عليّ» is the concept's cartoon → read every subtitle along its timeline (seek is exact: frame(t))
        subs = pc.evaluate("""()=>{const c=window.stCtl;if(!c)return [];c.pause();const out=new Set();
          for(let t=0;t<=c.DUR;t+=0.4){c.seek(t);const s=document.getElementById('stSub');if(s&&s.textContent.trim())out.add(s.textContent.trim());}return [...out];}""")
        forms = {"مبني على": ("مبني على", "مبنية على", "مبنيين على"), "بسبب": ("بسبب",), "بيحتاج": ("بيحتاج", "بتحتاج")}   # + the feminine / plural (batch 33)
        other = [f for w, fs in forms.items() if w != word for f in fs]
        said = [x for x in subs if any(f in x for f in forms[word])]; wrong = [x for x in subs if any(w in x for w in other)]
        ok(f"arrow word in «{title}» = «{word}» (the concept cartoon says it, never another subject's word)", bool(said) and not wrong, (said[:2], wrong[:2]))
    # ---------- (4) each concept its own drawing (Arabic, physics 6, chemistry 7) ----------
    for title in ("اللغة العربية", "الفيزياء · الصف السادس", "الكيمياء · الصف السابع"):
        g = gi(title); icons = {}
        for l in data["graphs"][g]["lessons"]:
            icons.update({k: v for k, v in l.get("icons", {}).items() if not str(v).startswith("subj:")})
        ok(f"{title}: every drawn concept has its own drawing", len(icons) == len(set(icons.values())), icons)
        open_lesson(pc, g, 0)
        ok(f"{title}: the drawings are on the page (no empty character)", pc.locator("#xs .xnode svg.ch").count() >= 2)
    b.close()
print("\n".join(r for r in res if r.startswith("❌")) or "")
print(f"✅ {sum(r.startswith('✅') for r in res)} checks passed · ❌ {sum(r.startswith('❌') for r in res)} failed")
print("JS errors:", errs or "none")
