"""🆕 batch 43 through the server: a book whose concept has only a WEAK picture (a word of its meaning) → the ONE model call
also shows the model that picture («now shows …») → it builds a better one, or says «keep» (saved: never asked again)."""
import copy
import json
import os
import re
import tempfile
import unittest

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("EXPLAIN_SEED", "0")
os.environ.setdefault("EXPLAIN_DATA_DIR", tempfile.mkdtemp())
import sys  # noqa: E402
sys.path.insert(0, HERE)
from core import service  # noqa: E402
import lego  # noqa: E402
import offline_generator as og  # noqa: E402

COMPUTER = os.path.join(os.path.dirname(HERE), "02_question_factory", "examples", "new_subject_computer_g7.json")
WEAK = ("الكركبة", "خليط فيه الماء والسكر")          # its NAME has no drawing; only «الماء» of its meaning → the water drop
NONE = ["الكركم", "الزعفران", "التخمير", "الشوي", "القرفة", "الهيل", "التحمير", "السمسم"]


def book(book_id):
    g = copy.deepcopy(json.load(open(COMPUTER, encoding="utf-8")))
    g["book"].update({"id": book_id, "title": "الطبخ · تجربة", "subject": "الطبخ"})
    ents = [n for n in g["nodes"] if n.get("level") == "entity"]
    for n, t in zip(ents, [WEAK[0]] + NONE):
        n["title"] = t
        n["learning_objective"] = WEAK[1] if t == WEAK[0] else "شي بنحضّره بالمطبخ"
    ids = {n["id"] for n in ents}
    g["node_content"] = [c for c in g.get("node_content", []) if c.get("node_id") not in ids]   # the meaning = the objective above
    return g


class Model:
    def __init__(self, keep):
        self.keep, self.prompts = keep, []

    def __call__(self, system, user):
        if "BUILD each picture" not in user:
            return ""
        self.prompts.append(user)
        names = re.findall(r"^  (.+?) — ", user, re.M)
        return json.dumps({"items": [({"name": n, "keep": True} if (self.keep and n == WEAK[0]) else
                                      {"name": n, "metaphor": "طنجرة", "options": [{"main": "pot"}]}) for n in names]}, ensure_ascii=False)


class TestWeakPicturesThroughTheServer(unittest.TestCase):
    def setUp(self):
        self.store = tempfile.mktemp(suffix=".json")
        lego.set_store(self.store)

    def tearDown(self):
        for b in ("weak_a", "weak_b"):
            try:
                service.delete_book(b)
            except Exception:
                pass
        if os.path.exists(self.store):
            os.remove(self.store)

    def test_the_weak_picture_is_shown_to_the_model_and_rebuilt(self):
        self.assertEqual(og.icon_source(*WEAK, "الطبخ")[1], "meaning")
        m = Model(keep=False)
        service.generate(graph=book("weak_a"), llm=m)
        self.assertEqual(len(m.prompts), 1)                                   # still ONE call for the whole book
        self.assertIn(f"{WEAK[0]}: now shows «💧»", m.prompts[0])
        self.assertEqual(og.icon_source(*WEAK, "الطبخ")[1], "lego")           # the built drawing wins now
        icons = {k: v for l in service.page_data(["weak_a"])["graphs"][0]["lessons"] for k, v in l["icons"].items()}
        self.assertTrue(icons and all(v.startswith("lego:pot:") for v in icons.values()), icons)

    def test_keep_then_no_second_call(self):
        m = Model(keep=True)
        service.generate(graph=book("weak_a"), llm=m)
        self.assertTrue(lego.kept(WEAK[0]))
        self.assertEqual(og.icon_source(*WEAK, "الطبخ"), ("💧", "meaning"))   # the model said it fits: it stays
        m2 = Model(keep=True)
        service.generate(graph=book("weak_b"), llm=m2)                         # another book with the same concepts
        self.assertEqual(m2.prompts, [])                                       # everything answered → no call, no cost
        lib = {e["name"]: e for e in service.lego_library()}
        self.assertEqual(lib[WEAK[0]]["status"], "keep")


if __name__ == "__main__":
    unittest.main()
