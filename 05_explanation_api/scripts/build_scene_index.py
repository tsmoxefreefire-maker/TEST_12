"""🆕 batch 42 · MAKE EVERYTHING BEFORE THE STUDENTS COME (the engineer: «نولّد قبل ما نطلع production»).

    python scripts/build_scene_index.py                      # every book on the server: its search rows (only the changed ones)
    python scripts/build_scene_index.py --graph my_book.json # a NEW graph: its explanations, then its rows
    python scripts/build_scene_index.py --samples            # the 12 sample books, then their rows
    python scripts/build_scene_index.py --book sci_g4 --ask "شو بيحتاج التلقيح؟"   # try one question (inside a book: 🆕 batch 43)

With DATABASE_URL set, everything goes into the database (and stays after a restart); without it, into data/.
With a meaning model (EMBED_PROVIDER / a key), the rows also get their meaning-numbers — once (a row that did not change keeps them)."""
import argparse
import json
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core import db, embed, service  # noqa: E402


def main(argv=None):
    ap = argparse.ArgumentParser(description="make the scenes' search rows BEFORE any student asks")
    ap.add_argument("--graph", action="append", default=[], help="a graph file to make first (can be repeated)")
    ap.add_argument("--samples", action="store_true", help="make the 12 sample books first")
    ap.add_argument("--book", action="append", default=[], help="only this book (can be repeated)")
    ap.add_argument("--ask", help="then try one question")
    a = ap.parse_args(argv)
    t0 = time.time()
    print(f"📦 where: {db.where()} · meaning model: {embed.provider()}")
    print(f"   restored from the database: {service.boot()['restored_files']} files")
    for g in a.graph:
        with open(g, encoding="utf-8") as f:
            r = service.generate(graph=json.load(f))
        print(f"   📘 {r['title']}: {len(r['lessons'])} lessons, {r['scenes']} scenes → {r['search']['rows']} rows")
    if a.samples:
        for r in service.seed_samples():
            print(f"   📘 {r['title']}: {r['search']['rows']} rows")
    out = []
    for b in (a.book or [None]):
        out += service.reindex(b)
    for r in out:
        print(f"   🔎 {r['book_id']}: {r['rows']} rows · {r['written']} written · {r['embedded']} with meaning-numbers · {r['ms']} ms")
    print(f"✅ {sum(r['rows'] for r in out)} scenes can be found by a question · {round(time.time() - t0, 1)} s")
    if a.ask:
        r = service.ask(a.ask, book_id=(a.book or [None])[0] or (service.list_books() or [{}])[0].get("book_id"))
        print(json.dumps({k: r.get(k) for k in ("found", "how", "name", "lesson_title", "matched_question", "page_url", "message", "back", "suggestions", "ms")}, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
