"""🆕 batch 42 · ASK A QUESTION → THE SCENE, AT ONCE (the engineer's idea: the scenes «created offline» before production, in a database with a description column and a JSON column,
reached by a «similarity measure». He did not say WHO asks: most likely the AI Tutor, when it needs to show something).

BEFORE (index_book, when a book is made — never while a student waits):
    every scene of every lesson → one row: the questions it answers + its words (description), its JSON, its concept (the graph's
    node id: the key the whole platform shares: the RAG, the AI Tutor…), its stage and grade — and, if a meaning model is set,
    its meaning-numbers. A row that did not change keeps its numbers (no second cost).
WHEN HE ASKS (ask):
    1. the NAME: a concept's name is inside the question («شو بيحتاج التلقيح؟» → «التلقيح») — instant, free, never wrong;
    2. the MEANING (if a model is set): the closest description by meaning («ليش الوردة بتصير تفاحة؟» → the pollination film);
    3. the SPELLING: the closest description by its letters (no model: free);
    🆕 batch 43 (Hareth: «لازم يسأل عن مشهد في نفس الكتاب، إذا برّا لازم نمنعه»): ALWAYS inside HIS book (book_id is required), his
    current lesson first; a question outside his book → no scene, and he is sent BACK to the concept he is studying (the plan,
    AI Tutor p.19: «أقدر أساعدك في موضوع الدرس، لكن خلينا نرجع للنقطة اللي بنذاكرها»).
    The answer: the concept's scenes in order (the cartoon first) + which one answers best + a link that opens the page right there.
Only the asked book's rows are held in memory (a few books at a time): the whole Saudi curriculum never sits in the server's memory.
A book whose rows are missing (a new database, a new version of the questions) is indexed on the spot, then saved."""
import collections
import os
import sys
import threading
import time

from core import db, embed, settings, storage

sys.path.insert(0, settings.FACTORY_DIR)
import scene_questions as sq  # noqa: E402
from graph_reader import Graph  # noqa: E402

TEXT_MIN = 0.30                     # the spelling search: below this the closest is not close enough
MAX_BOOKS = 24                      # 🆕 batch 43: how many books' rows stay in memory (the least recently asked one leaves first)
LESSON_FIRST = 0.05                 # 🆕 batch 43: his current lesson comes first when two scenes answer as well
_LOCK = threading.RLock()
_C = {"books": collections.OrderedDict(), "model": None}             # book_id → its rows, their trigrams, names and meaning-numbers


# ---------- BEFORE: the rows of a book ----------
def _graph(book_id: str):
    p = os.path.join(settings.GRAPHS_DIR, f"{book_id}.json")
    return Graph.load(p) if os.path.exists(p) else None


def _ver(scene: dict, qs: list) -> str:
    import hashlib, json
    return sq.VERSION + ":" + hashlib.sha1(json.dumps([scene, qs], ensure_ascii=False, sort_keys=True).encode()).hexdigest()[:16]


def rows_for_book(book_id: str) -> list:
    """[(row, scene)] for every scene of the book (lesson scenes too: the big picture, the puzzle)."""
    meta, g = storage.book_meta(book_id), _graph(book_id)
    if meta is None or g is None:
        return []
    out = []
    for lid in storage.lesson_ids(book_id):
        rec = storage.load_lesson(book_id, lid)
        if not rec:
            continue
        aud = rec.get("audience") or {}
        base = {"book_id": book_id, "lesson_id": lid, "lesson_title": rec.get("lesson_title", ""), "stage": aud.get("stage") or meta.get("stage"),
                "grade": _int(meta.get("grade")), "subject": str(meta.get("subject") or ""), "source": "factory", "approved": True}
        todo = [("", i, s) for i, s in enumerate(x for x in (rec.get("overview"), rec.get("world"), rec.get("assemble")) if x)]
        extra = _approved_llm(book_id, lid)                           # a scene the model wrote AND a teacher approved: found like the others
        for c in rec.get("concepts", []):
            mine = c.get("scenes", []) + extra.get(c["concept_id"], [])
            todo += [(c["concept_id"], i, s) for i, s in enumerate(mine)]
        for cid, i, s in todo:
            qs = sq.questions(g, base["lesson_title"], cid, s)
            name = g.concepts[cid].text if cid in g.concepts else base["lesson_title"]
            row = dict(base, id=f"{book_id}:{lid}:{cid or '_'}:{i}", concept_id=cid, position=i, kind=s.get("kind", ""), name=name,
                       questions=qs, description=sq.description(g, base["lesson_title"], cid, s, qs))
            if s.get("source") == "llm":
                row["source"] = "llm"
            row["version"] = _ver(s, qs)
            out.append((row, s))
    return out


