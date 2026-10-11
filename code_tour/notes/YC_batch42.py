# -*- coding: utf-8 -*-
"""🆕 batch 42 (the engineer's idea + Hareth's notes): the DATABASE (keep everything · find any scene by a question), «ask a question →
the scene at once», an optional meaning model, and LESS REPETITION (the same fact in other words · the same game in other looks ·
three new ways to show a lesson's parts).
Loaded after YB_batch41 (sorted: «YB» < «YC» < «Y_»). Y_batch31.py builds narrator.js and main.py again, so it calls finish() at its end."""
import copy
import importlib.util
import os

_HERE = os.path.dirname(os.path.abspath(__file__))
_ME = os.path.basename(__file__)


def _now():
    out = {}
    for fn in sorted(os.listdir(_HERE)):
        if fn.endswith(".py") and not fn.startswith("_") and fn < _ME:
            spec = importlib.util.spec_from_file_location("nC_" + fn[:-3], os.path.join(_HERE, fn))
            m = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(m)
            out.update(m.FILES)
    return out


_C = _now()


def _card(p):
    return copy.deepcopy(_C[p])


def _add(c, line):
    if len(c["how"]) < 9:
        c["how"].append(line)
    else:
        c["how"][-1] += " · " + line


FILES = {}
_ENG = "💡 المهندس: «الـ SVG يبقى created offline قبل ما نطلع production… similarity measure… الجيسون في كولم والديسكريبشن بتاعه في كولم». (مين بيبعت السؤال ما حكاه: الأقرب المدرس الذكي)"
_REP = "💡 حارث: «المشاهد بتتكرر من درس لدرس» → نفس المعلومة، بطريقة ثانية."

# ======================================================================= the server (05)
FILES["05_explanation_api/core/db.py"] = {
    "title": "الداتابيس: الحفظ والبحث (الدفعة ٤٢)",
    "one": "PostgreSQL واحدة من DATABASE_URL بتعمل شغلتين: نسخة من كل ملفات data/ (بترجع لما السيرفر يقوم بقرص فاضي)، وسطر لكل مشهد للبحث بالأسئلة.",
    "role": "service.py بينادي restore_files لما يقوم (boot) و save_files بعد كل تغيير (persist). scene_index.py بيقرأ ويكتب أسطر المشاهد من scenes(). بلا DATABASE_URL: ملفات بس.",
    "how": [
        _ENG + " + حارث: «السيرفر بيطفي والأشياء بتضيع» (Render المجاني بيمسح القرص).",
        "ie_files: مسار الملف (نسبة لـ data/) + محتواه + بصمته (sha). بنبعث بس اللي تغيّر (_MANIFEST بيتذكر البصمات)، واللي انمسح من القرص بينمسح منها.",
        "restore_files: لما السيرفر يقوم، كل ملف ناقص أو مختلف بالقرص بيرجع من الداتابيس (وما بيكتب برّا data/ أبداً).",
        "ie_scenes: سطر لكل مشهد: رقم الكتاب والدرس والمفهوم (من الجراف)، النوع، الاسم، المرحلة والصف، الأسئلة (jsonb)، الوصف، الـ JSON، النسخة، وأرقام المعنى (real[]) واسم موديلها.",
        "_PgScenes (الداتابيس) و _FileScenes (ملف data/scene_index.json) إلهم نفس الأوامر، و scenes() بتختار حسب DATABASE_URL.",
        "SQL عادي بلا إضافات، والمحرّك psycopg بيننادى بس لما في داتابيس. run بتعيد الاتصال مرة إذا انقطع، وبتعمل الجداول أول مرة.",
    ],
    "ideas": [["القرص كاش، والداتابيس هي الأصل", "المصنع بيضل يشتغل على ملفات (سريع وكوده ما تغيّر)، والداتابيس النسخة اللي ما بتضيع."],
              ["رابط الداتابيس سرّ", "فيه كلمة سر: بمتغيرات البيئة بس (Render)، و where() بتحكي «postgres» بس، مش الرابط."]],
    "tip": "جرّب محلياً: DATABASE_URL=postgresql://… وبعدين python scripts/build_scene_index.py --samples. وافتح /health: storage لازم تكون postgres.",
    "items": {
        "_MANIFEST": "مسار ← بصمة الملف اللي بالداتابيس (عشان نبعث بس المتغيّر).",
        "SCHEMA": "أوامر عمل الجدولين والفهارس (CREATE … IF NOT EXISTS: آمنة كل مرة).",
        "ROW": "أعمدة سطر المشهد بالترتيب (بلا الـ JSON والأرقام).",
        "url": "رابط الداتابيس من DATABASE_URL (أو فاضي).",
        "enabled": "في داتابيس؟",
        "where": "«postgres» أو «files» (للـ /health والصفحة، بلا الرابط).",
        "_connect": "بيفتح اتصال psycopg (autocommit).",
        "run": "أمر SQL واحد بقيمه (%s)، بإعادة اتصال مرة إذا انقطع، والجداول بتنعمل مع أول اتصال.",
        "close": "بيسكّر الاتصال (الفحص بيستعملها).",
        "_files": "كل ملفات data/ (بلا المؤقتة) بمسار نسبي.",
        "_pack": "محتوى الملف ← نص (والملف اللي مش نص ← base64).",
        "_unpack": "العكس: النص ← محتوى الملف.",
        "_sha": "بصمة ملف (sha1).",
        "restore_files": "الداتابيس ← القرص: كل ملف ناقص أو مختلف بيرجع. بترجّع كم ملف.",
        "save_files": "القرص ← الداتابيس: الجديد والمتغيّر بيروح، والممسوح بينمسح. بترجّع {saved, removed}.",
        "_PgScenes": "أسطر المشاهد بالداتابيس (جدول ie_scenes).",
        "_PgScenes.versions": "لكل سطر بكتاب: نسخته واسم موديل أرقامه (عشان نعرف شو تغيّر).",
        "_PgScenes.upsert": "بيكتب سطر (أو بيحدّثه) وبيمسح أرقامه القديمة (الوصف تغيّر).",
        "_PgScenes.upsert_many": "كذا سطر.",
        "_PgScenes.set_embs": "أرقام المعنى لكذا سطر.",
        "_PgScenes.delete": "بيمسح أسطر بأرقامها.",
        "_PgScenes.delete_book": "بيمسح أسطر كتاب كامل.",
        "_PgScenes.set_emb": "أرقام المعنى لسطر واحد (real[]) واسم الموديل.",
        "_PgScenes.all_rows": "كل الأسطر بلا الـ JSON (للبحث بالذاكرة).",
        "_PgScenes.scenes": "الـ JSON لكم سطر بأمر واحد (للجواب).",
        "_PgScenes.stamp": "عدد الأسطر وآخر تعديل: إذا تغيّر، البحث بيرجع يحمّل.",
        "_FileScenes": "نفس الإشي بملف data/scene_index.json (بلا داتابيس).",
        "_FileScenes._path": "مسار الملف.",
        "_FileScenes._load": "بيقرأ الملف مرة لحد ما يتغيّر (_memo).",
        "_FileScenes._save": "بيكتب الملف (عبر ملف مؤقت، فما بينكسر) وبيحدّث الـ _memo.",
        "_FileScenes.versions": "زي _PgScenes.versions.",
        "_FileScenes.upsert": "سطر واحد.",
        "_FileScenes.upsert_many": "كذا سطر بكتابة وحدة للملف (كتابة لكل سطر كانت بطيئة: ١٢ كتاب بدقيقة).",
        "_FileScenes.set_embs": "أرقام كذا سطر بكتابة وحدة.",
        "_FileScenes.delete": "بيمسح أسطر.",
        "_FileScenes.delete_book": "بيمسح كتاب.",
        "_FileScenes.set_emb": "أرقام سطر واحد.",
        "_FileScenes.all_rows": "كل الأسطر بلا الـ JSON، مرتّبة.",
        "_FileScenes.scenes": "الـ JSON لكم سطر.",
        "_FileScenes.stamp": "مسار الملف ووقت تعديله.",
        "scenes": "وين أسطر المشاهد: الداتابيس إذا في، وإلا الملف.",
    },
}

