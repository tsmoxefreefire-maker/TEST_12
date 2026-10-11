"""🆕 batch 43 · living things and their places (علم البيئة، والأحياء والعلوم): living and non-living factors, food levels and the
cycles of nitrogen, phosphorus and oxygen, the limiting factor, succession, water places (streams, wetlands, estuaries,
plankton), biodiversity and what threatens it (over-use, biomagnification, too many nutrients), sustainability and repair;
how animals behave (learned, habituation, imprinting, the two conditionings, aggression, ranks, territory, courtship);
relations (predation, parasitism, mutualism, commensalism); life's stages, the senses, plant groups, small creatures, and a few
science-book things (materials, properties, poles, the seasons' four days, temperature scales, ions, the periodic table's rows)."""
F = "eco"
SC = ["science"]
D = {
 # ---------- the environment ----------
 "biosphere": dict(words=["الغلاف الحيوي", "المحيط الحيوي"], anim="sun", face=(50, 50, .4), only=SC + ["social"],
   body='<circle cx="50" cy="50" r="46" fill="#9CD86C" opacity=".5"/><circle cx="50" cy="50" r="36" fill="#6CB8FF" {OL}/><path d="M26 34 C34 26 46 32 42 42 C38 50 26 46 26 34Z M56 52 C66 46 76 54 70 64 C64 72 54 66 56 52Z" fill="#6CC27A" {OL}/>'
        '<path d="M12 18 C16 12 22 12 24 18 M80 16 C84 10 90 12 90 18" fill="none" stroke="#3E8E4C" stroke-width="3" stroke-linecap="round"/><circle cx="86" cy="84" r="4" fill="#F6B73C" {OL}/>'),
 "biotic": dict(words=["العوامل الحيوية", "العوامل اللاحيوية", "العوامل الحيوية واللاحيوية", "مكونات النظام البيئي"], anim="sway", face=(26, 70, .32), only=SC,
   body='<path d="M50 4 L50 96" stroke="#AEB8C4" stroke-width="2" stroke-dasharray="4 3"/><path d="M26 60 L26 86 M26 70 C14 64 12 52 18 48 C26 50 28 60 26 70Z M26 66 C36 58 42 48 38 44 C30 46 26 56 26 66Z" fill="#6CC27A" {OL}/>'
        '<path d="M14 90 L38 90" stroke="#8B5E3C" stroke-width="4"/><circle cx="76" cy="22" r="10" fill="#FFD25A" {OL}/><path d="M62 54 C58 62 58 66 62 68 C66 66 66 62 62 54Z" fill="#7CC6F2" {OL}/><path d="M66 90 L72 74 L86 72 L94 90Z" fill="#9C8C7A" {OL}/>'),
 "trophic": dict(words=["المستوى الغذائي", "المستويات الغذائية", "هرم الطاقة", "الهرم الغذائي", "هرم الكتلة الحيوية"], anim="bob", face=(50, 78, .3), only=SC,
   body='<path d="M50 6 L64 30 L36 30Z" fill="#E8574A" {OL}/><path d="M36 30 L64 30 L76 52 L24 52Z" fill="#F6B73C" {OL}/><path d="M24 52 L76 52 L88 74 L12 74Z" fill="#9CD86C" {OL}/><path d="M12 74 L88 74 L98 94 L2 94Z" fill="#6CC27A" {OL}/>'),
 "nutrients": dict(words=["المغذيات", "العناصر المغذية", "خصوبة التربة", "الأسمدة"], anim="drip", face=(50, 80, .3), only=SC,
   body='<path d="M2 66 L98 66 L98 96 L2 96Z" fill="#8B5E3C" {OL}/><path d="M50 66 L50 36 M50 50 C38 44 34 34 40 30 C46 34 50 42 50 50Z M50 44 C62 38 66 28 60 24 C54 28 50 36 50 44Z" fill="#6CC27A" {OL}/>'
        '<text direction="ltr" x="18" y="24" font-size="14" font-weight="800" fill="#6CB8FF" font-family="sans-serif">N</text><text direction="ltr" x="70" y="20" font-size="14" font-weight="800" fill="#E8574A" font-family="sans-serif">P</text><text direction="ltr" x="82" y="44" font-size="14" font-weight="800" fill="#F6B73C" font-family="sans-serif">K</text>'),
 "nitrogen_cycle": dict(words=["دورة النيتروجين", "تثبيت النيتروجين", "البكتيريا المثبتة للنيتروجين", "العقد الجذرية"], anim="sun", face=(70, 30, .3), only=SC + ["environment"],
   body='<path d="M2 62 L98 62 L98 96 L2 96Z" fill="#8B5E3C" {OL}/><path d="M30 62 L30 30 M30 44 C20 38 18 28 24 26 C30 30 30 38 30 44Z" fill="#6CC27A" {OL}/><path d="M30 62 L24 82 M30 62 L36 84" stroke="#E6C08A" stroke-width="3"/>'
        '<circle cx="24" cy="80" r="4" fill="#F59BB8" {OL}/><circle cx="36" cy="82" r="4" fill="#F59BB8" {OL}/><text direction="ltr" x="70" y="36" text-anchor="middle" font-size="14" font-weight="800" fill="#3b2a1a" font-family="sans-serif">N₂</text>'
        '<path d="M58 44 C50 52 44 56 36 54 M80 46 C86 56 80 64 70 70" fill="none" stroke="#6CB8FF" stroke-width="3" stroke-linecap="round"/>'),
 "phosphorus_cycle": dict(words=["دورة الفوسفور", "الفوسفات"], anim="sun", face=(30, 80, .3), only=SC,
   body='<path d="M2 70 L36 46 L60 70Z" fill="#9C8C7A" {OL}/><path d="M2 70 L98 70 L98 96 L2 96Z" fill="#8B5E3C" {OL}/><path d="M80 70 L80 40 M80 52 C70 46 68 36 74 34 C80 38 80 46 80 52Z" fill="#6CC27A" {OL}/>'
        '<text direction="ltr" x="54" y="22" text-anchor="middle" font-size="16" font-weight="800" fill="#E8574A" font-family="sans-serif">P</text><path d="M40 44 C44 32 50 28 54 28 M66 28 C74 30 80 36 80 40" fill="none" stroke="#E8574A" stroke-width="3" stroke-linecap="round"/>'),
 "oxygen_cycle": dict(words=["دورة الأكسجين", "دورة الأكسجين وثاني أكسيد الكربون", "تبادل الغازات في الطبيعة"], anim="sun", face=(28, 60, .32), only=SC,
   body='<path d="M28 94 L28 60" stroke="#8B5E3C" stroke-width="6"/><circle cx="28" cy="46" r="22" fill="#6CC27A" {OL}/><path d="M64 94 C64 74 92 74 92 94Z" fill="#F7C9A4" {OL}/><circle cx="78" cy="62" r="10" fill="#F7C9A4" {OL}/>'
        '<path d="M48 30 C58 20 70 22 76 34 M70 30 L76 36 L80 28" fill="none" stroke="#6CB8FF" stroke-width="3"/><path d="M70 74 C60 84 48 82 46 72 M52 76 L46 70 L42 78" fill="none" stroke="#AEB8C4" stroke-width="3"/>'
        '<text direction="ltr" x="62" y="18" font-size="11" font-weight="800" fill="#2F6DB5" font-family="sans-serif">O₂</text><text direction="ltr" x="40" y="96" font-size="10" font-weight="800" fill="#5D646E" font-family="sans-serif">CO₂</text>'),
 "limiting": dict(words=["العامل المحدد", "العوامل المحددة", "القدرة الاستيعابية", "مدى التحمل"], anim="wobble", face=(50, 60, .36), only=SC,
   body='<path d="M20 30 L80 30 L76 94 L24 94Z" fill="#7CC6F2"/><path d="M20 10 L30 10 L30 94 L20 94Z M34 6 L44 6 L44 94 L34 94Z M48 52 L58 52 L58 94 L48 94Z M62 8 L72 8 L72 94 L62 94Z M74 12 L84 12 L82 94 L74 94Z" fill="#C98A55" {OL}/>'
        '<path d="M44 52 L62 52" stroke="#7CC6F2" stroke-width="3"/><path d="M48 52 C50 58 56 58 58 52" fill="none" stroke="#2F6DB5" stroke-width="3"/>'),
 "succession": dict(words=["التعاقب البيئي", "التعاقب الأولي", "التعاقب الثانوي", "المجتمع الذروة", "الأنواع الرائدة"], anim="sway", face=(80, 40, .3), only=SC + ["environment"],
   body='<path d="M2 80 L98 80 L98 96 L2 96Z" fill="#8B5E3C" {OL}/><path d="M6 80 L14 70 L22 80Z" fill="#9C8C7A" {OL}/><circle cx="16" cy="70" r="3" fill="#C9C35A"/>'
        '<path d="M32 80 L34 70 M38 80 L38 66 M44 80 L42 70" stroke="#6CC27A" stroke-width="3" stroke-linecap="round"/><path d="M60 80 L60 60" stroke="#8B5E3C" stroke-width="4"/><circle cx="60" cy="54" r="10" fill="#6CC27A" {OL}/>'
        '<path d="M80 80 L80 52" stroke="#8B5E3C" stroke-width="6"/><circle cx="80" cy="38" r="16" fill="#3E8E4C" {OL}/><path d="M24 50 L32 50 M28 46 L32 50 L28 54 M66 30 L74 30 M70 26 L74 30 L70 34" fill="none" stroke="#3b2a1a" stroke-width="2.4"/>'),
 "plankton": dict(words=["العوالق", "العوالق النباتية", "العوالق الحيوانية", "البلانكتون"], anim="wiggle", face=(50, 50, .36), only=SC,
   body='<circle cx="50" cy="50" r="46" fill="#BFE3F2" {OL}/><circle cx="50" cy="50" r="14" fill="#9CD86C" {OL}/><path d="M50 36 L50 24 M50 64 L50 76 M36 50 L24 50 M64 50 L76 50" stroke="#5A9A3A" stroke-width="3" stroke-linecap="round"/>'
        '<ellipse cx="24" cy="26" rx="8" ry="4" fill="#F6B73C" {OL}/><ellipse cx="76" cy="74" rx="6" ry="3" fill="#F6B73C" {OL}/><circle cx="76" cy="26" r="4" fill="#6CC27A" {OL}/><circle cx="24" cy="76" r="4" fill="#6CC27A" {OL}/>'),
 "stream": dict(words=["الأنهار والجداول", "الجداول", "الجدول المائي", "المياه العذبة الجارية"], anim="sway", face=(50, 50, .34), only=SC,
   body='<path d="M2 2 L98 2 L98 98 L2 98Z" fill="#9CD86C" {OL}/><path d="M30 2 C40 30 20 50 40 70 C50 82 60 90 62 98 L82 98 C78 82 66 74 60 62 C48 44 66 24 54 2Z" fill="#7CC6F2" {OL}/>'
        '<circle cx="76" cy="30" r="5" fill="#9C8C7A" {OL}/><circle cx="16" cy="70" r="6" fill="#9C8C7A" {OL}/>'),
 "wetland": dict(words=["الأراضي الرطبة", "المستنقعات", "الأهوار"], anim="sway", face=(50, 80, .3), only=SC,
   body='<rect x="2" y="2" width="96" height="60" fill="#E8F6FF"/><path d="M2 62 C20 56 40 66 60 60 C76 56 88 62 98 60 L98 98 L2 98Z" fill="#7CA88A" {OL}/>'
        '<path d="M20 70 L20 30 M30 72 L32 36 M74 70 L74 34 M84 72 L82 40" stroke="#5A8A3A" stroke-width="3" stroke-linecap="round"/><ellipse cx="20" cy="30" rx="3" ry="8" fill="#8B5E3C"/><ellipse cx="74" cy="34" rx="3" ry="8" fill="#8B5E3C"/>'),
 "estuary": dict(words=["مصبات الأنهار", "مصب النهر", "دلتا النهر", "المصبات"], anim="sway", face=(30, 30, .3), only=SC + ["social"],
   body='<rect x="2" y="2" width="96" height="96" rx="8" fill="#9CD86C" {OL}/><path d="M20 2 C26 20 30 36 40 50 C50 64 54 80 50 98 L98 98 L98 60 C80 66 68 56 62 44 C56 32 46 20 40 2Z" fill="#7CC6F2"/>'
        '<path d="M48 70 C58 74 70 70 80 78 M54 84 C64 86 74 84 86 92" fill="none" stroke="#C9A27A" stroke-width="3"/><rect x="2" y="2" width="96" height="96" rx="8" fill="none" {OL}/>'),
 "biodiversity": dict(words=["التنوع الحيوي", "التنوع البيولوجي", "قيمة التنوع الحيوي", "التنوع الوراثي", "تنوع الأنواع", "التنوع"], anim="bounce", face=(50, 50, .34), only=SC,
   body='<circle cx="50" cy="50" r="46" fill="#E6F4D8" {OL}/><path d="M20 40 C20 30 34 30 34 40 C34 48 20 48 20 40Z" fill="#F6B73C" {OL}/><circle cx="70" cy="28" r="8" fill="#E8574A" {OL}/>'
        '<path d="M66 64 C70 56 86 58 84 68 C80 76 66 72 66 64Z" fill="#6CB8FF" {OL}/><path d="M26 76 L26 60 M26 66 C18 62 18 56 22 54 C26 56 26 62 26 66Z" fill="#6CC27A" {OL}/><circle cx="48" cy="80" r="4" fill="#B0A8C9" {OL}/>'),
 "overuse": dict(words=["الاستغلال الجائر", "الصيد الجائر", "الرعي الجائر", "إزالة الغابات", "قطع الأشجار"], anim="wobble", face=(30, 70, .32), only=SC + ["social", "environment"],
   body='<path d="M2 86 L98 86" stroke="#8B5E3C" stroke-width="6"/><rect x="18" y="70" width="22" height="16" fill="#C98A55" {OL}/><ellipse cx="29" cy="70" rx="11" ry="4" fill="#E6C08A" {OL}/>'
        '<rect x="56" y="60" width="16" height="26" fill="#C98A55" {OL}/><ellipse cx="64" cy="60" rx="8" ry="3" fill="#E6C08A" {OL}/><path d="M78 20 L94 36 L74 56 L58 40Z" fill="#AEB8C4" {OL}/><path d="M58 40 L40 58" stroke="#8B5E3C" stroke-width="6" stroke-linecap="round"/>'),
 "edge_effect": dict(words=["تأثير الحافة", "حافة الغابة", "التجزئة البيئية"], anim="sway", face=(70, 80, .3), only=SC,
   body='<rect x="2" y="2" width="96" height="96" rx="8" fill="#E6F4D8" {OL}/><path d="M2 2 L50 2 C44 30 56 60 46 98 L2 98Z" fill="#3E8E4C"/><circle cx="16" cy="20" r="8" fill="#5AAE5A"/><circle cx="30" cy="50" r="9" fill="#5AAE5A"/><circle cx="18" cy="80" r="8" fill="#5AAE5A"/>'
        '<path d="M50 2 C44 30 56 60 46 98" fill="none" stroke="#F6B73C" stroke-width="4" stroke-dasharray="5 4"/><rect x="2" y="2" width="96" height="96" rx="8" fill="none" {OL}/>'),
 "biomagnification": dict(words=["التضخم الحيوي", "التراكم الحيوي", "تراكم المبيدات", "تلوث السلسلة الغذائية"], anim="bounce", face=(80, 30, .3), only=SC,
   body='<ellipse cx="14" cy="80" rx="10" ry="5" fill="#9CD86C" {OL}/><circle cx="14" cy="80" r="1.6" fill="#E8574A"/><path d="M28 74 C34 64 50 64 54 74 C50 84 34 84 28 74Z" fill="#6CB8FF" {OL}/><circle cx="40" cy="72" r="1.8" fill="#E8574A"/><circle cx="44" cy="76" r="1.8" fill="#E8574A"/>'
        '<path d="M58 50 C66 34 92 34 96 50 C92 66 66 66 58 50Z" fill="#4A90D9" {OL}/><circle cx="72" cy="46" r="2" fill="#E8574A"/><circle cx="78" cy="52" r="2" fill="#E8574A"/><circle cx="84" cy="46" r="2" fill="#E8574A"/><circle cx="70" cy="54" r="2" fill="#E8574A"/>'
        '<path d="M22 66 L26 62 M54 60 L58 56" stroke="#3b2a1a" stroke-width="2.4"/>'),
 "eutrophication": dict(words=["الإثراء الغذائي", "ازدهار الطحالب", "المد الأحمر"], anim="drip", face=(50, 50, .34), only=SC,
   body='<ellipse cx="50" cy="60" rx="46" ry="30" fill="#7CA88A" {OL}/><path d="M14 54 C24 46 34 58 44 50 C54 42 64 56 76 48 C82 44 88 50 90 54" fill="none" stroke="#5A9A3A" stroke-width="5" stroke-linecap="round"/>'
        '<circle cx="30" cy="70" r="3" fill="#5A9A3A"/><circle cx="62" cy="72" r="3" fill="#5A9A3A"/><path d="M76 8 L76 28 M70 22 L76 30 L82 22" fill="none" stroke="#3b2a1a" stroke-width="3"/><text direction="ltr" x="62" y="16" font-size="10" font-weight="800" fill="#3b2a1a" font-family="sans-serif">N P</text>'),
 "restoration": dict(words=["الاستعادة الحيوية", "المعالجة الحيوية", "إعادة التأهيل البيئي", "التشجير"], anim="sway", face=(50, 76, .32), only=SC + ["social", "environment"],
   body='<path d="M2 70 L98 70 L98 96 L2 96Z" fill="#8B5E3C" {OL}/><path d="M50 70 L50 30 M50 46 C36 40 32 28 38 24 C46 28 50 38 50 46Z M50 40 C64 34 68 22 62 18 C54 22 50 30 50 40Z" fill="#6CC27A" {OL}/>'
        '<path d="M14 78 C18 74 22 82 26 78 M70 82 C74 78 78 86 82 82" fill="none" stroke="#3b2a1a" stroke-width="2"/><path d="M78 30 L84 18 L90 30 M84 18 L84 40" fill="none" stroke="#6CB8FF" stroke-width="3"/>'),
 "sustainability2": dict(words=["الاستدامة", "الاستدامة البيئية"], anim="sun", face=(50, 50, .36),
   body='<path d="M50 8 C76 8 92 28 92 50 L80 50 M50 92 C24 92 8 72 8 50 L20 50" fill="none" stroke="#6CC27A" stroke-width="7" stroke-linecap="round"/><path d="M74 42 L80 52 L88 42 M26 58 L20 48 L12 58" fill="none" stroke="#6CC27A" stroke-width="5" stroke-linecap="round"/>'
        '<path d="M50 70 C30 64 28 44 40 32 C50 24 66 30 66 46 C66 58 58 66 50 70Z" fill="#9CD86C" {OL}/><path d="M50 70 L58 42" stroke="#3E8E4C" stroke-width="3"/>'),
 # ---------- how animals behave ----------
 "behavior": dict(words=["السلوك الحيواني", "السلوك المكتسب", "السلوك الفطري", "سلوك الحيوان"], anim="bounce", face=(40, 50, .38), only=SC,
   body='<path d="M14 70 C10 46 30 30 50 34 C66 36 78 50 74 64 L80 64 L84 56 L90 60 L86 70 L78 76 C70 86 30 88 14 70Z" fill="#C98A55" {OL}/>'
        '<path d="M24 74 L22 90 M40 80 L40 94 M58 80 L58 94 M70 74 L72 90" stroke="#3b2a1a" stroke-width="4" stroke-linecap="round"/><path d="M84 20 C90 26 90 34 84 40 M74 14 C84 22 84 38 74 46" fill="none" stroke="#6CB8FF" stroke-width="3" stroke-linecap="round"/>'),
 "habituation": dict(words=["التعود", "الاعتياد"], anim="sway", face=(30, 62, .3), only=SC,
   body='<path d="M2 86 L98 86" stroke="#6CC27A" stroke-width="6"/><path d="M50 86 L50 26 M30 40 L70 40" stroke="#8B5E3C" stroke-width="5"/><circle cx="50" cy="18" r="10" fill="#F2D07A" {OL}/>'
        '<path d="M14 70 C14 58 40 58 40 70 C40 78 14 78 14 70Z" fill="#AEB8C4" {OL}/><path d="M36 60 L44 54" stroke="#3b2a1a" stroke-width="2.4"/><path d="M74 70 C74 62 88 62 88 70 C88 76 74 76 74 70Z" fill="#AEB8C4" {OL}/>'),
 "imprinting": dict(words=["الطبع", "البصم", "التطبع"], anim="bounce", face=(26, 50, .32), only=SC,
   body='<path d="M8 60 C8 40 40 36 46 56 C50 70 36 80 22 78 C12 76 8 70 8 60Z" fill="#fff" {OL}/><circle cx="34" cy="44" r="10" fill="#fff" {OL}/><path d="M42 44 L52 46 L42 50Z" fill="#F6B73C" {OL}/>'
        '<path d="M60 76 C60 66 74 64 76 74 C78 82 62 84 60 76Z M80 82 C80 74 92 72 94 80 C96 88 82 90 80 82Z" fill="#FFD25A" {OL}/><path d="M2 92 L98 92" stroke="#6CC27A" stroke-width="4"/>'),
 "classical": dict(words=["الاشتراط الكلاسيكي", "الاشتراط", "التعلم الشرطي"], anim="buzz", face=(70, 70, .3), only=SC,
   body='<path d="M20 50 C20 26 46 26 46 50 L50 62 L16 62Z" fill="#F6B73C" {OL}/><circle cx="33" cy="68" r="5" fill="#C98A55" {OL}/><path d="M52 34 C56 38 56 46 52 50" fill="none" stroke="#3b2a1a" stroke-width="2.4"/>'
        '<path d="M58 86 L94 86 L88 72 L64 72Z" fill="#E8574A" {OL}/><circle cx="72" cy="76" r="3" fill="#C98A55"/><circle cx="80" cy="78" r="3" fill="#C98A55"/>'),
 "operant": dict(words=["الاشتراط الإجرائي", "التعلم بالمحاولة والخطأ", "التعزيز"], anim="bounce", face=(64, 40, .3), only=SC,
   body='<rect x="6" y="10" width="88" height="80" rx="6" fill="#E8F2F8" {OL}/><rect x="14" y="40" width="14" height="6" fill="#5D646E" {OL}/><path d="M21 40 L26 28" stroke="#5D646E" stroke-width="3"/>'
        '<path d="M44 70 C44 54 76 54 78 66 L86 66 L84 74 L76 76 C66 84 46 82 44 70Z" fill="#AEB8C4" {OL}/><circle cx="24" cy="80" r="4" fill="#C98A55" {OL}/><path d="M24 50 L24 72" stroke="#3b2a1a" stroke-width="2" stroke-dasharray="3 3"/>'),
 "aggression": dict(words=["السلوك العدواني", "العدوانية عند الحيوانات"], anim="wobble", face=(24, 50, .3), only=SC,
   body='<path d="M4 70 C4 50 30 44 42 56 L46 50 L48 62 L40 72 C30 82 8 82 4 70Z" fill="#C98A55" {OL}/><path d="M96 70 C96 50 70 44 58 56 L54 50 L52 62 L60 72 C70 82 92 82 96 70Z" fill="#9C8C7A" {OL}/>'
        '<path d="M46 30 L50 40 L54 30 M42 36 L50 42 L58 36" fill="none" stroke="#E8574A" stroke-width="3" stroke-linecap="round"/>'),
 "hierarchy": dict(words=["التسلسل الهرمي", "التدرج الهرمي", "ترتيب السيطرة"], anim="bounce", face=(50, 20, .3), only=SC,
   body='<rect x="38" y="28" width="24" height="16" fill="#FFD25A" {OL}/><rect x="24" y="52" width="52" height="16" fill="#F6B73C" {OL}/><rect x="8" y="76" width="84" height="16" fill="#C98A55" {OL}/>'
        '<circle cx="50" cy="18" r="9" fill="#E8574A" {OL}/><circle cx="36" cy="44" r="6" fill="#AEB8C4" {OL}/><circle cx="64" cy="44" r="6" fill="#AEB8C4" {OL}/>'),
 "territory": dict(words=["السلوك الإقليمي", "الإقليمية", "حماية المنطقة"], anim="sway", face=(50, 56, .32), only=SC,
   body='<ellipse cx="50" cy="60" rx="46" ry="34" fill="#E6F4D8" stroke="#E8574A" stroke-width="3" stroke-dasharray="6 4"/><path d="M30 64 C30 48 64 46 68 60 L76 60 L74 68 L66 70 C56 80 32 78 30 64Z" fill="#C98A55" {OL}/>'
        '<path d="M84 22 L84 6 L96 12 L84 18" fill="#E8574A" {OL}/>'),
 "courtship": dict(words=["سلوك التودد", "التودد", "طقوس التزاوج عند الطيور"], anim="bounce", face=(24, 56, .3), only=SC,
   body='<path d="M8 70 C8 50 34 44 40 60 C44 72 30 82 18 80 C10 78 8 74 8 70Z" fill="#6CB8FF" {OL}/><circle cx="30" cy="46" r="9" fill="#6CB8FF" {OL}/><path d="M38 46 L46 48 L38 50Z" fill="#F6B73C"/>'
        '<path d="M92 70 C92 50 66 44 60 60 C56 72 70 82 82 80 C90 78 92 74 92 70Z" fill="#F59BB8" {OL}/><circle cx="70" cy="46" r="9" fill="#F59BB8" {OL}/><path d="M62 46 L54 48 L62 50Z" fill="#F6B73C"/>'
        '<path d="M50 30 C46 24 40 28 44 34 L50 40 L56 34 C60 28 54 24 50 30Z" fill="#E8574A" {OL}/>'),
 # ---------- relations between living things ----------
 "predation": dict(words=["الافتراس", "المفترس والفريسة", "العلاقة بين المفترس والفريسة"], anim="bounce", face=(28, 54, .32), only=SC,
   body='<path d="M4 66 C4 44 34 38 46 52 L54 46 L56 58 L48 70 C38 82 8 82 4 66Z" fill="#F6A23C" {OL}/><path d="M12 46 L16 36 L22 46 M28 44 L32 34 L38 44" fill="#F6A23C" {OL}/>'
        '<path d="M70 70 C68 58 82 54 90 62 C96 68 92 80 82 80 C76 80 70 76 70 70Z" fill="#E8F2F8" {OL}/><path d="M80 56 L76 40 M86 56 L90 40" stroke="#3b2a1a" stroke-width="5" stroke-linecap="round"/>'),
 "parasitism": dict(words=["التطفل", "الطفيليات", "الطفيل والعائل"], anim="wiggle", face=(40, 50, .36), only=SC,
   body='<path d="M4 90 C4 50 30 30 60 34 C80 36 96 54 96 90Z" fill="#C98A55" {OL}/><ellipse cx="62" cy="44" rx="12" ry="9" fill="#5D3A1A" {OL}/><path d="M52 40 L44 36 M52 48 L44 52 M72 40 L80 36 M72 48 L80 52" stroke="#3b2a1a" stroke-width="2.4"/>'),
 "mutualism": dict(words=["تبادل المنفعة", "التكافل", "المنفعة المتبادلة"], anim="bounce", face=(26, 66, .32), only=SC,
   body='<path d="M26 94 L26 56" stroke="#5A9A3A" stroke-width="4"/><circle cx="26" cy="42" r="10" fill="#FFD25A" {OL}/><path d="M26 22 C34 22 34 32 26 32 C18 32 18 22 26 22Z M40 42 C40 50 30 50 30 42 M12 42 C12 34 22 34 22 42" fill="#F59BB8" {OL}/>'
        '<ellipse cx="72" cy="40" rx="14" ry="10" fill="#FFD25A" {OL}/><path d="M64 36 L80 36 M64 44 L80 44" stroke="#3b2a1a" stroke-width="3"/><path d="M68 30 C62 18 74 16 74 30 M76 30 C82 18 90 24 80 32" fill="#E8F6FF" {OL}/>'
        '<path d="M50 60 C46 54 40 58 44 64 L50 70 L56 64 C60 58 54 54 50 60Z" fill="#E8574A" {OL}/>'),
 "commensalism": dict(words=["التعايش", "المعايشة", "التطاعم"], anim="sway", face=(70, 60, .3), only=SC,
   body='<rect x="2" y="2" width="96" height="96" rx="8" fill="#7CC6F2" {OL}/><path d="M10 96 L18 60 L24 96 M28 96 L36 54 L44 96 M50 96 L56 62 L62 96" fill="#F59BB8" {OL}/>'
        '<path d="M56 60 C62 46 86 46 90 60 C86 74 62 74 56 60Z" fill="#F6A23C" {OL}/><path d="M64 50 L64 70 M76 48 L76 72" stroke="#fff" stroke-width="4"/>'),
 # ---------- life's stages and the senses ----------
 "childhood": dict(words=["الطفولة", "مرحلة الطفولة"], anim="bounce", face=(50, 40, .42),
   body='<circle cx="50" cy="40" r="26" fill="#F7C9A4" {OL}/><path d="M24 96 C24 70 76 70 76 96Z" fill="#9FD8F0" {OL}/><path d="M42 16 C46 10 54 10 56 16" fill="none" stroke="#8B5E3C" stroke-width="3"/>'),
 "teenage": dict(words=["المراهقة", "مرحلة المراهقة", "البلوغ", "التغيرات في مرحلة المراهقة"], anim="bob", face=(50, 32, .4),
   body='<circle cx="50" cy="32" r="20" fill="#F7C9A4" {OL}/><path d="M30 26 C32 10 68 10 70 26 C62 18 40 18 30 26Z" fill="#5D3A1A" {OL}/><path d="M22 96 C22 62 78 62 78 96Z" fill="#6CC27A" {OL}/><path d="M80 20 L92 8 M84 20 L92 20 M92 8 L92 20" fill="none" stroke="#F6B73C" stroke-width="3"/>'),
 "old_age": dict(words=["الشيخوخة", "مرحلة الشيخوخة", "كبار السن", "المسنون"], anim="sway", face=(46, 30, .38),
   body='<circle cx="46" cy="30" r="20" fill="#F7C9A4" {OL}/><path d="M28 24 C30 10 62 10 64 24" fill="none" stroke="#E8F2F8" stroke-width="8" stroke-linecap="round"/><path d="M20 96 C20 64 72 64 72 96Z" fill="#B0A8C9" {OL}/>'
        '<path d="M82 96 L82 60 C82 50 92 50 92 58" fill="none" stroke="#8B5E3C" stroke-width="5" stroke-linecap="round"/>'),
 "senses": dict(words=["الإحساس"], anim="bob", face=None, only=SC,
   body='<circle cx="50" cy="50" r="44" fill="#F7C9A4" {OL}/><circle cx="34" cy="40" r="7" fill="#fff" {OL}/><circle cx="66" cy="40" r="7" fill="#fff" {OL}/><circle cx="34" cy="40" r="3" fill="#3b2a1a"/><circle cx="66" cy="40" r="3" fill="#3b2a1a"/>'
        '<path d="M50 46 L46 60 L54 60" fill="none" stroke="#C98A55" stroke-width="3"/><path d="M38 72 C44 78 56 78 62 72" fill="none" stroke="#E8574A" stroke-width="4" stroke-linecap="round"/><path d="M6 44 C0 50 0 58 6 62 M94 44 C100 50 100 58 94 62" fill="none" stroke="#C98A55" stroke-width="4"/>'),
 "response": dict(words=["الاستجابة للمثيرات", "المنبهات"], anim="sway", face=(36, 70, .32), only=SC,
   body='<circle cx="84" cy="16" r="12" fill="#FFD25A" {OL}/><path d="M24 74 L76 74 L70 96 L30 96Z" fill="#C98A55" {OL}/><path d="M50 74 C50 54 56 40 70 28" fill="none" stroke="#5A9A3A" stroke-width="5" stroke-linecap="round"/>'
        '<path d="M66 32 C58 24 62 14 70 14 C74 20 72 28 66 32Z" fill="#6CC27A" {OL}/><path d="M52 52 C42 48 40 40 44 36 C50 40 52 46 52 52Z" fill="#6CC27A" {OL}/><path d="M72 22 L78 20" stroke="#F6B73C" stroke-width="2" stroke-dasharray="2 2"/>'),
 "herbivore": dict(words=["آكلات الأعشاب", "آكل الأعشاب", "الحيوانات العاشبة"], anim="bounce", face=(46, 46, .36),
   body='<ellipse cx="46" cy="56" rx="28" ry="22" fill="#E8F2F8" {OL}/><ellipse cx="38" cy="22" rx="6" ry="18" fill="#E8F2F8" {OL} transform="rotate(-10 38 22)"/><ellipse cx="54" cy="22" rx="6" ry="18" fill="#E8F2F8" {OL} transform="rotate(10 54 22)"/>'
        '<path d="M70 94 L74 70 M80 94 L80 66 M88 94 L86 72" stroke="#6CC27A" stroke-width="4" stroke-linecap="round"/><path d="M2 94 L98 94" stroke="#6CC27A" stroke-width="4"/>'),
 "levels_org": dict(words=["مستويات التنظيم", "مستويات التنظيم في الكائن الحي", "الخلية والنسيج والعضو"], anim="bounce", face=(84, 50, .3), only=SC,
   body='<circle cx="12" cy="50" r="8" fill="#9CD86C" {OL}/><circle cx="12" cy="50" r="3" fill="#3E8E4C"/><path d="M22 50 L28 50" stroke="#3b2a1a" stroke-width="2"/>'
        '<rect x="30" y="38" width="22" height="24" rx="4" fill="#9CD86C" {OL}/><path d="M37 38 L37 62 M45 38 L45 62 M30 50 L52 50" stroke="#3E8E4C" stroke-width="1.4"/><path d="M54 50 L60 50" stroke="#3b2a1a" stroke-width="2"/>'
        '<path d="M84 70 C64 58 60 44 66 38 C72 32 80 36 84 44 C88 36 96 32 100 40" fill="#E8574A" {OL}/>'),
 # ---------- plant groups and small creatures ----------
 "vascular": dict(words=["النباتات الوعائية", "النباتات الوعائية اللابذرية", "النباتات البذرية", "الأوعية الناقلة"], anim="sway", face=(50, 74, .3), only=SC,
   body='<path d="M50 96 L50 20" stroke="#5A9A3A" stroke-width="8" stroke-linecap="round"/><path d="M48 96 L48 20" stroke="#6CB8FF" stroke-width="2"/><path d="M52 96 L52 20" stroke="#E8853C" stroke-width="2"/>'
        '<path d="M50 40 C34 32 26 20 30 12 C42 14 50 26 50 40Z M50 56 C66 48 74 36 70 28 C58 30 50 42 50 56Z" fill="#6CC27A" {OL}/>'),
 "plant_lifespan": dict(words=["النباتات الحولية وثنائية الحول والمعمرة", "النباتات الحولية", "النباتات المعمرة", "النباتات ثنائية الحول"], anim="sway", face=(78, 80, .3), only=SC,
   body='<path d="M2 90 L98 90" stroke="#8B5E3C" stroke-width="5"/><path d="M14 90 L14 70 M14 76 C8 72 8 66 12 64 C16 68 14 72 14 76Z" fill="#6CC27A" {OL}/><circle cx="14" cy="64" r="3" fill="#F59BB8"/>'
        '<path d="M40 90 L40 60 M40 68 C30 62 30 54 36 52 C42 56 40 62 40 68Z M40 64 C50 58 50 50 44 48 C38 52 40 58 40 64Z" fill="#6CC27A" {OL}/><path d="M78 90 L78 50" stroke="#8B5E3C" stroke-width="6"/><circle cx="78" cy="38" r="18" fill="#3E8E4C" {OL}/>'
        '<text direction="ltr" x="14" y="18" text-anchor="middle" font-size="12" font-weight="800" fill="#3b2a1a" font-family="sans-serif">1</text><text direction="ltr" x="40" y="18" text-anchor="middle" font-size="12" font-weight="800" fill="#3b2a1a" font-family="sans-serif">2</text><text direction="ltr" x="78" y="14" text-anchor="middle" font-size="12" font-weight="800" fill="#3b2a1a" font-family="sans-serif">∞</text>'),
 "lichen": dict(words=["الأشنات", "الأشنة"], anim="sway", face=(50, 60, .36),
   body='<path d="M6 80 L14 44 L44 26 L80 34 L94 66 L78 92 L22 92Z" fill="#9C8C7A" {OL}/><circle cx="34" cy="48" r="10" fill="#C9C35A" {OL}/><circle cx="62" cy="44" r="8" fill="#9CB85A" {OL}/>'
        '<circle cx="70" cy="70" r="10" fill="#C9C35A" {OL}/><circle cx="36" cy="74" r="7" fill="#E8A85A" {OL}/>'),
 "cilia": dict(words=["الأهداب", "الأهداب والأسواط"], anim="wiggle", face=(50, 50, .36),
   body='<ellipse cx="50" cy="50" rx="34" ry="20" fill="#BFE3F2" {OL} transform="rotate(-20 50 50)"/>'
        '<path d="M18 50 L8 46 M22 38 L14 30 M34 30 L30 20 M48 26 L48 16 M62 26 L66 16 M76 34 L86 28 M82 50 L92 54 M78 62 L88 70 M66 70 L70 80 M52 74 L52 84 M38 74 L34 84 M26 66 L16 72" stroke="#3b2a1a" stroke-width="2"/>'),
 "conjugation": dict(words=["الاقتران البكتيري"], anim="wiggle", face=(24, 50, .3), only=["science", "biology"],
   body='<ellipse cx="24" cy="50" rx="20" ry="12" fill="#9CD86C" {OL}/><ellipse cx="76" cy="50" rx="20" ry="12" fill="#9CD86C" {OL}/><path d="M44 50 L56 50" stroke="#3E8E4C" stroke-width="5"/>'
        '<circle cx="70" cy="50" r="5" fill="none" stroke="#E8574A" stroke-width="2.4"/><circle cx="20" cy="50" r="5" fill="none" stroke="#E8574A" stroke-width="2.4"/>'),
 "plasmodium": dict(words=["البلازموديوم", "الملاريا", "طفيل الملاريا"], anim="wiggle", face=(50, 50, .36),
   body='<circle cx="50" cy="50" r="40" fill="#E8574A" {OL}/><circle cx="50" cy="50" r="24" fill="#F28A80"/><path d="M40 40 C48 32 60 40 56 50 C52 60 40 58 42 50" fill="none" stroke="#B0A8C9" stroke-width="6" stroke-linecap="round"/>'
        '<circle cx="42" cy="50" r="4" fill="#6E4A9E"/>'),
 "diatom": dict(words=["الدياتومات", "الطحالب الذهبية", "الدياتوم"], anim="sun", face=(50, 50, .36),
   body='<ellipse cx="50" cy="50" rx="44" ry="26" fill="#E8D86A" {OL}/><ellipse cx="50" cy="50" rx="34" ry="18" fill="none" stroke="#B5A83A" stroke-width="2"/>'
        '<path d="M16 50 L84 50 M24 38 L24 62 M34 34 L34 66 M44 32 L44 68 M56 32 L56 68 M66 34 L66 66 M76 38 L76 62" stroke="#B5A83A" stroke-width="1.6"/>'),
 "chitin": dict(words=["الكايتين", "الانسلاخ"], anim="bounce", face=(50, 46, .34),
   body='<ellipse cx="50" cy="50" rx="18" ry="34" fill="#8B5E3C" {OL}/><path d="M34 34 L66 34 M32 50 L68 50 M34 66 L66 66" stroke="#5D3A1A" stroke-width="3"/>'
        '<path d="M32 40 L10 30 M32 54 L8 56 M34 68 L12 82 M68 40 L90 30 M68 54 L92 56 M66 68 L88 82" stroke="#3b2a1a" stroke-width="3" stroke-linecap="round"/><path d="M44 16 L38 4 M56 16 L62 4" stroke="#3b2a1a" stroke-width="2.4"/>'),
 "segmented": dict(words=["التقطع", "الحيوانات المقسمة", "التجزؤ", "القطع الطرفية"], anim="wiggle", face=(84, 50, .3),
   body='<circle cx="14" cy="56" r="10" fill="#F59BB8" {OL}/><circle cx="30" cy="50" r="10" fill="#F59BB8" {OL}/><circle cx="46" cy="46" r="10" fill="#F59BB8" {OL}/><circle cx="62" cy="46" r="10" fill="#F59BB8" {OL}/><circle cx="80" cy="50" r="12" fill="#F28AA8" {OL}/>'),
 "body_cavity": dict(words=["تجاويف الجسم", "عديمة التجويف الجسمي", "ذات التجويف الجسمي الكاذب", "ذات التجويف الجسمي الحقيقي", "التجويف الجسمي الكاذب", "التجويف الجسمي"], anim="bob", face=(50, 50, .3),
   body='<circle cx="50" cy="50" r="44" fill="#F59BB8" {OL}/><circle cx="50" cy="50" r="30" fill="#FFF0D0" {OL}/><circle cx="50" cy="50" r="14" fill="#F6B73C" {OL}/><path d="M6 50 L20 50 M80 50 L94 50" stroke="#3b2a1a" stroke-width="1.6"/>'),
 "spines": dict(words=["الأشواك", "قنفذ البحر", "الشوك"], anim="wobble", face=(50, 56, .36),
   body='<circle cx="50" cy="56" r="26" fill="#8E5BB5" {OL}/><path d="M50 30 L50 6 M30 38 L12 22 M70 38 L88 22 M24 56 L2 56 M76 56 L98 56 M30 76 L14 92 M70 76 L86 92 M40 30 L32 8 M60 30 L68 8" stroke="#6E4A9E" stroke-width="3" stroke-linecap="round"/>'),
 "sieve_plate": dict(words=["الصفيحة المنخلية", "الأنابيب الغربالية", "اللحاء"], anim="bob", face=(50, 80, .3),
   body='<rect x="30" y="4" width="40" height="92" rx="6" fill="#9CD86C" {OL}/><ellipse cx="50" cy="50" rx="20" ry="6" fill="#fff" {OL}/><circle cx="42" cy="50" r="1.6" fill="#3b2a1a"/><circle cx="50" cy="48" r="1.6" fill="#3b2a1a"/><circle cx="58" cy="50" r="1.6" fill="#3b2a1a"/><circle cx="50" cy="52" r="1.6" fill="#3b2a1a"/>'
        '<path d="M50 14 L50 38 M44 32 L50 40 L56 32" fill="none" stroke="#E8853C" stroke-width="3"/>'),
 # ---------- things of the science books ----------
 "wood": dict(words=["الأخشاب", "الخشب", "المواد الخشبية"], anim="wobble", face=(50, 50, .4),
   body='<rect x="6" y="20" width="88" height="20" rx="4" fill="#C98A55" {OL}/><rect x="6" y="40" width="88" height="20" rx="4" fill="#B5733F" {OL}/><rect x="6" y="60" width="88" height="20" rx="4" fill="#C98A55" {OL}/>'
        '<path d="M16 30 C30 26 40 34 56 30 M20 70 C34 66 46 74 62 70" fill="none" stroke="#8B5E3C" stroke-width="2"/><ellipse cx="76" cy="50" rx="6" ry="4" fill="none" stroke="#8B5E3C" stroke-width="2"/>'),
 "properties": dict(words=["الخصائص", "الملمس", "الشكل والملمس", "خصائص الأشياء", "الشكل الثابت"], anim="bounce", face=(50, 76, .3), only=SC,
   body='<circle cx="22" cy="26" r="16" fill="#E8574A" {OL}/><rect x="44" y="12" width="28" height="28" rx="3" fill="#6CB8FF" {OL}/><path d="M86 12 L98 40 L74 40Z" fill="#FFD25A" {OL}/>'
        '<rect x="10" y="54" width="80" height="40" rx="8" fill="#F2D07A" {OL}/><path d="M18 66 L26 60 M30 70 L38 64 M44 66 L52 60 M58 70 L66 64 M72 66 L80 60" stroke="#C98A55" stroke-width="2.4"/>'),
 "vessel": dict(words=["الإناء", "الأواني", "الوعاء"], anim="wobble", face=(50, 60, .42), only=SC,
   body='<path d="M26 20 L74 20 L70 34 C86 44 86 80 70 92 L30 92 C14 80 14 44 30 34Z" fill="#7CC6F2" {OL}/><rect x="22" y="12" width="56" height="10" rx="4" fill="#4A90D9" {OL}/>'),
 "earth_axis": dict(words=["دوران الأرض حول محورها"], anim="sun", face=(50, 54, .4), only=SC + ["social"],
   body='<circle cx="50" cy="52" r="34" fill="#6CB8FF" {OL}/><path d="M30 38 C38 30 50 36 46 46 C42 54 30 50 30 38Z M56 58 C66 52 76 60 70 70 C64 78 54 72 56 58Z" fill="#6CC27A" {OL}/>'
        '<path d="M36 4 L64 98" stroke="#E8574A" stroke-width="4" stroke-linecap="round" stroke-dasharray="6 4"/>'),
 "poles": dict(words=["القطب الشمالي", "القطب الجنوبي", "القطبان", "المناطق القطبية"], anim="wind", face=(50, 70, .34), only=SC + ["social"],
   body='<rect x="2" y="2" width="96" height="96" rx="8" fill="#E8F2F8" {OL}/><path d="M2 70 L30 56 L50 66 L76 50 L98 62 L98 98 L2 98Z" fill="#fff" {OL}/><path d="M60 50 L60 20" stroke="#8B5E3C" stroke-width="3"/><path d="M60 20 L82 28 L60 34Z" fill="#E8574A" {OL}/>'
        '<path d="M16 22 L20 26 M30 12 L32 16 M86 50 L88 54" stroke="#AEB8C4" stroke-width="2.4"/>'),
 "natural_change": dict(words=["التغيرات الطبيعية", "تغيرات سطح الأرض", "التغيرات البطيئة والسريعة"], anim="sway", face=(50, 76, .3), only=SC + ["social"],
   body='<path d="M2 60 L30 30 L50 50 L70 24 L98 60 L98 98 L2 98Z" fill="#9C8C7A" {OL}/><path d="M2 76 C30 70 60 84 98 76 L98 98 L2 98Z" fill="#9CD86C" {OL}/>'
        '<path d="M80 6 C70 8 66 18 70 26 M80 6 L84 14 M80 6 L72 8" fill="none" stroke="#6CB8FF" stroke-width="3" stroke-linecap="round"/><path d="M14 10 C10 18 14 24 20 22" fill="none" stroke="#6CB8FF" stroke-width="3"/>'),
 "human_impact": dict(words=["تأثير الإنسان", "تأثير الإنسان في البيئة", "الأنشطة البشرية", "البصمة البيئية"], anim="wobble", face=(50, 52, .36), only=SC + ["social", "environment"],
   body='<path d="M30 92 C10 84 12 54 24 38 C32 26 30 10 44 8 C58 6 60 24 56 40 C52 60 66 74 56 88 C50 96 40 96 30 92Z" fill="#6CC27A" {OL}/>'
        '<circle cx="66" cy="16" r="6" fill="#6CC27A" {OL}/><circle cx="78" cy="26" r="5" fill="#6CC27A" {OL}/><circle cx="84" cy="40" r="4" fill="#6CC27A" {OL}/><circle cx="86" cy="54" r="4" fill="#6CC27A" {OL}/>'),
 "insulation": dict(words=["العزل", "العزل الحراري", "المواد العازلة", "الترمس"], anim="wobble", face=(50, 60, .4), only=SC,
   body='<rect x="26" y="20" width="48" height="74" rx="12" fill="#E8574A" {OL}/><rect x="34" y="8" width="32" height="14" rx="4" fill="#AEB8C4" {OL}/><rect x="26" y="44" width="48" height="14" fill="#fff"/>'
        '<path d="M80 40 L94 40 M80 52 L92 52 M8 40 L20 40 M10 52 L20 52" stroke="#6CB8FF" stroke-width="3" stroke-linecap="round"/>'),
 "desalination": dict(words=["تحلية المياه", "محطات تحلية المياه", "تحلية مياه البحر"], anim="drip", face=(64, 50, .34), only=SC + ["social"],
   body='<path d="M2 70 C14 64 26 74 40 68 L40 98 L2 98Z" fill="#4A90D9" {OL}/><rect x="44" y="34" width="40" height="64" fill="#C9D2DC" {OL}/><rect x="52" y="20" width="10" height="16" fill="#AEB8C4" {OL}/>'
        '<path d="M24 64 L24 50 L46 50" fill="none" stroke="#3b2a1a" stroke-width="4"/><path d="M84 80 L96 80 L96 94" fill="none" stroke="#3b2a1a" stroke-width="4"/><path d="M96 70 C93 76 93 78 96 80 C99 78 99 76 96 70Z" fill="#7CC6F2" {OL}/>'),
 "sci_name": dict(words=["الاسم العلمي", "التصنيف العلمي"], anim="bob", face=(30, 56, .34), only=SC,
   body='<path d="M4 30 L62 30 L80 50 L62 70 L4 70Z" fill="#FFF3C4" {OL}/><circle cx="68" cy="50" r="4" fill="#fff" {OL}/><path d="M80 50 C88 50 94 44 96 36" fill="none" stroke="#3b2a1a" stroke-width="2"/>'
        '<text direction="ltr" x="32" y="56" text-anchor="middle" font-size="14" font-style="italic" font-weight="700" fill="#3b2a1a" font-family="serif">Rosa</text>'),
 "fission": dict(words=["الانشطار", "الانشطار الثنائي", "التكاثر بالانشطار"], never=["physics", "earth"], anim="wiggle", face=(26, 50, .3), only=SC,
   body='<ellipse cx="26" cy="50" rx="20" ry="14" fill="#9CD86C" {OL}/><path d="M50 50 L56 50 M52 46 L56 50 L52 54" fill="none" stroke="#3b2a1a" stroke-width="2.4"/>'
        '<ellipse cx="78" cy="34" rx="16" ry="11" fill="#9CD86C" {OL}/><ellipse cx="78" cy="66" rx="16" ry="11" fill="#9CD86C" {OL}/>'),
 "inherited": dict(words=["الصفات الموروثة", "الوراثة", "انتقال الصفات"], anim="bob", face=(30, 40, .34), only=SC,
   body='<circle cx="30" cy="40" r="22" fill="#F7C9A4" {OL}/><path d="M10 34 C12 14 48 14 50 34 C44 24 16 24 10 34Z" fill="#E8853C" {OL}/><circle cx="74" cy="64" r="16" fill="#F7C9A4" {OL}/><path d="M60 60 C62 44 86 44 88 60 C82 52 66 52 60 60Z" fill="#E8853C" {OL}/>'
        '<path d="M46 60 C52 68 56 68 58 66" fill="none" stroke="#3b2a1a" stroke-width="2.4" stroke-dasharray="3 2"/>'),
 "climate_factors": dict(words=["العوامل المؤثرة في المناخ", "عوامل المناخ", "العوامل المؤثرة في الطقس"], anim="sun", face=(50, 84, .3), only=SC + ["social"],
   body='<circle cx="18" cy="18" r="12" fill="#FFD25A" {OL}/><path d="M34 70 L54 34 L74 70Z" fill="#9C8C7A" {OL}/><path d="M46 48 L54 34 L62 48Z" fill="#fff" {OL}/><path d="M2 76 C20 70 40 82 60 76 L98 76 L98 98 L2 98Z" fill="#7CC6F2" {OL}/>'
        '<path d="M80 30 C86 24 92 30 88 36 M76 42 C84 36 94 42 90 50" fill="none" stroke="#6CB8FF" stroke-width="3" stroke-linecap="round"/>'),
 "malleable": dict(words=["القابلية للطرق", "قابلية الطرق والسحب", "القابلية للسحب", "الليونة"], anim="bounce", face=(60, 84, .3), only=SC,
   body='<rect x="20" y="78" width="70" height="10" rx="3" fill="#C9D2DC" {OL}/><path d="M24 8 L58 8 L58 24 L24 24Z" fill="#5D646E" {OL}/><path d="M40 24 L40 60" stroke="#8B5E3C" stroke-width="6" stroke-linecap="round"/>'
        '<path d="M60 40 L66 34 M66 48 L74 44 M58 56 L66 56" stroke="#F6B73C" stroke-width="2.4" stroke-linecap="round"/>'),
 "mech_adv": dict(words=["الفائدة الآلية", "الآلات البسيطة"], anim="wobble", face=(84, 48, .3), only=SC,
   body='<path d="M4 76 L96 50" stroke="#8B5E3C" stroke-width="6" stroke-linecap="round"/><path d="M34 70 L26 92 L42 92Z" fill="#AEB8C4" {OL}/><rect x="4" y="54" width="20" height="18" rx="2" fill="#5D646E" {OL}/>'
        '<path d="M86 28 L86 44 M80 38 L86 46 L92 38" fill="none" stroke="#E8574A" stroke-width="4" stroke-linecap="round"/>'),
 "solstice": dict(words=["الاعتدالان", "الانقلابان", "الانقلاب الصيفي", "الانقلاب الشتوي", "الاعتدال الربيعي", "الاعتدال الخريفي"], anim="sun", face=(50, 50, .36), only=SC + ["social"],
   body='<ellipse cx="50" cy="50" rx="46" ry="26" fill="none" stroke="#AEB8C4" stroke-width="2" stroke-dasharray="4 3"/><circle cx="50" cy="50" r="14" fill="#FFD25A" {OL}/>'
        '<circle cx="4" cy="50" r="5" fill="#6CB8FF" {OL}/><circle cx="96" cy="50" r="5" fill="#6CB8FF" {OL}/><circle cx="50" cy="24" r="5" fill="#6CB8FF" {OL}/><circle cx="50" cy="76" r="5" fill="#6CB8FF" {OL}/>'),
 "chem_change": dict(words=["الخاصية الكيميائية", "النشاط الكيميائي", "الخواص الكيميائية", "التغير الكيميائي"], anim="wobble", face=(30, 70, .3), only=SC,
   body='<rect x="8" y="60" width="44" height="34" rx="4" fill="#C98A55" {OL}/><path d="M30 60 C20 48 26 36 30 24 C34 34 44 40 38 54 C46 46 46 38 44 32 C54 44 50 58 30 60Z" fill="#F6A23C" {OL}/>'
        '<path d="M66 70 C66 56 92 56 92 70 C92 84 66 84 66 70Z" fill="#B5651D" {OL}/><path d="M70 64 L76 70 M82 62 L86 68" stroke="#7A3A12" stroke-width="2"/>'),
 "phys_property": dict(words=["الخاصية الفيزيائية", "الخواص الفيزيائية", "الخواص المميزة والممتدة", "التغير الفيزيائي"], anim="drip", face=(30, 50, .3), only=SC,
   body='<rect x="10" y="30" width="36" height="36" rx="4" fill="#BFE3F2" {OL}/><path d="M52 48 L60 48 M56 44 L60 48 L56 52" fill="none" stroke="#3b2a1a" stroke-width="2.4"/>'
        '<path d="M64 70 C64 62 96 62 96 70 C96 78 64 78 64 70Z" fill="#7CC6F2" {OL}/><path d="M80 40 C76 48 76 52 80 54 C84 52 84 48 80 40Z" fill="#7CC6F2" {OL}/>'),
 "ions_h": dict(words=["أيون الهيدرونيوم", "أيون الهيدروكسيد", "أيونات الهيدروجين"], anim="bounce", face=(26, 76, .3), only=SC,
   body='<circle cx="26" cy="40" r="22" fill="#E8574A" {OL}/><text direction="ltr" x="26" y="46" text-anchor="middle" font-size="14" font-weight="800" fill="#fff" font-family="sans-serif">H₃O⁺</text>'
        '<circle cx="74" cy="60" r="22" fill="#6CB8FF" {OL}/><text direction="ltr" x="74" y="66" text-anchor="middle" font-size="15" font-weight="800" fill="#fff" font-family="sans-serif">OH⁻</text>'),
 "inner_transition": dict(words=["العناصر الداخلية الانتقالية", "اللانثانيدات", "الأكتنيدات"], anim="bob", face=(50, 30, .3), only=SC,
   body='<path d="M6 10 L18 10 L18 20 L6 20Z M82 10 L94 10 L94 20 L82 20Z M6 20 L30 20 L30 40 L6 40Z M58 20 L94 20 L94 40 L58 40Z" fill="#E8F2F8" {OL}/>'
        '<rect x="6" y="40" width="88" height="10" fill="#E8F2F8" {OL}/><rect x="14" y="62" width="76" height="12" fill="#F59BB8" {OL}/><rect x="14" y="78" width="76" height="12" fill="#B0A8C9" {OL}/>'
        '<path d="M14 62 L14 74 M24 62 L24 74 M34 62 L34 74 M44 62 L44 74 M54 62 L54 74 M64 62 L64 74 M74 62 L74 74" stroke="#3b2a1a" stroke-width="1"/>'),
 "fe_co_ni": dict(words=["الحديد والكوبالت والنيكل", "الفلزات المغناطيسية", "المواد المغناطيسية"], anim="wobble", face=(50, 74, .3), only=SC,
   body='<path d="M20 10 L20 46 C20 66 80 66 80 46 L80 10 L64 10 L64 46 C64 52 36 52 36 46 L36 10Z" fill="#E8574A" {OL}/><rect x="20" y="4" width="16" height="10" fill="#C9D2DC" {OL}/><rect x="64" y="4" width="16" height="10" fill="#C9D2DC" {OL}/>'
        '<rect x="14" y="76" width="18" height="14" rx="2" fill="#8A93A6" {OL}/><rect x="40" y="78" width="18" height="12" rx="2" fill="#6E8BB0" {OL}/><rect x="66" y="76" width="18" height="14" rx="2" fill="#AEB8C4" {OL}/>'),
 "polar_molecule": dict(words=["الجزيء القطبي", "القطبية"], anim="bob", face=(50, 46, .34), only=SC,
   body='<circle cx="50" cy="46" r="22" fill="#E8574A" {OL}/><circle cx="20" cy="72" r="13" fill="#fff" {OL}/><circle cx="80" cy="72" r="13" fill="#fff" {OL}/>'
        '<text direction="ltr" x="50" y="16" text-anchor="middle" font-size="12" font-weight="800" fill="#E8574A" font-family="sans-serif">δ−</text><text direction="ltr" x="50" y="96" text-anchor="middle" font-size="12" font-weight="800" fill="#6CB8FF" font-family="sans-serif">δ+</text>'),
 "ionic_lattice": dict(words=["المركب الأيوني", "المركبات الأيونية"], anim="wobble", face=(50, 50, .3), only=SC,
   body='<path d="M20 20 L80 20 L80 80 L20 80Z M50 20 L50 80 M20 50 L80 50" fill="none" stroke="#AEB8C4" stroke-width="2"/>'
        '<circle cx="20" cy="20" r="9" fill="#B0A8C9" {OL}/><circle cx="50" cy="20" r="6" fill="#9CD86C" {OL}/><circle cx="80" cy="20" r="9" fill="#B0A8C9" {OL}/><circle cx="20" cy="50" r="6" fill="#9CD86C" {OL}/><circle cx="50" cy="50" r="9" fill="#B0A8C9" {OL}/><circle cx="80" cy="50" r="6" fill="#9CD86C" {OL}/>'
        '<circle cx="20" cy="80" r="9" fill="#B0A8C9" {OL}/><circle cx="50" cy="80" r="6" fill="#9CD86C" {OL}/><circle cx="80" cy="80" r="9" fill="#B0A8C9" {OL}/>'),
 "temp_scales": dict(words=["المقياس السلسيوسي", "المقياس الفهرنهايتي", "مقياس كلفن", "تدريج الحرارة", "وحدات قياس الحرارة"], anim="bob", face=(50, 84, .3), only=SC,
   body='<rect x="40" y="6" width="20" height="70" rx="10" fill="#fff" {OL}/><rect x="45" y="30" width="10" height="50" fill="#E8574A"/><circle cx="50" cy="82" r="14" fill="#E8574A" {OL}/>'
        '<text direction="ltr" x="18" y="26" text-anchor="middle" font-size="13" font-weight="800" fill="#3b2a1a" font-family="sans-serif">°C</text><text direction="ltr" x="82" y="26" text-anchor="middle" font-size="13" font-weight="800" fill="#3b2a1a" font-family="sans-serif">°F</text><text direction="ltr" x="82" y="56" text-anchor="middle" font-size="13" font-weight="800" fill="#3b2a1a" font-family="sans-serif">K</text>'),
 "speedometer": dict(words=["السرعة اللحظية", "عداد السرعة", "التسارع الموجب", "التسارع السالب", "التباطؤ"], anim="sun", face=(50, 76, .3), only=SC,
   body='<path d="M8 66 A42 42 0 0 1 92 66Z" fill="#fff" {OL}/><path d="M16 60 L22 58 M24 40 L30 42 M40 28 L42 34 M60 28 L58 34 M76 40 L70 42 M84 60 L78 58" stroke="#3b2a1a" stroke-width="3"/>'
        '<path d="M50 66 L74 38" stroke="#E8574A" stroke-width="4" stroke-linecap="round"/><circle cx="50" cy="66" r="6" fill="#3b2a1a"/>'),
 "turbine": dict(words=["التوربين", "التوربينات", "توربينات الرياح"], anim="sun", face=(50, 40, .3), only=SC,
   body='<path d="M50 40 L50 96" stroke="#AEB8C4" stroke-width="6"/><path d="M50 40 L50 4 C58 10 58 30 50 40Z M50 40 L80 58 C72 64 56 54 50 40Z M50 40 L20 58 C24 50 42 36 50 40Z" fill="#E8F2F8" {OL}/><circle cx="50" cy="40" r="6" fill="#AEB8C4" {OL}/>'),
 "vaccine": dict(words=["التطعيمات", "المناعة المكتسبة"], anim="wobble", face=(40, 50, .3), only=SC + ["life"],
   body='<rect x="14" y="40" width="56" height="20" rx="4" fill="#E8F6FF" {OL}/><rect x="16" y="42" width="30" height="16" fill="#9CD86C"/><path d="M70 50 L96 50" stroke="#AEB8C4" stroke-width="3"/>'
        '<path d="M14 36 L14 64 M4 50 L14 50" stroke="#3b2a1a" stroke-width="4" stroke-linecap="round"/><path d="M24 40 L24 46 M34 40 L34 46 M44 40 L44 46 M54 40 L54 46" stroke="#3b2a1a" stroke-width="1.6"/>'),
 "food_groups": dict(words=["المواد الغذائية", "المجموعات الغذائية", "مكونات الغذاء"], anim="bounce", face=(50, 60, .32),
   body='<path d="M10 40 L90 40 L80 92 L20 92Z" fill="#C98A55" {OL}/><circle cx="28" cy="34" r="10" fill="#E8574A" {OL}/><path d="M44 36 C44 22 58 20 60 34Z" fill="#6CC27A" {OL}/>'
        '<path d="M66 40 C64 26 82 24 82 38" fill="#F2C46D" {OL}/><path d="M50 18 L56 6 L62 18Z" fill="#fff" {OL}/>'),
 "bladder": dict(words=["المثانة", "البول"], anim="drip", face=(50, 70, .34),
   body='<path d="M20 20 C10 20 8 44 20 48 C30 52 34 30 26 22Z M80 20 C90 20 92 44 80 48 C70 52 66 30 74 22Z" fill="#C9675A" {OL}/>'
        '<path d="M24 48 L42 62 M76 48 L58 62" stroke="#E8853C" stroke-width="3"/><path d="M36 62 C36 54 64 54 64 62 L62 84 C60 94 40 94 38 84Z" fill="#F2D07A" {OL}/>'),
 "atrium": dict(words=["الأذين", "البطين", "حجرات القلب", "صمامات القلب"], anim="bounce", face=(56, 60, .3),
   body='<path d="M50 92 C20 72 6 54 8 36 C10 18 32 12 50 30 C68 12 90 18 92 36 C94 54 80 72 50 92Z" fill="#E8574A" {OL}/>'
        '<path d="M50 30 L50 86 M18 44 L82 44" stroke="#B5332A" stroke-width="3"/><path d="M28 24 L28 6 M40 22 L42 4" stroke="#6CB8FF" stroke-width="6" stroke-linecap="round"/>'),
}
ALIAS_ONLY = None
ALIASES = {"المحور": ("eco.earth_axis", ("science",)), "مندل": ("eco.inherited", ("science",)), "الطرز الجينية": "sec:genotype", "الطرز الشكلية": "sec:genotype",
           "موازنة المعادلات": ("chem.eq_balanced", ("science",)), "القارات": ("geo:continents", ("science",))}
