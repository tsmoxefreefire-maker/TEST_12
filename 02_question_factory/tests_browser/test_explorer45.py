"""🗂️ batch 45 · the code explorer (code_tour/PROJECT_EXPLORER.html) in a real browser — Hareth's two asks:
(1) «بدي أشيله»: the × closes a tab (the open one or one behind), all closed → the welcome page, still closed after a reload;
(2) «لما أحدّد على فانكشن بيطلع شرحها… وخلّي الشرح أوضح وشامل»: select code with the mouse → its explanation (one thing: its card; several: a
    list to choose from); the card has all its parts (in a sentence · what it is · where · its first line · what it takes · what it calls · who calls it).
python tests_browser/test_explorer45.py      (build the explorer first: python code_tour/build_project_explorer.py)"""
import pathlib
from playwright.sync_api import sync_playwright
HERE = pathlib.Path(__file__).resolve().parent
URL = (HERE.parent.parent / "code_tour" / "PROJECT_EXPLORER.html").as_uri()
SH = None
res, errs = [], []
def ok(n, c, x=""): res.append(("✅" if c else "❌") + " " + n + ("" if c else " " + str(x)[:300]))
def drag(pg,a,b):
    pg.evaluate(f"document.getElementById('code').scrollTop=Math.max(0,document.querySelector('#code .ln[data-n=\"{a}\"]').offsetTop-document.getElementById('code').offsetTop-150)");pg.wait_for_timeout(150)
    pa=pg.evaluate(f"(()=>{{const r=document.querySelector('#code .ln[data-n=\"{a}\"] .tx').getBoundingClientRect();return [r.left+60,r.top+8];}})()")
    pb=pg.evaluate(f"(()=>{{const r=document.querySelector('#code .ln[data-n=\"{b}\"] .tx').getBoundingClientRect();return [r.left+40,r.top+8];}})()")
    pg.mouse.move(*pa);pg.mouse.down();pg.mouse.move(*pb,steps=10);pg.mouse.up();pg.wait_for_timeout(250)

# ---------- (1) the × closes the tab ----------
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={"width":1300,"height":850});pg.on("pageerror",lambda e:errs.append(str(e)[:200]))
    pg.goto(URL);pg.wait_for_timeout(500)
    files=pg.evaluate("[...document.querySelectorAll('.row.file')].slice(0,3).map(r=>r.dataset.p)")
    for f in files: pg.click(f'.row.file[data-p="{f}"]');pg.wait_for_timeout(150)
    n0=pg.locator("#tabs .tab").count()
    
    pg.click("#tabs .tab[aria-selected='true'] .x");pg.wait_for_timeout(200)
    ok("× closes the open tab",pg.locator("#tabs .tab").count()==n0-1,(n0,pg.locator("#tabs .tab").count()))
    pg.click("#tabs .tab:not([aria-selected='true']) .x");pg.wait_for_timeout(200)
    ok("× on a tab in the back closes it too",pg.locator("#tabs .tab").count()==n0-2)
    while pg.locator("#tabs .tab").count():pg.click("#tabs .tab .x");pg.wait_for_timeout(150)
    ok("all closed → no tabs, the welcome page",pg.locator("#tabs .tab").count()==0)
    
    pg.reload();pg.wait_for_timeout(500)
    ok("after a reload it stays closed",pg.locator("#tabs .tab").count()==0)
    pg.click('.ptab[data-mode="journey"]');pg.wait_for_timeout(200)
    st=pg.locator("[data-fstep],[data-jfile]").first
    if st.count():st.click();pg.wait_for_timeout(300)
    ok("step by step still opens files",pg.locator("#tabs .tab").count()>=1)
    b.close()