FILES["05_explanation_api/core/embed.py"] = {
    "title": "موديل المعنى (اختياري، الدفعة ٤٢)",
    "one": "نص ← أرقام؛ النصين اللي معناهم واحد أرقامهم قريبة، حتى بلا ولا كلمة مشتركة. Gemini أو OpenAI أو وهمي للفحص.",
    "role": "scene_index.py بيستعمله: embed للأوصاف (مرة وحدة لكل سطر) و query لسؤال الطالب. المفاتيح من llm_gateway.read_settings (متغيرات البيئة أو api_key.txt).",
    "how": [
        "💡 حارث: «الـ AI حطه، وأنا بعدين بحط المفتاح، وجرّبه على AI وهمي».",
        "provider: EMBED_PROVIDER إذا محدد (gemini / openai / fake / none)، وإلا أول مفتاح موجود (Gemini قبل OpenAI)، وإلا none.",
        "gemini-embedding-2 (طلب batchEmbedContents، والسؤال بيبلش بـ «task: search result | query:») · text-embedding-3-small (طلب embeddings مع dimensions). ٧٦٨ رقم، ومطبّعين (طولهم ١).",
        "الوهمي (_fake): نفس الكلمات ← نفس الأرقام. ما بيفهم معنى: بس بيثبت إنه كل الأسلاك شغّالة.",
        "query بتتذكر السؤال (_CACHE): نفس السؤال ثاني مرة ← ولا طلب. CALLS بتعدّ الطلبات (للفحص).",
        "⚠️ الموديل الحقيقي ما انجرّب هون (ما في مفتاح ولا نت): الفحص بيتأكد من شكل الطلب وقراءة الجواب حسب التوثيق.",
    ],
    "tip": "حطيت مفتاح؟ اعمل POST /search/reindex مرة وحدة (بيعطي أرقام بس للأسطر اللي ما إلها)، وجرّب أسئلة حقيقية، وعدّل MIN_SCORE إذا لزم.",
    "items": {
        "DIM": "عدد الأرقام لكل نص (٧٦٨).",
        "MODELS": "اسم موديل كل مزوّد (بيتغيّر بمتغير بيئة إذا تغيّرت الأسماء).",
        "MIN_SCORE": "أقل تشابه مقبول لكل مزوّد (تحته = «مش قريب كفاية»).",
        "_CACHE": "سؤال ← أرقامه (عشان السؤال المكرر ببلاش).",
        "CALLS": "كم طلب بعثنا للموديل (الفحص بيتأكد إنه ما في طلب زيادة).",
        "_keys": "المفاتيح من نفس مكان باقي المشروع.",
        "provider": "مين بيعمل الأرقام هلأ.",
        "model_name": "اسم كامل للموديل (بينحفظ مع كل سطر: موديل جديد ← أرقام جديدة).",
        "_unit": "بيخلّي طول الأرقام ١ (فالتشابه = ضرب بسيط).",
        "_fake": "الموديل الوهمي من كلمات النص.",
        "_post": "طلب HTTP بـ JSON (المكتبة العادية بس).",
        "_gemini": "طلب Gemini لكذا نص وقراءة الجواب.",
        "_openai": "طلب OpenAI لكذا نص وقراءة الجواب بالترتيب.",
        "embed": "نصوص ← أرقامها (٦٤ نص بكل طلب)، أو None إذا ما في مزوّد.",
        "query": "أرقام سؤال واحد (متذكّرة).",
        "min_score": "أقل تشابه للمزوّد الحالي.",
    },
}

