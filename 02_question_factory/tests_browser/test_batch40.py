"""🆕 batch 40 in a real browser:
(1) 🐰 THE WAY IT VANISHES FITS THE THING (Hareth: «الأرنب ما بيقدر يمسك التربة… لازم يكون في منطق»): water → a sponge soaks it up,
    sunlight → a cloud covers it, air → a balloon sucks it in, soil → a mole pulls it down, a seed → the rabbit carries it, a river / a force →
    «💭 تخيّلوا لو ما في…» — always: it vanishes, the ones who need it turn grey, somebody calls, it comes back; the agent is never seen before;
(2) 🗣️ the Arabic is right: «يا طيارة ورق! رجّعيه» (a «she»), «طيارة الورق», «الأرض موجودة»;
(3) 🎨 THE LIBRARY OF DRAWINGS in a real lesson of the Saudi curriculum (examples/saudi_science_g4_demo.json): every concept has its drawing
    with OUR face, the book carries only the drawings it uses, and the same drawing twice in a lesson comes in another colour (face untouched);
(4) ⚖️ the page did not get heavier (the library lives outside it).
python tests_browser/test_batch40.py"""
import json, os, pathlib, re, subprocess, sys, tempfile
from playwright.sync_api import sync_playwright
HERE = pathlib.Path(__file__).resolve().parent
F = HERE.parent
sys.path.insert(0, str(F)); sys.path.insert(0, str(F / "player"))
PAGE = F / "player" / "explain.html"
html = PAGE.read_text(encoding="utf-8"); head, rest = html.split("const DATA = ", 1); body, tail = rest.split(";\nconst $", 1)
data = json.loads(body)
res, errs = [], []
def ok(n, c, x=""): res.append(("✅" if c else "❌") + " " + n + ("" if c else " " + str(x)[:400]))
OPEN = "([gi,li])=>{window.stCtl&&window.stCtl.pause();document.querySelector(`#side .les[data-g=\"${gi}\"][data-l=\"${li}\"]`).click();}"
gi_of = lambda st, sj: next(i for i, g in enumerate(data["graphs"]) if g["audience"]["stage"] == st and g["subject"] == sj)
TMP = pathlib.Path(tempfile.mkdtemp())


def page_with(d, name):
    p = TMP / name
    p.write_text(head + "const DATA = " + json.dumps(d, ensure_ascii=False).replace("</", "<\\/") + ";\nconst $" + tail, encoding="utf-8")
    return p.as_uri()


SCAN = """T=>{const c=window.stCtl;c.pause();const th=document.querySelector('#xs .st-thief');const hub=document.querySelector('#xs .st-thief')?null:null;const subs=[],out=[];
  const op=g=>g.style.opacity===''?1:+g.style.opacity;
  for(let t=T;t<T+34&&t<c.DUR;t+=0.25){c.seek(t);const s=(document.getElementById('stSub')||{}).textContent||'';if(!subs.includes(s))subs.push(s);
    const sa=[...document.querySelectorAll('#xs .sa')];const m=th&&/translate\\(([-\\d.]+) /.exec(th.getAttribute('transform'));
    out.push({t:+t.toFixed(2),gone:sa.filter(g=>op(g)<0.3).length,grey:document.querySelectorAll('#xs .sa.st-gray').length,
      th:th?(th.style.opacity===''?1:+th.style.opacity):0,tx:m?+m[1]:-999,bub:[...document.querySelectorAll('#xs .st-bub')].map(g=>g.textContent).join('|')});}
  c.seek(0.5);const a=th?(th.style.opacity===''?1:+th.style.opacity):0,m0=th&&/translate\\(([-\\d.]+) /.exec(th.getAttribute('transform'));
  return {way:th&&th.dataset.way,kind:th&&th.dataset.k,subs,out,start:[a,m0?+m0[1]:-999],W:+document.getElementById('xs').viewBox.baseVal.width};}"""


def twist(pg, gi, li):
    pg.evaluate(OPEN, [gi, li]); pg.wait_for_timeout(120)
    chap = json.loads(pg.evaluate("document.querySelector('.st-screen').dataset.chap"))
    T = next((c[0] for c in chap if c[1] == "المفاجأة"), None)
    return None if T is None else pg.evaluate(SCAN, T)


