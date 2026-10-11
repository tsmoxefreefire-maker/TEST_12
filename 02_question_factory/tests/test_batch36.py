"""🆕 batch 36 — the activities ask the student to DECIDE (Hareth: «في فعاليات بتحس إنك بس بتلمس وتحط»).
The new wrong choices must be TRUE «wrong» ones (the picture must never teach something false):
  · 🍽️ recipe: the food that is not his (decoys) — he really does not need it, not even through a chain;
  · 🪜 ladder: every wrong rung is not linked the asked way to the rung above;
  · 🧭 journey: every wrong next station does not need the station before (not even through a chain);
  · and the old checks still catch a lie (a decoy that IS needed is reported)."""
import os
import unittest

import audience as A
import explain_activities as act
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


def scenes(kind):
    for name in BOOKS:
        g, recs = book(name)
        for rec in recs:
            for c in rec["concepts"]:
                for s in c["scenes"]:
                    if s["kind"] == kind:
                        yield name, g, s


class TestChoices(unittest.TestCase):
    def test_recipe_has_food_that_is_not_his(self):
        seen = [s for _, _, s in scenes("recipe")]
        self.assertTrue(seen)
        import offline_generator as og
        for name, g, s in scenes("recipe"):                                   # a decoy whenever the book has one (a tiny book can need everything)
            free = [x for x in g.concepts if og.is_entity(g, x) and x != s["target"] and x not in g.ancestors(s["target"])]
            self.assertTrue(s.get("decoys") or not free, (name, s["target"], "has no decoy although", free[:3]))
        for name, g, s in scenes("recipe"):
            for d in s.get("decoys", []):
                self.assertNotIn(d["id"], g.ancestors(s["target"]), (name, s["target"], d["id"]))
                self.assertIn("ما ", d["why"])

    def test_ladder_wrong_rungs_are_really_wrong(self):
        n = 0
        for name, g, s in scenes("ladder"):
            prev = s["target"]
            for r in s["rungs"]:
                for w in r.get("wrong", []):
                    n += 1
                    if s["mode"] == "why":
                        self.assertNotIn(w["id"], g.ancestors(prev), (name, prev, w["id"]))
                    else:
                        self.assertNotIn(w["id"], g.descendants(prev), (name, prev, w["id"]))
                    self.assertNotIn(w["id"], [s["target"]] + [x["id"] for x in s["rungs"]])
                prev = r["id"]
        self.assertGreater(n, 5, "most rungs are a real choice")

    def test_journey_wrong_stations_are_really_wrong(self):
        n = 0
        for name, g, s in scenes("journey"):
            for prev, st in zip(s["route"], s["stops"][1:]):
                for w in st.get("wrong", []):
                    n += 1
                    self.assertNotIn(w["id"], g.descendants(prev), (name, prev, w["id"]))
                    self.assertNotIn(w["id"], s["route"])
        self.assertGreater(n, 10, "most stations are a real choice")

    def test_every_new_scene_passes_the_graph_check(self):
        for kind in ("recipe", "ladder", "journey"):
            for name, g, s in scenes(kind):
                self.assertEqual(eg.check_scene(g, s), [], (name, kind, s["target"]))

    def test_the_check_catches_a_lying_decoy(self):
        name, g, s = next(scenes("recipe"))
        bad = dict(s, decoys=[{"id": s["needs"][0]["id"], "why": "x"}])
        self.assertTrue(act.check(g, bad))

    def test_the_little_ones_get_food_words_the_big_ones_do_not(self):
        for name, g, s in scenes("recipe"):
            first = s["steps"][0]
            if A.stage(g) in ("kids", "junior"):
                self.assertIn("🍽️", first)
            else:
                self.assertTrue("جهّز شروط" in first and "جوعان" not in " ".join(s["steps"]), (name, first))


if __name__ == "__main__":
    unittest.main()