FILES["05_explanation_api/core/scene_index.py"] = {
    "title": "اسأل سؤال ← المشهد فوراً (الدفعة ٤٢)",
    "one": "قبل: كل مشهد بيصير سطر (أسئلته ووصفه). لما ينسأل سؤال (المدرس الذكي أو صفحة التجربة): الاسم، بعدين المعنى، بعدين الحروف ← مشاهد المفهوم + أحسن مشهد + رابط بيفتح الصفحة عنده.",
    "role": "service.generate بينادي index_book بعد كل كتاب، و service.ask بينادي ask. الأسطر بـ db.scenes()، والأسئلة من scene_questions.py، والمعنى من embed.py.",
    "how": [
        _ENG,
        "index_book: لكل مشهد بالكتاب (الصورة الكبيرة ومشهد الأجزاء ومشاهد كل مفهوم، ومشاهد الموديل اللي وافق عليها المعلم) سطر؛ بنكتب بس اللي نسخته تغيّرت، وبنعطي أرقام معنى بس للي ما إله.",
        "_load: الأسطر بالذاكرة مع حروفها الثلاثية (محتوى، وأسئلة كل مشهد)، وأسماء المفاهيم، ومصفوفة الأرقام (numpy). بترجع تحمّل بس لما الجدول أو الموديل يتغيّر.",
        "١ الاسم (_by_name): أسماء المفاهيم اللي جوا السؤال (الاسم الأطول بيربح، ونص اسم طويل بيدخل بخصم). ٢ المعنى (_by_meaning) إذا في موديل، وبيربح على الاسم بس إذا واضح إنه بيأشّر لمفهوم ثاني. ٣ الحروف (_by_text).",
        "_pick_scene: جوا المفهوم، المشهد اللي أسئلته أقرب لسؤاله (شو / ليش / كيف / الفرق)، ولما يذكر مفهومين ونيته مقارنة: مشهد فيه الاثنين، والمفهوم اللي ذكره أول بياخد ميزة.",
        "_allowed: بكتابه بس إذا معروف، وبصفّه (± صف). بعيد عن كل إشي ← found=false + اقتراحات.",
        "الكتاب اللي ما إله أسطر (داتابيس جديدة) بيتعمله أسطر فوراً وبينحفظ.",
        "الدقة على ٤٦ سؤال تجربة: ٤٣ صح بلا موديل؛ الـ٣ الباقيين ما فيهم كلمة من الاسم (شغل موديل المعنى).",
    ],
    "ideas": [["الوصف = أسئلة", "الطالب بيسأل سؤال مش اسم، فكل مشهد بيحمل الأسئلة اللي بيجاوبها: سؤاله بيقرب منها أكثر."],
              ["ولا مشهد غلط", "إذا مش قريب كفاية، أحسن «ما في مشهد» + اقتراحات من إنه نعرض إشي غلط."]],
    "tip": "بدك تفهم ليش طلع مشهد؟ شوف how و score و matched_question بالجواب.",
    "items": {
        "TEXT_MIN": "أقل تشابه بالحروف مقبول.",
        "_C": "الأسطر بالذاكرة: الأسطر، حروف المحتوى، حروف الأسئلة، الأسماء، مصفوفة الأرقام وأرقام أسطرها، والموديل.",
        "_graph": "جراف الكتاب المحفوظ.",
        "_ver": "نسخة سطر: نسخة الأسئلة + بصمة المشهد وأسئلته.",
        "rows_for_book": "كل (سطر، مشهد) بالكتاب.",
        "_approved_llm": "مشاهد الموديل اللي وافق عليها المعلم بالدرس (اختياري).",
        "_int": "رقم أو None.",
        "index_book": "أسطر كتاب: بيمسح القديم اللي راح، بيكتب المتغيّر، بيعطي أرقام للي ناقصه.",
        "index_all": "كل الكتب.",
        "drop_book": "بيمسح أسطر كتاب.",
        "_load": "بيحمّل الأسطر للذاكرة (لما الجدول أو الموديل يتغيّر بس).",
        "_allowed": "هل السطر مسموح لهالطالب (كتابه، صفّه، مرحلته).",
        "_by_name": "المفاهيم اللي اسمها جوا السؤال (كامل، أو نصّه بخصم) ← أسطرها.",
        "_qscore": "قديش سؤاله قريب من أقرب سؤال من أسئلة المشهد.",
        "_pick_scene": "أحسن مشهد بين أسطر (النية، المفهومين، اللي ذكره أول، الاسم الأطول، الكرتون أول).",
        "_by_meaning": "الأقرب بالمعنى (ضرب مصفوفة).",
        "_by_text": "الأقرب بحروف الكلمات اللي بتسمّي أشياء (+ نص اسم طويل).",
        "ask": "السؤال ← الجواب كامل (أو found=false + اقتراحات) والوقت بالملّي ثانية.",
        "_page_url": "رابط الصفحة عند المشهد: /explain/<كتاب>?lesson=…&concept=…&at=…&kind=…",
        "_closest_question": "أقرب سؤال من أسئلة المشهد لسؤاله (بيطلع بالجواب).",
        "status": "وين محفوظ، كم سطر وكتاب، الموديل، كم سطر إله أرقام.",
    },
}

FILES["05_explanation_api/scripts/build_scene_index.py"] = {
    "title": "التوليد قبل ما الطلاب ييجوا (الدفعة ٤٢)",
    "one": "بيعمل أسطر البحث لكل الكتب (أو جراف جديد أو الكتب الـ١٢)، ولو بدك بيجرّب سؤال.",
    "role": "بيستعمل service.boot و generate و seed_samples و reindex و ask. بيحفظ بالداتابيس إذا DATABASE_URL موجود.",
    "how": [_ENG,
            "--graph كتاب.json: الشرح أول وبعدين الأسطر · --samples: الكتب الـ١٢ · --book: كتاب واحد · --ask «سؤال»: جرّب.",
            "بيطبع لكل كتاب: كم سطر، كم انكتب، كم أخذ أرقام معنى، وبكم ملّي ثانية."],
    "tip": "python scripts/build_scene_index.py --samples --ask \"شو بيحتاج التلقيح؟\"",
    "items": {"main": "بيقرأ الخيارات وبيعمل الشغل وبيطبع النتيجة."},
}

FILES["05_explanation_api/static/ask.html"] = {
    "title": "صفحة «اسأل سؤال» (الدفعة ٤٢)",
    "one": "خانة سؤال ← المفهوم وكيف انلقى ومشاهده، والصفحة التفاعلية بتفتح تحتها عند المشهد اللي بيجاوب.",
    "role": "GET /ask بيرجّعها. بتنادي POST /ask و GET /books و GET /search/status، والإطار بيفتح page_url.",
    "how": [_ENG, "فوق: وين محفوظ (داتابيس ولا ملفات) وكم مشهد وموديل المعنى.",
            "السؤال + الكتاب والصف (اختياري) + أسئلة أمثلة.",
            "الجواب: الاسم، الدرس، «لقيته بالاسم / بالمعنى / بالحروف»، الوقت، أقرب سؤال، مشاهد المفهوم والمضوّي اللي بيجاوب، وإطار الصفحة.",
            "ما في قريب: «ما في مشهد» + اقتراحات بتنكبس."],
    "tip": "HTML و JS عادي بلا مكتبات، بألوان فاتحة وغامقة.",
}

_S = _card("05_explanation_api/core/service.py")
_add(_S, "🆕 الدفعة ٤٢: generate بيعمل أسطر البحث للكتاب (_index) وبيحفظ بالداتابيس (persist) · boot بيرجّع الملفات من الداتابيس لما السيرفر يقوم · ask و search_status و reindex و ask_html لـ «اسأل سؤال» · delete_book بيمسح الأسطر · place_library صار بـ data/ (فبينحفظ كمان).")
_S["items"].update({
    "_index": "🆕 الدفعة ٤٢: أسطر البحث لكتاب، والخطأ ما بيوقف عمل الكتاب (بيصير تحذير).",
    "persist": "🆕 الدفعة ٤٢: بعد أي تغيير: (أسطر الكتاب إذا انعطى) وكل ملف تغيّر ← الداتابيس. الداتابيس واقعة؟ تحذير، والتغيير بيطلع المرة الجاية.",
    "boot": "🆕 الدفعة ٤٢: السيرفر قام: الملفات من الداتابيس ← القرص.",
    "ask": "🆕 الدفعة ٤٢: سؤال الطالب ← scene_index.ask (كتاب مش موجود 404، سؤال فاضي 400).",
    "search_status": "🆕 الدفعة ٤٢: حالة البحث.",
    "reindex": "🆕 الدفعة ٤٢: أسطر كتاب أو كل الكتب من جديد (بس المتغيّر) وحفظ.",
    "ask_html": "🆕 الدفعة ٤٢: صفحة static/ask.html.",
})
FILES["05_explanation_api/core/service.py"] = _S

_R = _card("05_explanation_api/api/routes.py")
_add(_R, "🆕 الدفعة ٤٢: GET/POST /ask · GET /search/status · POST /search/reindex · /health فيها storage · وكل طلب بيغيّر إشي (الليغو، مشاهد الموديل) بيمر بـ _write فبينحفظ بالداتابيس.")
_R["items"].update({
    "_write": "🆕 الدفعة ٤٢: نفس _call، وبعدها service.persist (الداتابيس).",
    "ask_page": "🆕 الدفعة ٤٢: صفحة «اسأل سؤال».",
    "ask": "🆕 الدفعة ٤٢: POST /ask: السؤال ← الجواب.",
    "search_status": "🆕 الدفعة ٤٢: GET /search/status.",
    "search_reindex": "🆕 الدفعة ٤٢: POST /search/reindex (كتاب أو الكل).",
})
_R["items"]["health"] = (_R["items"].get("health") or "السيرفر شغّال؟") + " 🆕 الدفعة ٤٢: + storage (postgres / files)."
FILES["05_explanation_api/api/routes.py"] = _R

