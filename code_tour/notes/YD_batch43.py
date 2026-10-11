# -*- coding: utf-8 -*-
"""🆕 batch 43 (Hareth: «زيد لنا رسمات بحيث إنها تغطي مفاهيم كثيرة جداً… وكمان الـ AI ياخذ من الليجو» + «فعالية فعاليتين جداد» +
«اسأل عن مشهد… لازم يكون بنفس الكتاب، وإذا برا بنرجعه على نفس المفهوم»): 675 new library drawings in 10 families (the Saudi coverage
78% → 95%, the 12 books unchanged), the model also reviews the WEAK pictures (lego), two new activities for the concepts with few scenes
(🕵️ مين أنا؟ · 🧩 ركّب الجملة), and the search only inside the student's book.
Loaded after YC_batch42 (sorted: «YC» < «YD» < «Y_»). Y_batch31.py builds narrator.js again, so it calls finish() at its end."""
import copy
import importlib.util
import os

_HERE = os.path.dirname(os.path.abspath(__file__))
_ME = os.path.basename(__file__)


def _now():
    out = {}
    for fn in sorted(os.listdir(_HERE)):
        if fn.endswith(".py") and not fn.startswith("_") and fn < _ME:
            spec = importlib.util.spec_from_file_location("nD_" + fn[:-3], os.path.join(_HERE, fn))
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
_ART = "💡 حارث: «زيد لنا رسمات بحيث إنها تغطي مفاهيم جداً جداً كثيرة… مواد كثيرة… والـ AI ياخذ من الليجو»."
_FAM = [
    "F = أول المفتاح («lib:F.اسم»)، و D = {اسم: رسمة}: لكل رسمة words و body (أشكال SVG بسيطة جوا ١٠٠×١٠٠، و{OL} = الخط الموحّد) و face و anim.",
    "only = المواد اللي الرسمة إلها (كلمة زي «البؤرة» عدسة بالفيزياء وزلزال بالأرض)، و never = مواد ممنوعة عليها، والنص من الشمال لليمين (direction=\"ltr\") فـ«C°» ما بتنقلب.",
    "ALIASES: اسم مفهوم بالضبط ← رسمته (حتى لو من عائلة ثانية)، والقيمة ممكن (مفتاح، (مواد)) لاسم إله معنى بمادة بس.",
    "🧪 فحصناها على ٧٩٥٢ مفهوم سعودي: الكلمة العامة اللي كانت تاخد مفهوم إله رسمة أحسن (الجهاز، الهوائي، النظرية، القاعدة…) انشالت أو انحصرت.",
]


def _fam(path, title, one, extra, items):
    FILES[path] = {"title": title, "one": one,
                   "role": "art_library.py بيقرأه (FAMILIES، 🆕 الدفعة ٤٣). offline_generator.icon_source بيختار منه بكلمات اسم المفهوم (الأطول بيربح)، والكتاب بياخد بس رسماته (for_book).",
                   "how": [_ART] + _FAM + extra,
                   "tip": "رسمة جديدة؟ ضيفها لـ D بنفس الشكل، وشغّل python art_library.py (لازم OK) و python art_coverage.py، وتأكد إنه tests/test_batch43.py ✅ (الكتب الـ١٢ ما تغيّرت).",
                   "items": items}


_fam("02_question_factory/art_lib/everyday.py", "رسمات المكتبة: الحياة اليومية (الدفعة ٤٣)",
     "عائلة «day» (١٠٧ رسمات): الأكل والطبخ (العجين، الفرن، الفلافل…)، النظافة والصحة، الإسعاف والأمان، البيت، والأخلاق والتعامل.",
     ["«الشعر» هون مشط للمهارات الحياتية بس (بالاجتماعيات الشعر قصيدة: civ.poetry).", "الإعلان never اجتماعيات («إعلان اسم المملكة» مش دعاية)."],
     {"ALIASES": "فاضية هون.", "ALIAS_ONLY": "بلا حد."})
_fam("02_question_factory/art_lib/money.py", "رسمات المكتبة: المال (الدفعة ٤٣)",
     "عائلة «money» (٢٩ رسمة): الدخل والمصروف، الادخار والاستثمار، الأسهم والسندات، المخاطر، القروض والائتمان، والوظيفة.",
     ["«الوسيط» للمالية بس (بالرياضيات الوسيط إحصاء)، والسند never اجتماعيات («بلاد السند» مكان)."],
     {"ALIASES": "فاضية هون.", "ALIAS_ONLY": "بلا حد."})
_fam("02_question_factory/art_lib/mind.py", "رسمات المكتبة: التفكير والطريقة العلمية (الدفعة ٤٣)",
     "عائلة «mind» (٣٣ رسمة): الفرضية والتجربة والمتغيرات والاستنتاج، الحقيقة والرأي، الإعلام والشائعات، الدقة والوضوح والعمق.",
     ["الدقة والاستنتاج والدليل never رياضيات (هناك إلها معنى ثاني)."],
     {"ALIASES": "متغيرة درجة الحرارة ← رسمتها القديمة · العينة الضابطة ← الثوابت.", "ALIAS_ONLY": "بلا حد."})
