"""🆕 batch 38 (Hareth's idea) in a real browser — the lesson's story:
(1) ONE BY ONE: the hero comes alone, says what it misses, the one it needs comes and gives, then says what IT misses… (any graph:
    the order is made from the graph's «needs» only — checked on made-up graphs too: branches, a diamond, two threads, no links, a loop);
(2) EVERY AGE ITS OWN PICTURE: 🌈 kids = a tale in the place · 🧭 junior = a team of explorers (calmer) · 🔬 teen = an investigation board
    (cards, pins, red strings, a magnifier) · 📐 senior = a documentary diagram that builds itself (one node + one arrow at a time, a camera);
(3) the bubbles of the cartoon: the name in bold, no «» marks (they were left in the teen / secondary bubbles in batch 37).
python tests_browser/test_batch38.py"""
import json, pathlib
from playwright.sync_api import sync_playwright
HERE = pathlib.Path(__file__).resolve().parent
PAGE = HERE.parent / "player" / "explain.html"; URL = PAGE.as_uri()
data = json.loads(PAGE.read_text(encoding="utf-8").split("const DATA = ")[1].split(";\nconst $")[0])
res, errs = [], []
def ok(n, c, x=""): res.append(("✅" if c else "❌") + " " + n + ("" if c else " " + str(x)[:400]))
LOOK = {"kids": "cast", "junior": "cast", "teen": "board", "senior": "doc"}
OPEN = "([gi,li])=>{window.stCtl&&window.stCtl.pause();document.querySelector(`#side .les[data-g=\"${gi}\"][data-l=\"${li}\"]`).click();}"
# when does each character come on stage? (cast: inside the picture · board / doc: it shows)
ENTRY = """()=>{const c=window.stCtl;c.pause();const scr=document.querySelector('.st-screen'),look=scr.dataset.look,W=+document.getElementById('xs').viewBox.baseVal.width;
  const first={};for(let t=0;t<=c.DUR;t+=0.2){c.seek(t);document.querySelectorAll('#xs .sa').forEach(g=>{const id=g.dataset.id;if(first[id]!=null)return;let on;
    if(look==='cast'){const m=/translate\\(([-\\d.]+)/.exec(g.getAttribute('transform')||'');on=m&&+m[1]>-20&&+m[1]<W+20&&g.style.opacity!=='0';}else on=+(g.style.opacity||0)>0.5;
    if(on)first[id]=+t.toFixed(1);});}
  return {look,first,n:document.querySelectorAll('#xs .sa').length,dur:c.DUR};}"""

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1150, "height": 950}); pg.route("**/fonts.*/**", lambda r: r.abort()); pg.on("pageerror", lambda e: errs.append(str(e)[:200]))
    pg.goto(URL); pg.wait_for_timeout(500)
    # ---------- (1) the order, on made-up graphs (any graph) ----------
    CASES = {
        "a chain + a branch + a guest + one alone": {"ids": ["leaf", "stem", "root", "flower"], "guests": ["soil", "water"],
            "edges": [["stem", "leaf"], ["root", "stem"], ["soil", "root"], ["water", "root"]]},
        "a diamond (two need the same one)": {"ids": ["x", "a", "b", "c"], "guests": [], "edges": [["a", "x"], ["b", "x"], ["c", "a"], ["c", "b"]]},
        "two threads": {"ids": ["p", "q", "r", "s"], "guests": [], "edges": [["q", "p"], ["s", "r"]]},
        "no links at all": {"ids": ["u", "v", "w"], "guests": [], "edges": []},
        "a loop in a broken graph (never stuck)": {"ids": ["m", "n"], "guests": [], "edges": [["m", "n"], ["n", "m"]]},
    }
    for name, c in CASES.items():
        s = {"ids": c["ids"], "guests": c["guests"], "edges": c["edges"]}
        P = pg.evaluate("s=>stPlan(s)", s)
        ids = c["guests"] + c["ids"]
        seen, order, bad = {P["hero"]}, [P["hero"]], []
        edges_done = []
        for bt in P["beats"]:
            if bt["t"] == "call":
                if bt["b"] not in seen: bad.append(("called by someone not there", bt))
                for a in bt["as"]:
                    if a in seen: bad.append(("called twice", a))
                    seen.add(a); order.append(a); edges_done.append((a, bt["b"]))
            elif bt["t"] == "link":
                if bt["a"] not in seen or bt["b"] not in seen: bad.append(("link before both are there", bt))
                edges_done.append((bt["a"], bt["b"]))
            elif bt["t"] in ("other", "lone"):
                if bt["id"] in seen: bad.append(("comes twice", bt))
                seen.add(bt["id"]); order.append(bt["id"])
            elif bt["t"] == "ask" and bt["x"] not in seen: bad.append(("asks before it is there", bt))
        real = {tuple(e) for e in c["edges"] if e[0] != e[1]}
        ok(f"🧩 the order works on any graph — {name}: everyone comes once, every «needs» is told once", set(order) == set(ids) and len(order) == len(ids)
           and sorted(edges_done) == sorted(real) and not bad, (order, edges_done, bad))
    P = pg.evaluate("s=>stPlan(s)", {"ids": ["leaf", "stem", "root", "flower"], "guests": ["soil", "water"], "edges": CASES["a chain + a branch + a guest + one alone"]["edges"]})
    kinds = [x["t"] for x in P["beats"]]
    ok("🧩 the hero is the end of the longest chain, it asks first, the base comes last in the chain, the one alone at the very end",
       P["hero"] == "leaf" and kinds[0] == "ask" and P["beats"][1] == {"t": "call", "as": ["stem"], "b": "leaf"} and P["beats"][-1] == {"t": "lone", "id": "flower"}
       and P["chain"] in (["soil", "root", "stem", "leaf"], ["water", "root", "stem", "leaf"]), P)
    grp = next((x for x in P["beats"] if x["t"] == "call" and len(x["as"]) > 1), None)
    ok("🧩 two things with nothing behind them (soil, water) that the same one needs come TOGETHER (the tale never drags)", grp and sorted(grp["as"]) == ["soil", "water"] and grp["b"] == "root", P["beats"])
    # ---------- (1)+(2) every lesson of every book: one by one, and its age's picture ----------
    bad_look, bad_one, n_les = [], [], 0
    for gi, g in enumerate(data["graphs"]):
        st = g["audience"]["stage"]
        for li, l in enumerate(g["lessons"]):
            pg.evaluate(OPEN, [gi, li]); pg.wait_for_timeout(60); n_les += 1
            e = pg.evaluate(ENTRY)
            if e["look"] != LOOK[st]: bad_look.append((g["title"], st, e["look"]))
            times = sorted(e["first"].values())
            hero_t = times[0] if times else None
            alone = sum(1 for x in times if x == hero_t) == 1
            # one by one: never more than 3 (a small group of guests) come within one second
            crowd = max((sum(1 for y in times if x <= y < x + 1.0) for x in times), default=0)
            party = pg.evaluate("document.querySelector('.st-screen').dataset.tale") == "party"   # 🆕 batch 45: «the gathering» — everybody is there from the start (test_batch45.py)
            if len(e["first"]) != e["n"] or (not party and (not alone or crowd > 3)):
                bad_one.append((g["title"], l["lesson_title"], e["n"], len(e["first"]), alone, crowd))
    ok(f"🎨 every lesson ({n_les}) has its age's picture (kids/junior: the place · teen: the board · senior: the diagram)", not bad_look, bad_look[:4])
    ok("👣 in every lesson the hero comes ALONE first, the others one by one (at most a small group of 3 together), and nobody is missing", not bad_one, bad_one[:4])
    # ---------- 🌈 kids: the plants tale ----------
    gk = next(i for i, g in enumerate(data["graphs"]) if g["audience"]["stage"] == "kids" and g["subject"] == "science")
    pg.evaluate(OPEN, [gk, 0]); pg.wait_for_timeout(200)
    subs = pg.evaluate("""()=>{const c=window.stCtl;c.pause();const out=[];let last='';for(let t=0;t<=c.DUR;t+=0.25){c.seek(t);const s=document.getElementById('stSub').textContent.trim();if(s&&s!==last){last=s;out.push(s);}}return out;}""")
    asks = [i for i, x in enumerate(subs) if "ناقص" in x]; comes = [i for i, x in enumerate(subs) if "إجى" in x or "إجت" in x or "إجوا" in x]
    ok("🌈 kids: «…ناقصها إشي» → «وفجأة… إجى…» → «…ناقصه إشي» → … (each one says what it misses, then the next one comes)",
       len(asks) >= 3 and len(comes) >= 3 and all(any(a < c for a in asks) for c in comes) and asks[0] < comes[0] < asks[1] < comes[1], subs[:12])
    bubs = pg.evaluate("""()=>{const c=window.stCtl;c.pause();const out=new Set();for(let t=0;t<=c.DUR;t+=0.3){c.seek(t);document.querySelectorAll('#xs .st-bub').forEach(g=>out.add(g.textContent));}return [...out];}""")
    ok("🌈 kids: the newcomer says hello («أنا … أنا بساعدك»), the one helped says «شكراً»", any("بساعدك" in x or "إحنا هون" in x for x in bubs) and any("شكراً" in x for x in bubs), bubs[:8])
    # ---------- 🧭 junior: the same characters, calmer ----------
    gj = next(i for i, g in enumerate(data["graphs"]) if g["audience"]["stage"] == "junior" and g["subject"] == "physics")
    pg.evaluate(OPEN, [gj, 0]); pg.wait_for_timeout(200)
    hop = """()=>{const c=window.stCtl;c.pause();let mx=0;for(let t=0;t<=Math.min(c.DUR,40);t+=0.1){c.seek(t);document.querySelectorAll('#xs .sa-b').forEach(b=>{const m=/translate\\(0 ([-\\d.]+)\\)/.exec(b.getAttribute('transform')||'');if(m)mx=Math.max(mx,-(+m[1]));});}return mx;}"""
    hj = pg.evaluate(hop); jsubs = pg.evaluate("""()=>{const c=window.stCtl;c.pause();const out=new Set();for(let t=0;t<=c.DUR;t+=0.3){c.seek(t);out.add(document.getElementById('stSub').textContent.trim());}return [...out];}""")
    pg.evaluate(OPEN, [gk, 0]); pg.wait_for_timeout(200); hk = pg.evaluate(hop)
    ok("🧭 junior: a team of explorers («انضمّ للفريق»), no «كان يا ما كان»", any("للفريق" in x for x in jsubs) and not any("كان يا ما كان" in x for x in jsubs), list(jsubs)[:6])
    ok("🧭 junior: calmer — they hop much lower than the little ones' characters", 0 < hj < hk * 0.6, (hj, hk))
    # ---------- 🔬 teen: the investigation board ----------
    gt = next(i for i, g in enumerate(data["graphs"]) if g["audience"]["stage"] == "teen" and g["subject"] == "science")
    pg.evaluate(OPEN, [gt, 0]); pg.wait_for_timeout(200)
    t0 = pg.evaluate("""()=>{const c=window.stCtl;c.pause();c.seek(2.6);return [[...document.querySelectorAll('#xs .bd-card')].filter(g=>+g.style.opacity>0.5).map(g=>g.querySelector('.bd-tag').textContent),document.querySelectorAll('#xs .bd-card').length,document.querySelectorAll('#xs .bd-str').length,document.querySelector('.st-screen .st-tt1').textContent];}""")
    ok("🔬 teen: a cork board — first only the case card «القضية» is pinned; the title says «ملف قضية»", t0[0] == ["القضية"] and "قضية" in t0[3], t0)
    mid = pg.evaluate("""()=>{const c=window.stCtl;c.pause();const ch=JSON.parse(document.querySelector('.st-screen').dataset.chap);const tE=ch.find(x=>x[1]==='الأدلة')[0];c.seek(tE+2.4);
      const L=document.querySelector('#xs .bd-lens');return [[...document.querySelectorAll('#xs .bd-card')].filter(g=>+g.style.opacity>0.5).map(g=>g.querySelector('.bd-tag').textContent),
        [...document.querySelectorAll('#xs .bd-str')].filter(s=>s.getAttribute('marker-mid')&&+s.getAttribute('stroke-dashoffset')<0.05).length,getComputedStyle(document.querySelector('#xs .bd-str')).stroke,+L.getAttribute('opacity'),
        [...document.querySelectorAll('#xs .bd-pin')].filter(p=>/scale\\(1/.test(p.getAttribute('transform'))).length];}""")
    ok("🔬 teen: the first evidence card «دليل ١» is pinned, a RED string with its arrow ties it, the magnifier is on it", "دليل ١" in mid[0] and mid[1] >= 1 and mid[2] in ("rgb(194, 48, 42)",) and mid[3] > 0.5 and mid[4] >= 2, mid)
    end = pg.evaluate("""()=>{const c=window.stCtl;c.pause();c.seek(c.DUR-0.2);return [[...document.querySelectorAll('#xs .bd-card')].filter(g=>+g.style.opacity>0.5).length,document.querySelectorAll('#xs .bd-card').length,
        [...document.querySelectorAll('#xs .bd-stamp')].filter(s=>+s.getAttribute('opacity')>0.5).map(s=>s.textContent)];}""")
    ok("🔬 teen: at the end every card is on the board and the case gets its green ✔", end[0] == end[1] and "✔" in end[2], end)
    tw = pg.evaluate("""()=>{const c=window.stCtl;c.pause();const ch=JSON.parse(document.querySelector('.st-screen').dataset.chap);const x=ch.find(y=>y[1]==='الاختبار');if(!x)return null;c.seek(x[0]+3.4);
      return [document.querySelectorAll('#xs .bd-card.st-gray').length,document.querySelectorAll('#xs .bd-str.bd-slack').length,[...document.querySelectorAll('#xs .bd-stamp')].filter(s=>+s.getAttribute('opacity')>0.5).map(s=>s.textContent)];}""")
    ok("🔬 teen: the test — the card everyone depends on is off the board: its strings hang loose, the others get a ✕", tw is None or (tw[0] >= 1 and tw[1] >= 1 and "✕" in tw[2]), tw)
    # ---------- 📐 senior: the documentary diagram ----------
    gs = next(i for i, g in enumerate(data["graphs"]) if g["audience"]["stage"] == "senior" and g["subject"] == "physics")
    pg.evaluate(OPEN, [gs, 0]); pg.wait_for_timeout(200)
    sd = pg.evaluate("""()=>{const c=window.stCtl;c.pause();const z=[],shown=[];let n='';for(let t=0;t<=c.DUR;t+=0.25){c.seek(t);const m=/scale\\(([\\d.]+)\\)/.exec(document.querySelector('#xs .sd-cam').getAttribute('transform'));z.push(+m[1]);
        shown.push([...document.querySelectorAll('#xs .sd-node')].filter(g=>g.style.opacity==='1').length);if(t<4)n=document.querySelector('#xs .sd-n').textContent;}
      return [Math.max(...z),z[z.length-1],shown,document.querySelector('#xs .sd-q').textContent,n,getComputedStyle(document.querySelector('#xs .sd-ring')).stroke,document.querySelector('.st-screen .st-tt1').textContent];}""")
    grow = sd[2]; steps = sorted(set(grow))
    ok("📐 senior: the diagram builds itself — one node at a time (1 → 2 → … → all), never all at once", grow[0] == 0 and steps == list(range(0, max(grow) + 1)) and all(b2 >= a2 for a2, b2 in zip(grow, grow[1:])), steps)
    ok("📐 senior: a camera — it comes closer to the new part, and is back on the whole map at the end", sd[0] > 1.05 and abs(sd[1] - 1) < 0.01, sd[:2])
    ok("📐 senior: the question on top (the name in colour, no «»), a counter «العناصر: ١ / …», calm thin lines, no faces, no emoji in the title",
       sd[3].startswith("السؤال") and "«" not in sd[3] and "العناصر" in sd[4] and sd[5] == "rgb(127, 214, 201)" and sd[6] == "مخطط الدرس"
       and pg.evaluate("[...document.querySelectorAll('#xs .sd-node .sface')].every(f=>getComputedStyle(f).display==='none')"), sd[3:])
    dim = pg.evaluate("""()=>{const c=window.stCtl;c.pause();let mx=0,last=-1;for(let t=0;t<=c.DUR;t+=0.25){c.seek(t);mx=Math.max(mx,document.querySelectorAll('#xs .sd-node.sd-dim').length);}c.seek(c.DUR-0.1);last=document.querySelectorAll('#xs .sd-node.sd-dim').length;return [mx,last];}""")
    ok("📐 senior: while it looks at one part, the rest steps back (dims); at the end the whole map is bright", dim[0] >= 1 and dim[1] == 0, dim)
    sw = pg.evaluate("""()=>{const c=window.stCtl;c.pause();const out=[];for(let t=0;t<=c.DUR;t+=0.3){c.seek(t);out.push(document.getElementById('stSub').textContent);}return out.join(' ');}""")
    ok("📐 senior: its words are the expert's («بيعتمد على»، «فرضية»، «الاستنتاج»), never «بيحتاج»", ("بيعتمد" in sw or "بتعتمد" in sw) and "فرضية" in sw and "الاستنتاج" in sw and "بيحتاج" not in sw and "بتحتاج" not in sw, sw[:200])
    # ---------- (3) no «» in any bubble of any cartoon ----------
    left = []
    for gi, g in enumerate(data["graphs"]):
        if g["audience"]["stage"] not in ("kids", "junior"): continue
        pg.evaluate(OPEN, [gi, 0]); pg.wait_for_timeout(60)
        left += pg.evaluate("""()=>{const c=window.stCtl;c.pause();const out=[];for(let t=0;t<=c.DUR;t+=0.4){c.seek(t);document.querySelectorAll('#xs .st-bub text, #xs text').forEach(x=>{if(/[«»]/.test(x.textContent))out.push(x.textContent);});}return out;}""")
    for st in ("teen", "senior"):
        gi = next(i for i, g in enumerate(data["graphs"]) if g["audience"]["stage"] == st)
        pg.evaluate(OPEN, [gi, 0]); pg.wait_for_timeout(60)
        left += pg.evaluate("""()=>{const c=window.stCtl;c.pause();const out=[];for(let t=0;t<=c.DUR;t+=0.5){c.seek(t);document.querySelectorAll('#xs text').forEach(x=>{if(/[«»]/.test(x.textContent))out.push(x.textContent);});}return out;}""")
    ok("🏷️ no «» in any story's picture (bubbles, cards, the diagram's question) — the name is bold instead", not left, sorted(set(left))[:4])
    # the concept cartoon «تعرّف عليّ» uses the same player and still works
    pg.evaluate(OPEN, [gk, 0]); pg.wait_for_timeout(150)
    pg.evaluate("window.stCtl&&window.stCtl.pause();document.querySelector('#prog .pstop[data-c=\"0\"]').click()"); pg.wait_for_timeout(300)
    ok("🎬 the concept cartoon «تعرّف عليّ» still plays on the same player", pg.evaluate("(document.querySelector('.st-screen')||{dataset:{}}).dataset.kind") == "cstory" and pg.evaluate("!!window.stCtl&&window.stCtl.DUR>5"))
    pg.close()
    # ---------- 📱 the phone ----------
    ctx = b.new_context(viewport={"width": 390, "height": 844}, has_touch=True, is_mobile=True); pg = ctx.new_page(); pg.route("**/fonts.*/**", lambda r: r.abort()); pg.on("pageerror", lambda e: errs.append(str(e)[:200]))
    pg.goto(URL); pg.wait_for_timeout(600); wide = []
    for st in ("kids", "junior", "teen", "senior"):
        gi = next(i for i, g in enumerate(data["graphs"]) if g["audience"]["stage"] == st)
        pg.evaluate(OPEN, [gi, 0]); pg.wait_for_timeout(250)
        pg.evaluate("window.stCtl.pause();window.stCtl.seek(window.stCtl.DUR-0.3)")
        w = pg.evaluate("""()=>{const sv=document.getElementById('xs'),r=sv.getBoundingClientRect(),vb=sv.viewBox.baseVal;let out=0;sv.querySelectorAll('.sa').forEach(g=>{const b=g.getBoundingClientRect();if(b.width&&(b.left<r.left-2||b.right>r.right+2))out++;});return [document.documentElement.scrollWidth,out,vb.width];}""")
        if w[0] > 391 or w[1] or w[2] != 380: wide.append((st, w))
    ok("📱 the phone: every age's story fits (no sideways scroll, every card / node inside the picture)", not wide, wide)
    ctx.close()
    b.close()
print("\n".join(r for r in res if r.startswith("❌")) or "")
print(f"✅ {sum(r.startswith('✅') for r in res)} checks passed · ❌ {sum(r.startswith('❌') for r in res)} failed")
print("JS errors:", errs or "none")
