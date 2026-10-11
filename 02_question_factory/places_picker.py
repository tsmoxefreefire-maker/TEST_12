"""🆕 batch 39 (Hareth: «خلفيات مناسبة لكل درس ولكل مفهوم ولكل مادة» + «المادة الغريبة… بتاخد مكان غرفة بدل مطبخ»)
The PLACE of every lesson and the little WORLD (zone) of every concept, picked from the words of the graph — no AI, no cost.

· lesson place: the JSON's "place" wins (the book or the lesson node); else the words of the lesson (its title counts more, then the
  names of its concepts, then the book's subject and title) → the best place; nothing matches → None (the page picks by the subject);
· concept zone: the words of the concept's name (counts more) and its meaning → the best zone (under the ground, inside the cell,
  the atoms, the rainy sky, the road of motion, numbers, the library, an ancient land, the energy workshop, or a place: sea, space…);
  a zone equal to the lesson's place is dropped (it would change nothing);
· a learned place (place_library.py: a recipe made from our pieces, saved once — later the model can add new ones) wins when its
  own words match better than the built-in places (it is how a strange subject gets a fitting place once, then for free).
The page draws them (places.js + zones.js). Longer words count more (they are more precise: «ضوء الشمس» before «شمس»)."""
import place_library

# the lesson's place (the 12 places of the page)
PLACE_WORDS = {
    "garden": ["نبات", "نبتة", "زهر", "بذر", "بذور", "شجر", "حديقة", "ورق", "جذر", "ثمر", "تربة", "إنبات", "تلقيح"],
    "forest": ["غابة", "حيوان", "مفترس", "بيئة", "سلسلة غذائية", "فريسة"],
    "sea": ["بحر", "محيط", "سمك", "موج", "شاطئ", "مرجان"],
    "space": ["فضاء", "كوكب", "نجم", "قمر", "مجرة", "حركة", "قوة", "سرعة", "جاذبية", "تسارع", "إزاحة", "مسافة"],
    "lab": ["خلية", "خلايا", "خلوي", "خلية نباتية", "خلية حيوانية", "بلاستيد", "فجوة", "ذرة", "ذرات", "عنصر", "مركب", "تفاعل", "حمض", "محلول",
            "إلكترون", "أيون", "رابطة", "وراث", "جين", "كروموسوم", "صفات", "مادة", "كيمياء",
            "جراثيم", "بكتيريا", "فيروس", "عدوى", "مناعة", "لقاح", "تطعيم", "ميكروب"],                 # 🆕 batch 40: germs are looked at in the lab
    "machine": ["طاقة", "كهرب", "تيار", "دارة", "بطارية", "مغناطيس", "آلة", "محرك"],
    "classroom": ["عدد", "أعداد", "جمع", "طرح", "ضرب", "قسمة", "كسر", "كسور", "معادلة", "اقتران", "إحداثي", "هندسة", "رياضيات"],
    "desert": ["فرعون", "فراعنة", "هرم", "أهرام", "نيل", "حضارة", "آثار", "تاريخ"],
    "map": ["جغرافيا", "قارة", "خريطة", "مناخ", "تضاريس", "أرض", "دولة"],
    "notebook": ["لغة", "حرف", "حروف", "كلمة", "كلمات", "جملة", "قواعد", "نحو", "إملاء"],
    "city": ["مدينة", "مجتمع", "وطن", "مواطن", "اقتصاد", "سوق", "مرور"],
    "kitchen": ["طبخ", "طعام", "أكل", "خبز", "عجين", "وصفة", "مطبخ", "تغذية", "خميرة"],
}
# the little world of a concept (zones.js) — or a place of the page
ZONE_WORDS = {
    "underground": ["جذر", "جذور", "تربة", "باطن الأرض", "دودة", "صخر", "تحت الأرض"],
    "cell": ["خلية", "خلايا", "نواة", "سيتوبلازم", "غشاء", "ميتوكندري", "كروموسوم", "صبغي", "جين", "وراث", "بروتين", "عضي"],
    "atoms": ["ذرة", "ذرات", "إلكترون", "الكترون", "بروتون", "نيوترون", "أيون", "جزيء", "رابطة", "عنصر", "مركب", "تكافؤ"],
    "sky": ["ماء", "مطر", "غيم", "سحاب", "هواء", "رياح", "طقس", "تبخر", "تكاثف", "ضوء الشمس", "أكسجين"],
    "motion": ["حركة", "سرعة", "تسارع", "قوة", "مسافة", "إزاحة", "موقع", "زمن", "احتكاك", "جاذبية", "سقوط"],
    "numbers": ["عدد", "أعداد", "جمع", "طرح", "ضرب", "قسمة", "كسر", "كسور", "مقام", "بسط", "معادلة", "اقتران", "إحداثي", "نسبة", "منزلة"],
    "library": ["حرف", "حروف", "كلمة", "كلمات", "جملة", "اسم", "فعل", "مبتدأ", "خبر", "قراءة", "كتابة"],
    "ancient": ["فرعون", "فراعنة", "هرم", "أهرام", "نيل", "حضارة", "ملك", "معبد", "آثار", "كتابة الهيروغليفية"],
    "machine": ["طاقة", "كهرب", "تيار", "دارة", "بطارية", "مغناطيس", "آلة", "محرك", "مصباح"],
    "sea": ["بحر", "محيط", "سمك", "موج", "شاطئ", "نهر"],
    "space": ["كوكب", "كواكب", "نجم", "نجوم", "قمر", "مجرة", "فضاء", "مدار"],
    "forest": ["غابة", "حيوان", "حيوانات", "مفترس", "سلسلة غذائية"],
    "kitchen": ["طبخ", "طعام", "خبز", "عجين", "وصفة", "خميرة", "تخمير", "فرن"],
    "city": ["مدينة", "مجتمع", "سوق", "تجارة", "مواطن", "مصنع", "اقتصاد"],
}
PLACES = tuple(PLACE_WORDS) + ("room",)
ZONES = tuple(ZONE_WORDS)


