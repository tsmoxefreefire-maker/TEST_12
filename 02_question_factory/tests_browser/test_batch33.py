"""🆕 batch 33 (Hareth: «كل مشهد يتحرك SVG زي الفيديو… لكل مفهوم… حتى لو احط مادة جديدة») in a real browser:
(1) EVERY concept of the 12 books opens with its own cartoon «🎬 تعرّف عليّ» (no error, a real length);
(2) the truth: its arrows are EXACTLY the concept's «needs» in the graph (what it needs + who needs it), nothing invented;
(3) it plays like a video: the concept walks in, each helper walks over and GIVES (a glowing ball), the arrow is drawn;
(4) «what if…?»: the concept leaves, the ones who need it turn grey · the summary says only what the graph says;
(5) at the end the video goes on by itself; the secondary hears its own words («بيعتمد على»);
(6) a NEW subject (a book the page has never seen: «الحاسوب») → a cartoon for every concept, automatically, no code;
(7) the phone: no sideways scroll, everyone inside the picture.
python tests_browser/test_batch33.py"""
import json, os, pathlib, sys, tempfile, urllib.parse, urllib.request
from playwright.sync_api import sync_playwright
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parent / "player"))
URL = (HERE.parent / "player" / "explain.html").as_uri()
html = open(urllib.request.url2pathname(urllib.parse.urlparse(URL).path), encoding="utf-8").read()
data = json.loads(html.split("const DATA = ")[1].split(";\nconst $")[0])
res, errs = [], []
def ok(n, c, x=""): res.append(("✅" if c else "❌") + " " + n + ("" if c else " " + str(x)[:300]))
KIND = "(document.querySelector('.st-screen')||{dataset:{}}).dataset.kind||null"
LINKS = "[...document.querySelectorAll('#xs .st-link')].map(p=>[p.dataset.a,p.dataset.b])"
SUBS = """()=>{const c=window.stCtl;c.pause();const out=[];let last='';
  for(let t=0;t<=c.DUR;t+=0.4){c.seek(t);const s=(document.getElementById('stSub')||{}).textContent||'';if(s.trim()&&s.trim()!==last){last=s.trim();out.push(last);}}return out;}"""


def want_links(m):
    """What the cartoon may draw: «X needs a» for its ins (≤3) and «o needs X» for its outs (≤3) — straight from «تعرّف عليّ»."""
    return {(a, m["target"]) for a in m.get("ins", [])[:3]} | {(m["target"], o) for o in m.get("outs", [])[:3]}


def every_concept(pg, graphs, label):
    """Open every concept's first stop; it must be its cartoon, with exactly the graph's arrows and all its characters."""
    n, not_cartoon, wrong, cast, short = 0, [], [], [], []
    for gi, g in enumerate(graphs):
        for li, l in enumerate(g["lessons"]):
            pg.click(f'#side .les[data-g="{gi}"][data-l="{li}"]', force=True); pg.wait_for_timeout(60)
            for ci, c in enumerate(l["concepts"]):
                m = c["scenes"][0] if c["scenes"] else {}
                if m.get("kind") != "meet":
                    continue
                pg.click(f'#prog .pstop[data-c="{ci}"]', force=True); pg.wait_for_timeout(70); n += 1
                if pg.evaluate(KIND) != "cstory":
                    not_cartoon.append((g["title"], c["concept_id"])); continue
                pg.evaluate("window.stCtl&&window.stCtl.pause()")
                links = {tuple(x) for x in pg.evaluate(LINKS)}
                if links != want_links(m):
                    wrong.append((c["concept_id"], sorted(links ^ want_links(m))))
                if pg.locator("#xs .sa").count() != 1 + len(m.get("ins", [])[:3]) + len(m.get("outs", [])[:3]):
                    cast.append(c["concept_id"])
                if float(pg.evaluate("document.querySelector('.st-screen').dataset.dur")) < 10:
                    short.append(c["concept_id"])
    ok(f"{label}: every concept ({n}) opens with its own cartoon 🎬", n > 0 and not not_cartoon, not_cartoon[:4])
    ok(f"{label}: every arrow is exactly the graph's «needs» (nothing invented, nothing missing)", not wrong, wrong[:3])
    ok(f"{label}: the concept + its helpers + the ones who need it are all on stage", not cast, cast[:4])
    ok(f"{label}: every cartoon has a real length", not short, short[:4])
    return n


