"""🆕 batch 35: since the fact budget, a concept keeps ~3 scenes, and 🔍 lens · 🗣️ dialogue · 🎤 interview · 🎴 flip rarely come
(the cartoon already says what they said). They still exist (the API serves them, a graph can need them), so the browser checks
open them on THIS page: every book as usual + those four scenes added to every concept of the first book (the plants).
python tests_browser/extra_page.py  → prints the page's path"""
import os
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
FACTORY = os.path.dirname(HERE)
sys.path.insert(0, FACTORY); sys.path.insert(0, os.path.join(FACTORY, "player"))


def build(folder=None):
    import audience as A
    import build_all_books as bab
    import build_explain_player as bep
    import explain_generator as eg
    from graph_reader import Graph
    books = sorted(bab.BOOKS, key=bab.grade)
    graphs = []
    for i, gf in enumerate(books):
        gp, od = os.path.join(FACTORY, gf), os.path.join(FACTORY, bab.out_dir(gf))
        extra = None
        if i == 0:
            g = Graph.load(gp); extra = {}
            for l in g.lessons():
                for c in l.concepts:
                    more = [eg.scene_dialogue(g, l, c.id), eg.scene_lens(g, l, c.id), eg.scene_interview(g, l, c.id), eg.scene_flip(g, l, c.id)]
                    extra[(l.id, c.id)] = [A.voice_record(s, A.stage(g)) for s in more if s]
        graphs.append(bep.pack(gp, od, extra))
    folder = folder or tempfile.mkdtemp()
    path = os.path.join(folder, "explain_extra.html")
    open(path, "w", encoding="utf-8").write(bep.page_html(graphs))
    return path


if __name__ == "__main__":
    print(build())