_fam("02_question_factory/art_lib/physics.py", "رسمات المكتبة: الفيزياء (الدفعة ٤٣)",
     "عائلة «phys» (٧٨ رسمة): القوى والعزم، الموجات والصوت، العدسات والضوء، الكهرباء (مكثف، مقاومة، ترانزستور)، الذرة والنواة، والوحدات.",
     ["العزم والحيود والمقذوف never علوم الأرض (هناك «العزم الزلزالي» و«الحيود» = مرتفعات)."],
     {"SC": "المواد: العلوم (والفيزياء جواها).",
      "ALIASES": "السعة ← قمة وقاع الموجة · الجسم والصورة ← العدسة (فيزياء) · الهوائي ← الهوائي (فيزياء بس) · الانشطار/الاندماج النووي ← النواة · التطعيم (الإشابة) ← حزم الطاقة.",
      "ALIAS_ONLY": "بلا حد."})
_fam("02_question_factory/art_lib/geo.py", "رسمات المكتبة: الأرض والجغرافيا (الدفعة ٤٣)",
     "عائلة «geo» (٩٤ رسمة): الصخور والمعادن، الزلازل والبراكين، الطقس والمناخ والأقاليم، الخرائط والإحداثيات، الكواكب والنجوم.",
     ["البؤرة هون زلزال (never فيزياء ورياضيات)، و«السكان» رجعت لرسمتها القديمة (الكثافة والمكتظة بس هون)."],
     {"E": "المواد: العلوم والاجتماعيات.", "ALIASES": "قارة آسيا ← رسمة القارات (اجتماعيات).", "ALIAS_ONLY": "بلا حد."})
_fam("02_question_factory/art_lib/ecology.py", "رسمات المكتبة: البيئة والأحياء العامة (الدفعة ٤٣)",
     "عائلة «eco» (٨٢ رسمة): السلاسل الغذائية والعلاقات بين الكائنات، السلوك، أعضاء الجسم (البطين، المثانة)، الوراثة، الكيمياء العامة، والفصول.",
     ["الانشطار هون انشطار ثنائي (never فيزياء وأرض)، واللقاح ما بيستعمل «اللقاح» (حبوب اللقاح شي ثاني)."],
     {"SC": "المواد: العلوم.",
      "ALIASES": "المحور ← محور الأرض (علوم؛ بالأحياء خلية عصبية، من biology.py) · مندل ← الوراثة · الطرز الجينية/الشكلية · موازنة المعادلات · القارات.",
      "ALIAS_ONLY": "بلا حد."})
_fam("02_question_factory/art_lib/tech.py", "رسمات المكتبة: التقنية (الدفعة ٤٣)",
     "عائلة «tech» (٧١ رسمة): البرمجة (لبنات، مكدس، طابور، شجرة)، الشبكات، الذكاء الاصطناعي، الأمن الرقمي، والمكتب (وورد، إكسل…).",
     ["«التحكم» لحالها انشالت (وحدة التحكم المركزية مش لبنة سكراتش)."],
     {"DG": "المواد: المهارات الرقمية.", "ALIASES": "وورد · إكسل · باوربوينت · المصادر · الأحداث · الجمهور المستهدف.", "ALIAS_ONLY": "بلا حد."})
_fam("02_question_factory/art_lib/civics.py", "رسمات المكتبة: التاريخ والوطن والمجتمع (الدفعة ٤٣)",
     "عائلة «civ» (٤٧ رسمة): الممالك القديمة والمخطوطات، الدولة والوزارات والسلطات، المجتمع (البطالة، الإسكان)، والمنظمات.",
     ["الكلمات العامة («الهوية»، «الشخصية»، «التقويم»، «الحصون») انشالت عشان ما تاخد مفاهيم إلها رسمات أحسن."],
     {"S": "المواد: الاجتماعيات.",
      "ALIASES": "التواريخ ← التقويم · الجبيل/ينبع ← الميناء الصناعي · حقل الغوار ← النفط · الجدول الزمني · التركيب العمري والهرم السكاني ← السكان…",
      "ALIAS_ONLY": "بلا حد."})
_fam("02_question_factory/art_lib/math2.py", "رسمات المكتبة: الرياضيات ٢ (الدفعة ٤٣)",
     "عائلة «math2» (٨٩ رسمة): الاحتمال والإحصاء، الدوال والمتطابقات، المصفوفات، الهندسة والتحويلات، الوحدات (سم، مل، إنش)، والمنطق.",
     ["«المسلمة» و«النظرية» لحالهم صاروا أسماء بالضبط بس (مسلمة التوازي بتضل الخطين المتوازيين)."],
     {"M": "المواد: الرياضيات.", "card": "بطاقة رمز رياضي (رمز، لون، حجم، مكان).",
      "ALIASES": "المسلمة/النظرية/المسلمات ← البرهان · متجه الإزاحة ← المتجه · النظرية الأساسية في الجبر ← رسمتها القديمة.",
      "ALIAS_ONLY": "بلا حد."})
_fam("02_question_factory/art_lib/english2.py", "رسمات المكتبة: الإنجليزي ٢ (الدفعة ٤٣)",
     "عائلة «en2» (٤٥ رسمة): مواضيع كتب الإنجليزي (المشاهير، الاختراعات، الهجرة، المفقودات، الموضة، الرياضيين، الألغاز…).",
     ["المنافسة هون رياضية (للإنجليزي بس)، و«كنزة صوفية» قميص مش كنز."],
     {"EN": "المواد: الإنجليزي.", "gcard": "بطاقة كلمة/قواعد إنجليزية.",
      "ALIASES": "سائح ← السياحة · الرسوم المتحركة · الروبوتات · كنزة صوفية ← القميص.", "ALIAS_ONLY": "بلا حد."})

