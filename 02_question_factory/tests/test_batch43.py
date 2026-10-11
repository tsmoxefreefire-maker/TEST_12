"""🆕 batch 43 (Hareth: «زيد لنا رسمات بحيث إنها تغطي مفاهيم كثيرة جداً… وكمان الـ AI ياخذ من الليجو»):
  · the library is MUCH bigger (10 new families: everyday, money, mind, physics, geo, ecology, tech, civics, math2, english2) and still clean;
  · most of the Saudi concepts have a drawing of their own now (the meter: art_coverage.py);
  · one word = a different drawing in each subject («البؤرة», «المحور», «الشعر»…), and the new generic words never take a concept
    that already had its own good picture («الجهاز الهضمي» stays the stomach, «مسلمة التوازي» stays the parallel lines);
  · the 12 sample books keep EXACTLY their pictures;
  · the model also looks at the WEAK pictures (found only from a word of the meaning): it builds a better one from parts, or says «keep»;
  · 🕵️ «مين أنا؟» and 🧩 «ركّب الجملة»: two new activities for the concepts with few scenes (only the name and the meaning)."""
import hashlib
import json
import os
import re
import tempfile
import unittest

import art_coverage
import art_library
import build_all_books
import explain_activities3 as a3
import explain_generator as eg
import lego
import scene_questions
import offline_generator as og
from graph_reader import Graph

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NEW_FAMILIES = ("everyday", "money", "mind", "physics", "geo", "ecology", "tech", "civics", "math2", "english2")
BOOKS_FINGERPRINT = "6d4021ce6a2f9f63"      # the 12 books' pictures before batch 43 (107 concepts) — they must not change


def books_fingerprint():
    rows = []
    for gf in build_all_books.BOOKS:
        g = Graph.load(os.path.join(HERE, gf))
        for c in sorted(g.concepts.values(), key=lambda c: c.id):
            if og.is_entity(g, c.id):
                rows.append(f"{gf}|{c.id}|" + og.icon_for(c.text, c.description, str(g.book.get("subject", ""))))
    return len(rows), hashlib.sha256("\n".join(rows).encode()).hexdigest()[:16]


class TestBiggerLibrary(unittest.TestCase):
    def test_the_library_is_bigger_and_clean(self):
        self.assertEqual(art_library.problems(), [])                       # only simple shapes, inside the box, a face, words, no duplicate word
        self.assertGreaterEqual(len(art_library.drawings()), 1400)
        fams = {r["family"] for r in art_library.drawings().values()}
        self.assertTrue(set(NEW_FAMILIES) <= fams)
        for k, r in art_library.drawings().items():
            if r["family"] in NEW_FAMILIES:
                self.assertNotIn("<script", r["body"]); self.assertNotIn("href", r["body"])
                for t in re.findall(r"<text\b[^>]*>", r["body"]):
                    self.assertIn('direction="ltr"', t, k)                     # «⁺H₃O», «C°» are never turned around on the Arabic page

    def test_most_saudi_concepts_have_their_own_drawing(self):
        res = art_coverage.measure(art_coverage.saudi_concepts())
        _, pct, n = art_coverage.table(res)
        self.assertGreater(n, 7000)
        self.assertGreaterEqual(pct["own"], 90)                              # 78% before batch 43
        self.assertLessEqual(pct["subject"], 6)


