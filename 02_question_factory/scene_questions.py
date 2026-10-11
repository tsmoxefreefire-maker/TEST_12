"""🆕 batch 42 · THE QUESTIONS A SCENE ANSWERS (the engineer: scenes made offline, a description column, and a «similarity measure»).

A student asks a QUESTION («ليش النبتة بتحتاج ماء؟»), not a concept's name. So every scene gets a description made of the
questions it answers — in the dialect AND in فصحى — plus its own words (the meaning, the steps, the «ليش؟» paragraph):
    meet (the cartoon)  → «شو هو X؟ · ما هو X؟ · شو بيحتاج X؟ · مين بيحتاج X؟»
    play (a film)       → «كيف بيصير X؟ · كيف يحدث X؟»
    what_if             → «شو بيصير لو ما في X؟ · ماذا يحدث بدون X؟»
    compare             → «شو الفرق بين X و Y؟ · ما الفرق بين X و Y؟»
    journey / chains    → «كيف بنوصل من X لـ Y؟ · ما ترتيب …؟»   …and so on for every kind.
Plain Python, no AI, no database: the API (05_explanation_api/core/scene_index.py) keeps the rows and searches them.
Also here: the text tools both sides use (norm, words, the names inside a question, character trigrams)."""
import math
import re
from collections import Counter

VERSION = "q2"                                    # bump when the questions change → every row is rebuilt (and re-embedded)
_MARKS = re.compile(r"[ً-ْٰـ]")          # tashkeel + tatweel
_PREFIXES = ("وال", "بال", "فال", "كال", "لل", "ال")
ENDINGS = ("ات", "ون", "ين", "ان", "ية", "يه", "ه", "ي")


def norm(text) -> str:
    """«النَّبتةُ بتحتاج الماء؟» → «النبته بتحتاج الماء»: no marks, one alef, ة → ه, ى → ي, no signs or emoji, lower case."""
    t = _MARKS.sub("", str(text or ""))
    t = re.sub(r"[أإآٱ]", "ا", t).replace("ة", "ه").replace("ى", "ي").replace("ؤ", "و").replace("ئ", "ي")
    t = re.sub(r"[^\w\s]|_", " ", t.lower())
    return " ".join(t.split())


def stem(w: str) -> str:
    """the word without «ال» and its long brothers (never one letter: «بيت» stays «بيت»)."""
    for p in _PREFIXES:
        if w.startswith(p) and len(w) - len(p) >= 2:
            return w[len(p):]
    return w


def words(text) -> list:
    return [stem(w) for w in norm(text).split()]


def _cut(w: str) -> str:
    """the word without ONE ending (when 3 letters stay): «قاره» and «قارات» → «قار», «كسرين» → «كسر»."""
    for e in ENDINGS:
        if w.endswith(e) and len(w) - len(e) >= 3:
            return w[:-len(e)]
    return w


def _bare(w: str) -> str:
    """the word's letters without its ending and its long vowels: «جذور» and «جذر» → «جذر», «بذور» and «بذره» → «بذر»."""
    w = _cut(w)
    return w[0] + re.sub(r"[اوي]", "", w[1:])


VERB = ("بن", "بت", "بي")                                  # the dialect's «we / you / he do» before a verb: «بنضرب» → «ضرب»


def _same(q: str, n: str) -> bool:
    """a word of the question is a word of the name: the same · + an ending («نباتات» ← «نبات», «قارة» ← «القارات») ·
    a broken plural («الجذور» ← «الجذر», «البذور» ← «البذرة»: same letters without the long vowels; long words only) ·
    a dialect verb of it («بنضرب» ← «الضرب»)."""
    if q == n or (len(n) >= 3 and _cut(q) == _cut(n)):
        return True
    if len(n) >= 3 and q.startswith(n) and q[len(n):] in ENDINGS:
        return True
    if len(q) >= 3 and n.startswith(q) and n[len(q):] in ENDINGS:
        return True
    if len(n) >= 3 and any(q.startswith(v) and len(q) >= 5 and (q[2:] == n or _bare(q[2:]) == _bare(n)) for v in VERB):
        return True                                                   # «بنضرب» ← «الضرب», «بتسقط» ← «السقوط»
    return max(len(q), len(n)) >= 4 and min(len(q), len(n)) >= 3 and len(_bare(q)) >= 3 and _bare(q) == _bare(n)


def name_at(name, question) -> int:
    """where the name starts in the question (word number), or 99: the concept he says FIRST is usually what he asks about."""
    n, q = words(name), words(question)
    for i in range(len(q)):
        if n and any(_same(q[i], w) for w in n):
            return i
    return 99


