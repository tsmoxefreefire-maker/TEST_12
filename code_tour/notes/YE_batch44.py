# -*- coding: utf-8 -*-
"""🆕 batch 44 (Hareth: «الكلام اللي تحت كثير سريع… الطالب ما بيلحق يقرا» + «لما الكلام يمشي هو يحكي… موديل كويس ورخيص، إحنا بس نجربه»):
the explanation reads SLOWER (and the story's moments with it), and a VOICE reads every line (a model, made once, kept; the line waits for it).
Loaded after YD_batch43 (sorted: «YD» < «YE» < «Y_»). Y_batch31.py builds narrator.js again, so it calls finish() at its end."""
import copy
import importlib.util
import os

_HERE = os.path.dirname(os.path.abspath(__file__))
_ME = os.path.basename(__file__)


def _now():
    out = {}
    for fn in sorted(os.listdir(_HERE)):
        if fn.endswith(".py") and not fn.startswith("_") and fn < _ME:
            spec = importlib.util.spec_from_file_location("nE_" + fn[:-3], os.path.join(_HERE, fn))
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
_ASK = "💡 حارث: «لما الكلام يمشي هو يحكي… موديل كويس وفي نفس الوقت رخيص، إحنا بس نجربه»."

FILES["05_explanation_api/core/tts.py"] = {
    "title": "الصوت اللي بيقرأ الشرح (الدفعة ٤٤)",
    "one": "سطر الشرح ← صوت. موديل بيعمله مرة وحدة، بينحفظ بـ data/tts (وبالداتابيس)، وكل طالب بعده بياخده فوراً وببلاش.",
    "role": "service.tts_audio و tts_status بينادوه، والطلبين GET /tts و GET /tts/status (routes.py). الصفحة (tts44.js) بتطلب كل سطر من /tts. المفاتيح من متغيرات البيئة (أو api_key.txt عبر llm_gateway).",
    "how": [_ASK,
            "provider: TTS_PROVIDER، أو مفتاح Azure ← azure، وإلا none. Gemini بس لما TTS_PROVIDER=gemini (عشان مفتاح الفريق ما يبلش يصرف على الصوت لحاله). fake للفحص.",
            "clean: اللي بينقرأ = السطر بلا إيموجي ولا «» ولا نقاط (نفس كلام الطالب، بس نظيف).",
            "_name: اسم الملف = بصمة (المزوّد، الصوت، الموديل، السرعة، النص): نفس السطر ← نفس الملف للأبد. speak: موجود؟ من الملف. مش موجود؟ الموديل مرة وبينحفظ.",
            "_azure: SSML بصوت أردني (ar-JO-SanaNeural) وسرعة حسب العمر (RATE: الصغار ‎-20٪)، mp3. المفتاح بالـ header بس، وما بيطلع بأي رسالة خطأ.",
            "_gemini: Interactions API (gemini-3.8-flash-lite-tts): النص لحاله، والأسلوب («speaking slowly…» حسب العمر، STYLE) بـ speech_metadata. الجواب base64؛ _find_audio بيلاقيه بالشكلين، و _wav بيلف الـ PCM بملف WAV.",
            "_fake: نغمة طولها على قد النص (٦٠ ملّي ثانية للحرف): الصفحة والفحوصات بتجرّب «استنى الصوت» بلا مفتاح ولا نت.",
            "MAX_CHARS = ٤٠٠: أطول من هيك مش سطر شرح ← مرفوض (ما حدا يصرف المفتاح بنصوص طويلة)."],
    "ideas": [["مرة وحدة وبينحفظ", "زي فكرة المهندس: كل إشي بينعمل قبل وبينحفظ. أول طالب بيستنى ثانية، والباقي فوراً."],
              ["المفتاح سر", "بمتغيرات البيئة على Render بس (AZURE_SPEECH_KEY، AZURE_SPEECH_REGION، أو GEMINI_API_KEY)، ولا مرة بـ GitHub ولا بالصفحة."]],
    "tip": "تجربة محلية بلا مفتاح: TTS_PROVIDER=fake. بمفتاح Azure: AZURE_SPEECH_KEY=… AZURE_SPEECH_REGION=westeurope. صوت ثاني: TTS_VOICE_AZURE=ar-JO-TaimNeural.",
    "items": {"MAX_CHARS": "أطول سطر بينقرأ.", "TIMEOUT": "كم ثانية نستنى الموديل.", "STAGES": "المراحل الأربع.",
              "RATE": "سرعة Azure حسب العمر (أبطأ للصغار).", "STYLE": "أسلوب Gemini حسب العمر.", "VOICE": "الصوت لكل مزوّد (بيتغيّر بمتغير بيئة).",
              "MODEL_GEMINI": "موديل Gemini للصوت.", "CALLS": "كم مرة نادينا الموديل (الفحوصات بتعدّ).", "_EMOJI": "الإيموجي اللي ما بينقرأ.",
              "TTSError": "ما في صوت / نص غلط / الموديل وقع.", "_keys": "المفاتيح من llm_gateway (البيئة أو api_key.txt).",
              "provider": "مين بيحكي هلأ.", "clean": "شو بينقرأ من السطر.", "_ext": "mp3 (Azure) أو wav.", "_name": "اسم ملف السطر (بصمة).",
              "_dir": "وين الملفات (TTS_DIR للفحص بس).", "folder": "المجلد (بيعمله إذا مش موجود).", "status": "شغّال؟ مين؟ كم سطر جاهز؟",
              "speak": "السطر ← (صوت، نوعه، انعمل هلأ؟).", "_azure": "طلب Azure.", "_find_audio": "بيلاقي الصوت بجواب Gemini.",
              "_wav": "PCM ← ملف WAV.", "_gemini": "طلب Gemini.", "_fake": "الصوت الوهمي للفحص."},
}

