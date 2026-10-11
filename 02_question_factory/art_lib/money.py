"""🆕 batch 43 · money (المعرفة المالية): work and skills, needs and the shopping list, the records and the accounts, credit and
interest, cheating with a card, the company's money (assets, liabilities, revenue, profit, cash), shares and bonds, risk and
spreading it, the cost of a choice. No piggy bank (a money jar, as in life.py)."""
F = "money"
D = {
 "job": dict(words=["الوظيفة", "الوظائف", "البحث عن وظيفة", "سوق العمل", "المهن", "اختيار المهنة"], anim="bob", face=(50, 64, .45),
   body='<rect x="8" y="32" width="84" height="58" rx="8" fill="#8B5E3C" {OL}/><path d="M36 32 L36 22 C36 16 64 16 64 22 L64 32" fill="none" stroke="#3b2a1a" stroke-width="5"/>'
        '<path d="M8 54 L92 54" stroke="#3b2a1a" stroke-width="2.6"/><rect x="42" y="48" width="16" height="12" rx="3" fill="#FFD25A" {OL}/>'),
 "skills": dict(words=["المهارات", "المهارات الشخصية", "تنمية المهارات", "المهارات الأساسية", "اكتساب المهارات"], anim="wobble", face=(50, 70, .42),
   body='<rect x="8" y="44" width="84" height="48" rx="6" fill="#E8574A" {OL}/><path d="M34 44 L34 32 C34 26 66 26 66 32 L66 44" fill="none" stroke="#3b2a1a" stroke-width="5"/>'
        '<path d="M8 60 L92 60" stroke="#3b2a1a" stroke-width="2.6"/><path d="M22 40 L40 12 M30 18 L44 20" stroke="#AEB8C4" stroke-width="6" stroke-linecap="round"/><circle cx="72" cy="22" r="10" fill="none" stroke="#AEB8C4" stroke-width="6"/>'),
 "freelance": dict(words=["العمل الحر", "العمل عن بعد", "ريادة الأعمال", "رائد الأعمال", "المشروع الصغير", "المشاريع الصغيرة"], anim="bob", face=(44, 44, .42),
   body='<rect x="14" y="14" width="60" height="44" rx="4" fill="#3b3b5c" {OL}/><rect x="18" y="18" width="52" height="36" fill="#BFE3F2"/><path d="M6 62 L82 62 L90 74 L-2 74Z" fill="#AEB8C4" {OL}/>'
        '<path d="M80 38 L96 38 L94 58 L82 58Z" fill="#fff" {OL}/><path d="M86 30 C84 26 88 24 86 20" fill="none" stroke="#AEB8C4" stroke-width="2.4"/>'),
 "needs": dict(words=["الاحتياجات"], anim="bob", face=(50, 70, .42),
   body='<path d="M10 40 L90 40 L80 92 L20 92Z" fill="#C98A55" {OL}/><path d="M10 40 L90 40" stroke="#8B5E3C" stroke-width="6"/><path d="M30 40 C30 20 70 20 70 40" fill="none" stroke="#3b2a1a" stroke-width="4"/>'
        '<circle cx="34" cy="34" r="10" fill="#E8574A" {OL}/><path d="M50 36 C50 24 64 22 66 34Z" fill="#6CC27A" {OL}/><rect x="58" y="24" width="14" height="16" rx="2" fill="#fff" {OL}/>'),
 "shopping_list": dict(words=["قائمة المشتريات", "قائمة التسوق", "التخطيط للشراء"], anim="wobble", face=(46, 70, .4),
   body='<rect x="16" y="8" width="60" height="86" rx="4" fill="#fff" {OL}/><path d="M26 28 L32 34 L42 22 M26 50 L32 56 L42 44" fill="none" stroke="#6CC27A" stroke-width="4" stroke-linecap="round"/>'
        '<path d="M48 30 L66 30 M48 52 L66 52 M26 72 L66 72" stroke="#3b2a1a" stroke-width="3" stroke-linecap="round"/><path d="M78 70 L94 30 L98 32 L82 72 L76 76Z" fill="#FFD25A" {OL}/>'),
 "ledger": dict(words=["السجلات المالية", "المحاسبة", "المبادئ المحاسبية", "الدفاتر المحاسبية", "تسجيل المصروفات", "سجل المصروفات"], anim="bob", face=(30, 62, .38),
   body='<rect x="8" y="12" width="84" height="78" rx="4" fill="#fff" {OL}/><path d="M50 12 L50 90" stroke="#3b2a1a" stroke-width="2.6"/><rect x="8" y="12" width="84" height="12" fill="#6CC27A" {OL}/>'
        '<path d="M58 36 L84 36 M58 48 L84 48 M58 60 L84 60 M58 72 L84 72" stroke="#AEB8C4" stroke-width="2"/><text direction="ltr" x="72" y="45" text-anchor="middle" font-size="9" font-weight="800" fill="#3E8E4C" font-family="sans-serif">+</text>'
        '<text direction="ltr" x="72" y="69" text-anchor="middle" font-size="10" font-weight="800" fill="#E8574A" font-family="sans-serif">−</text>'),
 "real_estate": dict(words=["العقار", "العقارات", "شراء منزل", "الرهن العقاري", "التمويل العقاري"], anim="bob", face=(40, 70, .42),
   body='<path d="M10 50 L40 24 L70 50 L70 94 L10 94Z" fill="#F2D07A" {OL}/><path d="M4 54 L40 22 L76 54" fill="none" stroke="#E8574A" stroke-width="6" stroke-linecap="round"/>'
        '<path d="M80 30 L80 94" stroke="#8B5E3C" stroke-width="4"/><rect x="66" y="34" width="30" height="20" rx="3" fill="#fff" {OL}/><text direction="ltr" x="81" y="48" text-anchor="middle" font-size="10" font-weight="800" fill="#E8574A" font-family="sans-serif">$</text>'),
 "risk": dict(words=["المخاطر", "إدارة المخاطر", "تقليل المخاطر", "تقييم المخاطر"], anim="wobble", face=(36, 62, .4),
   body='<rect x="10" y="34" width="46" height="46" rx="8" fill="#fff" {OL}/><circle cx="22" cy="46" r="4" fill="#3b2a1a"/><circle cx="44" cy="68" r="4" fill="#3b2a1a"/><circle cx="33" cy="57" r="4" fill="#3b2a1a"/>'
        '<path d="M76 12 L98 52 L54 52Z" fill="#FFD25A" {OL}/><path d="M76 24 L76 40" stroke="#3b2a1a" stroke-width="5" stroke-linecap="round"/><circle cx="76" cy="46" r="2.6" fill="#3b2a1a"/>'),
 "credit": dict(words=["الائتمان", "البطاقة الائتمانية"], anim="wobble", face=(30, 66, .38),
   body='<rect x="6" y="20" width="88" height="60" rx="8" fill="#6CB8FF" {OL}/><rect x="6" y="32" width="88" height="10" fill="#3b3b5c"/><rect x="14" y="52" width="18" height="14" rx="3" fill="#FFD25A" {OL}/>'
        '<path d="M50 62 L84 62" stroke="#fff" stroke-width="3" stroke-linecap="round"/>'),
 "interest": dict(words=["الفائدة", "سعر الفائدة", "الفائدة البسيطة"], anim="bounce", face=(36, 62, .42),
   body='<circle cx="36" cy="62" r="28" fill="#FFD25A" {OL}/><circle cx="36" cy="62" r="20" fill="none" stroke="#F6B73C" stroke-width="3"/>'
        '<text direction="ltr" x="76" y="40" text-anchor="middle" font-size="34" font-weight="800" fill="#6CC27A" font-family="sans-serif">%</text><path d="M66 70 L86 50 M78 50 L86 50 L86 58" fill="none" stroke="#6CC27A" stroke-width="4" stroke-linecap="round"/>'),
 "repay": dict(words=["السداد", "السداد المبكر", "سداد الدين", "الفاتورة المدفوعة"], anim="bob", face=(46, 70, .42),
   body='<path d="M16 8 L76 8 L76 94 L66 88 L56 94 L46 88 L36 94 L26 88 L16 94Z" fill="#fff" {OL}/><path d="M26 24 L66 24 M26 36 L56 36" stroke="#AEB8C4" stroke-width="3"/>'
        '<circle cx="74" cy="66" r="18" fill="#6CC27A" {OL}/><path d="M64 66 L72 74 L86 58" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round"/>'),
 "card_fraud": dict(words=["سرقة البطاقة", "الاحتيال المالي", "الاحتيال الإلكتروني", "التصيد الاحتيالي", "حماية البيانات المالية"], anim="wobble", face=(30, 70, .36),
   body='<rect x="6" y="40" width="70" height="48" rx="8" fill="#6CB8FF" {OL}/><rect x="6" y="50" width="70" height="8" fill="#3b3b5c"/><rect x="12" y="66" width="14" height="12" rx="2" fill="#FFD25A"/>'
        '<path d="M80 6 L80 30 C80 44 62 44 62 32" fill="none" stroke="#AEB8C4" stroke-width="5" stroke-linecap="round"/><path d="M62 32 L56 26" stroke="#AEB8C4" stroke-width="5" stroke-linecap="round"/><path d="M90 50 L96 44 M90 60 L98 60" stroke="#E8574A" stroke-width="3"/>'),
 "wallet": dict(words=["المالية الشخصية", "إدارة المال الشخصي", "الأموال الشخصية"], anim="wobble", face=(50, 64, .45),
   body='<rect x="8" y="28" width="84" height="60" rx="10" fill="#8B5E3C" {OL}/><path d="M8 40 L80 40" stroke="#6E4A2E" stroke-width="3"/><rect x="62" y="50" width="30" height="20" rx="6" fill="#A8774F" {OL}/>'
        '<circle cx="72" cy="60" r="4" fill="#FFD25A" {OL}/><rect x="20" y="16" width="40" height="18" rx="2" fill="#9CD86C" {OL}/>'),
 "company": dict(words=["مالية الشركات", "الشركة", "الشركات", "الشركة المساهمة"], anim="bob", face=(50, 60, .4),
   body='<rect x="20" y="14" width="60" height="80" fill="#AEB8C4" {OL}/><path d="M30 26 L40 26 M60 26 L70 26 M30 40 L40 40 M60 40 L70 40 M30 54 L40 54 M60 54 L70 54" stroke="#BFE3F2" stroke-width="6"/>'
        '<rect x="42" y="74" width="16" height="20" fill="#5D646E" {OL}/><circle cx="84" cy="22" r="12" fill="#FFD25A" {OL}/><text direction="ltr" x="84" y="27" text-anchor="middle" font-size="13" font-weight="800" fill="#3b2a1a" font-family="sans-serif">$</text>'),
 "broker": dict(words=["الوسيط المالي", "الوسيط", "الوساطة", "البنك وسيط"], anim="sway", face=(50, 32, .38), only=["finance", "life", "social"],
   body='<rect x="38" y="16" width="24" height="30" rx="6" fill="#6CB8FF" {OL}/><path d="M4 64 L32 64 M68 64 L96 64" stroke="#3b2a1a" stroke-width="4"/>'
        '<circle cx="18" cy="80" r="12" fill="#FFD25A" {OL}/><rect x="72" y="70" width="24" height="22" rx="3" fill="#9CD86C" {OL}/><path d="M32 64 L44 52 M68 64 L56 52" stroke="#3b2a1a" stroke-width="4" stroke-linecap="round"/>'
        '<path d="M44 46 L44 52 L56 52 L56 46" fill="none" stroke="#3b2a1a" stroke-width="3"/>'),
 "assets": dict(words=["الأصول", "الخصوم", "الأصول والخصوم", "الميزانية العمومية", "حقوق الملكية"], anim="wobble", face=(50, 22, .35),
   body='<path d="M50 14 L50 86 M24 86 L76 86" stroke="#3b2a1a" stroke-width="5" stroke-linecap="round"/><path d="M14 34 L86 34" stroke="#3b2a1a" stroke-width="4"/>'
        '<path d="M14 34 L4 62 L24 62Z M86 34 L76 62 L96 62Z" fill="none" stroke="#3b2a1a" stroke-width="2"/><path d="M2 62 C4 72 24 72 26 62Z" fill="#6CC27A" {OL}/><path d="M74 62 C76 72 96 72 98 62Z" fill="#E8574A" {OL}/>'),
 "revenue": dict(words=["الإيرادات", "الإيراد", "المبيعات", "الدخل الإجمالي"], anim="bounce", face=(36, 70, .4),
   body='<path d="M10 36 L50 36 L50 22 L74 48 L50 74 L50 60 L10 60Z" fill="#6CC27A" {OL}/><circle cx="78" cy="74" r="16" fill="#FFD25A" {OL}/><circle cx="86" cy="20" r="10" fill="#FFD25A" {OL}/>'),
 "profit": dict(words=["صافي الربح", "الربحية", "الربح", "هامش الربح"], anim="bounce", face=(30, 72, .38),
   body='<path d="M8 92 L92 92" stroke="#3b2a1a" stroke-width="4"/><rect x="14" y="64" width="16" height="28" fill="#9CD86C" {OL}/><rect x="40" y="48" width="16" height="44" fill="#6CC27A" {OL}/><rect x="66" y="28" width="16" height="64" fill="#3E8E4C" {OL}/>'
        '<path d="M10 52 L40 34 L60 40 L88 10 M76 10 L88 10 L88 22" fill="none" stroke="#F6B73C" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>'),
 "cash_flow": dict(words=["التدفق النقدي", "السيولة", "النقد", "التدفقات النقدية"], anim="drip", face=(30, 34, .38),
   body='<path d="M8 20 L44 20 C56 20 60 28 60 38 L60 48 L46 48 L46 38 C46 34 44 34 40 34 L8 34Z" fill="#C9D2DC" {OL}/>'
        '<circle cx="53" cy="62" r="8" fill="#FFD25A" {OL}/><circle cx="53" cy="82" r="7" fill="#FFD25A" {OL}/><path d="M20 94 L86 94" stroke="#3b2a1a" stroke-width="4"/><ellipse cx="72" cy="88" rx="14" ry="5" fill="#FFD25A" {OL}/>'),
 "ratios": dict(words=["نسب النشاط", "المديونية", "نسب التغطية", "النسب المالية", "التحليل المالي", "نسب السيولة"], anim="sun", face=(50, 70, .4),
   body='<path d="M8 74 A42 42 0 0 1 92 74Z" fill="#fff" {OL}/><path d="M8 74 A42 42 0 0 1 22 42 L50 74Z" fill="#E8574A"/><path d="M22 42 A42 42 0 0 1 78 42 L50 74Z" fill="#FFD25A"/><path d="M78 42 A42 42 0 0 1 92 74 L50 74Z" fill="#6CC27A"/>'
        '<path d="M8 74 A42 42 0 0 1 92 74" fill="none" {OL}/><path d="M50 74 L70 40" stroke="#3b2a1a" stroke-width="5" stroke-linecap="round"/><circle cx="50" cy="74" r="6" fill="#3b2a1a"/>'),
 "share": dict(words=["الأوراق المالية", "السهم العادي", "السهم الممتاز", "الأوراق المالية الأجنبية", "السوق المالية"], anim="bounce", face=(36, 62, .4),
   body='<rect x="6" y="20" width="70" height="72" rx="4" fill="#FFF3C4" {OL}/><rect x="12" y="26" width="58" height="60" rx="2" fill="none" stroke="#C98A55" stroke-width="2"/>'
        '<path d="M60 70 L72 46 L82 56 L96 26 M86 26 L96 26 L96 36" fill="none" stroke="#6CC27A" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>'),
 "bond": dict(words=["السند", "السندات", "الصكوك"], never=["social"], anim="sway", face=(46, 46, .4),
   body='<path d="M10 20 L82 20 L82 80 L10 80Z" fill="#FFF3C4" {OL}/><path d="M18 34 L60 34 M18 46 L54 46" stroke="#C98A55" stroke-width="3"/><circle cx="70" cy="70" r="14" fill="#E8574A" {OL}/>'
        '<path d="M62 82 L58 96 L66 90 L70 98 L72 84 M78 82 L82 96 L74 90" fill="#E8574A" {OL}/>'),
 "competition_shop": dict(words=["المنافسة", "التنافس التجاري", "المنافسة في السوق"], anim="bounce", face=(28, 62, .36), only=["finance", "social", "life"],
   body='<path d="M4 40 L50 40 L46 26 L8 26Z M52 40 L96 40 L92 26 L56 26Z" fill="#E8574A" {OL}/><rect x="8" y="40" width="38" height="50" fill="#fff" {OL}/><rect x="56" y="40" width="36" height="50" fill="#fff" {OL}/>'
        '<path d="M50 20 L50 4 M44 10 L50 4 L56 10" fill="none" stroke="#6CC27A" stroke-width="4" stroke-linecap="round"/><rect x="62" y="56" width="24" height="16" rx="3" fill="#FFD25A" {OL}/>'),
 "opportunity": dict(words=["تكلفة الفرصة البديلة", "الفرصة البديلة", "اتخاذ القرار المالي", "المفاضلة"], anim="wobble", face=(50, 70, .4),
   body='<path d="M50 96 L50 58 L20 30 M50 58 L80 30" fill="none" stroke="#C9A27A" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/>'
        '<circle cx="18" cy="20" r="14" fill="#E8574A" {OL}/><rect x="68" y="8" width="26" height="24" rx="4" fill="#6CB8FF" {OL}/>'),
 "discount": dict(words=["الخصم", "التخفيضات", "نسبة الخصم", "العروض"], anim="wobble", face=(56, 40, .38), only=["finance", "math", "life"],
   body='<path d="M8 50 L44 14 L90 14 L90 60 L54 96Z" fill="#FFD25A" {OL}/><circle cx="74" cy="30" r="6" fill="#fff" {OL}/>'
        '<text direction="ltr" x="54" y="72" text-anchor="middle" font-size="28" font-weight="800" fill="#E8574A" font-family="sans-serif" transform="rotate(-45 54 62)">%</text>'),
 "time_value": dict(words=["حالات القيمة الزمنية", "القيمة الزمنية للنقود"], anim="sun", face=(36, 60, .4),
   body='<circle cx="36" cy="54" r="30" fill="#fff" {OL}/><path d="M36 54 L36 34 M36 54 L50 62" stroke="#3b2a1a" stroke-width="4" stroke-linecap="round"/>'
        '<circle cx="78" cy="78" r="16" fill="#FFD25A" {OL}/><circle cx="82" cy="40" r="11" fill="#FFD25A" {OL}/><path d="M70 22 L82 10 L94 22" fill="none" stroke="#6CC27A" stroke-width="4" stroke-linecap="round"/>'),
 "diversify": dict(words=["التنويع", "تنويع الاستثمار", "المحفظة الاستثمارية"], anim="bounce", face=(50, 30, .35),
   body='<path d="M4 56 L32 56 L28 90 L8 90Z M36 56 L64 56 L60 90 L40 90Z M68 56 L96 56 L92 90 L72 90Z" fill="#C98A55" {OL}/>'
        '<ellipse cx="18" cy="50" rx="8" ry="10" fill="#fff" {OL}/><ellipse cx="50" cy="50" rx="8" ry="10" fill="#fff" {OL}/><ellipse cx="82" cy="50" rx="8" ry="10" fill="#fff" {OL}/>'),
 "capital": dict(words=["تكلفة رأس المال", "المتوسط المرجح لتكلفة رأس المال", "هيكل رأس المال", "مسائل هيكل رأس المال", "رأس المال"], anim="bob", face=(50, 30, .36),
   body='<rect x="16" y="64" width="68" height="26" rx="3" fill="#6CB8FF" {OL}/><rect x="22" y="40" width="56" height="24" rx="3" fill="#F6B73C" {OL}/><rect x="30" y="16" width="40" height="24" rx="3" fill="#6CC27A" {OL}/>'
        '<text direction="ltr" x="50" y="82" text-anchor="middle" font-size="12" font-weight="800" fill="#fff" font-family="sans-serif">$</text>'),
 "spread": dict(words=["الانحراف المعياري", "التباين", "تشتت البيانات", "مقاييس التشتت"], anim="sway", face=(50, 58, .4),
   body='<path d="M4 88 L96 88" stroke="#3b2a1a" stroke-width="3"/><path d="M6 86 C30 86 34 20 50 20 C66 20 70 86 94 86" fill="#BFE3F2" {OL}/>'
        '<path d="M34 88 L34 50 M66 88 L66 50" stroke="#E8574A" stroke-width="3" stroke-dasharray="4 3"/><path d="M36 60 L64 60 M40 56 L36 60 L40 64 M60 56 L64 60 L60 64" fill="none" stroke="#E8574A" stroke-width="2.6"/>'),
}
ALIAS_ONLY = None
ALIASES = {}
