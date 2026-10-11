# -*- coding: utf-8 -*-
"""🆕 batch 31: explanations for what batch 31 added (loaded after the other notes files; it ADDS to their cards)."""
import importlib.util
import os

_HERE = os.path.dirname(os.path.abspath(__file__))


def _load(name):
    spec = importlib.util.spec_from_file_location("n_" + name, os.path.join(_HERE, name + ".py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m.FILES


_D2 = _load("D2_page_player")
_E = _load("E_page_scenes")
_C = _load("C_server")

FILES = {}

# ---- narrator.js: the video goes on by itself ----
FILES["03_explain_player_src/narrator.js"] = dict(_D2["03_explain_player_src/narrator.js"])
FILES["03_explain_player_src/narrator.js"]["items"] = dict(_D2["03_explain_player_src/narrator.js"]["items"], **{
    "AUTO_SPEED": "وقت القراءة حسب العمر (اجتهاد): الصغار ×1.3 لأنهم بيقرأوا أبطأ، الثانوي ×0.9.",
    "t37": "🆕 الدفعة ٣٧: بتحوّل «الاسم» لاسم نظيف بخط عريض وملوّن، بلا علامات «» (الكلمات نفسها ما بتتغيّر). بتستعملها العناوين والأزرار والبطاقات.",
    "t37svg": "🆕 الدفعة ٣٧: نفس t37 بس جوّا نص SVG (فقاعات الكلام): الاسم عريض (tspan) بلا علامات.",
    "HANDS": "المشاهد اللي فيها شغل بالإيد (البزل، الشروط، ارسم الأسهم، قارن، العدسة… و🆕 الألعاب الخمسة، و🆕 الدفعة ٣٦: الرحلة و«شو لو» لأنهم صاروا اختيار): الفيديو بيورجي الحل أو بيعطي «🖐️ دورك».",
    "speedNow": "بترجّع رقم السرعة للمرحلة اللي على الشاشة هلأ (من AUTO_SPEED).",
    "stopGo": "بتوقّف العدّاد والمثال اللي شغّال، وبتشيل شريط «المشهد الجاي».",
    "countdown": "بتطلّع شريط «المشهد الجاي بعد ٥…» مع ⏸ وقّف و▶ هلأ وخط بيتعبّى، ولما يخلص بتنادي الخطوة الجاية.",
    "autoNext": "لما الفيديو يوصل آخر المشهد لحاله: إذا المشهد فيه حل كمثال بتشغّله، وبعدين عدّاد للمشهد الجاي (أو «دورك»، أو ملخّص الدرس بآخر مشهد).",
    "next": "بتروح للمشهد الجاي، أو بتطلّع ملخّص الدرس إذا هاد آخر مشهد.",
    "after": "بعد المثال (أو بدونه): بتختار أي عدّاد يطلع: ملخّص، «دورك»، أو «المشهد الجاي».",
    "lessonEnd": "كرت آخر الدرس: «🎉 خلصت درس…» + أسماء المفاهيم اللي تعرّف عليها + «من الأول» و«الدرس الجاي». ما بيدخل الدرس الجاي لحاله.",
})
FILES["03_explain_player_src/narrator.js"]["how"] = list(_D2["03_explain_player_src/narrator.js"]["how"]) + [
    "🆕 الدفعة ٣١: لما الفيديو يخلص مشهد لحاله، autoNext بتكمل: مثال (للبزل والشروط) ← عدّاد ← المشهد الجاي، وبآخر الدرس كرت ملخّص. أي لمسة من الطالب بتوقّف (stopGo)."]

# ---- stage.js: phone or computer ----
FILES["03_explain_player_src/stage.js"] = dict(_D2["03_explain_player_src/stage.js"])
FILES["03_explain_player_src/stage.js"]["items"] = dict(_D2["03_explain_player_src/stage.js"]["items"], **{
    "DEVICE": "بتعرف الجهاز من المتصفح: إصبع ولا فارة، حجم الشاشة، وقوة الجهاز ← dev (phone / tablet / desktop) و q (hi عالية / lo خفيفة). والرابط بيقدر يفرضها (?device= و ?q=).",
    "mm": "سؤال صغير للمتصفح (matchMedia): مثلاً هل الجهاز بيستعمل إصبع؟",
    "setQuality": "بتغيّر الجودة (عالية/خفيفة) على الصفحة وعلى زر الجودة، وإذا الطالب اختار بإيده بتحفظ اختياره. 🆕 الدفعة ٣٧: الزر بيورجي الخيارين (🍃 خفيفة · ✨ عالية) والشغّال معبّى، والمكان بيتبع الجودة فوراً (plRequality).",
})
FILES["03_explain_player_src/stage.js"]["how"] = list(_D2["03_explain_player_src/stage.js"]["how"]) + [
    "🆕 الدفعة ٣١: DEVICE بيعرف إذا تلفون ولا كمبيوتر وبيحط body[data-dev] و body[data-q]؛ الجهاز اللي بيتقطّع بينزل لحاله على «خفيفة»."]
FILES["03_explain_player_src/stage.js"]["how"][-1] += " · 🆕 الدفعة ٤٠: window.__ART صار فيه faceSVG، عشان scripts/export_art.py يصدّر وجهنا للسيرفر (رسمات المكتبة بنفس الوجه). · 🆕 الدفعة ٤١: و placeSVG و PLACE_NAMES، عشان فحص الأماكن (place_audit.py) يرسم كل مكان بكل حجم ويتأكد إنه كل إشي بمكانه."

# ---- the two demos ----
FILES["03_explain_player_src/more_scenes2.js"] = dict(_E["03_explain_player_src/more_scenes2.js"])
FILES["03_explain_player_src/more_scenes2.js"]["items"] = dict(_E["03_explain_player_src/more_scenes2.js"]["items"], **{
    "put": "بتحط القطعة بظلها: بتعلّمها «انحطت»، بتخبّي اسم الظل، الشخصية بتضحك وبتحكي، والأسهم بتبين. نفس الشي لما الطالب يحطها أو الفيديو.",
    "one": "مثال الفيديو بالبزل: بتاخد القطعة الجاية اللي لسا ما انحطت وبتطيّرها لظلها.",
    "fly": "حركة القطعة من مكانها لظلها بنعومة (بالساعة، مش بعدد الإطارات)، وبالآخر بتنادي put.",
})
FILES["03_explain_player_src/more_scenes3.js"] = dict(_E["03_explain_player_src/more_scenes3.js"])
FILES["03_explain_player_src/more_scenes3.js"]["items"] = dict(_E["03_explain_player_src/more_scenes3.js"]["items"], **{
})

# ---- main.py: the groups in /docs ----
FILES["05_explanation_api/main.py"] = dict(_C["05_explanation_api/main.py"])
FILES["05_explanation_api/main.py"]["items"] = dict(_C["05_explanation_api/main.py"].get("items", {}), **{
    "TAGS": "شرح عربي لكل مجموعة أبواب بصفحة /docs (الشرح، الصفحة، الرسومات، الليغو، الموديل…) عشان تطلع مرتّبة واحترافية.",
})

# ---- the new tests ----
FILES["02_question_factory/tests_browser/test_batch31.py"] = {
    "title": "فحص الفيديو اللي بيكمل لحاله",
    "one": "بيتأكد إن الفيديو بيمشي مشهد ورا مشهد لحاله، وإن الطالب دايماً بيقدر يوقّفه، وإن الصفحة بتعرف تلفون ولا كمبيوتر.",
    "role": "بيفحص narrator.js و stage.js و more_scenes2/3.js بالصفحة المبنية. بتشغّله: python tests_browser/test_batch31.py",
    "how": [
        "بيستعمل ساعة وهمية (Playwright clock): دقايق فيديو بتمر بثواني.",
        "بيستنى آخر المشهد: لازم يطلع العدّاد، ويعد لتحت، وبعدين المشهد الجاي لحاله.",
        "البزل: الفيديو لازم يحط كل القطع بظلالها كمثال. والشروط: يشغّل كل المفاتيح.",
        "⏸ و«هلأ» ولمسة على المشهد: كل واحد لازم يعمل شغلته.",
        "الصغار لازم ياخدوا وقت أطول لكل خطوة من الثانوي.",
        "آخر مشهد: كرت الملخّص بأسماء المفاهيم، وما بيدخل الدرس الجاي لحاله.",
        "الجهاز: كمبيوتر = desktop، تلفون = phone وجودة خفيفة، الزر بيغيّرها وبتنحفظ، والرابط بيفرضها.",
    ],
    "ideas": [["الساعة الوهمية", "بدل ما نستنى ١٠ دقايق فيديو، بنقدّم الوقت بالكود فبيخلص الفحص بسرعة."]],
    "tip": "شغّله بعد أي تعديل على وضع الفيديو أو المشاهد اللي فيها مثال.",
    "items": {
        "ok": "بتسجّل نتيجة فحص واحد (✅ أو ❌ مع السبب).",
        "ST": "سطر JavaScript بيقرأ حالة الصفحة: المشهد، العدّاد، الملخّص، الدرس، الخطوة.",
        "new": "بتفتح الصفحة بمتصفح جديد (كمبيوتر أو تلفون) مع الساعة الوهمية.",
        "run_until": "بتقدّم الساعة شوي شوي لحد ما يصير الشرط (أو يخلص الوقت).",
        "open_lesson": "بتفتح درس معيّن من القائمة.",
    },
}
FILES["05_explanation_api/tests_browser/test_home_page.py"] = {
    "title": "فحص صفحة السيرفر",
    "one": "بيتأكد إن صفحة السيرفر الرئيسية (الاحترافية) شغّالة مع السيرفر نفسه: الحالة، الأرقام، الكتب، الفلتر، البحث، كتاب جديد، النسخ، الحذف.",
    "role": "بيفحص static/home.html مع core/service.py (نفس الفانكشنز اللي FastAPI بينادي). بتشغّله من 05_explanation_api: python tests_browser/test_home_page.py",
    "how": [
        "Playwright بيوجّه كل طلب من الصفحة لفانكشن السيرفر الحقيقية (بدون ما نحتاج FastAPI هون).",
        "بيتأكد إن الحالة «شغّال» والنسخة، والـ١٢ كتاب، والأرقام.",
        "الفلتر «ثانوي» والبحث «كيمياء».",
        "بيبعت كتاب الحاسوب من الصفحة ← لازم يطلع «مادة جديدة» وكرته.",
        "نسخ الرابط، والحذف بكبستين.",
        "على التلفون: ما في سحب جانبي.",
    ],
    "items": {
        "ok": "بتسجّل نتيجة فحص واحد.",
        "handle": "بتجاوب على طلبات الصفحة من السيرفر الحقيقي (الصفحة، الحالة، الكتب، كتاب جديد، الحذف).",
    },
}


# 🆕 batch 41: this file builds narrator.js, more_scenes2.js and test_batch31.py again from the first notes, so their batch 41 parts are added here
_spec41 = importlib.util.spec_from_file_location("n_YB_batch41", os.path.join(_HERE, "YB_batch41.py"))
_m41 = importlib.util.module_from_spec(_spec41)
_spec41.loader.exec_module(_m41)
_m41.finish(FILES)

# 🆕 batch 42: the same — narrator.js (the new «parts» scenes in the video) and main.py (the boot from the database) get their batch 42 parts here
_spec42 = importlib.util.spec_from_file_location("n_YC_batch42", os.path.join(_HERE, "YC_batch42.py"))
_m42 = importlib.util.module_from_spec(_spec42)
_spec42.loader.exec_module(_m42)
_m42.finish(FILES)

# 🆕 batch 43: the same — narrator.js (the two new activities are the student's) gets its batch 43 part here
_spec43 = importlib.util.spec_from_file_location("n_YD_batch43", os.path.join(_HERE, "YD_batch43.py"))
_m43 = importlib.util.module_from_spec(_spec43)
_spec43.loader.exec_module(_m43)
_m43.finish(FILES)

# 🆕 batch 44: the same — narrator.js (slower reading, the voice stops with the video) gets its batch 44 part here
_spec44 = importlib.util.spec_from_file_location("n_YE_batch44", os.path.join(_HERE, "YE_batch44.py"))
_m44 = importlib.util.module_from_spec(_spec44)
_spec44.loader.exec_module(_m44)
_m44.finish(FILES)