def _approved_llm(book_id, lesson_id) -> dict:
    try:
        from core import llm_scenes
        return llm_scenes.approved_for_lesson(book_id, lesson_id)
    except Exception:                                                     # (the model part is optional)
        return {}


def _int(x):
    try:
        return int(x)
    except (TypeError, ValueError):
        return None


def index_book(book_id: str) -> dict:
    """make / refresh the rows of ONE book (only the changed ones are written and given meaning-numbers)."""
    store = db.scenes()
    t0 = time.time()
    pairs = rows_for_book(book_id)
    old = store.versions(book_id)                                     # id → (version, the model of its numbers)
    new_ids = {r["id"] for r, _ in pairs}
    store.delete([i for i in old if i not in new_ids])
    changed = [(r, s) for r, s in pairs if old.get(r["id"], (None, None))[0] != r["version"]]
    if changed:
        store.upsert_many(changed)                                    # (a changed row loses its old numbers)
    model = embed.model_name()
    changed_ids = {r["id"] for r, _ in changed}
    need = [r for r, _ in pairs if model and (r["id"] in changed_ids or old.get(r["id"], (None, None))[1] != model)]
    embedded = 0
    if need:
        vecs = embed.embed([r["description"] for r in need], "document") or []
        store.set_embs([(r["id"], v, model) for r, v in zip(need, vecs)])
        embedded = len(vecs)
    forget(book_id)                                                   # the next question reloads this book's rows
    return {"book_id": book_id, "rows": len(pairs), "written": len(changed), "removed": len(old.keys() - new_ids),
            "embedded": embedded, "model": model or None, "ms": round((time.time() - t0) * 1000)}


def index_all() -> list:
    return [index_book(m["book_id"]) for m in storage.list_books()]


def drop_book(book_id: str) -> None:
    db.scenes().delete_book(book_id)
    forget(book_id)


def forget(book_id: str = None) -> None:
    """drop a book's rows from memory (or every book's): the next question reads them again."""
    with _LOCK:
        if book_id is None:
            _C["books"].clear()
        else:
            _C["books"].pop(book_id, None)


# ---------- the rows in memory: ONE book at a time (refreshed only when that book changed) ----------
def _load(book_id: str) -> dict:
    """{rows, tri, qtri, names, mat, ids} of one book."""
    store = db.scenes()
    st = store.book_stamp(book_id)
    model = embed.model_name()
    with _LOCK:
        if model != _C["model"]:                                          # another meaning model: every book's numbers change
            _C["books"].clear()
            _C["model"] = model
        B = _C["books"].get(book_id)
        if B is not None and B["stamp"] == st:
            _C["books"].move_to_end(book_id)
            return B
        rows = store.book_rows(book_id)
        B = {"stamp": st, "rows": rows, "tri": [sq.trigrams(r["description"], content=True) for r in rows],
             "qtri": [[sq.trigrams(x) for x in r["questions"]] for r in rows], "names": {}}
        for i, r in enumerate(rows):
            if r["concept_id"]:
                B["names"].setdefault(r["name"], []).append(i)                 # one name → its rows (a name is checked once per question)
        vec = [(i, r["emb"]) for i, r in enumerate(rows) if r.get("emb") and r.get("emb_model") == model]
        try:
            import numpy as np
            B["mat"] = np.array([v for _, v in vec], dtype="float32") if vec else None
        except ImportError:                                               # (no numpy: plain Python, slower but the same)
            B["mat"] = [v for _, v in vec] if vec else None
        B["ids"] = [i for i, _ in vec]
        _C["books"][book_id] = B
        while len(_C["books"]) > MAX_BOOKS:
            _C["books"].popitem(last=False)
        return B


def _by_name(B, question, ok):
    """the rows of every concept whose NAME is inside the question («الفرق بين الجذر والساق» → الجذر and الساق) → {row: penalty};
    a long name half there («بدها شمس» → «ضوء الشمس») joins too, a bit behind (−0.2)."""
    whole, half = [], []
    for name, idx in B["names"].items():
        if not any(i in ok for i in idx):
            continue
        if sq.name_in(name, question):
            whole.append(name)
        elif len(sq.words(name)) >= 2 and sq.name_share(name, question) >= 0.5:
            half.append(name)
    whole = [n for n in whole if not any(m != n and len(sq.words(m)) > len(sq.words(n)) and sq.name_in(n, m) for m in whole)]
    out = {}                                                              # («الجملة الاسمية» said → not «الجملة» too: the longer name wins)
    for names, pen in ((half, 0.2), (whole, 0.0)):
        for n in names:
            out.update({i: pen for i in B["names"][n] if i in ok})
    return out


