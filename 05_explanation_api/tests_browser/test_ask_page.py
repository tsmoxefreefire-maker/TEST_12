"""🆕 batch 42 — «اسأل سؤال» (static/ask.html) in a real browser: a question → the scene that answers it opens at once.
The real service answers every request (Playwright routes them to core/service.py: the same functions FastAPI calls).
Checks: the status line · the book list (🆕 batch 43: no «كل الكتب») · «where he is now» (lesson, concept) · a question → the concept, how
it was found, its scenes, and the page opened RIGHT AT the scene that answers it (inside the frame) · 🆕 a question outside his book →
«خلينا نرجع لـ…» + a button that opens HIS concept · a concept of another book → not answered · the example chips · the phone ·
no JS error (the page and the frame).   Run:  python tests_browser/test_ask_page.py          (from 05_explanation_api)"""
import json
import os
import sys
import tempfile
import urllib.parse

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.environ["EXPLAIN_DATA_DIR"] = tempfile.mkdtemp(prefix="explain_ask_test_")
os.environ["EMBED_PROVIDER"] = "none"
sys.path.insert(0, HERE)
from playwright.sync_api import sync_playwright  # noqa: E402

from core import service  # noqa: E402

ORIGIN = "https://ie.test"
SHOTS = os.environ.get("ASK_SHOTS")                       # a folder → screenshots for the report
res, errs = [], []


def ok(n, c, x=""):
    res.append(("✅" if c else "❌") + " " + n + ("" if c else " " + str(x)[:300]))


def handle(route):
    req = route.request
    u = urllib.parse.urlparse(req.url)
    path, method = u.path, req.method
    j = lambda o, code=200: route.fulfill(status=code, content_type="application/json", body=json.dumps(o, ensure_ascii=False, default=str))
    try:
        if path == "/ask" and method == "GET":
            return route.fulfill(status=200, content_type="text/html; charset=utf-8", body=service.ask_html())
        if path == "/ask" and method == "POST":
            b = json.loads(req.post_data or "{}")
            return j(service.ask(b.get("question"), b.get("book_id"), b.get("grade"), b.get("stage"), b.get("lesson_id"), b.get("concept_id")))
        if path == "/books":
            return j(service.list_books())
        if path.startswith("/books/") and path.endswith("/lessons"):
            return j(service.list_lessons(path.split("/")[2]))
        if path.startswith("/lessons/") and path.endswith("/explanation"):
            return j(service.get_lesson(path.split("/")[2], urllib.parse.parse_qs(u.query).get("book_id", [None])[0]))
        if path == "/search/status":
            return j(service.search_status())
        if path.startswith("/explain/"):
            return route.fulfill(status=200, content_type="text/html; charset=utf-8", body=service.page_html([path.split("/")[2]]))
        return route.fulfill(status=404, body="not here")
    except service.NotFound as e:
        return j({"detail": str(e)}, 404)
    except service.BadInput as e:
        return j({"detail": str(e)}, 400)


def frame_text(pg):
    f = next((f for f in pg.frames if "/explain/" in f.url), None)
    if not f:
        return "", None
    try:
        f.wait_for_selector("#q .narr", timeout=8000)
        return f.inner_text("#q .narr"), f
    except Exception as e:   # noqa: BLE001
        return f"(no narr: {e})", f


