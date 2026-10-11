"""🆕 batch 40 · the human body and health: the organs and systems, health and disease, food and nutrition (science, biology, life skills, English)."""
F = "body"
D = {
 # ---------- organs and systems ----------
 "lungs": dict(words=["الرئتان", "الرئة", "رئة", "الرئتين", "الجهاز التنفسي", "التنفس", "جهاز التنفس", "الشهيق والزفير", "القصبة الهوائية"], anim="bob", face=(50, 66, .5),
   body='<path d="M50 6 L50 34 M50 34 L40 44 M50 34 L60 44" stroke="#C0392B" stroke-width="5" stroke-linecap="round" fill="none"/>'
        '<path d="M44 40 C30 30 12 44 12 70 C12 88 24 94 36 90 C44 88 46 80 46 70Z" fill="#F28AA8" {OL}/><path d="M56 40 C70 30 88 44 88 70 C88 88 76 94 64 90 C56 88 54 80 54 70Z" fill="#F28AA8" {OL}/>'),
 "stomach": dict(words=["المعدة", "معدة", "الجهاز الهضمي", "الهضم", "جهاز الهضم", "الأمعاء", "الأمعاء الدقيقة", "الأمعاء الغليظة", "المريء"], anim="wobble", face=(50, 58, .6),
   body='<path d="M30 6 L34 24 C20 30 14 52 22 70 C32 92 66 96 80 76 C90 60 82 44 68 46 C58 48 56 58 48 52 C42 46 46 30 44 18 L42 6Z" fill="#F8A5A5" {OL}/><path d="M80 76 C84 84 80 92 72 94" fill="none" stroke="#3b2a1a" stroke-width="3"/>'),
 "brain": dict(words=["الدماغ", "دماغ", "المخ", "الجهاز العصبي", "الأعصاب", "الخلية العصبية", "الحبل الشوكي", "النخاع الشوكي", "التفكير", "مستويات التفكير"], anim="wobble", face=(50, 58, .66),
   body='<path d="M50 14 C34 4 14 14 14 34 C4 42 6 64 18 70 C22 86 40 90 50 82 C60 90 78 86 82 70 C94 64 96 42 86 34 C86 14 66 4 50 14Z" fill="#F7B5C4" {OL}/>'
        '<path d="M50 16 L50 80 M28 30 Q36 36 30 44 M70 30 Q62 36 70 44 M22 52 Q32 56 26 64 M78 52 Q68 56 74 64" fill="none" stroke="#D97A93" stroke-width="2.6" stroke-linecap="round"/>'),
 "skeleton": dict(words=["الهيكل العظمي", "العظام", "عظم", "الجهاز الهيكلي", "الجمجمة", "المفاصل", "المفصل"], anim="wobble", face=(50, 22, .5),
   body='<circle cx="50" cy="20" r="15" fill="#F5EEDC" {OL}/><path d="M50 36 L50 70 M34 44 L66 44 M36 52 L64 52 M38 60 L62 60 M50 46 L28 62 M50 46 L72 62 M50 70 L38 94 M50 70 L62 94" stroke="#F5EEDC" stroke-width="7" stroke-linecap="round"/>'
        '<path d="M50 36 L50 70 M34 44 L66 44 M36 52 L64 52 M38 60 L62 60 M50 46 L28 62 M50 46 L72 62 M50 70 L38 94 M50 70 L62 94" stroke="#3b2a1a" stroke-width="1.6" stroke-linecap="round" fill="none"/>'),
 "muscle": dict(words=["العضلات", "عضلة", "الجهاز العضلي", "العضلة", "اللياقة البدنية", "القوة العضلية"], anim="bounce", face=(46, 52, .6),
   body='<path d="M10 70 L30 70 C34 50 40 30 54 24 C66 18 74 24 72 34 C70 40 62 40 58 36 C52 44 50 52 52 60 C66 50 88 52 90 70 C90 84 70 90 52 86 L10 86Z" fill="#F2B880" {OL}/><path d="M60 62 C66 58 74 60 76 66" fill="none" stroke="#C98A55" stroke-width="2.6"/>'),
 "blood": dict(words=["الدم", "دم", "خلايا الدم", "خلايا الدم الحمراء", "الصفائح الدموية", "البلازما", "فصائل الدم", "الأوعية الدموية", "الشرايين", "الأوردة", "الشعيرات الدموية", "جهاز الدوران", "الدورة الدموية", "ضغط الدم"], anim="drip", face=(50, 66, .9),
   body='<path d="M50 6 C50 6 20 44 20 64 C20 82 34 94 50 94 C66 94 80 82 80 64 C80 44 50 6 50 6Z" fill="#E74C3C" {OL}/><path d="M34 52 C30 60 30 66 33 72" stroke="#fff" stroke-width="4" fill="none" stroke-linecap="round" opacity=".7"/>'),
 "kidney": dict(words=["الكلية", "الكليتان", "الجهاز البولي", "الإخراج", "جهاز الإخراج", "الجهاز الإخراجي"], anim="wobble", face=(42, 50, .62),
   body='<path d="M60 14 C82 14 92 36 88 56 C84 80 64 92 46 86 C26 80 12 60 18 40 C24 20 40 14 52 18 C48 26 50 34 58 36 C64 38 66 30 60 14Z" fill="#B5563E" {OL}/><path d="M60 36 C70 44 72 54 64 62" fill="none" stroke="#3b2a1a" stroke-width="2.6"/>'),
 "eye": dict(words=["العين", "العينان", "العيون", "البصر", "حاسة البصر", "عين"], anim="bob", face=None,
   body='<path d="M6 50 C26 20 74 20 94 50 C74 80 26 80 6 50Z" fill="#fff" {OL}/><circle cx="50" cy="50" r="18" fill="#5DA9E9" {OL}/><circle cx="50" cy="50" r="9" fill="#2B1D12"/><circle cx="55" cy="45" r="4" fill="#fff"/>'
        '<path d="M22 28 L16 20 M38 22 L36 12 M62 22 L64 12 M78 28 L84 20" stroke="#3b2a1a" stroke-width="3" stroke-linecap="round"/>'),
 "ear": dict(words=["الأذن", "الأذنان", "أذن", "السمع", "حاسة السمع"], anim="wobble", face=(56, 58, .5),
   body='<path d="M30 40 C30 14 76 8 78 40 C80 58 66 62 62 74 C58 88 44 94 36 84 C30 78 34 70 40 70" fill="#F2C9A0" {OL}/><path d="M44 40 C44 28 64 26 64 40 C64 50 54 50 52 58" fill="none" stroke="#C98A55" stroke-width="3" stroke-linecap="round"/>'),
 "nose": dict(words=["الأنف", "أنف", "الشم", "حاسة الشم"], anim="wobble", face=(50, 40, .55),
   body='<path d="M44 10 C46 30 30 56 26 70 C22 86 40 92 50 86 C60 92 78 86 74 70 C70 56 54 30 56 10Z" fill="#F2C9A0" {OL}/><ellipse cx="40" cy="78" rx="5" ry="3.5" fill="#B07A4A"/><ellipse cx="60" cy="78" rx="5" ry="3.5" fill="#B07A4A"/>'),
 "tongue": dict(words=["اللسان", "التذوق", "حاسة التذوق", "الفم"], anim="wobble", face=(50, 36, .6),
   body='<path d="M10 40 C30 20 70 20 90 40 C80 70 20 70 10 40Z" fill="#E8574A" {OL}/><path d="M32 44 C30 70 40 90 50 90 C60 90 70 70 68 44Z" fill="#F48FB1" {OL}/><path d="M50 50 L50 74" stroke="#D2627F" stroke-width="2.6"/>'),
 "hand": dict(words=["اليد", "اليدان", "الأصابع", "اللمس", "حاسة اللمس", "الجلد", "يد", "الذراعان", "الذراع"], anim="wiggle", face=(50, 70, .55),
   body='<path d="M28 92 L26 56 C24 48 14 40 18 34 C22 30 28 36 32 44 L32 18 C32 12 40 12 40 18 L40 40 L42 12 C42 6 50 6 50 12 L50 40 L52 16 C52 10 60 10 60 16 L60 42 L62 26 C62 20 70 20 70 26 L70 62 C70 78 64 86 64 92Z" fill="#F2C9A0" {OL}/>'),
 "senses": dict(words=["الحواس", "الحواس الخمس", "أعضاء الحس"], anim="bob", face=(50, 56, .7),
   body='<circle cx="50" cy="54" r="38" fill="#F2C9A0" {OL}/><path d="M12 54 C2 50 4 64 12 64 M88 54 C98 50 96 64 88 64" fill="#F2C9A0" {OL}/><path d="M24 22 C36 10 64 10 76 22" fill="none" stroke="#6B4F3A" stroke-width="7" stroke-linecap="round"/>'),
 "tooth": dict(words=["الأسنان", "السن", "سن", "الضرس", "تسوس الأسنان", "صحة الفم والأسنان", "طبيب الأسنان", "ألم الأسنان"], anim="bounce", face=(50, 42, .66),
   body='<path d="M22 22 C22 6 40 8 50 14 C60 8 78 6 78 22 C78 40 72 50 70 64 C68 80 64 92 58 92 C52 92 54 72 50 72 C46 72 48 92 42 92 C36 92 32 80 30 64 C28 50 22 40 22 22Z" fill="#fff" {OL}/>'),
 "liver": dict(words=["الكبد", "البنكرياس", "الغدد", "الجهاز الهرموني", "الغدد الصماء", "الهرمونات"], anim="wobble", face=(44, 50, .6),
   body='<path d="M8 40 C10 22 40 16 70 20 C90 22 96 34 88 44 C78 58 60 76 40 80 C20 84 6 64 8 40Z" fill="#A0522D" {OL}/><path d="M60 22 C58 40 60 56 66 64" fill="none" stroke="#7A3A1E" stroke-width="2.6"/>'),
 "baby": dict(words=["التكاثر", "النمو والتكاثر", "الرضيع", "الطفل الرضيع", "مراحل النمو", "النمو"], anim="bob", face=(50, 44, .66), never=["math", "finance", "social"],
   body='<path d="M20 92 C20 66 36 60 50 60 C64 60 80 66 80 92Z" fill="#B9E3F7" {OL}/><circle cx="50" cy="40" r="26" fill="#F7D3B5" {OL}/><path d="M50 14 C46 8 52 4 56 8" fill="none" stroke="#6B4F3A" stroke-width="3" stroke-linecap="round"/>'),
 "dna2": dict(words=["الوراثة", "علم الوراثة", "الصفات الوراثية", "الصفات المكتسبة", "انتقال الصفات"], anim="sway", face=(50, 50, .5),
   body='<path d="M30 6 C70 24 70 36 30 50 C70 64 70 76 30 94 M70 6 C30 24 30 36 70 50 C30 64 30 76 70 94" fill="none" stroke="#6CB8FF" stroke-width="6" stroke-linecap="round"/>'
        '<path d="M40 14 L60 14 M46 30 L54 30 M40 86 L60 86 M46 70 L54 70" stroke="#F59BB8" stroke-width="5" stroke-linecap="round"/><circle cx="50" cy="50" r="13" fill="#FFD25A" {OL}/>'),
 "cellsdivide": dict(words=["الانقسام المتساوي", "الانقسام المنصف", "انقسام الخلية", "الانقسام الخلوي", "التكاثر الخلوي", "دورة الخلية"], anim="wobble", face=(30, 50, .5),
   body='<circle cx="30" cy="50" r="24" fill="#F8C9C1" {OL}/><circle cx="72" cy="50" r="24" fill="#F8C9C1" {OL}/><circle cx="36" cy="40" r="6" fill="#9C6FD6"/><circle cx="72" cy="58" r="6" fill="#9C6FD6"/><path d="M52 34 L50 66" stroke="#3b2a1a" stroke-width="2" stroke-dasharray="4 4"/>'),
 # ---------- health and disease ----------
 "germ": dict(words=["العدوى", "انتقال العدوى", "الأمراض المعدية", "المرض المعدي", "مسببات المرض", "الكوليرا", "الإنفلونزا"], anim="wiggle", face=(50, 52, .7),
   body='<path d="M50 14 L54 4 M78 26 L88 18 M88 54 L98 56 M74 82 L82 92 M40 86 L36 96 M14 68 L4 72 M14 34 L6 26" stroke="#3b2a1a" stroke-width="3" stroke-linecap="round"/>'
        '<path d="M50 14 C66 14 78 22 82 34 C90 46 90 62 80 74 C70 86 54 90 40 86 C24 82 12 70 12 52 C12 32 30 14 50 14Z" fill="#9CD86C" {OL}/><circle cx="34" cy="70" r="4" fill="#6FAE4A"/><circle cx="70" cy="34" r="3.4" fill="#6FAE4A"/>'),
 "sick": dict(words=["المرض", "الأمراض", "أسباب المرض", "الأمراض غير المعدية", "الحمى", "مريض", "الأعراض"], anim="wobble", face=(50, 56, .7),
   body='<circle cx="50" cy="56" r="36" fill="#C8E6A0" {OL}/><path d="M60 82 L84 58" stroke="#fff" stroke-width="10" stroke-linecap="round"/><path d="M60 82 L84 58" stroke="#E8574A" stroke-width="5" stroke-linecap="round"/>'
        '<rect x="22" y="12" width="56" height="14" rx="7" fill="#7CC6F2" {OL}/>'),
 "vaccine": dict(words=["التطعيم", "اللقاحات", "التحصين", "المناعة الاصطناعية"], anim="bob", face=(40, 52, .5),
   body='<path d="M70 14 L86 30 M78 22 L64 36" stroke="#3b2a1a" stroke-width="4" stroke-linecap="round"/><rect x="18" y="34" width="54" height="26" rx="6" transform="rotate(45 45 47)" fill="#E3F2FD" {OL}/>'
        '<path d="M20 80 L8 92" stroke="#3b2a1a" stroke-width="3" stroke-linecap="round"/><rect x="30" y="40" width="26" height="12" transform="rotate(45 45 47)" fill="#7CC6F2"/>'),
 "immune": dict(words=["جهاز المناعة", "المناعة", "المناعة الطبيعية", "الأجسام المضادة", "الجهاز المناعي", "خلايا الدم البيضاء"], anim="bounce", face=(50, 50, .66),
   body='<path d="M50 6 L86 18 L84 52 C82 74 66 88 50 94 C34 88 18 74 16 52 L14 18Z" fill="#7CC6F2" {OL}/><path d="M50 30 L50 70 M30 50 L70 50" stroke="#fff" stroke-width="9" stroke-linecap="round" opacity=".55"/>'),
 "medicine": dict(words=["الدواء", "الأدوية", "العلاج", "الصيدلية", "الأقراص"], anim="wobble", face=(50, 50, .62),
   body='<rect x="16" y="30" width="68" height="40" rx="20" transform="rotate(-30 50 50)" fill="#fff" {OL}/><path d="M50 30 L50 70" transform="rotate(-30 50 50)" stroke="#3b2a1a" stroke-width="2.6"/>'
        '<path d="M50 30 L66 30 C77 30 84 39 84 50 C84 61 77 70 66 70 L50 70Z" transform="rotate(-30 50 50)" fill="#E8574A" {OL}/>'),
 "firstaid": dict(words=["الإسعافات الأولية", "الإسعاف", "حقيبة الإسعافات", "الإسعافات"], anim="bob", face=(50, 70, .5),
   body='<rect x="10" y="26" width="80" height="62" rx="10" fill="#fff" {OL}/><path d="M36 26 L36 16 C36 12 64 12 64 16 L64 26" fill="none" stroke="#3b2a1a" stroke-width="3"/><path d="M42 36 L58 36 L58 46 L68 46 L68 60 L58 60 L58 70 L42 70 L42 60 L32 60 L32 46 L42 46Z" fill="#E74C3C" {OL}/>'),
 "hygiene": dict(words=["النظافة الشخصية", "النظافة", "غسل اليدين", "الصابون", "العادات الصحية", "الاستحمام"], anim="wobble", face=(50, 62, .6),
   body='<circle cx="22" cy="24" r="9" fill="#E3F2FD" {OL}/><circle cx="74" cy="16" r="7" fill="#E3F2FD" {OL}/><circle cx="84" cy="34" r="5" fill="#E3F2FD" {OL}/><rect x="14" y="44" width="72" height="44" rx="18" fill="#F59BB8" {OL}/><path d="M28 56 C36 52 48 54 54 58" stroke="#fff" stroke-width="4" fill="none" stroke-linecap="round" opacity=".7"/>'),
 "toothbrush": dict(words=["فرشاة الأسنان", "تفريش الأسنان", "تنظيف الأسنان", "معجون الأسنان", "المسواك"], anim="wiggle", face=(56, 66, .5),
   body='<rect x="8" y="58" width="84" height="16" rx="8" fill="#6CB8FF" {OL}/><rect x="10" y="34" width="30" height="24" rx="4" fill="#fff" {OL}/><path d="M16 34 L16 26 M22 34 L22 24 M28 34 L28 26 M34 34 L34 24" stroke="#7CC6F2" stroke-width="4" stroke-linecap="round"/>'),
 "sleep": dict(words=["النوم", "الراحة", "النوم الكافي", "ساعات النوم"], anim="bob", face=(46, 62, .6),
   body='<path d="M60 10 C40 14 24 32 24 54 C24 78 44 94 66 92 C80 92 90 84 94 76 C84 80 70 80 58 72 C42 62 40 30 60 10Z" fill="#FFD25A" {OL}/><text x="70" y="34" font-size="16" font-weight="800" fill="#7A6AC8" font-family="sans-serif">Z</text><text x="82" y="22" font-size="11" font-weight="800" fill="#7A6AC8" font-family="sans-serif">z</text>'),
 "exercise": dict(words=["الرياضة", "التمارين الرياضية", "التمارين", "النشاط البدني", "ممارسة الرياضة", "الرياضة البدنية"], anim="bounce", face=(50, 50, .5),
   body='<rect x="6" y="36" width="12" height="28" rx="4" fill="#5A6B7B" {OL}/><rect x="82" y="36" width="12" height="28" rx="4" fill="#5A6B7B" {OL}/><rect x="18" y="44" width="64" height="12" rx="5" fill="#AEB8C4" {OL}/><rect x="0" y="42" width="6" height="16" rx="2" fill="#5A6B7B"/><rect x="94" y="42" width="6" height="16" rx="2" fill="#5A6B7B"/>'),
 "thermometer": dict(words=["مقياس الحرارة", "ميزان الحرارة", "قياس الحرارة", "درجة حرارة الجسم", "العلامات الحيوية"], anim="bob", face=(50, 44, .5),
   body='<rect x="38" y="6" width="24" height="66" rx="12" fill="#fff" {OL}/><circle cx="50" cy="80" r="16" fill="#E74C3C" {OL}/><rect x="46" y="30" width="8" height="46" fill="#E74C3C"/><path d="M62 20 L56 20 M62 32 L56 32 M62 44 L56 44" stroke="#3b2a1a" stroke-width="2"/>'),
 "diabetes": dict(words=["داء السكري", "السكري", "الأنسولين", "سكر الدم", "السمنة"], anim="bob", face=(50, 68, .55),
   body='<rect x="20" y="10" width="60" height="80" rx="14" fill="#AEB8C4" {OL}/><rect x="28" y="18" width="44" height="30" rx="6" fill="#C8F0D8" {OL}/><text x="50" y="40" text-anchor="middle" font-size="16" font-weight="800" fill="#2E7D3A" font-family="sans-serif">120</text><path d="M50 90 L50 98" stroke="#E74C3C" stroke-width="4" stroke-linecap="round"/>'),
 # ---------- food and nutrition ----------
 "plate": dict(words=["الغذاء المتوازن", "الوجبة المتوازنة", "التغذية", "التغذية السليمة", "الهرم الغذائي", "الغذاء الصحي", "طعام صحي", "الوجبات الصحية", "العناصر الغذائية", "الغذاء", "الطعام"], anim="bob", face=(50, 52, .55),
   body='<circle cx="50" cy="52" r="42" fill="#fff" {OL}/><circle cx="50" cy="52" r="32" fill="#F7F3EA" stroke="#D8CFC0" stroke-width="2"/><path d="M50 20 L50 52 L80 44 C76 30 64 22 50 20Z" fill="#6CC27A" {OL}/><path d="M50 52 L80 44 C84 60 76 76 62 82Z" fill="#F6A04D" {OL}/><path d="M50 52 L62 82 C46 88 26 80 20 62Z" fill="#E8574A" {OL}/><path d="M50 52 L20 62 C14 44 26 24 50 20Z" fill="#F2D479" {OL}/>'),
 "bread": dict(words=["الكربوهيدرات", "النشويات", "الخبز", "خبز", "السكريات", "الحبوب"], anim="bob", face=(50, 58, .66),
   body='<path d="M14 44 C6 32 18 16 34 18 C42 10 58 10 66 18 C82 16 94 32 86 44 L86 84 C86 90 82 92 78 92 L22 92 C18 92 14 90 14 84Z" fill="#E9B872" {OL}/><path d="M24 40 C30 30 70 30 76 40 L76 84 L24 84Z" fill="#FBE3B6"/>'),
 "protein": dict(words=["البروتينات", "البروتين", "اللحوم", "الدجاج", "دجاج"], anim="bob", face=(46, 46, .6),
   body='<path d="M56 50 C40 70 16 64 14 46 C12 26 34 10 52 14 C70 18 72 36 56 50Z" fill="#C97A4A" {OL}/><path d="M56 50 L80 76" stroke="#F5EEDC" stroke-width="8" stroke-linecap="round"/><circle cx="84" cy="74" r="6" fill="#F5EEDC" {OL}/><circle cx="78" cy="84" r="6" fill="#F5EEDC" {OL}/>'),
 "fats": dict(words=["الدهون", "الزيوت", "الزبدة", "الزيت"], anim="drip", face=(50, 64, .62),
   body='<path d="M36 8 L64 8 L62 22 C78 30 82 44 82 60 L82 84 C82 90 78 94 72 94 L28 94 C22 94 18 90 18 84 L18 60 C18 44 22 30 38 22Z" fill="#F6D365" {OL}/><rect x="34" y="2" width="32" height="10" rx="3" fill="#6CC27A" {OL}/>'),
 "vitamins": dict(words=["الفيتامينات", "فيتامين", "الأملاح المعدنية", "المعادن الغذائية", "فيتامين ج"], anim="bounce", face=(50, 58, .7),
   body='<circle cx="50" cy="56" r="36" fill="#F6A04D" {OL}/><path d="M50 22 C54 12 62 8 70 10 C66 18 58 22 50 22Z" fill="#6CC27A" {OL}/><circle cx="36" cy="44" r="2" fill="#E3862E"/><circle cx="62" cy="40" r="2" fill="#E3862E"/><circle cx="70" cy="66" r="2" fill="#E3862E"/>'),
 "fastfood": dict(words=["الوجبات السريعة", "الأطعمة غير الصحية", "الوجبات غير الصحية", "البرجر"], anim="bob", face=(50, 54, .55),
   body='<path d="M14 40 C14 16 86 16 86 40Z" fill="#E9A54D" {OL}/><rect x="10" y="40" width="80" height="10" rx="5" fill="#6CC27A" {OL}/><rect x="12" y="50" width="76" height="14" rx="6" fill="#8B4A2B" {OL}/><rect x="12" y="64" width="76" height="8" rx="3" fill="#FFD25A" {OL}/><path d="M14 72 L86 72 C86 84 14 84 14 72Z" fill="#E9A54D" {OL}/>'),
 "water_drink": dict(words=["شرب الماء", "كوب الماء", "عطشان", "العطش"], anim="drip", face=(50, 64, .6),
   body='<path d="M20 12 L80 12 L72 92 L28 92Z" fill="#E3F2FD" {OL}/><path d="M24 40 L76 40 L72 88 L28 88Z" fill="#7CC6F2"/><path d="M34 50 L36 80" stroke="#fff" stroke-width="4" stroke-linecap="round" opacity=".7"/>'),
}
ALIAS_ONLY = None
ALIASES = {"صحة الإنسان": "body.immune", "صحة الجسم": "body.immune", "الصحة": "body.immune", "الوقاية من الأمراض": "body.immune", "الوقاية": "body.immune",
           "المحافظة على الصحة": "body.immune", "جسم الإنسان": "body.skeleton", "أجهزة جسم الإنسان": "body.skeleton", "أنظمة جسم الإنسان": "body.skeleton"}
