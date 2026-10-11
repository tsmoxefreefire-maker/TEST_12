"""🆕 batch 39 · THE LIBRARY OF PLACES THAT GROWS BY ITSELF (💡 Hareth's problem: variety + a strange new subject)
A place is a RECIPE (data, a few hundred bytes), never new code: which sky, which ground, which pieces where — always from OUR pieces
(the same ones the page draws: places.js / zones.js), so it is never distorted and always looks like the rest of the platform.

    {"id": "bakery", "label": "مخبز", "words": ["خبز", "عجين", "فرن"], "sky": ["#FFF6EC", "#FDEBD8"], "ground": ["#E9D3B6", "#D9BE98"],
     "far": "tiles", "farColor": "#EADFD2", "skyItems": [], "props": [["fridge", 0.07, 0, 1], ["potkit", 0.86, 0, 1]], "extras": [["chef", 0.2, 0, 0.9]]}

· today the library is a file (place_library.json, next to the factory); tomorrow the DATABASE (the same functions: recipes / add);
· a recipe is CHECKED before it is saved (check): known pieces only, numbers in range, real colours, a short Arabic label;
· with the model (use_llm, only when a new subject has no fitting place): ask_model asks ONCE for a recipe from our list of pieces,
  checks it, saves it — the next lesson of that subject gets it for free. Without keys nothing is asked and nothing changes."""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
PATH = os.environ.get("PLACE_LIBRARY", os.path.join(HERE, "place_library.json"))
# the pieces the page can draw (places.js PLP + zones.js) and the little extras (PLX) — test_batch39 checks they all exist in the page
PIECES = ("tree", "pine", "bush", "flower", "grass", "rock", "cloud", "sun", "flask", "tubes", "burner", "planet", "star", "rocket", "board",
          "clock", "books", "pyramid", "palm", "cactus", "compass", "boat", "waves", "mountain", "pencil", "letter", "window", "lamp", "pot",
          "shelf", "fish", "seaweed", "coral", "building", "car", "light", "potkit", "fridge", "mushroom",
          "worm", "pebble", "roots", "mito", "vesicle", "er", "atom", "particle", "raincloud", "rainbow", "ball", "ruler", "flag", "sym",
          "numline", "bookshelf", "column", "obelisk", "scroll", "gear", "bulb", "battery", "wire")
EXTRAS = ("bird", "robot", "astronaut", "kid", "camel", "owl", "cat", "crab", "pigeon", "chef", "snail")
MOTIONS = ("still", "sway", "sway2", "bob", "float0", "float1", "float2", "wiggle", "spin-slow", "twinkle0", "twinkle1", "twinkle2", "drift2", "bubble", "swim", "wave")
FARS = ("", "hills", "wall", "tiles")
SKY_ITEMS = ("sun", "clouds", "stars")
_HEX = re.compile(r"^#[0-9A-Fa-f]{6}$")
_ID = re.compile(r"^[a-z][a-z0-9_]{1,30}$")
_cache = None


def recipes() -> dict:
    """{id: recipe} — the learned places (empty when there are none yet)."""
    global _cache
    if _cache is None:
        try:
            with open(PATH, encoding="utf-8") as f:
                _cache = {k: v for k, v in json.load(f).items() if not check(v)}
        except (OSError, ValueError):
            _cache = {}
    return _cache


