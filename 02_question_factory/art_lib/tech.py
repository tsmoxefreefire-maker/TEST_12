"""🆕 batch 43 · the digital skills (المهارات الرقمية): block programming (looks, events, sensing, control), the spreadsheet's references,
the web (tags, paragraphs, tables, style sheets, the responsive page), images (pixels, layers, selection, retouching), design and
marketing, devices (router, modem, micro-controller and its LED matrix, the smart speaker, the self-driving car, VR and AR),
data structures (stack, queue, tree, recursion, dictionary, nested lists), machine learning (with and without labels,
clustering, bias, language models), how code runs (compiler and interpreter, versions, the IDE), and cyber-safety.
No brand logos: a word processor is a page, a spreadsheet a grid, a board just a board."""
F = "tech"
DG = ["digital"]
D = {
 # ---------- block programming ----------
 "block_looks": dict(words=["لبنات المظهر", "لبنات الصوت", "لبنات القلم"], anim="wiggle", face=(40, 50, .36), only=DG,
   body='<path d="M6 30 L22 30 L26 36 L36 36 L40 30 L94 30 L94 70 L40 70 L36 76 L26 76 L22 70 L6 70Z" fill="#9B6CD9" {OL}/><path d="M50 44 L84 44 M50 56 L76 56" stroke="#fff" stroke-width="4" stroke-linecap="round"/>'),
 "block_events": dict(words=["لبنات الأحداث", "عند نقر العلم", "الأحداث في البرمجة"], anim="bounce", face=(64, 60, .34), only=DG,
   body='<path d="M6 40 C6 20 50 18 54 34 L94 34 L94 80 L40 80 L36 86 L26 86 L22 80 L6 80Z" fill="#FFC23D" {OL}/><path d="M18 62 L18 44 M18 44 L32 46 L24 52 L32 58 L18 56" fill="#6CC27A" stroke="#3b2a1a" stroke-width="2"/>'),
 "block_sensing": dict(words=["لبنات الاستشعار", "الاستشعار في البرمجة"], anim="sway", face=(36, 50, .34), only=DG,
   body='<path d="M6 30 L22 30 L26 36 L36 36 L40 30 L94 30 L94 70 L40 70 L36 76 L26 76 L22 70 L6 70Z" fill="#5CB1D6" {OL}/><circle cx="70" cy="50" r="12" fill="#fff" {OL}/><circle cx="70" cy="50" r="4" fill="#3b2a1a"/>'),
 "block_control": dict(words=["لبنات التحكم", "التحكم في البرنامج", "أوامر التحكم"], anim="bob", face=(50, 34, .34), only=DG,
   body='<path d="M6 14 L94 14 L94 30 L30 30 L30 62 L94 62 L94 80 L6 80Z" fill="#F6A23C" {OL}/><path d="M40 46 L70 46" stroke="#fff" stroke-width="4"/><path d="M70 40 L78 46 L70 52" fill="none" stroke="#fff" stroke-width="3"/>'),
 # ---------- spreadsheets, files, the web ----------
 "cell_ref": dict(words=["المرجع النسبي", "المرجع المطلق", "مرجع الخلية", "الخلية النشطة"], anim="bob", face=(70, 76, .3), only=DG,
   body='<rect x="6" y="10" width="88" height="80" rx="4" fill="#fff" {OL}/><path d="M6 30 L94 30 M6 50 L94 50 M6 70 L94 70 M30 10 L30 90 M58 10 L58 90" stroke="#AEB8C4" stroke-width="2"/>'
        '<rect x="30" y="30" width="28" height="20" fill="none" stroke="#3E8E4C" stroke-width="4"/><text direction="ltr" x="44" y="45" text-anchor="middle" font-size="11" font-weight="800" fill="#3E8E4C" font-family="sans-serif">$A$1</text>'),
 "router": dict(words=["الموجّه", "الموجه", "جهاز التوجيه"], anim="buzz", face=(50, 72, .3), only=DG,
   body='<rect x="8" y="54" width="84" height="30" rx="8" fill="#3b3b5c" {OL}/><circle cx="24" cy="70" r="3" fill="#6CC27A"/><circle cx="36" cy="70" r="3" fill="#6CC27A"/><circle cx="48" cy="70" r="3" fill="#FFD25A"/>'
        '<path d="M22 54 L16 22 M78 54 L84 22" stroke="#3b2a1a" stroke-width="4" stroke-linecap="round"/><path d="M40 30 C46 24 54 24 60 30 M34 22 C44 12 56 12 66 22" fill="none" stroke="#6CB8FF" stroke-width="3" stroke-linecap="round"/>'),
 "modem": dict(words=["المودم", "الاتصال بالإنترنت", "مزود خدمة الإنترنت"], anim="buzz", face=(50, 54, .32), only=DG,
   body='<rect x="16" y="20" width="68" height="64" rx="8" fill="#E8F2F8" {OL}/><rect x="16" y="20" width="68" height="14" rx="6" fill="#AEB8C4" {OL}/><circle cx="30" cy="27" r="2.6" fill="#6CC27A"/><circle cx="42" cy="27" r="2.6" fill="#6CC27A"/><circle cx="54" cy="27" r="2.6" fill="#E8574A"/>'
        '<path d="M50 84 L50 96 L80 96" fill="none" stroke="#3b2a1a" stroke-width="3"/>'),
 "backup": dict(words=["النسخ الاحتياطي", "النسخة الاحتياطية", "استعادة البيانات"], anim="bob", face=(50, 46, .34), only=DG,
   body='<path d="M20 60 C6 60 6 38 22 38 C24 20 52 16 58 32 C70 24 90 32 86 48 C98 50 96 70 82 70 L24 70 C22 70 20 66 20 60Z" fill="#BFE3F2" {OL}/>'
        '<path d="M50 74 L50 96 M42 84 L50 76 L58 84" fill="none" stroke="#3E8E4C" stroke-width="4" stroke-linecap="round"/><rect x="66" y="80" width="26" height="16" rx="3" fill="#AEB8C4" {OL}/>'),
 "db_relations": dict(words=["العلاقات", "المفتاح الأجنبي"], anim="wiggle", face=(50, 86, .3), only=DG,
   body='<rect x="4" y="14" width="38" height="50" rx="4" fill="#fff" {OL}/><rect x="4" y="14" width="38" height="12" rx="4" fill="#6CB8FF" {OL}/><path d="M4 38 L42 38 M4 50 L42 50" stroke="#AEB8C4" stroke-width="2"/>'
        '<rect x="58" y="30" width="38" height="50" rx="4" fill="#fff" {OL}/><rect x="58" y="30" width="38" height="12" rx="4" fill="#F6B73C" {OL}/><path d="M58 54 L96 54 M58 66 L96 66" stroke="#AEB8C4" stroke-width="2"/>'
        '<path d="M42 44 C50 44 50 60 58 60" fill="none" stroke="#E8574A" stroke-width="3"/>'),
 "criteria": dict(words=["المعايير", "معايير التقييم", "قائمة التحقق"], anim="bob", face=(30, 74, .3), only=DG + ["thinking"],
   body='<rect x="10" y="8" width="70" height="86" rx="6" fill="#fff" {OL}/><rect x="30" y="2" width="30" height="12" rx="4" fill="#AEB8C4" {OL}/>'
        '<path d="M20 30 L26 36 L36 24 M20 52 L26 58 L36 46" fill="none" stroke="#6CC27A" stroke-width="4" stroke-linecap="round"/><path d="M44 30 L70 30 M44 52 L70 52 M44 74 L70 74" stroke="#3b2a1a" stroke-width="3" stroke-linecap="round"/><rect x="20" y="68" width="12" height="12" fill="none" stroke="#3b2a1a" stroke-width="2"/>'),
 "eshop": dict(words=["المتجر الإلكتروني", "قالب المتجر", "التجارة الإلكترونية", "المتاجر الإلكترونية", "الطلبات"], anim="bounce", face=(50, 46, .3), only=DG + ["finance"],
   body='<rect x="6" y="8" width="88" height="66" rx="6" fill="#3b3b5c" {OL}/><rect x="12" y="14" width="76" height="54" rx="3" fill="#fff"/><path d="M12 14 L88 14 L84 28 L16 28Z" fill="#E8574A"/>'
        '<path d="M30 40 L36 40 L42 58 L66 58 L70 44 L38 44" fill="none" stroke="#3b2a1a" stroke-width="3" stroke-linejoin="round"/><circle cx="46" cy="62" r="3" fill="#3b2a1a"/><circle cx="62" cy="62" r="3" fill="#3b2a1a"/><path d="M40 74 L60 74 L66 90 L34 90Z" fill="#AEB8C4" {OL}/>'),
 "shipping": dict(words=["الشحن", "التوصيل", "شحن الطلبات", "خدمات التوصيل"], anim="bounce", face=(36, 50, .32), only=DG + ["finance", "english"],
   body='<rect x="4" y="30" width="58" height="40" rx="4" fill="#F6B73C" {OL}/><path d="M62 42 L82 42 L94 56 L94 70 L62 70Z" fill="#6CB8FF" {OL}/><circle cx="22" cy="76" r="9" fill="#3b3b5c" {OL}/><circle cx="78" cy="76" r="9" fill="#3b3b5c" {OL}/>'
        '<rect x="20" y="10" width="26" height="20" fill="#C98A55" {OL}/><path d="M33 10 L33 30" stroke="#8B5E3C" stroke-width="2"/>'),
 "list_ds": dict(words=["القائمة", "القوائم", "القوائم المتداخلة", "القوائم في بايثون"], anim="bob", face=(70, 70, .3), only=DG,
   body='<rect x="8" y="16" width="84" height="20" rx="4" fill="#fff" {OL}/><path d="M30 16 L30 36 M52 16 L52 36 M74 16 L74 36" stroke="#3b2a1a" stroke-width="2"/>'
        '<rect x="30" y="50" width="62" height="20" rx="4" fill="#E8F2F8" {OL}/><path d="M52 50 L52 70 M74 50 L74 70" stroke="#3b2a1a" stroke-width="2"/><path d="M41 36 L41 60 L30 60" fill="none" stroke="#E8574A" stroke-width="2.4"/>'
        '<text direction="ltr" x="8" y="94" font-size="14" font-weight="800" fill="#3b2a1a" font-family="monospace">[ , , ]</text>'),
 "import_mod": dict(words=["الاستيراد import", "الاستيراد", "المكتبات البرمجية", "الوحدات البرمجية"], anim="bounce", face=(66, 66, .3), only=DG,
   body='<path d="M40 40 L92 40 L92 92 L40 92Z" fill="#C98A55" {OL}/><path d="M40 40 L52 28 L104 28 L92 40" fill="#E6C08A" {OL}/><path d="M6 20 L34 50 M22 50 L34 50 L34 38" fill="none" stroke="#3E8E4C" stroke-width="5" stroke-linecap="round"/>'),
 "ui_button": dict(words=["الأزرار", "الزر", "زر الأمر", "عناصر الواجهة", "واجهة التطبيق", "واجهة المستخدم"], anim="bounce", face=(50, 44, .3), only=DG,
   body='<rect x="10" y="26" width="80" height="36" rx="18" fill="#6CB8FF" {OL}/><path d="M60 70 L60 96 L66 88 L72 98 L76 96 L70 86 L80 86Z" fill="#fff" {OL}/>'),
 "dictionary_ds": dict(words=["القاموس", "القواميس", "المفتاح والقيمة"], anim="bob", face=(50, 76, .3), only=DG,
   body='<rect x="10" y="12" width="80" height="76" rx="6" fill="#9B6CD9" {OL}/><rect x="16" y="18" width="68" height="64" rx="3" fill="#fff"/>'
        '<text direction="ltr" x="50" y="44" text-anchor="middle" font-size="16" font-weight="800" fill="#3b2a1a" font-family="monospace">{k:v}</text>'),
 "repair_pc": dict(words=["الأعطال الشائعة", "صيانة الحاسب", "الصيانة", "حل المشكلات التقنية"], anim="wobble", face=(36, 42, .32), only=DG,
   body='<rect x="6" y="14" width="62" height="46" rx="4" fill="#3b3b5c" {OL}/><rect x="11" y="19" width="52" height="36" fill="#BFE3F2"/><path d="M26 30 L46 46 M46 30 L26 46" stroke="#E8574A" stroke-width="3"/>'
        '<path d="M66 92 L84 62 C78 56 82 44 92 46 L86 54 L92 58 L98 52 C100 62 92 68 86 66 L70 96Z" fill="#AEB8C4" {OL}/>'),
 "sync": dict(words=["المزامنة", "مزامنة البيانات", "التحديث التلقائي"], anim="sun", face=(50, 50, .34), only=DG,
   body='<path d="M20 44 C24 24 46 14 64 22 L60 30 L80 30 L76 10 L70 18 C48 6 18 18 12 44Z" fill="#6CB8FF" {OL}/><path d="M80 56 C76 76 54 86 36 78 L40 70 L20 70 L24 90 L30 82 C52 94 82 82 88 56Z" fill="#6CC27A" {OL}/>'),
 "protocol": dict(words=["البروتوكول", "بروتوكول MQTT", "بروتوكول الاتصال"], anim="wiggle", face=(50, 30, .3), only=DG,
   body='<rect x="2" y="54" width="34" height="26" rx="3" fill="#3b3b5c" {OL}/><rect x="64" y="54" width="34" height="26" rx="3" fill="#3b3b5c" {OL}/><path d="M36 60 L64 60 M58 54 L64 60 L58 66 M64 74 L36 74 M42 68 L36 74 L42 80" fill="none" stroke="#E8574A" stroke-width="3"/>'
        '<path d="M30 30 L70 30 L70 44 L30 44Z" fill="#FFF3C4" {OL}/><path d="M36 37 L64 37" stroke="#3b2a1a" stroke-width="2"/>'),
 "client_server": dict(words=["الخادم والعميل", "الخادم", "الخوادم", "العميل"], anim="buzz", face=(26, 30, .3), only=DG,
   body='<rect x="10" y="8" width="32" height="84" rx="4" fill="#5D646E" {OL}/><path d="M16 22 L36 22 M16 36 L36 36 M16 50 L36 50" stroke="#AEB8C4" stroke-width="3"/><circle cx="32" cy="70" r="3" fill="#6CC27A"/>'
        '<rect x="58" y="50" width="38" height="26" rx="3" fill="#3b3b5c" {OL}/><rect x="62" y="54" width="30" height="18" fill="#BFE3F2"/><path d="M54 80 L100 80" stroke="#3b2a1a" stroke-width="4"/><path d="M42 40 L58 56" stroke="#E8574A" stroke-width="2.6" stroke-dasharray="4 3"/>'),
 "video_meeting": dict(words=["الاجتماع المرئي", "مايكروسوفت تيمز", "الاجتماعات عن بعد", "التعلم عن بعد", "الفصول الافتراضية"], anim="bob", face=(32, 34, .3), only=DG,
   body='<rect x="4" y="10" width="92" height="70" rx="6" fill="#3b3b5c" {OL}/><rect x="10" y="16" width="38" height="28" rx="3" fill="#BFE3F2"/><rect x="52" y="16" width="38" height="28" rx="3" fill="#FFF3C4"/><rect x="10" y="48" width="38" height="26" rx="3" fill="#E6F4D8"/><rect x="52" y="48" width="38" height="26" rx="3" fill="#FBE9E7"/>'
        '<circle cx="71" cy="30" r="6" fill="#F7C9A4"/><circle cx="29" cy="60" r="6" fill="#F7C9A4"/><circle cx="71" cy="60" r="6" fill="#F7C9A4"/><path d="M40 80 L60 80 L64 92 L36 92Z" fill="#AEB8C4" {OL}/>'),
 "digital_notes": dict(words=["تدوين الملاحظات الرقمية", "الملاحظات الرقمية", "تطبيقات الملاحظات"], anim="bob", face=(40, 62, .32), only=DG,
   body='<rect x="16" y="6" width="56" height="88" rx="8" fill="#3b3b5c" {OL}/><rect x="21" y="14" width="46" height="70" rx="3" fill="#FFF3C4"/><path d="M28 30 L60 30 M28 42 L56 42 M28 54 L60 54" stroke="#C98A55" stroke-width="2.4"/>'
        '<path d="M74 70 L92 30 L98 32 L80 72 L72 78Z" fill="#6CB8FF" {OL}/>'),
 "actuator": dict(words=["المشغلات", "المحرك الكهربائي"], anim="sun", face=(36, 50, .32), only=DG,
   body='<rect x="8" y="30" width="56" height="40" rx="8" fill="#AEB8C4" {OL}/><path d="M64 50 L80 50" stroke="#3b2a1a" stroke-width="6"/><circle cx="84" cy="50" r="12" fill="#F6B73C" {OL}/><path d="M84 38 L84 62 M72 50 L96 50" stroke="#3b2a1a" stroke-width="2"/>'
        '<path d="M20 70 L20 84 M52 70 L52 84" stroke="#E8574A" stroke-width="3"/>'),
 "vr": dict(words=["الواقع الافتراضي", "نظارة الواقع الافتراضي"], anim="bob", face=None, only=DG,
   body='<rect x="8" y="30" width="84" height="40" rx="14" fill="#3b3b5c" {OL}/><rect x="16" y="38" width="30" height="24" rx="8" fill="#6CB8FF"/><rect x="54" y="38" width="30" height="24" rx="8" fill="#6CB8FF"/>'
        '<path d="M8 46 C0 46 0 30 10 24 M92 46 C100 46 100 30 90 24" fill="none" stroke="#3b2a1a" stroke-width="4"/><path d="M22 44 L30 44 M60 44 L68 44" stroke="#fff" stroke-width="3" stroke-linecap="round"/>'),
 "ar": dict(words=["الواقع المعزز", "تطبيقات الواقع المعزز"], anim="bounce", face=(40, 58, .3), only=DG,
   body='<rect x="16" y="20" width="48" height="76" rx="8" fill="#3b3b5c" {OL}/><rect x="21" y="28" width="38" height="58" rx="3" fill="#E6F4D8"/>'
        '<path d="M40 36 L58 46 L58 66 L40 76 L22 66 L22 46Z" fill="#F6B73C" opacity=".9" {OL}/><path d="M60 40 L88 22 M88 22 L80 22 M88 22 L86 30" stroke="#6CB8FF" stroke-width="3" fill="none"/><path d="M76 12 L80 6 L84 12" fill="none" stroke="#6CB8FF" stroke-width="2.4"/>'),
 "blockchain": dict(words=["سلسلة الكتل", "البلوك تشين", "العملات الرقمية"], anim="wiggle", face=(50, 50, .3), only=DG + ["finance"],
   body='<rect x="2" y="34" width="26" height="26" rx="4" fill="#6CB8FF" {OL}/><rect x="37" y="34" width="26" height="26" rx="4" fill="#6CC27A" {OL}/><rect x="72" y="34" width="26" height="26" rx="4" fill="#F6B73C" {OL}/>'
        '<path d="M28 47 L37 47 M63 47 L72 47" stroke="#3b2a1a" stroke-width="4"/><path d="M45 34 L45 28 C45 22 55 22 55 28 L55 34" fill="none" stroke="#3b2a1a" stroke-width="2.4"/>'),
 "html_tags": dict(words=["لغة HTML", "الوسوم", "وسوم التنسيق", "صفحات الويب", "تصميم صفحات الويب"], anim="bob", face=(50, 76, .3), only=DG,
   body='<rect x="6" y="12" width="88" height="76" rx="6" fill="#fff" {OL}/><rect x="6" y="12" width="88" height="14" rx="6" fill="#E8853C" {OL}/>'
        '<text direction="ltr" x="50" y="58" text-anchor="middle" font-size="22" font-weight="800" fill="#E8574A" font-family="monospace">&lt;/&gt;</text>'),
 "paragraph": dict(words=["الفقرات", "الفقرة", "تنسيق الفقرات"], anim="bob", face=(70, 74, .3), only=DG,
   body='<rect x="6" y="10" width="88" height="80" rx="4" fill="#fff" {OL}/><path d="M16 26 L84 26 M16 38 L84 38 M16 50 L70 50 M16 66 L84 66 M16 78 L60 78" stroke="#AEB8C4" stroke-width="3" stroke-linecap="round"/>'
        '<text direction="ltr" x="80" y="58" font-size="18" font-weight="800" fill="#6CB8FF" font-family="serif">¶</text>'),
 "table_ui": dict(words=["الجداول", "إدراج جدول", "الجداول في صفحات الويب"], anim="bob", face=(50, 50, .3), only=DG,
   body='<rect x="6" y="14" width="88" height="72" rx="4" fill="#fff" {OL}/><rect x="6" y="14" width="88" height="16" rx="4" fill="#6CB8FF" {OL}/><path d="M6 48 L94 48 M6 66 L94 66 M36 14 L36 86 M66 14 L66 86" stroke="#3b2a1a" stroke-width="2"/>'),
 "css": dict(words=["صفحات التنسيق النمطية CSS", "التنسيق النمطي", "تنسيق الصفحات"], anim="wiggle", face=(34, 66, .3), only=DG,
   body='<rect x="6" y="40" width="58" height="52" rx="6" fill="#fff" {OL}/><path d="M14 54 L52 54 M14 66 L44 66 M14 78 L50 78" stroke="#6CB8FF" stroke-width="3" stroke-linecap="round"/>'
        '<path d="M60 44 L88 8 L96 14 L70 50Z" fill="#C98A55" {OL}/><path d="M60 44 C52 46 50 56 58 60 C64 62 70 56 70 50Z" fill="#E8574A" {OL}/>'),
 "responsive": dict(words=["التصميم المستجيب", "التصميم المتجاوب", "تصميم يناسب كل الشاشات"], anim="bounce", face=(36, 40, .3), only=DG,
   body='<rect x="4" y="14" width="60" height="44" rx="4" fill="#3b3b5c" {OL}/><rect x="8" y="18" width="52" height="36" fill="#BFE3F2"/><path d="M24 58 L44 58 L48 68 L20 68Z" fill="#AEB8C4" {OL}/>'
        '<rect x="56" y="38" width="28" height="42" rx="4" fill="#5A5A7C" {OL}/><rect x="59" y="42" width="22" height="32" fill="#E6F4D8"/><rect x="84" y="54" width="14" height="26" rx="3" fill="#3b3b5c" {OL}/><rect x="86" y="58" width="10" height="18" fill="#FFF3C4"/>'),
 "js_code": dict(words=["جافا سكريبت", "لغة ++C", "لغة بايثون", "لغة C"], anim="bob", face=(50, 72, .3), only=DG,
   body='<rect x="8" y="10" width="84" height="80" rx="8" fill="#2A2F45" {OL}/><path d="M18 30 L28 30 M34 30 L60 30 M18 42 L46 42 M26 54 L56 54 M26 66 L48 66" stroke="#9CD86C" stroke-width="4" stroke-linecap="round"/><path d="M62 42 L80 42" stroke="#F6B73C" stroke-width="4" stroke-linecap="round"/>'),
 "app_mobile": dict(words=["تطبيق الجوال", "تطبيقات الهواتف", "تطوير التطبيقات", "التطبيقات"], anim="bob", face=(50, 76, .3), only=DG + ["english"],
   body='<rect x="22" y="4" width="56" height="92" rx="10" fill="#3b3b5c" {OL}/><rect x="27" y="12" width="46" height="74" rx="4" fill="#fff"/>'
        '<rect x="32" y="18" width="14" height="14" rx="4" fill="#E8574A"/><rect x="54" y="18" width="14" height="14" rx="4" fill="#6CB8FF"/><rect x="32" y="38" width="14" height="14" rx="4" fill="#6CC27A"/><rect x="54" y="38" width="14" height="14" rx="4" fill="#FFD25A"/>'),
 "pixel": dict(words=["البكسل", "البكسلات", "دقة الصورة"], anim="bob", face=(50, 50, .3), only=DG,
   body='<rect x="10" y="10" width="80" height="80" fill="#fff" {OL}/><rect x="10" y="10" width="20" height="20" fill="#E8574A"/><rect x="30" y="10" width="20" height="20" fill="#F6B73C"/><rect x="50" y="30" width="20" height="20" fill="#6CB8FF"/><rect x="70" y="50" width="20" height="20" fill="#6CC27A"/><rect x="30" y="70" width="20" height="20" fill="#9B6CD9"/>'
        '<path d="M30 10 L30 90 M50 10 L50 90 M70 10 L70 90 M10 30 L90 30 M10 50 L90 50 M10 70 L90 70" stroke="#AEB8C4" stroke-width="1.4"/><rect x="10" y="10" width="80" height="80" fill="none" {OL}/>'),
 "layer": dict(words=["الطبقة", "طبقات الصورة", "الطبقات في برامج الرسم"], anim="bob", face=(50, 30, .3), only=DG,
   body='<path d="M50 10 L94 30 L50 50 L6 30Z" fill="#6CB8FF" {OL}/><path d="M6 46 L50 66 L94 46 L94 50 L50 70 L6 50Z" fill="#6CC27A" {OL}/><path d="M6 66 L50 86 L94 66 L94 70 L50 90 L6 70Z" fill="#F6B73C" {OL}/>'),
 "selection": dict(words=["أدوات التحديد", "تحديد جزء من الصورة"], anim="wiggle", face=(50, 50, .34), only=DG,
   body='<rect x="6" y="6" width="88" height="88" rx="4" fill="#E6F4D8" {OL}/><rect x="22" y="22" width="56" height="56" fill="none" stroke="#3b2a1a" stroke-width="3" stroke-dasharray="6 4"/>'
        '<path d="M70 70 L70 96 L76 88 L82 98 L86 96 L80 86 L90 86Z" fill="#fff" {OL}/>'),
 "retouch": dict(words=["إزالة العيوب", "تحسين الصور", "أداة الترقيع"], anim="sway", face=(36, 50, .32), only=DG,
   body='<rect x="6" y="20" width="62" height="60" rx="4" fill="#BFE3F2" {OL}/><path d="M6 66 L26 46 L40 60 L52 50 L68 66 L68 80 L6 80Z" fill="#6CC27A"/><circle cx="24" cy="36" r="4" fill="#9C8C7A"/>'
        '<path d="M58 70 L88 14 L96 18 L66 74Z" fill="#C98A55" {OL}/><path d="M58 70 C50 74 52 84 60 82 C66 80 68 76 66 74Z" fill="#F59BB8" {OL}/><path d="M76 34 L80 28 M84 40 L90 36" stroke="#F6B73C" stroke-width="2.4"/>'),
 "formal_letter": dict(words=["الخطاب الرسمي", "المذكرة", "الرسالة الرسمية", "المراسلات الرسمية"], anim="bob", face=(30, 72, .3), only=DG + ["arabic", "life"],
   body='<rect x="8" y="6" width="70" height="88" rx="4" fill="#fff" {OL}/><path d="M18 22 L50 22 M18 36 L68 36 M18 46 L68 46 M18 56 L60 56" stroke="#AEB8C4" stroke-width="2.4"/>'
        '<circle cx="64" cy="78" r="12" fill="#E8574A" {OL}/><path d="M58 78 L70 78 M64 72 L64 84" stroke="#fff" stroke-width="2"/>'),
 "design": dict(words=["مبادئ التصميم", "عناصر التصميم", "التصميم الرسومي", "التصميم", "التصميم الجرافيكي"], anim="wiggle", face=(64, 64, .3), only=DG + ["english", "art"],
   body='<circle cx="30" cy="30" r="18" fill="#E8574A" {OL}/><rect x="52" y="12" width="36" height="36" rx="4" fill="#6CB8FF" {OL}/><path d="M64 56 L90 96 L38 96Z" fill="#FFD25A" {OL}/>'
        '<path d="M8 92 L34 54 L40 58 L14 96Z" fill="#AEB8C4" {OL}/>'),
 "business_model": dict(words=["نماذج الأعمال", "نموذج العمل التجاري", "خطة العمل"], anim="bob", face=(50, 50, .3), only=DG + ["finance"],
   body='<rect x="6" y="14" width="88" height="72" rx="4" fill="#fff" {OL}/><path d="M28 14 L28 62 M50 14 L50 62 M72 14 L72 62 M6 62 L94 62 M50 62 L50 86 M28 38 L50 38 M72 38 L94 38" stroke="#3b2a1a" stroke-width="2"/>'
        '<rect x="54" y="66" width="36" height="16" fill="#9CD86C"/><rect x="10" y="66" width="36" height="16" fill="#FBE9E7"/>'),
 "invoice": dict(words=["الفاتورة", "الفواتير", "الفاتورة الإلكترونية"], anim="bob", face=(40, 74, .3), only=DG + ["finance", "life"],
   body='<path d="M14 6 L78 6 L78 94 L68 88 L58 94 L48 88 L38 94 L28 88 L14 94Z" fill="#fff" {OL}/><path d="M24 22 L56 22 M24 36 L68 36 M24 46 L68 46 M24 56 L68 56" stroke="#AEB8C4" stroke-width="2.4"/>'
        '<path d="M48 70 L68 70" stroke="#3b2a1a" stroke-width="3"/><text direction="ltr" x="30" y="76" font-size="14" font-weight="800" fill="#3E8E4C" font-family="sans-serif">$</text>'),
 "wireless": dict(words=["البلوتوث", "الشبكة اللاسلكية"], anim="buzz", face=(50, 74, .3), only=DG,
   body='<rect x="4" y="50" width="26" height="40" rx="5" fill="#3b3b5c" {OL}/><rect x="70" y="50" width="26" height="40" rx="5" fill="#3b3b5c" {OL}/>'
        '<path d="M38 50 C44 44 56 44 62 50 M32 40 C42 30 58 30 68 40 M26 30 C40 16 60 16 74 30" fill="none" stroke="#6CB8FF" stroke-width="3" stroke-linecap="round"/>'),
 "microcontroller": dict(words=["المتحكم الدقيق", "الأردوينو", "المايكروبت", "مصفوفة الأضواء", "اللوحة الإلكترونية", "لوحة التحكم الدقيق"], anim="buzz", face=(30, 70, .3), only=DG,
   body='<rect x="6" y="14" width="88" height="72" rx="6" fill="#2F8F6A" {OL}/><rect x="40" y="26" width="44" height="44" rx="3" fill="#1F2A44" {OL}/>'
        '<circle cx="48" cy="34" r="2.6" fill="#E8574A"/><circle cx="58" cy="34" r="2.6" fill="#E8574A"/><circle cx="68" cy="34" r="2.6" fill="#3b3b5c"/><circle cx="76" cy="34" r="2.6" fill="#E8574A"/><circle cx="48" cy="46" r="2.6" fill="#3b3b5c"/><circle cx="58" cy="46" r="2.6" fill="#E8574A"/><circle cx="68" cy="46" r="2.6" fill="#E8574A"/><circle cx="76" cy="46" r="2.6" fill="#3b3b5c"/><circle cx="48" cy="58" r="2.6" fill="#E8574A"/><circle cx="58" cy="58" r="2.6" fill="#3b3b5c"/><circle cx="68" cy="58" r="2.6" fill="#E8574A"/><circle cx="76" cy="58" r="2.6" fill="#E8574A"/>'
        '<path d="M10 86 L10 96 M20 86 L20 96 M30 86 L30 96 M40 86 L40 96" stroke="#FFD25A" stroke-width="3"/>'),
 "knowledge": dict(words=["المعرفة", "اكتساب المعرفة", "مجتمع المعرفة"], anim="bob", face=(50, 62, .34), only=DG + ["thinking", "english"],
   body='<path d="M6 30 C24 22 40 24 50 32 C60 24 76 22 94 30 L94 86 C76 78 60 80 50 88 C40 80 24 78 6 86Z" fill="#fff" {OL}/><path d="M50 32 L50 88" stroke="#3b2a1a" stroke-width="2.6"/>'
        '<circle cx="50" cy="16" r="10" fill="#FFD25A" {OL}/><path d="M50 2 L50 0 M36 8 L32 4 M64 8 L68 4" stroke="#F6B73C" stroke-width="3"/>'),
 "predict": dict(words=["التنبؤ", "التوقع", "التنبؤ بالبيانات", "النمذجة التنبؤية"], anim="bounce", face=(36, 70, .3), only=DG,
   body='<path d="M6 90 L94 90 M6 90 L6 8" stroke="#3b2a1a" stroke-width="3"/><path d="M10 80 L28 66 L44 70 L60 50" fill="none" stroke="#6CB8FF" stroke-width="4" stroke-linecap="round"/>'
        '<path d="M60 50 L74 38 L90 20" fill="none" stroke="#E8574A" stroke-width="4" stroke-dasharray="5 4" stroke-linecap="round"/><circle cx="60" cy="50" r="4" fill="#3b2a1a"/>'),
 "regression": dict(words=["الانحدار", "الانحدار الخطي", "خط الاتجاه"], anim="bob", face=(70, 74, .3), only=DG + ["math"],
   body='<path d="M6 92 L94 92 M6 92 L6 6" stroke="#3b2a1a" stroke-width="3"/><circle cx="18" cy="76" r="3.4" fill="#6CB8FF"/><circle cx="30" cy="70" r="3.4" fill="#6CB8FF"/><circle cx="38" cy="58" r="3.4" fill="#6CB8FF"/><circle cx="52" cy="54" r="3.4" fill="#6CB8FF"/><circle cx="62" cy="40" r="3.4" fill="#6CB8FF"/><circle cx="76" cy="34" r="3.4" fill="#6CB8FF"/><circle cx="86" cy="20" r="3.4" fill="#6CB8FF"/>'
        '<path d="M10 84 L92 18" stroke="#E8574A" stroke-width="3"/>'),
 "optimize": dict(words=["التحسين", "تحسين الأداء", "الحل الأمثل"], anim="sun", face=(36, 60, .3), only=DG + ["math"],
   body='<circle cx="36" cy="60" r="24" fill="#AEB8C4" {OL}/><circle cx="36" cy="60" r="9" fill="#fff" {OL}/><path d="M36 30 L36 36 M36 84 L36 90 M6 60 L12 60 M60 60 L66 60 M15 39 L19 43 M53 77 L57 81 M15 81 L19 77 M53 43 L57 39" stroke="#3b2a1a" stroke-width="5" stroke-linecap="round"/>'
        '<path d="M70 50 L84 20 L98 50 M84 20 L84 70" fill="none" stroke="#6CC27A" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>'),
 "smart_health": dict(words=["الصحة الذكية", "الساعة الذكية", "الأجهزة القابلة للارتداء"], anim="bounce", face=(50, 50, .3), only=DG,
   body='<rect x="30" y="2" width="40" height="22" rx="6" fill="#3b3b5c" {OL}/><rect x="30" y="76" width="40" height="22" rx="6" fill="#3b3b5c" {OL}/><rect x="22" y="22" width="56" height="56" rx="14" fill="#5A5A7C" {OL}/>'
        '<rect x="28" y="28" width="44" height="44" rx="10" fill="#1F2A44"/><path d="M30 52 L40 52 L44 42 L50 62 L56 48 L60 52 L70 52" fill="none" stroke="#E8574A" stroke-width="3" stroke-linejoin="round"/>'),
 "challenge": dict(words=["مواجهة التحديات"], anim="bounce", face=(36, 74, .3), only=DG + ["social", "english", "life"],
   body='<path d="M2 94 L40 30 L56 54 L68 40 L98 94Z" fill="#9C8C7A" {OL}/><path d="M40 30 L34 42 L40 40 L46 44Z" fill="#fff" {OL}/>'
        '<path d="M40 30 L40 6" stroke="#3b2a1a" stroke-width="3"/><path d="M40 6 L58 12 L40 18Z" fill="#E8574A" {OL}/>'),
 "alarm": dict(words=["الإنذار", "جهاز الإنذار", "إنذار الحريق", "صافرة الإنذار"], anim="buzz", face=(50, 62, .34), only=DG + ["life"],
   body='<path d="M24 80 L24 50 C24 28 76 28 76 50 L76 80Z" fill="#E8574A" {OL}/><rect x="14" y="80" width="72" height="14" rx="4" fill="#AEB8C4" {OL}/>'
        '<path d="M10 30 L20 36 M90 30 L80 36 M50 4 L50 16 M24 12 L30 22 M76 12 L70 22" stroke="#F6B73C" stroke-width="4" stroke-linecap="round"/>'),
 "ide": dict(words=["بيئة التطوير", "بيئة التطوير المتكاملة", "محرر الأكواد"], anim="bob", face=(70, 70, .3), only=DG,
   body='<rect x="4" y="10" width="92" height="80" rx="6" fill="#2A2F45" {OL}/><rect x="4" y="10" width="92" height="12" rx="6" fill="#5D646E" {OL}/><circle cx="12" cy="16" r="2.4" fill="#E8574A"/><circle cx="20" cy="16" r="2.4" fill="#FFD25A"/><circle cx="28" cy="16" r="2.4" fill="#6CC27A"/>'
        '<rect x="4" y="22" width="20" height="68" fill="#1F2A44"/><path d="M30 34 L60 34 M36 46 L72 46 M36 58 L56 58" stroke="#9CD86C" stroke-width="3" stroke-linecap="round"/><path d="M30 76 L90 76" stroke="#6CB8FF" stroke-width="3"/>'),
 "smart_city": dict(words=["المدينة الذكية", "النقل الذكي", "الحاوية الذكية", "الجهاز الذكي", "الأجهزة المؤتمتة"], anim="buzz", face=(50, 66, .3), only=DG,
   body='<rect x="6" y="40" width="20" height="56" fill="#AEB8C4" {OL}/><rect x="28" y="24" width="24" height="72" fill="#C9D2DC" {OL}/><rect x="54" y="48" width="18" height="48" fill="#AEB8C4" {OL}/><rect x="74" y="32" width="20" height="64" fill="#C9D2DC" {OL}/>'
        '<path d="M34 14 C38 10 42 10 46 14 M30 8 C36 2 44 2 50 8" fill="none" stroke="#6CB8FF" stroke-width="3" stroke-linecap="round"/><circle cx="40" cy="18" r="2.6" fill="#6CB8FF"/>'),
 "self_driving": dict(words=["السيارات ذاتية القيادة", "القيادة الذاتية", "المركبات الذاتية"], anim="bounce", face=(40, 62, .3), only=DG,
   body='<path d="M6 70 L14 50 C18 42 26 40 34 40 L62 40 C70 40 76 44 80 50 L94 56 L94 74 L6 74Z" fill="#6CB8FF" {OL}/><path d="M24 50 L32 44 L58 44 L64 50Z" fill="#E8F6FF" {OL}/>'
        '<circle cx="24" cy="76" r="9" fill="#3b3b5c" {OL}/><circle cx="76" cy="76" r="9" fill="#3b3b5c" {OL}/><path d="M50 34 L50 26 M42 20 C46 16 54 16 58 20 M36 14 C44 6 56 6 64 14" fill="none" stroke="#E8574A" stroke-width="3" stroke-linecap="round"/>'),
 "smart_speaker": dict(words=["المساعد الذكي", "المساعد الصوتي", "الأوامر الصوتية"], anim="buzz", face=(40, 60, .32), only=DG,
   body='<rect x="20" y="20" width="40" height="72" rx="20" fill="#5A5A7C" {OL}/><ellipse cx="40" cy="24" rx="16" ry="5" fill="#6CB8FF" {OL}/><path d="M28 50 L52 50 M28 60 L52 60 M28 70 L52 70" stroke="#8A93A6" stroke-width="2"/>'
        '<path d="M68 40 C74 46 74 56 68 62 M78 32 C88 42 88 60 78 70" fill="none" stroke="#6CB8FF" stroke-width="3" stroke-linecap="round"/>'),
 # ---------- data structures, machine learning, code ----------
 "stack": dict(words=["المكدس", "المكدسات", "الدفع والسحب"], anim="bounce", face=(50, 30, .3), only=DG,
   body='<rect x="22" y="70" width="56" height="16" rx="4" fill="#6CB8FF" {OL}/><rect x="22" y="52" width="56" height="16" rx="4" fill="#6CC27A" {OL}/><rect x="22" y="34" width="56" height="16" rx="4" fill="#F6B73C" {OL}/>'
        '<path d="M50 6 L50 26 M42 18 L50 26 L58 18" fill="none" stroke="#3b2a1a" stroke-width="3"/><path d="M16 90 L84 90" stroke="#3b2a1a" stroke-width="4"/>'),
 "queue": dict(words=["الطابور", "الطوابير", "الطابور في البرمجة"], anim="bounce", face=(86, 44, .3), only=DG,
   body='<circle cx="14" cy="44" r="9" fill="#AEB8C4" {OL}/><path d="M4 80 C4 60 24 60 24 80Z" fill="#AEB8C4" {OL}/><circle cx="38" cy="44" r="9" fill="#9CD86C" {OL}/><path d="M28 80 C28 60 48 60 48 80Z" fill="#9CD86C" {OL}/>'
        '<circle cx="62" cy="44" r="9" fill="#F6B73C" {OL}/><path d="M52 80 C52 60 72 60 72 80Z" fill="#F6B73C" {OL}/><circle cx="86" cy="44" r="9" fill="#6CB8FF" {OL}/><path d="M76 80 C76 60 96 60 96 80Z" fill="#6CB8FF" {OL}/><path d="M60 92 L92 92 M86 88 L92 92 L86 96" fill="none" stroke="#3b2a1a" stroke-width="2.6"/>'),
 "tree_ds": dict(words=["الشجرة", "شجرة البيانات", "الشجرة الثنائية", "هياكل البيانات"], anim="sway", face=(50, 16, .3), only=DG,
   body='<path d="M50 16 L26 46 M50 16 L74 46 M26 46 L14 78 M26 46 L38 78 M74 46 L62 78 M74 46 L86 78" stroke="#3b2a1a" stroke-width="3"/>'
        '<circle cx="50" cy="16" r="10" fill="#E8574A" {OL}/><circle cx="26" cy="46" r="9" fill="#6CB8FF" {OL}/><circle cx="74" cy="46" r="9" fill="#6CB8FF" {OL}/><circle cx="14" cy="80" r="8" fill="#6CC27A" {OL}/><circle cx="38" cy="80" r="8" fill="#6CC27A" {OL}/><circle cx="62" cy="80" r="8" fill="#6CC27A" {OL}/><circle cx="86" cy="80" r="8" fill="#6CC27A" {OL}/>'),
 "recursion": dict(words=["الاستدعاء الذاتي", "الدوال العودية", "التعاود"], anim="sun", face=(50, 50, .3), only=DG,
   body='<rect x="6" y="6" width="88" height="88" rx="6" fill="#6CB8FF" {OL}/><rect x="18" y="18" width="64" height="64" rx="5" fill="#6CC27A" {OL}/><rect x="30" y="30" width="40" height="40" rx="4" fill="#F6B73C" {OL}/><rect x="40" y="40" width="20" height="20" rx="3" fill="#E8574A" {OL}/>'),
 "rules": dict(words=["القواعد", "القواعد والضوابط", "قواعد البيانات المنطقية"], anim="bob", face=(50, 60, .3), only=DG,
   body='<rect x="12" y="10" width="76" height="84" rx="6" fill="#6CB8FF" {OL}/><rect x="18" y="16" width="64" height="72" rx="3" fill="#fff"/>'
        '<text direction="ltr" x="26" y="38" font-size="12" font-weight="800" fill="#3b2a1a" font-family="monospace">IF → THEN</text><path d="M26 52 L74 52 M26 64 L66 64" stroke="#AEB8C4" stroke-width="3"/>'),
 "supervised": dict(words=["التعلم الموجه", "التصنيف", "التعلم الآلي"], anim="bounce", face=(50, 86, .3), only=DG,
   body='<rect x="4" y="4" width="92" height="92" rx="8" fill="#fff" {OL}/><path d="M10 90 L90 10" stroke="#3b2a1a" stroke-width="2" stroke-dasharray="5 4"/>'
        '<circle cx="24" cy="30" r="5" fill="#E8574A" {OL}/><circle cx="36" cy="18" r="5" fill="#E8574A" {OL}/><circle cx="18" cy="52" r="5" fill="#E8574A" {OL}/><circle cx="40" cy="38" r="5" fill="#E8574A" {OL}/>'
        '<rect x="58" y="60" width="10" height="10" fill="#6CB8FF" {OL}/><rect x="76" y="50" width="10" height="10" fill="#6CB8FF" {OL}/><rect x="70" y="76" width="10" height="10" fill="#6CB8FF" {OL}/><rect x="52" y="80" width="10" height="10" fill="#6CB8FF" {OL}/>'),
 "unsupervised": dict(words=["التعلم غير الموجه", "التجميع", "العنقدة"], anim="wiggle", face=(50, 50, .3), only=DG,
   body='<rect x="4" y="4" width="92" height="92" rx="8" fill="#fff" {OL}/><circle cx="28" cy="30" r="20" fill="#FBE9E7" stroke="#E8574A" stroke-width="2" stroke-dasharray="4 3"/><circle cx="70" cy="70" r="20" fill="#E8F6FF" stroke="#6CB8FF" stroke-width="2" stroke-dasharray="4 3"/>'
        '<circle cx="22" cy="26" r="4" fill="#AEB8C4"/><circle cx="32" cy="22" r="4" fill="#AEB8C4"/><circle cx="28" cy="36" r="4" fill="#AEB8C4"/><circle cx="66" cy="66" r="4" fill="#AEB8C4"/><circle cx="76" cy="70" r="4" fill="#AEB8C4"/><circle cx="68" cy="78" r="4" fill="#AEB8C4"/>'),
 "language_model": dict(words=["توليد النص", "النماذج اللغوية", "النماذج اللغوية الكبيرة", "الذكاء الاصطناعي التوليدي", "روبوت المحادثة"], anim="bob", face=(40, 46, .34), only=DG,
   body='<path d="M6 14 L78 14 C82 14 84 16 84 20 L84 62 C84 66 82 68 78 68 L32 68 L16 84 L18 68 L12 68 C8 68 6 66 6 62Z" fill="#9B6CD9" {OL}/><path d="M18 30 L70 30 M18 42 L60 42 M18 54 L52 54" stroke="#fff" stroke-width="3" stroke-linecap="round"/>'
        '<path d="M88 8 L92 18 L100 20 L92 24 L88 34 L84 24 L76 20 L84 18Z" fill="#FFD25A" {OL}/>'),
 "bias": dict(words=["التحيز", "التحيز في البيانات", "التحيز الخوارزمي"], anim="wobble", face=(50, 22, .3), only=DG + ["math", "thinking"],
   body='<path d="M50 14 L50 88 M26 88 L74 88" stroke="#8B5E3C" stroke-width="5" stroke-linecap="round"/><path d="M10 50 L90 22" stroke="#8B5E3C" stroke-width="4"/>'
        '<path d="M10 50 L0 74 L20 74Z M90 22 L80 46 L100 46Z" fill="none" stroke="#3b2a1a" stroke-width="2"/><path d="M-2 74 C0 84 20 84 22 74Z" fill="#E8574A" {OL}/><path d="M78 46 C80 56 100 56 102 46Z" fill="#6CB8FF" {OL}/>'),
 "compiler": dict(words=["المترجم", "المفسر", "المترجم والمفسر", "ترجمة البرنامج"], anim="sun", face=(50, 54, .3), only=DG,
   body='<rect x="2" y="32" width="26" height="34" rx="3" fill="#fff" {OL}/><path d="M7 42 L22 42 M7 50 L18 50 M7 58 L22 58" stroke="#6CB8FF" stroke-width="2.4"/>'
        '<circle cx="50" cy="49" r="14" fill="#AEB8C4" {OL}/><circle cx="50" cy="49" r="5" fill="#fff" {OL}/><path d="M28 49 L36 49 M64 49 L72 49" stroke="#3b2a1a" stroke-width="3"/>'
        '<rect x="72" y="32" width="26" height="34" rx="3" fill="#1F2A44" {OL}/><text direction="ltr" x="85" y="46" text-anchor="middle" font-size="8" font-weight="800" fill="#9CD86C" font-family="monospace">101</text><text direction="ltr" x="85" y="58" text-anchor="middle" font-size="8" font-weight="800" fill="#9CD86C" font-family="monospace">010</text>'),
 "versions": dict(words=["التحكم في الإصدارات", "الإصدارات", "إدارة الإصدارات"], anim="sway", face=(80, 30, .3), only=DG,
   body='<path d="M20 90 L20 10 M20 60 C20 40 50 40 50 30 M20 40 C20 30 80 30 80 20" fill="none" stroke="#3b2a1a" stroke-width="4"/>'
        '<circle cx="20" cy="80" r="7" fill="#6CB8FF" {OL}/><circle cx="20" cy="56" r="7" fill="#6CB8FF" {OL}/><circle cx="20" cy="14" r="7" fill="#6CB8FF" {OL}/><circle cx="50" cy="28" r="7" fill="#6CC27A" {OL}/><circle cx="80" cy="18" r="7" fill="#F6B73C" {OL}/>'),
 "wireframe": dict(words=["الإطار الشبكي", "النموذج الأولي", "مخطط الواجهة"], anim="bob", face=(70, 70, .3), only=DG,
   body='<rect x="6" y="8" width="88" height="84" rx="4" fill="#fff" stroke="#3b2a1a" stroke-width="2.6" stroke-dasharray="5 3"/><rect x="14" y="16" width="72" height="12" fill="none" stroke="#AEB8C4" stroke-width="2"/>'
        '<rect x="14" y="36" width="32" height="28" fill="none" stroke="#AEB8C4" stroke-width="2"/><path d="M14 36 L46 64 M46 36 L14 64" stroke="#AEB8C4" stroke-width="1.6"/><path d="M54 40 L86 40 M54 50 L80 50 M54 60 L84 60" stroke="#AEB8C4" stroke-width="2"/>'),
 "accessibility": dict(words=["التضمين الرقمي", "قابلية الوصول", "ذوو الإعاقة", "ذوي الاحتياجات الخاصة", "الإتاحة"], anim="bounce", face=(50, 50, .3), only=DG + ["life", "social"],
   body='<circle cx="50" cy="50" r="44" fill="#6CB8FF" {OL}/><circle cx="50" cy="22" r="7" fill="#fff"/><path d="M24 36 L76 36 M50 36 L50 60 M50 60 L36 86 M50 60 L64 86" stroke="#fff" stroke-width="7" stroke-linecap="round"/>'),
 "cyber_threat": dict(words=["المخاطر الرقمية", "الثغرات", "التهديدات", "التهديدات الرقمية", "الضوابط الأمنية", "أمن الويب", "الاستجابة للحوادث", "الجرائم السيبرانية", "مكافحة الجرائم"], anim="wobble", face=(50, 54, .34), only=DG,
   body='<path d="M50 6 L88 18 C88 56 74 80 50 94 C26 80 12 56 12 18Z" fill="#6CC27A" {OL}/><path d="M50 26 L44 42 L54 50 L46 68" fill="none" stroke="#E8574A" stroke-width="4" stroke-linejoin="round"/>'
        '<path d="M70 70 C70 62 86 62 86 70 L86 84 L70 84Z" fill="#5D3A1A" {OL}/><path d="M70 74 L64 72 M70 80 L64 82 M86 74 L92 72 M86 80 L92 82" stroke="#3b2a1a" stroke-width="2"/>'),
 "legislation": dict(words=["التشريعات", "الأنظمة والتشريعات", "الأنظمة الرقمية", "اللوائح", "العقوبات", "مبادئ الحكم"], anim="bob", face=(40, 64, .3), only=DG + ["social"],
   body='<rect x="10" y="20" width="56" height="74" rx="4" fill="#8B5E3C" {OL}/><rect x="16" y="26" width="44" height="62" fill="#F7E9C8"/><path d="M22 40 L54 40 M22 52 L54 52 M22 64 L48 64" stroke="#C98A55" stroke-width="2.4"/>'
        '<rect x="66" y="8" width="16" height="36" rx="3" fill="#C98A55" {OL} transform="rotate(35 74 26)"/><rect x="62" y="44" width="30" height="8" rx="2" fill="#8B5E3C" {OL}/>'),
 "emerging": dict(words=["التقنيات الناشئة", "التقنيات الحديثة الناشئة", "مستقبل التقنية"], anim="bounce", face=(50, 50, .3), only=DG,
   body='<path d="M50 4 C66 18 70 40 64 64 L36 64 C30 40 34 18 50 4Z" fill="#fff" {OL}/><circle cx="50" cy="34" r="8" fill="#6CB8FF" {OL}/><path d="M36 52 L22 70 L36 66 M64 52 L78 70 L64 66" fill="#E8574A" {OL}/>'
        '<path d="M42 70 C40 80 44 86 50 94 C56 86 60 80 58 70Z" fill="#F6B73C" {OL}/>'),
 "digital_citizen": dict(words=["المواطن الرقمي", "المواطنة الرقمية المسؤولة"], anim="sun", face=(50, 34, .34), only=DG,
   body='<circle cx="50" cy="56" r="40" fill="#6CB8FF" {OL}/><path d="M24 48 C34 40 46 46 42 56 C38 64 26 60 24 48Z M58 66 C68 60 78 68 72 78 C66 86 56 80 58 66Z" fill="#6CC27A" {OL}/>'
        '<circle cx="50" cy="20" r="14" fill="#FFD25A" {OL}/>'),
}
ALIAS_ONLY = None
ALIASES = {"وورد": ("dig.word", ("digital",)), "إكسل": ("dig.spreadsheet", ("digital",)), "باوربوينت": ("dig.slides", ("digital",)),
           "المصادر": ("dig.folder", ("digital",)), "الأحداث": ("tech.block_events", ("digital",)), "الجمهور المستهدف": ("day.billboard", ("digital",))}
