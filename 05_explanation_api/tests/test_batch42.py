"""🆕 batch 42: the database and «ask a question → the scene at once» (the engineer's idea + Render's disk that forgets).
    PYTHONPATH=tests/local_stub_only_for_sandbox python -m unittest tests.test_batch42
The database part runs against a REAL PostgreSQL when TEST_DATABASE_URL is set (here: a local server + the stub driver in
tests/local_stub_only_for_sandbox/psycopg; on a real machine: pip install "psycopg[binary]"); without it, that part is skipped."""
import hashlib
import json
import os
import shutil
import statistics
import sys
import tempfile
import unittest
from unittest import mock

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, HERE)
os.environ.setdefault("EXPLAIN_SEED", "0")
from core import db, embed, scene_index, service, settings, storage  # noqa: E402
import scene_questions as sq  # noqa: E402

# (question, HIS book, the concept that must answer · None = «no scene») — 🆕 batch 43: always inside his book
CASES = [
    ("شو بيحتاج التلقيح؟", "sci_g4", "التلقيح"), ("ليش الجذور مهمة للنبتة", "sci_g4", "الجذر"), ("شو يعني الإنبات", "sci_g4", "الإنبات"),
    ("ليش النبتة بدها شمس", "sci_g4", "ضوء الشمس"), ("شو هو الكسر", "b_math", "الكسر"), ("ما الفرق بين البسط والمقام", "b_math", "البسط|المقام"),
    ("كيف بنضرب الأعداد", "b_math", "الضرب"), ("ما هي الجملة الاسمية", "ara", "الجملة الاسمية"), ("شو الفرق بين المبتدأ والخبر", "ara", "المبتدأ|الخبر"),
    ("ليش بنو الأهرام", "b", "الأهرامات"), ("كم قارة في العالم", "geo", "القارات"), ("شو الفرق بين الطقس والمناخ", "geo", "الطقس|المناخ"),
    ("شو هي الجاذبية", "phy", "الجاذبية"), ("كيف بيشتغل المغناطيس", "phy", "المغناطيس"), ("ما هو الحمض", "che", "الحمض"),
    ("شو بتعمل الميتوكندريا", "sci_g8", "الميتوكندريا"), ("كيف بحسب الميل", "math_g9", "الميل"), ("شو الفرق بين المسافة والإزاحة", "phy_g10", "المسافة|الإزاحة"),
    ("كيف بتتكون الرابطة الأيونية", "chem_g11", "الرابطة الأيونية"), ("كيف بنستعمل مربع بانيت", "bio_g12", "مربع بانيت"),
    ("شو أكلة المنسف", "sci_g4", None), ("مين ربح كاس العالم", "geo", None), ("كيف بعمل حساب انستغرام", "che", None),
    ("شو هو التلقيح", "b_math", None), ("شو هو الجين", "sci_g4", None),            # 🆕 in the platform, but NOT in his book → no scene
]


def _use_dir(d):
    settings.DATA_DIR, settings.GRAPHS_DIR, settings.BOOKS_DIR = d, os.path.join(d, "graphs"), os.path.join(d, "books")
    scene_index.forget()


class _Base(unittest.TestCase):
    provider = "none"

    @classmethod
    def setUpClass(cls):
        cls.old = (settings.DATA_DIR, settings.GRAPHS_DIR, settings.BOOKS_DIR, os.environ.get("EMBED_PROVIDER"), os.environ.get("DATABASE_URL"))
        cls.tmp = tempfile.mkdtemp()
        _use_dir(cls.tmp)
        os.environ["EMBED_PROVIDER"] = cls.provider
        os.environ.pop("DATABASE_URL", None)
        cls.made = service.seed_samples()

    @classmethod
    def tearDownClass(cls):
        settings.DATA_DIR, settings.GRAPHS_DIR, settings.BOOKS_DIR = cls.old[:3]
        for k, v in (("EMBED_PROVIDER", cls.old[3]), ("DATABASE_URL", cls.old[4])):
            os.environ.pop(k, None) if v is None else os.environ.__setitem__(k, v)
        scene_index.forget()
        shutil.rmtree(cls.tmp, ignore_errors=True)


