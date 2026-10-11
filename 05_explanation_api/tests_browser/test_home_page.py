"""🆕 batch 31 — the server's FRONT PAGE (static/home.html, more professional) in a real browser.
The real service answers every request (Playwright routes them to core/service.py: the same functions FastAPI calls), so this checks
the page AND the service together, without installing FastAPI here:
  the server status · the numbers · every book as a card · filter by stage · search · send a NEW graph (the computer book) → its card ·
  delete with two clicks · copy a link · the endpoints for developers · phone width with no sideways scroll · no JS error.
Run:  python tests_browser/test_home_page.py          (from 05_explanation_api)"""
import json
import os
import sys
import tempfile
import urllib.parse

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.environ["EXPLAIN_DATA_DIR"] = tempfile.mkdtemp(prefix="explain_home_test_")
sys.path.insert(0, HERE)
from playwright.sync_api import sync_playwright  # noqa: E402

from core import service, settings  # noqa: E402

FACTORY = os.path.join(os.path.dirname(HERE), "02_question_factory")
ORIGIN = "https://ie.test"   # https: a secure page, so the clipboard works like on the real server
res, errs = [], []


def ok(n, c, x=""):
    res.append(("✅" if c else "❌") + " " + n + ("" if c else " " + str(x)[:300]))


def handle(route):
    req = route.request
    u = urllib.parse.urlparse(req.url)
    path, method = u.path, req.method
    try:
        if path == "/" and method == "GET":
            return route.fulfill(status=200, content_type="text/html; charset=utf-8", body=service.home_html())
        if path == "/health":
            return route.fulfill(status=200, content_type="application/json", body=json.dumps({"status": "ok", "version": settings.API_VERSION}))
        if path == "/books" and method == "GET":
            service.ensure_samples()
            return route.fulfill(status=200, content_type="application/json", body=json.dumps(service.list_books(), ensure_ascii=False))
        if path.startswith("/books/") and method == "DELETE":
            return route.fulfill(status=200, content_type="application/json", body=json.dumps(service.delete_book(path.split("/")[2])))
        if path == "/explanations/generate" and method == "POST":
            body = json.loads(req.post_data or "{}")
            out = service.generate(graph=body.get("graph"), use_llm=bool(body.get("use_llm")))
            return route.fulfill(status=200, content_type="application/json", body=json.dumps(out, ensure_ascii=False, default=str))
        return route.fulfill(status=404, body="not here")
    except Exception as e:   # noqa: BLE001
        return route.fulfill(status=422, content_type="application/json", body=json.dumps({"detail": str(e)}))


with sync_playwright() as p:
    b = p.chromium.launch()
    for vp in ({"width": 1300, "height": 900}, {"width": 390, "height": 844}):
        tag = "📱" if vp["width"] < 500 else "🖥️"
        ctx = b.new_context(viewport=vp, permissions=["clipboard-read", "clipboard-write"])
        pg = ctx.new_page(); pg.on("pageerror", lambda e: errs.append(str(e)[:160]))
        pg.route("**/fonts.*/**", lambda r: r.abort()); pg.route(ORIGIN + "/**", handle)
        pg.goto(ORIGIN + "/"); pg.wait_for_timeout(1500)
        ok(f"{tag} the server status shows «شغّال» + the version", "شغّال" in pg.inner_text("#status") and settings.API_VERSION in pg.inner_text("#status"), pg.inner_text("#status"))
        n = pg.evaluate("document.querySelectorAll('.book').length")
        ok(f"{tag} the 12 sample books, one card each", n == 12, n)
        ok(f"{tag} the numbers: books / scenes", pg.inner_text("#sBooks").strip() == "١٢" and pg.inner_text("#sScenes").strip() not in ("—", "٠"), (pg.inner_text("#sBooks"), pg.inner_text("#sScenes")))
        pg.click('.tab[data-st="senior"]'); pg.wait_for_timeout(150)
        sen = pg.evaluate("document.querySelectorAll('.book').length")
        ok(f"{tag} the «📐 ثانوي» filter keeps only the secondary books ({sen})", 0 < sen < 12 and all("ثانوي" in t for t in pg.evaluate("[...document.querySelectorAll('.book .tag.st')].map(t=>t.textContent)")))
        pg.click('.tab[data-st=""]'); pg.fill("#q", "كيمياء"); pg.wait_for_timeout(150)
        ok(f"{tag} search «كيمياء» finds the chemistry books", 0 < pg.evaluate("document.querySelectorAll('.book').length") < 12, pg.evaluate("document.querySelectorAll('.book').length"))
        pg.fill("#q", ""); pg.wait_for_timeout(100)
        sw = pg.evaluate("document.documentElement.scrollWidth")
        ok(f"{tag} no sideways scroll", sw <= vp["width"], sw)
        pg.screenshot(path=os.path.join(tempfile.gettempdir(), f"home_{vp['width']}.png"), full_page=False)
        if vp["width"] > 500:
            # send a NEW graph (the computer book) from the page
            pg.click("#go"); pg.wait_for_timeout(150)
            ok("🖥️ «اعمل الشرح» with nothing → a clear message (no crash)", "اختار ملف" in pg.inner_text("#out"), pg.inner_text("#out"))
            pg.set_input_files("#file", os.path.join(FACTORY, "examples", "new_subject_computer_g7.json")); pg.wait_for_timeout(300)
            ok("🖥️ the chosen file's name shows", "new_subject_computer_g7.json" in pg.inner_text("#fname"))
            pg.click("#go"); pg.wait_for_selector("#out.ok", timeout=60000)
            out = pg.inner_text("#out")
            ok("🖥️ new graph → ✅ its title, lessons, scenes, and «🆕 مادة جديدة» with its mascot", "✅" in out and "مادة جديدة" in out and "مشهد" in out, out)
            pg.wait_for_timeout(600)
            ok("🖥️ …and its card appears in the books (13)", pg.evaluate("document.querySelectorAll('.book').length") == 13 and pg.inner_text("#sNew").strip() == "١")
            # copy a link
            pg.locator(".book .cp").first.click(); pg.wait_for_timeout(200)
            clip = pg.evaluate("navigator.clipboard.readText()")
            ok("🖥️ «🔗 نسخ الرابط» copies the book's page link", clip.startswith(ORIGIN + "/explain/"), clip)
            # delete with two clicks
            card = pg.locator(".book", has_text="الحاسوب")
            card.locator(".del").click(); pg.wait_for_timeout(100)
            ok("🖥️ delete: the first click only asks «متأكد؟»", "متأكد" in card.locator(".del").inner_text() and pg.evaluate("document.querySelectorAll('.book').length") == 13)
            card.locator(".del").click(); pg.wait_for_timeout(800)
            ok("🖥️ …the second click deletes it", pg.evaluate("document.querySelectorAll('.book').length") == 12)
            ok("🖥️ the developers' part lists the main endpoints + a curl example with this server's address",
               pg.evaluate("document.querySelectorAll('#dev .ep').length") >= 6 and (ORIGIN + "/explanations/generate") in pg.inner_text("#curl"))
        ctx.close()
    b.close()
print("\n".join(r for r in res if r.startswith("❌")) or "")
print(f"✅ {sum(r.startswith('✅') for r in res)} checks passed · ❌ {sum(r.startswith('❌') for r in res)} failed")
print("JS errors:", errs or "none")