class TestOneWordManyMeanings(unittest.TestCase):
    CASES = [("physics", "البؤرة", "lib:phys.focus_lens"), ("earth science", "البؤرة", "lib:geo.epicenter"), ("math", "البؤرة", "lib:math2.parabola_focus"),
             ("biology", "المحور", "lib:bio.neuron"), ("science", "المحور", "lib:eco.earth_axis"),
             ("life skills", "الشعر", "lib:day.comb"), ("social studies", "الشعر", "lib:civ.poetry"),
             ("science", "البطين", "lib:eco.atrium"), ("math", "التربيع", "lib:math2.power"), ("social studies", "رعاية كبار السن", "lib:eco.old_age"),
             ("english", "كنزة صوفية", "lib:en.shirt"), ("physics", "الانشطار النووي", "lib:mat.nuclear"), ("physics", "التطعيم (الإشابة)", "lib:phys.bands")]

    def test_each_subject_gets_its_own_meaning(self):
        for subject, name, want in self.CASES:
            self.assertEqual(og.icon_for(name, "", subject), want, (subject, name))

    def test_new_generic_words_never_take_a_good_old_picture(self):
        keep = [("science", "الجهاز الهضمي", "lib:body.stomach"), ("science", "الجهاز التنفسي", "lib:body.lungs"),
                ("science", "الكتلة الهوائية", "lib:earth.airmass"), ("biology", "القصبة الهوائية", "lib:body.lungs"),
                ("math", "مسلمة التوازي", "lib:math.parallel"), ("math", "مسلمة التطابق SSS", "lib:math.congruent"),
                ("math", "مركز التمدد", "lib:math.dilation"), ("science", "التطعيم", "lib:body.vaccine"), ("science", "الرافعة", "lib:mat.lever"),
                ("social studies", "القيم الشخصية", "lib:soc.values"), ("social studies", "السكان", "lib:soc.population"),
                ("chemistry", "ثابت الغاز المثالي", "lib:mat.gaslaws"), ("earth science", "مقياس العزم الزلزالي", "lib:earth.earthquake")]
        for subject, name, want in keep:
            self.assertEqual(og.icon_for(name, "", subject), want, (subject, name))

    def test_no_cartoon_from_a_name_that_only_looks_like_a_word(self):
        for subject, name in (("social studies", "عمر بن عبدالعزيز"), ("social studies", "بلاد السند"), ("computer", "وحدة التحكم المركزية")):
            self.assertTrue(og.icon_for(name, "", subject).startswith("subj:"), name)     # not a birthday cake, not a bond, not the Scratch block

    def test_the_12_books_keep_their_pictures(self):
        self.assertEqual(books_fingerprint(), (107, BOOKS_FINGERPRINT))


def fake_model(answer_for):
    """Reads the names from the prompt; answer_for(name) → an item (options or keep). Counts its calls, keeps the prompts."""
    calls = []

    def llm(system, user):
        calls.append(user)
        names = re.findall(r"^  (.+?) — ", user, re.M)
        return json.dumps({"items": [dict(answer_for(n), name=n) for n in names]}, ensure_ascii=False)
    llm.calls = calls
    return llm


class TestTheModelLooksAtWeakPictures(unittest.TestCase):
    WEAK = ("الكركبة", "خليط فيه الماء والسكر")          # no drawing by its NAME: only «الماء» of its meaning → the water drop (weak)

    def setUp(self):
        self.store = tempfile.mktemp(suffix=".json")
        lego.set_store(self.store)

    def tearDown(self):
        if os.path.exists(self.store):
            os.remove(self.store)

    def test_weak_and_strong_ways(self):
        self.assertEqual(og.icon_source(*self.WEAK, "الطبخ"), ("💧", "meaning"))
        self.assertIn("meaning", og.WEAK); self.assertIn("subject", og.WEAK)
        self.assertEqual(og.icon_source("الفرن", "", "life skills")[1], "library")
        self.assertEqual(og.icon_label("lib:day.oven"), "الفرن")
        self.assertTrue(og.icon_label("subj:🔹:x").startswith("the subject's character"))

    def test_the_model_sees_the_weak_picture_and_builds_a_better_one(self):
        name, meaning = self.WEAK
        llm = fake_model(lambda n: {"metaphor": "خلاط", "options": [{"main": "pot", "extras": ["spark"]}]})
        out = lego.ask_model([name], llm, "الطبخ", {name: meaning}, current={name: og.icon_label("💧")})
        self.assertIn("now shows «💧»", llm.calls[0])                       # the model is told what is shown now
        self.assertTrue(out[name].startswith("lego:pot:spark:"))
        self.assertEqual(og.icon_source(name, meaning, "الطبخ"), (out[name], "lego"))   # a BUILT drawing beats a word of the meaning

    def test_keep_is_saved_and_never_asked_again(self):
        name, meaning = self.WEAK
        llm = fake_model(lambda n: {"keep": True})
        self.assertEqual(lego.ask_model([name], llm, "الطبخ", {name: meaning}, current={name: "💧"}), {name: None})
        self.assertTrue(lego.kept(name))
        self.assertEqual(og.icon_source(name, meaning, "الطبخ"), ("💧", "meaning"))       # the picture stays
        self.assertEqual(lego.ask_model([name], llm, "الطبخ", {name: meaning}, current={name: "💧"}), {})
        self.assertEqual(len(llm.calls), 1)                                  # no second cost
        with self.assertRaises(ValueError):
            lego.choose(name, pick=0)                                        # nothing to pick for a «keep»

    def test_keep_only_for_a_picture_we_showed(self):
        llm = fake_model(lambda n: {"keep": True})                           # «keep» for a concept that had NO picture: ignored
        self.assertEqual(lego.ask_model(["التخمير"], llm, "الطبخ"), {})
        self.assertFalse(lego.kept("التخمير"))
        self.assertNotIn("now shows", llm.calls[0])                          # no weak picture → no review text

    def test_the_teachers_no_is_never_asked_again(self):
        lego.ask_model(["التخمير"], fake_model(lambda n: {"options": [{"main": "pot"}, {"main": "cube"}]}), "الطبخ")
        lego.choose("التخمير", reject=True)
        llm = fake_model(lambda n: {"options": [{"main": "bag"}]})
        self.assertEqual(lego.ask_model(["التخمير"], llm, "الطبخ"), {})
        self.assertEqual(llm.calls, [])                                      # the model is not asked behind the teacher's back
        self.assertTrue(og.icon_for("التخمير", "", "الطبخ").startswith("subj:"))