def new_subject_page(tmp):
    """A book the 12 books are not (examples/new_subject_computer_g7.json, «الحاسوب»): the factory + the page builder, no code change."""
    import explain_main, build_explain_player as bep, lego
    lego.set_store(os.path.join(tmp, "lego_library.json"))           # nothing saved in the project
    gp = str(HERE.parent / "examples" / "new_subject_computer_g7.json"); od = os.path.join(tmp, "explain_out_cs")
    explain_main.run(gp, od)
    packed = bep.pack(gp, od)
    out = os.path.join(tmp, "explain_cs.html")
    open(out, "w", encoding="utf-8").write(bep.page_html([packed]))
    return pathlib.Path(out).as_uri(), packed


with sync_playwright() as p:
    b = p.chromium.launch()
    # ---------- (1) + (2) every concept of the 12 books ----------
    pg = b.new_page(viewport={"width": 1250, "height": 950}); pg.route("**/fonts.*/**", lambda r: r.abort()); pg.on("pageerror", lambda e: errs.append(str(e)[:160]))
    pg.goto(URL); pg.wait_for_timeout(500)
    every_concept(pg, data["graphs"], "12 books")
    # ---------- (5b) the secondary hears its own words ----------
    gs = next(i for i, g in enumerate(data["graphs"]) if g["audience"]["stage"] == "senior")
    spot = next((li, ci) for li, l in enumerate(data["graphs"][gs]["lessons"]) for ci, c in enumerate(l["concepts"])
                if c["scenes"] and c["scenes"][0]["kind"] == "meet" and c["scenes"][0].get("ins"))
    pg.click(f'#side .les[data-g="{gs}"][data-l="{spot[0]}"]', force=True); pg.click(f'#prog .pstop[data-c="{spot[1]}"]', force=True); pg.wait_for_timeout(200)
    subs = pg.evaluate(SUBS)
    ok("the secondary's concept cartoon says «بيعتمد على», never «بيحتاج»", any(("بيعتمد" in s or "بتعتمد" in s) for s in subs) and not any(("بيحتاج" in s or "بتحتاج" in s) for s in subs), subs[:6])
    pg.close()
    # ---------- (3) + (4) + (5) one concept with helpers AND ones who need it, on a fake clock ----------
    g0 = data["graphs"][0]
    li, ci, m = next((li, ci, c["scenes"][0]) for li, l in enumerate(g0["lessons"]) for ci, c in enumerate(l["concepts"])
                     if c["scenes"] and c["scenes"][0]["kind"] == "meet" and c["scenes"][0].get("ins") and c["scenes"][0].get("outs"))
    X = m["target"]; NX = g0["names"][X]
    ctx = b.new_context(viewport={"width": 1250, "height": 950}); pg = ctx.new_page(); pg.route("**/fonts.*/**", lambda r: r.abort()); pg.on("pageerror", lambda e: errs.append(str(e)[:160]))
    pg.clock.install(); pg.goto(URL); pg.clock.run_for(400)
    pg.click(f'#side .les[data-g="0"][data-l="{li}"]', force=True); pg.clock.run_for(200)
    pg.click(f'#prog .pstop[data-c="{ci}"]', force=True); pg.clock.run_for(300)
    ok(f"«{NX}» opens with its cartoon, named after it", pg.evaluate(KIND) == "cstory" and NX in (pg.get_attribute("#xs", "aria-label") or ""), pg.get_attribute("#xs", "aria-label"))
    XPOS = f"(document.querySelector('#xs .sa[data-id=\"{X}\"]')||{{getAttribute:()=>''}}).getAttribute('transform')"
    t0 = pg.inner_text("#stTime"); x0 = pg.evaluate(XPOS)
    pg.clock.run_for(3500)
    ok("it plays by itself: the time runs", pg.inner_text("#stTime") != t0, (t0, pg.inner_text("#stTime")))
    ok(f"«{NX}» walks in (its place changes)", pg.evaluate(XPOS) != x0, (x0, pg.evaluate(XPOS)))
    chap = json.loads(pg.evaluate("document.querySelector('.st-screen').dataset.chap"))
    names = [c[1] for c in chap]
    ok("the chapters: meet it → what it needs → who needs it → what if → the summary", names[1:] == ["تعرّف عليّ", f"شو بيحتاج «{NX}»؟", "مين بيحتاجه؟", "شو لو اختفى؟", "الخلاصة"]
       or (len(names) == 6 and "اختفى" in names[4] and names[5] == "الخلاصة"), names)
    seen_orb = seen_link = False
    for _ in range(160):
        pg.clock.run_for(250)
        seen_orb = seen_orb or pg.evaluate("[...document.querySelectorAll('#xs .st-orb')].some(o=>o.getAttribute('opacity')==='1')")
        seen_link = seen_link or pg.evaluate("[...document.querySelectorAll('#xs .st-link')].some(p=>p.getAttribute('marker-end')&&+p.getAttribute('stroke-dashoffset')<0.05)")
        if seen_orb and seen_link:
            break
    ok("a helper walks over and GIVES it a glowing ball", seen_orb)
    ok("…and the «needs» arrow between them is drawn", seen_link)
    sub = pg.inner_text("#stSub")
    ok("the subtitles name who gives to whom (🆕 batch 37: bold, no «» marks)", "«" not in sub and NX in sub and pg.evaluate("document.querySelectorAll('#stSub b').length") >= 1, sub)
    subs = pg.evaluate(SUBS)                                         # pauses, then reads the whole timeline
    ok("every helper is said by name in the subtitles", all(any(g0["names"][a] in s for s in subs) for a in m["ins"][:3]), subs)
    ok("every one who needs it is said by name too", all(any(g0["names"][o] in s for s in subs) for o in m["outs"][:3]), subs)
    wi = next(t for t, name in chap if "اختفى" in name)
    pg.evaluate(f"window.stCtl.seek({wi + 3.6})")
    gone = pg.evaluate(f"(document.querySelector('#xs .sa[data-id=\"{X}\"]')||{{style:{{}}}}).style.opacity")
    grey = pg.evaluate("[...document.querySelectorAll('#xs .sa.st-gray')].map(g=>g.dataset.id)")
    ok(f"«what if…?»: «{NX}» is gone and the ones who need it turn grey", gone == "0" and grey and set(grey) <= set(m["outs"]), (gone, grey))
    pg.evaluate(f"window.stCtl.seek({wi - 0.3})")                     # everyone on stage, at rest
    who = pg.evaluate("""()=>{const sc=document.querySelector('.st-screen').getBoundingClientRect();return [...document.querySelectorAll('#xs .sa')].map(g=>{const r=g.querySelector('.xnode').getBoundingClientRect();
        return {id:g.dataset.id,x:r.x+r.width/2,y:r.y+r.height/2,in:r.x>sc.x&&r.right<sc.right};}).filter(a=>a.in);}""")
    pg.clock.run_for(4000)
    n0 = pg.evaluate("window.__SOUND.log.length")
    if who:
        pg.mouse.move(who[0]["x"], who[0]["y"]); pg.clock.run_for(500)
    ok("🖱️ pointing at a character in the cartoon → it answers with its sound (nothing see-through in the way)", who and pg.evaluate("window.__SOUND.log.length") > n0, (who[:1], n0, pg.evaluate("window.__SOUND.log.length")))
    pg.mouse.move(5, 5)
    end = next(t for t, name in chap if name == "الخلاصة")
    pg.evaluate(f"window.stCtl.seek({end + 1})"); s_end = pg.inner_text("#stSub")
    ok("the summary says only what the graph says (it + its helpers + who needs it)", NX in s_end and all(g0["names"][a] in s_end for a in m["ins"][:3]) and all(g0["names"][o] in s_end for o in m["outs"][:3]), s_end)
    pg.evaluate(f"window.stCtl.seek({max(0, end - 0.5)})"); pg.evaluate("window.stCtl.play()")
    for _ in range(60):
        pg.clock.run_for(500)
        if pg.evaluate("!!document.getElementById('goNext')") or pg.evaluate(KIND) != "cstory":
            break
    ok("at the end the video goes on by itself (the countdown / the next scene)", pg.evaluate("!!document.getElementById('goNext')") or pg.evaluate(KIND) != "cstory")
    ctx.close()
    # ---------- (6) a NEW subject, never seen before ----------
    with tempfile.TemporaryDirectory() as tmp:
        url, packed = new_subject_page(tmp)
        pg = b.new_page(viewport={"width": 1250, "height": 950}); pg.route("**/fonts.*/**", lambda r: r.abort()); pg.on("pageerror", lambda e: errs.append(str(e)[:160]))
        pg.goto(url); pg.wait_for_timeout(500)
        n = every_concept(pg, [packed], "🆕 new subject «الحاسوب»")
        nc = sum(len(l["concepts"]) for l in packed["lessons"])
        ok(f"🆕 new subject: a cartoon for EVERY concept ({n} of {nc})", n == nc and nc >= 5, (n, nc))
        pg.click('#side .les[data-g="0"][data-l="0"]', force=True); pg.click('#prog .pstop[data-c="0"]', force=True); pg.wait_for_timeout(200)
        subs = pg.evaluate(SUBS)
        ok("🆕 new subject: its cartoon speaks with the book's names", any(any(n in s for n in packed["names"].values()) for s in subs) and len(subs) >= 4, subs[:4])
        pg.close()
    # ---------- (7) the phone ----------
    ctx = b.new_context(viewport={"width": 390, "height": 844}, has_touch=True, is_mobile=True); pg = ctx.new_page(); pg.route("**/fonts.*/**", lambda r: r.abort()); pg.on("pageerror", lambda e: errs.append(str(e)[:160]))
    pg.goto(URL); pg.wait_for_timeout(600)
    pg.click(f'#side .les[data-g="0"][data-l="{li}"]', force=True); pg.wait_for_timeout(200)
    pg.evaluate(f"document.querySelector('#prog .pstop[data-c=\"{ci}\"]').click()"); pg.wait_for_timeout(500)
    pg.evaluate("window.stCtl.pause();window.stCtl.seek(window.stCtl.DUR-0.1)")
    ok("📱 the concept cartoon on the phone: no sideways scroll", pg.evaluate("document.documentElement.scrollWidth") <= 390, pg.evaluate("document.documentElement.scrollWidth"))
    out = pg.evaluate("""()=>{const v=document.getElementById('xs').viewBox.baseVal;return [...document.querySelectorAll('#xs .sa')].filter(g=>{
        const t=(g.getAttribute('transform')||'').match(/translate\\(([-\\d.]+)[ ,]+([-\\d.]+)/);if(!t)return true;const x=+t[1],y=+t[2];return x<20||x>v.width-20||y<20||y>v.height-20;}).map(g=>g.dataset.id);}""")
    ok("📱 everyone stands inside the picture", not out, out)
    ctx.close()
    b.close()
print("\n".join(r for r in res if r.startswith("❌")) or "")
print(f"✅ {sum(r.startswith('✅') for r in res)} checks passed · ❌ {sum(r.startswith('❌') for r in res)} failed")
print("JS errors:", errs or "none")
