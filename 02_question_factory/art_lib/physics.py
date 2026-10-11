"""🆕 batch 43 · physics (الفيزياء، وفيزياء العلوم): measuring (units, significant figures, calibration), forces and balance (contact
and field forces, the free-body diagram, torque, the projectile), energy and heat (the watt, efficiency, entropy, the heat pump,
expansion), fluids (Pascal's press, Bernoulli), waves and sound (crest and trough, interference, Doppler, standing waves),
light (sources, lenses and images, diffraction, polarisation, the mirage), electricity (charging, the volt and the ampere,
resistors, AC/DC, transformers), and the modern atom (the laser, the diode, the transistor, decay, quarks).
A word that means something else in maths («البؤرة»، «الصورة»، «التكبير») is limited to science books."""
F = "phys"
SC = ["science"]
D = {
 # ---------- measuring ----------
 "si_units": dict(words=["الوحدات الأساسية", "الوحدات المشتقة", "النظام الدولي للوحدات", "وحدات القياس الدولية"], anim="bob", face=(50, 76, .36), only=SC,
   body='<rect x="4" y="56" width="92" height="14" rx="3" fill="#FFD25A" {OL}/><path d="M14 56 L14 64 M24 56 L24 62 M34 56 L34 64 M44 56 L44 62 M54 56 L54 64 M64 56 L64 62 M74 56 L74 64 M84 56 L84 62" stroke="#3b2a1a" stroke-width="2"/>'
        '<circle cx="26" cy="28" r="18" fill="#fff" {OL}/><path d="M26 28 L26 16 M26 28 L34 32" stroke="#3b2a1a" stroke-width="3" stroke-linecap="round"/><path d="M60 46 L66 14 L84 14 L90 46Z" fill="#AEB8C4" {OL}/>'
        '<text direction="ltr" x="75" y="40" text-anchor="middle" font-size="12" font-weight="800" fill="#3b2a1a" font-family="sans-serif">kg</text>'),
 "sig_figs": dict(words=["الأرقام المعنوية", "الأرقام ذات الدلالة", "التقريب العلمي"], anim="bounce", face=(50, 76, .36), only=SC,
   body='<rect x="6" y="20" width="88" height="44" rx="8" fill="#fff" {OL}/><text direction="ltr" x="50" y="52" text-anchor="middle" font-size="26" font-weight="800" fill="#3b2a1a" font-family="sans-serif">3.40</text>'
        '<path d="M14 58 L86 58" stroke="#6CC27A" stroke-width="4" stroke-linecap="round"/>'),
 "calibration": dict(words=["المعايرة", "الضبط", "معايرة الأجهزة", "خطأ القياس", "أخطاء القياس"], anim="wobble", face=(50, 66, .4), only=SC,
   body='<path d="M10 60 A40 40 0 0 1 90 60Z" fill="#fff" {OL}/><path d="M18 52 L24 56 M30 36 L34 42 M50 28 L50 34 M70 36 L66 42 M82 52 L76 56" stroke="#3b2a1a" stroke-width="3"/>'
        '<path d="M50 60 L64 34" stroke="#E8574A" stroke-width="4" stroke-linecap="round"/><rect x="18" y="66" width="64" height="26" rx="6" fill="#AEB8C4" {OL}/><circle cx="72" cy="79" r="7" fill="#3b3b5c" {OL}/><path d="M72 72 L72 79" stroke="#fff" stroke-width="2.4"/>'),
 "point_particle": dict(words=["نموذج الجسيم النقطي", "الجسيم النقطي", "مخطط الحركة"], anim="bounce", face=(82, 50, .32), only=SC,
   body='<path d="M4 70 L96 70" stroke="#AEB8C4" stroke-width="3"/><circle cx="12" cy="50" r="5" fill="#AEB8C4"/><circle cx="30" cy="50" r="6" fill="#AEB8C4"/><circle cx="52" cy="50" r="7" fill="#AEB8C4"/>'
        '<circle cx="82" cy="50" r="12" fill="#E8574A" {OL}/><path d="M62 30 L80 30 M74 24 L80 30 L74 36" fill="none" stroke="#3b2a1a" stroke-width="3" stroke-linecap="round"/>'),
 "origin": dict(words=["نقطة الأصل", "الإطار المرجعي", "نظام الإحداثيات", "الموقع والإزاحة"], anim="sun", face=(70, 34, .34), only=SC,
   body='<path d="M20 90 L20 8 M8 78 L96 78" stroke="#3b2a1a" stroke-width="4" stroke-linecap="round"/><path d="M14 16 L20 8 L26 16 M88 72 L96 78 L88 84" fill="none" stroke="#3b2a1a" stroke-width="4" stroke-linecap="round"/>'
        '<circle cx="20" cy="78" r="7" fill="#E8574A" {OL}/><circle cx="70" cy="34" r="12" fill="#FFD25A" {OL}/><path d="M20 78 L62 40" stroke="#6CB8FF" stroke-width="3" stroke-dasharray="4 4"/>'),
 "interval": dict(words=["الفترة الزمنية", "ساعة الإيقاف", "قياس الزمن"], anim="sun", face=(50, 66, .4), only=SC,
   body='<circle cx="50" cy="56" r="38" fill="#fff" {OL}/><rect x="42" y="6" width="16" height="10" rx="3" fill="#AEB8C4" {OL}/><path d="M76 22 L84 14" stroke="#3b2a1a" stroke-width="5" stroke-linecap="round"/>'
        '<path d="M50 56 L50 18 A38 38 0 0 1 86 50Z" fill="#9CD86C"/><path d="M50 56 L50 26" stroke="#3b2a1a" stroke-width="4" stroke-linecap="round"/><circle cx="50" cy="56" r="4" fill="#3b2a1a"/><circle cx="50" cy="56" r="38" fill="none" {OL}/>'),
 # ---------- forces and balance ----------
 "contact_force": dict(words=["قوى التلامس", "قوة الدفع", "قوة السحب", "القوة العمودية", "قوة الشد"], anim="bounce", face=(66, 60, .4), only=SC,
   body='<rect x="44" y="34" width="50" height="50" rx="4" fill="#C98A55" {OL}/><path d="M4 84 L96 84" stroke="#3b2a1a" stroke-width="4"/>'
        '<path d="M8 60 L38 60 M30 52 L40 60 L30 68" fill="none" stroke="#E8574A" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>'),
 "field_force": dict(words=["قوى المجال", "قوى عن بعد", "المجال", "خطوط المجال"], anim="sun", face=(50, 50, .38), only=SC,
   body='<circle cx="50" cy="50" r="16" fill="#E8574A" {OL}/><path d="M50 30 L50 6 M50 70 L50 94 M30 50 L6 50 M70 50 L94 50 M36 36 L18 18 M64 36 L82 18 M36 64 L18 82 M64 64 L82 82" stroke="#6CB8FF" stroke-width="3" stroke-linecap="round"/>'
        '<path d="M46 10 L50 4 L54 10 M46 90 L50 96 L54 90 M10 46 L4 50 L10 54 M90 46 L96 50 L90 54" fill="none" stroke="#6CB8FF" stroke-width="3"/>'),
 "free_body": dict(words=["مخطط الجسم الحر", "مخطط القوى", "تمثيل القوى"], anim="bob", face=(50, 50, .4), only=SC,
   body='<rect x="32" y="32" width="36" height="36" rx="4" fill="#C98A55" {OL}/><path d="M50 32 L50 6 M50 68 L50 94 M32 50 L8 50 M68 50 L92 50" stroke="#E8574A" stroke-width="4" stroke-linecap="round"/>'
        '<path d="M44 12 L50 4 L56 12 M44 88 L50 96 L56 88 M14 44 L6 50 L14 56 M86 44 L94 50 L86 56" fill="none" stroke="#E8574A" stroke-width="4" stroke-linecap="round"/>'),
 "equilibrium_f": dict(words=["الاتزان", "الشرط الأول للاتزان", "الشرط الثاني للاتزان", "القوى المتوازنة", "اتزان الأجسام"], anim="wobble", face=(50, 36, .36), only=SC,
   body='<path d="M6 60 L94 60" stroke="#8B5E3C" stroke-width="7" stroke-linecap="round"/><path d="M50 60 L36 90 L64 90Z" fill="#AEB8C4" {OL}/>'
        '<rect x="8" y="38" width="22" height="22" rx="3" fill="#6CB8FF" {OL}/><rect x="70" y="38" width="22" height="22" rx="3" fill="#6CB8FF" {OL}/><circle cx="50" cy="36" r="10" fill="#6CC27A" {OL}/>'),
 "unbalanced": dict(words=["القوى غير المتوازنة", "القوة المحصلة غير الصفرية"], anim="wobble", face=(50, 30, .34), only=SC,
   body='<path d="M8 74 L92 40" stroke="#8B5E3C" stroke-width="7" stroke-linecap="round"/><path d="M50 58 L36 90 L64 90Z" fill="#AEB8C4" {OL}/>'
        '<rect x="6" y="46" width="28" height="28" rx="3" fill="#E8574A" {OL}/><rect x="72" y="24" width="16" height="16" rx="3" fill="#6CB8FF" {OL}/>'),
 "action_reaction": dict(words=["زوج التأثير المتبادل", "الفعل ورد الفعل", "قانون نيوتن الثالث", "الارتداد"], anim="bounce", face=(50, 20, .34), only=SC,
   body='<rect x="8" y="40" width="34" height="34" rx="4" fill="#6CB8FF" {OL}/><rect x="58" y="40" width="34" height="34" rx="4" fill="#F6B73C" {OL}/>'
        '<path d="M42 57 L58 57" stroke="#3b2a1a" stroke-width="3"/><path d="M34 88 L4 88 M12 82 L4 88 L12 94 M66 88 L96 88 M88 82 L96 88 L88 94" fill="none" stroke="#E8574A" stroke-width="4" stroke-linecap="round"/>'),
 "resultant": dict(words=["المحصلة", "محصلة القوى", "محصلة المتجهات"], anim="bob", face=(30, 70, .34),
   body='<path d="M10 86 L60 86" stroke="#6CB8FF" stroke-width="5" stroke-linecap="round"/><path d="M60 86 L86 26" stroke="#6CC27A" stroke-width="5" stroke-linecap="round"/><path d="M10 86 L86 26" stroke="#E8574A" stroke-width="6" stroke-linecap="round"/>'
        '<path d="M52 80 L60 86 L52 92 M78 30 L86 26 L86 36 M74 28 L86 26 L82 38" fill="none" stroke="#3b2a1a" stroke-width="3"/>'),
 "torque": dict(words=["العزم", "العزم المحصل", "عزم القوة", "الجسم الجاسئ", "ذراع القوة"], never=["earth"], anim="sun", face=(30, 30, .36), only=SC,
   body='<circle cx="30" cy="30" r="16" fill="#AEB8C4" {OL}/><polygon points="30,20 39,25 39,35 30,40 21,35 21,25" fill="#5D646E"/><path d="M40 40 L86 86" stroke="#C9D2DC" stroke-width="14" stroke-linecap="round"/>'
        '<path d="M40 40 L86 86" stroke="#3b2a1a" stroke-width="2"/><path d="M74 58 C88 62 92 74 88 88 M82 80 L88 88 L94 80" fill="none" stroke="#E8574A" stroke-width="4" stroke-linecap="round"/>'),
 "radian": dict(words=["الراديان", "القياس الدائري", "الزاوية بالراديان"], anim="sun", face=(66, 66, .34),
   body='<circle cx="50" cy="50" r="40" fill="#fff" {OL}/><path d="M50 50 L90 50" stroke="#6CB8FF" stroke-width="4"/><path d="M50 50 L71.6 16.3" stroke="#6CB8FF" stroke-width="4"/>'
        '<path d="M90 50 A40 40 0 0 0 71.6 16.3" fill="none" stroke="#E8574A" stroke-width="6"/><path d="M62 50 A12 12 0 0 0 56.5 39.9" fill="none" stroke="#3b2a1a" stroke-width="2"/><circle cx="50" cy="50" r="3" fill="#3b2a1a"/>'),
 "projectile": dict(words=["المقذوف", "مسار المقذوف", "المركبتان الأفقية والرأسية", "أقصى ارتفاع", "حركة المقذوفات", "المدى الأفقي"], never=["earth"], anim="bounce", face=(50, 26, .32), only=SC,
   body='<path d="M4 90 L96 90" stroke="#3b2a1a" stroke-width="4"/><path d="M10 88 C30 4 70 4 90 88" fill="none" stroke="#6CB8FF" stroke-width="3" stroke-dasharray="5 4"/>'
        '<circle cx="50" cy="26" r="9" fill="#E8574A" {OL}/><path d="M50 26 L72 26 M66 22 L72 26 L66 30" fill="none" stroke="#3b2a1a" stroke-width="3"/><path d="M50 40 L50 86" stroke="#AEB8C4" stroke-width="2" stroke-dasharray="3 3"/>'),
 # ---------- energy and heat ----------
 "watt": dict(words=["الواط", "القدرة الكهربائية"], anim="bob", face=(50, 40, .42), only=SC,
   body='<path d="M50 6 C28 6 18 24 24 40 C28 50 36 54 36 64 L64 64 C64 54 72 50 76 40 C82 24 72 6 50 6Z" fill="#FFD25A" {OL}/><rect x="36" y="64" width="28" height="18" rx="3" fill="#AEB8C4" {OL}/>'
        '<text direction="ltr" x="50" y="98" text-anchor="middle" font-size="16" font-weight="800" fill="#3b2a1a" font-family="sans-serif">W</text>'),
 "efficiency": dict(words=["الكفاءة", "كفاءة الطاقة", "كفاءة الآلة", "الكفاءة الحرارية"], anim="bounce", face=(30, 50, .36), only=SC,
   body='<path d="M4 34 L56 34 L56 66 L4 66Z" fill="#F6B73C" {OL}/><path d="M56 34 L96 22 L96 46 L56 54Z" fill="#6CC27A" {OL}/><path d="M56 58 L84 86 L72 92 L56 66Z" fill="#E8574A" {OL}/>'
        '<path d="M90 70 C86 62 94 60 90 52" fill="none" stroke="#E8574A" stroke-width="2.4"/>'),
 "reference_level": dict(words=["مستوى الإسناد", "طاقة الوضع الجاذبية", "الارتفاع المرجعي"], anim="bob", face=(64, 26, .34), only=SC,
   body='<path d="M4 90 L96 90" stroke="#3b2a1a" stroke-width="4" stroke-dasharray="6 4"/><rect x="50" y="40" width="40" height="8" fill="#C98A55" {OL}/><circle cx="64" cy="28" r="12" fill="#E8574A" {OL}/>'
        '<path d="M24 86 L24 46 M18 52 L24 44 L30 52 M18 80 L24 88 L30 80" fill="none" stroke="#6CB8FF" stroke-width="3"/><text direction="ltr" x="12" y="70" font-size="14" font-weight="800" fill="#3b2a1a" font-family="sans-serif">h</text>'),
 "thermal_eq": dict(words=["الاتزان الحراري", "انتقال الحرارة بين جسمين", "التوازن الحراري"], anim="wobble", face=(50, 76, .34), only=SC,
   body='<rect x="6" y="40" width="40" height="40" rx="4" fill="#E8574A" {OL}/><rect x="54" y="40" width="40" height="40" rx="4" fill="#F6A23C" {OL}/>'
        '<path d="M30 26 C40 18 60 18 70 26 M64 20 L70 26 L62 30" fill="none" stroke="#3b2a1a" stroke-width="3" stroke-linecap="round"/><path d="M40 92 L60 92" stroke="#3b2a1a" stroke-width="3"/><path d="M40 96 L60 96" stroke="#3b2a1a" stroke-width="3"/>'),
 "entropy": dict(words=["الإنتروبي", "العشوائية الحرارية", "القانون الثاني للديناميكا الحرارية"], anim="wiggle", face=(76, 80, .32), only=SC,
   body='<rect x="4" y="16" width="42" height="42" rx="4" fill="#fff" {OL}/><circle cx="15" cy="27" r="4" fill="#6CB8FF"/><circle cx="25" cy="27" r="4" fill="#6CB8FF"/><circle cx="35" cy="27" r="4" fill="#6CB8FF"/><circle cx="15" cy="37" r="4" fill="#E8574A"/><circle cx="25" cy="37" r="4" fill="#E8574A"/><circle cx="35" cy="37" r="4" fill="#E8574A"/>'
        '<path d="M48 40 L56 40 M52 36 L56 40 L52 44" fill="none" stroke="#3b2a1a" stroke-width="3"/><rect x="58" y="16" width="38" height="42" rx="4" fill="#fff" {OL}/><circle cx="66" cy="44" r="4" fill="#6CB8FF"/><circle cx="84" cy="24" r="4" fill="#6CB8FF"/><circle cx="74" cy="30" r="4" fill="#E8574A"/><circle cx="88" cy="48" r="4" fill="#E8574A"/><circle cx="66" cy="22" r="4" fill="#E8574A"/><circle cx="80" cy="40" r="4" fill="#6CB8FF"/>'),
 "heat_pump": dict(words=["المضخة الحرارية", "المكيف", "المبرد", "التكييف"], anim="wind", face=(50, 50, .4), only=SC,
   body='<rect x="16" y="20" width="68" height="60" rx="8" fill="#E8F2F8" {OL}/><circle cx="50" cy="50" r="18" fill="#fff" {OL}/><path d="M50 32 C56 42 56 46 50 50 C44 54 44 58 50 68 M32 50 C42 44 46 44 50 50 C54 56 58 56 68 50" fill="none" stroke="#6CB8FF" stroke-width="3"/>'
        '<path d="M2 36 L12 36 M2 50 L12 50 M2 64 L12 64" stroke="#6CB8FF" stroke-width="3" stroke-linecap="round"/><path d="M88 36 L98 36 M88 50 L98 50 M88 64 L98 64" stroke="#E8574A" stroke-width="3" stroke-linecap="round"/>'),
 "expansion": dict(words=["معامل التمدد الطولي", "معامل التمدد الحجمي", "التمدد الحراري", "تمدد المواد بالحرارة"], anim="wobble", face=(50, 40, .34), only=SC,
   body='<rect x="10" y="30" width="60" height="16" rx="4" fill="#AEB8C4" {OL}/><rect x="10" y="58" width="80" height="16" rx="4" fill="#E8853C" {OL}/>'
        '<path d="M74 38 L90 38 M84 32 L90 38 L84 44" fill="none" stroke="#E8574A" stroke-width="3"/><path d="M30 86 C26 80 34 78 30 72 M50 88 C46 82 54 80 50 74 M70 86 C66 80 74 78 70 72" fill="none" stroke="#E8574A" stroke-width="3" stroke-linecap="round"/>'),
 # ---------- fluids ----------
 "fluids": dict(words=["الموائع", "الموائع الساكنة", "خصائص الموائع"], anim="drip", face=(50, 70, .4), only=SC,
   body='<path d="M16 10 L16 90 C16 96 84 96 84 90 L84 10" fill="#E8F6FF" {OL}/><path d="M17 50 C30 44 40 56 50 50 C60 44 70 56 83 50 L83 90 C83 94 17 94 17 90Z" fill="#7CC6F2"/>'
        '<circle cx="34" cy="30" r="3" fill="#AEB8C4"/><circle cx="56" cy="22" r="3" fill="#AEB8C4"/><circle cx="68" cy="34" r="3" fill="#AEB8C4"/><path d="M16 10 L16 90 C16 96 84 96 84 90 L84 10" fill="none" {OL}/>'),
 "pascal_unit": dict(words=["الباسكال", "وحدة الضغط", "مقياس الضغط"], anim="sun", face=(50, 70, .36), only=SC,
   body='<circle cx="50" cy="50" r="40" fill="#fff" {OL}/><path d="M22 62 A30 30 0 0 1 78 62" fill="none" stroke="#AEB8C4" stroke-width="6"/><path d="M50 56 L70 34" stroke="#E8574A" stroke-width="4" stroke-linecap="round"/>'
        '<circle cx="50" cy="56" r="5" fill="#3b2a1a"/><text direction="ltr" x="50" y="82" text-anchor="middle" font-size="14" font-weight="800" fill="#3b2a1a" font-family="sans-serif">Pa</text>'),
 "cohesion": dict(words=["قوى التماسك", "قوى التلاصق"], anim="drip", face=(30, 64, .38), only=SC,
   body='<path d="M4 80 C20 70 40 70 56 80Z" fill="#9CD86C" {OL}/><path d="M30 74 C18 74 16 56 30 44 C44 56 42 74 30 74Z" fill="#7CC6F2" {OL}/>'
        '<rect x="70" y="10" width="14" height="80" rx="4" fill="#E8F6FF" {OL}/><rect x="71" y="34" width="12" height="55" fill="#7CC6F2"/><path d="M62 90 L92 90" stroke="#7CC6F2" stroke-width="6"/>'),
 "hydraulic": dict(words=["مبدأ باسكال", "المكبس الهيدروليكي", "الرافعة الهيدروليكية", "الضغط في السوائل"], anim="bounce", face=(78, 24, .34), only=SC,
   body='<path d="M6 40 L26 40 L26 74 L64 74 L64 30 L94 30 L94 92 L6 92Z" fill="#7CC6F2" {OL}/><rect x="6" y="30" width="20" height="10" fill="#AEB8C4" {OL}/><rect x="64" y="20" width="30" height="10" fill="#AEB8C4" {OL}/>'
        '<path d="M16 6 L16 26 M10 20 L16 28 L22 20" fill="none" stroke="#E8574A" stroke-width="4" stroke-linecap="round"/><rect x="68" y="4" width="22" height="16" rx="3" fill="#E8574A" {OL}/>'),
 "bernoulli": dict(words=["مبدأ برنولي", "خطوط الانسياب", "الرفع الهوائي", "جناح الطائرة"], anim="wind", face=(46, 50, .38), only=SC,
   body='<path d="M10 54 C20 34 70 30 92 50 C70 56 30 60 10 54Z" fill="#AEB8C4" {OL}/><path d="M2 30 C30 16 70 14 98 30 M2 70 C30 66 70 66 98 66" fill="none" stroke="#6CB8FF" stroke-width="3" stroke-linecap="round"/>'
        '<path d="M2 42 C30 26 70 24 98 40" fill="none" stroke="#6CB8FF" stroke-width="2" stroke-dasharray="4 3"/><path d="M50 28 L50 8 M44 14 L50 6 L56 14" fill="none" stroke="#6CC27A" stroke-width="4" stroke-linecap="round"/>'),
 "elasticity": dict(words=["المرونة", "قانون هوك", "النابض", "الزنبرك", "ثابت النابض"], anim="bounce", face=(50, 84, .32), only=SC,
   body='<rect x="20" y="4" width="60" height="8" fill="#8B5E3C" {OL}/><path d="M50 12 L50 18 L36 24 L64 30 L36 36 L64 42 L36 48 L64 54 L36 60 L50 66 L50 70" fill="none" stroke="#3b2a1a" stroke-width="3" stroke-linejoin="round"/>'
        '<rect x="34" y="70" width="32" height="26" rx="4" fill="#AEB8C4" {OL}/>'),
 # ---------- waves and sound ----------
 "crest_trough": dict(words=["القمة والقاع", "قمة الموجة", "قاع الموجة", "الطول الموجي", "سعة الموجة"], anim="sway", face=(30, 24, .32), only=SC,
   body='<path d="M4 50 L96 50" stroke="#AEB8C4" stroke-width="2" stroke-dasharray="4 3"/><path d="M4 50 C14 10 34 10 42 50 C50 90 70 90 78 50 C84 26 92 22 96 30" fill="none" stroke="#6CB8FF" stroke-width="5" stroke-linecap="round"/>'
        '<circle cx="23" cy="20" r="4" fill="#E8574A"/><circle cx="60" cy="80" r="4" fill="#6CC27A"/><path d="M23 24 L23 50" stroke="#E8574A" stroke-width="2"/>'),
 "interference": dict(words=["مبدأ التراكب", "التداخل البناء", "التداخل الهدام", "تداخل الموجات", "التداخل"], anim="sway", face=(50, 86, .3), only=SC,
   body='<path d="M4 20 C14 6 24 6 30 20 C36 34 46 34 52 20 C58 6 68 6 74 20 C80 34 90 34 96 20" fill="none" stroke="#6CB8FF" stroke-width="3"/><path d="M4 44 C14 30 24 30 30 44 C36 58 46 58 52 44 C58 30 68 30 74 44 C80 58 90 58 96 44" fill="none" stroke="#6CC27A" stroke-width="3"/>'
        '<path d="M4 76 C14 52 24 52 30 76 C36 98 46 98 52 76 C58 52 68 52 74 76 C80 98 90 98 96 76" fill="none" stroke="#E8574A" stroke-width="4"/>'),
 "decibel": dict(words=["الديسبل", "الديسيبل", "شدة الصوت", "مستوى الصوت"], anim="buzz", face=(34, 30, .32), only=SC,
   body='<rect x="8" y="8" width="52" height="84" rx="10" fill="#3b3b5c" {OL}/><rect x="14" y="16" width="40" height="30" rx="4" fill="#BFE3F2"/><text direction="ltr" x="34" y="38" text-anchor="middle" font-size="12" font-weight="800" fill="#3b2a1a" font-family="sans-serif">dB</text>'
        '<rect x="16" y="56" width="8" height="28" fill="#6CC27A"/><rect x="30" y="64" width="8" height="20" fill="#FFD25A"/><rect x="44" y="70" width="8" height="14" fill="#E8574A"/><path d="M70 36 C78 42 78 58 70 64 M80 26 C92 38 92 62 80 74" fill="none" stroke="#3b2a1a" stroke-width="3" stroke-linecap="round"/>'),
 "doppler": dict(words=["تأثير دوبلر", "ظاهرة دوبلر"], anim="bounce", face=(56, 62, .34), only=SC,
   body='<path d="M30 40 C26 40 26 60 30 60 M22 34 C16 34 16 66 22 66 M12 28 C4 28 4 72 12 72" fill="none" stroke="#6CB8FF" stroke-width="3"/>'
        '<path d="M80 40 C82 40 82 60 80 60 M84 36 C88 36 88 64 84 64 M88 32 C92 32 92 68 88 68" fill="none" stroke="#E8574A" stroke-width="3"/>'
        '<rect x="38" y="44" width="38" height="28" rx="6" fill="#fff" {OL}/><path d="M54 50 L54 66 M46 58 L62 58" stroke="#E8574A" stroke-width="4"/><circle cx="46" cy="76" r="5" fill="#3b2a1a"/><circle cx="68" cy="76" r="5" fill="#3b2a1a"/><rect x="50" y="36" width="10" height="8" fill="#6CB8FF" {OL}/>'),
 "tuning_fork": dict(words=["الرنان", "الشوكة الرنانة", "الأوتار المهتزة", "النغمات التوافقية", "الموجات الموقوفة"], anim="buzz", face=(50, 70, .34), only=SC,
   body='<path d="M36 6 L36 48 C36 62 64 62 64 48 L64 6" fill="none" stroke="#AEB8C4" stroke-width="9" stroke-linecap="round"/><path d="M50 60 L50 92" stroke="#AEB8C4" stroke-width="9" stroke-linecap="round"/>'
        '<path d="M22 16 C16 22 16 30 22 36 M78 16 C84 22 84 30 78 36 M12 10 C2 20 2 34 12 44 M88 10 C98 20 98 34 88 44" fill="none" stroke="#6CB8FF" stroke-width="3" stroke-linecap="round"/>'),
 "air_column": dict(words=["العمود الهوائي المغلق", "العمود الهوائي المفتوح", "الأعمدة الهوائية", "الآلات الهوائية"], anim="sway", face=(50, 86, .3), only=SC,
   body='<rect x="8" y="30" width="84" height="40" rx="4" fill="#E8F6FF" {OL}/><path d="M92 30 L92 70" stroke="#3b2a1a" stroke-width="7"/>'
        '<path d="M8 32 C40 32 60 50 90 50 C60 50 40 68 8 68" fill="none" stroke="#6CB8FF" stroke-width="4"/>'),
 "beats": dict(words=["الضربات", "ضربات الصوت"], anim="buzz", face=(50, 86, .3), only=SC,
   body='<path d="M4 50 C10 20 14 20 18 50 C22 80 26 80 30 50 C34 34 38 34 42 50 C46 60 50 60 54 50 C58 34 62 34 66 50 C70 80 74 80 78 50 C82 20 86 20 90 50 L96 50" fill="none" stroke="#6CB8FF" stroke-width="3"/>'
        '<path d="M4 50 C30 4 30 4 48 50 C66 96 66 96 96 50" fill="none" stroke="#E8574A" stroke-width="2" stroke-dasharray="4 3"/>'),
 # ---------- light ----------
 "light_source": dict(words=["المصدر المضيء", "الأجسام المضيئة", "مصادر الضوء", "الأجسام المضيئة بذاتها"], anim="sun", face=(50, 50, .45), only=SC,
   body='<circle cx="50" cy="50" r="24" fill="#FFD25A" {OL}/><path d="M50 4 L50 18 M50 82 L50 96 M4 50 L18 50 M82 50 L96 50 M17 17 L27 27 M73 73 L83 83 M17 83 L27 73 M73 27 L83 17" stroke="#F6B73C" stroke-width="5" stroke-linecap="round"/>'),
 "lit_object": dict(words=["المصدر المستضيء", "الأجسام المستضيئة", "الأجسام غير المضيئة"], anim="bob", face=(66, 60, .4), only=SC,
   body='<circle cx="16" cy="20" r="12" fill="#FFD25A" {OL}/><path d="M28 26 L52 40 M26 34 L48 52" stroke="#F6B73C" stroke-width="3" stroke-dasharray="4 3"/>'
        '<circle cx="66" cy="60" r="28" fill="#C9D2DC" {OL}/><path d="M66 32 A28 28 0 0 1 66 88 A20 28 0 0 0 66 32Z" fill="#8A93A6"/>'),
 "illuminance": dict(words=["الاستضاءة", "شدة الإضاءة", "التدفق الضوئي", "الإضاءة"], anim="sun", face=(50, 86, .3), only=SC,
   body='<path d="M30 6 L70 6 L80 30 L20 30Z" fill="#6CC27A" {OL}/><path d="M24 30 L6 86 L94 86 L76 30Z" fill="#FFF3C4" opacity=".9"/><path d="M4 86 L96 86" stroke="#C98A55" stroke-width="8" stroke-linecap="round"/>'
        '<rect x="34" y="72" width="32" height="14" fill="#fff" {OL}/>'),
 "diffraction": dict(words=["الحيود", "الحيود في الشق المفرد", "محزوز الحيود", "أهداب التداخل", "معيار رايلي", "حيود الضوء"], never=["earth"], anim="sway", face=(20, 50, .3), only=SC,
   body='<path d="M4 20 L4 80 M12 20 L12 80 M20 20 L20 80" stroke="#6CB8FF" stroke-width="3"/><rect x="34" y="4" width="8" height="40" fill="#3b2a1a"/><rect x="34" y="56" width="8" height="40" fill="#3b2a1a"/>'
        '<path d="M52 40 A14 14 0 0 1 52 60 M60 30 A24 24 0 0 1 60 70 M70 20 A36 36 0 0 1 70 80 M82 10 A48 48 0 0 1 82 90" fill="none" stroke="#6CB8FF" stroke-width="3"/>'),
 "pigments": dict(words=["الأصباغ", "الأصباغ الأساسية", "خلط الألوان", "ألوان الطيف"], anim="bounce", face=(50, 70, .36), only=SC,
   body='<path d="M50 6 C20 6 4 30 8 54 C12 76 30 86 46 84 C56 82 52 70 60 66 C72 60 92 70 94 50 C96 24 78 6 50 6Z" fill="#F2D07A" {OL}/>'
        '<circle cx="28" cy="34" r="8" fill="#E8574A" {OL}/><circle cx="50" cy="22" r="8" fill="#FFD25A" {OL}/><circle cx="72" cy="30" r="8" fill="#6CB8FF" {OL}/><circle cx="26" cy="58" r="8" fill="#6CC27A" {OL}/>'),
 "polarization": dict(words=["الاستقطاب", "استقطاب الضوء", "المرشح المستقطب"], anim="sway", face=(50, 86, .3), only=SC,
   body='<path d="M4 50 L20 50 M8 40 L20 60 M8 60 L20 40 M12 38 L12 62" stroke="#FFD25A" stroke-width="3"/><rect x="30" y="16" width="16" height="68" rx="4" fill="#B0A8C9" {OL}/>'
        '<path d="M34 24 L34 76 M38 24 L38 76 M42 24 L42 76" stroke="#3b2a1a" stroke-width="1.6"/><path d="M56 50 L96 50 M64 36 L64 64 M78 36 L78 64 M92 36 L92 64" stroke="#FFD25A" stroke-width="3"/>'),
 "lens_image": dict(words=["الصورة الحقيقية", "الصورة الخيالية", "الصورة الحقيقية والخيالية", "المحور الرئيس", "البعد البؤري", "بؤرة العدسة", "العدسة المحدبة", "العدسة المقعرة", "تكوين الصور"], anim="bob", face=(50, 22, .3), only=SC,
   body='<path d="M4 50 L96 50" stroke="#3b2a1a" stroke-width="2"/><path d="M50 10 C62 30 62 70 50 90 C38 70 38 30 50 10Z" fill="#BFE3F2" {OL}/>'
        '<path d="M14 50 L14 30 M10 34 L14 28 L18 34" fill="none" stroke="#6CC27A" stroke-width="4"/><path d="M84 50 L84 70 M80 66 L84 72 L88 66" fill="none" stroke="#E8574A" stroke-width="4"/>'
        '<path d="M14 30 L50 30 L84 70 M14 30 L84 70" fill="none" stroke="#F6B73C" stroke-width="2"/><circle cx="70" cy="50" r="3" fill="#3b2a1a"/><circle cx="30" cy="50" r="3" fill="#3b2a1a"/>'),
 "focus_lens": dict(words=["البؤرة", "التكبير", "التكبير البصري", "تجميع الأشعة"], anim="bob", face=(50, 80, .3), only=["physics"],
   body='<path d="M4 50 L96 50" stroke="#AEB8C4" stroke-width="2"/><path d="M40 10 C52 30 52 70 40 90 C28 70 28 30 40 10Z" fill="#BFE3F2" {OL}/>'
        '<path d="M2 30 L40 30 L78 50 M2 50 L78 50 M2 70 L40 70 L78 50" fill="none" stroke="#F6B73C" stroke-width="3"/><circle cx="78" cy="50" r="6" fill="#E8574A" {OL}/>'),
 "aberration": dict(words=["الزيغ الكروي", "الزيغ اللوني", "عيوب العدسات"], anim="wobble", face=(36, 22, .3), only=SC,
   body='<path d="M36 6 C50 30 50 70 36 94 C22 70 22 30 36 6Z" fill="#BFE3F2" {OL}/><path d="M2 30 L36 30 L76 54 M2 70 L36 70 L76 46" fill="none" stroke="#E8574A" stroke-width="2.6"/>'
        '<path d="M2 40 L36 40 L86 52 M2 60 L36 60 L86 48" fill="none" stroke="#6CB8FF" stroke-width="2.6"/><ellipse cx="80" cy="50" rx="12" ry="8" fill="none" stroke="#3b2a1a" stroke-width="2" stroke-dasharray="3 2"/>'),
 "critical_angle": dict(words=["الزاوية الحرجة", "الانعكاس الكلي الداخلي", "الألياف البصرية"], anim="sway", face=(80, 76, .3), only=SC,
   body='<rect x="4" y="50" width="92" height="46" fill="#7CC6F2" {OL}/><path d="M30 92 L50 50 L96 50" fill="none" stroke="#FFD25A" stroke-width="4" stroke-linejoin="round"/>'
        '<path d="M50 30 L50 96" stroke="#3b2a1a" stroke-width="2" stroke-dasharray="4 3"/><path d="M50 62 A12 12 0 0 1 44 61" fill="none" stroke="#E8574A" stroke-width="3"/>'),
 "mirage": dict(words=["السراب", "ظاهرة السراب"], anim="sway", face=(78, 30, .32), only=SC,
   body='<rect x="4" y="4" width="92" height="50" fill="#BFE3F2"/><circle cx="78" cy="22" r="10" fill="#FFD25A" {OL}/><path d="M4 54 L96 54 L96 96 L4 96Z" fill="#F2C46D" {OL}/>'
        '<path d="M14 66 C24 62 34 70 44 66 C54 62 64 70 74 66 M20 78 C30 74 40 82 50 78 C60 74 70 82 80 78" fill="none" stroke="#7CC6F2" stroke-width="4" stroke-linecap="round"/><path d="M30 40 C30 30 40 30 40 40 L40 54 L30 54Z" fill="#6CC27A" {OL}/>'),
 "myopia": dict(words=["قصر النظر", "طول النظر", "عيوب الإبصار", "تصحيح النظر"], anim="wobble", face=(30, 34, .3), only=SC,
   body='<circle cx="62" cy="50" r="34" fill="#fff" {OL}/><circle cx="34" cy="50" r="10" fill="#6CB8FF" {OL}/>'
        '<path d="M2 36 L30 44 L74 54 M2 64 L30 56 L74 46" fill="none" stroke="#F6B73C" stroke-width="2.6"/><circle cx="74" cy="50" r="4" fill="#E8574A"/><path d="M96 30 C100 44 100 56 96 70" fill="none" stroke="#E8574A" stroke-width="3"/>'),
 "microscope": dict(words=["المجهر", "المجهر الضوئي", "المجهر المركب", "استخدام المجهر"], anim="bob", face=(46, 30, .3),
   body='<rect x="38" y="6" width="16" height="44" rx="4" fill="#AEB8C4" {OL} transform="rotate(-20 46 28)"/><path d="M60 30 C80 40 80 70 60 76" fill="none" stroke="#3b2a1a" stroke-width="8" stroke-linecap="round"/>'
        '<rect x="26" y="60" width="44" height="8" rx="2" fill="#5D646E" {OL}/><rect x="20" y="86" width="60" height="10" rx="3" fill="#5D646E" {OL}/><path d="M64 76 L64 86" stroke="#3b2a1a" stroke-width="8"/><circle cx="48" cy="56" r="4" fill="#BFE3F2" {OL}/>'),
 "thin_film": dict(words=["التداخل في الأغشية الرقيقة", "فقاعة الصابون", "ألوان الأغشية الرقيقة"], anim="bob", face=(50, 60, .4), only=SC,
   body='<circle cx="50" cy="50" r="42" fill="#E8F6FF" {OL}/><path d="M18 40 C28 20 52 14 70 22" fill="none" stroke="#F59BB8" stroke-width="5" stroke-linecap="round"/><path d="M14 54 C20 34 40 22 62 24" fill="none" stroke="#FFD25A" stroke-width="4" stroke-linecap="round"/>'
        '<path d="M24 70 C30 80 50 86 66 80" fill="none" stroke="#9CD86C" stroke-width="4" stroke-linecap="round"/><circle cx="64" cy="30" r="5" fill="#fff"/>'),
 # ---------- electricity ----------
 "charging": dict(words=["الشحن بالدلك", "حفظ الشحنة", "الشحن بالتوصيل", "الشحن بالحث", "تقاسم الشحنة", "الكهرباء الساكنة", "الشحنات الكهربائية"], anim="wiggle", face=(40, 40, .38), only=SC,
   body='<ellipse cx="40" cy="40" rx="30" ry="34" fill="#E8574A" {OL}/><path d="M40 74 L36 84 L44 84Z" fill="#E8574A" {OL}/><path d="M40 84 C40 92 48 92 46 98" fill="none" stroke="#3b2a1a" stroke-width="2"/>'
        '<text direction="ltr" x="30" y="40" text-anchor="middle" font-size="14" font-weight="800" fill="#fff" font-family="sans-serif">−</text><text direction="ltr" x="50" y="54" text-anchor="middle" font-size="14" font-weight="800" fill="#fff" font-family="sans-serif">−</text>'
        '<path d="M76 20 L84 30 M84 20 L76 30 M80 46 L80 56 M75 51 L85 51 M78 70 L88 80" stroke="#FFD25A" stroke-width="3" stroke-linecap="round"/>'),
 "grounding": dict(words=["التأريض", "السلك الأرضي", "توصيل الأرضي"], anim="buzz", face=(50, 24, .32), only=SC,
   body='<path d="M50 4 L50 54" stroke="#3b2a1a" stroke-width="5"/><path d="M20 54 L80 54 M30 66 L70 66 M40 78 L60 78 M46 90 L54 90" stroke="#3b2a1a" stroke-width="5" stroke-linecap="round"/>'
        '<path d="M64 10 L56 26 L66 26 L58 42" fill="none" stroke="#FFD25A" stroke-width="4" stroke-linejoin="round"/>'),
 "coulomb": dict(words=["الكولوم", "الشحنة الأساسية", "شحنة الاختبار", "قانون كولوم", "شحنة الإلكترون"], anim="bounce", face=(30, 70, .3), only=SC,
   body='<circle cx="28" cy="40" r="20" fill="#E8574A" {OL}/><text direction="ltr" x="28" y="48" text-anchor="middle" font-size="22" font-weight="800" fill="#fff" font-family="sans-serif">+</text>'
        '<circle cx="76" cy="40" r="14" fill="#6CB8FF" {OL}/><text direction="ltr" x="76" y="47" text-anchor="middle" font-size="18" font-weight="800" fill="#fff" font-family="sans-serif">−</text><path d="M50 40 L60 40 M46 40 L50 36 M46 40 L50 44" stroke="#3b2a1a" stroke-width="2.4"/>'
        '<text direction="ltr" x="50" y="88" text-anchor="middle" font-size="16" font-weight="800" fill="#3b2a1a" font-family="sans-serif">C</text>'),
 "meter_va": dict(words=["الفولت", "الفولتميتر", "الأميتر", "الجلفانومتر", "أجهزة القياس الكهربائية"], anim="sun", face=(50, 82, .3), only=SC,
   body='<rect x="8" y="10" width="84" height="80" rx="10" fill="#fff" {OL}/><path d="M18 60 A32 32 0 0 1 82 60" fill="none" stroke="#AEB8C4" stroke-width="5"/>'
        '<path d="M26 50 L30 54 M50 30 L50 36 M74 50 L70 54" stroke="#3b2a1a" stroke-width="3"/><path d="M50 62 L66 34" stroke="#E8574A" stroke-width="4" stroke-linecap="round"/><circle cx="50" cy="62" r="5" fill="#3b2a1a"/>'
        '<text direction="ltr" x="28" y="84" text-anchor="middle" font-size="13" font-weight="800" fill="#3b2a1a" font-family="sans-serif">V</text><text direction="ltr" x="72" y="84" text-anchor="middle" font-size="13" font-weight="800" fill="#3b2a1a" font-family="sans-serif">A</text>'),
 "equipotential": dict(words=["سطوح تساوي الجهد", "خطوط تساوي الجهد", "المجال الكهربائي"], anim="sun", face=(50, 50, .3), only=SC,
   body='<circle cx="50" cy="50" r="44" fill="none" stroke="#6CB8FF" stroke-width="2.6" stroke-dasharray="4 3"/><circle cx="50" cy="50" r="30" fill="none" stroke="#6CB8FF" stroke-width="2.6" stroke-dasharray="4 3"/>'
        '<circle cx="50" cy="50" r="16" fill="#E8574A" {OL}/><text direction="ltr" x="50" y="57" text-anchor="middle" font-size="18" font-weight="800" fill="#fff" font-family="sans-serif">+</text>'),
 "capacitor": dict(words=["المكثف الكهربائي", "المواسع", "السعة الكهربائية"], anim="buzz", face=(50, 86, .3), only=SC,
   body='<path d="M4 50 L40 50 M60 50 L96 50" stroke="#3b2a1a" stroke-width="4"/><rect x="38" y="16" width="8" height="68" fill="#E8574A" {OL}/><rect x="54" y="16" width="8" height="68" fill="#6CB8FF" {OL}/>'
        '<text direction="ltr" x="30" y="30" text-anchor="middle" font-size="14" font-weight="800" fill="#E8574A" font-family="sans-serif">+</text><text direction="ltr" x="70" y="30" text-anchor="middle" font-size="14" font-weight="800" fill="#6CB8FF" font-family="sans-serif">−</text>'),
 "current": dict(words=["التيار الاصطلاحي", "الأمبير", "اتجاه التيار"], anim="buzz", face=(50, 30, .32), only=SC,
   body='<path d="M4 60 L96 60" stroke="#C98A55" stroke-width="12" stroke-linecap="round"/><path d="M4 60 L96 60" stroke="#E8853C" stroke-width="6" stroke-linecap="round"/>'
        '<path d="M60 76 L84 76 M76 70 L84 76 L76 82" fill="none" stroke="#E8574A" stroke-width="4" stroke-linecap="round"/><circle cx="24" cy="60" r="3" fill="#FFD25A"/><circle cx="48" cy="60" r="3" fill="#FFD25A"/><circle cx="72" cy="60" r="3" fill="#FFD25A"/>'),
 "resistor": dict(words=["المقاوم", "المقاومات"], anim="buzz", face=(50, 80, .3), only=SC,
   body='<path d="M4 50 L22 50 L28 34 L38 66 L48 34 L58 66 L68 34 L74 50 L96 50" fill="none" stroke="#3b2a1a" stroke-width="4" stroke-linejoin="round"/>'
        '<text direction="ltr" x="50" y="92" text-anchor="middle" font-size="16" font-weight="800" fill="#E8574A" font-family="sans-serif">Ω</text>'),
 "heating_effect": dict(words=["التأثير الحراري للتيار", "الأجهزة الحرارية", "السخان الكهربائي"], anim="wobble", face=(50, 30, .3), only=SC,
   body='<rect x="10" y="40" width="80" height="50" rx="10" fill="#C9D2DC" {OL}/><path d="M18 58 C26 50 30 66 38 58 C46 50 50 66 58 58 C66 50 70 66 78 58" fill="none" stroke="#E8574A" stroke-width="4"/>'
        '<path d="M30 30 C26 22 34 18 30 8 M50 30 C46 22 54 18 50 8 M70 30 C66 22 74 18 70 8" fill="none" stroke="#E8574A" stroke-width="3" stroke-linecap="round"/>'),
 "divider": dict(words=["مجزئ الجهد", "التوصيل على التوالي", "دارة التوالي"], anim="buzz", face=(80, 80, .3), only=SC,
   body='<path d="M20 6 L20 94 M80 6 L80 94 M20 6 L80 6 M20 94 L80 94" fill="none" stroke="#3b2a1a" stroke-width="3"/><rect x="72" y="20" width="16" height="24" fill="#F6B73C" {OL}/><rect x="72" y="56" width="16" height="24" fill="#F6B73C" {OL}/>'
        '<rect x="10" y="40" width="20" height="20" fill="#3b3b5c" {OL}/><path d="M80 50 L56 50" stroke="#E8574A" stroke-width="3"/>'),
 "parallel": dict(words=["التوصيل على التوازي", "دارة التوازي"], anim="buzz", face=(50, 50, .3), only=SC,
   body='<path d="M10 10 L90 10 L90 90 L10 90Z M10 50 L90 50" fill="none" stroke="#3b2a1a" stroke-width="3"/><circle cx="50" cy="10" r="8" fill="#FFD25A" {OL}/><circle cx="50" cy="50" r="8" fill="#FFD25A" {OL}/>'
        '<rect x="2" y="66" width="16" height="14" fill="#3b3b5c" {OL}/>'),
 "breaker": dict(words=["قاطع التسرب الأرضي", "القاطع الكهربائي", "المصهر", "الفيوز"], anim="wobble", face=(50, 76, .32), only=SC,
   body='<rect x="22" y="6" width="56" height="88" rx="6" fill="#fff" {OL}/><rect x="40" y="24" width="20" height="30" rx="4" fill="#3b3b5c" {OL}/><rect x="42" y="26" width="16" height="12" rx="2" fill="#6CC27A"/>'
        '<path d="M34 64 L66 64" stroke="#AEB8C4" stroke-width="3"/><path d="M58 70 L50 82 L58 82 L50 92" fill="none" stroke="#FFD25A" stroke-width="3"/>'),
 "tesla": dict(words=["التسلا", "شدة المجال المغناطيسي", "الفيض المغناطيسي"], anim="sun", face=(50, 50, .3), only=SC,
   body='<path d="M6 50 C6 10 94 10 94 50 C94 90 6 90 6 50Z M22 50 C22 24 78 24 78 50 C78 76 22 76 22 50Z" fill="none" stroke="#6CB8FF" stroke-width="2.6"/>'
        '<rect x="30" y="40" width="20" height="20" fill="#E8574A" {OL}/><rect x="50" y="40" width="20" height="20" fill="#6CB8FF" {OL}/><text direction="ltr" x="50" y="94" text-anchor="middle" font-size="12" font-weight="800" fill="#3b2a1a" font-family="sans-serif">T</text>'),
 "ac_dc": dict(words=["التيار المتناوب", "التيار المتردد", "التيار المستمر", "القيمة الفعالة للتيار والجهد", "التيار المباشر"], anim="sway", face=(80, 80, .3), only=SC,
   body='<path d="M4 30 L96 30" stroke="#E8574A" stroke-width="5" stroke-linecap="round"/>'
        '<path d="M4 70 C14 46 24 46 30 70 C36 94 46 94 52 70 C58 46 68 46 74 70 C80 94 90 94 96 70" fill="none" stroke="#6CB8FF" stroke-width="5" stroke-linecap="round"/>'
        '<text direction="ltr" x="22" y="22" text-anchor="middle" font-size="11" font-weight="800" fill="#E8574A" font-family="sans-serif">DC</text><text direction="ltr" x="22" y="52" text-anchor="middle" font-size="11" font-weight="800" fill="#6CB8FF" font-family="sans-serif">AC</text>'),
 "eddy": dict(words=["التيارات الدوامية", "تيارات فوكو"], anim="sun", face=(50, 86, .3), only=SC,
   body='<rect x="10" y="20" width="80" height="60" rx="4" fill="#C9D2DC" {OL}/><path d="M34 50 C34 40 46 38 48 46 C50 54 40 58 36 52 M66 50 C66 40 54 38 52 46 C50 54 60 58 64 52" fill="none" stroke="#E8574A" stroke-width="3" stroke-linecap="round"/>'
        '<path d="M50 4 L50 18 M44 12 L50 18 L56 12" fill="none" stroke="#6CB8FF" stroke-width="3"/>'),
 "inductor": dict(words=["الحث الذاتي", "الحث المتبادل", "الملف الكهربائي", "المحث"], anim="buzz", face=(50, 86, .3), only=SC,
   body='<path d="M4 50 L16 50 C16 30 32 30 32 50 C32 30 48 30 48 50 C48 30 64 30 64 50 C64 30 80 30 80 50 L96 50" fill="none" stroke="#E8853C" stroke-width="5" stroke-linecap="round"/>'
        '<path d="M16 50 C16 66 32 66 32 50 M32 50 C32 66 48 66 48 50 M48 50 C48 66 64 66 64 50 M64 50 C64 66 80 66 80 50" fill="none" stroke="#B5651D" stroke-width="3" stroke-dasharray="3 3"/>'),
 "transformer": dict(words=["المحول الرافع", "المحول الخافض", "المحولات"], anim="buzz", face=(50, 50, .3), only=SC,
   body='<rect x="16" y="16" width="68" height="68" rx="4" fill="none" stroke="#5D646E" stroke-width="12"/>'
        '<path d="M10 28 L22 24 M10 38 L22 34 M10 48 L22 44 M10 58 L22 54" stroke="#E8853C" stroke-width="4"/><path d="M78 24 L90 28 M78 32 L90 36 M78 40 L90 44 M78 48 L90 52 M78 56 L90 60 M78 64 L90 68 M78 72 L90 76" stroke="#E8853C" stroke-width="4"/>'),
 "antenna": dict(words=["الموجات الكهرومغناطيسية", "موجات الراديو", "البث"], anim="buzz", face=(50, 70, .32), only=SC,
   body='<path d="M50 30 L30 94 M50 30 L70 94 M38 66 L62 66 M34 80 L66 80" fill="none" stroke="#5D646E" stroke-width="4" stroke-linecap="round"/><circle cx="50" cy="26" r="6" fill="#E8574A" {OL}/>'
        '<path d="M34 16 C28 22 28 30 34 36 M66 16 C72 22 72 30 66 36 M24 8 C14 18 14 34 24 44 M76 8 C86 18 86 34 76 44" fill="none" stroke="#6CB8FF" stroke-width="3" stroke-linecap="round"/>'),
 # ---------- the modern atom ----------
 "compton": dict(words=["تأثير كومبتون"], anim="bounce", face=(70, 40, .3), only=SC,
   body='<path d="M4 60 C10 50 14 70 20 60 C26 50 30 70 36 60 C42 50 46 70 52 60" fill="none" stroke="#FFD25A" stroke-width="4"/><circle cx="62" cy="60" r="8" fill="#6CB8FF" {OL}/>'
        '<path d="M70 52 L92 24 M84 24 L92 24 L92 32" fill="none" stroke="#6CB8FF" stroke-width="3"/><path d="M68 66 C72 74 78 70 80 78 C82 86 88 82 92 90" fill="none" stroke="#E8853C" stroke-width="3"/>'),
 "uncertainty": dict(words=["مبدأ عدم التحديد لهايزنبرج", "مبدأ عدم اليقين", "ميكانيكا الكم"], anim="wiggle", face=(50, 50, .36), only=SC,
   body='<circle cx="50" cy="50" r="40" fill="#BFE3F2" opacity=".5"/><circle cx="50" cy="50" r="28" fill="#BFE3F2" opacity=".6"/><circle cx="50" cy="50" r="16" fill="#6CB8FF" {OL}/>'
        '<text direction="ltr" x="84" y="22" text-anchor="middle" font-size="22" font-weight="800" fill="#E8574A" font-family="sans-serif">?</text>'),
 "electron_wave": dict(words=["حيود الإلكترونات", "الطبيعة الموجية للجسيمات", "ازدواجية الموجة والجسيم"], anim="sway", face=(16, 50, .3), only=SC,
   body='<circle cx="16" cy="50" r="10" fill="#6CB8FF" {OL}/><path d="M30 50 C36 34 42 34 48 50 C54 66 60 66 66 50 C72 34 78 34 84 50 C88 60 92 60 96 54" fill="none" stroke="#6CB8FF" stroke-width="4" stroke-linecap="round"/>'),
 "laser": dict(words=["الليزر", "الانبعاث المستحث", "شعاع الليزر"], anim="buzz", face=(26, 50, .34), only=SC,
   body='<rect x="4" y="34" width="48" height="32" rx="6" fill="#AEB8C4" {OL}/><rect x="52" y="44" width="8" height="12" fill="#5D646E" {OL}/><path d="M60 50 L96 50" stroke="#E8574A" stroke-width="6" stroke-linecap="round"/>'
        '<path d="M60 50 L96 50" stroke="#FFB3A8" stroke-width="2"/>'),
 "bands": dict(words=["نظرية الحزم", "حزمة التكافؤ", "حزمة التوصيل", "فجوة الطاقة", "أشباه الموصلات"], anim="bob", face=(50, 50, .3), only=SC,
   body='<rect x="10" y="10" width="80" height="22" rx="3" fill="#BFE3F2" {OL}/><rect x="10" y="68" width="80" height="22" rx="3" fill="#6CB8FF" {OL}/>'
        '<path d="M30 64 L30 38 M24 44 L30 36 L36 44" fill="none" stroke="#E8574A" stroke-width="3"/><circle cx="30" cy="20" r="4" fill="#E8574A"/><circle cx="50" cy="79" r="4" fill="#3b2a1a"/><circle cx="66" cy="79" r="4" fill="#3b2a1a"/>'),
 "diode": dict(words=["الثنائي (الدايود)", "الدايود", "الوصلة الثنائية p-n", "الانحياز الأمامي", "الانحياز العكسي", "المقوم", "الثنائي الباعث للضوء"], anim="buzz", face=(30, 78, .3), only=SC,
   body='<path d="M4 50 L36 50 M64 50 L96 50" stroke="#3b2a1a" stroke-width="4"/><path d="M36 26 L36 74 L64 50Z" fill="#E8574A" {OL}/><path d="M64 26 L64 74" stroke="#3b2a1a" stroke-width="6"/>'),
 "transistor": dict(words=["الترانزستور", "الترانزستورات", "الدوائر المتكاملة"], anim="buzz", face=(50, 30, .32), only=SC,
   body='<path d="M28 12 C28 4 72 4 72 12 L72 50 L28 50Z" fill="#3b3b5c" {OL}/><path d="M36 50 L36 94 M50 50 L50 94 M64 50 L64 94" stroke="#AEB8C4" stroke-width="5" stroke-linecap="round"/>'),
 "nucleon": dict(words=["النيوكليون", "النيوكليونات", "مكونات النواة", "طاقة الربط النووية"], anim="wobble", face=(50, 50, .36), only=SC,
   body='<circle cx="40" cy="36" r="14" fill="#E8574A" {OL}/><circle cx="62" cy="38" r="14" fill="#AEB8C4" {OL}/><circle cx="34" cy="60" r="14" fill="#AEB8C4" {OL}/><circle cx="58" cy="62" r="14" fill="#E8574A" {OL}/><circle cx="48" cy="48" r="14" fill="#E8574A" {OL}/>'),
 "decay": dict(words=["اضمحلال ألفا", "اضمحلال بيتا", "الاضمحلال الإشعاعي", "النشاط الإشعاعي", "عمر النصف"], anim="buzz", face=(36, 50, .34), only=SC,
   body='<circle cx="36" cy="50" r="26" fill="#9CD86C" {OL}/><circle cx="28" cy="42" r="6" fill="#E8574A"/><circle cx="42" cy="46" r="6" fill="#AEB8C4"/><circle cx="32" cy="58" r="6" fill="#AEB8C4"/><circle cx="46" cy="60" r="6" fill="#E8574A"/>'
        '<path d="M64 40 L86 22 M64 60 L92 72" stroke="#E8574A" stroke-width="3" stroke-dasharray="4 3"/><circle cx="90" cy="18" r="6" fill="#FFD25A" {OL}/><circle cx="94" cy="74" r="4" fill="#6CB8FF" {OL}/>'),
 "quarks": dict(words=["الكواركات", "اللبتونات", "النيوترينو", "النموذج المعياري", "الجسيمات الأولية"], anim="wobble", face=(50, 50, .3), only=SC,
   body='<circle cx="50" cy="50" r="44" fill="#fff" {OL}/><circle cx="50" cy="30" r="12" fill="#E8574A" {OL}/><circle cx="32" cy="62" r="12" fill="#6CC27A" {OL}/><circle cx="68" cy="62" r="12" fill="#6CB8FF" {OL}/>'
        '<path d="M50 42 L36 54 M50 42 L64 54 M44 62 L56 62" stroke="#3b2a1a" stroke-width="2" stroke-dasharray="3 2"/>'),
}
ALIAS_ONLY = None
ALIASES = {"الهوائي": ("phys.antenna", ("physics",)), "الهوائيات": ("phys.antenna", ("physics",)), "الانشطار النووي": ("mat.nuclear", ("science",)), "الاندماج النووي": ("mat.nuclear", ("science",)), "التطعيم (الإشابة)": ("phys.bands", ("physics",)), "الإشابة": ("phys.bands", ("physics",)), "السعة": ("phys.crest_trough", ("physics", "science")), "الجسم": ("phys.focus_lens", ("physics",)),
           "الصورة": ("phys.lens_image", ("physics",)), "الفيزياء": ("phys.si_units", ("physics",))}
