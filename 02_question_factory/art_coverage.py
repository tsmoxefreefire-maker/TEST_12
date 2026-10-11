"""🆕 batch 40 (Hareth: «المكتبة لازم نوسّعها… تغطي كل الدروس وكل المواد من الصغار للثانوي» + «إحنا بنركّز على المنهج السعودي»
+ «مفهوم إله رسمة خلص… ليش ننشئ مليون رسمة؟»)
THE COVERAGE METER: for every concept of a curriculum, which picture would it get?
  · own   = a drawing of its own (the page's drawings, or the growing library art_library.py);
  · lego  = a drawing built from parts (lego.py, saved once);
  · subject = only the subject's character with its name on it (it works, but it is not a picture of the concept).
The curriculum = the Saudi books (curriculum/saudi/*.json: subjects, grades, units, lessons, concepts; Islamic studies are NOT in it),
or any graph JSON. Each concept is counted ONCE per subject (the same concept in many grades = one drawing).
    python art_coverage.py                      # the table: own / lego / subject, per subject and stage
    python art_coverage.py --missing 40         # + the 40 words that would cover the most concepts still without a picture
    python art_coverage.py --json out.json      # the same, as data (for the page / the engineers)"""
import collections
import glob
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import offline_generator as og  # noqa: E402

SAUDI = os.path.join(HERE, "curriculum", "saudi")
# the subject as the factory understands it (its words, its fallback character)
SUBJECT_OF = {"science": "science", "math": "math", "language": "arabic", "english": "english", "digital": "computer", "thinking": "thinking",
              "finance": "finance", "life": "life skills", "social": "social studies", "physics": "physics", "chemistry": "chemistry",
              "biology": "biology", "earth": "earth science", "environment": "environment"}
NAME_AR = {"science": "العلوم", "math": "الرياضيات", "language": "لغتي", "english": "الإنجليزي", "digital": "المهارات الرقمية", "thinking": "التفكير الناقد",
           "finance": "المعرفة المالية", "life": "المهارات الحياتية", "social": "الدراسات الاجتماعية", "physics": "الفيزياء", "chemistry": "الكيمياء",
           "biology": "الأحياء", "earth": "علوم الأرض والفضاء", "environment": "علم البيئة"}
# lessons that only teach HOW to solve (no thing to draw): they are not counted
SKIP_LESSON = re.compile(r"(خطة|مهارة|استراتيجية|استقصاء) حل المسألة|اختبار|مراجعة|دليل الدراسة|هيا بنا")
SKIP_CONCEPT = {"الاستماع", "الفهم القرائي", "النص الشعري", "التحدث", "الكتابة", "القراءة", "المشروع"}


def stage(grade):
    g = int(grade or 0)
    return "kids" if g <= 4 else "junior" if g <= 7 else "teen" if g <= 9 else "senior"


def saudi_concepts(folder=SAUDI):
    """[(subject_key, grade, concept name)] from the Saudi books (each book / grade / term / unit / lesson)."""
    out = []
    for f in sorted(glob.glob(os.path.join(folder, "*.json"))):
        with open(f, encoding="utf-8") as fh:
            d = json.load(fh)
        for e in d.get("grades") or d.get("books") or []:
            sk = e.get("subject_key") or d.get("subject_key")
            for u in e.get("units", []):
                for les in u.get("lessons", []):
                    if SKIP_LESSON.search(str(les.get("lesson", ""))):
                        continue
                    for c in les.get("concepts", []):
                        name = (c.get("ar") if isinstance(c, dict) else c) or ""
                        name = " ".join(str(name).split())
                        if name and name not in SKIP_CONCEPT:
                            out.append((sk, e.get("grade"), name))
    return out


def kind_of(icon):
    if icon.startswith("subj:"):
        return "subject"
    if icon.startswith("lego:"):
        return "lego"
    return "own"


def measure(items):
    """{subject: {"stage": {...}, "own": n, "lego": n, "subject": n, "names": {name: icon}}} — each name once per subject."""
    res = {}
    for sk, grade, name in items:
        r = res.setdefault(sk, {"own": 0, "lego": 0, "subject": 0, "names": {}, "stages": collections.Counter()})
        if name in r["names"]:
            continue
        icon = og.icon_for(name, "", SUBJECT_OF.get(sk, sk))
        r["names"][name] = icon
        r[kind_of(icon)] += 1
        r["stages"][stage(grade)] += 1
    return res


def missing_words(res, top=40):
    """The words (without «ال») that appear in the most concepts still without a picture → what to draw first."""
    cnt, ex = collections.Counter(), {}
    for sk, r in res.items():
        for name, icon in r["names"].items():
            if kind_of(icon) != "subject":
                continue
            for w in set(og._tokens(name)):
                if len(w) < 3 or w.startswith("ال"):
                    continue
                cnt[w] += 1
                ex.setdefault(w, []).append(name)
    return [(w, n, ex[w][:3]) for w, n in cnt.most_common(top)]


def table(res):
    lines = [f"{'المادة':<22} {'مفاهيم':>7} {'رسمة إلها':>10} {'ليغو':>6} {'شخصية المادة':>13}"]
    tot = collections.Counter()
    for sk in sorted(res, key=lambda k: -len(res[k]["names"])):
        r = res[sk]
        n = len(r["names"])
        tot["n"] += n
        for k in ("own", "lego", "subject"):
            tot[k] += r[k]
        lines.append(f"{NAME_AR.get(sk, sk):<22} {n:>7} {100 * r['own'] / n:>9.0f}% {100 * r['lego'] / n:>5.0f}% {100 * r['subject'] / n:>12.0f}%")
    n = tot["n"] or 1
    lines.append(f"{'الكل':<22} {tot['n']:>7} {100 * tot['own'] / n:>9.0f}% {100 * tot['lego'] / n:>5.0f}% {100 * tot['subject'] / n:>12.0f}%")
    return "\n".join(lines), {k: round(100 * tot[k] / n, 1) for k in ("own", "lego", "subject")}, tot["n"]


def main(argv):
    res = measure(saudi_concepts())
    text, pct, n = table(res)
    print(text)
    if "--missing" in argv:
        top = int(argv[argv.index("--missing") + 1])
        print("\nأكثر كلمات بلا رسمة (الكلمة · كم مفهوم · أمثلة):")
        for w, k, ex in missing_words(res, top):
            print(f"  {w:<14} {k:>4}  {' | '.join(ex)}")
    if "--json" in argv:
        out = argv[argv.index("--json") + 1]
        with open(out, "w", encoding="utf-8") as fh:
            json.dump({"total": n, "percent": pct, "subjects": {sk: {k: r[k] for k in ("own", "lego", "subject")} | {"concepts": len(r["names"])}
                                                                for sk, r in res.items()}}, fh, ensure_ascii=False, indent=1)
    return pct


if __name__ == "__main__":
    main(sys.argv[1:])