def name_share(name, question) -> float:
    """how much of the NAME is in the question (1 = all of it; «ضوء الشمس» in «بدها شمس» → 0.5)."""
    n, q = words(name), words(question)
    return sum(1 for w in n if any(_same(x, w) for x in q)) / len(n) if n else 0.0


def name_in(name, question) -> bool:
    """is this concept's NAME inside the question (all its words, in order, next to each other)?"""
    n, q = words(name), words(question)
    if not n or len(n) > len(q):
        return False
    return any(all(_same(q[i + k], n[k]) for k in range(len(n))) for i in range(len(q) - len(n) + 1))


# the words of ASKING (dialect + فصحى): they say WHAT KIND of answer he wants (what / why / how / the difference), not WHICH concept
ASK_WORDS = set(norm("""شو ما ماذا لماذا ليش ليه كيف كيفاش وين اين أين متى امتى مين من هو هي هم هن يعني معنى تعريف عرفني احكيلي
    اشرحلي اشرح فهمني بدي أريد اريد أعرف اعرف ممكن لو على عن في الى إلى بين الفرق الشبه الاختلاف أوجه اوجه بيصير يصير بتصير
    يحدث تصير بيحتاج يحتاج بتحتاج تحتاج بيحتاجوا يحتاجون مهم مهمة أهمية اهمية ليش وليش ايش إيش هل كم انو إنه انه هاد هذا هذه
    هاي اللي الذي التي بدون بلا شي شيء إشي اشي""").split())


PAIR = re.compile(r"(^| )(الفرق|فرق|الشبه|شبه|بين|قارن|نقارن|بنقارن|مقارنه|العلاقه|علاقه|الاختلاف)( |$)")   # (on norm() text) he asks about TWO concepts


def content_words(text) -> list:
    """the words of the question that name THINGS (without the asking words)."""
    return [w for w in norm(text).split() if w not in ASK_WORDS and stem(w) not in ASK_WORDS]


def trigrams(text, content: bool = False) -> Counter:
    """the letters three by three («ماء» → « ما»، «ماء»، «اء »): close spellings and close questions share most of them.
    content=True: only the words that name things (to find WHICH concept); all the words: to find which scene of it (what kind of answer)."""
    out = Counter()
    for w in (content_words(text) if content else norm(text).split()):
        w = f" {stem(w)} "
        for i in range(len(w) - 2):
            out[w[i:i + 3]] += 1
    return out


def cosine(a: Counter, b: Counter) -> float:
    if not a or not b:
        return 0.0
    dot = sum(v * b.get(k, 0) for k, v in a.items())
    return dot / (math.sqrt(sum(v * v for v in a.values())) * math.sqrt(sum(v * v for v in b.values())))


# ---------- the questions of a scene ----------
def _names(g, ids) -> list:
    return [g.concepts[i].text for i in ids if i in g.concepts]


def _ins(g, x):
    return _names(g, [p for p in g.prereq_in.get(x, [])])


def _outs(g, x):
    return _names(g, [n for n in g.prereq_out.get(x, [])])


def _clean(t: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"[«»📌🎉🙂😐🧲🪃🎚️⚖️🐝🍎💡❓]", "", str(t or ""))).strip()


def _li(n: str) -> str:
    """«لـ» stuck to the name the Arabic way: «الاسم» → «للاسم», «ماء» → «لماء»."""
    return "ل" + n[1:] if n.startswith("ال") else "ل" + n


def _bi(n: str) -> str:
    return "ب" + n


PRACTICE = {"recipe", "connect", "teach", "ladder", "throw", "tower", "magnet", "machine", "power", "who_am_i", "sentence"}


