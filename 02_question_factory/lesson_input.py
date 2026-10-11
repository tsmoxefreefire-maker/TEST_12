# -*- coding: utf-8 -*-
"""🆕 batch 46 · THE TEAM'S NEW INPUT: a LESSON GRAPH (JSON) + the LESSON'S TEXT (the book's pages, OCR).
The engineer: «شغلك لازم يستقبل الجراف (الجيسون) ويستقبل التكست اللي هو شرح الدرس، والـ LLM هو اللي بينسّق».
The plan (AI Tutor spec): the Learning Graph = what to learn · RAG = the trusted content · the LLM decides HOW to explain, it is NOT the
source of truth and does NOT draw (the renderer draws) · never invent what the content does not say · every objective has subject + grade.

This file (NO model):
  · is_lesson_graph()   → is it the new shape?  {"lesson": {...}, "entities": [...], "relationships": [...], "external_relationships": [...]}
  · to_book_graph()     → one lesson (or several) in the new shape → OUR book graph (book · unit · topic · lesson · entity nodes,
                          subsetOf + prerequisiteOf relationships, node_content), so the whole factory works on it unchanged.
                          An entity of another lesson (external_relationships) comes in as a guest ONLY if its lesson is in the same request.
  · subject_grade()     → subject and grade: given by the caller, else guessed from the book's file name («MA.01…» = maths, grade 1).
  · cut_lesson_text()   → the lesson's own part of the pages (the OCR file has the pages before it too: the unit test, the unit project…),
                          without page numbers, OCR notes, lone exercise numbers and the vowel marks.
lesson_organizer.py (the MODEL) turns that text into each concept's explanation, examples and the book's problem, checked against the text."""
import hashlib
import re

# the book's file name code → (subject as the factory knows it, its Arabic name)
SUBJECT_CODES = {"MA": ("Mathematics", "الرياضيات"), "SC": ("Science", "العلوم"), "AR": ("Arabic language", "اللغة العربية"),
                 "EN": ("English language", "اللغة الإنجليزية"), "PH": ("Physics", "الفيزياء"), "CH": ("Chemistry", "الكيمياء"),
                 "BI": ("Biology", "الأحياء"), "HI": ("History", "التاريخ"), "GE": ("Geography", "الجغرافيا"),
                 "IS": ("Islamic education", "التربية الإسلامية"), "SS": ("Social studies", "الدراسات الاجتماعية"),
                 "CS": ("Computer science", "الحاسوب"), "DS": ("Digital skills", "المهارات الرقمية")}
GRADE_AR = ["", "الأول", "الثاني", "الثالث", "الرابع", "الخامس", "السادس", "السابع", "الثامن", "التاسع", "العاشر", "الحادي عشر", "الثاني عشر"]
_TASHKEEL = re.compile("[ؐ-ًؚ-ٰٟۖ-ۭ]")


def is_lesson_graph(g) -> bool:
    """the new shape: one lesson {"lesson", "entities"} — or a list of them"""
    if isinstance(g, list):
        return bool(g) and all(is_lesson_graph(x) for x in g)
    return isinstance(g, dict) and isinstance(g.get("entities"), list) and isinstance(g.get("lesson"), dict) and "nodes" not in g


def subject_grade(lessons: list, subject=None, grade=None):
    """(subject, grade, how) — the caller's values win; else the book's file name («MA.01.ST.BOOK…»); else unknown"""
    how = "given"
    if not subject or not grade:
        name = next((str((x.get("metadata") or {}).get("source_file_name") or "") for x in lessons
                     if (x.get("metadata") or {}).get("source_file_name")), "")
        m = re.match(r"\s*([A-Za-z]{2})[._-](\d{1,2})\b", name)
        if m:
            code = m.group(1).upper()
            subject = subject or (SUBJECT_CODES.get(code, (None,))[0])
            grade = grade or int(m.group(2))
            how = "file name"
        else:
            how = "unknown"
    try:
        grade = int(grade) if grade else None
    except (TypeError, ValueError):
        grade = None
    return subject or "", grade, how


def _safe(x) -> str:
    return re.sub(r"[^A-Za-z0-9_-]", "_", str(x))


def short_name(text: str) -> str:
    """the character's name without the word «مفهوم» (the model gives a better short name when it runs)"""
    t = re.sub(r"^\s*(مفهوم|مفاهيم)\s+", "", str(text or "")).strip()
    return t or str(text or "")


def book_id_for(lessons, subject=None, grade=None) -> str:
    """ONE id per book (subject + grade + the book's file): lessons sent one by one all go into the same book"""
    lessons = lessons if isinstance(lessons, list) else [lessons]
    subject, grade, _ = subject_grade(lessons, subject, grade)
    code = next((c for c, v in SUBJECT_CODES.items() if v[0] == subject), None)
    src = next((str((x.get("metadata") or {}).get("source_file_name") or "") for x in lessons if (x.get("metadata") or {}).get("source_file_name")), "")
    bid = (f"{code.lower()}_g{grade}" if code and grade else "book_" + hashlib.sha1((src or str(subject)).encode("utf-8")).hexdigest()[:8])
    return bid + ("_" + hashlib.sha1(src.encode("utf-8")).hexdigest()[:4] if src else "")