# ======================================================================= the two new activities
FILES["02_question_factory/explain_activities3.py"] = {
    "title": "فعاليتين جداد للمفهوم اللي مشاهده قليلة (الدفعة ٤٣)",
    "one": "🕵️ مين أنا؟ (شخصية مخبّاية بتعطي أدلة، والطالب بيختارها من ٣ بطاقات) · 🧩 ركّب الجملة (معنى المفهوم بـ٣–٤ قطع مخلوطة). بدهم الاسم والمعنى بس.",
    "role": "explain_generator.explain_lesson بياخد منه وحدة لما المفهوم إله مشهدين أو أقل (FEW)، بالدور، والميزانية (explain_budget.RECALL) بتسمح بمرة ثانية بس. الصفحة بترسمهم بـ acts43.js، و check_scene بيفحصهم بـ check.",
    "how": [
        "💡 حارث: «ممكن تزيد لي فعالية فعاليتين جداد» (المشاهد نفسها والحكاية ما تغيّرت).",
        "ليش للمفهوم اللي مشاهده قليلة: الجراف بيعطيه أسهم قليلة، فالألعاب الثانية (المغناطيس، البرج…) ما بتنعمل إله. هدول بدهم المعنى بس.",
        "🕵️ scene_who_am_i: الأدلة = شو بيحتاج (إذا في) + قطع معناه (واسمه مخفي «…» بـ _mask) + مين بيحتاجه. بيبلش بدليلين، وكل غلطة بتفتح دليل.",
        "البطاقات الغلط من نفس الدرس أول (og.tiered)، بس ولا وحدة الأدلة بتنطبق عليها (_fits) ولا اسمها مذكور بالأدلة، وكل وحدة بتحكي هي شو («مش أنا! Y: …»).",
        "🧩 scene_sentence: قطعة من المعنى ٥–١٢ كلمة، بتنقص ٣ أو ٤ قطع بالترتيب (_cut): القطعة ما بتخلص بكلمة صغيرة («على»، «التي»…) وما بتبلش بـ«جداً».",
        "candidates: كل الطرق بالدور (وإذا الأسهم انحكت مرتين: مين أنا بالمعنى بس؛ أو قطعة ثانية من المعنى)، والمولّد بياخد أول وحدة الميزانية بتقبلها.",
        "check: الدليل من معناه أو سهم حقيقي · الصح بطاقة وحدة · ولا غلط بتنطبق عليه الأدلة · القطع = معناه حرف حرف.",
    ],
    "ideas": [["مين أنا؟ كانت لعبة بمصنع الأسئلة القديم", "هلأ صارت فعالية بصفحة الشرح، بنفس إطار الألعاب (المهمة، النقاط، النجوم)."]],
    "tip": "بدك فعالية ثالثة من المعنى؟ اكتب scene_… هون، زيدها على candidates و KINDS، وارسمها بـ acts43.js، وزيد نوعها على HANDS (narrator.js) والعقد.",
    "items": {
        "KINDS": "الأنواع: who_am_i و sentence.", "FEW": "مفهوم بهالعدد من المشاهد أو أقل بياخد وحدة (٢: الكرتون + وحدة).",
        "_SMALL": "كلمات صغيرة ما بتخلص فيها قطعة (في، على، التي، منه…).", "_TAIL": "كلمات ما بتبلش فيها قطعة (جداً، فقط، نفسه…).",
        "_by_stage": "جملة حسب المرحلة (صغار، ابتدائي عليا، متوسط، ثانوي).", "_mask": "بيخبّي اسم المفهوم بالدليل («…»)، مع «ال» و«و/ب» قبله.",
        "_fits": "هل الدليل بينطبق على مفهوم ثاني؟ (يعني ما بيصير بطاقة غلط).", "scene_who_am_i": "🕵️ مين أنا؟ (arrows=False: أدلة المعنى بس).",
        "_cut": "بيقص الجملة لـ k قطع بأماكن منيحة (أو أقل إذا ما في أماكن).", "_sentences_of": "قطع المعنى اللي بتصير جملة (٥–١٢ كلمة).",
        "scene_sentence": "🧩 ركّب الجملة (which = أي قطعة من المعنى).", "candidates": "كل الطرق بالدور، للمولّد.",
        "pick": "أول وحدة بتنعمل (بلا ميزانية).", "check": "الفحص مع الجراف.",
    },
}

