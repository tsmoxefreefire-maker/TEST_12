"""🆕 batch 43 · the earth and space (علوم الأرض والفضاء، وجغرافيا الدراسات الاجتماعية): the life of stars and the universe, orbits,
the sun's storms and the aurora, telescopes; minerals and rocks (Mohs, streak, felsic/mafic, sediments, the rock cycle); the moving
plates (Pangaea, ridges and trenches, the three boundaries, convection); volcanoes and earthquakes (waves, focus and epicentre,
the seismograph, the tsunami); fossils and geologic time; oil, water and minerals underground; maps, contour lines, the
atmosphere and the weather, oceans and the world's natural regions."""
F = "geo"
E = ["science", "social"]          # earth science and general science books + the geography of social studies
D = {
 # ---------- the universe ----------
 "big_bang": dict(words=["نظرية الانفجار العظيم", "الانفجار العظيم", "نشأة الكون", "تمدد الكون"], anim="sun", face=(50, 50, .36), only=E,
   body='<circle cx="50" cy="50" r="46" fill="#1F2A44" {OL}/><path d="M50 50 L50 10 M50 50 L86 30 M50 50 L88 66 M50 50 L58 90 M50 50 L18 82 M50 50 L10 42 M50 50 L28 12" stroke="#FFD25A" stroke-width="3" stroke-dasharray="3 4"/>'
        '<circle cx="50" cy="50" r="12" fill="#FFF3C4" {OL}/><circle cx="50" cy="10" r="3" fill="#fff"/><circle cx="86" cy="30" r="3" fill="#F59BB8"/><circle cx="88" cy="66" r="3" fill="#6CB8FF"/><circle cx="18" cy="82" r="3" fill="#fff"/><circle cx="10" cy="42" r="3" fill="#FFD25A"/>'),
 "redshift": dict(words=["الانزياح نحو الأحمر", "الانزياح الأحمر", "ابتعاد المجرات"], anim="sway", face=(22, 50, .32), only=E,
   body='<rect x="2" y="10" width="96" height="80" rx="8" fill="#1F2A44" {OL}/><ellipse cx="22" cy="50" rx="14" ry="8" fill="#B0A8C9" {OL}/>'
        '<path d="M40 50 C44 40 48 40 52 50 C58 62 64 62 70 50 C76 38 84 38 92 50" fill="none" stroke="#E8574A" stroke-width="4" stroke-linecap="round"/><path d="M80 70 L94 70 M88 64 L94 70 L88 76" fill="none" stroke="#fff" stroke-width="3"/>'),
 "nebula": dict(words=["السديم", "السدم", "سحابة الغاز والغبار"], anim="sway", face=(50, 50, .4), only=E,
   body='<path d="M10 54 C4 30 26 18 40 26 C50 8 80 12 82 32 C98 38 96 66 78 70 C72 90 40 92 34 76 C16 80 4 70 10 54Z" fill="#B565C9" opacity=".85" {OL}/>'
        '<path d="M24 50 C34 36 54 40 60 30 C70 40 80 50 70 60 C56 70 34 66 24 50Z" fill="#F59BB8"/><circle cx="46" cy="46" r="3" fill="#fff"/><circle cx="64" cy="54" r="2" fill="#fff"/><circle cx="30" cy="62" r="2" fill="#FFD25A"/>'),
 "white_dwarf": dict(words=["القزم الأبيض", "الأقزام البيضاء", "دورة حياة النجم", "حياة النجوم"], anim="sun", face=(50, 50, .4), only=E,
   body='<rect x="2" y="2" width="96" height="96" rx="10" fill="#1F2A44" {OL}/><circle cx="50" cy="50" r="16" fill="#fff" {OL}/><circle cx="50" cy="50" r="24" fill="none" stroke="#BFE3F2" stroke-width="2" opacity=".7"/>'
        '<circle cx="18" cy="20" r="2" fill="#fff"/><circle cx="82" cy="26" r="2" fill="#fff"/><circle cx="76" cy="82" r="2" fill="#fff"/>'),
 "supernova": dict(words=["المستعر الأعظم", "انفجار النجم", "السوبرنوفا"], anim="sun", face=(50, 50, .38), only=E,
   body='<path d="M50 2 L58 34 L90 18 L68 44 L98 52 L66 60 L84 90 L54 70 L48 98 L40 68 L10 86 L30 58 L2 48 L32 40 L16 12 L44 30Z" fill="#F6B73C" {OL}/>'
        '<circle cx="50" cy="50" r="16" fill="#FFF3C4" {OL}/>'),
 "black_hole": dict(words=["الثقب الأسود", "الثقوب السوداء"], anim="sun", face=(50, 50, .4), only=E,
   body='<ellipse cx="50" cy="50" rx="46" ry="20" fill="#F6A23C" {OL}/><ellipse cx="50" cy="50" rx="34" ry="12" fill="#E8574A"/><circle cx="50" cy="50" r="20" fill="#111" {OL}/>'
        '<path d="M14 46 C30 36 70 36 86 46" fill="none" stroke="#FFD25A" stroke-width="2"/>'),
 "orbit": dict(words=["الحضيض", "الأوج", "الحضيض والأوج", "المدار الإهليلجي", "قوانين كبلر"], anim="sun", face=(40, 50, .36), only=E,
   body='<ellipse cx="50" cy="50" rx="46" ry="30" fill="none" stroke="#6CB8FF" stroke-width="3" stroke-dasharray="5 4"/><circle cx="34" cy="50" r="14" fill="#FFD25A" {OL}/>'
        '<circle cx="6" cy="50" r="6" fill="#6CB8FF" {OL}/><circle cx="94" cy="50" r="6" fill="#6CB8FF" {OL}/>'),
 "eccentric": dict(words=["الاختلاف المركزي", "شكل المدار"], anim="sun", face=(30, 50, .3), only=E,
   body='<ellipse cx="50" cy="50" rx="44" ry="22" fill="#E8F6FF" {OL}/><circle cx="30" cy="50" r="5" fill="#FFD25A" {OL}/><circle cx="70" cy="50" r="5" fill="none" stroke="#3b2a1a" stroke-width="2"/><circle cx="50" cy="50" r="2.6" fill="#E8574A"/>'
        '<path d="M50 50 L30 50" stroke="#E8574A" stroke-width="2.4"/>'),
 "au": dict(words=["الوحدة الفلكية", "المسافات الفلكية", "السنة الضوئية"], anim="sun", face=(20, 50, .36), only=E,
   body='<circle cx="20" cy="50" r="16" fill="#FFD25A" {OL}/><circle cx="84" cy="50" r="8" fill="#6CB8FF" {OL}/><path d="M38 50 L74 50" stroke="#3b2a1a" stroke-width="3"/><path d="M42 44 L36 50 L42 56 M70 44 L76 50 L70 56" fill="none" stroke="#3b2a1a" stroke-width="3"/>'
        '<text direction="ltr" x="56" y="38" text-anchor="middle" font-size="12" font-weight="800" fill="#3b2a1a" font-family="sans-serif">1 AU</text>'),
 "probe": dict(words=["المسبار الفضائي", "المسابير الفضائية", "استكشاف الفضاء", "المركبة الفضائية"], anim="bob", face=(50, 50, .34), only=E,
   body='<rect x="38" y="38" width="24" height="24" rx="3" fill="#F6B73C" {OL}/><rect x="4" y="42" width="30" height="16" fill="#3b5d9c" {OL}/><rect x="66" y="42" width="30" height="16" fill="#3b5d9c" {OL}/>'
        '<path d="M34 50 L38 50 M62 50 L66 50 M50 38 L50 24" stroke="#3b2a1a" stroke-width="3"/><path d="M38 20 C44 12 56 12 62 20Z" fill="#C9D2DC" {OL}/><path d="M14 42 L14 58 M24 42 L24 58 M76 42 L76 58 M86 42 L86 58" stroke="#6CB8FF" stroke-width="1.6"/>'),
 "escape": dict(words=["سرعة الإفلات", "الإفلات من الجاذبية"], anim="bounce", face=(66, 32, .3), only=E,
   body='<path d="M0 100 C10 70 40 60 60 70 L100 100Z" fill="#6CB8FF" {OL}/><path d="M60 58 L76 18 L86 50Z" fill="#E8574A" {OL}/><path d="M70 30 C78 24 88 30 84 40Z" fill="#fff" {OL}/>'
        '<path d="M64 56 C58 64 58 72 52 78" fill="none" stroke="#F6B73C" stroke-width="4" stroke-linecap="round"/>'),
 "retrograde": dict(words=["الحركة التراجعية", "الحركة الظاهرية للكواكب"], anim="sway", face=(80, 46, .32), only=E,
   body='<rect x="2" y="10" width="96" height="80" rx="8" fill="#1F2A44" {OL}/><path d="M8 60 C26 56 36 40 48 40 C62 40 58 60 48 58 C38 56 46 36 62 40 C74 44 82 50 92 46" fill="none" stroke="#FFD25A" stroke-width="3" stroke-dasharray="4 3"/>'
        '<circle cx="80" cy="46" r="8" fill="#E8853C" {OL}/>'),
 "saturn": dict(words=["زحل وحلقاته", "زحل", "حلقات زحل", "الكواكب الغازية العملاقة", "المشتري"], anim="sun", face=(50, 50, .4), only=E,
   body='<ellipse cx="50" cy="52" rx="48" ry="14" fill="none" stroke="#C98A55" stroke-width="5" transform="rotate(-15 50 52)"/><circle cx="50" cy="50" r="26" fill="#F2C46D" {OL}/>'
        '<path d="M26 42 C40 38 60 38 74 42 M25 54 C40 58 60 58 75 54" fill="none" stroke="#C98A55" stroke-width="2.4"/><path d="M4 64 C30 58 70 46 96 40" fill="none" stroke="#C98A55" stroke-width="5"/>'),
 "ice_giants": dict(words=["أورانوس ونبتون", "أورانوس", "نبتون", "الكواكب الخارجية"], anim="sun", face=(36, 44, .36), only=E,
   body='<circle cx="36" cy="44" r="26" fill="#9FE0E6" {OL}/><path d="M36 14 L36 74" stroke="#7CC6D0" stroke-width="2"/><circle cx="76" cy="74" r="18" fill="#3B6FD9" {OL}/><path d="M62 70 C70 66 82 66 90 70" fill="none" stroke="#2A54B0" stroke-width="3"/>'),
 "sun_layers": dict(words=["الكروموسفير", "الهالة الشمسية", "طبقات الشمس", "الفوتوسفير", "الإكليل الشمسي"], anim="sun", face=(50, 50, .4), only=E,
   body='<circle cx="50" cy="50" r="46" fill="#FFF3C4" opacity=".7"/><circle cx="50" cy="50" r="38" fill="#F6A23C" {OL}/><circle cx="50" cy="50" r="30" fill="#FFD25A" {OL}/><circle cx="50" cy="50" r="46" fill="none" stroke="#F6B73C" stroke-width="2" stroke-dasharray="3 5"/>'),
 "sunspots": dict(words=["البقع الشمسية", "الدورة الشمسية", "النشاط الشمسي"], anim="sun", face=(50, 66, .36), only=E,
   body='<circle cx="50" cy="50" r="44" fill="#FFB43C" {OL}/><circle cx="34" cy="34" r="7" fill="#8B4A1A"/><circle cx="34" cy="34" r="11" fill="none" stroke="#C26A28" stroke-width="3"/><circle cx="66" cy="42" r="5" fill="#8B4A1A"/><circle cx="58" cy="30" r="3" fill="#8B4A1A"/>'),
 "solar_flare": dict(words=["التوهجات الشمسية", "الشواظ الشمسية", "الانبعاثات الكتلية الإكليلية", "العواصف الشمسية", "الرياح الشمسية"], anim="sun", face=(40, 60, .38), only=E,
   body='<circle cx="40" cy="60" r="36" fill="#FFB43C" {OL}/><path d="M56 30 C64 6 92 6 92 30 C92 44 78 46 72 38" fill="none" stroke="#E8574A" stroke-width="7" stroke-linecap="round"/>'
        '<path d="M72 38 L68 44" stroke="#E8574A" stroke-width="7" stroke-linecap="round"/>'),
 "aurora": dict(words=["الشفق القطبي", "الأضواء القطبية"], anim="wind", face=(50, 84, .3), only=E,
   body='<rect x="2" y="2" width="96" height="96" rx="10" fill="#1F2A44" {OL}/><path d="M10 50 C20 20 30 60 42 30 C52 8 62 50 74 24 C82 10 88 30 92 22 L92 60 C80 64 60 70 40 64 C26 60 16 66 10 60Z" fill="#6CE0A0" opacity=".8"/>'
        '<path d="M2 80 L30 70 L50 78 L76 66 L98 76 L98 98 L2 98Z" fill="#E8F2F8" {OL}/><circle cx="20" cy="14" r="2" fill="#fff"/><circle cx="80" cy="10" r="2" fill="#fff"/>'),
 "infrared": dict(words=["الأشعة تحت الحمراء", "الأشعة فوق البنفسجية", "الطيف الكهرومغناطيسي"], anim="sway", face=(22, 50, .32), only=E,
   body='<circle cx="22" cy="50" r="16" fill="#E8574A" {OL}/><path d="M42 50 C48 34 54 34 60 50 C66 66 72 66 78 50 C84 34 90 34 96 50" fill="none" stroke="#B5332A" stroke-width="4"/>'
        '<path d="M42 30 C48 18 54 18 60 30 M42 70 C48 82 54 82 60 70" fill="none" stroke="#E8853C" stroke-width="2.4"/>'),
 "xray": dict(words=["الأشعة السينية وأشعة جاما", "الأشعة السينية", "أشعة جاما", "صور الأشعة"], anim="buzz", face=(50, 84, .3),
   body='<rect x="10" y="6" width="80" height="88" rx="6" fill="#1F2A44" {OL}/><path d="M40 86 L40 54 L30 30 M40 54 L44 22 M46 54 L54 18 M50 56 L64 24 M54 60 L74 40" fill="none" stroke="#E8F2F8" stroke-width="5" stroke-linecap="round"/>'),
 "refractor": dict(words=["المنظار الكاسر", "المنظار العاكس", "المنظار الفلكي", "المناظير الفضائية"], anim="bob", face=(42, 34, .32),
   body='<rect x="8" y="22" width="72" height="20" rx="6" fill="#6CB8FF" {OL} transform="rotate(-20 44 32)"/><rect x="74" y="8" width="16" height="22" rx="4" fill="#3b5d9c" {OL} transform="rotate(-20 82 19)"/>'
        '<path d="M44 46 L28 94 M44 46 L60 94 M44 46 L44 94" stroke="#8B5E3C" stroke-width="4" stroke-linecap="round"/>'),
 "radio_telescope": dict(words=["المنظار الراديوي", "المنظار التداخلي", "التلسكوب الراديوي", "الأطباق الراديوية"], anim="bob", face=(46, 34, .32), only=E,
   body='<path d="M10 20 C20 60 70 70 90 40 Z" fill="#E8F2F8" {OL}/><path d="M50 50 L66 22" stroke="#3b2a1a" stroke-width="3"/><circle cx="66" cy="20" r="4" fill="#E8574A" {OL}/>'
        '<path d="M50 52 L40 94 M50 52 L64 94 M34 94 L70 94" stroke="#5D646E" stroke-width="5" stroke-linecap="round"/>'),
 # ---------- minerals and rocks ----------
 "mohs": dict(words=["مقياس موس", "صلادة المعادن", "مقياس الصلادة"], anim="bob", face=(50, 26, .32), only=E,
   body='<rect x="4" y="44" width="92" height="22" rx="4" fill="#fff" {OL}/><path d="M13 44 L13 66 M22 44 L22 66 M31 44 L31 66 M40 44 L40 66 M50 44 L50 66 M59 44 L59 66 M68 44 L68 66 M77 44 L77 66 M86 44 L86 66" stroke="#AEB8C4" stroke-width="1.6"/>'
        '<path d="M4 66 L96 44" stroke="#E8574A" stroke-width="2"/><path d="M50 4 L62 18 L50 34 L38 18Z" fill="#9FD8F0" {OL}/><text direction="ltr" x="10" y="84" font-size="12" font-weight="800" fill="#3b2a1a" font-family="sans-serif">1</text><text direction="ltr" x="84" y="84" font-size="12" font-weight="800" fill="#3b2a1a" font-family="sans-serif">10</text>'),
 "streak": dict(words=["المخدش", "لون المخدش", "خصائص المعادن"], anim="wiggle", face=(30, 34, .32), only=E,
   body='<rect x="6" y="50" width="88" height="40" rx="4" fill="#fff" {OL}/><path d="M24 70 L80 64" stroke="#8B3A2B" stroke-width="8" stroke-linecap="round"/>'
        '<path d="M18 16 L42 8 L52 30 L36 46 L14 38Z" fill="#5D4E4E" {OL}/>'),
 "cleavage": dict(words=["الانفصام والمكسر", "الانفصام", "المكسر", "التشقق"], anim="wobble", face=(30, 56, .32), only=E,
   body='<path d="M8 40 L40 30 L50 60 L18 70Z" fill="#9FD8F0" {OL}/><path d="M58 30 L92 24 L86 52 L60 58Z" fill="#9FD8F0" {OL}/><path d="M54 70 C62 64 70 76 78 68 C84 62 90 72 94 66 L94 92 L54 92Z" fill="#C9D2DC" {OL}/>'
        '<path d="M44 46 L54 42" stroke="#3b2a1a" stroke-width="2" stroke-dasharray="3 2"/>'),
 "ore": dict(words=["الخام", "الأكاسيد", "الكبريتات والهاليدات", "العناصر الطبيعية", "خامات المعادن", "مجموعات المعادن"], anim="wobble", face=(50, 60, .42), only=E,
   body='<path d="M10 70 L18 34 L44 18 L78 26 L92 58 L76 88 L26 90Z" fill="#7A6A5A" {OL}/><path d="M30 40 L38 36 L40 44Z M60 34 L70 38 L64 46Z M70 66 L78 62 L76 72Z M36 70 L44 66 L42 76Z" fill="#FFD25A" {OL}/>'),
 "felsic_mafic": dict(words=["الصخور الفلسية", "الصخور المافية", "الصخور فوق المافية", "تصنيف الصخور النارية"], anim="wobble", face=(30, 56, .32), only=E,
   body='<path d="M4 76 L8 42 L28 30 L48 40 L50 78 L30 88Z" fill="#E8D8C8" {OL}/><path d="M50 78 L52 40 L72 28 L94 38 L96 76 L74 88Z" fill="#3D3636" {OL}/>'
        '<circle cx="20" cy="56" r="2.4" fill="#C9A27A"/><circle cx="36" cy="66" r="2.4" fill="#F59BB8"/><circle cx="70" cy="50" r="2.4" fill="#6CC27A"/><circle cx="82" cy="66" r="2.4" fill="#111"/>'),
 "lithify": dict(words=["الرسوبيات", "التصخر", "السمنتة", "التطبق", "التطبق المتقاطع", "الدفن السريع", "التضاغط", "تكون الصخور الرسوبية"], anim="bob", face=(50, 30, .32), only=E,
   body='<path d="M50 4 L50 18 M44 12 L50 20 L56 12" fill="none" stroke="#3b2a1a" stroke-width="3"/><rect x="6" y="24" width="88" height="70" rx="4" fill="#E6C08A" {OL}/>'
        '<path d="M6 42 L94 40 M6 58 L94 58 M6 76 L94 76" stroke="#B88A50" stroke-width="5"/><circle cx="20" cy="32" r="3" fill="#C98A55"/><circle cx="40" cy="50" r="3" fill="#C98A55"/><circle cx="70" cy="66" r="3" fill="#C98A55"/><circle cx="84" cy="86" r="3" fill="#C98A55"/>'),
 "conglomerate": dict(words=["الكونجلوميرات", "البريشيا", "الحصى المتماسك"], anim="wobble", face=(50, 50, .36), only=E,
   body='<path d="M8 74 L14 34 L46 16 L82 24 L94 62 L72 90 L24 90Z" fill="#D8C49A" {OL}/><ellipse cx="32" cy="40" rx="9" ry="6" fill="#AEB8C4" {OL}/><ellipse cx="66" cy="38" rx="8" ry="6" fill="#C98A55" {OL}/>'
        '<ellipse cx="30" cy="70" rx="8" ry="6" fill="#8B5E3C" {OL}/><ellipse cx="72" cy="70" rx="10" ry="6" fill="#AEB8C4" {OL}/>'),
 "evaporite": dict(words=["المتبخرات", "الملح الصخري", "السبخات", "السبخة"], anim="sun", face=(50, 70, .36), only=E,
   body='<circle cx="80" cy="18" r="10" fill="#FFD25A" {OL}/><path d="M4 56 C24 48 76 48 96 56 L96 92 L4 92Z" fill="#E8D8C8" {OL}/>'
        '<path d="M14 60 L20 54 L26 60 L32 54 L38 60 M58 60 L64 54 L70 60 L76 54 L82 60" fill="#fff" stroke="#AEB8C4" stroke-width="2"/><path d="M40 70 C50 66 60 74 70 70" fill="none" stroke="#7CC6F2" stroke-width="3"/>'),
 "foliated": dict(words=["الصخور المتورقة", "الصخور غير المتورقة", "التورق", "التحول الصخري"], anim="wobble", face=(50, 56, .36), only=E,
   body='<path d="M8 74 L16 30 L58 16 L90 36 L88 78 L44 92Z" fill="#B0A8C9" {OL}/><path d="M14 44 C34 36 54 50 88 42 M12 56 C34 48 56 62 88 54 M12 68 C34 60 56 74 88 66" fill="none" stroke="#5E5480" stroke-width="3"/>'),
 "rock_cycle": dict(words=["الدورة الصخرية", "دورة الصخور"], anim="sun", face=(50, 50, .34),
   body='<circle cx="50" cy="16" r="12" fill="#5D4E4E" {OL}/><circle cx="84" cy="74" r="12" fill="#E6C08A" {OL}/><circle cx="16" cy="74" r="12" fill="#B0A8C9" {OL}/>'
        '<path d="M64 20 C80 30 86 44 86 58 M70 84 C56 94 44 94 30 84 M12 58 C12 44 20 30 36 20" fill="none" stroke="#E8574A" stroke-width="4" stroke-linecap="round"/>'
        '<path d="M80 54 L86 62 L92 54 M36 80 L28 86 L36 92 M30 24 L38 18 L32 12" fill="none" stroke="#E8574A" stroke-width="3"/>'),
 # ---------- the moving plates ----------
 "pangaea": dict(words=["بانجيا", "زحزحة القارات", "انجراف القارات", "القارة الأم"], anim="sway", face=(46, 50, .4), only=E,
   body='<circle cx="50" cy="50" r="46" fill="#6CB8FF" {OL}/><path d="M28 18 C44 10 64 16 70 30 C80 34 82 50 72 58 C70 74 56 86 44 80 C34 76 36 64 28 60 C16 54 14 38 22 32 C22 26 24 20 28 18Z" fill="#9CD86C" {OL}/>'
        '<path d="M44 26 C48 40 40 50 50 62" fill="none" stroke="#5A9A3A" stroke-width="2" stroke-dasharray="3 3"/>'),
 "ridge": dict(words=["الحيود المحيطية", "توسع قاع المحيط", "اتساع قاع المحيط", "عمر صخور قاع المحيط", "الحيد المحيطي", "ظهر المحيط"], anim="sway", face=(50, 78, .32), only=E,
   body='<rect x="2" y="2" width="96" height="40" fill="#7CC6F2" {OL}/><path d="M2 42 L40 42 L46 30 L50 36 L54 30 L60 42 L98 42 L98 96 L2 96Z" fill="#B48B65" {OL}/>'
        '<path d="M50 96 L50 44" stroke="#E8574A" stroke-width="4"/><path d="M38 62 L16 62 M22 56 L16 62 L22 68 M62 62 L84 62 M78 56 L84 62 L78 68" fill="none" stroke="#3b2a1a" stroke-width="3"/>'),
 "trench": dict(words=["الأخاديد المحيطية", "منطقة الاندساس", "الاندساس", "الأخدود المحيطي"], anim="wobble", face=(76, 30, .32), only=E,
   body='<rect x="2" y="2" width="56" height="40" fill="#7CC6F2" {OL}/><path d="M2 42 L50 42 L60 60 L98 98 L2 98Z" fill="#8A7A6A" {OL}/><path d="M58 42 L60 10 L98 22 L98 98 L60 60Z" fill="#C9A27A" {OL}/>'
        '<path d="M30 70 L50 86 M44 86 L50 86 L48 80" fill="none" stroke="#E8574A" stroke-width="3"/>'),
 "sonar": dict(words=["السونار", "قياس عمق المحيط", "الموجات فوق الصوتية"], anim="buzz", face=(50, 20, .3), only=E,
   body='<rect x="2" y="30" width="96" height="66" fill="#7CC6F2" {OL}/><path d="M30 30 L70 30 L64 40 L36 40Z" fill="#E8574A" {OL}/><path d="M46 30 L46 16 L60 22 L46 26" fill="#fff" {OL}/>'
        '<path d="M40 50 C44 54 56 54 60 50 M34 62 C42 70 58 70 66 62 M28 74 C40 86 60 86 72 74" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/><path d="M2 92 L30 86 L60 92 L98 86" fill="none" stroke="#8A7A6A" stroke-width="5"/>'),
 "divergent": dict(words=["الحدود المتباعدة", "تباعد الصفائح"], anim="wobble", face=(50, 30, .3), only=E,
   body='<path d="M2 50 L44 50 L44 90 L2 90Z" fill="#C9A27A" {OL}/><path d="M56 50 L98 50 L98 90 L56 90Z" fill="#B48B65" {OL}/><path d="M44 50 C48 40 52 40 56 50" fill="#E8574A" {OL}/>'
        '<path d="M34 26 L10 26 M16 20 L10 26 L16 32 M66 26 L90 26 M84 20 L90 26 L84 32" fill="none" stroke="#3b2a1a" stroke-width="4" stroke-linecap="round"/>'),
 "convergent": dict(words=["الحدود المتقاربة", "تقارب الصفائح", "تكون الجبال"], anim="wobble", face=(50, 70, .3), only=E,
   body='<path d="M2 60 L40 60 L50 26 L60 60 L98 60 L98 94 L2 94Z" fill="#B48B65" {OL}/><path d="M42 54 L50 26 L58 54" fill="#9C8C7A" {OL}/>'
        '<path d="M6 40 L30 40 M24 34 L30 40 L24 46 M94 40 L70 40 M76 34 L70 40 L76 46" fill="none" stroke="#3b2a1a" stroke-width="4" stroke-linecap="round"/>'),
 "transform_b": dict(words=["الحدود التحويلية", "الحدود الجانبية", "الصدوع التحويلية"], anim="wobble", face=(30, 50, .3), only=E,
   body='<path d="M2 10 L48 10 L48 90 L2 90Z" fill="#C9A27A" {OL}/><path d="M52 10 L98 10 L98 90 L52 90Z" fill="#B48B65" {OL}/>'
        '<path d="M26 70 L26 30 M20 36 L26 28 L32 36 M74 30 L74 70 M68 64 L74 72 L80 64" fill="none" stroke="#3b2a1a" stroke-width="4" stroke-linecap="round"/>'),
 "convection": dict(words=["تيارات الحمل", "الحمل الحراري", "تيارات الحمل في الوشاح"], anim="sun", face=(50, 50, .34), only=E,
   body='<rect x="2" y="2" width="96" height="96" rx="8" fill="#F6A23C" {OL}/><path d="M20 70 C20 30 46 30 46 50 C46 70 20 70 20 50 M80 30 C80 70 54 70 54 50 C54 30 80 30 80 50" fill="none" stroke="#E8574A" stroke-width="4" stroke-linecap="round"/>'
        '<path d="M2 14 L98 14" stroke="#8A7A6A" stroke-width="8"/>'),
 # ---------- volcanoes and earthquakes ----------
 "caldera": dict(words=["الفوهة", "الكالديرا", "فوهة البركان", "المخروط البركاني"], anim="wobble", face=(50, 70, .36), only=E,
   body='<path d="M2 94 L30 34 L42 44 L58 44 L70 34 L98 94Z" fill="#8A7A6A" {OL}/><path d="M30 34 C36 46 64 46 70 34 C64 28 36 28 30 34Z" fill="#E8574A" {OL}/>'
        '<path d="M44 26 C40 18 48 14 44 6 M56 26 C52 18 60 14 56 6" fill="none" stroke="#AEB8C4" stroke-width="3" stroke-linecap="round"/>'),
 "hotspot": dict(words=["البقعة الساخنة", "البقع الساخنة", "سلسلة الجزر البركانية"], anim="wobble", face=(50, 84, .3), only=E,
   body='<rect x="2" y="2" width="96" height="30" fill="#7CC6F2" {OL}/><path d="M10 32 L16 20 L22 32 M40 32 L48 14 L56 32 M74 32 L84 8 L94 32" fill="#8A7A6A" {OL}/><rect x="2" y="32" width="96" height="30" fill="#B48B65" {OL}/>'
        '<path d="M84 62 C80 70 88 76 84 84 C80 92 86 96 84 98" fill="none" stroke="#E8574A" stroke-width="6" stroke-linecap="round"/><circle cx="84" cy="90" r="8" fill="#F6A23C" {OL}/>'),
 "stress_strain": dict(words=["الإجهاد", "الانفعال", "الإجهاد والانفعال", "الضغط على الصخور"], anim="wobble", face=(50, 50, .34), only=E,
   body='<path d="M26 26 L74 26 C70 40 70 60 74 74 L26 74 C30 60 30 40 26 26Z" fill="#C9A27A" {OL}/>'
        '<path d="M2 50 L20 50 M14 44 L20 50 L14 56 M98 50 L80 50 M86 44 L80 50 L86 56" fill="none" stroke="#E8574A" stroke-width="4" stroke-linecap="round"/>'),
 "seismic_waves": dict(words=["الأمواج الأولية P", "الأمواج الثانوية S", "الأمواج السطحية", "الموجات الزلزالية", "الأمواج الزلزالية"], anim="buzz", face=(14, 50, .3), only=E,
   body='<path d="M4 30 L8 30 M12 30 L14 30 M18 30 L22 30 M26 30 L28 30 M32 30 L36 30 M40 30 L42 30 M46 30 L50 30 M54 30 L56 30 M60 30 L64 30 M68 30 L70 30 M74 30 L78 30 M82 30 L84 30 M88 30 L92 30" stroke="#E8574A" stroke-width="6"/>'
        '<path d="M4 60 C12 48 20 48 28 60 C36 72 44 72 52 60 C60 48 68 48 76 60 C84 72 92 72 96 64" fill="none" stroke="#6CB8FF" stroke-width="4"/><path d="M4 84 L96 84" stroke="#8A7A6A" stroke-width="4"/>'),
 "epicenter": dict(words=["البؤرة والمركز السطحي", "المركز السطحي", "تحديد المركز السطحي", "مركز الزلزال", "البؤرة"], anim="buzz", face=(50, 16, .3), only=E, never=["physics", "math"],
   body='<rect x="2" y="28" width="96" height="70" fill="#B48B65" {OL}/><path d="M2 28 L98 28" stroke="#6CC27A" stroke-width="6"/><circle cx="50" cy="74" r="6" fill="#E8574A" {OL}/>'
        '<circle cx="50" cy="74" r="14" fill="none" stroke="#E8574A" stroke-width="2"/><circle cx="50" cy="74" r="24" fill="none" stroke="#E8574A" stroke-width="2" stroke-dasharray="3 3"/><path d="M50 68 L50 30" stroke="#3b2a1a" stroke-width="2" stroke-dasharray="3 3"/><path d="M42 20 L50 30 L58 20" fill="#FFD25A" {OL}/>'),
 "mercalli": dict(words=["مقياس ميركالي المعدل", "مقياس ميركالي", "شدة الزلزال", "مقياس ريختر", "قوة الزلزال"], anim="wobble", face=(30, 70, .32), only=E,
   body='<path d="M8 94 L8 56 L30 36 L52 56 L52 94Z" fill="#F2D07A" {OL}/><path d="M14 60 L22 72 L18 80 M40 58 L46 70" fill="none" stroke="#3b2a1a" stroke-width="2"/>'
        '<rect x="62" y="10" width="30" height="84" rx="4" fill="#fff" {OL}/><rect x="66" y="70" width="22" height="20" fill="#6CC27A"/><rect x="66" y="46" width="22" height="22" fill="#FFD25A"/><rect x="66" y="16" width="22" height="28" fill="#E8574A"/>'),
 "seismograph": dict(words=["السيزموجراف", "جهاز رصد الزلازل", "السيزموجرام"], anim="buzz", face=(50, 20, .3), only=E,
   body='<rect x="6" y="40" width="88" height="44" rx="22" fill="#fff" {OL}/><path d="M12 62 L30 62 L34 50 L38 74 L42 44 L48 80 L52 52 L56 68 L60 62 L88 62" fill="none" stroke="#E8574A" stroke-width="2.6"/>'
        '<path d="M50 6 L50 40" stroke="#5D646E" stroke-width="4"/><path d="M50 40 L46 50" stroke="#3b2a1a" stroke-width="2"/><rect x="40" y="6" width="20" height="10" fill="#5D646E" {OL}/><path d="M6 94 L94 94" stroke="#5D646E" stroke-width="6"/>'),
 "tsunami": dict(words=["التسونامي", "تسونامي", "الأمواج الزلزالية العاتية"], anim="sway", face=(36, 46, .38), only=E,
   body='<path d="M2 96 L2 60 C2 20 40 4 64 18 C80 26 80 46 66 46 C56 46 56 34 64 32 C52 30 44 44 48 58 C52 72 74 76 98 70 L98 96Z" fill="#4A90D9" {OL}/>'
        '<path d="M66 18 C76 22 80 30 78 38" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round"/><path d="M80 96 L80 82 L90 74 L98 82 L98 96Z" fill="#F2D07A" {OL}/>'),
 # ---------- fossils and time ----------
 "amber": dict(words=["الحفظ في الكهرمان", "الكهرمان", "البقايا الأصلية", "الحفظ في الجليد"], anim="sun", face=(50, 74, .34), only=E,
   body='<path d="M20 30 C30 6 70 6 80 30 C94 60 76 94 50 94 C24 94 6 60 20 30Z" fill="#F6A23C" opacity=".9" {OL}/><ellipse cx="50" cy="48" rx="8" ry="12" fill="#5D3A1A"/>'
        '<path d="M42 40 C30 30 26 40 40 46 M58 40 C70 30 74 40 60 46" fill="#E8F6FF" opacity=".8" stroke="#3b2a1a" stroke-width="1.4"/><path d="M44 58 L38 66 M56 58 L62 66" stroke="#5D3A1A" stroke-width="2"/><path d="M30 24 C36 18 44 16 50 16" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>'),
 "petrify": dict(words=["التمعدن", "التحجر", "الخشب المتحجر", "الأحافير المتحجرة"], anim="wobble", face=(50, 50, .4), only=E,
   body='<path d="M10 30 L90 30 L90 70 L10 70Z" fill="#AEA090" {OL}/><ellipse cx="90" cy="50" rx="10" ry="20" fill="#C9B89A" {OL}/>'
        '<ellipse cx="90" cy="50" rx="6" ry="13" fill="none" stroke="#8A7A6A" stroke-width="2"/><path d="M14 42 L84 40 M14 56 L84 58" stroke="#8A7A6A" stroke-width="2"/>'),
 "mold_cast": dict(words=["القالب", "المصبوب", "القوالب والمصبوبات", "التفحم", "الآثار المتحجرة", "طبعات الأحافير"], anim="wobble", face=(76, 70, .3), only=E,
   body='<rect x="4" y="16" width="44" height="70" rx="6" fill="#C9B89A" {OL}/><path d="M26 30 C14 40 14 66 26 74 C38 66 38 40 26 30Z" fill="#8A7A6A" {OL}/><path d="M26 34 L26 72 M18 46 L34 46 M17 58 L35 58" stroke="#5D4E4E" stroke-width="1.6"/>'
        '<path d="M76 26 C62 36 62 66 76 76 C90 66 90 36 76 26Z" fill="#E6C08A" {OL}/><path d="M76 30 L76 72 M66 44 L86 44 M65 58 L87 58" stroke="#B88A50" stroke-width="2"/>'),
 "paleo_env": dict(words=["البيئات القديمة", "السجل الصخري", "الأحافير المرشدة", "التكوينات الجيولوجية"], anim="bob", face=(50, 24, .3), only=E,
   body='<rect x="4" y="14" width="92" height="80" rx="4" fill="#E6C08A" {OL}/><path d="M4 34 L96 34" stroke="#C98A55" stroke-width="5"/><path d="M4 54 L96 54" stroke="#B0A8C9" stroke-width="5"/><path d="M4 74 L96 74" stroke="#8A7A6A" stroke-width="5"/>'
        '<path d="M22 44 C26 40 30 40 32 44 C30 48 26 48 22 44Z M60 64 C62 58 70 58 72 64" fill="#fff" stroke="#3b2a1a" stroke-width="1.6"/><path d="M74 84 C70 80 74 76 78 80 C82 84 78 88 74 84Z" fill="#fff" stroke="#3b2a1a" stroke-width="1.6"/>'),
 "eon": dict(words=["الدهر", "ما قبل الكمبري", "صخور ما قبل الكمبري", "الزمن الجيولوجي", "مقياس الزمن الجيولوجي", "الحقب الجيولوجية"], anim="sun", face=(50, 50, .36), only=E,
   body='<circle cx="50" cy="50" r="44" fill="#fff" {OL}/><path d="M50 50 L50 6 A44 44 0 1 1 18 20Z" fill="#B0A8C9"/><path d="M50 50 L18 20 A44 44 0 0 1 34 9Z" fill="#9CD86C"/><path d="M50 50 L34 9 A44 44 0 0 1 50 6Z" fill="#F6B73C"/>'
        '<circle cx="50" cy="50" r="44" fill="none" {OL}/><path d="M50 50 L50 20" stroke="#3b2a1a" stroke-width="3"/>'),
 "relative_age": dict(words=["العمر النسبي", "مبدأ الأفقية الأصلية", "مبدأ تعاقب الطبقات", "قانون تعاقب الطبقات", "التأريخ النسبي"], anim="bob", face=(78, 82, .3), only=E,
   body='<rect x="4" y="10" width="92" height="84" rx="4" fill="#E6C08A" {OL}/><rect x="4" y="10" width="92" height="20" fill="#F2D07A" {OL}/><rect x="4" y="30" width="92" height="22" fill="#D8A86A" {OL}/><rect x="4" y="52" width="92" height="20" fill="#B48B65" {OL}/>'
        '<text direction="ltr" x="16" y="25" font-size="12" font-weight="800" fill="#3b2a1a" font-family="sans-serif">3</text><text direction="ltr" x="16" y="46" font-size="12" font-weight="800" fill="#3b2a1a" font-family="sans-serif">2</text><text direction="ltr" x="16" y="67" font-size="12" font-weight="800" fill="#fff" font-family="sans-serif">1</text>'),
 "crosscut": dict(words=["مبدأ العلاقات القاطعة", "العلاقات القاطعة", "القواطع الصخرية"], anim="bob", face=(50, 50, .3), only=E,
   body='<rect x="4" y="10" width="92" height="84" rx="4" fill="#E6C08A" {OL}/><path d="M4 32 L96 32 M4 54 L96 54 M4 74 L96 74" stroke="#B88A50" stroke-width="4"/><path d="M40 94 L54 10 L66 10 L52 94Z" fill="#E8574A" {OL}/>'),
 "unconformity": dict(words=["عدم التوافق", "سطح عدم التوافق", "عدم التوافق الزاوي"], anim="bob", face=(50, 20, .3), only=E,
   body='<rect x="4" y="10" width="92" height="84" rx="4" fill="#E6C08A" {OL}/><path d="M4 60 L30 94 M20 60 L46 94 M38 60 L64 94 M56 60 L82 94 M74 60 L96 88" stroke="#8A7A6A" stroke-width="4"/>'
        '<path d="M4 58 C20 50 34 64 50 56 C64 50 80 62 96 54" fill="none" stroke="#E8574A" stroke-width="5"/><path d="M4 34 L96 34" stroke="#C98A55" stroke-width="4"/>'),
 "correlation_r": dict(words=["المضاهاة", "مضاهاة الطبقات", "مقارنة الطبقات"], anim="bob", face=(50, 10, .3),
   only=E, body='<rect x="6" y="20" width="30" height="74" fill="#E6C08A" {OL}/><rect x="64" y="20" width="30" height="74" fill="#E6C08A" {OL}/>'
        '<rect x="6" y="40" width="30" height="14" fill="#B0A8C9"/><rect x="64" y="54" width="30" height="14" fill="#B0A8C9"/><path d="M36 47 L64 61" stroke="#E8574A" stroke-width="3" stroke-dasharray="4 3"/><rect x="6" y="20" width="30" height="74" fill="none" {OL}/><rect x="64" y="20" width="30" height="74" fill="none" {OL}/>'),
 "absolute_age": dict(words=["العمر المطلق", "التأريخ بالنظائر المشعة", "التأريخ الإشعاعي", "التأريخ بالكربون المشع"], anim="sun", face=(30, 62, .34), only=E,
   body='<circle cx="30" cy="60" r="24" fill="#9CD86C" {OL}/><circle cx="24" cy="54" r="5" fill="#E8574A"/><circle cx="36" cy="58" r="5" fill="#AEB8C4"/><circle cx="28" cy="68" r="5" fill="#E8574A"/>'
        '<circle cx="72" cy="34" r="24" fill="#fff" {OL}/><path d="M72 34 L72 18 M72 34 L84 40" stroke="#3b2a1a" stroke-width="3" stroke-linecap="round"/>'),
 # ---------- underground: oil, water, minerals ----------
 "drilling": dict(words=["الحفر الاستكشافي", "المسح الجاذبي", "التنقيب عن النفط", "الحفارة", "منصة الحفر"], anim="wobble", face=(50, 70, .3), only=E,
   body='<path d="M50 6 L30 70 L70 70Z" fill="none" stroke="#5D646E" stroke-width="5" stroke-linejoin="round"/><path d="M38 40 L62 40 M34 56 L66 56" stroke="#5D646E" stroke-width="4"/>'
        '<path d="M20 70 L80 70" stroke="#3b2a1a" stroke-width="6"/><path d="M50 70 L50 96" stroke="#3b2a1a" stroke-width="3"/><ellipse cx="50" cy="94" rx="14" ry="4" fill="#3b2a1a"/>'),
 "porosity": dict(words=["المسامية", "المسامية والنفاذية"], anim="drip", face=(50, 12, .3), only=E,
   body='<rect x="4" y="22" width="92" height="74" rx="4" fill="#BFE3F2" {OL}/><circle cx="18" cy="36" r="10" fill="#E6C08A" {OL}/><circle cx="42" cy="38" r="11" fill="#E6C08A" {OL}/><circle cx="68" cy="34" r="10" fill="#E6C08A" {OL}/><circle cx="88" cy="40" r="8" fill="#E6C08A" {OL}/>'
        '<circle cx="28" cy="62" r="11" fill="#E6C08A" {OL}/><circle cx="56" cy="62" r="11" fill="#E6C08A" {OL}/><circle cx="80" cy="66" r="10" fill="#E6C08A" {OL}/><circle cx="16" cy="86" r="8" fill="#E6C08A" {OL}/><circle cx="44" cy="86" r="9" fill="#E6C08A" {OL}/><circle cx="72" cy="88" r="8" fill="#E6C08A" {OL}/>'
        '<path d="M50 6 L50 20 M44 14 L50 20 L56 14" fill="none" stroke="#6CB8FF" stroke-width="3"/>'),
 "aquifer": dict(words=["الخزان الجوفي", "الخزانات الجوفية", "الطبقة الحاملة للمياه", "منسوب المياه الجوفية"], anim="drip", face=(50, 66, .34), only=E,
   body='<rect x="2" y="2" width="96" height="20" fill="#9CD86C" {OL}/><rect x="2" y="22" width="96" height="26" fill="#C98A55" {OL}/><rect x="2" y="48" width="96" height="30" fill="#7CC6F2" {OL}/><rect x="2" y="78" width="96" height="20" fill="#8A7A6A" {OL}/>'
        '<path d="M80 2 L80 60" stroke="#5D646E" stroke-width="5"/><path d="M14 60 C24 56 34 64 44 60" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>'),
 "uranium": dict(words=["اليورانيوم", "المواد المشعة", "العناصر المشعة"], anim="buzz", face=(50, 50, .3),
   body='<circle cx="50" cy="50" r="44" fill="#FFD25A" {OL}/><circle cx="50" cy="50" r="8" fill="#3b2a1a"/><path d="M50 40 L36 16 A40 40 0 0 1 64 16Z M59 55 L86 56 A40 40 0 0 1 72 80Z M41 55 L28 80 A40 40 0 0 1 14 56Z" fill="#3b2a1a"/>'),
 "arabian_shield": dict(words=["الدرع العربي", "الرف العربي", "الكتلة القارية"], anim="bob", face=(50, 50, .4), only=E,
   body='<path d="M50 6 L88 18 C88 56 74 80 50 94 C26 80 12 56 12 18Z" fill="#8A7A6A" {OL}/><path d="M24 30 L36 40 L28 54 M60 26 L66 44 L80 40 M46 64 L56 74" fill="none" stroke="#5D4E4E" stroke-width="3"/>'
        '<circle cx="62" cy="58" r="4" fill="#FFD25A" {OL}/><circle cx="34" cy="70" r="3" fill="#E8574A"/>'),
 # ---------- maps ----------
 "political_map": dict(words=["الخرائط السياسية", "الخريطة السياسية", "الوحدات السياسية", "الحدود السياسية"], anim="bob", face=(50, 50, .4), only=E,
   body='<path d="M6 16 L34 8 L66 16 L94 8 L94 84 L66 92 L34 84 L6 92Z" fill="#fff" {OL}/><path d="M8 18 L32 12 L40 40 L12 50Z" fill="#F6B73C"/><path d="M32 12 L64 18 L60 44 L40 40Z" fill="#6CC27A"/>'
        '<path d="M12 50 L40 40 L46 72 L10 86Z" fill="#F59BB8"/><path d="M40 40 L60 44 L92 36 L92 80 L66 88 L46 72Z" fill="#6CB8FF"/><path d="M40 40 L46 72 M40 40 L60 44" stroke="#3b2a1a" stroke-width="2" stroke-dasharray="3 2"/><path d="M6 16 L34 8 L66 16 L94 8 L94 84 L66 92 L34 84 L6 92Z" fill="none" {OL}/>'),
 "natural_map": dict(words=["الخرائط الطبيعية", "الخريطة الطبيعية", "الخرائط التفصيلية"], anim="bob", face=(30, 30, .36), only=E,
   body='<path d="M6 16 L34 8 L66 16 L94 8 L94 84 L66 92 L34 84 L6 92Z" fill="#9CD86C" {OL}/><path d="M48 60 L60 36 L72 60Z M62 64 L72 46 L82 64Z" fill="#B48B65" {OL}/>'
        '<path d="M10 70 C24 62 34 78 48 72" fill="none" stroke="#6CB8FF" stroke-width="4"/><path d="M70 74 C80 70 88 80 94 76 L94 84 L66 92 Z" fill="#6CB8FF"/>'),
 "climate_map": dict(words=["الخرائط المناخية", "الخريطة المناخية", "خرائط الطقس"], anim="sun", face=(70, 70, .32), only=E,
   body='<path d="M6 16 L34 8 L66 16 L94 8 L94 84 L66 92 L34 84 L6 92Z" fill="#fff" {OL}/><circle cx="28" cy="34" r="10" fill="#FFD25A" {OL}/>'
        '<path d="M56 30 C52 22 64 18 68 26 C76 24 80 34 74 36 L58 36 C50 36 50 30 56 30Z" fill="#AEB8C4" {OL}/><path d="M60 42 L58 48 M66 42 L64 48 M72 42 L70 48" stroke="#6CB8FF" stroke-width="2.6"/>'),
 "contour": dict(words=["خطوط الكنتور", "الخرائط الطبوغرافية", "الارتفاع عن سطح البحر", "الانحدار", "خطوط التساوي", "الخريطة الكنتورية"], anim="sun", face=(50, 50, .3), only=E,
   body='<path d="M6 16 L34 8 L66 16 L94 8 L94 84 L66 92 L34 84 L6 92Z" fill="#F7E9C8" {OL}/><ellipse cx="50" cy="50" rx="40" ry="32" fill="none" stroke="#B48B65" stroke-width="2.6"/>'
        '<ellipse cx="52" cy="48" rx="28" ry="22" fill="none" stroke="#B48B65" stroke-width="2.6"/><ellipse cx="54" cy="46" rx="16" ry="12" fill="none" stroke="#B48B65" stroke-width="2.6"/><circle cx="56" cy="44" r="4" fill="#8B5E3C"/>'),
 "north": dict(words=["اتجاه الشمال", "سهم الشمال", "الشمال الجغرافي"], anim="sun", face=(50, 70, .34), only=E,
   body='<circle cx="50" cy="56" r="38" fill="#fff" {OL}/><path d="M50 8 L64 56 L50 48 L36 56Z" fill="#E8574A" {OL}/><path d="M50 48 L64 56 L50 96 L36 56Z" fill="#AEB8C4" {OL}/>'
        '<text direction="ltr" x="50" y="6" text-anchor="middle" font-size="10" font-weight="800" fill="#3b2a1a" font-family="sans-serif">N</text>'),
 "coordinates": dict(words=["الإحداثيات", "الإحداثيات الجغرافية", "نظام الإحداثيات الجغرافي", "تحديد الموقع"], anim="bounce", face=(66, 30, .3), only=E,
   body='<rect x="6" y="6" width="88" height="88" rx="4" fill="#fff" {OL}/><path d="M28 6 L28 94 M50 6 L50 94 M72 6 L72 94 M6 28 L94 28 M6 50 L94 50 M6 72 L94 72" stroke="#AEB8C4" stroke-width="2"/>'
        '<path d="M66 44 C66 44 56 32 56 26 C56 20 60 16 66 16 C72 16 76 20 76 26 C76 32 66 44 66 44Z" fill="#E8574A" {OL}/><path d="M66 50 L66 94 M6 50 L66 50" stroke="#E8574A" stroke-width="2" stroke-dasharray="3 3"/>'),
 "navigation": dict(words=["الملاحة", "الملاحة البحرية", "الملاحة الجوية", "عجلة القيادة"], anim="sun", face=(50, 50, .34), only=E,
   body='<circle cx="50" cy="50" r="32" fill="none" stroke="#8B5E3C" stroke-width="8"/><circle cx="50" cy="50" r="12" fill="#C98A55" {OL}/>'
        '<path d="M50 4 L50 38 M50 62 L50 96 M4 50 L38 50 M62 50 L96 50 M18 18 L41 41 M59 59 L82 82 M18 82 L41 59 M59 41 L82 18" stroke="#8B5E3C" stroke-width="5" stroke-linecap="round"/>'),
 "surveying": dict(words=["علم المساحة", "المساحة الأرضية", "أجهزة المساحة", "المسح الأرضي", "مسح الأراضي"], anim="bob", face=(50, 20, .3), only=E,
   body='<rect x="36" y="10" width="28" height="22" rx="4" fill="#FFD25A" {OL}/><circle cx="64" cy="21" r="6" fill="#3b3b5c" {OL}/><path d="M50 32 L50 40" stroke="#3b2a1a" stroke-width="4"/>'
        '<path d="M50 40 L22 94 M50 40 L78 94 M50 40 L50 94" stroke="#C98A55" stroke-width="5" stroke-linecap="round"/>'),
 "scale_bar": dict(words=["المقياس الخطي", "المقياس الكسري (النسبي)", "المقياس الكسري", "المقياس النسبي", "علم الخرائط"], anim="bob", face=(50, 30, .32), only=E,
   body='<rect x="6" y="54" width="22" height="12" fill="#3b2a1a"/><rect x="28" y="54" width="22" height="12" fill="#fff" {OL}/><rect x="50" y="54" width="22" height="12" fill="#3b2a1a"/><rect x="72" y="54" width="22" height="12" fill="#fff" {OL}/>'
        '<text direction="ltr" x="50" y="40" text-anchor="middle" font-size="16" font-weight="800" fill="#3b2a1a" font-family="sans-serif">1:1000</text><text direction="ltr" x="6" y="84" font-size="10" font-weight="700" fill="#3b2a1a" font-family="sans-serif">0</text>'),
 "satellite_img": dict(words=["المرئيات الفضائية", "التقنيات الحديثة", "الأقمار الصناعية", "صور الأقمار الصناعية"], anim="bob", face=(50, 40, .3), only=E,
   body='<rect x="38" y="30" width="24" height="20" rx="3" fill="#AEB8C4" {OL}/><rect x="6" y="32" width="28" height="16" fill="#3b5d9c" {OL}/><rect x="66" y="32" width="28" height="16" fill="#3b5d9c" {OL}/>'
        '<path d="M50 50 L30 90 M50 50 L70 90" stroke="#FFD25A" stroke-width="2" stroke-dasharray="4 3"/><path d="M14 92 C30 84 70 84 86 92" fill="none" stroke="#6CC27A" stroke-width="6" stroke-linecap="round"/>'),
 "shading": dict(words=["التظليل", "الحدود والتظليل", "الألوان في الخرائط", "مفتاح الألوان"], anim="bob", face=(70, 70, .3),
   body='<rect x="6" y="10" width="88" height="80" rx="4" fill="#fff" {OL}/><rect x="14" y="20" width="22" height="16" fill="#E6F4D8"/><rect x="14" y="40" width="22" height="16" fill="#9CD86C"/><rect x="14" y="60" width="22" height="16" fill="#3E8E4C"/>'
        '<path d="M44 28 L84 28 M44 48 L80 48 M44 68 L76 68" stroke="#AEB8C4" stroke-width="3" stroke-linecap="round"/>'),
 "map_layers": dict(words=["طبقات الخريطة", "نظم المعلومات الجغرافية بالطبقات"], anim="bob", face=(50, 30, .3), only=["social", "digital"],
   body='<path d="M50 10 L94 30 L50 50 L6 30Z" fill="#6CB8FF" {OL}/><path d="M6 46 L50 66 L94 46" fill="none" stroke="#3b2a1a" stroke-width="3"/><path d="M6 46 L50 66 L94 46 L94 50 L50 70 L6 50Z" fill="#6CC27A" {OL}/>'
        '<path d="M6 66 L50 86 L94 66 L94 70 L50 90 L6 70Z" fill="#F6B73C" {OL}/>'),
 # ---------- the air and the weather ----------
 "troposphere": dict(words=["التروبوسفير", "طبقات الغلاف الجوي", "الستراتوسفير", "طبقة التروبوسفير"], anim="wind", face=(50, 80, .3), only=E,
   body='<rect x="2" y="2" width="96" height="96" rx="8" fill="#1F2A44" {OL}/><rect x="2" y="36" width="96" height="62" fill="#3B6FD9"/><rect x="2" y="62" width="96" height="36" fill="#BFE3F2"/>'
        '<path d="M2 92 C30 84 70 84 98 92 L98 98 L2 98Z" fill="#9CD86C"/><path d="M20 72 C18 66 26 64 28 68 C32 64 38 68 36 72Z" fill="#fff"/><path d="M60 52 L76 44" stroke="#fff" stroke-width="3"/><rect x="2" y="2" width="96" height="96" rx="8" fill="none" {OL}/>'),
 "weather_report": dict(words=["الأرصاد الجوية", "النشرة الجوية", "التنبؤ بالطقس", "محطة الأرصاد"], anim="bob", face=(50, 76, .3), only=E,
   body='<rect x="6" y="10" width="88" height="62" rx="6" fill="#3b3b5c" {OL}/><rect x="12" y="16" width="76" height="50" rx="3" fill="#BFE3F2"/><circle cx="34" cy="34" r="10" fill="#FFD25A" {OL}/>'
        '<path d="M52 44 C48 36 60 32 64 40 C72 38 76 48 70 50 L54 50 C46 50 46 44 52 44Z" fill="#fff" {OL}/><path d="M30 72 L24 88 M70 72 L76 88 M18 88 L82 88" stroke="#3b2a1a" stroke-width="4" stroke-linecap="round"/>'),
 "high_pressure": dict(words=["المرتفع الجوي", "الضغط المرتفع"], anim="sun", face=(50, 76, .3), only=E,
   body='<circle cx="50" cy="44" r="38" fill="#E8F6FF" {OL}/><circle cx="50" cy="44" r="26" fill="none" stroke="#6CB8FF" stroke-width="2.6"/><text direction="ltr" x="50" y="56" text-anchor="middle" font-size="32" font-weight="800" fill="#2F6DB5" font-family="sans-serif">H</text>'),
 "low_pressure": dict(words=["المنخفض الجوي", "الضغط المنخفض"], anim="sun", face=(50, 76, .3), only=E,
   body='<circle cx="50" cy="44" r="38" fill="#FBE9E7" {OL}/><circle cx="50" cy="44" r="26" fill="none" stroke="#E8574A" stroke-width="2.6"/><text direction="ltr" x="50" y="56" text-anchor="middle" font-size="32" font-weight="800" fill="#B8322A" font-family="sans-serif">L</text>'),
 "sea_breeze": dict(words=["نسيم البر والبحر", "نسيم البحر", "نسيم البر"], anim="wind", face=(26, 76, .3), only=E,
   body='<rect x="2" y="70" width="48" height="26" fill="#F2D07A" {OL}/><rect x="50" y="70" width="48" height="26" fill="#7CC6F2" {OL}/><circle cx="20" cy="18" r="10" fill="#FFD25A" {OL}/>'
        '<path d="M80 60 L24 60 M32 54 L24 60 L32 66 M24 34 C40 28 64 28 80 34" fill="none" stroke="#3b2a1a" stroke-width="3" stroke-linecap="round"/><path d="M74 28 L80 34 L72 38" fill="none" stroke="#3b2a1a" stroke-width="3"/>'),
 "oceans": dict(words=["المحيط الهادي", "المحيط الأطلسي", "المحيط الهندي", "المحيطات", "المحيط المتجمد الشمالي", "الغلاف المائي"], anim="sway", face=(50, 50, .38), only=E,
   body='<circle cx="50" cy="50" r="46" fill="#4A90D9" {OL}/><path d="M18 26 C28 18 40 24 36 36 C34 46 22 44 18 36Z M60 18 C72 14 84 24 78 34 C74 40 62 38 60 30Z M58 60 C70 54 82 64 76 76 C70 84 56 80 58 70Z" fill="#9CD86C" {OL}/>'
        '<path d="M14 64 C22 60 30 68 38 64 M22 78 C30 74 38 82 46 78" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>'),
 "waves_sea": dict(words=["الأمواج", "أمواج البحر", "المد والجزر"], anim="sway", face=(50, 80, .32), only=E,
   body='<path d="M2 50 C14 30 26 30 34 44 C40 54 52 54 58 40 C64 26 78 26 86 40 C90 46 94 48 98 46 L98 98 L2 98Z" fill="#4A90D9" {OL}/>'
        '<path d="M2 70 C14 60 26 62 36 70 C46 78 58 78 68 70 C78 62 90 62 98 70" fill="none" stroke="#BFE3F2" stroke-width="3"/><path d="M58 40 C62 34 70 32 76 36" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round"/>'),
 "currents": dict(words=["التيارات البحرية", "التيارات المحيطية", "التيار الدافئ", "التيار البارد"], anim="sway", face=(50, 50, .34), only=E,
   body='<rect x="2" y="2" width="96" height="96" rx="10" fill="#7CC6F2" {OL}/><path d="M14 40 C30 14 70 14 86 40 M86 60 C70 86 30 86 14 60" fill="none" stroke="#E8574A" stroke-width="5" stroke-linecap="round"/>'
        '<path d="M78 30 L86 40 L74 42 M22 70 L14 60 L26 58" fill="none" stroke="#E8574A" stroke-width="4"/><path d="M30 50 L70 50" stroke="#6CB8FF" stroke-width="4" stroke-dasharray="6 4"/>'),
 # ---------- the world's regions ----------
 "regions_geo": dict(words=["الإقليم الجغرافي", "الأقاليم الطبيعية", "الأقاليم المناخية", "الأقاليم البشرية", "الأقاليم الحيوية", "الأقاليم", "المنطقة الحيوية", "المناطق الحيوية"], anim="bob", face=(50, 50, .36), only=E,
   body='<circle cx="50" cy="50" r="46" fill="#fff" {OL}/><path d="M6 36 L94 36 A46 46 0 0 0 6 36Z" fill="#E8F2F8"/><path d="M5 40 L95 40 L96 60 L4 60Z" fill="#9CD86C"/><path d="M4 62 L96 62 L95 70 L5 70Z" fill="#F2C46D"/><path d="M6 72 L94 72 A46 46 0 0 1 6 72Z" fill="#3E8E4C"/>'
        '<circle cx="50" cy="50" r="46" fill="none" {OL}/>'),
 "savanna": dict(words=["السافانا", "حشائش السافانا", "الأراضي العشبية", "المراعي الطبيعية"], anim="sway", face=(30, 80, .3), only=E,
   body='<rect x="2" y="2" width="96" height="60" fill="#FFE7A8"/><circle cx="20" cy="20" r="10" fill="#FFD25A" {OL}/><rect x="2" y="62" width="96" height="36" fill="#E8C35A" {OL}/>'
        '<path d="M66 62 L66 38" stroke="#8B5E3C" stroke-width="5"/><path d="M44 36 C50 22 86 22 92 36Z" fill="#6CC27A" {OL}/><path d="M10 62 L14 52 L18 62 M28 62 L32 50 L36 62 M80 62 L84 52 L88 62" fill="none" stroke="#B5951D" stroke-width="2"/>'),
 "desert_region": dict(words=["الإقليم الصحراوي", "الأقاليم الصحراوية", "المناطق الصحراوية", "المناخ الصحراوي"], anim="sun", face=(30, 80, .3), only=E,
   body='<rect x="2" y="2" width="96" height="56" fill="#FFE7A8"/><circle cx="78" cy="20" r="12" fill="#F6B73C" {OL}/><path d="M2 70 C22 52 42 52 56 66 C68 54 86 54 98 64 L98 98 L2 98Z" fill="#F2C46D" {OL}/>'
        '<path d="M30 66 L30 40 M30 50 L22 50 L22 42 M30 56 L38 56 L38 46" fill="none" stroke="#3E8E4C" stroke-width="6" stroke-linecap="round"/>'),
 "mediterranean": dict(words=["إقليم البحر المتوسط", "مناخ البحر المتوسط", "البحر المتوسط"], anim="sway", face=(30, 50, .32), only=E,
   body='<rect x="2" y="2" width="96" height="50" fill="#BFE3F2"/><rect x="2" y="62" width="96" height="36" fill="#4A90D9" {OL}/><path d="M2 52 L60 52 L66 62 L2 62Z" fill="#F2D07A" {OL}/>'
        '<path d="M30 52 L30 28" stroke="#8B5E3C" stroke-width="5"/><ellipse cx="30" cy="22" rx="18" ry="12" fill="#8BA65A" {OL}/><circle cx="24" cy="22" r="2.4" fill="#3b3b5c"/><circle cx="36" cy="18" r="2.4" fill="#3b3b5c"/>'),
 "equatorial": dict(words=["الإقليم الاستوائي", "الغابات الاستوائية المطيرة", "المناخ الاستوائي"], anim="sway", face=(50, 84, .3), only=E,
   body='<rect x="2" y="2" width="96" height="96" rx="8" fill="#BFE3F2" {OL}/><path d="M20 98 L20 50 M50 98 L50 40 M80 98 L80 50" stroke="#8B5E3C" stroke-width="6"/>'
        '<circle cx="20" cy="42" r="18" fill="#3E8E4C" {OL}/><circle cx="50" cy="32" r="22" fill="#5AAE5A" {OL}/><circle cx="80" cy="42" r="18" fill="#3E8E4C" {OL}/><path d="M30 10 L28 18 M42 8 L40 16 M66 10 L64 18" stroke="#6CB8FF" stroke-width="2.4"/>'),
 "tundra": dict(words=["التندرا", "الأقاليم القطبية", "المناخ القطبي"], anim="wind", face=(70, 80, .3), only=E,
   body='<rect x="2" y="2" width="96" height="60" fill="#E8F2F8"/><rect x="2" y="62" width="96" height="36" fill="#A9B88A" {OL}/>'
        '<path d="M2 62 L20 50 L36 62 L56 46 L78 62 L98 52 L98 62Z" fill="#fff" {OL}/><circle cx="20" cy="80" r="5" fill="#E8574A"/><circle cx="46" cy="84" r="5" fill="#B0A8C9"/><path d="M14 20 L16 24 M40 14 L42 18 M70 24 L72 28" stroke="#AEB8C4" stroke-width="2.4"/>'),
 "temperate": dict(words=["المناطق المعتدلة", "المناخ المعتدل", "الإقليم المعتدل"], anim="sway", face=(50, 80, .3), only=E,
   body='<rect x="2" y="2" width="96" height="96" rx="8" fill="#E8F6FF" {OL}/><path d="M2 76 L98 76 L98 98 L2 98Z" fill="#9CD86C"/><path d="M30 76 L30 50 M70 76 L70 50" stroke="#8B5E3C" stroke-width="5"/>'
        '<circle cx="30" cy="40" r="16" fill="#6CC27A" {OL}/><circle cx="70" cy="40" r="16" fill="#F6A23C" {OL}/><circle cx="50" cy="16" r="8" fill="#FFD25A" {OL}/>'),
 "lithosphere": dict(words=["الغلاف الصخري", "الأغلفة الأرضية", "أغلفة الأرض"], anim="bob", face=(50, 30, .34), only=E,
   body='<circle cx="50" cy="50" r="44" fill="#6CB8FF" {OL}/><path d="M6 50 A44 44 0 0 0 94 50 L80 50 A30 30 0 0 1 20 50Z" fill="#8A7A6A" {OL}/>'
        '<path d="M20 50 A30 30 0 0 0 80 50Z" fill="#F6A23C"/><path d="M20 30 C30 22 44 30 40 40 C34 46 22 40 20 30Z" fill="#9CD86C" {OL}/>'),
 "folding": dict(words=["الالتواءات", "العمليات الباطنية", "العوامل الداخلية", "الطيات", "الحركات الباطنية"], anim="wobble", face=(50, 30, .3), only=E,
   body='<path d="M2 50 C18 24 34 24 50 50 C66 76 82 76 98 50 L98 66 C82 92 66 92 50 66 C34 40 18 40 2 66Z" fill="#E6C08A" {OL}/>'
        '<path d="M2 34 C18 8 34 8 50 34 C66 60 82 60 98 34 L98 50 C82 76 66 76 50 50 C34 24 18 24 2 50Z" fill="#B48B65" {OL}/>'
        '<path d="M2 80 L14 80 M86 80 L98 80 M8 74 L14 80 L8 86 M92 74 L86 80 L92 86" fill="none" stroke="#E8574A" stroke-width="3" stroke-linecap="round"/>'),
 "external_proc": dict(words=["العمليات الخارجية", "العوامل الخارجية", "الإرساب", "التعرية والإرساب", "النحت والإرساب"], anim="wind", face=(26, 76, .3), only=E,
   body='<path d="M2 50 L30 24 L54 46 L54 98 L2 98Z" fill="#9C8C7A" {OL}/><path d="M54 76 C70 70 84 80 98 74 L98 98 L54 98Z" fill="#F2D07A" {OL}/>'
        '<path d="M58 30 C68 26 76 34 86 30 M60 42 C70 38 78 46 88 42" fill="none" stroke="#6CB8FF" stroke-width="3" stroke-linecap="round"/><circle cx="64" cy="66" r="3" fill="#9C8C7A"/><circle cx="74" cy="70" r="2.4" fill="#9C8C7A"/>'),
 "crowded": dict(words=["المناطق المكتظة", "الكثافة السكانية", "الزيادة الطبيعية"], anim="bob", face=(50, 60, .32), only=["social"],
   body='<rect x="4" y="34" width="22" height="62" fill="#AEB8C4" {OL}/><rect x="26" y="20" width="24" height="76" fill="#C9D2DC" {OL}/><rect x="50" y="40" width="20" height="56" fill="#AEB8C4" {OL}/><rect x="70" y="26" width="26" height="70" fill="#C9D2DC" {OL}/>'
        '<path d="M10 44 L20 44 M10 56 L20 56 M32 30 L44 30 M32 44 L44 44 M56 50 L64 50 M76 36 L90 36 M76 50 L90 50" stroke="#FFF3C4" stroke-width="5"/>'),
}
ALIAS_ONLY = None
ALIASES = {"قارة آسيا": ("geo:continents", ("social",))}