def questions(g, lesson_title: str, cid: str, scene: dict) -> list:
    """The questions ONE scene answers (dialect + فصحى). cid = its concept ('' for the lesson's own scenes)."""
    k = scene.get("kind", "")
    X = g.concepts[cid].text if cid in g.concepts else ""
    L = lesson_title
    q = []
    if k == "overview":
        q += [f"شو بندرس بدرس {L}؟", f"ما هي مفاهيم درس {L}؟", f"ملخص درس {L}", f"شو مفاهيم {L} ومين بيحتاج مين؟"]
    elif k in ("assemble", "world", "build_up", "missing", "tour"):          # 🆕 batch 42: the lesson's «parts» scene, every way
        q += [f"كيف بترتبط مفاهيم {L} ببعض؟", f"ما العلاقة بين مفاهيم {L}؟", f"شو أجزاء {L}؟", f"ما مكونات {L}؟"]
        if k == "build_up":
            q += [f"شو الأساس بـ{L}؟", f"كيف بتنبني {L} من الأساس؟"]
        if k == "missing":
            q += [f"شو بيصير لو نقص جزء من {L}؟"]
        if k == "tour":
            q += [f"خدني جولة بـ{L}", f"اشرحلي أجزاء {L} واحد واحد"]
    elif k == "meet":
        q += [f"شو هو {X}؟", f"ما هو {X}؟", f"شو يعني {X}؟", f"ما معنى {X}؟", f"عرفني على {X}", f"ما تعريف {X}؟"]
        for y in _ins(g, cid)[:3]:
            q += [f"ليش {X} بيحتاج {y}؟", f"لماذا يحتاج {X} إلى {y}؟"]
        for y in _outs(g, cid)[:3]:
            q += [f"ليش {y} بيحتاج {X}؟", f"ما أهمية {X} {_li(y)}؟"]
        q += [f"شو بيحتاج {X}؟", f"ماذا يحتاج {X}؟", f"مين بيحتاج {X}؟", f"ليش {X} مهم؟"]
    elif k == "play":
        q += [f"كيف بيصير {X}؟", f"كيف يحدث {X}؟", f"شو بيصير {_bi(X)}؟", f"اشرحلي {X} خطوة خطوة", f"كيف تتم عملية {X}؟"]
    elif k == "what_if":
        q += [f"شو بيصير لو ما في {X}؟", f"شو بيصير لو اختفى {X}؟", f"ماذا يحدث بدون {X}؟", f"ماذا لو اختفى {X}؟", f"ليش {X} مهم؟"]
        q += [f"شو بيصير {_li(y)} بدون {X}؟" for y in _names(g, scene.get("affected", []))[:3]]
    elif k == "compare":
        Y = g.concepts[scene["other"]].text if scene.get("other") in g.concepts else ""
        q += [f"شو الفرق بين {X} و{Y}؟", f"ما الفرق بين {X} و{Y}؟", f"شو الشبه بين {X} و{Y}؟", f"ما أوجه الشبه والاختلاف بين {X} و{Y}؟"]
    elif k in ("journey", "ladder", "tower", "machine", "power"):
        chain = _names(g, scene.get("route") or [])
        if len(chain) >= 2:
            q += [f"كيف بنوصل من {chain[0]} {_li(chain[-1])}؟", f"ما ترتيب {' و'.join(chain)}؟", f"شو بيجي قبل {chain[-1]}؟"]
        q += [f"شو بيحتاج {X}؟", f"ماذا يحتاج {X}؟", f"شو الخطوات لحد {X}؟"]
    elif k == "slider":
        q += [f"كيف بيشتغل {X}؟", f"كيف بيتغير {X}؟", f"جربلي {X} بالأرقام", f"ما قاعدة {X}؟"]
    elif k == "before_after":
        B = g.concepts[scene["before"]].text if scene.get("before") in g.concepts else ""
        q += [f"كيف بيصير {B} {X}؟", f"كيف يتحول {B} إلى {X}؟", f"شو بيطلع من {B}؟", f"ما العلاقة بين {B} و{X}؟"]
    elif k == "who_am_i":                                                  # 🆕 batch 43
        q += [f"حزّرني مين هو {X}", f"لعبة مين أنا عن {X}", f"شو أدلة {X}؟", f"ما صفات {X}؟"]
    elif k == "sentence":
        q += [f"رتبلي تعريف {X}", f"ما تعريف {X}؟", f"شو معنى {X}؟", f"احفظ تعريف {X}"]
    elif k in ("interview", "flip", "lens", "dialogue", "custom"):          # (custom = a scene the model wrote and a teacher approved)
        q += [f"احكيلي عن {X}", f"معلومات عن {X}", f"ما خصائص {X}؟", f"شو بتعرف عن {X}؟"]
    if k in PRACTICE or k == "compare":
        q += [f"بدي أتمرن على {X}", f"تمرين على {X}", f"لعبة عن {X}"]
        q += [f"شو بيحتاج {X}؟", f"مين بيحتاج {X}؟"] if k in ("magnet", "throw", "recipe", "connect", "teach") else []
    out, seen = [], set()
    for x in q:
        x = re.sub(r"\s+", " ", x).strip()
        if x and norm(x) not in seen:
            seen.add(norm(x)); out.append(x)
    return out


def description(g, lesson_title: str, cid: str, scene: dict, qs: list = None) -> str:
    """the description column: the questions + the concept's meaning + the scene's own words (what the search reads)."""
    parts = list(qs if qs is not None else questions(g, lesson_title, cid, scene))
    if cid in g.concepts and g.concepts[cid].description:
        parts.append(g.concepts[cid].description)
    parts += [_clean(s) for s in scene.get("steps", [])]
    if scene.get("paragraph"):
        parts.append(_clean(scene["paragraph"]))
    return " · ".join(p for p in parts if p)