def to_book_graph(lessons, subject=None, grade=None, book_title=None, content=None) -> dict:
    """The new lesson graph(s) → our book graph. content = {entity_id: {"name": short name, "text": the description to use}} (from
    lesson_organizer); without it each entity keeps the team's description."""
    lessons = lessons if isinstance(lessons, list) else [lessons]
    content = content or {}
    subject, grade, _ = subject_grade(lessons, subject, grade)
    code = next((c for c, v in SUBJECT_CODES.items() if v[0] == subject), None)
    ar_subject = SUBJECT_CODES[code][1] if code else (subject or "الكتاب")
    book_id = book_id_for(lessons, subject, grade)              # (two books of the same subject and grade never mix: the file is in the id)
    title = book_title or (f"{ar_subject} · الصف {GRADE_AR[grade]}" if grade and grade < len(GRADE_AR) else ar_subject)
    nodes = [{"id": book_id, "title": title, "level": "book"}]
    rels, contents, seen = [], [], {book_id}
    in_request = {}                                              # entity id → it is in one of the lessons we got
    for L in lessons:
        for e in L.get("entities", []):
            in_request[str(e.get("id"))] = True

    def node(nid, title_, level):
        if nid not in seen:
            seen.add(nid)
            nodes.append({"id": nid, "title": title_, "level": level})

    def rel(s, t, kind):
        r = {"source_node_id": s, "target_node_id": t, "type": kind}
        if r not in rels:
            rels.append(r)
    for L in lessons:
        info = L["lesson"]
        uid, tid, lid = "u_" + _safe(info.get("unit_id", "1")), "t_" + _safe(info.get("topic_id", info.get("unit_id", "1"))), "l_" + _safe(info.get("lesson_id"))
        node(uid, str(info.get("unit_title") or "الوحدة"), "unit")
        node(tid, str(info.get("topic_title") or info.get("unit_title") or "الموضوع"), "topic")
        node(lid, str(info.get("lesson_title") or lid), "lesson")
        rel(uid, book_id, "subsetOf"); rel(tid, uid, "subsetOf"); rel(lid, tid, "subsetOf")
        for e in L.get("entities", []):
            eid = str(e.get("id"))
            c = content.get(eid) or {}
            node(eid, c.get("name") or short_name(e.get("text") or eid), "entity")
            rel(eid, lid, "subsetOf")
            desc = c.get("text") or e.get("description") or (e.get("metadata") or {}).get("description") or ""
            if desc:
                contents.append({"node_id": eid, "content_type": "text", "content_text": desc, "content_url": None})
        for r in L.get("relationships", []) + L.get("external_relationships", []):
            s, t, kind = str(r.get("source")), str(r.get("target")), r.get("type")
            if kind == "prerequisiteOf" and in_request.get(s) and in_request.get(t) and s != t:
                rel(s, t, "prerequisiteOf")                       # [a, b]: b needs a — a guest of another lesson only if it is here too
    return {"book": {"id": book_id, "title": title, "subject": subject, "grade": grade},
            "nodes": nodes, "relationships": rels, "node_content": contents}


def _norm(s: str) -> str:
    return _TASHKEEL.sub("", str(s or "")).replace("أ", "ا").replace("إ", "ا").replace("آ", "ا").strip()


def cut_lesson_text(text: str, lesson_title: str = "") -> str:
    """The lesson's own pages: from its heading («# العشرات» followed by «الدرس …») to the next unit / lesson heading;
    without OCR notes, page numbers, lone exercise numbers and vowel marks. No heading found → the whole text, cleaned."""
    lines = str(text or "").replace("\r", "").split("\n")
    title = _norm(lesson_title)
    start = None
    if title:
        for i, ln in enumerate(lines):
            if ln.lstrip().startswith("#") and _norm(ln.lstrip("# ")) == title:
                near = " ".join(_norm(x) for x in lines[i + 1:i + 4])
                if "الدرس" in near or start is None:
                    start = i                                    # the LAST heading of the title that is a lesson start wins
    if start is None:
        start = 0
    end = len(lines)
    for j in range(start + 1, len(lines)):
        s = lines[j].strip()
        if re.match(r"^#\s+", s) and (_norm(s.lstrip("# ")).startswith("الوحدة") or re.search(r"الدرس\s*\d", _norm(" ".join(lines[j:j + 2])))):
            if _norm(s.lstrip("# ")) != title:
                end = j
                break
    out = []
    for ln in lines[start:end]:
        s = re.sub(r"<!--.*?-->", "", ln).strip()
        s = _TASHKEEL.sub("", s)
        if not s or re.fullmatch(r"[\s.\-–:•*+=]*\d{0,3}[\s.\-–:•*+=]*", s):   # empty, a page number or a lone exercise number
            continue                                             # (a line of SEVERAL numbers stays: «10 50 20 90 40» is the lesson)
        if re.fullmatch(r"\.{3,}", s):
            continue
        out.append(s)
    return "\n".join(out).strip()