_SC = _card("05_explanation_api/api/schemas.py")
_add(_SC, "🆕 الدفعة ٤٢: AskRequest (السؤال + الكتاب والصف والمرحلة اختياري) · GenerateResponse.search (كم سطر بحث) · Health.storage.")
_SC["items"]["AskRequest"] = "🆕 الدفعة ٤٢: شكل طلب POST /ask."
FILES["05_explanation_api/api/schemas.py"] = _SC

_CT = _card("05_explanation_api/core/contract.py")
_add(_CT, "🆕 الدفعة ٤٢: build_up و missing و tour بالعقد، وحقل assemble بالدرس صار «مشهد أجزاء الدرس» ونوعه بيتبدّل.")
FILES["05_explanation_api/core/contract.py"] = _CT

FILES["05_explanation_api/tests/test_batch42.py"] = {
    "title": "فحص الدفعة ٤٢ (السيرفر)",
    "one": "بيفحص اسأل سؤال (٢٣ سؤال)، موديل المعنى (الوهمي وشكل طلبات الحقيقي)، الداتابيس الحقيقية (الحفظ والرجوع)، والطلبات.",
    "role": "بيفحص core/scene_index.py و db.py و embed.py و service.py والطلبات. PYTHONPATH=tests/local_stub_only_for_sandbox TEST_DATABASE_URL=… python -m unittest tests.test_batch42",
    "how": [
        "Ask: كل مشهد إله سطر · الوصف أسئلة عامية وفصحى · الأسئلة بتلاقي مفهومها الصح · البعيد ← لا · صفّه بس · أي مشهد جوا المفهوم · الرابط · أشكال الكلمات · السرعة · بس المتغيّر بينكتب · الكتاب الممسوح بيطلع.",
        "Meaning (الوهمي): كل سطر إله أرقام مرة وحدة · السؤال المكرر ببلاش · خطوة المعنى · طلب Gemini و OpenAI وقراءة جوابهم (جواب مزيّف) · بلا مفتاح ما بيخرب إشي.",
        "Database (بس مع TEST_DATABASE_URL): الأسطر والملفات بالداتابيس · إعادة تشغيل بقرص فاضي ما بتضيّع إشي (نفس الصفحة) · الكتاب الممسوح بيطلع منها · الداتابيس واقعة ما بتوقف الكتاب.",
        "API: POST /ask و GET /ask و /search/status و /health و /search/reindex.",
    ],
    "items": {
        "CASES": "الأسئلة (السؤال، الكتاب، الصف، المفهوم الصح أو None = لازم «ما في مشهد»).",
        "_use_dir": "بيحوّل مجلد الداتا لمجلد مؤقت (كأنه سيرفر جديد).",
        "_Base": "صف مشترك: مجلد مؤقت + الكتب الـ١٢ + مزوّد المعنى.",
        "_Base.setUpClass": "بيجهّز المجلد والكتب.",
        "_Base.tearDownClass": "بيرجّع كل إشي زي ما كان.",
        "Ask": "بلا داتابيس ولا موديل: الاسم والحروف بس.",
        "Ask.test_every_scene_of_every_book_can_be_found": "عدد الأسطر = عدد المشاهد.",
        "Ask.test_the_description_is_questions_in_dialect_and_fusha": "«شو هو» و«ما هو»، و«بدون» بـ «شو لو».",
        "Ask.test_the_right_scene_for_the_question": "كل الأسئلة بتلاقي المفهوم الصح (أو لا).",
        "Ask.test_far_questions_get_no_scene_and_suggestions": "«شو أكلة المنسف» ← لا + اقتراحات.",
        "Ask.test_his_grade_only": "الجين لصف ١٢ مش لصف ٤، والذرة بكتابه هو.",
        "Ask.test_which_scene_of_the_concept": "«شو لو» ← مشهد شو لو، «شو هو» ← الكرتون، والكرتون أول.",
        "Ask.test_the_link_opens_the_page_there": "الرابط فيه الدرس والمفهوم والمكان والنوع.",
        "Ask.test_word_forms": "الجذور/الجذر، قارة/القارات، بنضرب/الضرب… والغلط ما بينقبل (المائدة مش الماء).",
        "Ask.test_fast": "الوسط أقل من ٥٠ ملّي ثانية.",
        "Ask.test_only_what_changed_is_written_again": "ولا سطر بينكتب ثاني، ونسخة أسئلة جديدة ← كل الأسطر.",
        "Ask.test_a_deleted_book_leaves_the_search": "كتاب انضاف وانمسح ← أسطره راحت.",
        "Meaning": "بالموديل الوهمي.",
        "Meaning.test_every_row_got_its_numbers_once": "كل سطر إله أرقام، والمرة الثانية ولا طلب.",
        "Meaning.test_a_question_asked_again_costs_nothing": "نفس السؤال ← ولا طلب.",
        "Meaning.test_the_meaning_step": "سؤال بلا اسم والمعنى بيأشّر لفيلم ← how = meaning والفيلم.",
        "Meaning.test_the_real_providers_requests": "شكل طلب Gemini و OpenAI وقراءة جوابهم (بلا نت).",
        "Meaning.test_no_key_no_meaning_and_nothing_breaks": "بلا مفتاح ← none، والبحث بالاسم شغّال.",
        "Database": "داتابيس PostgreSQL حقيقية.",
        "Database.setUpClass": "بيمسح الجداول، بيعمل كتابين، وبيحفظ بصمة الصفحة.",
        "Database.tearDownClass": "بيرجّع الإعدادات.",
        "Database.test_1_the_rows_and_the_files_are_in_the_database": "الأسطر بأرقامها والملفات بالداتابيس.",
        "Database.test_2_a_restart_with_an_empty_disk_loses_nothing": "قرص فاضي ← boot ← نفس الكتب ونفس الصفحة والسؤال شغّال.",
        "Database.test_3_a_deleted_book_leaves_the_database": "أسطره وملفاته راحوا.",
        "Database.test_4_the_database_down_never_stops_a_book": "داتابيس مش موجودة ← الكتاب بينعمل وفي تحذير.",
        "API": "الطلبات.",
        "API.setUpClass": "مجلد مؤقت + كتاب النباتات.",
        "API.tearDownClass": "بيرجّع الإعدادات.",
        "API.test_ask": "POST /ask: صح، فاضي 400، كتاب مش موجود 404.",
        "API.test_the_page_status_and_health": "الصفحة، الحالة، storage، وإعادة الأسطر ما بتكتب إشي جديد.",
    },
}

