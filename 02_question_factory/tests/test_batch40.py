"""🆕 batch 40 (Hareth: «المكتبة لازم نوسّعها… تغطي كل الدروس وكل المواد» + «المنهج السعودي» + «مفهوم إله رسمة… ليش مليون رسمة؟»
+ «المواد الإسلامية لا تقرب إلها»): the growing library of drawings, the alias table, the coverage of the Saudi curriculum.
python -m unittest tests.test_batch40"""
import json
import os
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
import art_coverage  # noqa: E402
import art_library  # noqa: E402
import explain_generator as eg  # noqa: E402
import offline_generator as og  # noqa: E402
from graph_reader import Graph  # noqa: E402


def icon(name, subject):
    return og.icon_for(name, "", subject)


class Batch40(unittest.TestCase):
    def test_every_drawing_is_clean(self):
        self.assertEqual(art_library.problems(), [], "only simple SVG shapes, inside the box, a face, words, no word taken twice")
        self.assertGreaterEqual(len(art_library.drawings()), 600)

    def test_saudi_curriculum_without_islamic_subjects(self):
        items = art_coverage.saudi_concepts()
        self.assertGreater(len({n for _, _, n in items}), 6000, "the concepts of the Saudi books (grades 1–12)")
        keys = {k for k, _, _ in items}
        self.assertFalse(keys & {"islamic", "quran", "tawhid", "fiqh", "hadith", "tafsir"}, "no Islamic subject in the data")

    def test_coverage_of_the_saudi_curriculum(self):
        res = art_coverage.measure(art_coverage.saudi_concepts())
        n = sum(len(r["names"]) for r in res.values())
        own = sum(r["own"] for r in res.values())
        self.assertGreaterEqual(own / n, 0.65, "most concepts have a drawing of their own (it was 17% before this batch)")
        for sk, r in res.items():
            self.assertGreaterEqual(r["own"] / len(r["names"]), 0.40, f"{sk}: at least 40%")

    def test_one_concept_one_drawing_the_alias_table(self):
        self.assertEqual(icon("البناء الضوئي", "science"), icon("التمثيل الضوئي", "science"), "two names, the same drawing")
        self.assertEqual(icon("الجذور", "science"), "🫚", "the page's old root drawing, not a new one")
        self.assertEqual(icon("المحيط", "math"), "⭕", "in maths «المحيط» is a perimeter…")
        self.assertEqual(icon("المحيط", "science"), "🌊", "…in science it is an ocean")

    def test_the_longest_word_wins_old_or_new(self):
        self.assertEqual(icon("معادلة الخط المستقيم", "math"), "sec:lineq", "the old precise phrase beats the new short word")
        self.assertEqual(icon("الطاقة المتجددة", "science"), "lib:mat.renewable", "«الطاقة المتجددة» before «الطاقة»")
        self.assertEqual(icon("الكتابة", "arabic"), "lib:lang.writing", "Arabic «الكتابة» is writing, not hieroglyphs")

    def test_no_word_is_found_inside_another(self):
        for name, subject, wrong in (("بطاقة الائتمان", "finance", "lib:mat.energy2"), ("لبنات الاستشعار", "digital", "lib:en.milk"),
                                     ("المواطنة", "social studies", "lib:sci.habitat"), ("السيولة", "finance", "lib:earth.flood"),
                                     ("الملف اللولبي", "physics", "lib:mat.ramp"), ("دول المحور", "social studies", "lib:earth.orbit")):
            self.assertNotEqual(icon(name, subject), wrong, name)
        self.assertEqual(icon("حبة اللقاح", "science"), "🐝", "pollen (لقاح) is not a vaccine here")

    def test_never_a_cartoon_for_what_must_be_respected(self):
        for name in ("الشعار الوطني (السيفان والنخلة)", "عمارة الحرمين الشريفين", "الملك عبدالعزيز", "الإمام محمد بن سعود", "السيرة النبوية", "العلم الوطني"):
            self.assertTrue(icon(name, "social studies").startswith("subj:"), f"{name}: the subject's character with its name, no drawing")

    def test_each_book_carries_only_its_drawings(self):
        got = art_library.for_book(["lib:sci.volcano", "lib:sci.volcano~2", "lib:earth.volcano", "🫚", "lib:nope.none"])
        self.assertEqual(sorted(got), ["earth.volcano"], "only real library drawings, a variant is the same drawing")
        self.assertEqual(set(got["earth.volcano"]), {"body", "face", "anim"})

    def test_two_concepts_of_one_lesson_never_look_the_same(self):
        g = {"book": {"id": "t", "title": "تجربة", "subject": "science", "grade": 4}, "nodes": [
            {"id": "u", "book_id": "t", "title": "و", "level": "unit"}, {"id": "tp", "book_id": "t", "title": "م", "level": "topic"},
            {"id": "l", "book_id": "t", "title": "القياس", "level": "lesson"},
            {"id": "m", "book_id": "t", "title": "الكتلة", "learning_objective": "مقدار ما في الجسم من مادة.", "level": "entity"},
            {"id": "w", "book_id": "t", "title": "الوزن", "learning_objective": "قوة جذب الأرض للجسم.", "level": "entity"}],
             "relationships": [{"id": "1", "source_node_id": "tp", "target_node_id": "u", "type": "subsetOf"}, {"id": "2", "source_node_id": "l", "target_node_id": "tp", "type": "subsetOf"},
                               {"id": "3", "source_node_id": "m", "target_node_id": "l", "type": "subsetOf"}, {"id": "4", "source_node_id": "w", "target_node_id": "l", "type": "subsetOf"},
                               {"id": "5", "source_node_id": "m", "target_node_id": "w", "type": "prerequisiteOf"}]}
        with tempfile.TemporaryDirectory() as d:
            p = os.path.join(d, "g.json")
            with open(p, "w", encoding="utf-8") as fh:
                json.dump(g, fh, ensure_ascii=False)
            G = Graph.load(p)
            ics = eg._icons(G, G.lessons()[0])
        self.assertEqual(ics["m"], "lib:mat.mass")
        self.assertEqual(ics["w"], "lib:mat.mass~2", "the same family → the second one in another colour")

    def test_the_saudi_demo_book(self):
        G = Graph.load(os.path.join(ROOT, "examples", "saudi_science_g4_demo.json"))
        ics = {c.text: og.icon_for(c.text, c.description, "science") for c in G.concepts.values() if og.is_entity(G, c.id)}
        self.assertTrue(all(not v.startswith("subj:") for v in ics.values()), ics)
        self.assertEqual(ics["البركان"] if "البركان" in ics else ics["الصهارة"], "lib:earth.volcano")
        self.assertEqual(ics["نواقل المرض"], "lib:sci.mosquito")


if __name__ == "__main__":
    unittest.main()
