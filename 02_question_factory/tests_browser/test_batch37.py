"""🆕 batch 37 (Hareth's notes) in a real browser:
(1) the QUALITY switch is clear: it shows BOTH choices (🍃 خفيفة · ✨ عالية) and the one that is ON is filled (before, it showed only the
    state, which read like an order: «جودة عالية» looked like «press for high»); switching to high gives the place its living things AT ONCE
    (birds, butterflies…), switching to light takes them away at once;
(2) the TITLES are clean: no «» marks around a name anywhere the student reads (the welcome title, the story / cartoon title cards, the
    subtitles, the line under the steps, the captions, the bubbles, the cards, the buttons, the end card…) — the name is bold / a chip,
    and the words are exactly the same as before.
python tests_browser/test_batch37.py"""
import json, pathlib, sys
from playwright.sync_api import sync_playwright
HERE = pathlib.Path(__file__).resolve().parent
PAGE = HERE.parent / "player" / "explain.html"; URL = PAGE.as_uri()
data = json.loads(PAGE.read_text(encoding="utf-8").split("const DATA = ")[1].split(";\nconst $")[0])
STEPS = lambda s: 1 if s["kind"] == "meet" else len(s["steps"])
res, errs = [], []
def ok(n, c, x=""): res.append(("✅" if c else "❌") + " " + n + ("" if c else " " + str(x)[:300]))
GRAB = """()=>{const out=[];const add=(where,t)=>{if(/[«»]/.test(t||''))out.push(where+': '+t.trim().slice(0,70));};
  document.querySelectorAll('#welcome, #prog .where, #cap, #q .gx-mission, #q .gx-end, #q .na-zones, #q .g36-lane, #q .na-opts, #q .na-chat, #q .na-note, #q .xswitch, #q .g4-sws, #q .slider2, #q .g36-ask, #q .st-sub, #q .why, #lsum').forEach(e=>add(e.className||e.id,e.innerText));
  document.querySelectorAll('#xs text').forEach(t=>{const r=t.getBoundingClientRect();if(r.width)add('svg.'+(t.getAttribute('class')||t.parentNode.getAttribute('class')||'text'),t.textContent);});
  return out;}"""