WAYS = [  # (name for the hub, the way, a word of the «take» line, a word of the «comes back» line)
    ("الماء", "sponge", "نشّفت", "عصرت"), ("ضوء الشمس", "cloud", "غطّت", "تحرّكت"), ("الهواء", "balloon", "شفط", "طلّع"), ("التربة", "mole", "سحب", "رجّع")]

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1150, "height": 950}); pg.route("**/fonts.*/**", lambda r: r.abort()); pg.on("pageerror", lambda e: errs.append(str(e)[:200]))
    gk = gi_of("kids", "science")
    soil = next(k for k, v in data["graphs"][gk]["names"].items() if v == "التربة")
    for name, way, take, back in WAYS:
        d = json.loads(body); d["graphs"][gk]["names"][soil] = name
        pg.goto(page_with(d, f"w_{way}.html") + "?q=hi"); pg.wait_for_timeout(350)
        r = twist(pg, gk, 0)
        o, txt = r["out"], " / ".join(r["subs"])
        wo = [x for x in o if "بدون" in "".join(s for s in r["subs"] if "بدون" in s) and x["grey"] >= 2]
        i_take = next((i for i, s in enumerate(r["subs"]) if take in s), None); i_back = next((i for i, s in enumerate(r["subs"]) if back in s), None)
        ok(f"🧽 «{name}» vanishes the logical way: {way} («{take}» … «{back}»)", r["way"] == way and None not in (i_take, i_back) and i_take < i_back, (r["way"], txt[:300]))
        ok(f"…«{name}»: while it is away the ones who need it are grey, then everybody is back, nobody grey", max(x["gone"] for x in o) >= 1 and max(x["grey"] for x in o) >= 2
           and o[-1]["grey"] == 0 and o[-1]["gone"] == 0, (max(x["gone"] for x in o), max(x["grey"] for x in o), o[-1]))
        ok(f"…«{name}»: the {way} is not in the picture before the twist, nor after it", (r["start"][0] < 0.1 or not (0 < r["start"][1] < r["W"])) and (o[-1]["th"] < 0.1 or not (0 < o[-1]["tx"] < r["W"])), (r["start"], o[-1]))
    pg.goto(PAGE.as_uri() + "?q=hi"); pg.wait_for_timeout(400)
    r = twist(pg, gk, 2)
    ok("🐰 «البذرة» can be held: the rabbit grabs it and runs («خطف»)", r["way"] == "carry" and r["kind"] == "rabbit" and any("خطف" in s for s in r["subs"]), (r["way"], r["kind"]))
    r = twist(pg, gi_of("junior", "history"), 0)
    ok("💭 nobody can carry a river: «تخيّلوا لو اختفى نهر النيل…» → «بس نهر النيل موجود»", r["way"] == "think" and any("تخيّلوا" in s for s in r["subs"]) and any("موجود" in s for s in r["subs"]), r["subs"][:6])
    r = twist(pg, gi_of("junior", "physics"), 0)
    ok("💭 nor a force: «القوة» is imagined away, not grabbed", r["way"] == "think", r["way"])
    r = twist(pg, gi_of("junior", "geography"), 0)
    ok("🗣️ «الأرض» is a «she»: «بس الأرض موجودة، ما اختفت!»", any("الأرض موجودة" in s for s in r["subs"]), [s for s in r["subs"] if "الأرض" in s][:3])
    r = twist(pg, gi_of("kids", "math"), 0)
    ok("🗣️ to a «she» thief: «يا طيارة ورق! رجّعيه…» and «طيارة الورق»", any("رجّعي" in x["bub"] for x in r["out"]) and any("طيارة الورق" in s for s in r["subs"]),
       ([x["bub"] for x in r["out"] if "يا" in x["bub"]][:1], [s for s in r["subs"] if "ورق" in s][:2]))
    pg.close()
    # ---------- (3) the library in a lesson of the Saudi curriculum ----------
    gf = F / "examples" / "saudi_science_g4_demo.json"; od = TMP / "out_sa"
    rr = subprocess.run([sys.executable, str(F / "explain_main.py"), str(gf), str(od)], cwd=str(F), capture_output=True, text=True)
    import build_explain_player as bp
    g = bp.pack(str(gf), str(od))
    used = {v.split("~")[0][4:] for l in g["lessons"] for v in l["icons"].values() if str(v).startswith("lib:")}
    ok("🎨 the Saudi demo book carries ONLY the library drawings it uses", rr.returncode == 0 and set(g.get("artlib", {})) == used and len(used) >= 10, (rr.stderr[-200:], sorted(used)))
    demo = TMP / "demo.html"; demo.write_text(bp.page_html([g]), encoding="utf-8")
    pg = b.new_page(viewport={"width": 1150, "height": 950}); pg.route("**/fonts.*/**", lambda r: r.abort()); pg.on("pageerror", lambda e: errs.append(str(e)[:200]))
    pg.goto(demo.as_uri() + "?q=hi"); pg.wait_for_timeout(400)
    bad = []
    for li, l in enumerate(g["lessons"]):
        for ci, c in enumerate(l["concepts"]):
            pg.evaluate(OPEN, [0, li]); pg.wait_for_timeout(40)
            pg.evaluate(f"window.stCtl&&window.stCtl.pause();document.querySelector('#prog .pstop[data-c=\"{ci}\"]').click()"); pg.wait_for_timeout(60)
            key = l["icons"][c["concept_id"]]
            if not str(key).startswith("lib:"):
                continue
            # its shape only (the page's soft-shading pass rewrites the colours: fill="url(#c36…)")
            first = g["artlib"][key[4:]]["body"].split(" fill=")[0].split(" stroke=")[0][:40]
            got = pg.evaluate("f=>[...document.querySelectorAll('#xs svg.ch')].some(s=>s.innerHTML.includes(f)&&s.querySelector('.sface'))", first)
            if not got:
                bad.append(c["title"])
    ok("🎨 every concept of the Saudi lessons shows its library drawing, with our face", not bad, bad)
    pg.evaluate(OPEN, [0, 1]); pg.wait_for_timeout(100)
    shot = pg.evaluate("[...document.querySelectorAll('#xs .sa')].length")
    ok("🎬 the lesson story of a Saudi lesson plays with its characters", shot >= 5, shot)
    # the same drawing twice in a lesson → another colour, the face as it is
    g2 = json.loads(json.dumps(g)); L = g2["lessons"][1]; cs = [c["concept_id"] for c in L["concepts"]]
    L["icons"][cs[1]] = L["icons"][cs[0]] + "~2"
    d2 = {"graphs": [g2]}; pg.goto(page_with(d2, "variant.html") + "?q=hi"); pg.wait_for_timeout(400)
    pg.evaluate(OPEN, [0, 1]); pg.wait_for_timeout(100)
    v = pg.evaluate("""id=>{const s=[...document.querySelectorAll('#xs .sa')].find(g=>g.dataset.id===id);const svg=s&&s.querySelector('svg.ch');if(!svg)return null;
      const f=svg.querySelector('g[style*="hue-rotate"]');return [!!f,!!svg.querySelector('.sface'),f?!f.querySelector('.sface'):false];}""", cs[1])
    ok("🎨 two concepts of one lesson never look the same: «key~2» = the same drawing in another colour, the face untouched", v == [True, True, True], v)
    pg.close()
    # ---------- 📱 phone ----------
    ctx = b.new_context(viewport={"width": 390, "height": 844}, has_touch=True, is_mobile=True); pg = ctx.new_page(); pg.route("**/fonts.*/**", lambda r: r.abort())
    pg.on("pageerror", lambda e: errs.append(str(e)[:200]))
    pg.goto(demo.as_uri()); pg.wait_for_timeout(500); pg.evaluate(OPEN, [0, 0]); pg.wait_for_timeout(200)
    fit = pg.evaluate("[document.documentElement.scrollWidth,document.querySelectorAll('#xs svg.ch').length]")
    ok("📱 the phone: the Saudi lesson fits (no sideways scroll) and draws its characters", fit[0] <= 391 and fit[1] >= 5, fit)
    ctx.close(); b.close()
size = PAGE.stat().st_size
# 🆕 batch 43: +2 activities (32 scenes, 10 KB of code) → 1.3 MB; what matters: the library (1500+ drawings) is NOT inside, only what the books use
libs = len(set(re.findall(r'"lib:([a-z0-9_]+\.[a-z0-9_]+)', PAGE.read_text(encoding="utf-8"))))
ok(f"⚖️ the page stays light: {size // 1024} KB, with only {libs} library drawings inside (the library of 1500+ stays outside)", size < 1_300_000 and libs < 60, (size, libs))
print("\n".join(r for r in res if r.startswith("❌")) or "")
print(f"✅ {sum(r.startswith('✅') for r in res)} checks passed · ❌ {sum(r.startswith('❌') for r in res)} failed")
print("JS errors:", errs or "none")
