"""🆕 batch 39 (Hareth): a place for every lesson, a little world for every concept, and the library of places that grows as DATA.
python -m unittest tests.test_batch39"""
import json
import os
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import place_library  # noqa: E402
import places_picker  # noqa: E402
from graph_reader import Graph  # noqa: E402

ROOT = os.path.dirname(HERE)


def book(name):
    return Graph.load(os.path.join(ROOT, name))


GOOD = {"id": "bakery", "label": "مخبز", "words": ["حلويات", "كعك"], "sky": ["#FFF6EC", "#FDEBD8"], "ground": ["#E9D3B6", "#D9BE98"],
        "far": "tiles", "farColor": "#EADFD2", "skyItems": ["sun"], "props": [["fridge", 0.07, 0, 1], ["potkit", 0.86, 0, 1, None, "still"]],
        "extras": [["chef", 0.2, 0, 0.9]]}


class FakeLesson:
    def __init__(self, title, concepts):
        self.title, self.concepts = title, concepts


class FakeConcept:
    def __init__(self, cid, text, description=""):
        self.id, self.text, self.description = cid, text, description


class FakeGraph:
    def __init__(self, subject, title):
        self.book = {"subject": subject, "title": title}


class Batch39(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.old = place_library.PATH
        place_library.PATH = os.path.join(self.tmp.name, "place_library.json")
        place_library._cache = None

    def tearDown(self):
        place_library.PATH = self.old
        place_library._cache = None
        self.tmp.cleanup()

    def test_lesson_places_from_words(self):
        got = {}
        for f in ("plants_book_graph.json", "sci_g8_book_graph.json", "phy_g6_book_graph.json", "history_book_graph.json", "math_book_graph.json"):
            g = book(f)
            for l in g.lessons():
                got[l.title] = places_picker.lesson_place(g, l)
        self.assertEqual(got["أجزاء النبات"], "garden")
        self.assertEqual(got["مكوّنات الخلية"], "lab")
        self.assertEqual(got["الخلية النباتية والحيوانية"], "lab", "a cell lesson stays in the lab even with «نباتية / حيوانية»")
        self.assertEqual(got["الطاقة والكهرباء"], "machine")
        self.assertEqual(got["الحياة حول النيل"], "desert")
        self.assertEqual(got["الجمع والطرح"], "classroom")

    def test_strange_subject_gets_a_fitting_place(self):
        g = FakeGraph("الطبخ", "الطبخ · الصف الخامس")
        l = FakeLesson("العجين", [FakeConcept("a", "الخميرة"), FakeConcept("b", "التخمير")])
        self.assertEqual(places_picker.lesson_place(g, l), "kitchen", "cooking → a kitchen, not a room")

    def test_concept_zones_and_whole_words(self):
        g = book("plants_book_graph.json")
        parts = next(l for l in g.lessons() if l.title == "أجزاء النبات")
        z = {g.concepts[k].text: v for k, v in places_picker.concept_zones(g, parts, "garden").items()}
        self.assertEqual(z.get("الجذر"), "underground")
        self.assertNotEqual(z.get("البذرة"), "atoms", "«البذرة» has «ذرة» inside, but it is not an atom (whole words only)")
        cell = next(l for l in book("sci_g8_book_graph.json").lessons() if l.title == "مكوّنات الخلية")
        g8 = book("sci_g8_book_graph.json")
        zz = {g8.concepts[k].text: v for k, v in places_picker.concept_zones(g8, cell, "lab").items()}
        self.assertEqual(zz.get("النواة"), "cell")
        self.assertNotIn("lab", zz.values(), "a zone equal to the lesson's place is dropped (it would change nothing)")

    def test_recipe_check(self):
        self.assertEqual(place_library.check(GOOD), [])
        for bad in ({**GOOD, "props": [["dragon", 0.1, 0, 1]]}, {**GOOD, "sky": ["red", "#FFFFFF"]}, {**GOOD, "props": [["tree", 1.4, 0, 1]]},
                    {**GOOD, "id": "Bad Id"}, {**GOOD, "extras": [["unicorn", 0.2]]}, {**GOOD, "props": [["tree", 0.1, 0, 9]]}, "not a dict"):
            self.assertTrue(place_library.check(bad), bad)

    def test_library_grows_as_data_and_wins_by_its_words(self):
        self.assertTrue(place_library.add(GOOD))
        place_library._cache = None
        self.assertIn("bakery", place_library.recipes(), "saved, read back")
        self.assertLess(len(json.dumps(GOOD, ensure_ascii=False).encode()), 600, "a place is a few hundred bytes of data, not code")
        g = FakeGraph("الطبخ", "الطبخ · الصف الخامس")
        l = FakeLesson("صناعة الحلويات والكعك", [FakeConcept("a", "السكر")])
        self.assertEqual(places_picker.lesson_place(g, l), "bakery", "a learned place wins when its own words match")
        self.assertFalse(place_library.add({**GOOD, "id": "broken", "props": [["dragon", 0.1]]}), "a bad recipe is never saved")

    def test_model_hook_one_checked_call(self):
        calls = []

        def fake(system, user):
            calls.append(user)
            return "here: " + json.dumps({**GOOD, "id": "candy_shop"}, ensure_ascii=False)
        r = place_library.ask_model(fake, "الطبخ", "الحلويات", ["السكر", "العجين"])
        self.assertEqual(r["id"], "candy_shop")
        self.assertEqual(len(calls), 1, "ONE call")
        self.assertIn("fridge", calls[0], "the model only gets OUR pieces to choose from")
        self.assertIsNone(place_library.ask_model(lambda s, u: "no json at all", "x", "y", []), "a bad answer → nothing saved")
        self.assertIsNone(place_library.ask_model(None, "x", "y", []), "no model (no keys) → nothing asked")


if __name__ == "__main__":
    unittest.main()