FILES["03_explain_player_src/tts44.js"] = {
    "title": "الصفحة بتحكي (الدفعة ٤٤)",
    "one": "لما الصفحة جاية من سيرفرنا وفيه صوت: كل سطر شرح بينقرأ، والسطر ما بيروح إلا لما الصوت يخلص. بلا صوت: زي قبل بالزبط.",
    "role": "build_explain_template.py بيحطه مع acts43.js. explain.js (show) و story.js (stPlay) بينادوا ttsSay؛ narrator.js (stopVideo) و renderScene بينادوا ttsStop.",
    "how": [_ASK,
            "ttsInit: بس إذا الصفحة من سيرفرنا (/explain…): بيسأل /tts/status. إذا الصوت وصل بعد أول سطر، بيبلّش المشهد من جديد عشان ينقرأ.",
            "ttsSay: بيطلب /tts?stage=…&text=… وبيشغّله؛ بيرجع true لما يخلص، false إذا ما في صوت (فاللي ناداه بيستنى وقته العادي). ولا مرة بيعلق: حد ٤٥ ثانية.",
            "ttsStop: سطر جديد أو لمسة بتوقف الصوت القديم، والجواب القديم ما بيحرّك سطر جديد (seq).",
            "ttsButton: «🔊 الصوت» / «🔇» بأزرار الراوي (بينحفظ على الجهاز)، و«🔊 اكبس لتسمع» لما المتصفح مانع الصوت لحد أول كبسة."],
    "items": {"TTS": "الحالة: شغّال، مكتوم، ممنوع، الصوت الحالي، رقم السطر.", "ttsInit": "بيسأل السيرفر إذا في صوت (مرة وحدة).",
              "ttsOn": "في صوت وما هو مكتوم؟", "ttsStop": "بيوقف الصوت الحالي.", "ttsSay": "بيقرأ سطر وبيستنى يخلص.",
              "fin": "جوا ttsSay: الصوت خلص / وقع / انوقف.", "ttsButton": "زر الصوت."},
}

FILES["03_explain_player_src/b44.css"] = {
    "title": "ستايل الدفعة ٤٤",
    "one": "زر الصوت: عادي، مكتوم (أخف)، وبينبض لما المتصفح بده كبسة أول.",
    "role": "build_explain_template.py بيحطه آخر ملف CSS (بعد b43.css). tts44.js بيستعمله.",
    "how": ["ألوان من ألوان الصفحة فبيمشي بالفاتح والغامق.", "النبض بيوقف إذا الجهاز طالب حركة أقل.", "⚠️ ملفوف بـ <style>…</style> زي كل ملفات CSS هون."],
}