class Ask(_Base):
    """no database, no meaning model: the name and the spelling only (free)."""

    def test_every_scene_of_every_book_can_be_found(self):
        for m in self.made:
            want = sum(1 for lid in storage.lesson_ids(m["book_id"]) for rec in [storage.load_lesson(m["book_id"], lid)]
                       for _ in [x for x in (rec["overview"], rec.get("world"), rec.get("assemble")) if x] + [s for c in rec["concepts"] for s in c["scenes"]])
            self.assertEqual(m["search"]["rows"], want, m["book_id"])
        self.assertEqual(scene_index.status()["rows"], sum(m["search"]["rows"] for m in self.made))

    def test_the_description_is_questions_in_dialect_and_fusha(self):
        rows = db.scenes().all_rows()
        meet = next(r for r in rows if r["kind"] == "meet")
        self.assertTrue(any(q.startswith("شو هو") for q in meet["questions"]) and any(q.startswith("ما هو") for q in meet["questions"]))
        self.assertTrue(all(r["description"] and r["questions"] for r in rows))
        wi = next(r for r in rows if r["kind"] == "what_if")
        self.assertTrue(any("بدون" in q for q in wi["questions"]))

    def test_the_right_scene_for_the_question(self):
        bad = []
        for q, book, want in CASES:
            a = service.ask(q, book_id=book)
            got = a.get("name") if a["found"] else None
            if not ((want is None and got is None) or (want and got in want.split("|"))):
                bad.append((q, got, want))
        self.assertEqual(bad, [])

    def test_far_questions_get_no_scene_and_suggestions(self):
        a = service.ask("شو أكلة المنسف", book_id="sci_g4")
        self.assertFalse(a["found"])
        self.assertTrue(a["suggestions"] and a["message"])

    def test_his_book_only(self):
        """🆕 batch 43 (Hareth: «لازم يسأل عن مشهد في نفس الكتاب، إذا برّا لازم نمنعه»)."""
        self.assertTrue(service.ask("شو هو الجين", book_id="bio_g12")["found"])
        self.assertFalse(service.ask("شو هو الجين", book_id="sci_g4")["found"], "a grade-4 student never gets the grade-12 gene")
        self.assertFalse(service.ask("شو هو التلقيح", book_id="b_math")["found"], "the math book never answers with the science book")
        self.assertEqual(service.ask("شو هي الذرة", book_id="chem_g11")["book_id"], "chem_g11")
        self.assertEqual(service.ask("شو هي الذرة", book_id="che")["book_id"], "che")
        with self.assertRaises(service.BadInput):
            service.ask("شو هو التلقيح")                                   # no book → refused (never «every book»)

    def test_outside_his_book_he_goes_back_to_his_concept(self):
        """🆕 batch 43 — the plan (AI Tutor p.19): «أقدر أساعدك في موضوع الدرس، لكن خلينا نرجع للنقطة اللي بنذاكرها»."""
        rec = next(storage.load_lesson("b_math", l) for l in storage.lesson_ids("b_math"))
        lid, c = rec["lesson_id"], rec["concepts"][0]
        a = service.ask("مين ربح كاس العالم", book_id="b_math", lesson_id=lid, concept_id=c["concept_id"])
        self.assertFalse(a["found"])
        self.assertEqual((a["back"]["concept_id"], a["back"]["lesson_id"]), (c["concept_id"], lid))
        self.assertIn(f"«{c['title']}»", a["message"])
        self.assertIn("خلينا نرجع", a["message"])
        self.assertTrue(a["back"]["page_url"].startswith("/explain/b_math?") and f"concept={c['concept_id']}" in a["back"]["page_url"])
        self.assertIn("kind=meet", a["back"]["page_url"], "back to the concept's cartoon (its first scene)")
        self.assertTrue(set(a["suggestions"]) <= {x["title"] for x in rec["concepts"]}, "the suggestions are from HIS lesson")
        b = service.ask("مين ربح كاس العالم", book_id="b_math", lesson_id=lid)
        self.assertEqual((b["back"]["concept_id"], b["back"]["name"]), ("", rec["lesson_title"]), "only the lesson known → back to its start")

    def test_his_lesson_comes_first(self):
        a = service.ask("شو بيحتاج التلقيح؟", book_id="sci_g4", concept_id="pollination")
        self.assertTrue(a["found"] and a["in_his_lesson"])

    def test_only_the_asked_book_is_in_memory(self):
        scene_index.forget()
        service.ask("شو هو الكسر", book_id="b_math")
        self.assertEqual(list(scene_index._C["books"]), ["b_math"])
        with mock.patch.object(scene_index, "MAX_BOOKS", 2):
            for b in ("sci_g4", "geo", "phy"):
                service.ask("شو هو", book_id=b)
            self.assertEqual(list(scene_index._C["books"]), ["geo", "phy"], "the least recently asked book leaves first")

    def test_which_scene_of_the_concept(self):
        a = service.ask("شو بيصير لو ما في التلقيح", book_id="sci_g4")
        self.assertEqual(a["scenes"][a["start"]]["kind"], "what_if")
        a = service.ask("شو هو التلقيح", book_id="sci_g4")
        self.assertEqual(a["scenes"][a["start"]]["kind"], "meet")
        self.assertEqual(a["scenes"][0]["kind"], "meet", "the concept's scenes come in order: the cartoon first")

    def test_the_link_opens_the_page_there(self):
        a = service.ask("شو بيصير لو ما في التلقيح", book_id="sci_g4")
        for part in (f"/explain/{a['book_id']}?", f"lesson={a['lesson_id']}", f"concept={a['concept_id']}", "kind=what_if", "at="):
            self.assertIn(part, a["page_url"])

    def test_word_forms(self):
        for name, q in (("الجذر", "ليش الجذور مهمة"), ("البذرة", "وين البذور"), ("القارات", "كم قارة"), ("الضرب", "كيف بنضرب"),
                        ("الكسر", "بين كسرين"), ("الأيون", "الأيونات"), ("السقوط الحر", "السقوط الحر")):
            self.assertTrue(sq.name_in(name, q), (name, q))
        for name, q in (("الماء", "المائدة"), ("الفاعل", "شو هو التفاعل"), ("الساق", "السوق"), ("ضوء الشمس", "بدها شمس")):
            self.assertFalse(sq.name_in(name, q), (name, q))

    def test_fast(self):
        ms = [service.ask(q, book_id=b)["ms"] for q, b, _ in CASES]
        self.assertLess(statistics.median(ms), 50, ms)

    def test_only_what_changed_is_written_again(self):
        b = self.made[0]["book_id"]
        self.assertEqual(scene_index.index_book(b)["written"], 0)
        with mock.patch.object(sq, "VERSION", "q-test"):
            r = scene_index.index_book(b)
        self.assertEqual(r["written"], r["rows"], "new questions → every row of the book again")
        scene_index.index_book(b)

    def test_a_deleted_book_leaves_the_search(self):
        g = json.load(open(os.path.join(settings.SAMPLES_DIR, "history_book_graph.json"), encoding="utf-8"))
        g = dict(g, book=dict(g["book"], id="hist_copy"))
        service.generate(graph=g)
        self.assertEqual(service.ask("مين هم الفراعنة", book_id="hist_copy")["book_id"], "hist_copy")
        service.delete_book("hist_copy")
        self.assertFalse(any(r["book_id"] == "hist_copy" for r in db.scenes().all_rows()))