FILES["03_explain_player_src/acts43.js"] = {
    "title": "الفعاليتين الجداد بالصفحة (الدفعة ٤٣)",
    "one": "🕵️ مين أنا؟: «؟» كبيرة مكان الشخصية، أدلة تحت الصورة، و٣ بطاقات · 🧩 ركّب الجملة: الشخصية بتقول «جملتي تخربطت!»، أماكن ①②③، وقطع مخلوطة.",
    "role": "build_explain_template.py بيحطه مع parts42.js و skins42.js (مكان /*SKINS42*/). الداتا من explain_activities3.py. بـ HANDS (narrator.js) فمسكّرين على الفيديو. بيستعمل إطار اللعبة (games36.js) وبطاقات g36Opts (acts36.js).",
    "how": [
        "💡 حارث: «فعالية فعاليتين جداد»، ونفس الشكل والإطار (المكان، الشخصيات، النجوم) ما تغيّر.",
        "🕵️ sceneWhoAmI: الشخصية مرسومة بس مخفية (w43-hidden) وفوقها «؟»؛ دليلين ظاهرين؛ الغلط: البطاقة بتنشطب، الشرح «مش أنا! …»، ودليل جديد.",
        "الصح: كل الأدلة بتظهر، الـ«؟» بتختفي، الشخصية بتنط وبتقول «أنا X!»، والفوز (gxWin) ← «ليش؟» والفيديو بيكمل.",
        "mask: الشريط فوق (اسم المفهوم وصورته) بيستنى ورا «؟» لحد ما يحزر، عشان ما ينكشف الجواب.",
        "🧩 sceneSentence: القطع مخلوطة (ومش بالترتيب أبداً)؛ القطعة الصح بتروح لمكانها، والغلط بتتهز وبتحكي «دوّر على بداية الجملة» أو «شو بيجي بعد…؟».",
        "آخر قطعة: الجملة كاملة بخط أخضر، والشخصية بتقولها، والفوز.",
    ],
    "items": {"sceneWhoAmI": "🕵️ مين أنا؟", "mask": "جوا 🕵️: بيخبّي/بيرجّع اسم المفهوم وصورته بالشريط فوق.",
              "open": "جوا 🕵️: بيفتح الدليل الجاي (وبيرجع false إذا خلصوا).", "sceneSentence": "🧩 ركّب الجملة."},
}

FILES["03_explain_player_src/b43.css"] = {
    "title": "ستايل الدفعة ٤٣",
    "one": "شكل الفعاليتين الجداد: الـ«؟» والأدلة، وأماكن الجملة وقطعها.",
    "role": "build_explain_template.py بيحطه آخر ملف CSS (بعد b42.css). acts43.js بيستعمله.",
    "how": ["كل لون من ألوان الصفحة (--panel، --ink، --line، --good، --brand) فبيمشي بالفاتح والغامق.",
            "الـ«؟» بتختفي بنعومة والشخصية بتنط · الدليل الجديد بينزل · القطعة الغلط بتتهز · الجملة الكاملة بإطار أخضر.",
            "الشريط فوق: .pstop.w43-mask بتغطي اسم المفهوم وصورته بـ«؟».",
            "⚠️ ملفوف بـ <style>…</style> زي كل ملفات CSS هون."],
    "tip": "الحركة بتوقف إذا الجهاز طالب حركة أقل (prefers-reduced-motion).",
}

# ======================================================================= changed files (factory)
_O = _card("02_question_factory/offline_generator.py")
_add(_O, "🆕 الدفعة ٤٣: icon_source بيرجّع الرسمة وكيف انلقت (اسم، جدول، مكتبة، ليغو = قوية · كلمة من المعنى أو شخصية المادة = ضعيفة)، والليغو المحفوظ بيغلب كلمة المعنى.")
_O["items"].update({"STRONG": "🆕 الدفعة ٤٣: الطرق القوية (من الاسم): name · alias · library · lego.",
                    "WEAK": "🆕 الدفعة ٤٣: الطرق الضعيفة: meaning (كلمة من المعنى: «العجين» ← نقطة مي) · subject (شخصية المادة). هدول الموديل بيراجعهم.",
                    "icon_source": "🆕 الدفعة ٤٣: (الرسمة، كيف): never · name · alias · library · lego · meaning · subject.",
                    "icon_label": "🆕 الدفعة ٤٣: شو بتورجي الرسمة بكلمتين (للموديل لما يراجع الضعيفة)."})
_O["items"]["icon_for"] = (_O["items"].get("icon_for") or "") + " 🆕 الدفعة ٤٣: = icon_source(...)[0]."
FILES["02_question_factory/offline_generator.py"] = _O

_L = _card("02_question_factory/lego.py")
_add(_L, "🆕 الدفعة ٤٣: الموديل بيشوف كمان الرسمة الضعيفة («هلأ بتورجي…») وبيقدر يقول «keep» (بتنحفظ وما بينسأل مرة ثانية) · «لا» المعلم ما بينسأل عنها الموديل من وراه.")
_L["items"].update({"REVIEW": "🆕 الدفعة ٤٣: نص للموديل: هاي الرسمة الحالية (من كلمة بالمعنى)، إذا مناسبة جاوب keep.",
                    "kept": "🆕 الدفعة ٤٣: الموديل قال رسمته الحالية مناسبة؟"})
for k, v in (("needs_picture", "🆕 الدفعة ٤٣: بيتخطّى keep والمرفوض من المعلم."),
             ("ask_model", "🆕 الدفعة ٤٣: current = {اسم: شو بتورجي رسمته الضعيفة} ← keep بتنحفظ."),
             ("choose", "🆕 الدفعة ٤٣: keep ما إلها اقتراحات (رفض بس)."), ("PROMPT", "🆕 الدفعة ٤٣: + {review}.")):
    _L["items"][k] = (_L["items"].get(k) or "") + " " + v
FILES["02_question_factory/lego.py"] = _L