_E = _card("03_explain_player_src/explain.js")
_add(_E, "🆕 الدفعة ٤٤: بالفيديو كل سطر بينقرأ (ttsSay) والسطر الجاي ما بييجي إلا لما الصوت يخلص + نفَس صغير؛ بلا صوت: الوقت العادي (أبطأ هلأ). وهو بيمشي لحاله كمان بينقرأ كل سطر. SHOWN: صوت قديم ما بيحرّك سطر جديد.")
_E["items"]["go"] = "🆕 الدفعة ٤٤: جوا show: السطر الجاي (أو آخر المشهد)، بس إذا لسا نفس السطر ونفس الفيديو."
_E["items"]["renderScene"] = (_E["items"].get("renderScene") or "") + " 🆕 الدفعة ٤٤: بيوقف الصوت القديم وبيحط زر الصوت."
FILES["03_explain_player_src/explain.js"] = _E

_S = _card("03_explain_player_src/story.js")
_add(_S, "🆕 الدفعة ٤٤: stPlay: كل ترجمة (subtitle) بتنقرأ، وإذا الصوت لسا بيحكي لما الترجمة لازم تخلص، الحكاية بتستنى (الوقت بيوقف). الوقفة أو السحب بيوقفوا الصوت.")
_S["items"]["sayNow"] = "🆕 الدفعة ٤٤: جوا stPlay: بيقرأ الترجمة وبيتذكر لوين لازم يستنى."
FILES["03_explain_player_src/story.js"] = _S

_SV = _card("05_explanation_api/core/service.py")
_add(_SV, "🆕 الدفعة ٤٤: tts_status و tts_audio (الصوت: مش مشغّل ← 404، نص غلط ← 400، والسطر الجديد بينحفظ بالداتابيس).")
_SV["items"].update({"tts_status": "🆕 الدفعة ٤٤: حالة الصوت.", "tts_audio": "🆕 الدفعة ٤٤: سطر ← صوت (مرة وحدة وبينحفظ)."})
FILES["05_explanation_api/core/service.py"] = _SV

_R = _card("05_explanation_api/api/routes.py")
_add(_R, "🆕 الدفعة ٤٤: GET /tts/status · GET /tts?text=…&stage=… (الصوت، cache أسبوع بالمتصفح).")
_R["items"].update({"tts_status": "🆕 الدفعة ٤٤: الصوت شغّال؟", "tts": "🆕 الدفعة ٤٤: سطر مقروء (audio)."})
FILES["05_explanation_api/api/routes.py"] = _R

_B = _card("03_explain_player_src/build_explain_template.py")
_add(_B, "🆕 الدفعة ٤٤: tts44.js بعد acts43.js، و b44.css آخر CSS.")
FILES["03_explain_player_src/build_explain_template.py"] = _B

