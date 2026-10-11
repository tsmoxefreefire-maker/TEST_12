"""The CONTRACT with the front end: what each scene kind means and which fields it carries. Served at GET /scene-kinds.
Relations everywhere: an edge [a, b] means «b needs a» (a comes before b). Every text is Arabic and ready to show."""

COMMON = {"kind": "نوع المشهد", "steps": "جمل قصيرة بالترتيب (سطر الراوي)", "paragraph": "فقرة «ليش؟» (شرح أطول وبسيط)"}

SCENE_KINDS = {
    "overview": {"what": "🗺️ الصورة الكبيرة للدرس: كل المفاهيم مرقّمة بترتيب التعلّم وأسهم «بيحتاج».",
                 "fields": {"concepts": "ids المفاهيم", "edges": "[[a,b]] يعني b بيحتاج a", "levels": "{id: رقم العمود بترتيب التعلّم}"}},
    "world": {"what": "🌱 عالم حقيقي (طقم النبتة): مي وشمس وهوا، والطالب بيجرّب بإيده.",
              "fields": {"kit": "اسم الطقم (plant)", "parts": "{دور: concept_id}", "needs": "شو بتحتاج (water/sun/air)", "info": "{دور: معنى من الجراف}"}},
    "assemble": {"what": "🧩 ركّب المشهد: كل شخصية لظلّها (بازل)، ولما توصل بتحكي مين هي.",
                 "fields": {"concepts": "ids", "edges": "[[a,b]]", "levels": "{id: عمود}", "says": "{id: جملة تعريف}"}},
    # 🆕 batch 42: the lesson's «parts» scene (the field «assemble» of a lesson) takes turns, lesson after lesson: assemble · build_up · missing · tour
    "build_up": {"what": "🌱 ابنيها من تحت: أجزاء الدرس بالصينية؛ الطالب بيكبس الجزء اللي بييجي هلأ، وكل جزء بيقعد بس فوق اللي بيحتاجه (طابق فوق طابق). نشاط للطالب.",
                 "fields": {"concepts": "ids", "edges": "[[a,b]]", "levels": "{id: الطابق (0 = الأساس)}", "says": "{id: جملة تعريف}", "order": "ids من الأساس لفوق (ترتيب صح)"}},
    "missing": {"what": "❓ شو ناقص؟ صورة الدرس كاملة ناقصها جزء: اللي بيحتاجه زعلان؛ الطالب بيختار الناقص من بطاقات (جولتين). نشاط للطالب.",
                "fields": {"concepts": "ids", "edges": "[[a,b]]", "levels": "{id: طابق}", "says": "{id: جملة}", "rounds": "[{id: الناقص, options: [ids فيها الصح مرة وحدة], say, why}]"}},
    "tour": {"what": "🎥 جولة الكاميرا: فيلم بيمشي من الأساس لفوق، جزء بكل خطوة (شو هو، وعلى شو بيقعد). مش نشاط: الفيديو بيشغّله.",
             "fields": {"concepts": "ids", "edges": "[[a,b]]", "levels": "{id: طابق}", "says": "{id: جملة}", "order": "ids من الأساس لفوق", "stops": "[{id, under: ids اللي تحته}] (خطوة لكل جزء بعد الأولى)"}},
    "meet": {"what": "👋 تعرّف عليّ: المفهوم بالنص، واللي بيحتاجهم من جهة، واللي بيحتاجوه من الجهة الثانية.",
             "fields": {"target": "id", "ins": "اللي بيحتاجهم", "outs": "اللي بيحتاجوه", "roles": "{id: ليش}", "focus": "لكل خطوة: target / ins / out:<id> (مين نضوّي ونركّز الكاميرا عليه)"}},
    "interview": {"what": "🎤 مقابلة: الطالب بيكبس سؤال والشخصية بتجاوب.", "fields": {"target": "id", "qa": "[{q, a}]"}},
    "flip": {"what": "🎴 بطاقات بتتقلب: على الوجه سؤال، وورا كل بطاقة جملة كاملة بتنفهم لحالها.",
             "fields": {"target": "id", "cards": "[{front: السؤال, back: جملة كاملة}] (اعرضوا السؤال صغير فوق الجملة لما تنقلب)"}},
    "journey": {"what": "🚶 الرحلة: سلسلة «بيحتاج». إذا traveller = id بيمشي فعلاً (مي/هوا/ضوء)، وإذا spark شرارة بتمشي بالطريق. 🆕 الدفعة ٣٦: المحطات الجاية مخبّاية (؟) والطالب بيختار المحطة الجاية من بطاقات (الصح + غلط من stops[].wrong).",
                "fields": {"target": "id", "route": "ids بالترتيب", "traveller": "id أو spark", "stops": "[{id, say, wrong: [{id, say: ليش مش هي}]}] (wrong من المحطة الثانية)"}},
    "what_if": {"what": "🔮 شو بيصير لو: مفتاح بيطفي المفهوم، واللي بيحتاجوه بيتعبوا ورا بعض. 🆕 الدفعة ٣٦: الطالب بيتوقّع أول (بيكبس على اللي رح يتعبوا)، وبعد ما يطفّي كل توقّع بينفحص (✅/❌ وليش).",
                "fields": {"target": "id", "affected": "ids بالترتيب", "calm": "ids ما بتتأثر", "edges": "[[a,b]]"}},
    "before_after": {"what": "⏳ شريط بين مفهومين. mode=becomes: «قبل/بعد» واللي قبل بيتحوّل فعلاً للي بعد (البذرة ← الإنبات). mode=needs: «أول/وبعدين»: الأول بيضل موجود، والثاني بيجي بعده لأنه بيحتاجه (الساق بيحتاج الجذر).",
                     "fields": {"target": "id (بعد / وبعدين)", "before": "id (قبل / أول)", "mode": "becomes أو needs",
                                "why": "ليش (من معنى المفهوم بالجراف) أو فاضي إذا الجراف ما بيحكي"}},
    "play": {"what": "🎞️ فيلم عملية حقيقية (سينما وبعدين الطالب بيعملها).",
             "fields": {"verb": "visit/carry/transform/combine/take_away/groups/share/cut/equivalent/compare/build/exchange/flow_river/write",
                        "target": "id", "actor": "مين بيعمل الحركة (مثلاً النحلة)", "with": "id اللي بيزوره/بيحمله", "result": "id النتيجة",
                        "example": "أرقام المثال (للرياضيات)", "drive": "جملة «دورك»"}},
    "slider": {"what": "🎚️ الشريط السحري: الأرقام بتتغير والصورة معها فوراً. من الصف الثامن: line (y = mx + b) · motion (d = v × t) · accel (v = a × t).",
               "fields": {"target": "id", "mode": "add/sub/mul/div/frac · line/motion/accel (صف ٨+)"}},
    "dialogue": {"what": "🗣️ حوار شخصيتين عن ليش وحدة بتحتاج الثانية.", "fields": {"target": "id", "with": "id", "lines": "[{who: id, say}]"}},
    "lens": {"what": "🔍 العدسة: المعلومات مخبّاية، والطالب بيكشفها بالماوس/الإصبع.", "fields": {"target": "id", "facts": "[نص]"}},
    # 🆕 batch 26: five more activities (one per concept). No points, no failing: a wrong move gets an explanation.
    "recipe": {"what": "🧪 الشروط (🆕 الدفعة ٣٦: «🍽️ أطعم X» للصغار): على الطاولة اللي بيحتاجه المفهوم + أشياء مش إله (decoys). الصح بياكله (سهم + السبب)، والغلط «يع!» ورجع مع السبب. بيكتمل بس لما ياكل الكل، وإذا شلت واحد بيرجع ناقص.",
               "fields": {"target": "id", "needs": "[{id, why}] (٢ أو أكثر)", "decoys": "[{id, why: «X ما بيحتاج Y»}] (اللي مش إله؛ ممكن تكون فاضية)", "ready": "جملة لما يكتملوا كلهم"}},
    "connect": {"what": "✏️ ارسم الأسهم: الطالب بيرسم أسهم «بيحتاج» بنفسه (سحب، أو كبسة على الاثنين بالترتيب). الصح بيضل مع السبب، والمقلوب بينشرح ليش.",
                "fields": {"target": "id", "nodes": "ids (المفهوم أول واحد)", "links": "[{from: اللي بيحتاج, to: اللي بيحتاجه, required, ok_say, rev_say}] (required=false: سهم صح زيادة بين الباقيين، بينقبل)",
                           "calm": "ids ما إلهم سهم مع المفهوم (ولا من خلال سلسلة)", "end_say": "جملة النهاية"}},
    "compare": {"what": "⚖️ قارن: مفهومين قريبين. كل بطاقة بتروح عند الأول، عند الثاني، أو «الاثنين». الغلط: «جرّب مكان ثاني»، وثاني غلطة البطاقة بتروح لمكانها مع السبب.",
                "fields": {"target": "id (a)", "other": "id (b)", "facts": "[{fact: نص البطاقة, side: a/b/both, type: def/need/feed, ref: id, why: الشرح}]", "end_say": "جملة النهاية"}},
    "teach": {"what": "🧑‍🏫 اشرح لزميلك: زميل مش فاهم بيسأل ٢–٣ أسئلة، والطالب بيختار الجواب. الغلط بيترد عليه بالسبب (هاد تعريف مفهوم ثاني · السهم بالعكس). بالآخر: الشرح اللي بناه.",
              "fields": {"target": "id", "rounds": "[{ask, rel: def/needs/needed_by, options:[{opt, id, ok, reply}]}]", "learnt": "الشرح كامل بالآخر"}},
    "ladder": {"what": "🪜 السلّم: «ليش؟» ورا «ليش؟»: كل جواب درجة أعمق لحد الأساس (mode=why). أو «وبعدين؟» للي بيجي بعده (mode=then). الأسهم دايماً من اللي بيحتاج. 🆕 الدفعة ٣٦: كل درجة اختيار (الصح + rungs[].wrong)، وإذا ما في غلط للدرجة بيرجع زر «ليش؟ / وبعدين؟».",
               "fields": {"target": "id", "mode": "why أو then", "rungs": "[{id, because: الجملة الكاملة, short: جملة قصيرة للفقاعة, wrong: [{id, say: ليش مش هي}]}]", "end_say": "جملة النهاية"}},
    "throw": {"what": "🪃 ارمي وطيّر (فكرة حارث): كرات عليها أسماء؛ الطالب بيسحب الكرة ويفلّتها لـ«target». اللي بيحتاجه بيلقطها (سهم + السبب)، وغيرها بترجع.",
              "fields": {"target": "id", "balls": "[{id, ok: صح/غلط, say: الجملة بعد الرمية}] (مخلوطين)", "win": "جملة لما يوصل كل الصح"}},
    "tower": {"what": "🏗️ ابني البرج: قطع السلسلة مخلوطة؛ كل قطعة بتقعد بس فوق اللي بتحتاجه. الغلط بتتهزّ وبتوقع.",
              "fields": {"target": "id (فوق البرج)", "blocks": "[{id, why}] من تحت لفوق (الترتيب الصح؛ اخلطوهم بالعرض)", "win": "جملة لما يكمل البرج"}},
    "magnet": {"what": "🧲 المغناطيس: «target» مغناطيس؛ اللي بيحتاجوه بينشدّوا وبيلزقوا فيه، والباقي بيضل مكانه.",
               "fields": {"target": "id", "items": "[{id, ok: بيحتاجه؟, say}]", "win": "جملة لما ينشدّوا كلهم"}},
    "machine": {"what": "⚙️ الآلة الخربانة: سلسلة أسنان ناقصها سن «target»؛ الطالب بيختار السن اللي بيركب، والآلة بتلف كلها.",
                "fields": {"target": "id", "route": "ids السلسلة بالترتيب", "gap": "رقم مكان السن الناقص بـ route", "options": "[{id, ok, say}]", "says": "جملة لكل وصلة بالسلسلة", "win": "جملة لما تشتغل"}},
    "power": {"what": "⚡ وصّل الطاقة: مفاتيح للمصادر؛ اللمبة بتضوي بس لما كل اللي بتحتاجه يضوي. في مفتاح «decoy» ما إله دخل.",
              "fields": {"target": "id (اللمبة الكبيرة)", "nodes": "ids اللمبات", "edges": "[[a,b]] يعني b بيحتاج a", "sources": "ids اللي إلها مفاتيح", "decoy": "id أو null", "says": "{id: جملة لما تضوي}", "win": "جملة لما يضوي target"}},
    # 🆕 batch 43: two more activities, for the concepts with FEW scenes (few arrows): they need only the name and the meaning. The student's (closed to the video).
    "who_am_i": {"what": "🕵️ مين أنا؟ شخصية مخبّاية ورا «؟» بتعطي أدلة (من معناها، وشو بتحتاج، ومين بيحتاجها)؛ الطالب بيختارها من ٣ بطاقات. البطاقة الغلط بتحكي هي شو، وبتفتح دليل جديد. نشاط للطالب.",
                 "fields": {"target": "id", "clues": "[{type: def/needs/needed_by, piece: رقم قطعة المعنى (def), ref: id (needs/needed_by), say: نص الدليل (اسم المفهوم مخفي «…»)}]",
                            "options": "[{id, ok, why: «مش أنا! Y: معناه» للغلط}] (الصح مرة وحدة)", "start": "كم دليل بيبين بالأول", "win": "جملة لما يحزّر"}},
    "sentence": {"what": "🧩 ركّب الجملة: معنى المفهوم مقطّع ٣–٤ قطع مخلوطة؛ الطالب بيكبسها بالترتيب لتطلع الجملة. الغلط بيتهزّ وبيقول «شو بيجي بعد…؟». نشاط للطالب.",
                 "fields": {"target": "id", "chunks": "[نص] بالترتيب الصح (اخلطوها بالعرض)", "sentence": "الجملة كاملة", "piece": "رقم قطعة المعنى (-1 = المعنى كله)", "win": "جملة لما تكمل"}},
    "custom": {"what": "🤖 مشهد كتبه الموديل بأدوات القالب (SDK) وانقبل من المعلم. بيشتغل بس جوا <iframe sandbox=\"allow-scripts\">. بيوصل بس مع include_llm=true.",
               "fields": {"target": "id", "scene_id": "id المشهد", "runner_url": "رابط صفحة الصندوق المعزول", "source": "llm", "provider": "مين كتبه (gemini/openai/claude)"}},
}

