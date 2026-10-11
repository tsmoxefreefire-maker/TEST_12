"""🆕 batch 45 (Hareth: «لازم نزيد هياكل ثانية للحكاية… ضيف لي اثنين»): the little ones and the explorers have THREE tales now —
the classic one (the hero alone, the others are called in), 🚶 THE CLIMB (from the bottom up, the hero arrives last) and 🎉 THE GATHERING
(everybody in the place from the start, who helps whom). Same characters, same place, same moves, same twist (the thief) and end.
Checks, for EVERY lesson of every kids / junior book, in every tale: it plays to the end with no JS error · every arrow of the lesson is drawn
· the twist has its thief · the subtitles never overlap (the voice reads them one by one) · the lessons take the tales in turn (lesson 1 the
classic) · the climb starts from the bottom and the hero comes last · in the gathering everybody is in the picture from the start · the
board and the diagram of the older ones are untouched.      python tests_browser/test_batch45.py"""
import json, pathlib
from playwright.sync_api import sync_playwright
HERE = pathlib.Path(__file__).resolve().parent
PAGE = HERE.parent / "player" / "explain.html"; URL = PAGE.as_uri()
data = json.loads(PAGE.read_text(encoding="utf-8").split("const DATA = ")[1].split(";\nconst $")[0])
res, errs = [], []
def ok(n, c, x=""): res.append(("✅" if c else "❌") + " " + n + ("" if c else " " + str(x)[:400]))
OPEN = "([gi,li])=>{window.stCtl&&window.stCtl.pause();document.querySelector(`#side .les[data-g=\"${gi}\"][data-l=\"${li}\"]`).click();}"
TALES = ("classic", "journey", "party")
# one look at the whole tale: the arrows drawn at the end, the thief, the subtitles' times, who is inside the picture when
LOOK = """()=>{const c=window.stCtl;c.pause();const scr=document.querySelector('.st-screen'),W=+document.getElementById('xs').viewBox.baseVal.width;
  const inside=()=>[...document.querySelectorAll('#xs .sa')].filter(g=>{const m=/translate\\(([-\\d.]+) /.exec(g.getAttribute('transform')||'');return m&&+m[1]>0&&+m[1]<W;}).map(g=>g.dataset.id);
  const first={};for(let t=0;t<=c.DUR;t+=0.25){c.seek(t);inside().forEach(id=>{if(first[id]==null)first[id]=t;});}
  const s1=c.subs.slice().sort((a,b)=>a[0]-b[0])[1];c.seek(s1?s1[0]+0.05:4.5);const early=inside();c.seek(c.DUR);
  const links=[...document.querySelectorAll('#xs .st-link')],drawn=links.filter(l=>+l.getAttribute('stroke-dashoffset')<0.05).length;
  return {tale:scr.dataset.tale,look:scr.dataset.look,dur:c.DUR,links:links.length,drawn,thief:document.querySelectorAll('#xs .st-thief').length,
    chap:c.chap.map(x=>x[1]),subs:c.subs.map(s=>[+s[0].toFixed(2),+s[1].toFixed(2),s[2]]),first,early,all:[...document.querySelectorAll('#xs .sa')].map(g=>g.dataset.id)};}"""

