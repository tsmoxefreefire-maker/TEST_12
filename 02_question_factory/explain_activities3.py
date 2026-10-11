"""🆕 batch 43 (Hareth: «ممكن تزيد لي فعالية فعاليتين جداد») · TWO NEW ACTIVITIES, for the concepts that have FEW scenes
(the graph gives them few arrows, so the other games could not be made). They need only the concept's NAME and MEANING:

  who_am_i   🕵️ مين أنا؟      a hidden character gives clues (its meaning, what it needs, who needs it); the student picks it from 3 cards.
                               A wrong card says what THAT one really is, and opens one more clue.
  sentence   🧩 ركّب الجملة   the concept's meaning cut into 3–4 pieces, mixed up; the student taps them in order and the sentence is built.

Like every activity: they are the STUDENT's (the video waits for him, batch 41), no points, no failing — a wrong move = an explanation.
Plain Python, no AI. Truth rule: a clue is a piece of the concept's own meaning or one of its real arrows; a wrong card is never something
the clues also fit. check() re-checks both against the graph."""
import re

import audience as A
import explain_activities as a1
import explain_generator as eg
import offline_generator as og

N, V = a1.N, a1.V
_ins, _outs, _pieces, _short_def, _rng = a1._ins, a1._outs, a1._pieces, a1._short_def, a1._rng
KINDS = ("who_am_i", "sentence")
FEW = 2                    # a concept with this many scenes or fewer gets one of them (the cartoon + at most one more)
_SMALL = {"في", "من", "على", "إلى", "الى", "عن", "مع", "بين", "و", "أو", "ثم", "حتى", "التي", "الذي", "الذين", "اللي", "إن", "أن", "لا", "ما", "قد", "كل",
          "له", "لها", "منه", "منها", "فيه", "فيها", "عليه", "عليها", "به", "بها", "إليه", "إليها", "عنه", "عنها", "يمكن", "هو", "هي"}   # a piece never ENDS with these
_TAIL = {"جداً", "جدا", "فقط", "نفسه", "نفسها", "أيضاً", "أيضا", "كلها", "كله", "معاً"}                                     # … and never STARTS with these


def _by_stage(g, kids, junior, teen, senior):
    return {"kids": kids, "junior": junior, "teen": teen, "senior": senior}[A.stage(g)]


def _mask(text, name):
    """The clue never says the answer: the concept's name (with «ال», «و», «ب»… in front or not) becomes «…»."""
    base = name[2:] if name.startswith("ال") else name
    return re.sub(r"(?<![\w\u0600-\u06FF])[وبفلك]?(?:ال)?" + re.escape(base) + r"(?:ه|ها|ات)?(?![\w\u0600-\u06FF])", "…", text)


# ---------------------------------------------------------------- 🕵️ who am I?
def _fits(g, x, clue, target):
    """Does this clue ALSO fit concept x? (then x can not be a wrong card)"""
    t, ref = clue["type"], clue.get("ref")
    if t == "def":
        piece = _pieces(g, target)[clue["piece"]]
        return piece in (g.concepts[x].description or "")
    if t == "needs":
        return g.is_prereq(ref, x)
    if t == "needed_by":
        return g.is_prereq(x, ref)
    return False