_A = _card("02_question_factory/art_library.py")
_add(_A, "🆕 الدفعة ٤٣: ١٠ عائلات جديدة (١٥٠٤ رسمة كلهم) · TAGS: physics و earth · ALIASES ممكن (مفتاح، (مواد)) لاسم إله معنى بمادة بس.")
_A["items"]["FAMILIES"] = (_A["items"].get("FAMILIES") or "") + " 🆕 الدفعة ٤٣: + everyday, money, mind, physics, geo, ecology, tech, civics, math2, english2."
_A["items"]["TAGS"] = (_A["items"].get("TAGS") or "") + " 🆕 الدفعة ٤٣: + physics و earth («البؤرة» عدسة بالفيزياء وزلزال بالأرض)."
_A["items"]["_load"] = (_A["items"].get("_load") or "") + " 🆕 الدفعة ٤٣: الاسم الثاني ممكن يكون (مفتاح، مواده)."
FILES["02_question_factory/art_library.py"] = _A

_BI = _card("02_question_factory/art_lib/biology.py")
_add(_BI, "🆕 الدفعة ٤٣: «المحور» بالأحياء ← الخلية العصبية (المحور العصبي)، قبل ما يوصل لـ«محور الأرض» تبع العلوم (ecology.py).")
FILES["02_question_factory/art_lib/biology.py"] = _BI

_G = _card("02_question_factory/explain_generator.py")
_add(_G, "🆕 الدفعة ٤٣: المفهوم اللي إله مشهدين أو أقل بياخد 🕵️ مين أنا؟ أو 🧩 ركّب الجملة (explain_activities3.candidates، والميزانية بتقبل) · check_scene بيفحصهم.")
_G["items"]["explain_lesson"] += " 🆕 الدفعة ٤٣: + فعالية من explain_activities3 للمفهوم اللي مشاهده قليلة."
_G["items"]["check_scene"] = (_G["items"].get("check_scene") or "") + " 🆕 الدفعة ٤٣: + who_am_i و sentence."
FILES["02_question_factory/explain_generator.py"] = _G

_BU = _card("02_question_factory/explain_budget.py")
_add(_BU, "🆕 الدفعة ٤٣: RECALL (🕵️ و🧩): بيرجعوا يلاقوا المعنى مرة ثانية (عشان يتذكره)، بس ولا مرة ثالثة.")
_BU["items"]["RECALL"] = "🆕 الدفعة ٤٣: who_am_i و sentence: مرة ثانية مسموحة، ثالثة لأ."
_BU["items"]["facts"] = (_BU["items"].get("facts") or "") + " 🆕 الدفعة ٤٣: + أدلة مين أنا وجملة ركّب."
_BU["items"]["Budget.ok"] = (_BU["items"].get("Budget.ok") or "") + " 🆕 الدفعة ٤٣: RECALL بيدخل إذا ولا معلومة انحكت مرتين."
FILES["02_question_factory/explain_budget.py"] = _BU

_Q = _card("02_question_factory/scene_questions.py")
_add(_Q, "🆕 الدفعة ٤٣: أسئلة لـ who_am_i («حزّرني مين هو X»، «ما صفات X؟») و sentence («ما تعريف X؟»، «رتبلي تعريف X»)، وهم تمرين (PRACTICE).")
_Q["items"]["questions"] = (_Q["items"].get("questions") or "") + " 🆕 الدفعة ٤٣: + who_am_i و sentence."
_Q["items"]["PRACTICE"] = (_Q["items"].get("PRACTICE") or "") + " 🆕 الدفعة ٤٣: + who_am_i و sentence."
FILES["02_question_factory/scene_questions.py"] = _Q

_BT = _card("03_explain_player_src/build_explain_template.py")
_add(_BT, "🆕 الدفعة ٤٣: acts43.js مع parts42.js و skins42.js (مكان /*SKINS42*/)، و b43.css آخر CSS.")
FILES["03_explain_player_src/build_explain_template.py"] = _BT

# ======================================================================= changed files (server)
_SI = _card("05_explanation_api/core/scene_index.py")
_add(_SI, "🆕 الدفعة ٤٣ (💡 حارث: «لازم يسأل عن مشهد بنفس الكتاب، وإذا برا بنرجعه على نفس المفهوم» = الخطة، AI Tutor ص١٩): البحث بكتاب الطالب بس (الكتاب لازم)، ودرسه الحالي أول شوي (LESSON_FIRST، اجتهاد)؛ برا الكتاب ← «هاد مش من درسنا…» + زر يرجّعه لمفهومه + اقتراحات من درسه.")
_SI["items"].pop("_allowed", None)
_SI["items"].update({"MAX_BOOKS": "🆕 الدفعة ٤٣: كم كتاب بالذاكرة (الأقدم استعمالاً بيطلع).",
                     "LESSON_FIRST": "🆕 الدفعة ٤٣: زيادة صغيرة لمشاهد درسه الحالي (اجتهاد).",
                     "forget": "🆕 الدفعة ٤٣: بيمسح كتاب (أو الكل) من الذاكرة (لما الكتاب يتغيّر أو ينحذف).",
                     "_outside": "🆕 الدفعة ٤٣: الجواب لما السؤال برا الكتاب: الرسالة، back (مفهومه أو بداية درسه، والرابط)، واقتراحات."})