_PRE = ("وال", "بال", "فال", "كال", "لل", "ال")


def _norm(text):
    """The words of a text without «ال» (and «وال، بال، لل…») in front: «البذرة» → «بذرة», «والحيوانية» → «حيوانية»."""
    out = []
    for w in str(text or "").replace("،", " ").replace("·", " ").split():
        for p in _PRE:
            if w.startswith(p) and len(w) > len(p) + 1:
                w = w[len(p):]
                break
        out.append(w)
    return out


def _has(word, toks, joined):
    """A keyword is found when a word STARTS with it («بذرة» is not «ذرة», «أسماء» is not «ماء»); a phrase is found in the joined words."""
    k = " ".join(_norm(word))
    return k in joined if " " in k else any(t.startswith(k) for t in toks)


def _score(words, texts):
    """texts = [(text, weight)]: every keyword found counts its length × the weight of the text it was found in."""
    s = 0
    for t, k in texts:
        toks = _norm(t)
        joined = " " + " ".join(toks) + " "
        s += sum(len(w) * k for w in words if w and _has(w, toks, joined))
    return s


def _best(table, texts, extra=None, least=2):
    scores = {name: _score(words, texts) for name, words in table.items()}
    for rid, rec in (extra or {}).items():                               # learned places (place_library.py)
        scores[rid] = _score(rec.get("words", []), texts) + 1             # +1: a place made for these words wins a tie
    best = max(scores.items(), key=lambda kv: kv[1], default=(None, 0))
    return best[0] if best[1] >= least else None


def lesson_place(g, lesson, given=None):
    """The lesson's place: given (the JSON) → else from its words → else None (the page picks by the subject)."""
    if given:
        return given
    texts = [(lesson.title, 3)] + [(c.text, 1) for c in lesson.concepts] + \
            [(str(g.book.get("subject", "")), 1), (str(g.book.get("title", "")), 1)]
    return _best(PLACE_WORDS, texts, place_library.recipes())


def concept_zones(g, lesson, place):
    """{concept: zone} for the concepts of the lesson that have a world of their own (and it is not the lesson's place)."""
    out = {}
    for c in lesson.concepts:                                                              # Concept objects (graph_reader)
        z = _best(ZONE_WORDS, [(c.text, 3)])                                               # its NAME first (precise)
        if not z:                                                                          # else its meaning, only when it clearly says so
            z = _best(ZONE_WORDS, [(c.description or "", 1)], least=9)
        if z and z != place:
            out[c.id] = z
    return out