def scene_who_am_i(g, lesson, cid, used=None, arrows=True):
    """🕵️ The concept hides behind a «؟»; its clues come one by one; the student finds it among 3 cards.
    arrows=False: only clues from its meaning (when its arrows were already said twice in this concept)."""
    me = N(g, cid)
    st = A.stage(g)
    clues = []
    ins, outs = (_ins(g, cid), _outs(g, cid)) if arrows else ([], [])
    if ins:                                                      # the softest clue first: what it needs
        y = ins[0]
        clues.append({"type": "needs", "ref": y, "say": (f"أنا {'بعتمد على' if st in ('teen', 'senior') else 'بحتاج'} «{N(g, y)}»." if st != "senior"
                                                         else f"بيعتمد على «{N(g, y)}».")})
    for i, p in enumerate(_pieces(g, cid)[:3]):                  # then its own meaning, piece by piece
        m = _mask(p, me)
        if m.replace("…", "").strip() and len(m.split()) >= 2:
            clues.append({"type": "def", "piece": i, "say": m + "."})
    if outs:
        z = outs[0]
        clues.append({"type": "needed_by", "ref": z,
                      "say": (f"«{N(g, z)}» {V(N(g, z), 'بيحتاجني', 'بتحتاجني')}." if st in ("kids", "junior") else
                              f"«{N(g, z)}» {V(N(g, z), 'بيعتمد عليّ', 'بتعتمد عليّ')}." if st == "teen" else f"«{N(g, z)}» بيعتمد عليه.")})
    if len(clues) < 2 or not any(c["type"] == "def" for c in clues):
        return None
    wrong = []
    for x in og.tiered(g, lesson, _rng("who", cid), exclude={cid}):
        if N(g, x) == me or x in {c.get("ref") for c in clues} or any(_fits(g, x, c, cid) for c in clues):   # (a card the clues name is too easy)
            continue
        d = _short_def(g, x)
        why = (f"مش أنا! «{N(g, x)}»: {d}." if d else f"مش أنا! «{N(g, x)}» شي ثاني.") if st != "senior" else \
              (f"لا، «{N(g, x)}»: {d}." if d else f"لا، «{N(g, x)}» مفهوم آخر.")
        wrong.append({"id": x, "ok": False, "why": why})
        if len(wrong) == 2:
            break
    if len(wrong) < 2:
        return None
    options = [{"id": cid, "ok": True, "why": ""}] + wrong
    _rng("who-order", cid).shuffle(options)
    told = "، ".join(c["say"].rstrip(".") for c in clues)
    win = _by_stage(g, f"🎉 صح! أنا «{me}»! {told}.", f"🎉 صح! أنا «{me}»: {told}.", f"✅ صح، أنا «{me}»: {told}.", f"✅ صحيح: «{me}». {told}.")
    return {"kind": "who_am_i", "target": cid, "clues": clues, "options": options, "start": 2, "win": win,
            "steps": [_by_stage(g, "🕵️ مين أنا؟ في شخصية مخبّاية ورا الـ«؟»!", "🕵️ مين أنا؟ شخصية مخبّاية بتعطيك أدلة.",
                                "🕵️ مين أنا؟ حزّر المفهوم من الأدلة.", "🕵️ حدّد المفهوم من الأدلة."),
                      "اقرأ الأدلة واختار البطاقة الصح. كل غلطة بتفتحلك دليل جديد."],
            "paragraph": f"«{me}»: " + "، ".join(p for p in _pieces(g, cid)[:3]) + "."
                         + (f" {V(me, 'بيحتاج', 'بتحتاج')} «{N(g, ins[0])}»." if ins else "")
                         + (f" و«{N(g, outs[0])}» {V(N(g, outs[0]), 'بيحتاج', 'بتحتاج')} «{me}»." if outs else "")}


# ---------------------------------------------------------------- 🧩 build the sentence
def _cut(words, k):
    """k pieces in reading order, as even as possible; a piece never ENDS with a small word («في», «على», «التي»…: it goes with
    what follows), so no piece is a lonely «على». Fewer pieces when the sentence has not enough places to cut."""
    ok = [j for j in range(1, len(words)) if words[j - 1] not in _SMALL and words[j].strip("،؛.") not in _TAIL]   # cut BEFORE word j
    while k >= 3:
        if len(ok) >= k - 1:
            cuts, n = [], len(words)
            for m in range(1, k):
                want = n * m / k
                best = min((j for j in ok if j not in cuts and (not cuts or j > cuts[-1])), key=lambda j: abs(j - want), default=None)
                if best is None:
                    break
                cuts.append(best)
            if len(cuts) == k - 1:
                b = [0] + cuts + [n]
                return [" ".join(words[b[i]:b[i + 1]]) for i in range(k)]
        k -= 1
    return []


def _sentences_of(g, cid):
    """[(piece index, or -1 for the whole meaning; its words)] — the pieces of 5–12 words, in the meaning's order."""
    out = [(i, p.strip(" .").split()) for i, p in enumerate(_pieces(g, cid)) if 5 <= len(p.strip(" .").split()) <= 12]
    d = (g.concepts[cid].description or "").strip(" .").split()
    if 5 <= len(d) <= 12 and all(w != d for _, w in out):
        out.append((-1, d))
    return out