FILES["05_explanation_api/tests_browser/test_ask_page.py"] = {
    "title": "فحص صفحة «اسأل سؤال» بالمتصفح (الدفعة ٤٢)",
    "one": "سؤال ← المفهوم ومشاهده والصفحة بتفتح عند المشهد · سؤال بعيد ← لا + اقتراحات · كمبيوتر وتلفون.",
    "role": "بيفحص static/ask.html مع core/service.py الحقيقي (Playwright بيوجّه الطلبات للخدمة). python tests_browser/test_ask_page.py",
    "how": ["الحالة والكتب · «شو بيصير لو ما في التلقيح؟» ← التلقيح بالاسم، و«شو لو» مضوّي، والإطار مفتوح عند «اختفى».",
            "سؤال بعيد ← اقتراحات بتنكبس وبتلاقي · مثال + كتابه ← مشهد قارن · بلا سحب عالجنب."],
    "items": {"ok": "بيسجّل فحص.", "handle": "بيجاوب كل طلب من الخدمة نفسها (نفس اللي FastAPI بيناديه).",
              "frame_text": "سطر الراوي جوا إطار الصفحة."},
}

FILES["05_explanation_api/tests/local_stub_only_for_sandbox/psycopg/__init__.py"] = {
    "title": "نسخة تجريبية من psycopg (للفحص هون بس)",
    "one": "بتحكي مع PostgreSQL حقيقية محلية (بلا كلمة سر) عشان نفحص الداتابيس هون، لأنه ما بنقدر ننزّل psycopg. مش للإنتاج.",
    "role": "بس مع PYTHONPATH=tests/local_stub_only_for_sandbox (زي نسخة FastAPI التجريبية). بالسيرفر الحقيقي: psycopg من requirements.txt.",
    "how": ["بتعمل الاتصال ببروتوكول PostgreSQL (النسخة ٣، أوامر بسيطة) بدخول «trust».",
            "القيم (%s) بتنحط بالـ SQL كنصوص محمية بعلامات، و jsonb و real[] و bool بيرجعوا Python.",
            "الكود بيستعمل بس اللي بيشتركوا فيه: connect و execute و fetchall و fetchone و close."],
    "tip": "الكود الحقيقي (core/db.py) بيبعث الـ JSON والمصفوفات كنص مع cast بالـ SQL، فبيشتغل نفسه مع الاثنين.",
    "items": {"Error": "خطأ SQL.", "OperationalError": "خطأ اتصال.", "_lit": "قيمة Python ← نص SQL محمي.", "_fill": "بيحط القيم مكان %s (و %% = %).",
              "_arr": "مصفوفة Postgres ← قائمة.", "_CAST": "نوع العمود ← تحويله (رقم، bool، json، مصفوفة).", "Cursor": "نتيجة أمر.",
              "Cursor.__init__": "الأسطر وعددها.", "Cursor.fetchall": "كل الأسطر.", "Cursor.fetchone": "أول سطر أو None.",
              "Connection": "اتصال واحد.", "Connection.__init__": "بيفتح الاتصال وبيدخل.", "Connection._read": "بيقرأ عدد بايتات.",
              "Connection._msg": "رسالة وحدة من السيرفر.", "Connection._err": "نص الخطأ من رسالة السيرفر.", "Connection.execute": "أمر وحدة ← Cursor.",
              "Connection.close": "بيسكّر.", "Connection.__enter__": "with.", "Connection.__exit__": "بيسكّر بآخر with.", "connect": "اتصال جديد."},
}

_T = _card("05_explanation_api/tests_browser/test_server_page.py")
_add(_T, "🆕 الدفعة ٤٢: «كل آلة صوتها مختلف» بيضل على نفس النغمة (معدّل ٤)، وصفحة السيرفر صار فيها مشاهد الأجزاء الجديدة والأشكال.")
FILES["05_explanation_api/tests_browser/test_server_page.py"] = _T

# ======================================================================= the factory (02)
FILES["02_question_factory/scene_questions.py"] = {
    "title": "الأسئلة اللي بيجاوبها المشهد (الدفعة ٤٢)",
    "one": "لكل مشهد: الأسئلة اللي بيجاوبها بالعامية والفصحى + كلامه، عشان سؤال الطالب يلاقيه. وأدوات النص للبحث.",
    "role": "05_explanation_api/core/scene_index.py بيستعمله (الأسطر والبحث). بلا داتابيس وبلا AI.",
    "how": [
        _ENG,
        "questions: حسب النوع: تعرّف عليّ ← «شو هو X؟ ما هو X؟ شو بيحتاج؟ مين بيحتاجه؟» · فيلم ← «كيف بيصير؟» · شو لو ← «شو بيصير بدون؟» · قارن ← «الفرق بين؟» · سلاسل ← «كيف بنوصل؟» · أجزاء الدرس ← «شو أجزاء؟»…",
        "description: الأسئلة + معنى المفهوم + كلام المشهد (خطواته وفقرة ليش).",
        "norm: بلا تشكيل، ألف وحدة، ة ← ه، ى ← ي، بلا علامات وإيموجي. stem: بلا «ال» وأخواتها الطويلة.",
        "_same: الكلمة نفسها · + نهاية (نباتات/نبات، قارة/القارات) · جمع تكسير (الجذور/الجذر، البذور/البذرة) · فعل بالعامية (بنضرب/الضرب). والكلمات القصيرة ما بتنقارن هيك (المائدة مش الماء).",
        "trigrams: الحروف ثلاثة ثلاثة؛ content=True بلا كلمات السؤال (شو، ليش، كيف…) عشان نلاقي أي مفهوم، ومعها عشان نلاقي أي مشهد.",
        "VERSION: نسخة الأسئلة؛ لما تتغيّر كل الأسطر بتنعمل من جديد (وبتاخد أرقام معنى جديدة).",
    ],
    "tip": "سؤال ما بيلاقي مشهده؟ زيد صيغة بـ questions للنوع، وكبّر VERSION.",
    "items": {
        "VERSION": "نسخة الأسئلة.", "_MARKS": "التشكيل والتطويل.", "_PREFIXES": "وال، بال، فال، كال، لل، ال.", "ENDINGS": "النهايات (ات، ون، ين، ان، ية، يه، ه، ي).",
        "norm": "نص ← شكل موحّد للمقارنة.", "stem": "كلمة بلا «ال» وأخواتها.", "words": "كلمات النص بلا «ال».",
        "_cut": "كلمة بلا نهاية وحدة (إذا ضل ٣ حروف).", "_bare": "حروف الكلمة بلا نهاية وبلا حروف المد (لجمع التكسير).",
        "VERB": "بداية الفعل بالعامية (بن، بت، بي).", "_same": "هل كلمة السؤال هي كلمة الاسم (بأشكالها).",
        "name_at": "وين بيبلش الاسم بالسؤال (اللي بيذكره أول غالباً هو الموضوع).", "name_share": "قديش من الاسم موجود بالسؤال (١ = كله).",
        "name_in": "هل الاسم كله جوا السؤال (كلماته ورا بعض).", "PAIR": "كلمات المقارنة (الفرق، الشبه، بين، قارن، العلاقة).",
        "ASK_WORDS": "كلمات السؤال (شو، ما، ليش، كيف، هو…) اللي ما بتسمّي أشياء.", "content_words": "كلمات السؤال اللي بتسمّي أشياء.",
        "trigrams": "الحروف ثلاثة ثلاثة (كل الكلمات أو كلمات الأشياء بس).", "cosine": "قديش مجموعتين حروف متشابهين (٠–١).",
        "_names": "أرقام ← أسماء.", "_ins": "اللي بيحتاجهم المفهوم.", "_outs": "اللي بيحتاجوه.", "_clean": "بلا علامات وإيموجي.",
        "_li": "«لـ» ملزوقة صح («للاسم»، «لماء»).", "_bi": "«بـ» ملزوقة.", "PRACTICE": "الألعاب (بتاخد أسئلة «تمرين على X»).",
        "questions": "أسئلة مشهد واحد (بلا تكرار).", "description": "عمود الوصف: الأسئلة + المعنى + كلام المشهد.",
    },
}