class Meaning(_Base):
    """the meaning model: wired, used once per row and once per question, never needed (the pretend model: no key, no internet)."""
    provider = "fake"

    def test_every_row_got_its_numbers_once(self):
        st = scene_index.status()
        self.assertEqual(st["embedded_rows"], st["rows"])
        n = embed.CALLS["n"]
        for m in self.made:
            self.assertEqual(scene_index.index_book(m["book_id"])["embedded"], 0, "a row that did not change keeps its numbers")
        self.assertEqual(embed.CALLS["n"], n)

    def test_a_question_asked_again_costs_nothing(self):
        service.ask("سؤال جديد عن النباتات والضوء", book_id="sci_g4")
        n = embed.CALLS["n"]
        service.ask("سؤال جديد عن النباتات والضوء", book_id="sci_g4")
        self.assertEqual(embed.CALLS["n"], n)

    def test_the_meaning_step(self):
        """a question with no name in it: the row the meaning model points to answers it (how = meaning)."""
        B = scene_index._load("sci_g4")
        rows = B["rows"]
        k = next(i for i, r in enumerate(rows) if r["kind"] == "play")
        vec = B["mat"][B["ids"].index(k)]
        with mock.patch.object(embed, "query", return_value=list(map(float, vec))):
            a = service.ask("وين بتطير النحلة؟", book_id="sci_g4")
        self.assertEqual((a["how"], a["name"], a["scenes"][a["start"]]["kind"]), ("meaning", rows[k]["name"], "play"))

    def test_the_real_providers_requests(self):
        """Gemini and OpenAI: the request we send and how we read the answer (no internet: the reply is pretended)."""
        seen = []

        def fake_post(url, body, headers):
            seen.append((url, body, headers))
            if "googleapis" in url:
                return {"embeddings": [{"values": [3.0, 4.0] + [0.0] * (embed.DIM - 2)} for _ in body["requests"]]}
            return {"data": [{"index": i, "embedding": [0.0] * (embed.DIM - 1) + [2.0]} for i, _ in enumerate(body["input"])]}

        for p, key in (("gemini", "GEMINI_API_KEY"), ("openai", "OPENAI_API_KEY")):
            with mock.patch.dict(os.environ, {"EMBED_PROVIDER": p, key: "test-key-not-real"}), mock.patch.object(embed, "_post", fake_post):
                v = embed.embed(["مرحبا", "سؤال"], "query")
            self.assertEqual(len(v), 2)
            self.assertAlmostEqual(sum(x * x for x in v[0]), 1.0, places=5)
        g_url, g_body, g_head = seen[0]
        self.assertIn(":batchEmbedContents", g_url)
        self.assertEqual(g_body["requests"][0]["output_dimensionality"], embed.DIM)
        self.assertTrue(g_body["requests"][0]["content"]["parts"][0]["text"].startswith("task: search result | query: "))
        self.assertEqual(g_head["x-goog-api-key"], "test-key-not-real")
        o_url, o_body, o_head = seen[1]
        self.assertTrue(o_url.endswith("/v1/embeddings"))
        self.assertEqual((o_body["dimensions"], o_body["input"]), (embed.DIM, ["مرحبا", "سؤال"]))
        self.assertEqual(o_head["Authorization"], "Bearer test-key-not-real")

    def test_no_key_no_meaning_and_nothing_breaks(self):
        with mock.patch.dict(os.environ, {"EMBED_PROVIDER": "gemini"}), mock.patch.object(embed, "_keys", return_value={}):
            self.assertEqual(embed.provider(), "none")
            self.assertTrue(service.ask("شو بيحتاج التلقيح؟", book_id="sci_g4")["found"])


