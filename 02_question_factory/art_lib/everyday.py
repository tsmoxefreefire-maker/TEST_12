"""🆕 batch 43 (Hareth: «زيد لنا رسمات بحيث إنها تغطي مفاهيم كثيرة… مواد كثيرة») · everyday life: food and the kitchen, the body's
care, first aid and safety, the home and its things, manners and how we treat each other, the school day, and the warnings
(smoking, drugs, a screen that takes too much). Same style as every drawing: our outline, flat colours, a place for the face.
No people of history, nothing religious (art_library.NEVER_DRAW)."""
F = "day"
D = {
 # ---------- food ----------
 "breakfast": dict(words=["وجبة الإفطار", "الإفطار الصحي", "يتناول الفطور", "الفطور"], anim="bob", face=(50, 58, .45),
   body='<ellipse cx="50" cy="62" rx="44" ry="28" fill="#fff" {OL}/><ellipse cx="40" cy="58" rx="20" ry="16" fill="#fff" {OL}/><circle cx="40" cy="58" r="8" fill="#FFC23D" {OL}/>'
        '<path d="M64 44 C60 36 80 34 82 42 L84 70 L66 72Z" fill="#E8B26A" {OL}/>'),
 "balanced_meal": dict(words=["الوجبة الصحية", "الوجبات المتوازنة", "العادات الغذائية", "الوجبات المنتظمة", "الحمية الغذائية", "الطبق الصحي"], anim="bob", face=(50, 50, .45),
   body='<circle cx="50" cy="50" r="44" fill="#fff" {OL}/><path d="M50 50 L50 6 A44 44 0 0 1 94 50Z" fill="#6CC27A" {OL}/><path d="M50 50 L94 50 A44 44 0 0 1 50 94Z" fill="#F6B73C" {OL}/>'
        '<path d="M50 50 L50 94 A44 44 0 0 1 6 50Z" fill="#E8574A" {OL}/><path d="M50 50 L6 50 A44 44 0 0 1 50 6Z" fill="#F2D07A" {OL}/><circle cx="50" cy="50" r="13" fill="#fff" {OL}/>'),
 "salad": dict(words=["السلطة", "الخس", "الخضروات الورقية", "سلطة الخضار"], anim="sway", face=(50, 70, .45),
   body='<path d="M8 54 L92 54 C90 80 72 94 50 94 C28 94 10 80 8 54Z" fill="#fff" {OL}/><path d="M16 54 C14 36 30 30 36 42 C38 26 58 24 60 40 C66 28 86 32 84 54Z" fill="#8BD06A" {OL}/>'
        '<circle cx="32" cy="50" r="6" fill="#E8574A" {OL}/><circle cx="66" cy="48" r="5" fill="#E8574A" {OL}/><path d="M46 36 L50 52 M62 40 L58 52" stroke="#5A9A3A" stroke-width="2.4"/>'),
 "apple2": dict(words=["التفاح", "تفاح"], anim="bob", face=(50, 60, .55),
   body='<path d="M50 28 C30 14 6 26 10 54 C14 82 34 94 50 86 C66 94 86 82 90 54 C94 26 70 14 50 28Z" fill="#E8574A" {OL}/><path d="M50 28 C50 18 54 10 60 6" fill="none" stroke="#8B5E3C" stroke-width="4" stroke-linecap="round"/>'
        '<path d="M56 16 C66 6 80 10 80 16 C72 22 62 22 56 16Z" fill="#6CC27A" {OL}/>'),
 "orange": dict(words=["البرتقال", "برتقال", "البرتقالة", "الحمضيات"], anim="bob", face=(50, 56, .55),
   body='<circle cx="50" cy="56" r="38" fill="#F6A23C" {OL}/><circle cx="36" cy="44" r="2" fill="#D9822B"/><circle cx="62" cy="40" r="2" fill="#D9822B"/><circle cx="66" cy="70" r="2" fill="#D9822B"/>'
        '<path d="M50 18 C46 10 52 6 56 8" fill="none" stroke="#8B5E3C" stroke-width="3"/><path d="M54 16 C62 6 76 10 74 18 C66 22 58 22 54 16Z" fill="#6CC27A" {OL}/>'),
 "grapes": dict(words=["العنب", "عنب", "عنقود العنب"], anim="sway", face=(50, 52, .45),
   body='<circle cx="34" cy="34" r="12" fill="#8E5BB5" {OL}/><circle cx="58" cy="34" r="12" fill="#8E5BB5" {OL}/><circle cx="46" cy="52" r="12" fill="#8E5BB5" {OL}/><circle cx="70" cy="52" r="11" fill="#8E5BB5" {OL}/>'
        '<circle cx="34" cy="56" r="11" fill="#8E5BB5" {OL}/><circle cx="58" cy="70" r="11" fill="#8E5BB5" {OL}/><circle cx="44" cy="78" r="10" fill="#8E5BB5" {OL}/><path d="M46 22 L50 8 M50 12 C58 4 70 8 70 14" fill="none" stroke="#5A9A3A" stroke-width="3"/>'),
 "sandwich": dict(words=["الشطيرة", "الساندويتش", "شطيرة"], anim="bob", face=(50, 54, .45),
   body='<path d="M8 56 L50 20 L92 56Z" fill="#F2C46D" {OL}/><path d="M10 60 C30 66 70 66 90 60 L90 66 C70 72 30 72 10 66Z" fill="#8BD06A" {OL}/><path d="M10 66 L90 66 L90 72 L10 72Z" fill="#E8574A" {OL}/>'
        '<path d="M8 72 L92 72 L92 84 C70 90 30 90 8 84Z" fill="#F2C46D" {OL}/>'),
 "popcorn": dict(words=["الفشار", "فشار"], anim="bounce", face=(50, 74, .42),
   body='<path d="M20 44 L80 44 L72 96 L28 96Z" fill="#fff" {OL}/><path d="M30 44 L34 96 M50 44 L50 96 M70 44 L66 96" stroke="#E8574A" stroke-width="6"/>'
        '<circle cx="28" cy="36" r="10" fill="#FFF3C4" {OL}/><circle cx="46" cy="28" r="11" fill="#FFF3C4" {OL}/><circle cx="64" cy="32" r="10" fill="#FFF3C4" {OL}/><circle cx="76" cy="40" r="8" fill="#FFF3C4" {OL}/>'),
 "teapot": dict(words=["الشاي", "إبريق الشاي", "تحضير الشاي", "كوب الشاي"], anim="wobble", face=(46, 62, .5),
   body='<path d="M18 46 C18 30 74 30 74 46 L72 80 C70 90 22 90 20 80Z" fill="#E8574A" {OL}/><path d="M74 54 L92 40 L90 48 L74 66" fill="#E8574A" {OL}/><path d="M18 52 C4 52 4 74 20 72" fill="none" stroke="#3b2a1a" stroke-width="3"/>'
        '<rect x="38" y="24" width="16" height="10" rx="4" fill="#E8574A" {OL}/><path d="M94 32 C96 26 92 22 94 16" fill="none" stroke="#AEB8C4" stroke-width="2.6" stroke-linecap="round"/>'),
 "coffee_pot": dict(words=["الفنجان", "آداب تقديم القهوة", "تقديم القهوة"], anim="wobble", face=(40, 66, .45),
   body='<path d="M28 30 L52 30 L58 50 C66 60 66 82 58 92 L22 92 C14 82 14 60 22 50Z" fill="#E8C35A" {OL}/><path d="M28 30 C30 18 50 18 52 30" fill="#E8C35A" {OL}/>'
        '<path d="M58 54 C74 48 82 40 90 32" fill="none" stroke="#3b2a1a" stroke-width="5" stroke-linecap="round"/><path d="M68 78 L94 78 L90 94 L72 94Z" fill="#fff" {OL}/>'),
 "soup": dict(words=["الحساء (الشوربة)", "الحساء", "الشوربة", "القدر", "طنجرة"], anim="wobble", face=(50, 70, .5),
   body='<path d="M12 46 L88 46 L84 84 C80 94 20 94 16 84Z" fill="#AEB8C4" {OL}/><rect x="8" y="40" width="84" height="10" rx="5" fill="#C9D2DC" {OL}/><path d="M8 56 L2 56 M92 56 L98 56" stroke="#3b2a1a" stroke-width="5" stroke-linecap="round"/>'
        '<path d="M36 34 C32 26 40 22 36 12 M52 32 C48 24 56 20 52 10 M68 34 C64 26 72 22 68 12" fill="none" stroke="#AEB8C4" stroke-width="3" stroke-linecap="round"/>'),
 "sauce": dict(words=["التتبيلة", "الصلصة", "البهارات", "التوابل"], anim="wobble", face=(50, 70, .45),
   body='<path d="M14 50 L86 50 C84 80 68 94 50 94 C32 94 16 80 14 50Z" fill="#fff" {OL}/><path d="M18 56 L82 56 C80 76 66 88 50 88 C34 88 20 76 18 56Z" fill="#D9582E"/>'
        '<path d="M60 52 L84 10" stroke="#C98A55" stroke-width="7" stroke-linecap="round"/><circle cx="34" cy="66" r="2.6" fill="#7A2A12"/><circle cx="48" cy="74" r="2.6" fill="#7A2A12"/><circle cx="62" cy="66" r="2.6" fill="#7A2A12"/>'),
 "rice_platter": dict(words=["الكبسة", "الأكلات الشعبية", "الأكلات الشعبية السعودية", "المندي"], anim="bob", face=(50, 52, .45),
   body='<ellipse cx="50" cy="72" rx="46" ry="18" fill="#C9D2DC" {OL}/><path d="M12 70 C14 34 86 34 88 70Z" fill="#F6C76A" {OL}/>'
        '<path d="M36 44 C30 34 44 26 50 36 C56 26 70 34 64 44 C60 52 40 52 36 44Z" fill="#C98A55" {OL}/><circle cx="24" cy="62" r="2.4" fill="#6CC27A"/><circle cx="74" cy="58" r="2.4" fill="#E8574A"/><circle cx="64" cy="66" r="2.4" fill="#6CC27A"/>'),
 "fries": dict(words=["البطاطس المقلية", "البطاطا المقلية"], anim="bounce", face=(50, 76, .42),
   body='<path d="M30 30 L34 70 M40 22 L42 70 M50 26 L50 70 M60 20 L58 70 M70 28 L66 70" stroke="#FFD25A" stroke-width="8" stroke-linecap="round"/>'
        '<path d="M22 50 L78 50 L70 96 L30 96Z" fill="#E8574A" {OL}/>'),
 "canned": dict(words=["المضافات الغذائية", "المواد الحافظة", "التعليب", "الأطعمة المعلبة", "المعلبات", "حفظ الأغذية", "حفظ الطعام"], anim="wobble", face=(50, 62, .5),
   body='<rect x="22" y="22" width="56" height="70" rx="6" fill="#AEB8C4" {OL}/><ellipse cx="50" cy="22" rx="28" ry="7" fill="#C9D2DC" {OL}/><rect x="22" y="40" width="56" height="34" fill="#F6B73C" {OL}/>'
        '<path d="M34 52 L42 60 L60 48" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round"/>'),
 "drying": dict(words=["التجفيف", "تجفيف الطعام", "الفواكه المجففة"], anim="sun", face=(50, 70, .45),
   body='<circle cx="78" cy="22" r="12" fill="#FFD25A" {OL}/><path d="M78 4 L78 0 M96 22 L100 22 M90 10 L93 7" stroke="#F6B73C" stroke-width="3"/>'
        '<rect x="8" y="56" width="84" height="10" rx="3" fill="#C98A55" {OL}/><circle cx="24" cy="50" r="7" fill="#B05A3A" {OL}/><circle cx="44" cy="50" r="7" fill="#B05A3A" {OL}/><circle cx="64" cy="50" r="7" fill="#B05A3A" {OL}/>'
        '<path d="M16 66 L12 94 M84 66 L88 94" stroke="#8B5E3C" stroke-width="4"/>'),
 "legumes": dict(words=["البقول", "العدس", "الفول", "البقوليات", "الحمص"], anim="bob", face=(50, 70, .45),
   body='<path d="M10 50 L90 50 C88 80 70 94 50 94 C30 94 12 80 10 50Z" fill="#C98A55" {OL}/><ellipse cx="50" cy="50" rx="40" ry="8" fill="#E8C35A" {OL}/>'
        '<ellipse cx="34" cy="46" rx="5" ry="3.4" fill="#B5651D"/><ellipse cx="50" cy="44" rx="5" ry="3.4" fill="#B5651D"/><ellipse cx="64" cy="47" rx="5" ry="3.4" fill="#B5651D"/><ellipse cx="44" cy="52" rx="5" ry="3.4" fill="#B5651D"/>'),
 "falafel": dict(words=["الفلافل", "فلافل"], anim="bounce", face=(50, 50, .45),
   body='<ellipse cx="50" cy="78" rx="44" ry="12" fill="#fff" {OL}/><circle cx="30" cy="62" r="16" fill="#9B6A2B" {OL}/><circle cx="64" cy="62" r="16" fill="#9B6A2B" {OL}/><circle cx="47" cy="40" r="16" fill="#A8772F" {OL}/>'
        '<circle cx="42" cy="36" r="1.6" fill="#6CC27A"/><circle cx="26" cy="58" r="1.6" fill="#6CC27A"/><circle cx="68" cy="58" r="1.6" fill="#6CC27A"/>'),
 "tuna": dict(words=["التونة", "تونة", "السمك المعلب"], anim="wobble", face=(56, 44, .4),
   body='<ellipse cx="50" cy="70" rx="40" ry="16" fill="#AEB8C4" {OL}/><path d="M10 62 L10 70 M90 62 L90 70" stroke="#3b2a1a" stroke-width="2.6"/><ellipse cx="50" cy="62" rx="40" ry="14" fill="#C9D2DC" {OL}/>'
        '<path d="M22 40 C36 22 66 22 80 40 C66 56 36 56 22 40Z" fill="#6CB8FF" {OL}/><path d="M22 40 L8 30 L10 50Z" fill="#6CB8FF" {OL}/>'),
 "honey": dict(words=["العسل", "عسل", "عسل النحل"], anim="drip", face=(50, 66, .45),
   body='<rect x="22" y="34" width="56" height="60" rx="12" fill="#F6B73C" {OL}/><rect x="26" y="20" width="48" height="14" rx="4" fill="#C98A55" {OL}/><path d="M22 48 C32 56 40 44 50 52 C60 60 68 46 78 52" fill="none" stroke="#fff" stroke-width="3"/>'
        '<path d="M70 20 L86 4" stroke="#8B5E3C" stroke-width="4"/><ellipse cx="88" cy="4" rx="5" ry="3" fill="#8B5E3C"/>'),
 "herbs": dict(words=["الأعشاب الطبية", "الحبة السوداء", "الأعشاب", "النباتات الطبية", "الطب الشعبي"], anim="sway", face=(50, 76, .4),
   body='<path d="M14 62 L86 62 C84 84 70 94 50 94 C30 94 16 84 14 62Z" fill="#C98A55" {OL}/><path d="M64 64 L86 36" stroke="#8B5E3C" stroke-width="7" stroke-linecap="round"/>'
        '<path d="M30 60 C24 40 30 26 38 22 C40 36 36 48 30 60Z M44 60 C44 42 52 30 60 28 C58 42 52 52 44 60Z" fill="#6CC27A" {OL}/><circle cx="56" cy="56" r="2.4" fill="#3b2a1a"/><circle cx="62" cy="58" r="2.4" fill="#3b2a1a"/>'),
 "milk_calcium": dict(words=["الكالسيوم", "منتجات الألبان", "الحليب ومشتقاته"], anim="bob", face=(50, 64, .45),
   body='<path d="M28 30 L72 30 L72 94 L28 94Z" fill="#fff" {OL}/><path d="M28 30 L36 14 L64 14 L72 30" fill="#6CB8FF" {OL}/><rect x="28" y="48" width="44" height="22" fill="#6CB8FF"/>'
        '<path d="M50 52 C56 52 60 58 56 62 C60 66 56 72 50 70 C44 72 40 66 44 62 C40 58 44 52 50 52Z" fill="#fff"/>'),
 "waste_food": dict(words=["الإسراف", "الإسراف في الطعام", "هدر الطعام", "التبذير"], anim="wobble", face=(50, 70, .45),
   body='<path d="M22 40 L78 40 L72 94 L28 94Z" fill="#AEB8C4" {OL}/><rect x="16" y="32" width="68" height="10" rx="4" fill="#C9D2DC" {OL}/>'
        '<path d="M30 30 C30 18 46 16 48 28 M52 26 C56 14 72 16 70 30" fill="#F6C76A" {OL}/><path d="M8 8 L92 92" stroke="#E8574A" stroke-width="6" stroke-linecap="round"/>'),
 "table_set": dict(words=["المائدة", "ترتيب المائدة", "إعداد المائدة"], anim="bob", face=(50, 46, .45),
   body='<path d="M4 58 L96 58 L86 70 L14 70Z" fill="#C98A55" {OL}/><path d="M20 70 L20 94 M80 70 L80 94" stroke="#8B5E3C" stroke-width="5"/><ellipse cx="50" cy="48" rx="20" ry="8" fill="#fff" {OL}/>'
        '<path d="M22 32 L22 54 M18 32 L18 40 C18 44 26 44 26 40 L26 32" fill="none" stroke="#AEB8C4" stroke-width="3"/><path d="M78 32 L78 54 M78 32 C86 36 86 44 78 46" fill="none" stroke="#AEB8C4" stroke-width="3"/>'),
 "cutlery": dict(words=["الملاعق والشوك", "الملعقة", "الشوكة", "أدوات الطعام"], anim="sway", face=(50, 50, .4),
   body='<ellipse cx="32" cy="26" rx="12" ry="16" fill="#C9D2DC" {OL}/><path d="M32 42 L32 94" stroke="#AEB8C4" stroke-width="7" stroke-linecap="round"/>'
        '<path d="M62 8 L62 32 M70 8 L70 32 M78 8 L78 32 M60 30 C60 42 80 42 80 30" fill="none" stroke="#AEB8C4" stroke-width="4" stroke-linecap="round"/><path d="M70 40 L70 94" stroke="#AEB8C4" stroke-width="7" stroke-linecap="round"/>'),
 "cups": dict(words=["الأكواب", "الكوب", "الكأس الزجاجية"], anim="bob", face=(36, 62, .42),
   body='<path d="M14 30 L54 30 L50 92 L18 92Z" fill="#BFE3F2" {OL}/><path d="M16 50 L52 50 L50 92 L18 92Z" fill="#7CC6F2"/><path d="M60 46 L90 46 L88 92 L62 92Z" fill="#fff" {OL}/>'
        '<path d="M88 56 C98 56 98 76 88 76" fill="none" stroke="#3b2a1a" stroke-width="3"/>'),
 "napkin": dict(words=["مناديل المائدة", "طي المناديل", "المنديل", "المناديل"], anim="wobble", face=(50, 62, .45),
   body='<path d="M10 80 L50 18 L90 80Z" fill="#F59BB8" {OL}/><path d="M50 18 L50 80 M30 50 L50 80 L70 50" fill="none" stroke="#D2627F" stroke-width="2.4"/><rect x="8" y="80" width="84" height="10" rx="4" fill="#fff" {OL}/>'),
 "oven": dict(words=["الفرن", "فرن", "الخبز في الفرن", "المخبز"], anim="wobble", face=(50, 30, .4),
   body='<rect x="10" y="10" width="80" height="84" rx="8" fill="#C9D2DC" {OL}/><rect x="10" y="10" width="80" height="18" rx="6" fill="#AEB8C4" {OL}/><circle cx="24" cy="19" r="4" fill="#3b2a1a"/><circle cx="76" cy="19" r="4" fill="#3b2a1a"/>'
        '<rect x="20" y="38" width="60" height="46" rx="6" fill="#3b3b5c" {OL}/><path d="M28 70 C34 62 40 74 46 66 C52 58 58 72 64 64 C68 60 72 66 74 70" fill="none" stroke="#F6B73C" stroke-width="4" stroke-linecap="round"/><path d="M30 44 L70 44" stroke="#fff" stroke-width="3"/>'),
 "dough": dict(words=["العجين", "العجينة", "عجن", "تحضير العجين", "الخميرة في العجين"], anim="wobble", face=(50, 58, .5),
   body='<path d="M6 60 L94 60 C92 84 72 96 50 96 C28 96 8 84 6 60Z" fill="#AEB8C4" {OL}/><path d="M16 60 C14 36 32 24 50 24 C68 24 86 36 84 60Z" fill="#FFF0D0" {OL}/>'
        '<path d="M30 44 C36 40 42 42 46 46 M56 38 C62 36 68 40 70 44" fill="none" stroke="#E6C890" stroke-width="2.4" stroke-linecap="round"/>'),
 # ---------- the body's care ----------
 "face_wash": dict(words=["غسل الوجه", "غسل اليدين والوجه", "المغسلة", "الوضوء بالماء"], anim="drip", face=(50, 74, .42),
   body='<path d="M8 60 L92 60 C90 84 72 94 50 94 C28 94 10 84 8 60Z" fill="#fff" {OL}/><path d="M64 10 L64 28 L44 28" fill="none" stroke="#AEB8C4" stroke-width="7" stroke-linecap="round"/>'
        '<path d="M44 34 C40 42 40 46 44 48 C48 46 48 42 44 34Z M40 50 C36 56 38 60 42 60 M50 50 C52 54 52 58 48 60" fill="#7CC6F2" {OL}/>'),
 "foot_wash": dict(words=["غسل القدمين", "نظافة القدمين", "القدمين"], anim="drip", face=(50, 80, .38),
   body='<path d="M30 20 C18 20 16 42 20 58 C24 74 22 88 32 90 C42 92 42 80 40 66 C38 52 44 30 30 20Z" fill="#F7C9A4" {OL}/><path d="M70 20 C82 20 84 42 80 58 C76 74 78 88 68 90 C58 92 58 80 60 66 C62 52 56 30 70 20Z" fill="#F7C9A4" {OL}/>'
        '<path d="M50 10 C46 18 46 22 50 24 C54 22 54 18 50 10Z" fill="#7CC6F2" {OL}/><path d="M6 94 L94 94" stroke="#7CC6F2" stroke-width="6" stroke-linecap="round"/>'),
 "nail_clipper": dict(words=["الأظفار", "الأظافر", "قصّاصة الأظفار", "قصاصة الأظافر", "تقليم الأظفار", "تقليم الأظافر", "العناية بالأظافر"], anim="wobble", face=(36, 60, .4),
   body='<path d="M8 60 L74 46 C86 44 92 52 88 58 C84 64 76 64 70 62 L8 66Z" fill="#C9D2DC" {OL}/><path d="M10 72 L70 64 C82 64 88 72 84 78 C80 84 70 82 66 80 L10 78Z" fill="#AEB8C4" {OL}/>'
        '<path d="M30 58 L54 30 L60 34 L40 60" fill="#C9D2DC" {OL}/><circle cx="80" cy="56" r="3" fill="#3b2a1a"/>'),
 "comb": dict(words=["الشعر", "تمشيط الشعر", "المشط", "العناية بالشعر", "قص الشعر"], anim="sway", face=(50, 30, .4), only=["life"],
   body='<rect x="8" y="16" width="84" height="26" rx="8" fill="#F59BB8" {OL}/><path d="M16 42 L16 86 M26 42 L26 86 M36 42 L36 86 M46 42 L46 86 M56 42 L56 86 M66 42 L66 86 M76 42 L76 86 M86 42 L86 80" stroke="#F59BB8" stroke-width="5" stroke-linecap="round"/>'),
 "skin_care": dict(words=["البشرة", "حب الشباب", "العناية بالجسم", "العناية بالبشرة", "النظافة الشخصية للمراهق"], anim="bob", face=(50, 66, .5),
   body='<rect x="16" y="40" width="68" height="52" rx="14" fill="#FFF0D0" {OL}/><rect x="20" y="24" width="60" height="18" rx="6" fill="#6CB8FF" {OL}/>'
        '<path d="M38 52 C42 50 46 54 50 52 C54 50 58 54 62 52" fill="none" stroke="#F59BB8" stroke-width="3" stroke-linecap="round"/><path d="M86 20 L90 12 L94 20 L90 28Z" fill="#FFD25A" {OL}/>'),
 "dandruff": dict(words=["القشرة", "قشرة الرأس"], anim="wiggle", face=(50, 32, .4),
   body='<rect x="10" y="12" width="80" height="22" rx="8" fill="#B0A8C9" {OL}/><path d="M18 34 L18 64 M30 34 L30 64 M42 34 L42 64 M54 34 L54 64 M66 34 L66 64 M78 34 L78 64" stroke="#B0A8C9" stroke-width="5" stroke-linecap="round"/>'
        '<circle cx="24" cy="78" r="3" fill="#fff" {OL}/><circle cx="46" cy="86" r="3" fill="#fff" {OL}/><circle cx="66" cy="76" r="3" fill="#fff" {OL}/><circle cx="80" cy="90" r="3" fill="#fff" {OL}/>'),
 "tap": dict(words=["الصنبور", "إغلاق الصنبور", "الحنفية", "ترشيد استهلاك الماء", "ترشيد المياه"], anim="drip", face=(40, 30, .42),
   body='<rect x="8" y="16" width="20" height="30" rx="4" fill="#AEB8C4" {OL}/><path d="M28 22 L66 22 C78 22 82 30 82 40 L82 50 L68 50 L68 40 C68 36 66 36 62 36 L28 36Z" fill="#C9D2DC" {OL}/>'
        '<rect x="40" y="8" width="14" height="14" rx="3" fill="#E8574A" {OL}/><path d="M75 60 C71 68 71 72 75 74 C79 72 79 68 75 60Z" fill="#7CC6F2" {OL}/><path d="M75 82 C72 88 72 90 75 92 C78 90 78 88 75 82Z" fill="#7CC6F2" {OL}/>'),
 "sanitizer": dict(words=["التعقيم", "المطهر", "المعقم", "الوقاية الصحية", "تعقيم الأدوات", "مطهر اليدين"], anim="bob", face=(46, 70, .45),
   body='<rect x="24" y="40" width="44" height="54" rx="10" fill="#7CC6F2" {OL}/><path d="M34 40 L34 26 L60 26 L60 40" fill="#fff" {OL}/><path d="M38 26 L38 18 L74 18 L74 24" fill="none" stroke="#3b2a1a" stroke-width="3"/>'
        '<path d="M80 22 L86 16 M80 28 L90 28 M80 34 L86 40" stroke="#6CB8FF" stroke-width="3" stroke-linecap="round"/><path d="M38 64 L54 64 M46 56 L46 72" stroke="#fff" stroke-width="5" stroke-linecap="round"/>'),
 "bandage": dict(words=["الضمادات", "الضمادة", "الجروح", "إيقاف النزيف", "الجرح", "تضميد الجروح", "حقيبة الإسعافات الأولية"], anim="wobble", face=(50, 50, .45),
   body='<rect x="6" y="34" width="88" height="32" rx="16" fill="#F2C9A0" {OL} transform="rotate(-25 50 50)"/><rect x="34" y="36" width="32" height="28" rx="6" fill="#FFF0D0" {OL} transform="rotate(-25 50 50)"/>'
        '<circle cx="20" cy="56" r="1.6" fill="#C98A55"/><circle cx="80" cy="44" r="1.6" fill="#C98A55"/>'),
 "burn": dict(words=["الحروق", "درجات الحروق", "الحرق", "إسعاف الحروق"], anim="wobble", face=(50, 70, .42),
   body='<path d="M50 6 C62 22 78 30 76 56 C74 78 62 90 50 90 C38 90 26 78 24 56 C24 40 34 34 38 20 C42 30 46 32 50 6Z" fill="#F6A23C" {OL}/><path d="M50 40 C56 50 64 56 62 70 C60 80 54 84 50 84 C46 84 40 80 38 70 C38 60 46 54 50 40Z" fill="#FFD25A"/>'
        '<path d="M80 74 C78 80 78 84 82 86 C86 84 86 80 84 74 M88 60 C86 64 86 66 89 68 C92 66 92 64 90 60" fill="#7CC6F2" {OL}/>'),
 "nosebleed": dict(words=["الرعاف", "نزيف الأنف"], anim="drip", face=(50, 74, .4),
   body='<rect x="16" y="54" width="68" height="40" rx="6" fill="#fff" {OL}/><path d="M34 54 C34 40 46 36 50 44 C54 36 66 40 66 54" fill="#fff" {OL}/>'
        '<path d="M50 6 C42 22 40 30 50 34 C60 30 58 22 50 6Z" fill="#E8574A" {OL}/>'),
 "choking": dict(words=["الغصص", "الضرب على الظهر", "الشرقة", "انسداد مجرى التنفس"], anim="wobble", face=(50, 56, .45),
   body='<rect x="24" y="22" width="52" height="72" rx="20" fill="#F7C9A4" {OL}/><path d="M50 30 L50 60" stroke="#E8574A" stroke-width="5" stroke-linecap="round"/><circle cx="50" cy="44" r="7" fill="#C98A55" {OL}/>'
        '<path d="M84 30 L96 30 M84 40 L94 46 M84 20 L94 14" stroke="#3b2a1a" stroke-width="3" stroke-linecap="round"/>'),
 "fracture": dict(words=["الكسور", "كسر العظم", "الجبيرة", "كسور العظام"], anim="wobble", face=(50, 50, .45),
   body='<path d="M10 40 C2 34 6 22 16 26 C20 18 32 20 30 30 L44 44 L56 56 L70 70 C80 68 84 80 76 84 C80 94 68 98 64 88 L50 74" fill="#FFF8E8" {OL}/>'
        '<path d="M44 44 L50 52 L46 56 L56 56" fill="none" stroke="#E8574A" stroke-width="3"/><rect x="30" y="38" width="40" height="26" rx="6" fill="#fff" opacity=".85" {OL} transform="rotate(45 50 51)"/>'),
 "sport_injury": dict(words=["الإصابة أثناء اللعب", "الإصابات الرياضية", "إصابات الملاعب"], anim="bounce", face=(50, 50, .45),
   body='<circle cx="50" cy="50" r="40" fill="#fff" {OL}/><path d="M50 22 L66 34 L60 52 L40 52 L34 34Z" fill="#3b2a1a"/><path d="M16 60 L36 54 M84 60 L64 54 M40 80 L44 60 M60 80 L56 60" stroke="#3b2a1a" stroke-width="2.6"/>'
        '<rect x="56" y="64" width="34" height="14" rx="7" fill="#F2C9A0" {OL} transform="rotate(-30 73 71)"/>'),
 "pulse": dict(words=["النبض", "قياس النبض", "نبضات القلب", "معدل ضربات القلب"], anim="bounce", face=(50, 44, .45),
   body='<path d="M50 84 C20 64 6 46 8 30 C10 14 32 8 50 26 C68 8 90 14 92 30 C94 46 80 64 50 84Z" fill="#E8574A" {OL}/>'
        '<path d="M6 60 L28 60 L36 46 L46 74 L56 52 L62 60 L94 60" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>'),
 "dose": dict(words=["الجرعة", "الجرعة الزائدة", "التسمم الدوائي", "جرعة الدواء", "الاستخدام الآمن للدواء"], anim="wobble", face=(36, 64, .42),
   body='<rect x="12" y="34" width="44" height="60" rx="8" fill="#F6B73C" {OL}/><rect x="16" y="20" width="36" height="14" rx="4" fill="#fff" {OL}/><rect x="12" y="50" width="44" height="20" fill="#fff"/>'
        '<path d="M64 52 L90 52 L86 80 L68 80Z" fill="#BFE3F2" {OL}/><path d="M66 64 L88 64" stroke="#3b2a1a" stroke-width="2"/>'),
 "food_poison": dict(words=["التسمم الغذائي", "تسمم الطعام", "الطعام الفاسد"], anim="wiggle", face=(50, 58, .45),
   body='<ellipse cx="50" cy="70" rx="44" ry="22" fill="#fff" {OL}/><path d="M18 64 C22 44 78 44 82 64Z" fill="#A9C35A" {OL}/>'
        '<path d="M32 40 C28 30 36 26 32 16 M50 36 C46 26 54 22 50 12 M68 40 C64 30 72 26 68 16" fill="none" stroke="#8BB04A" stroke-width="3" stroke-linecap="round"/><circle cx="40" cy="58" r="3" fill="#6B8A2A"/><circle cx="60" cy="56" r="3" fill="#6B8A2A"/>'),
 "no_smoking": dict(words=["التدخين", "السيجارة", "الدخان", "أضرار التدخين", "التدخين السلبي", "الشيشة"], anim="wobble", face=(50, 50, .4),
   body='<circle cx="50" cy="50" r="44" fill="#fff" {OL}/><rect x="16" y="44" width="56" height="12" fill="#fff" {OL}/><rect x="72" y="44" width="12" height="12" fill="#F6B73C" {OL}/>'
        '<path d="M80 36 C76 30 84 26 80 18" fill="none" stroke="#AEB8C4" stroke-width="3" stroke-linecap="round"/><circle cx="50" cy="50" r="40" fill="none" stroke="#E8574A" stroke-width="8"/><path d="M22 22 L78 78" stroke="#E8574A" stroke-width="8"/>'),
 "no_drugs": dict(words=["المخدرات", "المؤثرات العقلية", "علامات التعاطي", "الإدمان", "التعاطي", "الوقاية من المخدرات", "مكافحة المخدرات"], anim="wobble", face=(50, 74, .38),
   body='<path d="M50 6 L94 84 L6 84Z" fill="#FFD25A" {OL}/><rect x="30" y="38" width="40" height="18" rx="9" fill="#fff" {OL} transform="rotate(-20 50 47)"/><path d="M50 38 L50 56" stroke="#3b2a1a" stroke-width="2.6" transform="rotate(-20 50 47)"/>'
        '<path d="M26 34 L74 66" stroke="#E8574A" stroke-width="6" stroke-linecap="round"/>'),
 "screen_addiction": dict(words=["إدمان الأجهزة", "إدمان الإنترنت", "الإفراط في استخدام الأجهزة", "التوازن الرقمي", "وقت الشاشة"], anim="wobble", face=(50, 46, .42),
   body='<rect x="28" y="8" width="44" height="76" rx="8" fill="#3b3b5c" {OL}/><rect x="32" y="16" width="36" height="58" rx="3" fill="#BFE3F2"/>'
        '<path d="M8 70 C18 62 22 76 32 70 M68 70 C78 62 82 76 92 70" fill="none" stroke="#AEB8C4" stroke-width="6" stroke-linecap="round"/><circle cx="50" cy="90" r="6" fill="#E8574A" {OL}/>'),
 # ---------- safety ----------
 "crossing": dict(words=["عبور الشارع", "النزول من جهة الرصيف", "ممر المشاة", "إشارة المرور", "الرصيف"], anim="bob", face=(78, 30, .38),
   body='<rect x="4" y="60" width="92" height="34" fill="#5D646E" {OL}/><path d="M14 66 L14 88 M30 66 L30 88 M46 66 L46 88 M62 66 L62 88 M78 66 L78 88" stroke="#fff" stroke-width="8"/>'
        '<rect x="66" y="8" width="24" height="46" rx="6" fill="#3b3b5c" {OL}/><circle cx="78" cy="20" r="6" fill="#E8574A"/><circle cx="78" cy="38" r="6" fill="#6CC27A"/><path d="M78 54 L78 60" stroke="#3b2a1a" stroke-width="4"/>'),
 "danger_sign": dict(words=["الرموز الإرشادية", "علامة الخطر", "علامات التحذير", "إشارات السلامة", "اللافتات التحذيرية", "الإنذار"], anim="wobble", face=(50, 70, .38),
   body='<path d="M50 6 L94 86 L6 86Z" fill="#FFD25A" {OL}/><path d="M50 30 L50 60" stroke="#3b2a1a" stroke-width="8" stroke-linecap="round"/><circle cx="50" cy="74" r="5" fill="#3b2a1a"/>'),
 "door_stranger": dict(words=["عدم فتح الباب للغرباء", "الغرباء", "الحذر من الغرباء", "الأمان في المنزل"], anim="wobble", face=(40, 50, .45),
   body='<rect x="18" y="6" width="64" height="88" rx="4" fill="#C98A55" {OL}/><circle cx="68" cy="52" r="5" fill="#FFD25A" {OL}/><circle cx="50" cy="26" r="6" fill="#3b3b5c" {OL}/>'
        '<rect x="56" y="62" width="22" height="18" rx="3" fill="#AEB8C4" {OL}/><path d="M60 62 L60 56 C60 48 74 48 74 56 L74 62" fill="none" stroke="#3b2a1a" stroke-width="3"/>'),
 "wet_floor": dict(words=["الأرضية المبللة", "الانزلاق", "أرضية زلقة"], anim="wobble", face=(50, 46, .42),
   body='<path d="M30 10 L70 10 L84 86 L16 86Z" fill="#FFD25A" {OL}/><path d="M50 26 C44 38 42 44 50 48 C58 44 56 38 50 26Z" fill="#7CC6F2" {OL}/>'
        '<path d="M8 92 C20 86 34 96 50 90 C66 84 80 96 92 90" fill="none" stroke="#7CC6F2" stroke-width="5" stroke-linecap="round"/>'),
 "loud_noise": dict(words=["الأصوات العالية", "الضوضاء", "التلوث السمعي", "الضجيج"], anim="buzz", face=(30, 50, .4),
   body='<path d="M10 36 L28 36 L50 16 L50 84 L28 64 L10 64Z" fill="#AEB8C4" {OL}/><path d="M60 36 C66 42 66 58 60 64 M70 26 C80 38 80 62 70 74 M80 16 C94 34 94 66 80 84" fill="none" stroke="#E8574A" stroke-width="4" stroke-linecap="round"/>'),
 "wires": dict(words=["الأسلاك", "الأسلاك الكهربائية", "المقابس الكهربائية", "السلامة الكهربائية", "الأفياش"], anim="buzz", face=(30, 34, .4), only=["life", "science"],
   body='<rect x="10" y="12" width="40" height="44" rx="8" fill="#fff" {OL}/><circle cx="22" cy="34" r="4" fill="#3b2a1a"/><circle cx="38" cy="34" r="4" fill="#3b2a1a"/>'
        '<path d="M30 56 C30 76 60 70 64 86 C66 94 82 94 88 88" fill="none" stroke="#3b2a1a" stroke-width="5" stroke-linecap="round"/><path d="M66 18 L58 34 L68 34 L60 50" fill="none" stroke="#FFD25A" stroke-width="4" stroke-linejoin="round"/>'),
 "sharp_tools": dict(words=["الأدوات الحادة", "السكين", "المقص", "استخدام الأدوات الحادة"], anim="wobble", face=(36, 70, .4),
   body='<path d="M20 90 L20 56 L48 10 L50 12 L36 56 L36 90Z" fill="#C9D2DC" {OL}/><rect x="16" y="60" width="24" height="34" rx="6" fill="#8B5E3C" {OL}/>'
        '<circle cx="66" cy="80" r="9" fill="none" stroke="#E8574A" stroke-width="5"/><circle cx="86" cy="80" r="9" fill="none" stroke="#E8574A" stroke-width="5"/><path d="M70 72 L84 20 M82 72 L68 20" stroke="#AEB8C4" stroke-width="5" stroke-linecap="round"/>'),
 "lifebuoy": dict(words=["المنقذ", "طوق النجاة", "السلامة في المسبح", "السباحة الآمنة", "الغرق"], anim="sway", face=(50, 50, .4),
   body='<circle cx="50" cy="50" r="42" fill="#E8574A" {OL}/><circle cx="50" cy="50" r="20" fill="#7CC6F2" {OL}/><path d="M50 8 L50 30 M50 70 L50 92 M8 50 L30 50 M70 50 L92 50" stroke="#fff" stroke-width="14"/>'
        '<circle cx="50" cy="50" r="42" fill="none" {OL}/>'),
 # ---------- the home and its things ----------
 "fridge": dict(words=["الثلاجة", "حفظ الطعام في الثلاجة"], anim="wobble", face=(50, 70, .45),
   body='<rect x="20" y="4" width="60" height="92" rx="8" fill="#E8F2F8" {OL}/><path d="M20 40 L80 40" stroke="#3b2a1a" stroke-width="2.6"/><path d="M28 18 L28 32 M28 50 L28 64" stroke="#AEB8C4" stroke-width="5" stroke-linecap="round"/>'
        '<path d="M64 14 L64 30 M58 18 L70 26 M70 18 L58 26" stroke="#6CB8FF" stroke-width="2.4"/>'),
 "wardrobe": dict(words=["الخزانة", "خزانة الملابس", "ترتيب الخزانة", "الدولاب"], anim="bob", face=(50, 30, .4),
   body='<rect x="12" y="6" width="76" height="84" rx="4" fill="#C98A55" {OL}/><path d="M50 6 L50 90" stroke="#3b2a1a" stroke-width="2.6"/><circle cx="44" cy="50" r="3" fill="#FFD25A" {OL}/><circle cx="56" cy="50" r="3" fill="#FFD25A" {OL}/>'
        '<path d="M18 90 L18 96 M82 90 L82 96" stroke="#3b2a1a" stroke-width="4"/>'),
 "uniform": dict(words=["الزي المدرسي", "الملابس المدرسية", "الثوب المدرسي"], anim="sway", face=(50, 56, .45),
   body='<path d="M30 8 L14 22 L4 44 L22 52 L26 40 L26 94 L74 94 L74 40 L78 52 L96 44 L86 22 L70 8 C66 18 34 18 30 8Z" fill="#fff" {OL}/>'
        '<path d="M42 12 L50 26 L58 12" fill="none" stroke="#3b2a1a" stroke-width="2.6"/><circle cx="50" cy="40" r="2.4" fill="#3b2a1a"/><rect x="58" y="36" width="10" height="8" fill="#6CB8FF"/>'),
 "hat": dict(words=["القبعة", "قبعة", "غطاء الرأس", "الطاقية"], anim="bob", face=(50, 50, .45),
   body='<path d="M22 64 C22 30 78 30 78 64Z" fill="#6CB8FF" {OL}/><path d="M4 66 C20 58 80 58 96 66 C80 76 20 76 4 66Z" fill="#4A90D9" {OL}/><path d="M24 56 L76 56" stroke="#FFD25A" stroke-width="5"/>'),
 "sunglasses": dict(words=["النظارة الشمسية", "نظارة شمسية", "حماية العينين من الشمس"], anim="sun", face=(50, 30, .35),
   body='<circle cx="80" cy="16" r="10" fill="#FFD25A" {OL}/><path d="M6 46 L94 46" stroke="#3b2a1a" stroke-width="4"/>'
        '<path d="M8 46 L44 46 L42 62 C40 74 12 74 10 62Z" fill="#3b3b5c" {OL}/><path d="M56 46 L92 46 L90 62 C88 74 60 74 58 62Z" fill="#3b3b5c" {OL}/><path d="M16 52 L24 50 M64 52 L72 50" stroke="#fff" stroke-width="2.4"/>'),
 "buttons": dict(words=["الأزرار", "الكبسون", "خياطة الأزرار", "تركيب الأزرار", "الزر"], anim="wobble", face=(36, 46, .45), only=["life", "english"],
   body='<circle cx="36" cy="46" r="28" fill="#F6B73C" {OL}/><circle cx="28" cy="40" r="3.4" fill="#3b2a1a"/><circle cx="44" cy="40" r="3.4" fill="#3b2a1a"/><circle cx="28" cy="54" r="3.4" fill="#3b2a1a"/><circle cx="44" cy="54" r="3.4" fill="#3b2a1a"/>'
        '<circle cx="76" cy="74" r="16" fill="#AEB8C4" {OL}/><circle cx="76" cy="74" r="6" fill="#C9D2DC" {OL}/>'),
 "tape_measure": dict(words=["المقاس", "المقاسات", "شريط القياس", "أخذ المقاسات"], anim="wobble", face=(36, 50, .42),
   body='<circle cx="36" cy="50" r="28" fill="#FFD25A" {OL}/><circle cx="36" cy="50" r="8" fill="#F6B73C" {OL}/><path d="M60 64 L96 64 L96 78 L56 78" fill="#FFF3C4" {OL}/>'
        '<path d="M66 64 L66 70 M74 64 L74 72 M82 64 L82 70 M90 64 L90 72" stroke="#3b2a1a" stroke-width="2"/>'),
 "sorting": dict(words=["الفرز", "فرز الملابس", "فرز النفايات", "التصنيف حسب النوع"], anim="bounce", face=(50, 30, .35),
   body='<rect x="4" y="50" width="28" height="44" rx="4" fill="#6CB8FF" {OL}/><rect x="36" y="50" width="28" height="44" rx="4" fill="#6CC27A" {OL}/><rect x="68" y="50" width="28" height="44" rx="4" fill="#F6B73C" {OL}/>'
        '<path d="M50 10 L50 34 M42 26 L50 36 L58 26" fill="none" stroke="#3b2a1a" stroke-width="4" stroke-linecap="round"/>'),
 "stain": dict(words=["البقع", "إزالة البقع", "البقعة", "تنظيف البقع"], anim="wiggle", face=(50, 64, .42),
   body='<path d="M30 8 L14 22 L4 44 L22 52 L26 40 L26 94 L74 94 L74 40 L78 52 L96 44 L86 22 L70 8 C66 18 34 18 30 8Z" fill="#BFE3F2" {OL}/>'
        '<path d="M44 46 C36 40 40 30 50 34 C58 28 66 38 60 46 C68 50 62 62 52 58 C46 66 34 60 38 52 C32 50 36 44 44 46Z" fill="#9B6A2B"/>'),
 "flower_pot": dict(words=["الأصيص", "أصيص الزرع", "زراعة النباتات المنزلية", "النباتات المنزلية"], anim="sway", face=(50, 76, .42),
   body='<path d="M24 60 L76 60 L70 94 L30 94Z" fill="#C98A55" {OL}/><rect x="20" y="54" width="60" height="10" rx="3" fill="#B5651D" {OL}/><path d="M50 54 L50 26" stroke="#5A9A3A" stroke-width="4"/>'
        '<path d="M50 40 C36 36 30 24 34 18 C44 20 50 30 50 40Z M50 32 C62 26 70 14 66 8 C56 10 50 22 50 32Z" fill="#6CC27A" {OL}/>'),
 "classroom": dict(words=["الفصل الدراسي", "الصف الدراسي", "غرفة الصف", "قوانين الصف", "اللوائح المدرسية"], anim="bob", face=(50, 40, .4),
   body='<rect x="6" y="10" width="88" height="56" rx="4" fill="#3E7A5A" {OL}/><rect x="6" y="10" width="88" height="56" rx="4" fill="none" stroke="#C98A55" stroke-width="4"/>'
        '<path d="M16 26 L40 26 M16 36 L52 36" stroke="#fff" stroke-width="3" stroke-linecap="round"/><path d="M14 80 L40 80 M60 80 L86 80" stroke="#C98A55" stroke-width="6"/><path d="M18 80 L18 94 M36 80 L36 94 M64 80 L64 94 M82 80 L82 94" stroke="#8B5E3C" stroke-width="3"/>'),
 "timetable": dict(words=["الجدول الدراسي", "الجدولة", "توزيع المهام", "تنظيم الوقت", "إدارة الوقت", "الجدول اليومي", "التخطيط اليومي"], anim="bob", face=(50, 60, .42),
   body='<rect x="8" y="10" width="84" height="84" rx="6" fill="#fff" {OL}/><rect x="8" y="10" width="84" height="16" rx="6" fill="#E8574A" {OL}/>'
        '<path d="M8 46 L92 46 M8 66 L92 66 M36 26 L36 94 M64 26 L64 94" stroke="#AEB8C4" stroke-width="2"/><rect x="40" y="30" width="20" height="12" fill="#6CB8FF"/><rect x="12" y="50" width="20" height="12" fill="#6CC27A"/><rect x="68" y="70" width="20" height="12" fill="#F6B73C"/>'),
 "clock_hands": dict(words=["عقرب الساعات", "عقرب الدقائق", "عقرب الثواني", "قراءة الساعة"], anim="sun", face=(50, 70, .38),
   body='<circle cx="50" cy="50" r="42" fill="#fff" {OL}/><path d="M50 50 L50 22" stroke="#E8574A" stroke-width="5" stroke-linecap="round"/><path d="M50 50 L70 50" stroke="#3b2a1a" stroke-width="7" stroke-linecap="round"/>'
        '<circle cx="50" cy="50" r="4" fill="#3b2a1a"/><path d="M50 12 L50 18 M88 50 L82 50 M50 88 L50 82 M12 50 L18 50" stroke="#3b2a1a" stroke-width="3"/>'),
 "healthy_home": dict(words=["المسكن الصحي", "التهوية", "تهوية المنزل", "البيت الصحي"], anim="wind", face=(50, 74, .4),
   body='<path d="M10 46 L50 12 L90 46 L90 94 L10 94Z" fill="#F2D07A" {OL}/><path d="M4 50 L50 10 L96 50" fill="none" stroke="#E8574A" stroke-width="6" stroke-linecap="round"/>'
        '<rect x="22" y="52" width="22" height="20" fill="#BFE3F2" {OL}/><path d="M33 52 L33 72 M22 62 L44 62" stroke="#3b2a1a" stroke-width="2"/><path d="M52 58 C62 54 70 62 80 58 M54 68 C64 64 72 72 82 68" fill="none" stroke="#6CB8FF" stroke-width="3" stroke-linecap="round"/>'),
 "public_place": dict(words=["الأماكن العامة", "الحدائق العامة", "المحافظة على المرافق العامة", "الذوق العام"], anim="sway", face=(50, 52, .4),
   body='<path d="M6 94 L94 94" stroke="#6CC27A" stroke-width="8" stroke-linecap="round"/><rect x="10" y="56" width="52" height="8" rx="3" fill="#C98A55" {OL}/><rect x="10" y="40" width="52" height="8" rx="3" fill="#C98A55" {OL}/>'
        '<path d="M16 64 L16 90 M56 64 L56 90" stroke="#8B5E3C" stroke-width="4"/><path d="M80 90 L80 50" stroke="#8B5E3C" stroke-width="5"/><circle cx="80" cy="40" r="16" fill="#6CC27A" {OL}/>'),
 "gadgets": dict(words=["الأجهزة الإلكترونية", "الأجهزة الذكية"], anim="bob", face=(36, 50, .4),
   body='<rect x="8" y="16" width="56" height="74" rx="8" fill="#3b3b5c" {OL}/><rect x="14" y="24" width="44" height="56" rx="3" fill="#BFE3F2"/>'
        '<rect x="66" y="40" width="28" height="50" rx="6" fill="#5A5A7C" {OL}/><rect x="70" y="46" width="20" height="36" rx="2" fill="#FFF3C4"/>'),
 "billboard": dict(words=["الإعلان", "الدعاية", "الإعلانات", "الإعلان التجاري", "الملصق الإعلاني", "الإعلان المتحرك", "التسويق", "التسويق الإلكتروني", "الحملة التسويقية"], never=["social"], anim="sway", face=(50, 34, .42),
   body='<rect x="6" y="10" width="88" height="50" rx="4" fill="#fff" {OL}/><path d="M14 22 L54 22 M14 32 L44 32" stroke="#E8574A" stroke-width="5" stroke-linecap="round"/><path d="M60 48 L70 22 L80 48Z" fill="#FFD25A" {OL}/>'
        '<path d="M30 60 L30 94 M70 60 L70 94" stroke="#8B5E3C" stroke-width="6"/>'),
 "cart": dict(words=["المستهلك", "سلوك المستهلك", "النزعة الاستهلاكية", "التسوق", "حقوق المستهلك"], anim="bounce", face=(50, 50, .42),
   body='<path d="M4 14 L18 14 L28 64 L82 64 L92 28 L22 28" fill="none" stroke="#3b2a1a" stroke-width="5" stroke-linejoin="round"/><path d="M24 30 L90 30 L82 62 L30 62Z" fill="#6CB8FF" opacity=".55"/>'
        '<circle cx="34" cy="80" r="8" fill="#AEB8C4" {OL}/><circle cx="76" cy="80" r="8" fill="#AEB8C4" {OL}/>'),
 "bottles_cans": dict(words=["العلب والزجاجات", "إعادة استخدام العلب", "الزجاجات الفارغة"], anim="wobble", face=(30, 66, .38),
   body='<path d="M20 30 L20 18 L36 18 L36 30 C46 36 48 46 48 56 L48 94 L8 94 L8 56 C8 46 10 36 20 30Z" fill="#7CC6F2" {OL}/><rect x="54" y="40" width="36" height="54" rx="6" fill="#E8574A" {OL}/>'
        '<ellipse cx="72" cy="40" rx="18" ry="5" fill="#C9D2DC" {OL}/><path d="M60 58 L84 58" stroke="#fff" stroke-width="5"/>'),
 "storm_umbrella": dict(words=["الأزمات", "إدارة الأزمات", "مواجهة الأزمات", "خطة الطوارئ"], anim="wobble", face=(50, 46, .42),
   body='<path d="M20 30 C14 14 34 6 42 16 C48 4 70 6 72 20 C86 18 90 34 78 38 L24 38 C10 38 10 26 20 30Z" fill="#8A93A6" {OL}/><path d="M50 40 L44 54 L52 54 L46 68" fill="none" stroke="#FFD25A" stroke-width="4" stroke-linejoin="round"/>'
        '<path d="M14 72 C20 56 80 56 86 72Z" fill="#E8574A" {OL}/><path d="M50 72 L50 92 C50 96 44 96 44 92" fill="none" stroke="#3b2a1a" stroke-width="4"/>'),
 # ---------- manners, feelings and the people around us ----------
 "good_deed": dict(words=["التصرف الحسن", "التصرفات الإيجابية", "السلوك الإيجابي", "السلوك الحسن"], anim="bounce", face=(50, 56, .45),
   body='<circle cx="50" cy="50" r="44" fill="#6CC27A" {OL}/><path d="M28 50 L44 66 L74 34" fill="none" stroke="#fff" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/>'),
 "bad_deed": dict(words=["التصرف الخاطئ", "التصرفات الخاطئة", "السلوك السلبي", "السلوك الخاطئ"], anim="wobble", face=(50, 56, .45),
   body='<circle cx="50" cy="50" r="44" fill="#E8574A" {OL}/><path d="M32 32 L68 68 M68 32 L32 68" stroke="#fff" stroke-width="10" stroke-linecap="round"/>'),
 "virtues": dict(words=["الصفات الحميدة", "الصفات الحسنة", "الشخصية المثالية", "الأخلاق الحميدة", "القيم الأخلاقية", "الأخلاق الحسنة"], anim="sun", face=(50, 54, .45),
   body='<path d="M50 4 L62 34 L94 36 L68 56 L78 88 L50 70 L22 88 L32 56 L6 36 L38 34Z" fill="#FFD25A" {OL}/><path d="M50 66 C38 58 34 50 38 44 C42 38 48 40 50 46 C52 40 58 38 62 44 C66 50 62 58 50 66Z" fill="#E8574A"/>'),
 "apology": dict(words=["الاعتذار", "آسف", "طلب السماح", "التسامح"], anim="bob", face=(50, 46, .45),
   body='<path d="M50 88 C20 68 6 50 8 32 C10 16 32 10 50 28 C68 10 90 16 92 32 C94 50 80 68 50 88Z" fill="#F59BB8" {OL}/>'
        '<rect x="24" y="48" width="52" height="14" rx="7" fill="#F2C9A0" {OL} transform="rotate(-20 50 55)"/>'),
 "greeting": dict(words=["السلام", "إلقاء التحية", "التعارف"], anim="wiggle", face=(46, 60, .45),
   body='<path d="M30 94 L30 50 C30 44 38 44 38 50 L38 30 C38 24 46 24 46 30 L46 26 C46 20 54 20 54 26 L54 30 C54 24 62 24 62 30 L62 40 C62 34 70 34 70 40 L70 70 C70 84 62 94 50 94Z" fill="#F7C9A4" {OL}/>'
        '<path d="M80 22 C86 28 86 36 80 42 M88 16 C96 26 96 38 88 48" fill="none" stroke="#3b2a1a" stroke-width="3" stroke-linecap="round"/>'),
 "guests": dict(words=["الضيوف", "الزيارة", "استقبال الضيوف", "يزور", "زيارة الأقارب"], anim="bob", face=(36, 52, .42),
   body='<rect x="10" y="10" width="52" height="84" rx="4" fill="#C98A55" {OL}/><circle cx="52" cy="54" r="4" fill="#FFD25A" {OL}/><rect x="4" y="86" width="64" height="8" rx="3" fill="#E8574A" {OL}/>'
        '<path d="M78 22 C70 22 70 34 78 34 C86 34 86 22 78 22Z M66 60 C66 44 90 44 90 60" fill="#6CB8FF" {OL}/><path d="M86 70 C80 64 74 70 80 76 L86 82 L92 76 C98 70 92 64 86 70Z" fill="#E8574A"/>'),
 "permission": dict(words=["الاستئذان", "طرق الباب", "آداب الاستئذان"], anim="wobble", face=(36, 50, .42),
   body='<rect x="10" y="6" width="56" height="88" rx="4" fill="#C98A55" {OL}/><circle cx="56" cy="52" r="4" fill="#FFD25A" {OL}/><circle cx="82" cy="40" r="9" fill="#F7C9A4" {OL}/>'
        '<path d="M70 26 L74 30 M70 54 L74 50 M90 26 L86 30" stroke="#3b2a1a" stroke-width="3" stroke-linecap="round"/><path d="M76 66 C76 58 92 58 92 66 L92 80 L76 80Z" fill="#fff" {OL}/>'),
 "listening": dict(words=["الإنصات", "حسن الاستماع", "الاستماع الجيد", "الاستماع للآخرين", "آداب الاستماع"], anim="sway", face=(40, 50, .42),
   body='<path d="M60 20 C40 0 10 14 14 44 C16 58 30 60 30 72 C30 88 44 94 54 86 C60 80 56 72 62 64 C72 50 78 36 60 20Z" fill="#F7C9A4" {OL}/>'
        '<path d="M34 40 C34 28 52 26 54 38 C56 48 44 50 44 58" fill="none" stroke="#C98A55" stroke-width="3" stroke-linecap="round"/><path d="M78 34 C84 40 84 50 78 56 M86 26 C96 36 96 56 86 66" fill="none" stroke="#6CB8FF" stroke-width="3" stroke-linecap="round"/>'),
 "dialogue2": dict(words=["الحوار", "آداب الحوار", "أهمية الحوار", "أركان الحوار", "المتحاورون", "موضوع الحوار", "الرأي والرأي الآخر", "الحوار الهادف", "النقاش"], anim="bob", face=(34, 36, .4),
   body='<path d="M6 12 L62 12 C66 12 68 14 68 18 L68 50 C68 54 66 56 62 56 L30 56 L16 68 L18 56 L12 56 C8 56 6 54 6 50Z" fill="#6CB8FF" {OL}/>'
        '<path d="M94 40 L44 40 C40 40 38 42 38 46 L38 76 C38 80 40 82 44 82 L72 82 L86 94 L84 82 L88 82 C92 82 94 80 94 76Z" fill="#FFD25A" {OL}/><path d="M50 56 L82 56 M50 66 L74 66" stroke="#3b2a1a" stroke-width="3" stroke-linecap="round"/>'),
 "calm": dict(words=["الهدوء", "ضبط النفس", "الهدوء عند الغضب", "التحكم في الغضب"], anim="sway", face=(50, 50, .45),
   body='<circle cx="50" cy="50" r="44" fill="#BFE3F2" {OL}/><path d="M18 62 C30 54 40 70 50 62 C60 54 70 70 82 62" fill="none" stroke="#6CB8FF" stroke-width="4" stroke-linecap="round"/>'
        '<path d="M50 20 C40 30 40 40 50 46 C60 40 60 30 50 20Z" fill="#6CC27A" {OL}/>'),
 "no_interrupt": dict(words=["عدم المقاطعة", "احترام دور الآخرين", "انتظار الدور"], anim="wobble", face=(36, 34, .38),
   body='<path d="M6 10 L66 10 C70 10 72 12 72 16 L72 52 C72 56 70 58 66 58 L34 58 L18 72 L20 58 L12 58 C8 58 6 56 6 52Z" fill="#6CB8FF" {OL}/>'
        '<path d="M66 94 L66 70 C66 66 72 66 72 70 L72 62 C72 58 78 58 78 62 L78 60 C78 56 84 56 84 60 L84 64 C84 60 90 60 90 64 L90 82 C90 90 84 94 78 94Z" fill="#F7C9A4" {OL}/>'),
 "handshake": dict(words=["التفاوض", "التسوية", "حل النزاع", "الصراع", "إدارة الصراع", "حل الخلافات", "الصلح", "الشراكة", "التعايش", "التعايش السلمي"], anim="wiggle", face=(50, 30, .4),
   body='<path d="M4 50 L24 40 L40 46 L56 40 L76 46 L96 40 L96 66 L76 72 L60 84 C54 88 48 84 50 78 L40 82 C34 84 30 78 34 74 L26 74 C20 74 20 66 26 64 L4 66Z" fill="#F7C9A4" {OL}/>'
        '<path d="M4 44 L22 36 L22 70 L4 72Z" fill="#6CB8FF" {OL}/><path d="M96 34 L78 40 L78 72 L96 70Z" fill="#E8574A" {OL}/>'),
 "smile": dict(words=["الابتسامة", "البشاشة", "التفاؤل والابتسامة"], anim="bounce", face=None,
   body='<circle cx="50" cy="50" r="44" fill="#FFD25A" {OL}/><circle cx="34" cy="40" r="5" fill="#3b2a1a"/><circle cx="66" cy="40" r="5" fill="#3b2a1a"/><path d="M26 58 C34 80 66 80 74 58Z" fill="#fff" {OL}/>'),
 "charity": dict(words=["التبرع", "مساعدة المحتاجين", "العمل الإغاثي", "الجمعيات الأهلية", "الجمعيات الخيرية", "خدمة"], anim="bounce", face=(50, 66, .45),
   body='<rect x="14" y="40" width="72" height="54" rx="4" fill="#F6B73C" {OL}/><rect x="10" y="30" width="80" height="16" rx="3" fill="#E8574A" {OL}/><path d="M50 30 L50 94" stroke="#E8574A" stroke-width="8"/>'
        '<path d="M50 28 C40 10 26 18 34 26 C38 30 46 30 50 28 C54 30 62 30 66 26 C74 18 60 10 50 28Z" fill="#E8574A" {OL}/>'),
 "diligence": dict(words=["الاجتهاد", "أداء الواجبات", "الواجب المنزلي", "إتقان العمل", "المثابرة", "الجد والاجتهاد"], anim="bob", face=(40, 56, .42),
   body='<rect x="10" y="20" width="60" height="74" rx="4" fill="#fff" {OL}/><path d="M18 36 L60 36 M18 48 L60 48 M18 60 L50 60" stroke="#6CB8FF" stroke-width="3"/>'
        '<path d="M66 82 L90 22 L98 26 L74 86 L64 92Z" fill="#FFD25A" {OL}/><path d="M80 6 L84 14 L92 16 L86 22 L88 30 L80 26 L72 30 L74 22 L68 16 L76 14Z" fill="#F6B73C" {OL}/>'),
 "attention": dict(words=["الانتباه", "التركيز في الدرس"], anim="sun", face=None,
   body='<path d="M4 50 C22 20 78 20 96 50 C78 80 22 80 4 50Z" fill="#fff" {OL}/><circle cx="50" cy="50" r="20" fill="#6CB8FF" {OL}/><circle cx="50" cy="50" r="9" fill="#3b2a1a"/><circle cx="56" cy="44" r="4" fill="#fff"/>'
        '<path d="M50 4 L50 14 M20 12 L26 20 M80 12 L74 20" stroke="#F6B73C" stroke-width="4" stroke-linecap="round"/>'),
 "optimism": dict(words=["التفاؤل", "الأمل", "النظرة الإيجابية"], anim="sun", face=(50, 60, .45),
   body='<path d="M6 80 L94 80" stroke="#6CC27A" stroke-width="8" stroke-linecap="round"/><path d="M18 80 C18 40 82 40 82 80Z" fill="#FFD25A" {OL}/>'
        '<path d="M50 30 L50 14 M24 42 L14 32 M76 42 L86 32 M10 64 L2 62 M90 64 L98 62" stroke="#F6B73C" stroke-width="4" stroke-linecap="round"/>'),
 "friend": dict(words=["الصديق", "الصديق الصالح", "الصداقة", "اختيار الأصدقاء", "الأصدقاء"], anim="sway", face=(50, 30, .35),
   body='<circle cx="30" cy="34" r="14" fill="#6CB8FF" {OL}/><circle cx="70" cy="34" r="14" fill="#F59BB8" {OL}/><path d="M10 92 C10 62 50 62 50 92Z" fill="#6CB8FF" {OL}/><path d="M50 92 C50 62 90 62 90 92Z" fill="#F59BB8" {OL}/>'
        '<path d="M50 60 C44 54 38 60 44 66 L50 72 L56 66 C62 60 56 54 50 60Z" fill="#E8574A" {OL}/>'),
 "cyberbully": dict(words=["التنمر الإلكتروني", "العنف الإلكتروني", "الإيذاء", "التنمر", "الإساءة الإلكترونية"], anim="wobble", face=(40, 62, .4),
   body='<rect x="16" y="10" width="48" height="84" rx="8" fill="#3b3b5c" {OL}/><rect x="20" y="18" width="40" height="64" rx="3" fill="#BFE3F2"/><path d="M24 26 L52 26 L52 40 L32 40 L26 46 L28 40 L24 40Z" fill="#E8574A" {OL}/>'
        '<circle cx="78" cy="70" r="16" fill="#E8574A" {OL}/><path d="M70 70 L86 70" stroke="#fff" stroke-width="5" stroke-linecap="round"/>'),
 "report": dict(words=["الإبلاغ", "الإبلاغ عن المخالفات", "التبليغ"], anim="buzz", face=(36, 56, .42),
   body='<rect x="12" y="12" width="48" height="80" rx="8" fill="#6CC27A" {OL}/><rect x="18" y="20" width="36" height="56" rx="3" fill="#fff"/><path d="M36 30 L36 54" stroke="#E8574A" stroke-width="6" stroke-linecap="round"/><circle cx="36" cy="64" r="3.6" fill="#E8574A"/>'
        '<path d="M70 30 C78 36 78 48 70 54 M78 22 C90 32 90 52 78 62" fill="none" stroke="#3b2a1a" stroke-width="3" stroke-linecap="round"/>'),
 "block": dict(words=["الحظر", "حظر الحسابات", "حظر المتنمر"], anim="wobble", face=(36, 60, .4),
   body='<circle cx="36" cy="36" r="16" fill="#AEB8C4" {OL}/><path d="M8 92 C8 60 64 60 64 92Z" fill="#AEB8C4" {OL}/><circle cx="72" cy="66" r="22" fill="#fff" {OL}/>'
        '<circle cx="72" cy="66" r="18" fill="none" stroke="#E8574A" stroke-width="6"/><path d="M60 54 L84 78" stroke="#E8574A" stroke-width="6"/>'),
 "support": dict(words=["الدعم النفسي", "مد يد العون", "المساندة"], anim="bob", face=(50, 30, .38),
   body='<circle cx="50" cy="30" r="20" fill="#E8574A" {OL}/><path d="M6 70 C20 56 34 60 44 66 L66 66 C72 66 72 74 66 74 L48 74 L70 76 L88 64 C94 60 98 68 94 72 L74 90 L6 90Z" fill="#F7C9A4" {OL}/>'),
 "self_manage": dict(words=["إدارة الذات", "الذكاء العاطفي", "التعامل مع الضغوط", "إدارة الضغوط", "التعبير عن الذات", "فهم الذات"], anim="bob", face=(50, 56, .45),
   body='<path d="M50 92 C22 74 8 58 10 40 C12 24 32 18 50 34 C68 18 88 24 90 40 C92 58 78 74 50 92Z" fill="#F59BB8" {OL}/>'
        '<path d="M30 40 C30 30 44 28 46 36 C50 28 64 30 64 38 C70 40 70 50 62 50 L34 50 C26 50 26 42 30 40Z" fill="#fff" {OL}/>'),
 "initiative": dict(words=["المبادرة", "روح المبادرة", "المبادرة الذاتية", "المشاركة الصفية"], anim="bounce", face=(50, 74, .4),
   body='<path d="M36 94 L36 40 C36 34 44 34 44 40 L44 10 C44 4 54 4 54 10 L54 34 C54 28 62 28 62 34 L62 40 C62 34 70 34 70 40 L70 70 C70 84 62 94 50 94Z" fill="#F7C9A4" {OL}/>'
        '<path d="M20 20 L28 26 M80 20 L72 26 M14 40 L24 42 M86 40 L76 42" stroke="#F6B73C" stroke-width="4" stroke-linecap="round"/>'),
 "speech_mic": dict(words=["الإلقاء", "فن الإلقاء", "الخطابة", "التحدث أمام الجمهور", "العرض الشفهي"], anim="bob", face=(50, 30, .4),
   body='<rect x="36" y="6" width="28" height="46" rx="14" fill="#AEB8C4" {OL}/><path d="M36 22 L64 22 M36 32 L64 32" stroke="#8A93A6" stroke-width="2"/><path d="M28 40 C28 64 72 64 72 40" fill="none" stroke="#3b2a1a" stroke-width="4"/>'
        '<path d="M50 62 L50 86 M32 90 L68 90" stroke="#3b2a1a" stroke-width="5" stroke-linecap="round"/>'),
 "body_lang": dict(words=["لغة الجسد", "الإيماءات", "تعابير الوجه", "التواصل غير اللفظي"], anim="wiggle", face=(50, 30, .4),
   body='<circle cx="50" cy="30" r="22" fill="#FFD25A" {OL}/><path d="M8 70 L28 58 L36 70 M92 70 L72 58 L64 70" fill="none" stroke="#3b2a1a" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>'
        '<path d="M36 94 C36 64 64 64 64 94Z" fill="#6CB8FF" {OL}/><path d="M10 70 L4 64 M90 70 L96 64" stroke="#3b2a1a" stroke-width="3" stroke-linecap="round"/>'),
 "small_talk": dict(words=["الحديث", "المحادثة", "آداب الحديث", "فن الحديث"], anim="bob", face=(46, 40, .45),
   body='<path d="M10 14 L86 14 C90 14 92 16 92 20 L92 62 C92 66 90 68 86 68 L40 68 L22 86 L24 68 L16 68 C12 68 10 66 10 62Z" fill="#9CD86C" {OL}/>'
        '<circle cx="34" cy="42" r="4" fill="#3b2a1a"/><circle cx="52" cy="42" r="4" fill="#3b2a1a"/><circle cx="70" cy="42" r="4" fill="#3b2a1a"/>'),
 "id_badge": dict(words=["اسمي", "بطاقة الاسم", "التعريف بنفسي", "من أنا"], anim="bob", face=(32, 54, .4),
   body='<rect x="8" y="22" width="84" height="64" rx="8" fill="#fff" {OL}/><rect x="8" y="22" width="84" height="16" rx="8" fill="#6CB8FF" {OL}/><rect x="40" y="10" width="20" height="16" rx="4" fill="#AEB8C4" {OL}/>'
        '<circle cx="30" cy="58" r="12" fill="#FFD25A" {OL}/><path d="M50 52 L82 52 M50 64 L74 64" stroke="#3b2a1a" stroke-width="3" stroke-linecap="round"/>'),
 "birthday": dict(words=["عمري", "يوم الميلاد", "عيد الميلاد"], anim="bob", face=(50, 70, .45),
   body='<rect x="14" y="52" width="72" height="40" rx="6" fill="#F59BB8" {OL}/><path d="M14 64 C24 70 34 58 44 64 C54 70 64 58 74 64 C80 68 84 66 86 64" fill="none" stroke="#fff" stroke-width="4"/>'
        '<path d="M34 52 L34 30 M50 52 L50 26 M66 52 L66 30" stroke="#6CB8FF" stroke-width="5"/><path d="M34 22 C30 28 32 30 34 30 C36 30 38 28 34 22Z M50 18 C46 24 48 26 50 26 C52 26 54 24 50 18Z M66 22 C62 28 64 30 66 30 C68 30 70 28 66 22Z" fill="#FFD25A" {OL}/>'),
 "my_family": dict(words=["أسرتي", "عائلتي", "اجتماع عائلي"], anim="sway", face=(50, 70, .42),
   body='<path d="M10 50 L50 14 L90 50 L90 94 L10 94Z" fill="#F2D07A" {OL}/><path d="M4 54 L50 12 L96 54" fill="none" stroke="#E8574A" stroke-width="6" stroke-linecap="round"/>'
        '<path d="M50 54 C42 44 30 52 38 62 L50 74 L62 62 C70 52 58 44 50 54Z" fill="#E8574A" {OL}/>'),
}
ALIAS_ONLY = None
ALIASES = {}
