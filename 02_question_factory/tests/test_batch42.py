"""🆕 batch 42 (Hareth: «التكرار»): the same fact in other words, the lesson's parts in four ways that take turns, and the questions a
scene answers (for «ask a question → the scene»).
python -m unittest tests.test_batch42"""
import collections
import json
import os
import re
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
import build_all_books  # noqa: E402
import explain_generator as eg  # noqa: E402
import explain_parts as ep  # noqa: E402
import scene_questions as sq  # noqa: E402
import variety  # noqa: E402
from graph_reader import Graph  # noqa: E402

BOOKS = [Graph.load(os.path.join(ROOT, b)) for b in build_all_books.BOOKS]


class Variety(unittest.TestCase):
    def test_the_same_concept_always_gets_the_same_words(self):
        for key in variety.POOL:
            a = variety.say(key, "l1:x", me="الجذر", on="الساق", L="النبات", n=3)
            self.assertEqual(a, variety.say(key, "l1:x", me="الجذر", on="الساق", L="النبات", n=3), key)

    def test_concepts_get_different_words(self):
        forms = {variety.say("what_if.ask", f"l:{i}", me="س") for i in range(40)}
        self.assertEqual(len(forms), len(variety.POOL["what_if.ask"]), "every form is used")

    def test_the_old_sentence_is_still_one_of_them(self):
        self.assertIn("شو بيصير لو [اختفى|اختفت] «{me}»؟", variety.POOL["what_if.ask"])
        self.assertIn("اكبس على أي مفهوم، وشوف مين بيحتاج مين.", variety.POOL["overview.tap"])

    def test_the_verb_agrees(self):
        he = {variety.say("what_if.ask", f"s{i}", False, me="الجذر") for i in range(30)}
        she = {variety.say("what_if.ask", f"s{i}", True, me="الورقة") for i in range(30)}
        self.assertTrue(any("اختفى «الجذر»" in x for x in he) and any("اختفت «الورقة»" in x for x in she))
        self.assertFalse(any(re.search(r"[\[\]|{}]", x) for x in he | she), "no template mark is left")

    def test_the_twelve_books_say_it_in_more_than_one_way(self):
        lines = collections.Counter()
        for b in build_all_books.BOOKS:
            d = os.path.join(ROOT, build_all_books.out_dir(b) if hasattr(build_all_books, "out_dir") else "explain_out_" + b.replace("_book_graph.json", ""))
            for root, _, files in os.walk(os.path.join(d, "lessons")):
                for f in files:
                    r = json.load(open(os.path.join(root, f), encoding="utf-8"))
                    for c in r["concepts"]:
                        for s in c["scenes"]:
                            if s["kind"] == "what_if":
                                lines[re.sub(r"«[^»]*»", "X", s["steps"][0])] += 1
        self.assertGreaterEqual(len(lines), 3, lines)
        self.assertLess(max(lines.values()), sum(lines.values()), "it was ONE sentence 18 times")


class Parts(unittest.TestCase):
    def test_every_lesson_gets_a_parts_scene_and_the_kinds_take_turns(self):
        seen = collections.Counter()
        for g in BOOKS:
            kinds = [(ep.lesson_parts(g, l) or {}).get("kind") for l in g.lessons()]
            seen.update(k for k in kinds if k)
            for a, b in zip(kinds, kinds[1:]):
                if a and b and a != "assemble" and b != "assemble":
                    self.assertNotEqual(a, b, f"two lessons in a row with the same «parts» scene: {g.book.get('title')}")
        self.assertTrue({"assemble", "build_up", "missing", "tour"} <= set(seen), seen)

    def test_they_teach_only_what_the_graph_says(self):
        for g in BOOKS:
            for l in g.lessons():
                s = ep.lesson_parts(g, l)
                if s:
                    self.assertEqual(eg.check_scene(g, s), [], (g.book.get("title"), l.title, s["kind"]))

    def test_build_up_from_the_base(self):
        g = next(g for g in BOOKS if any((ep.scene_build_up(g, l) or {}).get("kind") for l in g.lessons()))
        s = next(ep.scene_build_up(g, l) for l in g.lessons() if ep.scene_build_up(g, l))
        self.assertEqual(s["levels"][s["order"][0]], 0, "the first part is a base part")
        self.assertEqual(len(s["steps"]), 3, "title · how to play («🖐️ دورك») · the end")

    def test_missing_the_right_card_is_there_once(self):
        for g in BOOKS:
            for l in g.lessons():
                s = ep.scene_missing(g, l)
                for r in (s or {}).get("rounds", []):
                    self.assertEqual(r["options"].count(r["id"]), 1)
                    self.assertEqual(len(set(r["options"])), len(r["options"]))
                    self.assertTrue(r["why"].endswith("."))

    def test_the_tour_has_a_step_per_part(self):
        for g in BOOKS:
            for l in g.lessons():
                s = ep.scene_tour(g, l)
                if s:
                    self.assertEqual(len(s["steps"]), len(s["concepts"]) + 1)
                    self.assertEqual(len(s["stops"]), len(s["concepts"]))
                    self.assertTrue(all(x.startswith("📍") for x in s["steps"][1:]))


class Questions(unittest.TestCase):
    def test_norm_and_words(self):
        self.assertEqual(sq.norm("النَّبتةُ بتحتاجُ الماءَ؟ 🍎"), "النبته بتحتاج الماء")
        self.assertEqual(sq.words("والجذور"), ["جذور"])

    def test_every_scene_kind_has_questions(self):
        g = BOOKS[0]
        for l in g.lessons():
            r = eg.explain_lesson(g, l)
            for s in [r["overview"], r.get("assemble")] + [s for c in r["concepts"] for s in c["scenes"]]:
                if s:
                    cid = s.get("target", "") if s["kind"] not in ("overview", "assemble", "build_up", "missing", "tour", "world") else ""
                    self.assertTrue(sq.questions(g, l.title, cid, s), s["kind"])

    def test_close_spellings_are_close(self):
        self.assertGreater(sq.cosine(sq.trigrams("شو بيحتاج التلقيح"), sq.trigrams("شو بيحتاج التلقيح؟")), 0.95)
        self.assertLess(sq.cosine(sq.trigrams("المنسف", content=True), sq.trigrams("التلقيح", content=True)), 0.2)


if __name__ == "__main__":
    unittest.main()
