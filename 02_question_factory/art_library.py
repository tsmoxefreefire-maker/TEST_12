"""🆕 batch 40 · THE GROWING LIBRARY OF DRAWINGS (Hareth: «لازم نوسّع الليغو بشكل كبير… تغطي كل الدروس وكل المواد من الصغار للثانوية»
+ «إحنا بنركّز على المنهج السعودي» + «مفهوم إله رسمة خلص… ليش ننشئ مليون رسمة؟» + «المواد الإسلامية لا تقرب إلها»).

· ONE CONCEPT = ONE DRAWING, made once, used everywhere: in every grade, every book, for every student.
· A drawing is DATA: {words, body (SVG in our style, 0–100 box), face (where our face goes), anim} — a few hundred bytes. The family files
  in art_lib/ hold them (science, maths, language, social, English and life, digital…). Tomorrow they can live in the database.
· THE ALIAS TABLE: other names of the same concept → the SAME drawing («البناء الضوئي» and «التمثيل الضوئي» → the leaf; «الجذور» → the root),
  so nothing is drawn twice. An alias can point to an old drawing of the page or to a new one of the library.
· CARDS: one drawing with a symbol on it serves many concepts of language and maths («همزة القطع» → «أ», «التاء المربوطة» → «ة», «ستة» → «٦»).
· EACH BOOK CARRIES ONLY ITS DRAWINGS (for_book): the library can grow to thousands of drawings and the page does not get heavier.
· How a concept finds its drawing (offline_generator.icon_for): the old drawings by NAME first → an EXACT name of the alias table →
  the library by the words of the NAME (the longest word wins, «الطاقة المتجددة» before «الطاقة») → the old drawings by the MEANING →
  Lego → the subject's character. No AI, no cost.
    python art_library.py                 # checks every drawing (allowed SVG only, inside the box, words not taken twice)"""
import importlib
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

OL = 'stroke="#3b2a1a" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"'   # the outline of every drawing (= the page's OL)
FAMILIES = ("science", "body", "earth", "matter", "math", "language", "social", "english", "digital", "life", "biology", "chemistry",   # 🆕 batch 41: + biology, chemistry
            "everyday", "money", "mind", "physics", "geo", "ecology", "tech", "civics", "math2", "english2")   # 🆕 batch 43: + the everyday, money, thinking, physics, earth & space, ecology, digital, maths and English drawings
ANIMS = ("bob", "sway", "wobble", "bounce", "wiggle", "sun", "drip", "grow", "leaf", "wind", "buzz", "chug")
# the subjects a drawing may be limited to (a word means different things in different subjects)
TAGS = {"math": ("math", "رياضيات"), "arabic": ("arabic", "عربي", "لغتي", "لغة عربية", "language"), "english": ("english", "إنجليزي", "انجليزي"),
        "science": ("science", "علوم", "biology", "أحياء", "chem", "كيمياء", "physic", "فيزياء", "earth", "أرض", "environment", "بيئة"),
        "social": ("social", "اجتماعي", "geograph", "جغرافيا", "history", "تاريخ", "وطنية"), "digital": ("computer", "digital", "رقمي", "حاسب", "حاسوب", "تقنية"),
        "life": ("life", "حياتية", "أسرية"), "finance": ("finance", "مالية"), "thinking": ("thinking", "تفكير"),
        "biology": ("biology", "أحياء"), "chemistry": ("chem", "كيمياء"),   # 🆕 batch 41: a biology book only (in science grade 5 «الامتصاص» is light, in biology it is the villi)
        "physics": ("physic", "فيزياء"), "earth": ("earth", "أرض", "جيولوج")}   # 🆕 batch 43: «البؤرة» is a lens's focus in physics, an earthquake's in earth science