@unittest.skipUnless(os.environ.get("TEST_DATABASE_URL"), "set TEST_DATABASE_URL (a PostgreSQL to test with)")
class Database(unittest.TestCase):
    """a REAL PostgreSQL: everything is kept, and comes back after a restart with an empty disk."""

    @classmethod
    def setUpClass(cls):
        cls.old = (settings.DATA_DIR, settings.GRAPHS_DIR, settings.BOOKS_DIR, os.environ.get("DATABASE_URL"), os.environ.get("EMBED_PROVIDER"))
        os.environ["DATABASE_URL"] = os.environ["TEST_DATABASE_URL"]
        os.environ["EMBED_PROVIDER"] = "fake"
        db.close()
        db.run("DROP TABLE IF EXISTS ie_scenes")
        db.run("DROP TABLE IF EXISTS ie_files")
        db.close()                                                     # (the tables are made again on the next connection)
        db._MANIFEST.clear()
        cls.a, cls.b = tempfile.mkdtemp(), tempfile.mkdtemp()
        _use_dir(cls.a)
        cls.made = [service.generate(graph_path=n) for n in ("plants_book_graph.json", "chem_g7_book_graph.json")]
        cls.page = hashlib.sha1(service.page_html().encode()).hexdigest()

    @classmethod
    def tearDownClass(cls):
        settings.DATA_DIR, settings.GRAPHS_DIR, settings.BOOKS_DIR = cls.old[:3]
        for k, v in (("DATABASE_URL", cls.old[3]), ("EMBED_PROVIDER", cls.old[4])):
            os.environ.pop(k, None) if v is None else os.environ.__setitem__(k, v)
        db.close()
        db._MANIFEST.clear()
        scene_index.forget()
        for d in (cls.a, cls.b):
            shutil.rmtree(d, ignore_errors=True)

    def test_1_the_rows_and_the_files_are_in_the_database(self):
        n, e = db.run("SELECT count(*), count(emb) FROM ie_scenes").fetchone()
        self.assertEqual(n, sum(m["search"]["rows"] for m in self.made))
        self.assertEqual(e, n)
        paths = {p for (p,) in db.run("SELECT path FROM ie_files").fetchall()}
        self.assertTrue({"graphs/sci_g4.json", "books/sci_g4/meta.json"} <= paths, sorted(paths)[:5])

    def test_2_a_restart_with_an_empty_disk_loses_nothing(self):
        _use_dir(self.b)                                               # Render after a restart: data/ is empty
        db._MANIFEST.clear()
        self.assertEqual(os.listdir(self.b), [])
        r = service.boot()
        self.assertGreater(r["restored_files"], 5)
        self.assertEqual({m["book_id"] for m in service.list_books()}, {"sci_g4", "che"})
        self.assertEqual(hashlib.sha1(service.page_html().encode()).hexdigest(), self.page, "the same page as before the restart")
        a = service.ask("شو بيحتاج التلقيح؟", book_id="sci_g4")
        self.assertEqual((a["found"], a["how"], a["name"]), (True, "name", "التلقيح"))

    def test_3_a_deleted_book_leaves_the_database(self):
        service.delete_book("che")
        self.assertEqual(db.run("SELECT count(*) FROM ie_scenes WHERE book_id = %s", ["che"]).fetchone()[0], 0)
        self.assertEqual(db.run("SELECT count(*) FROM ie_files WHERE path LIKE %s", ["books/che/%%"]).fetchone()[0], 0)

    def test_4_the_database_down_never_stops_a_book(self):
        with mock.patch.dict(os.environ, {"DATABASE_URL": "postgresql://postgres@127.0.0.1:1/nothing"}):
            db.close()
            r = service.generate(graph_path="math_book_graph.json")
            self.assertTrue(r["lessons"])
            self.assertTrue(any("البحث" in w for w in r["warnings"]))
        db.close()