def _qscore(B, q, i) -> float:
    """how close his question is to the CLOSEST of the scene's questions."""
    return max((sq.cosine(q, t) for t in B["qtri"][i]), default=0.0)


def _pick_scene(B, question, rows_i, pen=None, lesson_id=None):
    """among these rows: the scene whose questions are closest to his (what / why / how / the difference…), and — when he names
    TWO concepts («الفرق بين الجذر والساق») — a scene that shows both of them; a tie → the longer name, then the first scene (the cartoon)."""
    q = sq.trigrams(question)
    R, pen = B["rows"], pen or {}
    names = {R[i]["name"] for i in rows_i if not pen.get(i)}                     # the names he really said (whole)
    every = {R[i]["name"] for i in rows_i}
    first = min(every, key=lambda n: (sq.name_at(n, question), -len(n), n)) if len(every) > 1 else None   # the one he says FIRST is usually the topic (a tie: the longer name)
    pair = bool(sq.PAIR.search(sq.norm(question)))                                # «الفرق / الشبه / بين / قارن / العلاقة»: he asks about TWO
    both = lambda i: 0 if (pen.get(i) or not pair) else sum(1 for n in names if n != R[i]["name"] and sq.name_in(n, R[i]["description"]))
    here = lambda i: LESSON_FIRST if lesson_id and R[i]["lesson_id"] == lesson_id else 0.0     # 🆕 batch 43: his lesson first
    score = lambda i: _qscore(B, q, i) + 0.25 * both(i) + (0.1 if R[i]["name"] == first else 0.0) + here(i) - pen.get(i, 0.0)
    return max(rows_i, key=lambda i: (round(score(i), 3), len(R[i]["name"]), -R[i]["position"]))


def _by_meaning(B, question, ok):
    if B["mat"] is None or not ok:
        return None, 0.0
    q = embed.query(question)
    if q is None:
        return None, 0.0
    try:
        import numpy as np
        sims = B["mat"] @ np.array(q, dtype="float32")
        order = [int(k) for k in np.argsort(-sims)]
        sims = [float(x) for x in sims]
    except ImportError:
        sims = [sum(a * b for a, b in zip(v, q)) for v in B["mat"]]
        order = sorted(range(len(sims)), key=lambda k: -sims[k])
    for k in order:
        if B["ids"][k] in ok:
            return B["ids"][k], sims[k]
    return None, 0.0


def _by_text(B, question, ok):
    """the closest description by the letters of the words that NAME things (the asking words do not count here)."""
    q = sq.trigrams(question, content=True)
    best, score = None, 0.0
    for i in sorted(ok):
        sc = sq.cosine(q, B["tri"][i])
        if B["rows"][i]["concept_id"] and len(sq.words(B["rows"][i]["name"])) >= 2:
            sc += 0.3 * sq.name_share(B["rows"][i]["name"], question)        # part of a long name is there («شمس» → «ضوء الشمس»)
        if sc > score:
            best, score = i, sc
    return best, score