service.seed_samples()
with sync_playwright() as p:
    b = p.chromium.launch()
    for vp in ({"width": 1280, "height": 900}, {"width": 390, "height": 844}):
        tag = "📱" if vp["width"] < 500 else "🖥️"
        ctx = b.new_context(viewport=vp)
        pg = ctx.new_page(); pg.on("pageerror", lambda e: errs.append(str(e)[:160]))
        pg.route("**/fonts.*/**", lambda r: r.abort()); pg.route(ORIGIN + "/**", handle)
        pg.goto(ORIGIN + "/ask"); pg.wait_for_timeout(900)
        st = pg.inner_text("#status")
        n = str(service.search_status().get("rows", ""))         # (🆕 batch 43: 388 — the two new activities are scenes too; never a fixed number)
        ok(f"{tag} the status: where it is kept + how many scenes can be found", "بالملفات" in st and n and n in st, (n, st))
        ok(f"{tag} 🆕 the book list: the 12 books, and NO «كل الكتب» (the search is always inside his book)",
           pg.locator("#book option").count() == 12 and "كل الكتب" not in pg.inner_text("#book"), pg.locator("#book option").count())
        pg.select_option("#book", "sci_g4"); pg.wait_for_timeout(500)
        ok(f"{tag} 🆕 «where he is now»: his book's lessons, and the concepts of his lesson", pg.locator("#lesson option").count() >= 2 and pg.locator("#concept option").count() >= 2,
           [pg.locator("#lesson option").count(), pg.locator("#concept option").count()])
        # a question → the concept, how, its scenes, and the page opened AT the scene
        pg.fill("#q", "شو بيصير لو ما في التلقيح؟"); pg.click(".go"); pg.wait_for_selector(".hit h2", timeout=8000)
        ok(f"{tag} «شو بيصير لو ما في التلقيح؟» → «التلقيح», found by its name, in a few ms",
           pg.inner_text(".hit h2") == "التلقيح" and "بالاسم" in pg.inner_text(".how"), pg.inner_text("#res")[:200])
        ok(f"{tag} its scenes in order, the one that answers lit («🔮 شو لو»)", "شو لو" in pg.inner_text(".sc.on") and pg.locator(".sc").count() >= 3,
           [pg.inner_text(".sc.on"), pg.locator(".sc").count()])
        pg.wait_for_timeout(2500)
        txt, fr = frame_text(pg)
        ok(f"{tag} the page inside opened RIGHT AT that scene (not at the lesson's start)", "اختفى" in txt and "التلقيح" in txt, txt[:120])
        if SHOTS and fr:
            pg.screenshot(path=os.path.join(SHOTS, f"ask_{'phone' if tag == '📱' else 'desktop'}.png"), full_page=tag == "📱")
        # 🆕 a question outside his book → no scene + «خلينا نرجع لـ…» + a button back to the concept he is studying
        mine = pg.evaluate("document.querySelector('#concept').selectedOptions[0].textContent")
        pg.fill("#q", "شو أكلة المنسف؟"); pg.click(".go"); pg.wait_for_selector(".none", timeout=8000)
        ok(f"{tag} 🆕 a question outside his book → no scene (never a wrong one) + «خلينا نرجع لـ«{mine}»» (the plan, p.19)",
           "خلينا نرجع" in pg.inner_text(".none .msg") and mine in pg.inner_text(".none .msg") and pg.locator("#goBack").count() == 1, pg.inner_text("#res")[:200])
        if SHOTS and tag == "🖥️":
            pg.screenshot(path=os.path.join(SHOTS, "ask_none.png"))
        pg.click("#goBack"); pg.wait_for_timeout(2500)
        fb = next((f for f in pg.frames if "/explain/" in f.url and "kind=meet" in f.url), None)
        bt = ""
        if fb:
            try:
                fb.wait_for_selector("#q", timeout=8000); bt = fb.inner_text("#prog .where")
            except Exception as e:   # noqa: BLE001
                bt = str(e)
        ok(f"{tag} 🆕 «↩️ ارجع» opens HIS concept's cartoon («تعرّف عليّ · {mine}»)", fb is not None and mine in bt, bt[:120])
        pg.locator(".none .sug").first.click(); pg.wait_for_selector(".hit h2", timeout=8000)
        ok(f"{tag} a suggestion (from his lesson) is a question that finds its scene", pg.locator(".hit h2").count() == 1, pg.inner_text("#res")[:120])
        # 🆕 a concept of ANOTHER book: the math student asks about pollination → not in his book → back
        pg.locator("#ex .chip", has_text="من كتاب الرياضيات").click(); pg.wait_for_selector(".none", timeout=8000); pg.wait_for_timeout(300)
        ok(f"{tag} 🆕 the math student asks «شو هو التلقيح؟» → no scene from the science book, back to his math concept",
           pg.input_value("#book") == "b_math" and "خلينا نرجع" in pg.inner_text(".none") and pg.locator(".hit").count() == 0, pg.inner_text("#res")[:160])
        # an example chip, his book
        pg.locator("#ex .chip", has_text="البسط").click(); pg.wait_for_selector(".hit h2", timeout=8000)
        pg.wait_for_timeout(300)
        ok(f"{tag} an example chip (its book): «ما الفرق بين البسط والمقام» → the compare scene", pg.inner_text(".hit h2") in ("البسط", "المقام") and "قارن" in pg.inner_text(".sc.on"),
           [pg.inner_text(".hit h2"), pg.inner_text(".sc.on")])
        w = pg.evaluate("[document.documentElement.scrollWidth, innerWidth]")
        ok(f"{tag} no sideways scroll", w[0] <= w[1] + 1, w)
        ctx.close()
    b.close()

print("\n".join(res))
print(f"✅ {sum(r.startswith('✅') for r in res)} checks passed · ❌ {sum(r.startswith('❌') for r in res)} failed")
print("JS errors:", errs[:5] or "none")