_ALLOWED = re.compile(r"<(/?)(path|circle|ellipse|rect|line|polyline|polygon|g|text|tspan)\b")
_TAG = re.compile(r"<(/?)([a-zA-Z]+)")
_NUM = re.compile(r"-?\d+(?:\.\d+)?")
_PREFIXES = ("وال", "بال", "فال", "كال", "لل", "ال", "و", "ب", "ف", "ل")
_cache = None
# 🆕 never a cartoon (Hareth: «المواد الإسلامية لا تقرب إلها»): anything religious, the national symbols, and people with a royal or
# religious title — the subject's character just carries the name (respect first; no drawing is better than a wrong one)
NEVER_DRAW = re.compile(r"الحرم|الكعبة|مسجد|المساجد|القرآن|قرآن|الصلاة|الحج\b|العمرة|الصيام|الزكاة|النبي|الرسول|صلى الله|الأنبياء|الصحاب|الخلفاء الراشد|"
                        r"السيرة النبوية|الإسلام|إسلامي|الخلافة|الشعار الوطني|العلم الوطني|النشيد الوطني|الرموز الوطنية|الملك |الملكة |الإمام|الأمير|"
                        r"ولي العهد|خادم الحرمين|الشيخ |البيعة")


def tags_of(subject):
    s = str(subject or "").lower()
    return {t for t, words in TAGS.items() if any(w in s for w in words)}


def _norm(text):
    """«الجذور» → «جذور»: the name without «ال» and the marks around it, for the alias table."""
    t = re.sub(r"[«»()\[\]،,.:؛\"']", " ", str(text or ""))
    t = " ".join(t.split())
    return t[2:] if t.startswith("ال") and len(t) > 3 else t


ENDINGS = ("", "ة", "ه", "ات", "ان", "ين", "ي", "ية")


def _strip(w):
    """«والجذور» → «جذور»: only the long prefixes (وال، بال، فال، كال، لل، ال). Never one letter alone: «بطاقة» is not «ب + طاقة»."""
    for p in _PREFIXES[:6]:
        if w.startswith(p) and len(w) - len(p) >= 2:
            return w[len(p):]
    return w


def _words(text):
    return re.findall(r"[\w\u0600-\u06FF]+", str(text or "").lower())


def _forms(tok):
    """The word and the word without its ending («شمسية» → شمسية، شمس), with and without its prefix."""
    out = set()
    for t in {tok, _strip(tok)}:
        for e in ENDINGS:
            if e and t.endswith(e) and len(t) - len(e) >= 2:
                out.add(t[:-len(e)])
        out.add(t)
    return out


def _joined(text):
    return " " + " ".join(_strip(w) for w in _words(text)) + " "


def _key_word(w):
    w = " ".join(_strip(x) for x in _words(w))
    return w


def _load():
    """{key: record} + {normalized name: key} from every family file of art_lib/ (and the cards they make)."""
    global _cache
    if _cache is not None:
        return _cache
    recs, alias, order, single, phrase = {}, {}, [], {}, []
    for fam in FAMILIES:
        try:
            m = importlib.import_module("art_lib." + fam)
        except ImportError:
            continue
        pre = getattr(m, "F", fam[:4])
        for k, r in getattr(m, "D", {}).items():
            key = f"{pre}.{k}"
            rec = dict(r)
            rec["body"] = rec["body"].replace("{OL}", OL)
            rec.setdefault("face", (50, 55, 0.8)) if "face" not in rec else None
            rec.setdefault("anim", "bob")
            rec.setdefault("words", [])
            rec["family"] = fam
            recs[key] = rec
            order.append(key)
            for w in rec["words"]:
                kw = _key_word(w)
                if not kw:
                    continue
                (phrase.append((" " + kw + " ", key, len(kw))) if " " in kw else single.setdefault(kw, []).append((key, len(kw))))
        only = getattr(m, "ALIAS_ONLY", None)              # the subjects these aliases are for («المحيط» = an ocean in science, a perimeter in maths)
        for name, key in getattr(m, "ALIASES", {}).items():
            own = only
            if isinstance(key, tuple):                         # 🆕 batch 43: (key, its own subjects) — one alias limited, the others not
                key, own = key
            key = key if (":" in key or "." not in key) else "lib:" + key
            alias.setdefault(_norm(name), []).append((key, tuple(own or ())))
    _cache = (recs, alias, order, single, phrase)
    return _cache


def drawings():
    return _load()[0]


def record(key):
    """One drawing (key with or without «lib:»), or None."""
    return drawings().get(key[4:] if key.startswith("lib:") else key)


def exact(name, subject=""):
    """The alias table: this exact concept name → its drawing key («lib:…» or one of the page's old keys), or None."""
    tg = tags_of(subject)
    for k, only in _load()[1].get(_norm(name), []):
        if only and not (tg & set(only)):
            continue
        if k.startswith("lib:") and not record(k):                  # (the alias's own subjects decide, not the drawing's)
            continue
        return k
    return None