def ask(question: str, book_id: str = None, grade=None, stage: str = None, lesson_id: str = None, concept_id: str = None) -> dict:
    """a question → the scenes that answer it, INSIDE his book (see the top of this file).
    lesson_id / concept_id = where he is now (optional): his lesson comes first, and a question outside his book sends him back there.
    (grade / stage are kept for old callers: the book already is his grade.)"""
    t0 = time.time()
    question = (question or "").strip()
    if not question:
        return {"found": False, "reason": "empty", "ms": 0}
    if not book_id:
        return {"found": False, "reason": "no_book", "message": "لازم نعرف كتاب الطالب: البحث بيكون جوا كتابه بس.", "ms": 0}
    B = _load(book_id)
    if not B["rows"] and storage.book_meta(book_id) is not None:
        index_book(book_id)                                               # his book has no rows yet: build them now, keep them
        B = _load(book_id)
    with _LOCK:
        rows = B["rows"]
        if lesson_id is None and concept_id:                              # (only the concept given: its lesson is his lesson)
            lesson_id = next((r["lesson_id"] for r in rows if r["concept_id"] == concept_id), None)
        ok = set(range(len(rows)))
        how, i, score = None, None, 0.0
        named = _by_name(B, question, ok)
        if named:
            how, i = "name", _pick_scene(B, question, list(named), named, lesson_id)
            score = round(1.0 - named[i], 3)
            j, sc = _by_meaning(B, question, ok)                          # a meaning model (if set) that CLEARLY points elsewhere wins:
            if j is not None and rows[j]["concept_id"] != rows[i]["concept_id"] and sc >= embed.min_score() + 0.12 and j not in named:
                how, i, score = "meaning", j, sc                          # the name in a question is not always its topic
        else:
            j, sc = _by_meaning(B, question, ok)
            if j is not None and sc >= embed.min_score():
                how, i, score = "meaning", j, sc
            else:
                j, sc = _by_text(B, question, ok)
                if j is not None and sc >= TEXT_MIN:
                    how, i, score = "text", j, sc
        if i is None:
            return dict(_outside(B, question, lesson_id, concept_id), ms=round((time.time() - t0) * 1000, 1))
        hit = rows[i]
        same = [k for k in ok if rows[k]["lesson_id"] == hit["lesson_id"] and rows[k]["concept_id"] == hit["concept_id"]]
        same.sort(key=lambda k: rows[k]["position"])
        start = i if how == "name" else _pick_scene(B, question, same)   # (by meaning / spelling: the concept is found; then its best scene)
    scenes = db.scenes().scenes([rows[k]["id"] for k in same])
    from core import art
    out = {"found": True, "how": how, "score": round(score, 3), "book_id": hit["book_id"], "lesson_id": hit["lesson_id"], "lesson_title": hit["lesson_title"],
           "concept_id": hit["concept_id"], "name": hit["name"], "stage": hit["stage"], "grade": hit["grade"],
           "in_his_lesson": bool(lesson_id) and hit["lesson_id"] == lesson_id,
           "start": same.index(start), "scenes": [dict(scenes.get(rows[k]["id"], {}), _row=rows[k]["id"]) for k in same],
           "matched_question": _closest_question(question, rows[start]["questions"]),
           "page_url": _page_url(hit, rows[start])}
    rec = storage.load_lesson(hit["book_id"], hit["lesson_id"]) or {}
    out["art"] = art.art_url(rec.get("icons", {}).get(hit["concept_id"])) if hit["concept_id"] else None
    out["ms"] = round((time.time() - t0) * 1000, 1)
    return out


def _outside(B, question, lesson_id, concept_id) -> dict:
    """🆕 batch 43: nothing in HIS book answers it → no scene (never one from another book), and back to what he is studying."""
    rows = B["rows"]
    mine = [k for k, r in enumerate(rows) if concept_id and r["concept_id"] == concept_id and (not lesson_id or r["lesson_id"] == lesson_id)]
    if not mine and lesson_id:
        mine = [k for k, r in enumerate(rows) if r["lesson_id"] == lesson_id and not r["concept_id"]]      # the lesson's start (the big picture)
    back = None
    if mine:
        k = min(mine, key=lambda k: rows[k]["position"])
        r = rows[k]
        back = {"lesson_id": r["lesson_id"], "concept_id": r["concept_id"], "name": r["name"] if r["concept_id"] else r["lesson_title"],
                "page_url": _page_url(r, r)}
    if back:
        msg = f"هاد مش من درسنا. أقدر أساعدك بموضوع الدرس، خلينا نرجع لـ«{back['name']}»."
        near = [r["name"] for r in rows if r["lesson_id"] == back["lesson_id"] and r["concept_id"] and r["position"] == 0 and r["name"] != back["name"]]
    else:
        msg = "هاد مش من كتابك. أقدر أساعدك بمواضيع كتابك: جرّب تسأل عن وحدة منها."
        qc, near = sq.trigrams(question, content=True), []
        for k in sorted(range(len(rows)), key=lambda k: (-sq.cosine(qc, B["tri"][k]), k)):
            if rows[k]["concept_id"] and rows[k]["name"] not in near:
                near.append(rows[k]["name"])
            if len(near) == 4:
                break
    return {"found": False, "reason": "outside", "message": msg, "back": back, "suggestions": list(dict.fromkeys(near))[:4]}


def _page_url(hit, row) -> str:
    """/explain/<book>?lesson=…&concept=…&at=…&kind=… : the page opens right at this scene (explain.js reads it)."""
    from urllib.parse import urlencode
    q = {"lesson": hit["lesson_id"]}
    if hit["concept_id"]:
        q["concept"] = hit["concept_id"]
    q.update(at=row["position"], kind=row["kind"])
    return f"/explain/{hit['book_id']}?" + urlencode(q)


def _closest_question(question, qs):
    q = sq.trigrams(question)
    return max(qs, key=lambda x: sq.cosine(q, sq.trigrams(x))) if qs else ""


def status() -> dict:
    model = embed.model_name()
    c = db.scenes().counts(model)
    return {"where": db.where(), "rows": c["rows"], "books": c["books"], "embed_provider": embed.provider(),
            "embedded_rows": c["embedded"], "questions_version": sq.VERSION, "books_in_memory": len(_C["books"])}