for k in ("_load", "_by_name", "_qscore", "_pick_scene", "_by_meaning", "_by_text"):
    if k in _SI["items"]:
        _SI["items"][k] += " 🆕 الدفعة ٤٣: لكتاب واحد بس (B)."
_SI["items"]["ask"] = (_SI["items"].get("ask") or "") + " 🆕 الدفعة ٤٣: book_id لازم (بلاه no_book)، lesson_id و concept_id (وين هو هلأ)، و in_his_lesson."
FILES["05_explanation_api/core/scene_index.py"] = _SI

_DB = _card("05_explanation_api/core/db.py")
_add(_DB, "🆕 الدفعة ٤٣: أسطر كتاب واحد بس (book_rows)، وبصمته (book_stamp)، والأعداد للحالة (counts) — بالداتابيس وبالملف.")
_DB["items"].update({"_PgScenes.book_rows": "🆕 الدفعة ٤٣: أسطر كتاب واحد بالترتيب.", "_PgScenes.book_stamp": "🆕 الدفعة ٤٣: (عدد، آخر تعديل) لكتاب: تغيّر؟ بنقرأ من جديد.",
                     "_PgScenes.counts": "🆕 الدفعة ٤٣: كم سطر، كم كتاب، وكم سطر إله أرقام معنى.", "_FileScenes.book_rows": "🆕 الدفعة ٤٣: نفسها بالملف.",
                     "_FileScenes.book_stamp": "🆕 الدفعة ٤٣: نفسها بالملف.", "_FileScenes.counts": "🆕 الدفعة ٤٣: نفسها بالملف."})
FILES["05_explanation_api/core/db.py"] = _DB

_SV = _card("05_explanation_api/core/service.py")
_add(_SV, "🆕 الدفعة ٤٣: ask بدها الكتاب (ومعه الدرس والمفهوم) · _lego_for_book بيبعت كمان المفاهيم اللي رسمتها ضعيفة ومعها شو بتورجي هلأ (الموديل بيبني أحسن أو بيقول keep).")
_SV["items"]["ask"] = (_SV["items"].get("ask") or "") + " 🆕 الدفعة ٤٣: book_id لازم + lesson_id و concept_id."
_SV["items"]["_lego_for_book"] = (_SV["items"].get("_lego_for_book") or "") + " 🆕 الدفعة ٤٣: + الضعيفة (og.WEAK) مع current."
FILES["05_explanation_api/core/service.py"] = _SV

for p, line, items in (
        ("05_explanation_api/api/schemas.py", "🆕 الدفعة ٤٣: AskRequest: book_id لازم + lesson_id و concept_id (وين الطالب هلأ)؛ grade و stage قدام.", {"AskRequest": " 🆕 الدفعة ٤٣: + lesson_id و concept_id."}),
        ("05_explanation_api/api/routes.py", "🆕 الدفعة ٤٣: POST /ask بيبعت الدرس والمفهوم كمان.", {"ask": " 🆕 الدفعة ٤٣: + الدرس والمفهوم."}),
        ("05_explanation_api/static/ask.html", "🆕 الدفعة ٤٣: بلا «كل الكتب»: كتاب الطالب، الدرس اللي هو فيه، والمفهوم · السؤال برا الكتاب ← الرسالة وزر «↩️ ارجع لـ X» واقتراحات.", {}),
        ("05_explanation_api/scripts/build_scene_index.py", "🆕 الدفعة ٤٣: --ask بيدوّر بكتاب واحد (--book أو أول كتاب) وبيطبع الرسالة وback.", {}),
        ("05_explanation_api/core/contract.py", "🆕 الدفعة ٤٣: who_am_i و sentence بالعقد (فعاليتين للطالب).", {}),
        ("05_explanation_api/tests_browser/test_ask_page.py", "🆕 الدفعة ٤٣: بلا «كل الكتب»، والسؤال برا الكتاب بيرجّعه لمفهومه (الزر بيفتح الصفحة عنده).", {}),
        ("02_question_factory/tests/test_lego.py", "🆕 الدفعة ٤٣: الأمثلة اللي «بلا رسمة» صارت الكركم والزعفران (العجين والتتبيلة صار إلهم رسمات).", {}),
        ("05_explanation_api/tests/test_lego_api.py", "🆕 الدفعة ٤٣: مفاهيم الطبخ صارت اللي لسا بلا رسمة (الكركم، الزعفران، القرفة…).", {"COOKING": " 🆕 الدفعة ٤٣: أسماء جديدة بلا رسمات."}),
        ("02_question_factory/tests/test_budget.py", "🆕 الدفعة ٤٣: 🕵️ و🧩 بيرجعوا يلاقوا المعنى مرة ثانية بس (للمفهوم اللي مشاهده قليلة)، ولا مرة ثالثة.", {}),
        ("02_question_factory/tests_browser/test_batch41.py", "🆕 الدفعة ٤٣: 🕵️ و🧩 فعاليات كمان (ACTS).", {"ACTS": " 🆕 الدفعة ٤٣: + who_am_i و sentence."}),
        ("02_question_factory/tests_browser/test_batch40.py", "🆕 الدفعة ٤٣: «الصفحة خفيفة» صار يقيس الأهم: المكتبة (١٥٠٠+) مش جوا الصفحة (أقل من ٦٠ رسمة منها)، والحجم أقل من ١٫٣ ميغا (الفعاليتين زادوا ٣٢ مشهد).", {})):
    c = _card(p)
    _add(c, line)
    for k, v in items.items():
        c["items"][k] = (c["items"].get(k) or "") + v
    FILES[p] = c