def never(name):
    """True for the concepts that never get a cartoon (religious, national symbols, titled people)."""
    return bool(NEVER_DRAW.search(str(name or "")))


def by_words(name, subject="", own=False, with_len=False):
    """The library drawing whose word is found in the concept's NAME (the longest word wins), or None.
    own=True: only the drawings made for THIS subject (they come before the general old words: Arabic «الكتابة» is writing, not hieroglyphs)."""
    recs, _, _, single, phrase = _load()
    tg, joined = tags_of(subject), _joined(name)
    cands = []
    for tok in _words(name):
        for f in _forms(tok):
            cands += single.get(f, [])
    cands += [(k, n) for ph, k, n in phrase if ph in joined]
    best, blen = None, 0
    for key, n in cands:
        r = recs[key]
        if r.get("only") and not (tg & set(r["only"])):
            continue
        if own and not r.get("only"):
            continue
        if r.get("never") and (tg & set(r["never"])):
            continue
        if n > blen:
            best, blen = key, n
    if with_len:
        return ("lib:" + best, blen) if best else None
    return "lib:" + best if best else None


def word_len(word):
    """How long a word is for «the longest word wins» (the same measure for the old words and the library's)."""
    return len(_key_word(word))


def for_book(keys):
    """{key: {"body", "face", "anim"}} for the «lib:» keys a book uses — only those go into the book (the page stays light)."""
    out = {}
    for k in sorted({re.sub(r"~\d+$", "", str(x)) for x in keys}):            # «lib:body.germ~2» is the same drawing in another colour
        r = record(k) if str(k).startswith("lib:") else None
        if r:
            out[k[4:]] = {"body": r["body"], "face": list(r["face"]) if r.get("face") else None, "anim": r["anim"]}
    return out


def check(key, r):
    """The problems of one drawing ([] = good): only simple SVG shapes (no script, no links, no ids), inside the 0–100 box, a face, words."""
    p = []
    b = r.get("body", "")
    for m in _TAG.finditer(b):
        if not _ALLOWED.match(b, m.start()):
            p.append(f"tag «{m.group(2)}» is not allowed")
    if re.search(r"\son\w+=|href|url\(|\sid=|<script|javascript:", b, re.I):
        p.append("no events, links, ids or url()")
    shapes = re.sub(r"#[0-9A-Fa-f]{3,8}", "", re.sub(r">[^<]*<", "><", b))   # the words on a card and the colours are not coordinates
    nums = [float(x) for x in _NUM.findall(re.sub(r'(stroke-width|font-size|opacity|r|rx|ry|stroke-dasharray|font-weight|transform)="[^"]*"', "", shapes))]
    if nums and (min(nums) < -25 or max(nums) > 125):                 # (relative path steps can be negative: a soft check)
        p.append(f"outside the box ({min(nums)}…{max(nums)})")
    f = r.get("face")
    if f is not None and not (isinstance(f, (list, tuple)) and len(f) == 3 and 0 <= f[0] <= 100 and 0 <= f[1] <= 100 and 0.3 <= f[2] <= 1.4):
        p.append("face = (x, y, size) inside the box")
    if r.get("anim") not in ANIMS:
        p.append(f"anim must be one of {ANIMS}")
    if not r.get("words") and not r.get("alias_only"):
        p.append("no words (nobody would find it)")
    return p


def problems():
    recs, alias = _load()[:2]
    out = []
    seen = {}
    for k, r in recs.items():
        out += [f"{k}: {x}" for x in check(k, r)]
        for w in r.get("words", []):
            n = _norm(w)
            if n in seen and seen[n] != k and not (set(r.get("only") or ()) ^ set(recs[seen[n]].get("only") or ())):
                out.append(f"{k}: the word «{w}» is already a word of {seen[n]}")
            seen.setdefault(n, k)
    for n, ks in alias.items():
        for k, _ in ks:
            if k.startswith("lib:") and k[4:] not in recs:
                out.append(f"alias «{n}» → {k}: no such drawing")
    return out


if __name__ == "__main__":
    recs, alias = _load()[:2]
    pr = problems()
    print("\n".join(pr) if pr else f"OK · {len(recs)} drawings · {len(alias)} aliases")
    sys.exit(1 if pr else 0)