LESSON_FIELDS = {
    "lesson_id": "id الدرس", "lesson_title": "اسم الدرس", "overview": "مشهد الصورة الكبيرة", "world": "مشهد العالم (أو null)",
    "assemble": "🆕 مشهد «أجزاء الدرس» (أو null): نوعه بيتبدّل من درس لدرس: assemble · build_up · missing · tour", "concepts": "[{concept_id, title, scenes:[...], teach:{hook, answer, summary, recap}}]",
    "icons": "{concept_id: مفتاح الرسمة}", "art": "{concept_id: رابط الرسمة SVG}", "status": "needs_review = بانتظار مراجعة المعلم",
    "warnings": "مشاكل انكشفت (المشهد الغلط ما بيوصل)",
    "audience": "{grade, stage, label, persona} — المرحلة العمرية: kids (١–٤) · junior (٥–٧) · teen (٨–٩) · senior (١٠–١٢). الفرونت بيختار الشكل والأصوات منها، والكلام جاي جاهز للعمر",
}

STAGES = {"kids": "🌈 رفيق مرح: وجوه كاملة، ضحك، إيموجي، ألحان صغيرة · الفارة على الشخصية: بتضحك بصوتها هي",
          "junior": "🧭 مستكشف فضولي: وجوه بلا خدود، بلا ضحك، أصوات ناعمة · الفارة: بتميل وبتقول «همم؟»",
          "teen": "🔬 زميل واثق: عيون بس، «بيعتمد على»، نوتات قصيرة نظيفة، شكل دفتر مختبر · الفارة: بتضوي + اسمها ومعناها",
          "senior": "📐 خبير هادي: بلا وجوه، رسومات علمية رفيعة، بلا إيموجي، «نقاش»، شبه صامت · الفارة: اسمها ومعناها بلا صوت"}

SOUNDS = {"what": "🎵 الأصوات بتنعمل بالمتصفح (Web Audio)، بلا ملفات. المرحلة بتقرر قديش وكم عالي، والمادة بتقرر الآلة والسلّم الموسيقي، وما في نفس النوتة مرتين ورا بعض.",
          "subject_instrument": {"science": "ماريمبا", "math": "وتر مقروص", "physics": "بيانو كهربائي", "chemistry": "أجراس زجاج",
                                 "geography": "كاليمبا", "history": "خشب", "language": "ناي ناعم", "general": "جرس صغير"},
          "where": "03_explain_player_src/sound.js (الفرونت بقدر ياخذه زي ما هو)"}


def describe() -> dict:
    return {"relation": "edge [a, b] = «b بيحتاج a»", "common_fields": COMMON, "lesson_fields": LESSON_FIELDS, "scene_kinds": SCENE_KINDS, "stages": STAGES, "sounds": SOUNDS}