_T42 = _card("05_explanation_api/tests/test_batch42.py")
_add(_T42, "🆕 الدفعة ٤٣: CASES فيها الكتاب · بكتابه بس · برا كتابه ← بيرجع لمفهومه · درسه أول · بس الكتاب المسؤول بالذاكرة.")
_T42["items"].update({"Ask.test_his_book_only": "🆕 الدفعة ٤٣: سؤال عن كتاب ثاني ← برا (ما بيطلع مشهد من كتاب ثاني).",
                      "Ask.test_outside_his_book_he_goes_back_to_his_concept": "🆕 الدفعة ٤٣: برا كتابه ← الرسالة + back لمفهومه + اقتراحات.",
                      "Ask.test_his_lesson_comes_first": "🆕 الدفعة ٤٣: نفس الاسم بدرسين: درسه أول.",
                      "Ask.test_only_the_asked_book_is_in_memory": "🆕 الدفعة ٤٣: الذاكرة فيها بس الكتاب اللي انسأل عنه."})
FILES["05_explanation_api/tests/test_batch42.py"] = _T42

# ======================================================================= the new tests
FILES["02_question_factory/tests/test_batch43.py"] = {
    "title": "فحص الدفعة ٤٣ (المصنع)",
    "one": "المكتبة الكبيرة نظيفة، التغطية ≥٩٠٪، كل كلمة بمعناها بكل مادة، الكتب الـ١٢ ما تغيّرت، الموديل بيراجع الضعيفة، والفعاليتين الجداد.",
    "role": "بيفحص art_library.py والعائلات الجديدة و art_coverage.py و offline_generator.icon_source و lego.py و explain_activities3.py. python -m unittest tests.test_batch43",
    "how": ["المكتبة: ولا مشكلة، ≥١٤٠٠ رسمة، العائلات العشرة، ولا سكربت ولا رابط، وكل نص من الشمال لليمين.",
            "التغطية: أكثر من ٧٠٠٠ مفهوم سعودي، ≥٩٠٪ إلهم رسمة إلهم (كانت ٧٨٪).",
            "كلمة وحدة بمعاني: البؤرة، المحور، الشعر… · الكلمات العامة الجديدة ما أخذت ولا رسمة قديمة أحسن (الجهاز الهضمي، مسلمة التوازي…).",
            "الكتب الـ١٢: بصمة رسمات الـ١٠٧ مفهوم نفسها قبل الدفعة.",
            "الموديل (وهمي): بيشوف الرسمة الضعيفة وبيبني أحسن · keep بتنحفظ وما بينسأل ثاني · keep لرسمة ما ورّيناه إياها ← لا · «لا» المعلم ما بينسأل عنها.",
            "الفعاليتين: موجودات وصادقات مع الجراف، بس للمفهوم اللي مشاهده قليلة وآخر شي، الأدلة ما بتقول الجواب، القطع = المعنى، والغلط بينكشف."],
    "items": {"NEW_FAMILIES": "العائلات العشرة الجديدة.", "BOOKS_FINGERPRINT": "بصمة رسمات الكتب الـ١٢ قبل الدفعة.",
              "books_fingerprint": "بتحسب البصمة هلأ.", "fake_model": "موديل وهمي (بيقرأ الأسماء وبيعدّ المرات).",
              "TestBiggerLibrary": "المكتبة والتغطية.", "TestBiggerLibrary.test_the_library_is_bigger_and_clean": "نظيفة وكبيرة.",
              "TestBiggerLibrary.test_most_saudi_concepts_have_their_own_drawing": "≥٩٠٪.",
              "TestOneWordManyMeanings": "الكلمات بمعانيها.", "TestOneWordManyMeanings.test_each_subject_gets_its_own_meaning": "كل مادة معناها.",
              "TestOneWordManyMeanings.test_new_generic_words_never_take_a_good_old_picture": "القديم الأحسن ضل.",
              "TestOneWordManyMeanings.test_no_cartoon_from_a_name_that_only_looks_like_a_word": "عمر بن عبدالعزيز وبلاد السند ووحدة التحكم: لا.",
              "TestOneWordManyMeanings.test_the_12_books_keep_their_pictures": "الكتب ما تغيّرت.",
              "TestTheModelLooksAtWeakPictures": "مراجعة الضعيفة.", "TestTheModelLooksAtWeakPictures.setUp": "مكتبة ليغو مؤقتة.",
              "TestTheModelLooksAtWeakPictures.tearDown": "بيمسحها.", "TestTheModelLooksAtWeakPictures.test_weak_and_strong_ways": "قوية/ضعيفة.",
              "TestTheModelLooksAtWeakPictures.test_the_model_sees_the_weak_picture_and_builds_a_better_one": "بيبني أحسن، والمبنية بتغلب.",
              "TestTheModelLooksAtWeakPictures.test_keep_is_saved_and_never_asked_again": "keep مرة وحدة.",
              "TestTheModelLooksAtWeakPictures.test_keep_only_for_a_picture_we_showed": "keep بلا رسمة ← لا.",
              "TestTheModelLooksAtWeakPictures.test_the_teachers_no_is_never_asked_again": "«لا» المعلم بتضل.",
              "TestTwoNewActivities": "الفعاليتين.", "TestTwoNewActivities.setUpClass": "بيولّد الكتب الـ١٢ وبيجمع الفعاليتين.",
              "TestTwoNewActivities.test_both_are_made_and_true_to_the_graph": "موجودات وصادقات.",
              "TestTwoNewActivities.test_only_for_the_concepts_with_few_scenes": "بس للقليلة، وآخر مشهد.",
              "TestTwoNewActivities.test_the_clues_never_say_the_answer_and_no_wrong_card_fits": "الأدلة والبطاقات.",
              "TestTwoNewActivities.test_the_sentence_is_the_meaning_cut_in_good_places": "القطع.",
              "TestTwoNewActivities.test_a_broken_one_is_caught": "الغلط بينكشف.", "TestTwoNewActivities.test_the_search_and_the_contract_know_them": "الأسئلة والعقد.",
              "TestTwoNewActivities.test_the_page_has_them_and_they_are_the_students": "بالصفحة وبـ HANDS."},
}