def scene_sentence(g, lesson, cid, used=None, which=0):
    """🧩 The concept's meaning in 3–4 mixed pieces: tap them in order and the sentence about «X» is built.
    which = the n-th piece that can be a sentence (the next one when the first was already said twice)."""
    me = N(g, cid)
    cands = _sentences_of(g, cid)
    if which >= len(cands):
        return None
    i, words = cands[which]
    chunks = _cut(words, 3 if len(words) <= 8 else 4)
    if len(chunks) < 3:
        return None
    sentence = " ".join(chunks)
    return {"kind": "sentence", "target": cid, "chunks": chunks, "piece": i, "sentence": sentence,
            "win": _by_stage(g, f"🎉 برافو! «{me}»: {sentence}.", f"🎉 «{me}»: {sentence}.", f"✅ الجملة كاملة: «{me}»: {sentence}.", f"✅ «{me}»: {sentence}."),
            "steps": [_by_stage(g, f"🧩 ركّب جملة «{me}»!", f"🧩 ركّب جملة «{me}».", f"🧩 رتّب وصف «{me}».", f"🧩 رتّب تعريف «{me}»."),
                      f"اكبس القطع بالترتيب، لتطلع الجملة اللي بتوصف «{me}»."],
            "paragraph": f"«{me}»: {sentence}."}


def candidates(g, lesson, cid, i, used=None):
    """Every way to make one of the two, in turn order (they take turns from concept to concept): the generator takes the first
    one the fact budget lets in (a version with only the meaning, or another piece of it, when the first one was said twice already)."""
    ids = [l.id for l in g.lessons()]
    who = [lambda: scene_who_am_i(g, lesson, cid, used), lambda: scene_who_am_i(g, lesson, cid, used, arrows=False)]
    sen = [lambda w=w: scene_sentence(g, lesson, cid, used, w) for w in range(4)]
    order = [who, sen] if (i + (ids.index(lesson.id) if lesson.id in ids else 0)) % 2 == 0 else [sen, who]
    for group in order:
        for make in group:
            s = make()
            if s:
                yield s


def pick(g, lesson, cid, i, used=None):
    """The first one that can be made (no budget): one of the two."""
    return next(candidates(g, lesson, cid, i, used), None)


def check(g, s) -> list:
    """The picture must never teach something wrong."""
    k, t, errors = s["kind"], s.get("target"), []
    if t not in g.concepts or not og.is_entity(g, t):
        return [f"{k}: unknown concept {t}"]
    if k == "who_am_i":
        for c in s["clues"]:
            if c["type"] == "def" and not (0 <= c.get("piece", -1) < len(_pieces(g, t))):
                errors.append("who_am_i: a clue that is not in the meaning")
            if c["type"] == "needs" and not g.is_prereq(c["ref"], t):
                errors.append(f"who_am_i: {t} does not need {c['ref']}")
            if c["type"] == "needed_by" and not g.is_prereq(t, c["ref"]):
                errors.append(f"who_am_i: {c['ref']} does not need {t}")
        ok = [o["id"] for o in s["options"] if o["ok"]]
        if ok != [t]:
            errors.append("who_am_i: the concept must be the only right card")
        for o in s["options"]:
            if o["id"] not in g.concepts or not og.is_entity(g, o["id"]):
                errors.append(f"who_am_i: unknown concept {o['id']}")
            elif not o["ok"] and any(_fits(g, o["id"], c, t) for c in s["clues"]):
                errors.append(f"who_am_i: the clues also fit {o['id']}")
    elif k == "sentence":
        p = s.get("piece")
        src = (_pieces(g, t)[p] if isinstance(p, int) and 0 <= p < len(_pieces(g, t)) else
               (g.concepts[t].description or "") if p == -1 else None)
        if src is None or " ".join(s["chunks"]) != " ".join(src.strip(" .").split()):
            errors.append("sentence: the pieces are not the concept's own meaning")
        if len(s["chunks"]) < 3:
            errors.append("sentence: too few pieces")
    return errors
