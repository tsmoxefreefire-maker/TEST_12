"""🆕 batch 35 — the FACT BUDGET (Hareth: «بتضل تعيد المعلومة كثير»): inside a concept a fact is taught, practised once, and that is it."""
import os
import statistics
import unittest

import explain_budget as budget
import explain_generator as eg
from graph_reader import Graph

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOOKS = ["plants", "math", "arabic_g4", "history", "geo_g5", "phy_g6", "chem_g7", "sci_g8", "math_g9", "phy_g10", "chem_g11", "bio_g12"]
_ALL = {}


def book(name):
    if name not in _ALL:
        g = Graph.load(os.path.join(HERE, name + "_book_graph.json"))
        _ALL[name] = (g, [eg.explain_lesson(g, l) for l in g.lessons()])
    return _ALL[name]


def concepts():
    for name in BOOKS:
        g, recs = book(name)
        for rec in recs:
            for c in rec["concepts"]:
                yield name, g, rec, c


class TestBudget(unittest.TestCase):
    def test_the_cartoon_still_opens_every_concept(self):
        self.assertTrue(all(c["scenes"][0]["kind"] == "meet" for *_, c in concepts()))

    def test_no_fact_is_said_more_than_twice_outside_a_chain(self):
        """learn (the cartoon) + practise once = twice. Only a chain may show a known link again, as the road to something new."""
        bad = []
        for name, g, rec, c in concepts():
            seen = {}
            for s in c["scenes"]:
                if s["kind"] in budget.CHAINS:
                    continue                                  # a chain passes known links on its way to new ones
                for f in budget.facts(g, s):
                    seen[f] = seen.get(f, 0) + 1
                    if seen[f] > 2:
                        bad.append((name, c["concept_id"], s["kind"], f))
        self.assertEqual(bad, [])

    def test_the_same_fact_is_repeated_far_less_than_before(self):
        """Before batch 35 the first «needs» of a concept was said in 5.4 scenes (of ~6). Now: learn + practise."""
        reps = []
        for name, g, rec, c in concepts():
            m = c["scenes"][0]
            if m.get("ins"):
                f = ("e", m["ins"][0], c["concept_id"])
                reps.append(sum(1 for s in c["scenes"] if f in budget.facts(g, s)))
        self.assertLessEqual(statistics.mean(reps), 2.6, statistics.mean(reps))

    def test_short_concepts(self):
        for name, g, rec, c in concepts():
            core = [s for s in c["scenes"] if s["kind"] not in budget.UNIQUE]
            self.assertLessEqual(len(core), budget.MAX_SCENES, (name, c["concept_id"], [s["kind"] for s in c["scenes"]]))

    def test_every_scene_after_the_cartoon_brings_something_new_or_is_the_practice(self):
        for name, g, rec, c in concepts():
            seen, practised = set(), False
            for s in c["scenes"]:
                f = budget.facts(g, s)
                new = [x for x in f if x not in seen]
                if s["kind"] != "meet" and not new:
                    if s["kind"] in budget.RECALL:                     # 🆕 batch 43: 🕵️/🧩 of a concept with few scenes finds its meaning again —
                        self.assertLessEqual(len(c["scenes"]), 3)     # only there, and only a second time (never a third)
                        self.assertTrue(all(sum(1 for t in c["scenes"][:c["scenes"].index(s)] if x in budget.facts(g, t)) < 2 for x in f), (name, c["concept_id"]))
                        continue
                    self.assertTrue(s["kind"] in budget.PRACTICE and not practised, (name, c["concept_id"], s["kind"]))
                if s["kind"] in budget.PRACTICE and s["kind"] != "meet":
                    practised = practised or not new
                seen |= f

    def test_a_chain_is_not_walked_twice_in_a_lesson(self):
        for name in BOOKS:
            g, recs = book(name)
            for rec in recs:
                walked = set()
                for c in rec["concepts"]:
                    for s in c["scenes"]:
                        if s["kind"] in budget.CHAINS:
                            f = budget.facts(g, s)
                            self.assertGreaterEqual(sum(1 for x in f if x not in walked) / len(f), 0.5, (name, rec["lesson_id"], s["kind"]))
                            walked |= f


if __name__ == "__main__":
    unittest.main()