with sync_playwright() as p:
    b = p.chromium.launch()
    ctx = b.new_context(viewport={"width": 1150, "height": 950}); pg = ctx.new_page(); pg.route("**/fonts.*/**", lambda r: r.abort()); pg.on("pageerror", lambda e: errs.append(str(e)[:200]))
    pg.goto(URL); pg.wait_for_timeout(600)
    # ---------- (1) the quality switch ----------
    q = lambda: pg.evaluate("[document.body.dataset.q,[...document.querySelectorAll('#qBtn .q37-o')].map(o=>o.textContent.trim()),(document.querySelector('#qBtn .q37-on')||{}).dataset.q,document.querySelectorAll('#xs .pl-life').length]")
    s0 = q()
    ok("🎚️ the switch shows BOTH choices (🍃 خفيفة · ✨ عالية), the one ON is filled and is the real one", s0[1] == ["🍃 خفيفة", "✨ عالية"] and s0[2] == s0[0], s0)
    pg.click('#qBtn .q37-o[data-q="hi"]'); pg.wait_for_timeout(250); s1 = q()
    ok("✨ high: the place gets its living things AT ONCE (no need to wait for the next scene)", s1[0] == "hi" and s1[2] == "hi" and s1[3] > 0, s1)
    ok("✨ high: they really move (the birds fly)", pg.evaluate("getComputedStyle(document.querySelector('#xs .pl-cross')).animationName").startswith("plCross"))
    pg.click('#qBtn .q37-o[data-q="lo"]'); pg.wait_for_timeout(250); s2 = q()
    ok("🍃 light: they go away at once, and the switch says light", s2[0] == "lo" and s2[2] == "lo" and s2[3] == 0, s2)
    pg.click('#qBtn .q37-l'); pg.wait_for_timeout(250)
    ok("tapping the switch's label flips it", q()[0] == "hi")
    pg.evaluate("window.stCtl&&window.stCtl.pause();document.querySelector('#prog .pstop[data-c=\"-1\"]').click()"); pg.wait_for_timeout(400)
    ok("✨ high on a normal scene too (the big picture): the living things are there", q()[3] > 0, q())
    # ---------- (2) clean titles ----------
    h1 = pg.evaluate("[document.querySelector('#welcome h1').textContent,!!document.querySelector('#welcome h1 .t37-name')]")
    ok("🏷️ the welcome title: «أهلاً! 👋 أنا بذور» — the name in colour, no marks", "«" not in h1[0] and "»" not in h1[0] and h1[1], h1)
    pg.evaluate("window.stCtl&&window.stCtl.pause();document.querySelector('#side .les[data-g=\"0\"][data-l=\"0\"]').click()"); pg.wait_for_timeout(400)
    pg.evaluate("(()=>{const c=window.stCtl;c.pause();c.seek(0.5);})()"); pg.wait_for_timeout(300)
    tt = pg.evaluate("(document.querySelector('#xs .st-tt2')||{}).textContent||''")
    ok("🎬 the story's title card: the lesson's name alone (no marks)", tt and "«" not in tt and tt.strip() == data["graphs"][0]["lessons"][0]["lesson_title"].strip(), tt)
    sub = pg.evaluate("(()=>{const c=window.stCtl;for(let t=0;t<8;t+=0.4){c.seek(t);const s=document.getElementById('stSub');if(s&&s.querySelector('b'))return [s.textContent,s.querySelector('b').textContent];}return ['',''];})()")
    ok("📖 the story's subtitles: the name in yellow bold, no marks", sub[1] and "«" not in sub[0], sub)
    first = data["graphs"][0]["lessons"][0]["concepts"][0]
    pg.evaluate("window.stCtl&&window.stCtl.pause();document.querySelector('#prog .pstop[data-c=\"0\"]').click()"); pg.wait_for_timeout(400)
    wh = pg.evaluate("[document.querySelector('#prog .where').textContent,!!document.querySelector('#prog .where .t37-name')]")
    ok("🧭 the line under the steps: «👋 تعرّف عليّ · الزهرة» (the name in colour, no marks)", "«" not in wh[0] and wh[1] and first["title"] in wh[0], wh)
    capt = pg.evaluate("[document.getElementById('cap').innerText,[...document.querySelectorAll('#cap .kw')].map(k=>k.textContent)]")
    ok("💬 the caption: the names are chips WITHOUT marks — and the words are the same", "«" not in capt[0] and capt[1] and all("«" not in k for k in capt[1]), capt)
    # every kind of scene, the little ones and the big ones: nothing the student reads shows «»
    seen, left = set(), []
    for gi, g in enumerate(data["graphs"]):
        for li, l in enumerate(g["lessons"]):
            for ci, c in enumerate(l["concepts"]):
                for si, s in enumerate(c["scenes"]):
                    key = (s["kind"], g["audience"]["stage"])
                    if key in seen: continue
                    seen.add(key)
                    pg.evaluate("window.stCtl&&window.stCtl.pause()")
                    pg.evaluate(f"document.querySelector('#side .les[data-g=\"{gi}\"][data-l=\"{li}\"]').click()"); pg.wait_for_timeout(100)
                    left += pg.evaluate(GRAB)
                    pg.evaluate("window.stCtl&&window.stCtl.pause()")
                    pg.evaluate(f"document.querySelector('#prog .pstop[data-c=\"{ci}\"]').click()"); pg.wait_for_timeout(100)
                    pg.evaluate("document.getElementById('play').textContent.includes('وقّف')&&document.getElementById('play').click()")
                    for _ in range(sum(STEPS(x) for x in c["scenes"][:si])): pg.evaluate("document.getElementById('next').click()")
                    for st in range(STEPS(s)):
                        pg.wait_for_timeout(220); left += pg.evaluate(GRAB)
                        if st < STEPS(s) - 1: pg.evaluate("document.getElementById('next').click()")
                    pg.evaluate("""()=>{const e=document.querySelector('#naOpts .na-opt, .na-zone, #xs .na-ing, .g4-sw, #xs .g4-opt, #xs .g4-brick, #sw, .na-opt');if(e){e.dispatchEvent(new MouseEvent('click',{bubbles:true}));const r=e.getBoundingClientRect();['pointerdown','pointerup'].forEach(t=>e.dispatchEvent(new PointerEvent(t,{bubbles:true,clientX:r.left+5,clientY:r.top+5,pointerId:1})));}}""")
                    pg.wait_for_timeout(1200); left += pg.evaluate(GRAB)
    ok(f"🧹 every kind of scene × every stage ({len(seen)}): no «» left in anything the student reads (titles, captions, bubbles, cards, buttons)", not left, sorted(set(left))[:5])
    # the end card of a game, and the lesson's end card
    f = next((gi, li, ci, si) for gi, g in enumerate(data["graphs"]) if g["audience"]["stage"] == "kids" for li, l in enumerate(g["lessons"]) for ci, c in enumerate(l["concepts"]) for si, s in enumerate(c["scenes"]) if s["kind"] == "compare")
    gi, li, ci, si = f; c = data["graphs"][gi]["lessons"][li]["concepts"][ci]; s = c["scenes"][si]
    pg.evaluate(f"window.stCtl&&window.stCtl.pause();document.querySelector('#side .les[data-g=\"{gi}\"][data-l=\"{li}\"]').click()"); pg.wait_for_timeout(150)
    pg.evaluate(f"window.stCtl&&window.stCtl.pause();document.querySelector('#prog .pstop[data-c=\"{ci}\"]').click()"); pg.wait_for_timeout(150)
    pg.evaluate("document.getElementById('play').textContent.includes('وقّف')&&document.getElementById('play').click()")
    for _ in range(sum(STEPS(x) for x in c["scenes"][:si])): pg.evaluate("document.getElementById('next').click()")
    pg.wait_for_timeout(300); pg.evaluate("document.getElementById('play').textContent.includes('وقّف')&&document.getElementById('play').click()"); pg.wait_for_timeout(300)
    for f_ in s["facts"]: pg.evaluate(f"document.querySelector('.na-zone[data-side=\"{f_['side']}\"]').dispatchEvent(new MouseEvent('click',{{bubbles:true}}))"); pg.wait_for_timeout(1150)
    pg.wait_for_timeout(1300)
    end = pg.evaluate("(document.querySelector('.gx-end')||{}).innerText||''")
    ok("⭐ the stars card: its badge has no marks", end and "«" not in end, end)
    ctx.close()
    # the phone: the switch fits
    ctx = b.new_context(viewport={"width": 390, "height": 844}, has_touch=True, is_mobile=True); pg = ctx.new_page(); pg.route("**/fonts.*/**", lambda r: r.abort()); pg.on("pageerror", lambda e: errs.append(str(e)[:200]))
    pg.goto(URL); pg.wait_for_timeout(600)
    ok("📱 the phone: the switch fits (no sideways scroll), and a phone starts light (ON = 🍃 خفيفة)", pg.evaluate("document.documentElement.scrollWidth") <= 391 and pg.evaluate("(()=>{const r=document.getElementById('qBtn').getBoundingClientRect();return r.left>=0&&r.right<=390;})()") and pg.evaluate("document.querySelector('#qBtn .q37-on').dataset.q") == "lo")
    ctx.close()
    b.close()
print("\n".join(r for r in res if r.startswith("❌")) or "")
print(f"✅ {sum(r.startswith('✅') for r in res)} checks passed · ❌ {sum(r.startswith('❌') for r in res)} failed")
print("JS errors:", errs or "none")