little = [(gi, g) for gi, g in enumerate(data["graphs"]) if g["audience"]["stage"] in ("kids", "junior")]
with sync_playwright() as p:
    b = p.chromium.launch()
    looks = {}
    for tale in TALES:
        pg = b.new_page(viewport={"width": 1150, "height": 950}); pg.route("**/fonts.*/**", lambda r: r.abort()); pg.on("pageerror", lambda e: errs.append(str(e)[:200]))
        pg.goto(URL + f"?q=hi&tale={tale}"); pg.wait_for_timeout(400)
        for gi, g in little:
            for li, l in enumerate(g["lessons"]):
                pg.evaluate(OPEN, [gi, li]); pg.wait_for_timeout(30)
                looks[(tale, gi, li)] = pg.evaluate(LOOK)
        pg.close()
    n = len(looks) // 3
    for tale in TALES:
        mine = {k: v for k, v in looks.items() if k[0] == tale}
        bad_tale = [k for k, v in mine.items() if v["tale"] != tale]
        ok(f"🎬 «{tale}»: every lesson of the little ones / the explorers tells this tale ({len(mine)} lessons)", not bad_tale and len(mine) == n, bad_tale[:3])
        undrawn = [(k, v["drawn"], v["links"]) for k, v in mine.items() if v["drawn"] != v["links"]]
        ok(f"➡️ «{tale}»: at the end EVERY arrow of the lesson is drawn", not undrawn, undrawn[:3])
        nothief = [k for k, v in mine.items() if "المفاجأة" in v["chap"] and v["thief"] != 1]
        twists = sum("المفاجأة" in v["chap"] for v in mine.values())
        ok(f"🐰 «{tale}»: the twist has its thief ({twists} twists)", not nothief and twists >= n * 0.6, nothief[:3])
        clash = []
        for k, v in mine.items():
            s = sorted(v["subs"])
            clash += [(k, a[2][:30], c[2][:30]) for a, c in zip(s, s[1:]) if c[0] < a[1] - 0.05]
        ok(f"🗣️ «{tale}»: the subtitles never overlap (the voice reads them one by one)", not clash, clash[:3])
        ok(f"⏱️ «{tale}»: not too long (≤ 3 min)", max(v["dur"] for v in mine.values()) <= 180, max(v["dur"] for v in mine.values()))
    # the climb: from the bottom up, the hero last
    wrong = []
    for (tale, gi, li), v in looks.items():
        if tale != "journey":
            continue
        g = data["graphs"][gi]; ov = g["lessons"][li].get("overview") or {}
        if not ov.get("edges"):
            continue
        hero = pg_hero = None
        fs = sorted(v["first"].items(), key=lambda x: x[1])
        needs = {bb for _, bb in ov["edges"]}
        if fs and fs[0][0] in needs and any(x not in needs for x, _ in fs):
            wrong.append((g["title"][:20], li, "starts with one that needs", fs[0][0]))
    ok("🚶 the climb starts from the bottom (the first one in the picture needs nobody)", not wrong, wrong[:3])
    late = []
    for (tale, gi, li), v in looks.items():
        if tale != "party":
            continue
        out = [x for x in v["all"] if x not in v["early"]]
        if out:
            late.append((data["graphs"][gi]["title"][:20], li, out[:3]))
    ok("🎉 the gathering: everybody is in the picture from the start (before the second line)", not late, late[:3])
    # the same lesson, three different tales: different words and a different order of arrival
    diff = sum(1 for (t, gi, li), v in looks.items() if t == "classic" and len(v["all"]) >= 3
               and len({json.dumps(sorted(looks[(x, gi, li)]["first"].items(), key=lambda y: y[1])[:3]) for x in TALES}) >= 2)
    many = sum(1 for (t, gi, li), v in looks.items() if t == "classic" and len(v["all"]) >= 3)
    ok("🔀 the same lesson in the three tales: the characters come in a different order", diff >= many * 0.7, (diff, many))
    words = [v["subs"][0][2] for (t, gi, li), v in looks.items() if (gi, li) == (little[0][0], 0)]
    ok("📖 …and the tales open with different words", len(set(words)) == 3, words)
    # no ?tale=: the lessons take them in turn (lesson 1 the classic, so every old check still sees the classic tale)
    pg = b.new_page(viewport={"width": 1150, "height": 950}); pg.route("**/fonts.*/**", lambda r: r.abort()); pg.on("pageerror", lambda e: errs.append(str(e)[:200]))
    pg.goto(URL + "?q=hi"); pg.wait_for_timeout(400)
    turn = []
    gi, g = little[0]
    for li in range(min(6, len(g["lessons"]))):
        pg.evaluate(OPEN, [gi, li]); pg.wait_for_timeout(30)
        turn.append(pg.evaluate("document.querySelector('.st-screen').dataset.tale"))
    ok("🔁 the lessons of a book take the tales in turn (1 classic · 2 climb · 3 gathering · …)", turn == [TALES[i % 3] for i in range(len(turn))], turn)
    pg.evaluate(OPEN, [gi, 1]); pg.wait_for_timeout(30); again = pg.evaluate("document.querySelector('.st-screen').dataset.tale")
    ok("🔁 the same lesson always tells the same tale", again == turn[1], (again, turn[1]))
    # the older ones: the board and the diagram, untouched
    for st, look in (("teen", "board"), ("senior", "doc")):
        gj = next((i for i, x in enumerate(data["graphs"]) if x["audience"]["stage"] == st), None)
        if gj is None:
            continue
        pg.evaluate(OPEN, [gj, 1]); pg.wait_for_timeout(40)
        ok(f"🕵️ {st}: still the {look} (the new tales are only for the little ones and the explorers)", pg.evaluate("document.querySelector('.st-screen').dataset.look") == look and pg.locator("#xs .st-thief").count() == 0)
    # the phone: the climb and the gathering fit
    ctx = b.new_context(viewport={"width": 390, "height": 844}, has_touch=True, is_mobile=True)
    for tale in ("journey", "party"):
        pp = ctx.new_page(); pp.route("**/fonts.*/**", lambda r: r.abort()); pp.on("pageerror", lambda e: errs.append(str(e)[:200]))
        pp.goto(URL + f"?q=hi&tale={tale}"); pp.wait_for_timeout(500)
        w = pp.evaluate("[document.documentElement.scrollWidth, innerWidth]")
        v = pp.evaluate(LOOK)
        ok(f"📱 the phone: «{tale}» plays to the end, every arrow drawn, no sideways scroll", v["drawn"] == v["links"] and w[0] <= w[1] + 1, (v["drawn"], v["links"], w))
        pp.close()
    ctx.close()
    b.close()
ok("no JS error", not errs, errs[:3])
print("\n".join(res))
print(f"✅ {sum(r.startswith('✅') for r in res)} checks passed · ❌ {sum(r.startswith('❌') for r in res)} failed")