FILES["05_explanation_api/tests/test_batch44_api.py"] = {
    "title": "فحص الدفعة ٤٤ (الصوت)",
    "one": "مين بيحكي، شو بينقرأ، مرة وحدة، طلبات Azure و Gemini (حسب توثيقهم، بلا نت)، الطلبات، والصفحة أبطأ.",
    "role": "بيفحص core/tts.py و service و routes و القالب. python -m unittest tests.test_batch44_api",
    "how": ["بلا مفتاح ← ولا صوت (404) · مفتاح Azure ← azure · Gemini بس لما ينطلب.",
            "نفس السطر ← نفس الملف ومرة وحدة · عمر ثاني ← ملف ثاني · نص فاضي أو طويل ← 400.",
            "Azure: العنوان، الـ headers، الصوت الأردني، ‎-20٪ للصغار · الخطأ ما فيه المفتاح.",
            "Gemini: العنوان، المفتاح بالـ header، الموديل والصوت، الأسلوب برّا النص، والجوابين ← WAV.",
            "الصفحة: AUTO_SPEED أبطأ، والسطر بيستنى الصوت."],
    "items": {"TEMPLATE": "قالب الصفحة.", "_Answer": "جواب وهمي بدل النت.", "_Answer.__init__": "بياخد الجسم.", "_Answer.read": "بيرجّعه.",
              "_Answer.__enter__": "with.", "_Answer.__exit__": "with.", "TestWhoSpeaks": "مين بيحكي.",
              "TestWhoSpeaks.test_no_key_no_voice": "بلا مفتاح.", "TestWhoSpeaks.test_an_azure_key_turns_it_on_and_gemini_only_when_asked": "Azure / Gemini.",
              "TestWhoSpeaks.test_what_is_read": "شو بينقرأ.", "TestMadeOnce": "مرة وحدة.", "TestMadeOnce.setUp": "صوت وهمي ومجلد مؤقت.",
              "TestMadeOnce.tearDown": "بيرجّع البيئة.", "TestMadeOnce.test_the_same_line_is_made_once_and_kept": "نفس السطر.", "TestMadeOnce.test_bad_lines": "نصوص غلط.",
              "TestTheRealProviders": "Azure و Gemini.", "TestTheRealProviders.setUp": "مجلد مؤقت.", "TestTheRealProviders.tearDown": "بيرجّع البيئة.",
              "TestTheRealProviders.test_azure_request_jordanian_voice_slower_for_kids": "طلب Azure.",
              "TestTheRealProviders.test_azure_failure_never_shows_the_key": "الخطأ بلا مفتاح.", "TestTheRealProviders.test_gemini_request_and_both_answer_shapes": "طلب Gemini.",
              "TestEndpoints": "الطلبات.", "TestEndpoints.test_status_and_a_line": "/tts/status و /tts.",
              "TestThePageReadsSlower": "الصفحة.", "TestThePageReadsSlower.test_reading_time_by_age_is_longer": "أبطأ وبتستنى الصوت."},
}

FILES["05_explanation_api/tests_browser/test_tts_page.py"] = {
    "title": "فحص الصوت بالمتصفح (الدفعة ٤٤)",
    "one": "الصفحة من السيرفر الحقيقي بصوت وهمي وساعة وهمية: الزر، السطر بيستنى الصوت، 🔇، الحكاية بتستنى، وبلا صوت زي قبل.",
    "role": "بيفحص tts44.js و explain.js و story.js و /tts. صوت المتصفح متبدّل بمسجّل (الفحص بيقرر متى الصوت «يخلص»). python tests_browser/test_tts_page.py",
    "how": ["الزر بيطلع بس لما السيرفر فيه صوت · السطر بينبعت لـ /tts (المرحلة ونفس الكلام).",
            "٢٥ ثانية والصوت لسا بيحكي ← السطر ما بيتحرك · الصوت خلص ← نفَس ← السطر الجاي وبينقرأ.",
            "🔇 ← بيرجع يمشي بوقته وبلا صوت · الحكاية: الترجمة بتنقرأ والوقت بيوقف لحد ما الصوت يخلص.",
            "بلا صوت: ولا زر ولا طلب، والصفحة زي قبل · التلفون · ملف الصوت حقيقي ومرة وحدة."],
    "items": {"VOICE_ON": "السيرفر فيه صوت ولا لأ (الفحص بيبدّل).", "ok": "بتسجّل نتيجة.", "handle": "بتجاوب الصفحة من الخدمة الحقيقية (الصفحة، /tts/status، /tts).",
              "FAKE_AUDIO": "صوت المتصفح الوهمي (بيسجّل وبيستنى الفحص).", "STEP": "رقم السطر الحالي.", "LAST": "آخر سطر انطلب صوته.",
              "new": "صفحة جديدة بساعة وهمية والصوت الوهمي."},
}


def finish(F):
    n = F["03_explain_player_src/narrator.js"]
    n["how"][-1] += " · 🆕 الدفعة ٤٤: AUTO_SPEED أبطأ (الصغار ١٫٧، الابتدائي العليا ١٫٤، المتوسط ١٫٢، الثانوي ١٫٠٥) والحكاية معه · stopVideo بيوقف الصوت."
    n["items"]["AUTO_SPEED"] = (n["items"].get("AUTO_SPEED") or "") + " 🆕 الدفعة ٤٤: أبطأ ٢٠–٣٠٪ («الطالب ما بيلحق يقرا»)."
    n["items"]["stopVideo"] = (n["items"].get("stopVideo") or "") + " 🆕 الدفعة ٤٤: + بيوقف الصوت."
