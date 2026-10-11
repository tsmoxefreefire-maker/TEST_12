"""🆕 batch 42 · THE LESSON'S PARTS, THREE NEW WAYS (Hareth: «مشهد أجزاء النبات… يصير في مشهد ثاني غيره، بس الهدف إنه يوصل المعلومة»).

A lesson's concepts are the PARTS of one whole (the plant's parts, the cell's parts, the parts of a sentence…), joined by «needs».
Until now every lesson showed them ONE way: 🧩 the puzzle (assemble). Now the lesson's «parts» scene takes turns, lesson after lesson
(the next lesson never repeats the one before), and each says the same thing — what the parts are and which needs which:
    🧩 assemble   · drag each part to its shadow (the old one)
    🌱 build_up   · build it from the ground up: tap the part that comes NOW (a part sits only on what it needs)
    ❓ missing    · the whole picture with a hole: which part is missing? (the parts that need it are sad until it is back)
    🎥 tour       · the camera walks up from the base, part by part (a film to watch, not a game)
Plain Python from the graph, no AI. The page draws them (03_explain_player_src/parts42.js)."""
import random

import explain_generator as eg
import offline_generator as og

TURNS = ("assemble", "build_up", "missing", "tour")


def _base(g, lesson):
    ids = [c.id for c in lesson.concepts]
    if len(ids) < 3:
        return None
    edges = [[a, b] for a in ids for b in g.prereq_out.get(a, []) if b in ids]
    if not edges:
        return None
    level = {c: g.depth(c) for c in ids}
    low = min(level.values())
    levels = {c: level[c] - low for c in ids}
    says = {c: (og.fragments(g.concepts[c].description) or [g.concepts[c].description.strip(" .")])[0] for c in ids}
    order = sorted(ids, key=lambda c: (levels[c], ids.index(c)))         # from the base up
    return ids, edges, levels, says, order


def scene_build_up(g, lesson):
    """🌱 the base first, then what sits on it: he taps the part that can come NOW (everything it needs is already there)."""
    b = _base(g, lesson)
    if not b or len(set(b[2].values())) < 2:
        return None
    ids, edges, levels, says, order = b
    L = lesson.title
    return {"kind": "build_up", "concepts": ids, "edges": edges, "levels": levels, "says": says, "order": order,
            "steps": [f"🌱 ابني «{L}» من تحت لفوق!",
                      "اكبس على الجزء اللي بييجي هلأ: كل جزء بيقعد فوق اللي بيحتاجه.",
                      "طابق فوق طابق… لحد ما تكتمل الصورة."],
            "paragraph": f"بـ«{L}» في أجزاء هي الأساس ({eg._join([eg._name(g, c) for c in order if levels[c] == 0][:3])})، "
                         f"وفي أجزاء بتقعد فوقها لأنها بتحتاجها. ما في جزء بيقعد بالهوا."}


def scene_missing(g, lesson):
    """❓ the whole picture, one part missing: which is it? Two rounds (a part in the middle first: it has the most to say)."""
    b = _base(g, lesson)
    if not b:
        return None
    ids, edges, levels, says, order = b
    ins = {c: [a for a, x in edges if x == c] for c in ids}
    outs = {c: [x for a, x in edges if a == c] for c in ids}
    cands = sorted([c for c in ids if outs[c]], key=lambda c: (-(bool(ins[c]) and bool(outs[c])), -len(outs[c]), ids.index(c)))
    if not cands:
        return None
    rng = random.Random(f"missing:{lesson.id}")
    rounds = []
    for c in cands[:2]:
        others = [x for x in ids if x != c]
        rng.shuffle(others)
        name = eg._name(g, c)
        why = []
        if ins[c]:
            why.append(f"«{name}» {eg._v(name, 'بيحتاج', 'بتحتاج')} {eg._join([eg._name(g, a) for a in ins[c][:2]])}")
        need = [eg._name(g, x) for x in outs[c][:2]]
        why.append(f"{eg._join(need)} بيحتاجوا «{name}»" if len(need) > 1 else f"«{need[0]}» {eg._v(need[0], 'بيحتاج', 'بتحتاج')} «{name}»")
        rounds.append({"id": c, "options": [c] + others[:2], "say": says.get(c, ""), "why": "، و".join(why) + "."})
    L = lesson.title
    return {"kind": "missing", "concepts": ids, "edges": edges, "levels": levels, "says": says, "rounds": rounds,
            "steps": [f"❓ صورة «{L}» ناقصها جزء!",
                      "شوف مين زعلان، واختار من البطاقات الجزء الناقص.",
                      "لما يرجع، الأسهم بترجع تشتغل والكل بيفرح."],
            "paragraph": f"كل جزء بـ«{L}» إله مكان: لما يغيب، اللي بيحتاجه ما بيقدر يشتغل. "
                         + " ".join(r["why"] for r in rounds)}


def scene_tour(g, lesson):
    """🎥 a film: the camera starts at the base and climbs, one part per step (what it is · what it sits on)."""
    b = _base(g, lesson)
    if not b:
        return None
    ids, edges, levels, says, order = b
    steps, stops = [], []
    for c in order:
        name = eg._name(g, c)
        under = [eg._name(g, a) for a, x in edges if x == c]
        line = f"📍 «{name}»: {says.get(c, '')}".rstrip(": ") + "."
        if under:
            line += f" {eg._v(name, 'بيقعد', 'بتقعد')} فوق {eg._join(under[:2])}."
        else:
            line += f" {eg._v(name, 'هو', 'هي')} من الأساس."
        steps.append(line.replace("..", "."))
        stops.append({"id": c, "under": [a for a, x in edges if x == c]})
    L = lesson.title
    return {"kind": "tour", "concepts": ids, "edges": edges, "levels": levels, "says": says, "order": order, "stops": stops,
            "steps": [f"🎥 جولة بـ«{L}»: من الأساس لفوق."] + steps,
            "paragraph": f"جولة بأجزاء «{L}»: بلشنا من {eg._join([eg._name(g, c) for c in order if levels[c] == 0][:3])}، "
                         f"وطلعنا جزء جزء لحد {eg._name(g, order[-1])}."}


MAKERS = {"assemble": eg.scene_assemble, "build_up": scene_build_up, "missing": scene_missing, "tour": scene_tour}


def lesson_parts(g, lesson):
    """the lesson's «parts» scene: the lessons of a book take turns (the puzzle → build it up → what's missing → the tour → again;
    each book starts at its own place in the turn, so every kind shows up); a lesson that cannot have its turn's scene gets the puzzle."""
    ids = [l.id for l in g.lessons()]
    i = ids.index(lesson.id) if lesson.id in ids else 0
    start = sum(map(ord, str(g.book.get("id") or g.book.get("title") or ""))) % len(TURNS)   # each book starts at its own turn
    first = TURNS[(start + i) % len(TURNS)]
    for kind in (first, "assemble"):
        s = MAKERS[kind](g, lesson)
        if s:
            return s
    return None