class TestTwoNewActivities(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.found = []                                                       # (graph, lesson, concept record, scene)
        for gf in build_all_books.BOOKS:
            g = Graph.load(os.path.join(HERE, gf))
            for les in g.lessons():
                for c in eg.explain_lesson(g, les)["concepts"]:
                    for s in c["scenes"]:
                        if s["kind"] in a3.KINDS:
                            cls.found.append((g, les, c, s))

    def test_both_are_made_and_true_to_the_graph(self):
        kinds = {s["kind"] for _, _, _, s in self.found}
        self.assertEqual(kinds, {"who_am_i", "sentence"})
        for g, les, c, s in self.found:
            self.assertEqual(eg.check_scene(g, s), [], (c["title"], s["kind"]))

    def test_only_for_the_concepts_with_few_scenes(self):
        for g, les, c, s in self.found:
            self.assertLessEqual(len(c["scenes"]), a3.FEW + 1, c["title"])      # it came because there were few
            self.assertIs(c["scenes"][-1], s)                                    # after the other scenes (learn first, then find it again)

    def test_the_clues_never_say_the_answer_and_no_wrong_card_fits(self):
        for g, les, c, s in self.found:
            if s["kind"] != "who_am_i":
                continue
            name = g.concepts[s["target"]].text
            for cl in s["clues"]:
                self.assertNotIn(name, cl["say"].replace(f"«{name}»", "X") if cl["type"] != "def" else cl["say"], (name, cl))
            self.assertEqual([o["id"] for o in s["options"] if o["ok"]], [s["target"]])
            self.assertEqual(len(s["options"]), 3)
            for o in s["options"]:
                if not o["ok"]:
                    self.assertIn(g.concepts[o["id"]].text, o["why"])          # a wrong card says what THAT one is
                    self.assertNotIn(o["id"], {cl.get("ref") for cl in s["clues"]})

    def test_the_sentence_is_the_meaning_cut_in_good_places(self):
        for g, les, c, s in self.found:
            if s["kind"] != "sentence":
                continue
            self.assertIn(len(s["chunks"]), (3, 4))
            self.assertEqual(" ".join(s["chunks"]), s["sentence"])
            for ch in s["chunks"][:-1]:
                self.assertNotIn(ch.split()[-1], a3._SMALL, s["chunks"])        # never a lonely «على» / «التي» at the end of a piece

    def test_a_broken_one_is_caught(self):
        g, les, c, s = next(x for x in self.found if x[3]["kind"] == "who_am_i")
        bad = json.loads(json.dumps(s))
        for o in bad["options"]:
            o["ok"] = not o["ok"]
        self.assertTrue(eg.check_scene(g, bad))
        g, les, c, s = next(x for x in self.found if x[3]["kind"] == "sentence")
        bad = dict(s, chunks=list(reversed(s["chunks"])))
        self.assertTrue(eg.check_scene(g, bad))

    def test_the_search_and_the_contract_know_them(self):
        g, les, c, s = self.found[0]
        self.assertTrue(scene_questions.questions(g, les.title, s["target"], s))
        sys_path = os.path.join(os.path.dirname(HERE), "05_explanation_api", "core", "contract.py")
        with open(sys_path, encoding="utf-8") as f:
            txt = f.read()
        self.assertIn('"who_am_i":', txt); self.assertIn('"sentence":', txt)

    def test_the_page_has_them_and_they_are_the_students(self):
        with open(os.path.join(HERE, "player", "explain_template.html"), encoding="utf-8") as f:
            page = f.read()
        self.assertIn("SCENES.who_am_i=sceneWhoAmI", page); self.assertIn("SCENES.sentence=sceneSentence", page)
        self.assertRegex(page, r"const HANDS=\{[^}]*who_am_i:1,sentence:1")


if __name__ == "__main__":
    unittest.main()
