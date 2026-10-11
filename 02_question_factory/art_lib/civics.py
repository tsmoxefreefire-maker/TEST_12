"""🆕 batch 43 · history, society and the state (التاريخ، الدراسات الاجتماعية، والمواطنة): the historian's tools (sources, oral accounts,
methods, documenting, cause and effect), old writing and art (rock art, Musnad, Arabic calligraphy, poetry), ancient kingdoms and
trade roads, the voyages of discovery, the world's organisations and summits, the state's councils and powers (no person, no
royal or religious symbol: art_library.NEVER_DRAW), the economy and services (roads, rail, housing, ports, exports), society
(unemployment, poverty, scarcity, hobbies, procrastination), and geography as a science."""
F = "civ"
S = ["social"]
D = {
 # ---------- the historian's tools ----------
 "manuscript": dict(words=["المصادر الأصلية", "المصادر الكلاسيكية", "كتب التراجم", "المخطوطات", "المخطوطة", "المصادر التاريخية"], anim="sway", face=(50, 56, .4), only=S + ["arabic"],
   body='<path d="M14 14 C8 14 8 26 14 26 L86 26 C92 26 92 14 86 14Z" fill="#C98A55" {OL}/><rect x="14" y="20" width="72" height="66" fill="#F2DDB0" {OL}/><path d="M14 80 C8 80 8 92 14 92 L86 92 C92 92 92 80 86 80Z" fill="#C98A55" {OL}/>'
        '<path d="M24 38 C34 34 44 42 54 38 C64 34 70 40 76 38 M24 50 C34 46 44 54 54 50 C64 46 70 52 76 50 M24 62 C34 58 44 66 54 62" fill="none" stroke="#8B5E3C" stroke-width="2.4"/>'),
 "oral": dict(words=["الروايات الشفهية", "الرواية الشفهية", "التاريخ الشفهي", "القصص الشعبية"], anim="bob", face=(32, 40, .38), only=S,
   body='<circle cx="32" cy="40" r="20" fill="#F7C9A4" {OL}/><path d="M14 34 C16 16 50 16 52 34 C46 26 20 26 14 34Z" fill="#E8F2F8" {OL}/><path d="M10 96 C10 66 54 66 54 96Z" fill="#B0A8C9" {OL}/>'
        '<path d="M60 22 L94 22 C96 22 98 24 98 26 L98 46 C98 48 96 50 94 50 L74 50 L64 58 L66 50 L60 50 C58 50 56 48 56 46 L56 26 C56 24 58 22 60 22Z" fill="#fff" {OL}/><path d="M64 32 L90 32 M64 40 L82 40" stroke="#AEB8C4" stroke-width="2.4"/>'),
 "historians": dict(words=["المؤرخون", "المؤرخون المسلمون", "المؤرخون النجديون", "المؤرخون اليونان والرومان", "كتابة التاريخ", "تدوين التاريخ"], anim="bob", face=(36, 66, .38), only=S,
   body='<path d="M6 40 C22 32 36 34 46 42 L46 92 C36 84 22 82 6 90Z" fill="#fff" {OL}/><path d="M46 42 C56 34 70 32 86 40 L86 90 C70 82 56 84 46 92Z" fill="#fff" {OL}/><path d="M14 54 L38 50 M14 64 L38 62 M54 50 L78 54 M54 62 L78 64" stroke="#AEB8C4" stroke-width="2"/>'
        '<path d="M70 36 C80 14 92 6 96 4 C94 14 88 28 74 40Z" fill="#E8F2F8" {OL}/><path d="M74 40 L66 52" stroke="#3b2a1a" stroke-width="2.4"/>'),
 "annals": dict(words=["المنهج الحولي", "التأريخ بالسنوات", "الحوليات"], anim="bob", face=(50, 70, .34), only=S,
   body='<rect x="10" y="16" width="80" height="78" rx="6" fill="#fff" {OL}/><rect x="10" y="16" width="80" height="18" rx="6" fill="#E8574A" {OL}/><path d="M30 8 L30 22 M70 8 L70 22" stroke="#3b2a1a" stroke-width="5" stroke-linecap="round"/>'
        '<path d="M22 46 L22 84 M22 52 L40 52 M22 66 L48 66 M22 80 L36 80" stroke="#3b2a1a" stroke-width="2.6"/><circle cx="22" cy="52" r="3" fill="#6CB8FF"/><circle cx="22" cy="66" r="3" fill="#6CB8FF"/><circle cx="22" cy="80" r="3" fill="#6CB8FF"/>'),
 "topical": dict(words=["المنهج الموضوعي", "التصنيف حسب الموضوع", "تنظيم المعلومات"], anim="bob", face=(50, 66, .34), only=S + ["thinking"],
   body='<path d="M6 30 L34 30 L40 38 L94 38 L94 90 L6 90Z" fill="#F6B73C" {OL}/><path d="M12 24 L36 24 L40 30" fill="none" stroke="#3b2a1a" stroke-width="2"/><rect x="16" y="46" width="22" height="8" rx="2" fill="#fff" {OL}/><rect x="42" y="46" width="22" height="8" rx="2" fill="#6CB8FF" {OL}/><rect x="68" y="46" width="18" height="8" rx="2" fill="#6CC27A" {OL}/>'),
 "documenting": dict(words=["التوثيق", "توثيق المعلومات", "توثيق المصادر"], anim="bounce", face=(36, 50, .36), only=S + ["arabic", "thinking"],
   body='<rect x="8" y="10" width="58" height="80" rx="4" fill="#fff" {OL}/><path d="M18 26 L56 26 M18 38 L56 38 M18 50 L46 50" stroke="#AEB8C4" stroke-width="2.4"/>'
        '<rect x="58" y="54" width="34" height="10" rx="2" fill="#8B5E3C" {OL}/><path d="M66 54 L66 36 C66 28 84 28 84 36 L84 54" fill="#C98A55" {OL}/><ellipse cx="44" cy="76" rx="14" ry="8" fill="none" stroke="#E8574A" stroke-width="3"/>'),
 "cause_effect": dict(words=["السبب والنتيجة", "الأسباب والنتائج", "العلاقة السببية"], anim="wobble", face=(84, 70, .3), only=S + ["thinking", "arabic"],
   body='<path d="M2 92 L98 92" stroke="#3b2a1a" stroke-width="4"/><rect x="8" y="30" width="12" height="62" rx="2" fill="#E8574A" {OL} transform="rotate(30 14 92)"/><rect x="30" y="40" width="12" height="52" rx="2" fill="#F6B73C" {OL} transform="rotate(20 36 92)"/>'
        '<rect x="52" y="42" width="12" height="50" rx="2" fill="#6CC27A" {OL} transform="rotate(8 58 92)"/><rect x="76" y="42" width="12" height="50" rx="2" fill="#6CB8FF" {OL}/>'),
 "compare_two": dict(words=["المقارنة", "المقارنة بين الأشياء", "أوجه الشبه والاختلاف", "الفروق"], anim="wobble", face=(50, 74, .3), only=S + ["life", "thinking", "english"],
   body='<rect x="4" y="16" width="40" height="56" rx="6" fill="#6CB8FF" {OL}/><rect x="56" y="16" width="40" height="56" rx="6" fill="#F6B73C" {OL}/>'
        '<path d="M14 34 L34 34 M14 46 L30 46 M66 34 L86 34 M66 46 L82 46" stroke="#fff" stroke-width="4" stroke-linecap="round"/><text direction="ltr" x="50" y="50" text-anchor="middle" font-size="18" font-weight="800" fill="#3b2a1a" font-family="sans-serif">≠</text>'),
 # ---------- old writing and art ----------
 "rock_art": dict(words=["الرسوم الصخرية", "النقوش الصخرية", "الفن الصخري", "الرسوم على الصخور"], anim="sway", face=(76, 30, .3), only=S,
   body='<path d="M4 90 L10 30 L40 12 L80 18 L96 52 L90 90Z" fill="#C9A27A" {OL}/>'
        '<path d="M24 60 C24 52 40 50 44 56 L50 52 L50 60 L46 64 L46 72 M28 64 L28 74 M38 64 L38 74 M44 56 L48 46 M52 50 L56 42" fill="none" stroke="#8B3A2B" stroke-width="3" stroke-linecap="round"/><path d="M62 70 L62 50 M56 56 L68 56 M62 70 L56 80 M62 70 L68 80" fill="none" stroke="#8B3A2B" stroke-width="3" stroke-linecap="round"/><circle cx="62" cy="44" r="4" fill="#8B3A2B"/>'),
 "musnad": dict(words=["الخط المسند", "الخط المسند الجنوبي", "النقوش القديمة", "الكتابات القديمة"], anim="wobble", face=(50, 80, .3), only=S + ["arabic"],
   body='<path d="M14 8 L86 8 L90 94 L10 94Z" fill="#B48B65" {OL}/><path d="M24 22 L24 36 L32 36 L32 22 M42 22 L48 36 L54 22 M64 22 L64 36 M60 28 L70 28 M24 46 L32 60 L24 60 M42 46 L42 60 L52 60 L52 46 M64 46 L72 60 M72 46 L64 60" fill="none" stroke="#5D3A1A" stroke-width="3"/>'),
 "calligraphy": dict(words=["الخط العربي", "فن الخط العربي", "أنواع الخطوط العربية", "خط النسخ", "خط الرقعة"], anim="sway", face=(30, 70, .32), only=S + ["arabic", "english", "art"],
   body='<rect x="4" y="14" width="92" height="72" rx="6" fill="#FFF8E8" {OL}/><path d="M16 60 C28 40 40 70 52 50 C58 40 66 44 70 52 C74 60 82 56 86 44" fill="none" stroke="#1F2A44" stroke-width="5" stroke-linecap="round"/>'
        '<circle cx="44" cy="34" r="3" fill="#1F2A44"/><path d="M74 8 L92 30 L86 34 L70 12Z" fill="#C98A55" {OL}/>'),
 "poetry": dict(words=["الشعر العربي", "الشعر", "المعلقات", "القصيدة", "الشعر الجاهلي", "الشعراء"], anim="sway", face=(40, 56, .36), only=S + ["arabic"],
   body='<path d="M10 14 C4 14 4 26 10 26 L70 26 C76 26 76 14 70 14Z" fill="#C98A55" {OL}/><rect x="10" y="20" width="60" height="70" fill="#F2DDB0" {OL}/>'
        '<path d="M18 38 L36 38 M44 38 L62 38 M18 52 L36 52 M44 52 L62 52 M18 66 L36 66 M44 66 L62 66" stroke="#8B5E3C" stroke-width="3" stroke-linecap="round"/><path d="M74 60 C86 34 94 20 98 14 C96 30 90 46 78 64Z" fill="#fff" {OL}/>'),
 "courage": dict(words=["الشجاعة", "الشجاع", "الإقدام"], anim="bounce", face=(50, 50, .4),
   body='<circle cx="50" cy="50" r="44" fill="#F6B73C" {OL}/><path d="M50 14 L54 26 M78 26 L70 34 M86 50 L74 50 M22 26 L30 34 M14 50 L26 50" stroke="#C26A28" stroke-width="5" stroke-linecap="round"/>'
        '<circle cx="50" cy="56" r="26" fill="#FFD25A" {OL}/>'),
 "loyalty": dict(words=["الوفاء", "الوفاء بالوعد", "الإخلاص"], anim="bob", face=(50, 40, .38),
   body='<path d="M50 74 C24 58 12 44 14 30 C16 16 34 12 50 26 C66 12 84 16 86 30 C88 44 76 58 50 74Z" fill="#E8574A" {OL}/>'
        '<path d="M6 84 L32 76 L50 84 L68 76 L94 84" fill="none" stroke="#F7C9A4" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/>'),
 "arches": dict(words=["القباب والأقواس", "الأقواس", "العمارة القديمة", "الفن المعماري"], anim="bob", face=(50, 70, .32), only=S,
   body='<rect x="4" y="40" width="92" height="56" fill="#F2DDB0" {OL}/><path d="M12 96 L12 64 C12 50 32 50 32 64 L32 96 M40 96 L40 64 C40 50 60 50 60 64 L60 96 M68 96 L68 64 C68 50 88 50 88 64 L88 96" fill="#C98A55" {OL}/>'
        '<path d="M30 40 C30 18 70 18 70 40Z" fill="#6CB8FF" {OL}/>'),
 # ---------- ancient kingdoms, trade, discovery ----------
 "ancient_kingdom": dict(words=["مملكة دادان", "مملكة لحيان", "مملكة كندة", "مملكة الأنباط", "تيماء", "الحضارات المفقودة", "الممالك العربية القديمة", "الحضارات القديمة"], anim="bob", face=(50, 54, .34), only=S + ["english"],
   body='<path d="M2 96 L2 10 L98 10 L98 96Z" fill="#D8A86A" {OL}/><path d="M28 96 L28 50 L72 50 L72 96" fill="#B5733F" {OL}/><path d="M24 50 L76 50 L68 36 L32 36Z" fill="#C98A55" {OL}/>'
        '<path d="M42 96 L42 68 C42 60 58 60 58 68 L58 96" fill="#5D3A1A"/><path d="M32 36 L32 22 L40 30 L50 18 L60 30 L68 22 L68 36" fill="none" stroke="#8B5E3C" stroke-width="3"/>'),
 "zubaida": dict(words=["درب زبيدة", "طرق الحج القديمة", "الطرق التاريخية"], anim="sway", face=(30, 50, .32), only=S,
   body='<rect x="2" y="2" width="96" height="96" rx="8" fill="#FFE7A8" {OL}/><path d="M2 80 C30 70 60 86 98 74" fill="none" stroke="#C98A55" stroke-width="10"/><path d="M2 80 C30 70 60 86 98 74" fill="none" stroke="#fff" stroke-width="2" stroke-dasharray="6 6"/>'
        '<path d="M16 66 C16 50 34 44 42 52 L50 40 L56 42 L50 56 L50 66 M22 66 L22 76 M44 66 L44 76" fill="#C98A55" stroke="#3b2a1a" stroke-width="2.4"/><circle cx="78" cy="22" r="10" fill="#F6B73C" {OL}/>'),
 "voyage": dict(words=["الكشوف الجغرافية", "اكتشاف الأمريكتين", "رأس الرجاء الصالح", "الرحلات البحرية", "مستكشف", "الاكتشافات", "المستكشفون"], anim="sway", face=(40, 62, .32), only=S + ["english"],
   body='<path d="M2 80 C14 74 26 84 38 78 C50 72 62 84 74 78 C84 74 92 80 98 78 L98 98 L2 98Z" fill="#4A90D9" {OL}/><path d="M14 68 L86 68 L76 82 L24 82Z" fill="#8B5E3C" {OL}/>'
        '<path d="M48 68 L48 8" stroke="#3b2a1a" stroke-width="3"/><path d="M48 12 C70 18 74 40 50 60Z" fill="#fff" {OL}/><path d="M46 20 C30 26 28 44 46 56Z" fill="#E8F2F8" {OL}/><path d="M48 8 L60 12 L48 16" fill="#E8574A"/>'),
 "great_wall": dict(words=["سور الصين العظيم", "الأسوار القديمة"], anim="bob", face=(50, 70, .32), only=S + ["english"],
   body='<path d="M2 80 C20 70 30 50 50 46 C70 42 80 30 98 26 L98 44 C80 48 70 60 50 64 C30 68 20 88 2 96Z" fill="#C9A27A" {OL}/>'
        '<path d="M18 74 L18 66 L24 66 L24 72 M44 62 L44 54 L50 54 L50 60 M74 50 L74 42 L80 42 L80 48" fill="none" stroke="#8B5E3C" stroke-width="3"/><path d="M2 98 C30 90 70 80 98 60" fill="none" stroke="#9CD86C" stroke-width="4"/>'),
 "euro": dict(words=["اليورو", "العملة الموحدة", "التكامل الأوروبي", "الاتحاد الأوروبي"], anim="sun", face=(50, 70, .32), only=S + ["finance"],
   body='<circle cx="50" cy="50" r="44" fill="#FFD25A" {OL}/><circle cx="50" cy="50" r="34" fill="none" stroke="#F6B73C" stroke-width="3"/>'
        '<text direction="ltr" x="50" y="64" text-anchor="middle" font-size="40" font-weight="800" fill="#B5651D" font-family="sans-serif">€</text>'),
 "world_org": dict(words=["هيئة الأمم المتحدة", "الأمم المتحدة", "الجمعية العامة", "الوكالات المتخصصة", "عصبة الأمم", "المنظمات الدولية", "المنظمات العربية", "مقر الرابطة",
                          "العمل العربي المشترك", "التضامن العربي", "الدول الأعضاء", "التعاون الدولي", "جامعة الدول العربية", "مجلس التعاون الخليجي"], anim="sun", face=(50, 46, .34), only=S,
   body='<circle cx="50" cy="46" r="32" fill="#6CB8FF" {OL}/><path d="M26 36 C34 28 46 34 42 44 C38 52 26 48 26 36Z M56 50 C66 44 76 52 70 62 C64 70 54 64 56 50Z" fill="#9CD86C" {OL}/>'
        '<path d="M10 70 C20 88 40 96 50 96 C60 96 80 88 90 70" fill="none" stroke="#3b2a1a" stroke-width="3"/><circle cx="18" cy="80" r="5" fill="#6CC27A" {OL}/><circle cx="34" cy="90" r="5" fill="#6CC27A" {OL}/><circle cx="66" cy="90" r="5" fill="#6CC27A" {OL}/><circle cx="82" cy="80" r="5" fill="#6CC27A" {OL}/>'),
 "summit": dict(words=["مجموعة العشرين (G20)", "مجموعة العشرين", "قمة الرياض 2020", "القمة الدولية", "القمم الدولية", "المؤتمرات الدولية"], anim="bob", face=(50, 50, .34), only=S,
   body='<ellipse cx="50" cy="56" rx="34" ry="20" fill="#C98A55" {OL}/><ellipse cx="50" cy="52" rx="18" ry="9" fill="#6CB8FF" {OL}/>'
        '<circle cx="14" cy="40" r="6" fill="#F7C9A4" {OL}/><circle cx="32" cy="28" r="6" fill="#F7C9A4" {OL}/><circle cx="50" cy="24" r="6" fill="#F7C9A4" {OL}/><circle cx="68" cy="28" r="6" fill="#F7C9A4" {OL}/><circle cx="86" cy="40" r="6" fill="#F7C9A4" {OL}/>'
        '<circle cx="20" cy="80" r="6" fill="#F7C9A4" {OL}/><circle cx="50" cy="86" r="6" fill="#F7C9A4" {OL}/><circle cx="80" cy="80" r="6" fill="#F7C9A4" {OL}/>'),
 "future_city": dict(words=["نيوم", "المدن المستقبلية", "مدينة المستقبل", "المشاريع العملاقة"], anim="bob", face=(50, 70, .3), only=S,
   body='<rect x="2" y="2" width="96" height="96" rx="8" fill="#BFE3F2" {OL}/><path d="M2 84 C30 78 70 78 98 84 L98 98 L2 98Z" fill="#4A90D9"/>'
        '<path d="M14 84 L14 40 L26 30 L26 84 M34 84 L34 20 L48 12 L48 84 M58 84 L58 34 C58 26 72 26 72 34 L72 84 M80 84 L80 46 L92 40 L92 84" fill="#E8F2F8" {OL}/><path d="M38 30 L44 30 M38 44 L44 44 M38 58 L44 58" stroke="#6CB8FF" stroke-width="3"/><rect x="2" y="2" width="96" height="96" rx="8" fill="none" {OL}/>'),
 "industrial_port": dict(words=["المدن الصناعية", "الموانئ الصناعية", "المناطق الصناعية"], anim="bob", face=(30, 60, .3), only=S,
   body='<rect x="6" y="40" width="44" height="40" fill="#AEB8C4" {OL}/><path d="M12 40 L12 18 L20 18 L20 40 M28 40 L28 24 L36 24 L36 40" fill="#8A93A6" {OL}/><path d="M16 14 C14 8 22 6 20 0 M32 20 C30 14 38 12 36 6" fill="none" stroke="#AEB8C4" stroke-width="3"/>'
        '<path d="M50 80 C62 76 80 84 98 80 L98 98 L50 98Z" fill="#4A90D9" {OL}/><path d="M60 72 L94 72 L88 82 L66 82Z" fill="#E8574A" {OL}/><rect x="66" y="60" width="10" height="12" fill="#6CB8FF" {OL}/><rect x="78" y="60" width="10" height="12" fill="#F6B73C" {OL}/>'),
 "trade": dict(words=["الصادرات والواردات", "الصادرات", "الواردات", "التجارة الخارجية", "الميزان التجاري"], anim="sway", face=(50, 58, .32), only=S + ["finance"],
   body='<path d="M2 70 C14 64 26 74 40 68 C54 62 66 74 80 68 C88 64 94 68 98 68 L98 98 L2 98Z" fill="#4A90D9" {OL}/><path d="M18 60 L82 60 L74 74 L26 74Z" fill="#5D646E" {OL}/>'
        '<rect x="26" y="44" width="14" height="16" fill="#E8574A" {OL}/><rect x="42" y="44" width="14" height="16" fill="#6CC27A" {OL}/><rect x="58" y="44" width="14" height="16" fill="#F6B73C" {OL}/>'
        '<path d="M10 20 L36 20 M30 14 L36 20 L30 26 M90 32 L64 32 M70 26 L64 32 L70 38" fill="none" stroke="#3b2a1a" stroke-width="3" stroke-linecap="round"/>'),
 "roads": dict(words=["الطرق", "الطرق السريعة", "الجسور"], anim="bob", face=(78, 30, .3), only=S,
   body='<rect x="2" y="2" width="96" height="96" rx="8" fill="#9CD86C" {OL}/><path d="M30 98 L44 2 L56 2 L70 98Z" fill="#5D646E"/><path d="M50 10 L50 22 M50 34 L50 50 M50 62 L50 82" stroke="#fff" stroke-width="3"/>'
        '<rect x="2" y="2" width="96" height="96" rx="8" fill="none" {OL}/>'),
 "railway": dict(words=["السكك الحديدية", "القطارات", "قطار الحرمين", "شبكة القطارات"], anim="bounce", face=(46, 46, .3), only=S + ["english"],
   body='<path d="M20 98 L42 4 M80 98 L58 4" stroke="#8B5E3C" stroke-width="4"/><path d="M24 84 L76 84 M28 66 L72 66 M32 48 L68 48 M36 30 L64 30 M39 14 L61 14" stroke="#C98A55" stroke-width="5"/>'
        '<rect x="30" y="30" width="34" height="30" rx="8" fill="#E8574A" {OL}/><rect x="36" y="36" width="22" height="10" rx="2" fill="#BFE3F2"/>'),
 "housing": dict(words=["الإسكان", "المساكن", "أنواع المساكن", "شقة", "فيلا", "العمارات السكنية"], anim="bob", face=(30, 66, .3), only=S + ["english", "life"],
   body='<rect x="6" y="30" width="44" height="66" fill="#F2D07A" {OL}/><path d="M12 40 L22 40 M30 40 L42 40 M12 54 L22 54 M30 54 L42 54 M12 68 L22 68 M30 68 L42 68" stroke="#6CB8FF" stroke-width="6"/>'
        '<path d="M54 62 L76 44 L98 62 L98 96 L54 96Z" fill="#F59BB8" {OL}/><rect x="70" y="74" width="12" height="22" fill="#8B5E3C" {OL}/>'),
 "infrastructure": dict(words=["البنية الأساسية", "البنية التحتية", "المشاريع التنموية", "التنمية الشاملة"], anim="bob", face=(30, 80, .3), only=S,
   body='<path d="M60 96 L60 14 L90 14" fill="none" stroke="#F6B73C" stroke-width="6"/><path d="M60 26 L90 14 M60 40 L80 14" stroke="#F6B73C" stroke-width="3"/><path d="M86 14 L86 40" stroke="#3b2a1a" stroke-width="2"/><rect x="80" y="40" width="12" height="10" fill="#AEB8C4" {OL}/>'
        '<path d="M2 96 L98 96" stroke="#5D646E" stroke-width="8"/><rect x="10" y="60" width="36" height="36" fill="#C9D2DC" {OL}/><path d="M16 70 L40 70 M16 82 L40 82" stroke="#6CB8FF" stroke-width="4"/>'),
 "scholarship": dict(words=["الابتعاث", "البعثات الدراسية", "الدراسة في الخارج", "يتخرج", "التخرج"], anim="bounce", face=(36, 64, .34), only=S + ["english"],
   body='<path d="M36 26 L70 40 L36 54 L2 40Z" fill="#3b3b5c" {OL}/><path d="M14 46 L14 62 C14 72 58 72 58 62 L58 46" fill="#3b3b5c" {OL}/><path d="M70 40 L70 58" stroke="#FFD25A" stroke-width="3"/><circle cx="70" cy="60" r="3" fill="#FFD25A"/>'
        '<path d="M64 84 L98 70 L94 66 L80 70 L70 62 L66 64 L72 72 L64 76 L60 72 L56 74Z" fill="#E8F2F8" {OL}/>'),
 # ---------- the state (no person, no symbol) ----------
 "council": dict(words=["الشورى", "مجلس المنطقة", "هيئة الخبراء", "المجالس", "المجلس البلدي"], anim="bob", face=(50, 54, .34), only=S,
   body='<path d="M10 70 C10 40 90 40 90 70Z" fill="#C98A55" {OL}/><path d="M24 70 C24 54 76 54 76 70Z" fill="#E6C08A" {OL}/>'
        '<circle cx="12" cy="40" r="6" fill="#AEB8C4" {OL}/><circle cx="30" cy="26" r="6" fill="#AEB8C4" {OL}/><circle cx="50" cy="22" r="6" fill="#AEB8C4" {OL}/><circle cx="70" cy="26" r="6" fill="#AEB8C4" {OL}/><circle cx="88" cy="40" r="6" fill="#AEB8C4" {OL}/>'
        '<path d="M4 86 L96 86" stroke="#3b2a1a" stroke-width="4"/>'),
 "powers": dict(words=["السلطة التنظيمية", "السلطة التنفيذية", "السلطات الثلاث", "سلطات الدولة"], anim="bob", face=(50, 30, .3), only=S,
   body='<path d="M6 26 L50 6 L94 26Z" fill="#E8F2F8" {OL}/><rect x="12" y="30" width="14" height="52" fill="#E8F2F8" {OL}/><rect x="43" y="30" width="14" height="52" fill="#E8F2F8" {OL}/><rect x="74" y="30" width="14" height="52" fill="#E8F2F8" {OL}/>'
        '<rect x="4" y="82" width="92" height="12" rx="2" fill="#AEB8C4" {OL}/><circle cx="19" cy="46" r="4" fill="#6CB8FF"/><circle cx="50" cy="46" r="4" fill="#F6B73C"/><circle cx="81" cy="46" r="4" fill="#6CC27A"/>'),
 "judiciary": dict(words=["السلطة القضائية", "القضاء", "المحكمة", "المحاكم", "العدل", "العدالة"], anim="wobble", face=(50, 20, .3), only=S + ["english"],
   body='<path d="M50 12 L50 86 M24 90 L76 90" stroke="#8B5E3C" stroke-width="5" stroke-linecap="round"/><path d="M14 30 L86 30" stroke="#8B5E3C" stroke-width="4"/>'
        '<path d="M14 30 L4 58 L24 58Z M86 30 L76 58 L96 58Z" fill="none" stroke="#3b2a1a" stroke-width="2"/><path d="M2 58 C4 68 24 68 26 58Z M74 58 C76 68 96 68 98 58Z" fill="#FFD25A" {OL}/>'),
 "ministry": dict(words=["الوزير", "الوزارة", "وزارة الداخلية"], anim="bob", face=(50, 66, .3), only=S,
   body='<path d="M4 34 L50 10 L96 34Z" fill="#C9D2DC" {OL}/><path d="M14 38 L14 82 M30 38 L30 82 M46 38 L46 82 M62 38 L62 82 M78 38 L78 82" stroke="#AEB8C4" stroke-width="7"/><rect x="4" y="82" width="92" height="12" fill="#AEB8C4" {OL}/>'
        '<rect x="6" y="34" width="88" height="6" fill="#AEB8C4" {OL}/><rect x="40" y="58" width="20" height="24" fill="#5D646E" {OL}/>'),
 "decree": dict(words=["المراسيم الملكية", "الأوامر الملكية", "الأنظمة الصادرة", "القرارات الرسمية"], anim="sway", face=(46, 46, .34), only=S,
   body='<path d="M16 10 C10 10 10 22 16 22 L76 22 C82 22 82 10 76 10Z" fill="#E6C08A" {OL}/><rect x="16" y="16" width="60" height="70" fill="#FFF8E8" {OL}/><path d="M26 34 L66 34 M26 46 L66 46 M26 58 L54 58" stroke="#AEB8C4" stroke-width="2.4"/>'
        '<circle cx="66" cy="80" r="12" fill="#3E8E4C" {OL}/><path d="M60 90 L56 98 L64 94 L66 100 M72 90 L76 98 L68 94" fill="#3E8E4C" stroke="#3b2a1a" stroke-width="1.6"/>'),
 "medals": dict(words=["الأوسمة السعودية", "الأوسمة", "الأنواط", "الأوسمة والأنواط", "الجوائز"], anim="sway", face=(50, 70, .34), only=S,
   body='<path d="M30 4 L44 46 L56 46 L70 4 L58 4 L50 30 L42 4Z" fill="#3E8E4C" {OL}/><circle cx="50" cy="66" r="24" fill="#FFD25A" {OL}/>'
        '<path d="M50 50 L54 60 L64 60 L56 66 L60 76 L50 70 L40 76 L44 66 L36 60 L46 60Z" fill="#F6B73C" {OL}/>'),
 "calendar_date": dict(words=["المناسبات الوطنية", "التاريخ الهجري", "التاريخ الميلادي"], anim="bob", face=(50, 66, .36), only=S,
   body='<rect x="10" y="16" width="80" height="78" rx="6" fill="#fff" {OL}/><rect x="10" y="16" width="80" height="20" rx="6" fill="#3E8E4C" {OL}/><path d="M30 8 L30 24 M70 8 L70 24" stroke="#3b2a1a" stroke-width="5" stroke-linecap="round"/>'
        '<path d="M22 50 L32 50 M42 50 L52 50 M62 50 L72 50 M22 64 L32 64 M42 64 L52 64 M22 78 L32 78" stroke="#AEB8C4" stroke-width="4"/><circle cx="67" cy="69" r="10" fill="none" stroke="#E8574A" stroke-width="3"/>'),
 # ---------- society ----------
 "unemployment": dict(words=["البطالة", "التحديات الاجتماعية", "فرص العمل"], anim="wobble", face=(50, 64, .34), only=S,
   body='<rect x="8" y="34" width="84" height="54" rx="8" fill="#8B5E3C" {OL}/><path d="M36 34 L36 24 C36 18 64 18 64 24 L64 34" fill="none" stroke="#3b2a1a" stroke-width="5"/>'
        '<circle cx="78" cy="22" r="14" fill="#fff" {OL}/><text direction="ltr" x="78" y="29" text-anchor="middle" font-size="18" font-weight="800" fill="#E8574A" font-family="sans-serif">?</text>'),
 "poverty": dict(words=["الفقر", "مكافحة الفقر", "الفقراء والمحتاجين"], anim="wobble", face=(50, 60, .36), only=S,
   body='<rect x="8" y="30" width="84" height="56" rx="10" fill="#A8774F" {OL}/><path d="M8 42 L80 42" stroke="#8B5E3C" stroke-width="3"/><rect x="62" y="50" width="30" height="20" rx="6" fill="#C9A27A" {OL}/>'
        '<path d="M30 20 L40 30 M60 20 L50 30" stroke="#AEB8C4" stroke-width="3" stroke-linecap="round"/><path d="M22 92 C30 86 40 96 48 90" fill="none" stroke="#AEB8C4" stroke-width="3"/>'),
 "scarcity": dict(words=["الندرة", "ندرة الموارد", "الموارد المحدودة"], anim="wobble", face=(50, 74, .32), only=S + ["finance"],
   body='<path d="M10 44 L90 44 L80 94 L20 94Z" fill="#C98A55" {OL}/><path d="M10 44 L90 44" stroke="#8B5E3C" stroke-width="6"/><circle cx="50" cy="36" r="10" fill="#E8574A" {OL}/>'
        '<path d="M50 26 C50 18 54 14 58 12" fill="none" stroke="#8B5E3C" stroke-width="3"/>'),
 "procrastination": dict(words=["التسويف", "تأجيل المهام", "إضاعة الوقت"], anim="wobble", face=(36, 60, .34), only=S + ["life"],
   body='<circle cx="36" cy="60" r="30" fill="#fff" {OL}/><path d="M36 60 L36 40 M36 60 L50 66" stroke="#3b2a1a" stroke-width="4" stroke-linecap="round"/>'
        '<text direction="ltr" x="72" y="26" font-size="16" font-weight="800" fill="#6CB8FF" font-family="sans-serif">z</text><text direction="ltr" x="82" y="16" font-size="12" font-weight="800" fill="#6CB8FF" font-family="sans-serif">z</text><text direction="ltr" x="64" y="38" font-size="20" font-weight="800" fill="#6CB8FF" font-family="sans-serif">Z</text>'),
 "follow_up": dict(words=["المتابعة", "متابعة الإنجاز", "متابعة المهام"], anim="bob", face=(30, 70, .3), only=S + ["life"],
   body='<rect x="8" y="10" width="60" height="84" rx="6" fill="#fff" {OL}/><path d="M18 28 L24 34 L34 22 M18 50 L24 56 L34 44" fill="none" stroke="#6CC27A" stroke-width="4" stroke-linecap="round"/><rect x="18" y="66" width="14" height="14" fill="none" stroke="#3b2a1a" stroke-width="2"/>'
        '<path d="M74 30 C90 34 96 54 84 66 M80 60 L84 68 L92 62" fill="none" stroke="#6CB8FF" stroke-width="4" stroke-linecap="round"/>'),
 "hobbies": dict(words=["الهوايات", "أنواع الهوايات", "الهوايات الرياضية", "الهوايات الثقافية", "وقت الفراغ", "الهواية"], anim="bounce", face=(30, 34, .32), only=S + ["life", "english"],
   body='<circle cx="30" cy="34" r="22" fill="#fff" {OL}/><path d="M30 12 L42 24 L38 42 L22 42 L18 24Z" fill="#3b2a1a"/>'
        '<rect x="56" y="14" width="38" height="28" rx="3" fill="#F2D07A" {OL}/><path d="M60 22 L90 22 M60 30 L84 30" stroke="#C98A55" stroke-width="2"/>'
        '<path d="M14 92 C14 70 46 62 60 72 C70 80 64 94 52 94Z" fill="#F2D07A" {OL}/><circle cx="26" cy="80" r="4" fill="#E8574A"/><circle cx="38" cy="74" r="4" fill="#6CB8FF"/><circle cx="48" cy="84" r="4" fill="#6CC27A"/><path d="M72 60 L92 96" stroke="#C98A55" stroke-width="5" stroke-linecap="round"/>'),
 "self_identity": dict(words=["الهوية الذاتية", "معرفة الذات"], anim="bob", face=(46, 42, .36), only=S + ["english"],
   body='<ellipse cx="46" cy="44" rx="34" ry="40" fill="#BFE3F2" {OL}/><ellipse cx="46" cy="44" rx="26" ry="32" fill="#E8F6FF" {OL}/><path d="M46 84 L46 94 M30 96 L62 96" stroke="#8B5E3C" stroke-width="5" stroke-linecap="round"/>'
        '<path d="M30 26 C34 20 40 18 46 18" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round"/><path d="M84 20 L88 28 L96 30 L90 36 L92 44 L84 40 L76 44 L78 36 L72 30 L80 28Z" fill="#FFD25A" {OL}/>'),
 "lifelong": dict(words=["التعلم المستمر", "التعلم مدى الحياة", "طلب العلم"], anim="sun", face=(50, 60, .34), only=S + ["life", "english"],
   body='<path d="M8 40 C24 32 40 34 50 42 C60 34 76 32 92 40 L92 88 C76 80 60 82 50 90 C40 82 24 80 8 88Z" fill="#fff" {OL}/><path d="M50 42 L50 90" stroke="#3b2a1a" stroke-width="2.6"/>'
        '<path d="M30 16 C30 6 46 6 50 16 C54 26 70 26 70 16 C70 6 54 6 50 16 C46 26 30 26 30 16Z" fill="none" stroke="#6CB8FF" stroke-width="4"/>'),
 "geography": dict(words=["علم الجغرافيا", "الجغرافيا الطبيعية", "الجغرافيا البشرية", "فروع الجغرافيا", "تطور علم الجغرافيا", "الجغرافيا عند الإغريق", "الجغرافيا الحديثة",
                          "الجغرافيون المسلمون", "الخرائط عند المسلمين", "الجغرافيون"], anim="sun", face=(50, 40, .36), only=S,
   body='<circle cx="50" cy="40" r="32" fill="#6CB8FF" {OL}/><path d="M28 28 C36 20 48 26 44 36 C40 44 28 40 28 28Z M56 44 C66 38 76 46 70 56 C64 64 54 58 56 44Z" fill="#9CD86C" {OL}/>'
        '<path d="M18 40 C18 66 82 66 82 40" fill="none" stroke="#C98A55" stroke-width="4"/><path d="M50 72 L50 88 M30 94 L70 94" stroke="#8B5E3C" stroke-width="6" stroke-linecap="round"/>'),
 "celestial": dict(words=["الأجرام السماوية", "النجوم والكواكب", "الكون والنجوم"], anim="sun", face=(36, 54, .36), only=S + ["english"],
   body='<rect x="2" y="2" width="96" height="96" rx="10" fill="#1F2A44" {OL}/><circle cx="36" cy="54" r="22" fill="#F2C46D" {OL}/><path d="M10 64 C30 50 50 46 64 46" fill="none" stroke="#C98A55" stroke-width="3"/>'
        '<path d="M76 16 L80 26 L90 28 L82 34 L84 44 L76 38 L68 44 L70 34 L62 28 L72 26Z" fill="#FFD25A" {OL}/><circle cx="20" cy="18" r="2" fill="#fff"/><circle cx="84" cy="76" r="5" fill="#E8853C" {OL}/>'),
}
ALIAS_ONLY = None
ALIASES = {"التركيب العمري": ("soc.population", ("social", "science")), "الهرم السكاني": ("soc.population", ("social", "science")), "الجدول الزمني": ("soc.timeline", ("social",)), "حقل الغوار": ("earth.oil", ("social",)), "الجبيل": ("civ.industrial_port", ("social",)),
           "ينبع": ("civ.industrial_port", ("social",)), "مبادرة السعودية الخضراء": ("eco.restoration", ("social",)), "العالم العربي": ("geo.political_map", ("social",)),
           "الدول العربية": ("geo.political_map", ("social",)), "الدول المستقلة": ("geo.political_map", ("social",)), "الشعب": ("geo.crowded", ("social",)),
           "المواطنون والمقيمون": ("geo.crowded", ("social",)), "التوزيع": ("geo.crowded", ("social",)),
           "عام 1139هـ (1727م)": ("civ.calendar_date", ("social",)), "عام 1240هـ": ("civ.calendar_date", ("social",)), "عام 1351هـ (1932م)": ("civ.calendar_date", ("social",)),
           "عام 1401هـ (1981م)": ("civ.calendar_date", ("social",)), "عام 1309هـ": ("civ.calendar_date", ("social",)), "22 فبراير": ("civ.calendar_date", ("social",)),
           "23 سبتمبر": ("civ.calendar_date", ("social",)), "11 مارس": ("civ.calendar_date", ("social",)), "العمل": ("money.job", ("social",)),
           "المهارات": ("money.skills", ("social",)), "العلوم والمعارف": ("tech.knowledge", ("social",)), "الجانب العلمي": ("tech.knowledge", ("social",)),
           "الازدهار العلمي": ("tech.knowledge", ("social",)), "الطمأنينة": ("day.calm", ("social",))}