FILES["02_question_factory/variety.py"] = {
    "title": "نفس المعلومة بكلام ثاني (الدفعة ٤٢)",
    "one": "الجمل اللي مش معلومة (عنوان اللعبة، كيف تلعب، الجملة الأخيرة) صار إلها ٣–٤ صيغ، وكل مفهوم بياخد وحدة ثابتة إله.",
    "role": "explain_generator.py (الصورة الكبيرة، الرحلة، شو لو، الشريط) و explain_activities.py (قارن، علّم صاحبك) و explain_activities2.py (ارمي، المغناطيس، الطاقة).",
    "how": [_REP,
            "POOL: لكل جملة صيغها بنفس المعنى، والجملة القديمة وحدة منهم. {me} {on} {L} {n} = الأسماء والدرس والرقم، و[هو|هي] = الفعل حسب المفهوم.",
            "pick: نفس المفتاح (الدرس + المفهوم) ← نفس الصيغة دايماً، فالصفحة ما بتتغيّر بين زيارة وزيارة.",
            "«شو بيصير لو اختفى…؟» كانت نفس الجملة ١٨ مرة؛ هلأ ٧ صيغ وأكثر وحدة ٥ مرات. المعلومات نفسها ما بتتغيّر."],
    "tip": "بدك صيغة جديدة؟ زيدها بـ POOL (بنفس المعنى بالضبط).",
    "items": {"POOL": "الصيغ لكل جملة.", "pick": "اختيار ثابت لنفس المفتاح.", "say": "الصيغة جاهزة: الأسماء محطوطة والفعل موافق."},
}

FILES["02_question_factory/explain_parts.py"] = {
    "title": "أجزاء الدرس بأربع طرق (الدفعة ٤٢)",
    "one": "مشهد «أجزاء الدرس» صار يتبدّل من درس لدرس: 🧩 ركّب · 🌱 ابنيها من تحت · ❓ شو ناقص؟ · 🎥 جولة الكاميرا. نفس المعلومة، طريقة ثانية.",
    "role": "explain_generator.explain_lesson بياخد منه حقل assemble للدرس (lesson_parts). الصفحة بترسمه بـ parts42.js (ركّب القديم بـ more_scenes2.js). check_scene بيفحصه.",
    "how": [
        "💡 حارث: «مشهد أجزاء النبات… يصير في مشهد ثاني غيره، بس الهدف إنه يوصل المعلومة».",
        "_base: مفاهيم الدرس (٣ وأكثر) وأسهمها وطوابقها (الأساس = ٠) وجملة لكل واحد، وترتيبها من الأساس لفوق.",
        "scene_build_up: الطالب بيكبس الجزء اللي بييجي هلأ: بيقعد بس إذا كل اللي بيحتاجه تحته (بدها طابقين عالأقل).",
        "scene_missing: صورة الدرس ناقصها جزء (من النص أول: إله شي قبله وشي بعده)، ٣ بطاقات فيها الصح مرة، جولتين، والسبب من الأسهم.",
        "scene_tour: فيلم: خطوة لكل جزء من الأساس لفوق (شو هو، وعلى شو بيقعد).",
        "lesson_parts: الدرس رقم i بالكتاب بياخد الدور (بداية الكتاب + i) من TURNS؛ إذا ما بينفع ← ركّب. هيك درسين ورا بعض ما بيتشابهوا، والأنواع الأربعة طلعوا بالكتب الـ١٢.",
    ],
    "tip": "بدك نوع خامس؟ اكتب scene_… هون، زيده على MAKERS و TURNS، وارسمه بـ parts42.js.",
    "items": {"TURNS": "ترتيب الأدوار: ركّب، ابنيها، شو ناقص، الجولة.", "_base": "داتا الأجزاء المشتركة (أو None إذا قليلة أو بلا أسهم).",
              "scene_build_up": "🌱 ابنيها من تحت.", "scene_missing": "❓ شو ناقص؟", "scene_tour": "🎥 جولة الكاميرا.",
              "MAKERS": "اسم النوع ← الدالة اللي بتعمله.", "lesson_parts": "مشهد أجزاء هالدرس حسب دوره."},
}

_G = _card("02_question_factory/explain_generator.py")
_add(_G, "🆕 الدفعة ٤٢: الجمل اللي مش معلومة من variety.say (صيغ ثانية، ثابتة لكل مفهوم) · حقل assemble للدرس صار من explain_parts.lesson_parts (بيتبدّل) · check_scene بيفحص build_up و missing و tour كمان.")
for k in ("scene_overview", "scene_journey", "scene_what_if", "scene_slider"):
    _G["items"][k] = (_G["items"].get(k) or "") + " 🆕 الدفعة ٤٢: جملها من variety.say."
_G["items"]["explain_lesson"] += " 🆕 الدفعة ٤٢: assemble = lesson_parts (ركّب / ابنيها / شو ناقص / الجولة)."
_G["items"]["check_scene"] = (_G["items"].get("check_scene") or "") + " 🆕 الدفعة ٤٢: + أجزاء الدرس الجديدة (الأسهم، البطاقات، الترتيب من الأساس)."
FILES["02_question_factory/explain_generator.py"] = _G

for p, names in (("02_question_factory/explain_activities.py", ("scene_compare", "scene_teach")),
                 ("02_question_factory/explain_activities2.py", ("scene_throw", "scene_magnet", "scene_power"))):
    c = _card(p)
    _add(c, "🆕 الدفعة ٤٢: عنوان اللعبة وكيف تلعب والجملة الأخيرة من variety.say (صيغ ثانية بنفس المعنى، ثابتة لكل مفهوم).")
    for k in names:
        c["items"][k] = (c["items"].get(k) or "") + " 🆕 الدفعة ٤٢: جملها من variety.say."
    FILES[p] = c