def check(r) -> list:
    """What is wrong with a recipe ([] = good). Only our pieces, sensible numbers, real colours."""
    bad = []
    if not isinstance(r, dict):
        return ["not a recipe"]
    if not _ID.match(str(r.get("id", ""))):
        bad.append("id: small latin letters / digits / _")
    if not (isinstance(r.get("label"), str) and 1 <= len(r["label"]) <= 20):
        bad.append("label: a short name (Arabic)")
    if not (isinstance(r.get("words"), list) and all(isinstance(w, str) and 1 < len(w) < 25 for w in r["words"]) and len(r["words"]) <= 20):
        bad.append("words: up to 20 short words")
    for k in ("sky", "ground"):
        v = r.get(k)
        if v is not None and not (isinstance(v, list) and len(v) == 2 and all(isinstance(c, str) and _HEX.match(c) for c in v)):
            bad.append(f"{k}: two colours like #A1B2C3")
    if r.get("far", "") not in FARS:
        bad.append("far: hills / wall / tiles / nothing")
    if r.get("farColor") is not None and not (isinstance(r["farColor"], str) and _HEX.match(r["farColor"])):
        bad.append("farColor: a colour like #A1B2C3")
    if not all(x in SKY_ITEMS for x in r.get("skyItems", [])):
        bad.append("skyItems: sun / clouds / stars")
    props = r.get("props", [])
    if not (isinstance(props, list) and 1 <= len(props) <= 14):
        bad.append("props: 1 to 14 pieces")
    else:
        for p in props:
            if not (isinstance(p, list) and 2 <= len(p) <= 6 and p[0] in PIECES and isinstance(p[1], (int, float)) and 0 <= p[1] <= 1):
                bad.append(f"prop {p!r}: [piece, x 0..1, dy, scale, colour, motion]")
                continue
            if len(p) > 2 and not (isinstance(p[2], (int, float)) and -200 <= p[2] <= 60):
                bad.append(f"prop {p[0]}: dy -200..60")
            if len(p) > 3 and not (isinstance(p[3], (int, float)) and 0.3 <= p[3] <= 2.5):
                bad.append(f"prop {p[0]}: scale 0.3..2.5")
            if len(p) > 4 and p[4] is not None and not (isinstance(p[4], str) and _HEX.match(p[4])):
                bad.append(f"prop {p[0]}: colour like #A1B2C3")
            if len(p) > 5 and p[5] not in MOTIONS:
                bad.append(f"prop {p[0]}: a motion of the list")
    for x in r.get("extras", []):
        if not (isinstance(x, list) and 2 <= len(x) <= 4 and x[0] in EXTRAS and isinstance(x[1], (int, float)) and 0 <= x[1] <= 1):
            bad.append(f"extra {x!r}: [extra, x 0..1, dy, scale]")
    return bad


def add(r) -> bool:
    """Save a checked recipe in the library (today the file; with the database: the same call). True = saved."""
    if check(r):
        return False
    lib = dict(recipes())
    lib[r["id"]] = r
    with open(PATH, "w", encoding="utf-8") as f:
        json.dump(lib, f, ensure_ascii=False, indent=1)
    global _cache
    _cache = lib
    return True


def prompt(subject: str, lesson_title: str, concept_names: list) -> str:
    """What the model is asked (once): a recipe from OUR pieces only, as JSON."""
    return ("Design a background PLACE for an educational cartoon, as JSON only (no prose). Subject: «%s». Lesson: «%s». Concepts: %s.\n"
            "Use ONLY these pieces: %s. Extras (little background characters): %s. Motions: %s. far: %s. skyItems: %s.\n"
            'Format: {"id":"latin_id","label":"اسم عربي قصير","words":["كلمات","المادة"],"sky":["#RRGGBB","#RRGGBB"],"ground":["#RRGGBB","#RRGGBB"],'
            '"far":"tiles","farColor":"#RRGGBB","skyItems":["sun"],"props":[["piece",x0to1,dy,scale,"#RRGGBB or null","motion"]],"extras":[["extra",x0to1,dy,scale]]}\n'
            "Put the pieces mostly near the edges (x<0.25 or x>0.75); the middle belongs to the characters. 4 to 10 props."
            % (subject, lesson_title, "، ".join(concept_names[:8]), ", ".join(PIECES), ", ".join(EXTRAS), ", ".join(MOTIONS), ", ".join(FARS[1:]), ", ".join(SKY_ITEMS)))


def ask_model(llm, subject: str, lesson_title: str, concept_names: list):
    """ONE call for a new subject without a fitting place → a checked recipe saved in the library (or None). Needs a model (keys)."""
    if llm is None:
        return None
    try:
        raw = llm("You answer with one JSON object only.", prompt(subject, lesson_title, concept_names))   # the same model door as lego.py
        m = re.search(r"\{.*\}", raw or "", re.S)
        r = json.loads(m.group(0)) if m else None
    except Exception:                                                    # a model that fails never breaks the explanation
        return None
    return r if r and add(r) else None