# ---------- (2) select → the explanation ----------
ar = "٠١٢٣٤٥٦٧٨٩"
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={"width":1400,"height":900});pg.on("pageerror",lambda e:errs.append(str(e)[:200]))
    pg.goto(URL+"#03_explain_player_src~story38.js");pg.wait_for_timeout(600)
    ok("🖱️ the hint is above the code",pg.locator(".selhint").count()==1 and "حدّد" in pg.inner_text(".selhint"))
    # the lines of stCast: find via the items list in the panel
    rng=pg.evaluate("(()=>{const b=[...document.querySelectorAll('#info .it')].find(x=>x.dataset.item==='stCast');return b?b.querySelector('small').textContent:null;})()")
    ar="٠١٢٣٤٥٦٧٨٩";conv=lambda s:int("".join(str(ar.index(c)) if c in ar else c for c in s))
    a,bb=[conv(x) for x in rng.split("–")]
    drag(pg,a+3,a+6)
    card=pg.inner_text("#info .icard") if pg.locator("#info .icard").count() else ""
    ok("selecting a few lines inside stCast → stCast's explanation",pg.evaluate("document.querySelector('#info .icard code')?.textContent")=="stCast",card[:120])
    for h in ["📌 بجملة","🧩 شو هي","📍 وينها","✍️ أول سطر منها","📥 شو بتاخد","🔗 بتستعمل","👥 مين بيستعملها"]:
        if h not in card: ok("the card has «"+h+"»",False,card[:200])
    ok("📋 the card has all its parts (in a sentence · what · where · first line · takes · calls · who calls)",all(h in card for h in ["📌","🧩","📍","✍️","📥","🔗","👥"]))
    ok("📥 what it takes: s, P, tale",all(x in pg.inner_text("#info .icard") for x in ["s","P","tale"]) and pg.evaluate("[...document.querySelectorAll('#info .icard p.takes code')].map(c=>c.textContent).join(',')")=="s,P,tale",pg.evaluate("[...document.querySelectorAll('#info .icard p.takes code')].map(c=>c.textContent).join(',')"))
    ok("the selected text is still selected (you can still copy it)",len(pg.evaluate("getSelection().toString()"))>10)
    
    # select across several functions (the start of the file: several small consts)
    drag(pg,16,26)
    n=pg.locator("#info .icard .it").count()
    ok("selecting several → a list to choose from",n>=3,(n,pg.inner_text("#info .icard")[:200] if pg.locator("#info .icard").count() else ""))
    
    if n:
        k=pg.evaluate("document.querySelector('#info .icard .it').dataset.item");pg.click("#info .icard .it");pg.wait_for_timeout(200)
        ok("…a click on one → its full explanation",pg.evaluate("document.querySelector('#info .icard code')?.textContent")==k,k)
    pg.click("#info .icard .x");pg.wait_for_timeout(150)
    ok("✕ → back to the file's explanation",pg.locator("#info .icard").count()==0)
    # the line number still works
    pg.click(f'#code .ln[data-n="{a+2}"] .g',force=True);pg.wait_for_timeout(150)
    ok("a click on the line number still works",pg.evaluate("document.querySelector('#info .icard code')?.textContent")=="stCast")
    # a python file
    pg.goto(URL+"#05_explanation_api~core~tts.py");pg.reload();pg.wait_for_timeout(600)
    rng=pg.evaluate("(()=>{const b=[...document.querySelectorAll('#info .it')].find(x=>x.dataset.item==='speak');return b?b.querySelector('small').textContent:null;})()")
    a,bb=[conv(x) for x in rng.split("–")];drag(pg,a+2,a+4)
    ps=pg.evaluate("[...document.querySelectorAll('#info .icard p.takes code')].map(c=>c.textContent).join(',')")
    ok("🐍 python: selecting inside speak → its explanation, it takes text, stage",pg.evaluate("document.querySelector('#info .icard code')?.textContent")=="speak" and ps=="text,stage",ps)
    # another file clears an old list
    drag(pg,1,40);pg.click('.row.file[data-p="03_explain_player_src/outfit45.js"]') if pg.locator('.row.file[data-p="03_explain_player_src/outfit45.js"]').count() else (pg.goto(URL+"#03_explain_player_src~outfit45.js"),pg.reload());pg.wait_for_timeout(400)
    ok("opening another file never shows the old selection",pg.locator("#info .icard").count()==0)
    b.close()
    # the phone
    b=p.chromium.launch();ctx=b.new_context(viewport={"width":390,"height":844},is_mobile=True,has_touch=True);pg=ctx.new_page();pg.on("pageerror",lambda e:errs.append(str(e)[:200]))
    pg.goto(URL+"#03_explain_player_src~story38.js");pg.wait_for_timeout(600)
    w=pg.evaluate("[document.documentElement.scrollWidth,innerWidth]")
    ok("📱 the phone: no sideways scroll",w[0]<=w[1]+1,w)
    b.close()
ok("no JS error", not errs, errs[:3])
print("\n".join(res))
print(f"✅ {sum(r.startswith('✅') for r in res)} checks passed · ❌ {sum(r.startswith('❌') for r in res)} failed")