FILES["02_question_factory/tests/test_batch42.py"] = {
    "title": "فحص الدفعة ٤٢ (المصنع)",
    "one": "بيفحص الصيغ، وأجزاء الدرس الأربعة، وأسئلة المشاهد.",
    "role": "بيفحص variety.py و explain_parts.py و scene_questions.py و explain_generator.check_scene. python -m unittest tests.test_batch42",
    "how": ["الصيغ: ثابتة لكل مفهوم، مختلفة بين المفاهيم، القديمة وحدة منهم، الفعل بيوافق، والكتب صار فيها أكثر من صيغة.",
            "الأجزاء: كل درس إله مشهد، درسين ورا بعض مختلفين، الأربعة موجودين، وكلهم بيطابقوا الجراف.",
            "الأسئلة: norm، أسئلة لكل نوع، والقريب بالكتابة قريب."],
    "items": {"BOOKS": "الكتب الـ١٢ كجرافات.", "Variety": "الصيغ.", "Variety.test_the_same_concept_always_gets_the_same_words": "نفس المفتاح ← نفس الجملة.",
              "Variety.test_concepts_get_different_words": "كل الصيغ بتنستعمل.", "Variety.test_the_old_sentence_is_still_one_of_them": "الجملة القديمة موجودة.",
              "Variety.test_the_verb_agrees": "اختفى / اختفت، وما بيضل علامة قالب.", "Variety.test_the_twelve_books_say_it_in_more_than_one_way": "«شو لو» بأكثر من صيغة بالكتب.",
              "Parts": "أجزاء الدرس.", "Parts.test_every_lesson_gets_a_parts_scene_and_the_kinds_take_turns": "بتتبدّل والأربعة موجودين.",
              "Parts.test_they_teach_only_what_the_graph_says": "check_scene فاضي.", "Parts.test_build_up_from_the_base": "أول جزء من الأساس، و٣ خطوات.",
              "Parts.test_missing_the_right_card_is_there_once": "الصح مرة، بلا تكرار، والسبب جملة.", "Parts.test_the_tour_has_a_step_per_part": "خطوة لكل جزء.",
              "Questions": "الأسئلة.", "Questions.test_norm_and_words": "الشكل الموحّد.", "Questions.test_every_scene_kind_has_questions": "كل نوع إله أسئلة.",
              "Questions.test_close_spellings_are_close": "القريب قريب، والبعيد بعيد."},
}

FILES["02_question_factory/tests_browser/test_batch42.py"] = {
    "title": "فحص الدفعة ٤٢ بالمتصفح",
    "one": "الأشكال الجديدة للألعاب، ابنيها من تحت، شو ناقص، جولة الكاميرا، الرابط للمشهد، والتلفون.",
    "role": "بيفحص skins42.js و parts42.js و narrator.js و explain.js بالصفحة المبنية (ساعة وهمية). python tests_browser/test_batch42.py",
    "how": ["كل شكل بيترسم (?skin=) واللعبة شغّالة فيه (الرحلة بالنهر، القلعة والعلم)، والشكل بيتغيّر بين الدروس.",
            "🌱 مسكّرة، الغلط بيحكي شو ناقصه تحته، الفوز ← ليش والعد · ❓ الحفرة، البطاقة الغلط، الجولات، الفوز · 🎥 فيلم بيمشي لحاله.",
            "الرابط بيفتح المشهد · التلفون بلا سحب عالجنب."],
    "items": {"ok": "بيسجّل فحص.", "LOOKS": "أشكال كل لعبة.", "DECO": "الرسمة اللي لازم تطلع بكل شكل.", "ST": "حالة الصفحة.",
              "lesson_scene": "أول درس فيه نوع أجزاء معيّن.", "concept_scene": "أول مفهوم فيه نوع مشهد.", "link": "رابط الصفحة عند مشهد (+ شكل).",
              "new": "صفحة بساعة وهمية.", "go": "افتح رابط واستنى شوي."},
}

_note = {
    "02_question_factory/tests_browser/test_batch29.py": "🆕 الدفعة ٤٢: بيختار الدرس اللي مشهد أجزائه «ركّب» (صار يتبدّل).",
    "02_question_factory/tests_browser/test_ways.py": "🆕 الدفعة ٤٢: بيختار الدرس اللي مشهد أجزائه «ركّب».",
    "02_question_factory/tests_browser/test_batch41.py": "🆕 الدفعة ٤٢: build_up و missing بقائمة الفعاليات، والبزل من الدرس اللي مشهد أجزائه «ركّب».",
    "02_question_factory/tests_browser/test_films.py": "🆕 الدفعة ٤٢: بيمسك النحلة من رسمتها (svg جوا actor)، مش من نص المربع: هي بتطير، فالنص مرات بيوقع بالفراغ تحت اسمها.",
    "03_explain_player_src/world.js": "🆕 الدفعة ٤٢: st.said: لما الطالب يكبس جزء، شرحه بيضل ٤ ثواني (٢٤٠ فريم) قبل ما يرجع تذكير «بدها…» (كان ينمسح بأقل من ثانية).",
}
for _p, _l in _note.items():
    _c = _card(_p)
    _add(_c, _l)
    FILES[_p] = _c

# ======================================================================= the page (03)
FILES["03_explain_player_src/skins42.js"] = {
    "title": "نفس اللعبة بشكل ثاني (الدفعة ٤٢)",
    "one": "الرحلة والبرج وقارن والبزل بيلبسوا شكل مختلف بكل درس (نهر، قلعة، سلال، براويز…)، واللعبة نفسها ما بتتغيّر.",
    "role": "build_explain_template.py بيحطه مكان /*SKINS42*/ بـ explain.js (بعد ما كل المشاهد انسجّلت). بيغلّف SCENES.journey/tower/compare/assemble. ألوانه بـ b42.css.",
    "how": [_REP,
            "LOOKS: الرحلة (طريق، نهر، سكة، فضاء) · البرج (مكعبات، قلعة، كتب) · قارن (دوائر، سلال، بيوت) · البزل (ظلال، براويز، نجوم).",
            "lookOf: من الكتاب والدرس والمفهوم ← نفس الشكل لنفس المشهد، والدرس الجاي الشكل اللي بعده. ?skin=river بالرابط بيجرّب شكل.",
            "LOOK_DRAW: بعد ما المشهد يترسم، بيزيد رسم بس (مي تحت الطريق، سكة وقطار، نجوم، قلعة وعلم، رف، سلال، بيوت، براويز، دوائر نجوم).",
            "الأسماء LOOKS و lookOf (مش SKINS و skinOf: هذول موجودين من قبل لأشكال المواد، والتعارض كان رح يوقف الصفحة)."],
    "tip": "شكل جديد؟ زيد اسمه على LOOKS ورسمه بـ LOOK_DRAW وألوانه بـ b42.css، وجرّبه بـ ?skin=اسمه.",
    "items": {"LOOKS": "أشكال كل لعبة.", "LOOK_TRY": "شكل من الرابط (?skin=).", "lookOf": "شكل هالمشهد.",
              "lkEl": "عنصر SVG جديد.", "lkBox": "عرض وطول الصورة.", "lkAt": "مكان عنصر من translate.", "OL42": "خط الرسم الموحّد.",
              "LOOK_TRAVELLER": "قارب، قطار، صاروخ (بدل الشرارة).", "LOOK_DRAW": "رسم كل شكل لكل لعبة.",
              "bk": "سلة (جوا رسم قارن).", "hs": "بيت (جوا رسم قارن).", "dressed": "المشهد القديم + الشكل."},
}

