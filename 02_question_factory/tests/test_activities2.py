"""🆕 The 5 games (batch 34): throw · tower · magnet · machine · power — made from the graph only, true, spread over the books,
said the way each age talks, and never making a concept longer than before."""
import os
import unittest
from collections import Counter

import explain_activities2 as act2
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


def games(kind=None):
    for name in BOOKS:
        g, recs = book(name)
        for rec in recs:
            for c in rec["concepts"]:
                for s in c["scenes"]:
                    if s["kind"] in act2.KINDS and (kind is None or s["kind"] == kind):
                        yield name, g, rec, c, s


class TestGames(unittest.TestCase):
    def test_every_game_is_in_the_books(self):
        n = Counter(s["kind"] for *_, s in games())
        for k in act2.KINDS:
            self.assertGreaterEqual(n[k], 3, (k, n))      # batch 35: ~3 scenes per concept (the fact budget), so fewer of each

    def test_every_game_tells_the_truth(self):
        bad = [(name, s["kind"], e) for name, g, rec, c, s in games() for e in act2.check(g, s)]
        self.assertEqual(bad, [])

    def test_the_check_catches_a_lie(self):
        name, g, rec, c, s = next(games("throw"))
        lie = dict(s, balls=[dict(b, ok=not b["ok"]) for b in s["balls"]])
        self.assertTrue(act2.check(g, lie))
        name, g, rec, c, s = next(games("tower"))
        self.assertTrue(act2.check(g, dict(s, blocks=list(reversed(s["blocks"])))))

    def test_one_game_per_concept_at_most(self):
        for name in BOOKS:
            g, recs = book(name)
            for rec in recs:
                for c in rec["concepts"]:
                    self.assertLessEqual(sum(s["kind"] in act2.KINDS for s in c["scenes"]), 1, c["concept_id"])

    def test_a_concept_is_not_longer_than_before(self):
        """The game takes the place of one of the extra scenes: never more than 5 + the activity (6, 7 with a film)."""
        for name in BOOKS:
            g, recs = book(name)
            for rec in recs:
                for c in rec["concepts"]:
                    self.assertLessEqual(len(c["scenes"]), 7, (name, c["concept_id"], [s["kind"] for s in c["scenes"]]))

    def test_throw_and_magnet_have_both_sides(self):
        for kind, key in (("throw", "balls"), ("magnet", "items")):
            for *_, s in games(kind):
                oks = [b["ok"] for b in s[key]]
                self.assertTrue(any(oks) and not all(oks), s)

    def test_machine_gap_is_the_concept_with_a_neighbour_on_each_side(self):
        for *_, s in games("machine"):
            self.assertEqual(s["route"][s["gap"]], s["target"])
            self.assertTrue(0 < s["gap"] < len(s["route"]) - 1)
            self.assertEqual(sum(o["ok"] for o in s["options"]), 1)

    def test_power_lights_the_concept_with_its_real_sources(self):
        """Switching on every source except the decoy must light the concept (and the decoy alone never does)."""
        for *_, s in games("power"):
            ins = lambda x: [a for a, b in s["edges"] if b == x]
            def lit(on):
                now = set()
                for _ in s["nodes"]:
                    for x in s["nodes"]:
                        if (x in s["sources"] and x in on) or (x not in s["sources"] and ins(x) and all(a in now for a in ins(x))):
                            now.add(x)
                return now
            self.assertIn(s["target"], lit(set(s["sources"]) - {s["decoy"]}), s)
            if s["decoy"]:
                self.assertNotIn(s["target"], lit({s["decoy"]}), s)

    def test_the_big_ones_hear_their_words(self):
        for name, g, rec, c, s in games():
            if rec["audience"]["stage"] == "senior":
                text = " ".join(str(x) for x in s["steps"]) + " " + s.get("paragraph", "") + " " + s.get("win", "")
                self.assertNotIn("بيحتاج ", text, (name, s["kind"]))

    def test_tower_is_a_real_chain_ending_at_the_concept(self):
        for name, g, rec, c, s in games("tower"):
            ids = [b["id"] for b in s["blocks"]]
            self.assertEqual(ids[-1], s["target"])
            self.assertGreaterEqual(len(ids), 3)
            self.assertTrue(all(g.is_prereq(ids[i], ids[i + 1]) for i in range(len(ids) - 1)))


if __name__ == "__main__":
    unittest.main()