class API(unittest.TestCase):
    """the endpoints (FastAPI, or the local stub here)."""

    @classmethod
    def setUpClass(cls):
        try:
            from fastapi.testclient import TestClient
            from main import app
        except ImportError:
            raise unittest.SkipTest("pip install -r requirements.txt")
        cls.old = (settings.DATA_DIR, settings.GRAPHS_DIR, settings.BOOKS_DIR)
        cls.tmp = tempfile.mkdtemp()
        _use_dir(cls.tmp)
        cls.c = TestClient(app)
        cls.c.post("/explanations/generate", json={"graph_path": "plants_book_graph.json"})

    @classmethod
    def tearDownClass(cls):
        settings.DATA_DIR, settings.GRAPHS_DIR, settings.BOOKS_DIR = cls.old
        scene_index.forget()
        shutil.rmtree(cls.tmp, ignore_errors=True)

    def test_ask(self):
        r = self.c.post("/ask", json={"question": "شو بيحتاج التلقيح؟", "book_id": "sci_g4"})
        self.assertEqual(r.status_code, 200)
        a = r.json()
        self.assertTrue(a["found"] and a["scenes"] and a["page_url"].startswith("/explain/sci_g4?"))
        self.assertEqual(self.c.post("/ask", json={"question": "  "}).status_code, 400)
        self.assertEqual(self.c.post("/ask", json={"question": "شو هو التلقيح"}).status_code, 400, "🆕 batch 43: no book → refused")
        r = self.c.post("/ask", json={"question": "مين ربح كاس العالم", "book_id": "sci_g4", "concept_id": "pollination"}).json()
        self.assertEqual((r["found"], r["back"]["concept_id"]), (False, "pollination"))
        self.assertEqual(self.c.post("/ask", json={"question": "شو", "book_id": "nothing"}).status_code, 404)

    def test_the_page_status_and_health(self):
        self.assertIn("اسأل سؤال", self.c.get("/ask").text)
        st = self.c.get("/search/status").json()
        self.assertGreater(st["rows"], 10)
        self.assertEqual(self.c.get("/health").json()["storage"], "files")
        self.assertEqual(self.c.post("/search/reindex", params={"book_id": "sci_g4"}).json()[0]["written"], 0)


if __name__ == "__main__":
    unittest.main()
