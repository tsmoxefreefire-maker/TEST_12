"""🆕 batch 43 · thinking and the scientist's ways (التفكير الناقد، والمنهج العلمي بالعلوم): the standards of thinking (clear, exact,
linked, deep, wide), the critical thinker, fair and open minds, the media and rumours, the reasoning (premises → conclusion,
general ↔ particular), evidence, the fallacies (the straw man!), the middle way; and the scientist's tools: the data, the variable
and the constant, the model, the fact and the opinion, the method and the experiment."""
F = "mind"
D = {
 # ---------- the standards of thinking ----------
 "clarity": dict(words=["الوضوح", "وضوح الفكرة", "الوضوح في التفكير"], anim="sun", face=(40, 44, .42),
   body='<circle cx="40" cy="40" r="30" fill="#E8F6FF" {OL}/><path d="M24 30 L36 30 M24 40 L52 40 M24 50 L46 50" stroke="#3b2a1a" stroke-width="3" stroke-linecap="round"/>'
        '<path d="M62 62 L92 92" stroke="#8B5E3C" stroke-width="10" stroke-linecap="round"/><path d="M22 20 C26 16 32 14 38 14" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round"/>'),
 "precision": dict(words=["الدقة", "الدقة في التفكير"], anim="wobble", face=(50, 50, .4), never=["math"],
   body='<circle cx="50" cy="50" r="44" fill="#fff" {OL}/><circle cx="50" cy="50" r="32" fill="#E8574A" {OL}/><circle cx="50" cy="50" r="20" fill="#fff" {OL}/><circle cx="50" cy="50" r="9" fill="#E8574A" {OL}/>'
        '<path d="M50 50 L90 10 M82 8 L92 8 L92 18" fill="none" stroke="#3b2a1a" stroke-width="4" stroke-linecap="round"/>'),
 "linking": dict(words=["الربط", "الترابط", "ربط الأفكار", "العلاقة بين الأفكار"], anim="wiggle", face=(50, 50, .38),
   body='<rect x="6" y="34" width="44" height="32" rx="16" fill="none" stroke="#6CB8FF" stroke-width="10"/><rect x="50" y="34" width="44" height="32" rx="16" fill="none" stroke="#F6B73C" stroke-width="10"/>'
        '<rect x="6" y="34" width="44" height="32" rx="16" fill="none" {OL}/><rect x="50" y="34" width="44" height="32" rx="16" fill="none" {OL}/>'),
 "depth": dict(words=["العمق", "التعمق", "التفكير العميق"], anim="drip", face=(50, 30, .38),
   body='<rect x="6" y="20" width="88" height="74" rx="6" fill="#7CC6F2" {OL}/><path d="M6 44 L94 44" stroke="#4A90D9" stroke-width="2"/><path d="M6 68 L94 68" stroke="#2F6DB5" stroke-width="2"/>'
        '<path d="M50 30 L50 84 M40 74 L50 86 L60 74" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>'),
 "breadth": dict(words=["الاتساع", "الشمول", "تعدد وجهات النظر", "النظرة الشاملة"], anim="sway", face=(50, 30, .38),
   body='<path d="M6 60 L94 60" stroke="#3b2a1a" stroke-width="5" stroke-linecap="round"/><path d="M16 50 L6 60 L16 70 M84 50 L94 60 L84 70" fill="none" stroke="#3b2a1a" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>'
        '<path d="M30 40 C30 20 70 20 70 40" fill="#9CD86C" {OL}/><path d="M20 80 L80 80" stroke="#6CB8FF" stroke-width="6" stroke-linecap="round"/>'),
 "critical_thinker": dict(words=["المفكر الناقد", "التفكير الناقد", "مهارات التفكير الناقد", "التفكير النقدي"], anim="bob", face=(42, 46, .45),
   body='<path d="M20 90 L20 70 C6 60 6 30 26 18 C42 8 66 12 72 30 L80 44 L72 48 L72 60 C72 68 64 70 58 68 L58 90Z" fill="#B0A8C9" {OL}/>'
        '<circle cx="74" cy="72" r="14" fill="#E8F6FF" {OL}/><path d="M84 82 L96 94" stroke="#8B5E3C" stroke-width="6" stroke-linecap="round"/><circle cx="40" cy="30" r="8" fill="#FFD25A" {OL}/><path d="M40 18 L40 22 M28 30 L32 30 M52 30 L48 30" stroke="#F6B73C" stroke-width="2.4"/>'),
 "objectivity": dict(words=["الموضوعية", "الحياد", "الإنصاف", "عدم التحيز"], anim="wobble", face=(50, 20, .34),
   body='<path d="M50 12 L50 88 M26 88 L74 88" stroke="#8B5E3C" stroke-width="5" stroke-linecap="round"/><path d="M12 32 L88 32" stroke="#8B5E3C" stroke-width="4"/>'
        '<path d="M12 32 L2 58 L22 58Z M88 32 L78 58 L98 58Z" fill="none" stroke="#3b2a1a" stroke-width="2"/><path d="M0 58 C2 68 22 68 24 58Z M76 58 C78 68 98 68 100 58Z" fill="#FFD25A" {OL}/>'),
 "open_mind": dict(words=["الانفتاح الذهني", "تقبل الآراء", "المرونة الفكرية", "تقبل الرأي الآخر"], anim="bob", face=(40, 62, .42),
   body='<path d="M16 92 L16 72 C2 60 4 34 22 22 L60 22 L72 36 L64 40 L64 60 C64 68 58 70 52 68 L52 92Z" fill="#F7C9A4" {OL}/>'
        '<path d="M22 22 C34 2 58 2 66 14" fill="none" stroke="#3b2a1a" stroke-width="3" stroke-dasharray="4 4"/><circle cx="80" cy="16" r="10" fill="#FFD25A" {OL}/><path d="M80 2 L80 0 M94 16 L98 16 M90 6 L93 3" stroke="#F6B73C" stroke-width="3"/>'),
 "media": dict(words=["الإعلام", "وسائل الإعلام", "الأخبار", "الإعلام الرقمي", "الصحافة"], anim="bob", face=(36, 60, .4),
   body='<rect x="6" y="16" width="64" height="74" rx="4" fill="#fff" {OL}/><rect x="12" y="24" width="52" height="14" fill="#3b3b5c"/><rect x="12" y="44" width="22" height="20" fill="#BFE3F2"/>'
        '<path d="M40 46 L64 46 M40 54 L64 54 M40 62 L58 62 M12 72 L64 72 M12 80 L56 80" stroke="#AEB8C4" stroke-width="2.6"/><rect x="74" y="34" width="22" height="18" rx="3" fill="#E8574A" {OL}/><path d="M80 34 L84 26 L90 34" fill="none" stroke="#3b2a1a" stroke-width="2"/>'),
 "rumour": dict(words=["الشائعات", "الشائعة", "الأخبار المزيفة", "التحقق من الأخبار", "نشر الشائعات"], anim="wiggle", face=(30, 44, .38),
   body='<path d="M6 20 L52 20 C56 20 58 22 58 26 L58 52 C58 56 56 58 52 58 L28 58 L16 70 L18 58 L12 58 C8 58 6 56 6 52Z" fill="#AEB8C4" {OL}/>'
        '<path d="M50 50 L88 50 C92 50 94 52 94 56 L94 78 C94 82 92 84 88 84 L84 84 L86 94 L74 84 L56 84 C52 84 50 82 50 78Z" fill="#E8574A" {OL}/><text direction="ltr" x="72" y="76" text-anchor="middle" font-size="24" font-weight="800" fill="#fff" font-family="sans-serif">؟</text>'),
 # ---------- reasoning ----------
 "syllogism": dict(words=["القضية الحملية", "المقدمة الكبرى", "المقدمة الصغرى", "القياس المنطقي", "الاستدلال", "المقدمات"], anim="bounce", face=(50, 82, .36),
   body='<rect x="10" y="6" width="80" height="20" rx="6" fill="#6CB8FF" {OL}/><rect x="20" y="34" width="60" height="20" rx="6" fill="#9CD86C" {OL}/>'
        '<path d="M50 58 L50 68 M44 64 L50 70 L56 64" fill="none" stroke="#3b2a1a" stroke-width="4" stroke-linecap="round"/><rect x="28" y="72" width="44" height="22" rx="6" fill="#FFD25A" {OL}/>'),
 "conclusion": dict(words=["النتيجة", "الاستنتاج", "الخلاصة", "الاستنتاجات"], anim="sun", face=(50, 70, .42), never=["math"],
   body='<path d="M8 8 L92 8 L58 46 L58 78 L42 88 L42 46Z" fill="#BFE3F2" {OL}/><circle cx="26" cy="20" r="4" fill="#6CB8FF"/><circle cx="50" cy="24" r="4" fill="#6CB8FF"/><circle cx="72" cy="18" r="4" fill="#6CB8FF"/>'
        '<circle cx="50" cy="94" r="6" fill="#FFD25A" {OL}/>'),
 "general_to_particular": dict(words=["من العام إلى الخاص", "الاستنباط", "التبرير الاستنتاجي"], anim="bounce", face=(50, 30, .38),
   body='<circle cx="50" cy="30" r="24" fill="#6CB8FF" {OL}/><circle cx="40" cy="24" r="3" fill="#fff"/><circle cx="58" cy="22" r="3" fill="#fff"/><circle cx="48" cy="38" r="3" fill="#fff"/><circle cx="62" cy="36" r="3" fill="#fff"/>'
        '<path d="M50 58 L50 76 M42 70 L50 78 L58 70" fill="none" stroke="#3b2a1a" stroke-width="4" stroke-linecap="round"/><circle cx="50" cy="88" r="7" fill="#FFD25A" {OL}/>'),
 "particular_to_general": dict(words=["من الخاص إلى العام", "الاستقراء", "التبرير الاستقرائي", "التعميم"], anim="bounce", face=(50, 74, .38),
   body='<circle cx="24" cy="14" r="7" fill="#FFD25A" {OL}/><circle cx="50" cy="12" r="7" fill="#FFD25A" {OL}/><circle cx="76" cy="14" r="7" fill="#FFD25A" {OL}/>'
        '<path d="M50 26 L50 42 M42 36 L50 44 L58 36" fill="none" stroke="#3b2a1a" stroke-width="4" stroke-linecap="round"/><circle cx="50" cy="72" r="24" fill="#6CB8FF" {OL}/>'),
 "evidence": dict(words=["الدليل", "الشواهد", "الحجاج", "الحجة", "البرهان", "دليل"], anim="wobble", face=(30, 60, .38), never=["math"],
   body='<rect x="6" y="14" width="56" height="76" rx="4" fill="#fff" {OL}/><path d="M14 30 L54 30 M14 42 L54 42 M14 54 L40 54" stroke="#AEB8C4" stroke-width="3"/>'
        '<circle cx="66" cy="60" r="18" fill="#E8F6FF" {OL}/><path d="M78 74 L94 92" stroke="#8B5E3C" stroke-width="7" stroke-linecap="round"/><path d="M58 60 L64 66 L74 54" fill="none" stroke="#6CC27A" stroke-width="4" stroke-linecap="round"/>'),
 "solo_work": dict(words=["العمل الفردي", "التعلم الذاتي", "الاعتماد على النفس"], anim="bob", face=(50, 30, .38),
   body='<circle cx="50" cy="28" r="16" fill="#FFD25A" {OL}/><path d="M24 74 C24 50 76 50 76 74Z" fill="#6CB8FF" {OL}/><path d="M6 74 L94 74" stroke="#C98A55" stroke-width="8" stroke-linecap="round"/>'
        '<path d="M16 74 L16 94 M84 74 L84 94" stroke="#8B5E3C" stroke-width="5"/><rect x="40" y="62" width="22" height="12" fill="#fff" {OL}/>'),
 "middle_way": dict(words=["الوسطية", "الاعتدال"], anim="wobble", face=(50, 40, .4),
   body='<path d="M4 80 L96 80" stroke="#3b2a1a" stroke-width="5" stroke-linecap="round"/><path d="M50 80 L36 94 L64 94Z" fill="#C98A55" {OL}/>'
        '<circle cx="50" cy="44" r="22" fill="#6CC27A" {OL}/><path d="M8 72 L8 88 M92 72 L92 88" stroke="#E8574A" stroke-width="5" stroke-linecap="round"/>'),
 "extremism": dict(words=["الفكر الضال", "التطرف", "الغلو"], anim="wobble", face=(30, 34, .36),
   body='<path d="M4 50 L62 50 L62 96 L4 96Z" fill="#9C8C7A" {OL}/><path d="M10 40 C20 30 40 30 54 40" fill="none" stroke="#3b2a1a" stroke-width="4" stroke-dasharray="5 4"/>'
        '<path d="M54 40 L66 52" stroke="#3b2a1a" stroke-width="4"/><path d="M74 20 L96 60 L52 60Z" fill="#FFD25A" {OL}/><path d="M74 32 L74 46" stroke="#3b2a1a" stroke-width="5" stroke-linecap="round"/><circle cx="74" cy="53" r="2.6" fill="#3b2a1a"/>'),
 "strawman": dict(words=["مغالطة رجل القش", "رجل القش", "المغالطات المنطقية", "المغالطة"], anim="sway", face=(50, 26, .42),
   body='<path d="M50 40 L50 94 M18 50 L82 50" stroke="#8B5E3C" stroke-width="5" stroke-linecap="round"/><circle cx="50" cy="26" r="16" fill="#F2D07A" {OL}/><path d="M30 14 L70 14 L62 4 L38 4Z" fill="#C98A55" {OL}/>'
        '<path d="M36 46 L64 46 L60 76 L40 76Z" fill="#6CB8FF" {OL}/><path d="M18 50 L10 44 M18 50 L10 56 M82 50 L90 44 M82 50 L90 56 M40 76 L36 84 M60 76 L64 84" stroke="#E6B83A" stroke-width="3" stroke-linecap="round"/>'),
 "ad_hominem": dict(words=["مغالطة الشخصنة", "الشخصنة", "مهاجمة الشخص"], anim="wobble", face=(76, 40, .38),
   body='<path d="M4 54 L40 54 L40 44 L56 44 C60 44 60 52 56 52 L50 52 L62 54 C66 54 66 62 62 62 L40 62 L40 66 L4 66Z" fill="#F7C9A4" {OL}/>'
        '<circle cx="76" cy="40" r="18" fill="#AEB8C4" {OL}/><path d="M58 92 C58 66 94 66 94 92Z" fill="#AEB8C4" {OL}/><path d="M60 20 L66 26 M92 20 L86 26" stroke="#E8574A" stroke-width="3"/>'),
 # ---------- the scientist's tools ----------
 "data": dict(words=["البيانات", "جمع البيانات", "تنظيم البيانات", "تمثيل البيانات", "الجداول والبيانات"], anim="bounce", face=(50, 24, .34), never=["digital"],
   body='<rect x="6" y="40" width="88" height="54" rx="4" fill="#fff" {OL}/><path d="M6 54 L94 54 M6 68 L94 68 M6 82 L94 82 M36 40 L36 94 M66 40 L66 94" stroke="#AEB8C4" stroke-width="2"/>'
        '<rect x="6" y="40" width="88" height="14" fill="#6CB8FF" {OL}/><rect x="18" y="6" width="12" height="26" fill="#6CC27A" {OL}/><rect x="44" y="14" width="12" height="18" fill="#F6B73C" {OL}/><rect x="70" y="2" width="12" height="30" fill="#E8574A" {OL}/>'),
 "evaluate_info": dict(words=["تقويم البيانات", "تقويم المعلومات", "التحقق من المعلومات", "مصادر المعلومات الموثوقة", "تقييم المصادر"], anim="wobble", face=(30, 56, .38),
   body='<rect x="6" y="10" width="54" height="80" rx="4" fill="#fff" {OL}/><path d="M14 28 L20 34 L30 22 M14 50 L20 56 L30 44" fill="none" stroke="#6CC27A" stroke-width="4" stroke-linecap="round"/>'
        '<path d="M14 66 L28 80 M28 66 L14 80" stroke="#E8574A" stroke-width="4" stroke-linecap="round"/><circle cx="70" cy="56" r="17" fill="#E8F6FF" {OL}/><path d="M82 70 L96 88" stroke="#8B5E3C" stroke-width="7" stroke-linecap="round"/>'),
 "fact_opinion": dict(words=["الرأي والحقيقة", "الحقيقة والرأي", "الحقيقة العلمية", "الحقائق والآراء"], anim="bounce", face=(28, 44, .36),
   body='<rect x="4" y="16" width="46" height="56" rx="6" fill="#6CC27A" {OL}/><path d="M14 44 L24 54 L40 32" fill="none" stroke="#fff" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>'
        '<path d="M56 30 C56 18 94 18 94 34 C94 48 76 50 70 48 L60 58 L62 46 C58 42 56 38 56 30Z" fill="#FFD25A" {OL}/><path d="M64 34 L86 34" stroke="#3b2a1a" stroke-width="3" stroke-linecap="round"/>'),
 "sci_method": dict(words=["المنهج العلمي", "المنهج التجريبي", "خطوات المنهج العلمي", "البحث العلمي", "التفسير العلمي", "الطريقة العلمية"], anim="bob", face=(50, 66, .4),
   body='<path d="M40 8 L60 8 M44 8 L44 36 L20 84 C16 92 22 96 30 96 L70 96 C78 96 84 92 80 84 L56 36 L56 8" fill="#E8F6FF" {OL}/><path d="M28 70 L72 70 L80 84 C84 92 78 96 70 96 L30 96 C22 96 16 92 20 84Z" fill="#9CD86C"/>'
        '<path d="M44 36 L20 84 C16 92 22 96 30 96 L70 96 C78 96 84 92 80 84 L56 36" fill="none" {OL}/><circle cx="84" cy="22" r="6" fill="#FFD25A" {OL}/><path d="M70 22 L76 22 M92 22 L98 22" stroke="#3b2a1a" stroke-width="2"/>'),
 "experiment": dict(words=["التجربة", "التجربة العلمية", "إجراء التجارب", "التجارب العملية"], anim="wobble", face=(30, 70, .38), never=["math", "english"],
   body='<rect x="8" y="30" width="16" height="64" rx="8" fill="#E8F6FF" {OL}/><rect x="8" y="64" width="16" height="30" rx="8" fill="#E8574A"/><rect x="8" y="30" width="16" height="64" rx="8" fill="none" {OL}/>'
        '<rect x="32" y="40" width="16" height="54" rx="8" fill="#E8F6FF" {OL}/><rect x="32" y="70" width="16" height="24" rx="8" fill="#6CB8FF"/><path d="M4 94 L96 94" stroke="#8B5E3C" stroke-width="5"/>'
        '<path d="M66 40 L56 94 L96 94 L86 40Z" fill="#9CD86C" {OL}/><path d="M64 40 L88 40" stroke="#3b2a1a" stroke-width="4"/><circle cx="72" cy="26" r="4" fill="#9CD86C" {OL}/><circle cx="80" cy="14" r="3" fill="#9CD86C" {OL}/>'),
 "hypothesis2": dict(words=["الفرضية", "وضع الفرضيات", "الفرض العلمي"], anim="bob", face=(40, 50, .42), never=["math"],
   body='<path d="M10 40 C10 16 70 10 74 34 C88 34 92 56 76 60 C72 76 30 78 26 64 C8 64 4 46 10 40Z" fill="#fff" {OL}/>'
        '<text direction="ltr" x="46" y="58" text-anchor="middle" font-size="34" font-weight="800" fill="#6CB8FF" font-family="sans-serif">؟</text><circle cx="20" cy="82" r="6" fill="#fff" {OL}/><circle cx="10" cy="94" r="3.6" fill="#fff" {OL}/>'),
 "variable": dict(words=["المتغير", "المتغير المستقل", "المتغير التابع", "المتغيرات"], anim="sway", face=(50, 76, .38), only=["science", "digital", "thinking"],
   body='<rect x="8" y="34" width="84" height="12" rx="6" fill="#C9D2DC" {OL}/><rect x="8" y="34" width="54" height="12" rx="6" fill="#6CB8FF" {OL}/><circle cx="62" cy="40" r="12" fill="#fff" {OL}/>'
        '<path d="M30 20 L18 20 M24 14 L18 20 L24 26 M70 20 L82 20 M76 14 L82 20 L76 26" fill="none" stroke="#3b2a1a" stroke-width="3" stroke-linecap="round"/><rect x="26" y="58" width="48" height="36" rx="8" fill="#F6B73C" {OL}/>'),
 "constant": dict(words=["المتغير الثابت", "العوامل الثابتة"], anim="wobble", face=(50, 70, .4), only=["science", "thinking"],
   body='<rect x="20" y="44" width="60" height="50" rx="8" fill="#AEB8C4" {OL}/><path d="M32 44 L32 30 C32 10 68 10 68 30 L68 44" fill="none" stroke="#3b2a1a" stroke-width="7"/><circle cx="50" cy="64" r="6" fill="#3b2a1a"/>'),
 "phys_model": dict(words=["النموذج المادي", "النماذج العلمية", "النموذج العلمي", "المجسم"], anim="sun", face=(50, 50, .4),
   body='<circle cx="50" cy="44" r="34" fill="#6CB8FF" {OL}/><path d="M26 30 C34 22 46 30 42 42 C38 50 26 46 26 30Z M58 50 C66 44 78 52 72 62 C66 70 56 64 58 50Z" fill="#6CC27A" {OL}/>'
        '<path d="M50 78 L50 90 M30 94 L70 94" stroke="#8B5E3C" stroke-width="5" stroke-linecap="round"/>'),
 "idea_model": dict(words=["النموذج الفكري", "النموذج الذهني", "الخريطة الذهنية", "التخيل"], anim="bob", face=(44, 44, .42),
   body='<path d="M12 44 C8 22 30 10 46 18 C58 4 86 12 84 32 C98 40 94 64 76 64 C70 78 44 78 38 66 C18 70 6 58 12 44Z" fill="#B0A8C9" {OL}/>'
        '<circle cx="34" cy="40" r="5" fill="#fff" {OL}/><circle cx="64" cy="34" r="5" fill="#fff" {OL}/><circle cx="58" cy="56" r="5" fill="#fff" {OL}/><path d="M34 40 L64 34 L58 56Z" fill="none" stroke="#fff" stroke-width="2"/>'
        '<circle cx="24" cy="84" r="6" fill="#B0A8C9" {OL}/><circle cx="12" cy="94" r="3.4" fill="#B0A8C9" {OL}/>'),
 "sci_ethics": dict(words=["أخلاقيات العلم", "أخلاقيات البحث العلمي", "الأمانة العلمية"], anim="bob", face=(36, 70, .38),
   body='<path d="M28 8 L44 8 M32 8 L32 34 L12 76 C8 84 14 90 22 90 L50 90 C58 90 64 84 60 76 L40 34 L40 8" fill="#E8F6FF" {OL}/>'
        '<path d="M74 70 C60 60 54 50 58 42 C62 34 70 36 74 44 C78 36 86 34 90 42 C94 50 88 60 74 70Z" fill="#E8574A" {OL}/>'),
 "ai_brain": dict(words=["الذكاء الاصطناعي", "تطبيقات الذكاء الاصطناعي", "الآلة الذكية", "تعلم الآلة"], anim="buzz", face=(50, 56, .42),
   body='<rect x="16" y="20" width="68" height="60" rx="14" fill="#AEB8C4" {OL}/><path d="M50 20 L50 6" stroke="#3b2a1a" stroke-width="4"/><circle cx="50" cy="6" r="5" fill="#E8574A" {OL}/>'
        '<path d="M16 46 L4 46 M84 46 L96 46 M16 60 L6 60 M84 60 L94 60" stroke="#3b2a1a" stroke-width="3"/><path d="M28 32 L40 32 L40 26 M72 32 L60 32 L60 26" fill="none" stroke="#6CB8FF" stroke-width="3"/>'),
 "scale_drawing": dict(words=["مقياس الرسم"], anim="bob", face=(50, 40, .42), only=["science", "math"],
   body='<rect x="8" y="12" width="84" height="56" rx="4" fill="#F7E9C8" {OL}/><path d="M20 50 C30 30 46 54 58 34 C64 26 74 30 80 38" fill="none" stroke="#8B5E3C" stroke-width="3"/>'
        '<rect x="14" y="78" width="24" height="10" fill="#3b2a1a"/><rect x="38" y="78" width="24" height="10" fill="#fff" {OL}/><rect x="62" y="78" width="24" height="10" fill="#3b2a1a"/>'),
}
ALIAS_ONLY = None
ALIASES = {"متغيرة درجة الحرارة": ("🌡️", ("science",)), "الحيوانات متغيرة درجة الحرارة": ("🐾", ("science",)), "العينة الضابطة": ("mind.constant", ("science",)), }