FILES["03_explain_player_src/parts42.js"] = {
    "title": "مشاهد أجزاء الدرس الجديدة (الدفعة ٤٢)",
    "one": "🌱 ابنيها من تحت · ❓ شو ناقص؟ · 🎥 جولة الكاميرا: ثلاث طرق جديدة لنفس معلومة «أجزاء الدرس ومين بيحتاج مين».",
    "role": "build_explain_template.py بيحطه مع skins42.js. الداتا من explain_parts.py (حقل assemble للدرس). 🌱 و❓ بـ HANDS (narrator.js) فمسكّرين على الفيديو؛ 🎥 بـ stepTargets/cameraTargets.",
    "how": ["💡 حارث: «يصير في مشهد ثاني غيره، بس الهدف إنه يوصل المعلومة».",
            "p42Lay: الأجزاء بالطوابق: الأساس تحت، واللي بيحتاجه فوق.",
            "🌱 sceneBuildUp: صينية قطع؛ الجزء اللي كل اللي بيحتاجه موجود بيطير لمكانه وبيصحى وبتضوي أسهمه، وغيره بيتهز وبيحكي شو ناقصه تحته؛ الفوز ← gxWin ← الفيديو بيكمل.",
            "❓ sceneMissing: حفرة «؟» مكان الجزء، اللي بيحتاجه زعلان ورمادي؛ بطاقات؛ الصح بيرجع والكل بيفرح، الغلط «موجود بالصورة»؛ جولتين.",
            "🎥 sceneTour: الكل موجود، وكل خطوة بتصحّي جزء (من الأساس لفوق) وبتركّز عليه؛ بالفيديو الكاميرا بتقرّب عليه."],
    "items": {"p42Lay": "أماكن الأجزاء بالطوابق.", "p42Edges": "أسهم الدرس.", "p42Lesson": "اسم الدرس.",
              "sceneBuildUp": "🌱 ابنيها من تحت.", "lit": "جوا 🌱: بيضوّي الأسهم اللي طرفيها انحطوا.", "tryPiece": "جوا 🌱: كبسة على قطعة (بتقعد أو بتتهز).",
              "sceneMissing": "❓ شو ناقص؟", "nd": "جوا ❓: عنصر جزء.", "hide": "جوا ❓: بيخبّي الجزء وبيزعّل اللي بيحتاجه.", "back": "جوا ❓: بيرجّعه.",
              "round": "جوا ❓: جولة: السؤال والبطاقات.", "sceneTour": "🎥 جولة الكاميرا (فيلم بخطوة لكل جزء)."},
}

FILES["03_explain_player_src/b42.css"] = {
    "title": "ستايل الدفعة ٤٢",
    "one": "ألوان الأشكال الجديدة للألعاب ومشاهد أجزاء الدرس الجديدة.",
    "role": "build_explain_template.py بيحطه آخر ملف CSS (بعد b41.css). skins42.js و parts42.js بيستعملوه.",
    "how": ["كل لون من ألوان الصفحة (--panel، --ink، --line) فبيمشي بالفاتح والغامق.",
            "مي ونهر، سكة، نجوم، حجارة القلعة والعلم (بيطلع لما يكتمل البرج)، رف الكتب، سلال وبيوت وحديقة، براويز ودوائر النجوم.",
            "طوابق ابنيها والأماكن الفاضية، حفرة «شو ناقص» بتنبض، والأجزاء الزعلانة رمادي.",
            "⚠️ ملفوف بـ <style>…</style> زي كل ملفات CSS هون."],
    "tip": "الحركة بتوقف إذا الجهاز طالب حركة أقل.",
}

_ST = _card("03_explain_player_src/story.js")
_add(_ST, "🆕 الدفعة ٤٢ (" + _REP + "): كرتون «تعرّف عليّ» للصغار والابتدائي العليا: السلام و«شو بيحتاج؟» و«مين بيحتاجه؟» و«شو لو اختفى؟» والرجوع، كل واحد بصيغ (CV)، وكل مفهوم بياخد وحدة ثابتة (cvPick).")
_ST["items"].update({"cvPick": "🆕 الدفعة ٤٢: صيغة ثابتة لمفهوم (من رقمه).", "CV": "🆕 الدفعة ٤٢: صيغ جمل الكرتون."})
_ST["items"]["sceneCStory"] += " 🆕 الدفعة ٤٢: الجمل اللي مش معلومة بصيغ مختلفة للصغار والابتدائي العليا."
FILES["03_explain_player_src/story.js"] = _ST

_E = _card("03_explain_player_src/explain.js")
_add(_E, "🆕 الدفعة ٤٢: رابط بيفتح الصفحة عند مشهد (?lesson=…&concept=…&at=…&kind=…، و book= إذا في كذا كتاب)، وبينزل لعنده (جواب «اسأل سؤال») · /*SKINS42*/ مكان مشاهد الأجزاء الجديدة والأشكال.")
_E["items"]["renderAll2"] = (_E["items"].get("renderAll2") or "") + " 🆕 الدفعة ٤٢: قبلها الرابط بيحدد الدرس والمشهد (DEEP)."
FILES["03_explain_player_src/explain.js"] = _E

_B = _card("03_explain_player_src/build_explain_template.py")
_add(_B, "🆕 الدفعة ٤٢: parts42.js و skins42.js مكان /*SKINS42*/ بـ explain.js (بعد تسجيل كل المشاهد)، و b42.css آخر CSS.")
FILES["03_explain_player_src/build_explain_template.py"] = _B


# ======================================================================= the cards Y_batch31.py builds again (it calls finish at its end)
def finish(F):
    n = F["03_explain_player_src/narrator.js"]
    n["how"][-1] += " · 🆕 الدفعة ٤٢: 🌱 ابنيها من تحت و ❓ شو ناقص؟ فعاليات (HANDS)، و🎥 الجولة فيلم: الضوء والكاميرا على جزء بكل خطوة."
    n["items"]["HANDS"] += " 🆕 الدفعة ٤٢: + build_up و missing."
    n["items"]["stepTargets"] += " 🆕 الدفعة ٤٢: tour: الجزء وتحته."
    n["items"]["cameraTargets"] += " 🆕 الدفعة ٤٢: tour: الجزء بس."
    n["items"]["videoStep"] += " 🆕 الدفعة ٤٢: أول خطوة بالجولة: الصورة كاملة."
    t = F["02_question_factory/tests_browser/test_batch31.py"]
    t["how"][2] += " 🆕 الدفعة ٤٢: بدرس فيه البزل (PUZ) لأنه مشهد الأجزاء صار يتبدّل."
    t["items"]["puzzle_lesson"] = "🆕 الدفعة ٤٢: بتفتح درس النبات اللي مشهد أجزائه البزل (PUZ، والأفضل بلا «عالم النبتة» قبله) وبتبلّش من الصورة الكبيرة."
    m = F["05_explanation_api/main.py"]
    if len(m["how"]) < 9:
        m["how"].append("🆕 الدفعة ٤٢: BOOT = service.boot(): لما السيرفر يقوم، الملفات من الداتابيس ← القرص · مجموعة «ask» بـ /docs.")
    m["items"]["TAGS"] = (m["items"].get("TAGS") or "") + " 🆕 الدفعة ٤٢: + ask."