FILES["02_question_factory/tests_browser/test_batch43.py"] = {
    "title": "فحص الدفعة ٤٣ بالمتصفح",
    "one": "🕵️ مين أنا؟ و🧩 ركّب الجملة بالصفحة المبنية (ساعة وهمية)، كمبيوتر وتلفون، وصور.",
    "role": "بيفحص acts43.js و b43.css و narrator.js (HANDS). python tests_browser/test_batch43.py [مجلد الصور]",
    "how": ["🕵️: مسكّرة (🖐️ دورك، بلا ▶) · الـ«؟» وفي دليلين · الشريط فوق ما بيكشف الجواب · الغلط بينشطب وبيحكي هو شو (ودليل جديد) · الصح: الشخصية بتطلع، الفوز، «ليش؟» والعدّاد.",
            "🧩: مسكّرة · القطع مخلوطة · أول قطعة غلط بتتهز («دوّر على البداية») · بالترتيب ← الجملة كاملة والفوز والعدّاد.",
            "📱 التلفون: بلا سحب جانبي · ولا خطأ JS."],
    "items": {"ok": "بتسجّل نتيجة فحص.", "ST": "حالة الصفحة (دورك، العدّاد، ▶، النص، ليش؟).", "concept_scene": "أول (أو رقم k) مفهوم فيه هالنوع.",
              "link": "رابط بيفتح الصفحة عند المشهد.", "new": "صفحة جديدة بساعة وهمية.", "go": "بيفتح الرابط وبيستنى.",
              "shot": "صورة (إذا انعطى مجلد).", "wait_go": "بيستنى العدّاد (الفيديو بيكمل)."},
}

FILES["05_explanation_api/tests/test_batch43_api.py"] = {
    "title": "فحص الدفعة ٤٣ (السيرفر: الرسمات الضعيفة)",
    "one": "كتاب فيه مفهوم رسمته ضعيفة: سؤال واحد للموديل فيه «هلأ بتورجي 💧» ← بيبني أحسن، أو keep وما في سؤال ثاني.",
    "role": "بيفحص service._lego_for_book و lego.ask_model عبر service.generate. PYTHONPATH=tests/local_stub_only_for_sandbox python -m unittest tests.test_batch43_api",
    "how": ["book: كتاب الحاسوب بأسماء طبخ؛ «الكركبة» معناها «خليط فيه الماء» ← نقطة مي (ضعيفة).",
            "Model: موديل وهمي بيجاوب أجزاء ليغو، أو keep للكركبة.",
            "بيبني: سؤال واحد، فيه «now shows «💧»»، والرسمة المبنية بتغلب، وكل الصفحة ليغو.",
            "keep: بتنحفظ، الرسمة بتضل، وكتاب ثاني بنفس المفاهيم ← ولا سؤال."],
    "items": {"WEAK": "المفهوم الضعيف ومعناه.", "NONE": "مفاهيم بلا رسمة.", "book": "الكتاب التجريبي.", "Model": "الموديل الوهمي.",
              "Model.__init__": "keep ولا لأ.", "Model.__call__": "بيجاوب سؤال الليغو بس.", "TestWeakPicturesThroughTheServer": "الفحوصات.",
              "TestWeakPicturesThroughTheServer.setUp": "مكتبة ليغو مؤقتة.", "TestWeakPicturesThroughTheServer.tearDown": "بيمسح الكتب والمكتبة.",
              "TestWeakPicturesThroughTheServer.test_the_weak_picture_is_shown_to_the_model_and_rebuilt": "بيشوفها وبيبني.",
              "TestWeakPicturesThroughTheServer.test_keep_then_no_second_call": "keep وبعدين ولا سؤال."},
}


# ======================================================================= the cards Y_batch31.py builds again (it calls finish at its end)
def finish(F):
    n = F["03_explain_player_src/narrator.js"]
    n["how"][-1] += " · 🆕 الدفعة ٤٣: 🕵️ مين أنا؟ و 🧩 ركّب الجملة فعاليات (HANDS)."
    n["items"]["HANDS"] += " 🆕 الدفعة ٤٣: + who_am_i و sentence."
