"""🆕 batch 43 · more maths (الرياضيات، من الصغار للثانوي): the problem-solving steps, position words, units (cm, mm, mL, mg, inch,
foot, yard), morning and evening, chance (certain / possible / impossible, events, independent events), place value (thousands to
billions, tenths), shapes (quadrilateral, octagon, symmetry, 2-D and 3-D, composite, tiling, views), angles, algebra cards
(expressions, input → output, terms, polynomials, reciprocals and opposites, powers, roots, the discriminant), graphs (asymptotes,
max and min, zeros, direct and inverse variation), matrices, the complex plane, polar axes, the conics, statistics (surveys,
sectors, double bars, outliers, quartiles, the normal curve, the binomial), logic (and / or / not, if-then, truth values),
trigonometry identities, Heron, limits, Pascal's triangle. A symbol card where the concept IS a symbol («π»، «n!»، «√»)."""
F = "math2"
M = ["math"]


def card(sym, color="#6CB8FF", size=30, y=60):
    return (f'<rect x="8" y="16" width="84" height="68" rx="12" fill="{color}" {{OL}}/><rect x="14" y="22" width="72" height="56" rx="8" fill="#fff"/>'
            f'<text direction="ltr" x="50" y="{y}" text-anchor="middle" font-size="{size}" font-weight="800" fill="#3b2a1a" font-family="sans-serif">{sym}</text>')


D = {
 # ---------- solving a problem ----------
 "problem_steps": dict(words=["حل المسألة", "خطوات حل المسألة", "أفهم", "أخطط", "أحل", "أتحقق", "الحل عكسياً", "رسم صورة", "خطة حل المسألة"], anim="bounce", face=(50, 50, .3), only=M,
   body='<circle cx="22" cy="22" r="16" fill="#6CB8FF" {OL}/><circle cx="78" cy="22" r="16" fill="#F6B73C" {OL}/><circle cx="78" cy="78" r="16" fill="#6CC27A" {OL}/><circle cx="22" cy="78" r="16" fill="#E8574A" {OL}/>'
        '<text direction="ltr" x="22" y="28" text-anchor="middle" font-size="16" font-weight="800" fill="#fff" font-family="sans-serif">1</text><text direction="ltr" x="78" y="28" text-anchor="middle" font-size="16" font-weight="800" fill="#fff" font-family="sans-serif">2</text>'
        '<text direction="ltr" x="78" y="84" text-anchor="middle" font-size="16" font-weight="800" fill="#fff" font-family="sans-serif">3</text><path d="M14 78 L20 84 L30 72" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round"/>'
        '<path d="M40 22 L60 22 M78 40 L78 60 M60 78 L40 78" stroke="#3b2a1a" stroke-width="3"/>'),
 "between": dict(words=["بين", "الموقع والاتجاه", "فوق وتحت", "يمين ويسار", "أمام وخلف"], anim="bounce", face=(50, 50, .3), only=M,
   body='<rect x="4" y="34" width="28" height="40" rx="4" fill="#6CB8FF" {OL}/><rect x="68" y="34" width="28" height="40" rx="4" fill="#6CB8FF" {OL}/><circle cx="50" cy="54" r="14" fill="#E8574A" {OL}/>'
        '<path d="M34 90 L66 90 M40 84 L34 90 L40 96 M60 84 L66 90 L60 96" fill="none" stroke="#3b2a1a" stroke-width="2.6"/>'),
 "rows_cols": dict(words=["الصفوف", "الأعمدة والصفوف", "المصفوفة الحسابية", "الترتيب في صفوف"], anim="bob", face=(50, 50, .3), only=M,
   body='<circle cx="20" cy="20" r="8" fill="#F6B73C" {OL}/><circle cx="50" cy="20" r="8" fill="#F6B73C" {OL}/><circle cx="80" cy="20" r="8" fill="#F6B73C" {OL}/><circle cx="20" cy="50" r="8" fill="#F6B73C" {OL}/><circle cx="50" cy="50" r="8" fill="#F6B73C" {OL}/>'
        '<circle cx="80" cy="50" r="8" fill="#F6B73C" {OL}/><circle cx="20" cy="80" r="8" fill="#F6B73C" {OL}/><circle cx="50" cy="80" r="8" fill="#F6B73C" {OL}/><circle cx="80" cy="80" r="8" fill="#F6B73C" {OL}/>'),
 "sort_color_shape": dict(words=["اللون", "التصنيف حسب اللون", "التصنيف حسب الشكل", "الفرز حسب الخصائص"], anim="bounce", face=(50, 76, .3), only=M,
   body='<circle cx="20" cy="24" r="14" fill="#E8574A" {OL}/><circle cx="50" cy="24" r="14" fill="#E8574A" {OL}/><rect x="70" y="10" width="26" height="26" rx="3" fill="#6CB8FF" {OL}/>'
        '<path d="M6 44 L94 44" stroke="#AEB8C4" stroke-width="2" stroke-dasharray="4 3"/><path d="M8 94 L22 64 L36 94Z" fill="#FFD25A" {OL}/><rect x="56" y="62" width="30" height="30" rx="3" fill="#6CB8FF" {OL}/>'),
 # ---------- measuring ----------
 "cm_mm": dict(words=["السنتمتر", "المليمتر", "الوحدات المترية", "المتر والسنتمتر", "التحويل بين الوحدات", "التحويل"], anim="bob", face=(50, 30, .32), only=M,
   body='<rect x="4" y="50" width="92" height="30" rx="4" fill="#FFD25A" {OL}/><path d="M12 50 L12 66 M20 50 L20 58 M28 50 L28 58 M36 50 L36 58 M44 50 L44 66 M52 50 L52 58 M60 50 L60 58 M68 50 L68 58 M76 50 L76 66 M84 50 L84 58" stroke="#3b2a1a" stroke-width="2"/>'
        '<text direction="ltr" x="80" y="40" text-anchor="middle" font-size="14" font-weight="800" fill="#3b2a1a" font-family="sans-serif">cm</text>'),
 "ml": dict(words=["المليلتر", "اللتر والمليلتر", "السعة بالمليلتر", "قياس السعة"], anim="drip", face=(40, 70, .32), only=M,
   body='<path d="M20 20 L64 20 L60 92 L24 92Z" fill="#E8F6FF" {OL}/><path d="M22 50 L62 50 L60 92 L24 92Z" fill="#7CC6F2"/><path d="M20 20 L64 20 L60 92 L24 92Z" fill="none" {OL}/>'
        '<path d="M64 34 L56 34 M64 50 L56 50 M64 66 L56 66" stroke="#3b2a1a" stroke-width="2"/><text direction="ltr" x="82" y="54" text-anchor="middle" font-size="14" font-weight="800" fill="#3b2a1a" font-family="sans-serif">mL</text>'),
 "mg": dict(words=["الملجرام", "الجرام والملجرام", "الكيلوجرام والجرام"], anim="wobble", face=(50, 70, .32), only=M,
   body='<path d="M20 90 L30 40 L70 40 L80 90Z" fill="#AEB8C4" {OL}/><circle cx="50" cy="30" r="10" fill="none" stroke="#3b2a1a" stroke-width="4"/><text direction="ltr" x="50" y="78" text-anchor="middle" font-size="16" font-weight="800" fill="#3b2a1a" font-family="sans-serif">mg</text>'),
 "inch_foot": dict(words=["البوصة", "القدم", "الياردة", "الوحدات الإنجليزية"], anim="bob", face=(50, 30, .3), only=M,
   body='<rect x="4" y="50" width="92" height="30" rx="4" fill="#F2C46D" {OL}/><path d="M14 50 L14 70 M26 50 L26 60 M38 50 L38 70 M50 50 L50 60 M62 50 L62 70 M74 50 L74 60 M86 50 L86 70" stroke="#3b2a1a" stroke-width="2"/>'
        '<text direction="ltr" x="76" y="40" text-anchor="middle" font-size="14" font-weight="800" fill="#3b2a1a" font-family="sans-serif">in</text>'),
 "am": dict(words=["صباحاً", "الصباح", "صباحا"], anim="sun", face=(40, 62, .32), only=M,
   body='<circle cx="40" cy="62" r="30" fill="#fff" {OL}/><path d="M40 62 L40 42 M40 62 L54 62" stroke="#3b2a1a" stroke-width="4" stroke-linecap="round"/><circle cx="80" cy="20" r="14" fill="#FFD25A" {OL}/>'
        '<path d="M80 0 L80 2 M98 20 L96 20 M92 8 L90 10" stroke="#F6B73C" stroke-width="3"/>'),
 "pm": dict(words=["مساءً", "المساء", "مساء"], anim="sway", face=(40, 62, .32), only=M,
   body='<circle cx="40" cy="62" r="30" fill="#fff" {OL}/><path d="M40 62 L40 42 M40 62 L26 70" stroke="#3b2a1a" stroke-width="4" stroke-linecap="round"/><path d="M84 6 C70 8 64 22 70 34 C76 44 90 44 96 36 C84 38 76 28 80 18 C82 12 84 8 84 6Z" fill="#FFF3C4" {OL}/>'),
 # ---------- chance ----------
 "spinner": dict(words=["مؤكد", "ممكن", "مستحيل", "العشوائي", "العشوائية", "الاحتمال", "احتمال الحادثة"], anim="sun", face=(50, 72, .3), only=M,
   body='<circle cx="50" cy="50" r="44" fill="#fff" {OL}/><path d="M50 50 L50 6 A44 44 0 0 1 94 50Z" fill="#E8574A"/><path d="M50 50 L94 50 A44 44 0 0 1 50 94Z" fill="#6CB8FF"/><path d="M50 50 L50 94 A44 44 0 0 1 6 50Z" fill="#6CC27A"/><path d="M50 50 L6 50 A44 44 0 0 1 50 6Z" fill="#FFD25A"/>'
        '<circle cx="50" cy="50" r="44" fill="none" {OL}/><path d="M50 50 L70 22" stroke="#3b2a1a" stroke-width="5" stroke-linecap="round"/><circle cx="50" cy="50" r="5" fill="#3b2a1a"/>'),
 "events": dict(words=["الحادثة", "الحادثة البسيطة", "الحادثة المتممة", "الحادثة المركبة", "الحوادث المتنافية", "الحوادث غير المتنافية"], anim="bob", face=(50, 82, .3), only=M,
   body='<rect x="4" y="10" width="92" height="80" rx="6" fill="#fff" {OL}/><circle cx="38" cy="46" r="24" fill="#6CB8FF" opacity=".6" {OL}/><circle cx="62" cy="46" r="24" fill="#F6B73C" opacity=".6" {OL}/>'
        '<text direction="ltr" x="30" y="52" text-anchor="middle" font-size="14" font-weight="800" fill="#3b2a1a" font-family="sans-serif">A</text><text direction="ltr" x="70" y="52" text-anchor="middle" font-size="14" font-weight="800" fill="#3b2a1a" font-family="sans-serif">B</text>'),
 "independent": dict(words=["الحوادث المستقلة", "الحوادث غير المستقلة", "الاحتمال المشروط"], anim="bounce", face=(50, 86, .3), only=M,
   body='<circle cx="28" cy="40" r="22" fill="#FFD25A" {OL}/><circle cx="28" cy="40" r="15" fill="none" stroke="#F6B73C" stroke-width="2"/><circle cx="72" cy="40" r="22" fill="#C9D2DC" {OL}/><circle cx="72" cy="40" r="15" fill="none" stroke="#AEB8C4" stroke-width="2"/>'
        '<text direction="ltr" x="50" y="84" text-anchor="middle" font-size="14" font-weight="800" fill="#3b2a1a" font-family="sans-serif">P(A)·P(B)</text>'),
 "expected": dict(words=["القيمة المتوقعة", "التوقع الرياضي"], anim="bounce", face=(30, 70, .3), only=M,
   body='<rect x="8" y="16" width="40" height="40" rx="8" fill="#fff" {OL}/><circle cx="18" cy="26" r="3.6" fill="#3b2a1a"/><circle cx="38" cy="46" r="3.6" fill="#3b2a1a"/><circle cx="28" cy="36" r="3.6" fill="#3b2a1a"/>'
        '<text direction="ltr" x="72" y="44" text-anchor="middle" font-size="22" font-weight="800" fill="#6CB8FF" font-family="sans-serif">E(x)</text>'),
 # ---------- place value ----------
 "place_value": dict(words=["الألوف", "الملايين", "البلايين", "الأعداد الكبيرة"], anim="bob", face=(50, 82, .3), only=M,
   body='<rect x="2" y="24" width="96" height="44" rx="6" fill="#fff" {OL}/><path d="M26 24 L26 68 M50 24 L50 68 M74 24 L74 68" stroke="#3b2a1a" stroke-width="2"/>'
        '<rect x="2" y="24" width="24" height="12" fill="#E8574A"/><rect x="26" y="24" width="24" height="12" fill="#F6B73C"/><rect x="50" y="24" width="24" height="12" fill="#6CC27A"/><rect x="74" y="24" width="24" height="12" fill="#6CB8FF"/>'
        '<text direction="ltr" x="14" y="60" text-anchor="middle" font-size="16" font-weight="800" fill="#3b2a1a" font-family="sans-serif">3</text><text direction="ltr" x="38" y="60" text-anchor="middle" font-size="16" font-weight="800" fill="#3b2a1a" font-family="sans-serif">0</text><text direction="ltr" x="62" y="60" text-anchor="middle" font-size="16" font-weight="800" fill="#3b2a1a" font-family="sans-serif">5</text><text direction="ltr" x="86" y="60" text-anchor="middle" font-size="16" font-weight="800" fill="#3b2a1a" font-family="sans-serif">2</text>'),
 "tenths": dict(words=["الأعشار"], anim="bob", face=(50, 84, .3), only=M,
   body='<rect x="4" y="16" width="92" height="40" rx="4" fill="#fff" {OL}/><rect x="4" y="16" width="27.6" height="40" fill="#6CB8FF"/><path d="M13.2 16 L13.2 56 M22.4 16 L22.4 56 M31.6 16 L31.6 56 M40.8 16 L40.8 56 M50 16 L50 56 M59.2 16 L59.2 56 M68.4 16 L68.4 56 M77.6 16 L77.6 56 M86.8 16 L86.8 56" stroke="#3b2a1a" stroke-width="1.6"/>'
        '<rect x="4" y="16" width="92" height="40" rx="4" fill="none" {OL}/><text direction="ltr" x="50" y="80" text-anchor="middle" font-size="18" font-weight="800" fill="#3b2a1a" font-family="sans-serif">0.3</text>'),
 # ---------- shapes ----------
 "quadrilateral": dict(words=["الشكل الرباعي", "الأشكال الرباعية", "الرباعي"], anim="wobble", face=(50, 52, .36), only=M,
   body='<path d="M14 78 L28 18 L84 28 L90 84Z" fill="#9CD86C" {OL}/>'),
 "octagon": dict(words=["الشكل الثماني", "المثمن", "المضلعات المنتظمة"], anim="sun", face=(50, 50, .36), only=M,
   body='<path d="M34 6 L66 6 L94 34 L94 66 L66 94 L34 94 L6 66 L6 34Z" fill="#F6B73C" {OL}/>'),
 "symmetry": dict(words=["الشكل المتماثل", "التماثل", "خط التماثل", "التماثل حول محور", "العناصر المتناظرة"], anim="sway", face=(50, 48, .32), only=M,
   body='<path d="M50 20 C34 4 6 14 10 40 C14 60 40 60 50 50 C60 60 86 60 90 40 C94 14 66 4 50 20Z" fill="#F59BB8" {OL}/><path d="M50 50 C40 60 18 70 26 86 C34 98 46 86 50 74 C54 86 66 98 74 86 C82 70 60 60 50 50Z" fill="#B0A8C9" {OL}/>'
        '<path d="M50 4 L50 98" stroke="#3b2a1a" stroke-width="2.4" stroke-dasharray="5 4"/>'),
 "two_three_d": dict(words=["الشكل الثلاثي الأبعاد", "الشكل الثنائي الأبعاد"], anim="wobble", face=(70, 62, .3), only=M,
   body='<rect x="4" y="40" width="34" height="34" fill="#6CB8FF" {OL}/><path d="M50 46 L76 46 L76 80 L50 80Z" fill="#F6B73C" {OL}/><path d="M50 46 L62 34 L88 34 L76 46Z" fill="#FFD25A" {OL}/><path d="M76 46 L88 34 L88 68 L76 80Z" fill="#E6A23C" {OL}/>'),
 "composite": dict(words=["الشكل المركب", "تجزئة الشكل", "مساحة الشكل المركب", "الأشكال المركبة"], anim="bob", face=(30, 70, .32), only=M,
   body='<path d="M8 20 L48 20 L48 54 L92 54 L92 90 L8 90Z" fill="#9CD86C" {OL}/><path d="M48 54 L48 90" stroke="#E8574A" stroke-width="3" stroke-dasharray="5 4"/>'),
 "parallelepiped": dict(words=["متوازي السطوح", "المنشور"], anim="wobble", face=(40, 62, .3), only=M,
   body='<path d="M10 40 L66 40 L66 90 L10 90Z" fill="#6CB8FF" {OL}/><path d="M10 40 L34 16 L90 16 L66 40Z" fill="#9FD8F0" {OL}/><path d="M66 40 L90 16 L90 66 L66 90Z" fill="#4A90D9" {OL}/>'),
 "tessellation": dict(words=["التبليط", "التبليط المنتظم", "التبليط شبه المنتظم", "الأنماط الهندسية"], anim="bob", face=(50, 50, .3), only=M,
   body='<path d="M2 2 L34 2 L34 34 L2 34Z M34 2 L66 2 L66 34 L34 34Z M66 2 L98 2 L98 34 L66 34Z" fill="#F6B73C" {OL}/><path d="M2 34 L34 34 L34 66 L2 66Z M66 34 L98 34 L98 66 L66 66Z" fill="#6CB8FF" {OL}/><path d="M34 34 L66 34 L66 66 L34 66Z" fill="#E8574A" {OL}/>'
        '<path d="M2 66 L34 66 L34 98 L2 98Z M34 66 L66 66 L66 98 L34 98Z M66 66 L98 66 L98 98 L66 98Z" fill="#F6B73C" {OL}/>'),
 "views": dict(words=["المنظر العلوي", "المنظر الجانبي", "المنظر الأمامي", "الرسم المنظوري", "مناظر المجسمات"], anim="bob", face=(40, 66, .3), only=M,
   body='<path d="M10 56 L36 56 L36 82 L10 82Z M36 56 L62 56 L62 82 L36 82Z M10 30 L36 30 L36 56 L10 56Z" fill="#6CB8FF" {OL}/><path d="M10 30 L22 18 L48 18 L36 30Z M36 56 L48 44 L74 44 L62 56Z" fill="#9FD8F0" {OL}/><path d="M36 30 L48 18 L48 44 L36 56Z M62 56 L74 44 L74 70 L62 82Z" fill="#4A90D9" {OL}/>'
        '<circle cx="88" cy="20" r="8" fill="#fff" {OL}/><circle cx="88" cy="20" r="3" fill="#3b2a1a"/><path d="M80 26 L70 34" stroke="#3b2a1a" stroke-width="2" stroke-dasharray="3 2"/>'),
 "slant": dict(words=["الارتفاع الجانبي", "الهرم", "المخروط"], anim="wobble", face=(36, 70, .3), only=M,
   body='<path d="M50 6 L10 80 L66 94 L90 70Z" fill="#F2C46D" {OL}/><path d="M50 6 L66 94" stroke="#3b2a1a" stroke-width="2"/><path d="M50 6 L38 87" stroke="#E8574A" stroke-width="3" stroke-dasharray="4 3"/>'),
 "isosceles": dict(words=["زاويتا القاعدة", "المثلث المتطابق الضلعين", "القاعدتان"], anim="wobble", face=(50, 62, .32), only=M,
   body='<path d="M50 8 L90 90 L10 90Z" fill="#9CD86C" {OL}/><path d="M28 46 L34 50 M66 50 L72 46" stroke="#3b2a1a" stroke-width="3"/><path d="M20 90 A10 10 0 0 0 16 80 M80 90 A10 10 0 0 1 84 80" fill="none" stroke="#E8574A" stroke-width="3"/>'),
 "right_congruence": dict(words=["LL", "HA", "LA", "HL", "تطابق المثلثات القائمة", "حالات التطابق"], anim="wobble", face=(30, 64, .3), only=M,
   body='<path d="M8 90 L8 30 L50 90Z" fill="#6CB8FF" {OL}/><path d="M50 90 L50 30 L92 90Z" fill="#6CB8FF" {OL}/><rect x="8" y="80" width="10" height="10" fill="none" stroke="#3b2a1a" stroke-width="2"/><rect x="50" y="80" width="10" height="10" fill="none" stroke="#3b2a1a" stroke-width="2"/>'
        '<path d="M26 56 L34 62 M68 56 L76 62" stroke="#E8574A" stroke-width="3"/>'),
 "perp_bisector": dict(words=["العمود المنصف", "متساوي البعد", "المنصفات"], anim="wobble", face=(50, 20, .3), only=M,
   body='<path d="M8 60 L92 60" stroke="#3b2a1a" stroke-width="4"/><circle cx="8" cy="60" r="4" fill="#3b2a1a"/><circle cx="92" cy="60" r="4" fill="#3b2a1a"/><path d="M50 8 L50 96" stroke="#E8574A" stroke-width="3"/>'
        '<rect x="50" y="50" width="10" height="10" fill="none" stroke="#E8574A" stroke-width="2"/><path d="M28 54 L28 66 M72 54 L72 66" stroke="#3b2a1a" stroke-width="2.4"/>'),
 "orthocenter": dict(words=["ملتقى الارتفاعات", "ملتقى المتوسطات", "ملتقى المنصفات", "مركز الثقل"], anim="sun", face=(50, 20, .3), only=M,
   body='<path d="M50 8 L94 88 L6 88Z" fill="#FFF3C4" {OL}/><path d="M50 8 L50 88 M94 88 L30 44 M6 88 L70 44" stroke="#6CB8FF" stroke-width="2"/><circle cx="50" cy="58" r="5" fill="#E8574A" {OL}/>'),
 "cyclic_quad": dict(words=["الشكل الرباعي الدائري", "الأوتار المتطابقة", "الأقواس المتطابقة"], anim="sun", face=(50, 50, .3), only=M,
   body='<circle cx="50" cy="50" r="42" fill="#fff" {OL}/><path d="M20 22 L82 24 L88 64 L30 86Z" fill="#9CD86C" opacity=".7" {OL}/>'),
 "parallel_planes": dict(words=["المستويات المتوازية", "المستويات"], anim="bob", face=(50, 30, .3), only=M,
   body='<path d="M10 24 L74 24 L90 40 L26 40Z" fill="#6CB8FF" {OL}/><path d="M10 58 L74 58 L90 74 L26 74Z" fill="#6CB8FF" {OL}/><path d="M30 42 L30 56 M70 42 L70 56" stroke="#3b2a1a" stroke-width="2" stroke-dasharray="3 3"/>'),
 "angle_pairs": dict(words=["الزاويتان المتجاورتان", "الزاويتان المتتامتان", "الزاويتان المتكاملتان", "الزاويتان الداخليتان البعيدتان", "الزوايا المتقابلة بالرأس"], anim="wobble", face=(76, 30, .3), only=M,
   body='<path d="M6 84 L94 84 M50 84 L18 22 M50 84 L94 34" fill="none" stroke="#3b2a1a" stroke-width="4" stroke-linecap="round"/>'
        '<path d="M40 64 A22 22 0 0 1 66 72" fill="none" stroke="#E8574A" stroke-width="4"/><path d="M68 74 A22 22 0 0 1 72 84" fill="none" stroke="#6CB8FF" stroke-width="4"/>'),
 # ---------- algebra cards ----------
 "expression": dict(words=["العبارة العددية", "العبارة", "إيجاد قيمة العبارة", "التعويض"], anim="bob", face=(50, 76, .3), only=M, body=card("3 + x", "#6CB8FF", 28, 58)),
 "unknown": dict(words=["المجهول", "الترجمة من اللفظ إلى الرموز", "الرموز الجبرية"], anim="bounce", face=(50, 76, .3), only=M,
   body='<rect x="26" y="10" width="48" height="48" rx="8" fill="#FFD25A" {OL}/><text direction="ltr" x="50" y="46" text-anchor="middle" font-size="34" font-weight="800" fill="#3b2a1a" font-family="serif">x</text>'),
 "function_machine": dict(words=["المدخلة", "المخرجة", "المدخلات والمخرجات", "آلة الدالة"], anim="sun", face=(50, 54, .3), only=M,
   body='<rect x="30" y="30" width="40" height="44" rx="6" fill="#AEB8C4" {OL}/><circle cx="50" cy="52" r="10" fill="#fff" {OL}/><path d="M50 42 L50 62 M40 52 L60 52" stroke="#3b2a1a" stroke-width="2"/>'
        '<path d="M2 52 L28 52 M22 46 L28 52 L22 58 M72 52 L98 52 M92 46 L98 52 L92 58" fill="none" stroke="#E8574A" stroke-width="3"/><text direction="ltr" x="14" y="44" text-anchor="middle" font-size="12" font-weight="800" fill="#3b2a1a" font-family="sans-serif">2</text><text direction="ltr" x="86" y="44" text-anchor="middle" font-size="12" font-weight="800" fill="#3b2a1a" font-family="sans-serif">6</text>'),
 "terms": dict(words=["الحد", "الحد النوني", "حدود المتتابعة", "الأوساط الحسابية", "الأوساط الهندسية", "المجموع الجزئي"], anim="bounce", face=(50, 84, .3), only=M,
   body='<circle cx="14" cy="40" r="10" fill="#6CB8FF" {OL}/><circle cx="38" cy="40" r="10" fill="#6CB8FF" {OL}/><circle cx="62" cy="40" r="10" fill="#6CB8FF" {OL}/><circle cx="86" cy="40" r="10" fill="#E8574A" {OL}/>'
        '<text direction="ltr" x="86" y="45" text-anchor="middle" font-size="11" font-weight="800" fill="#fff" font-family="sans-serif">aₙ</text><path d="M24 40 L28 40 M48 40 L52 40 M72 40 L76 40" stroke="#3b2a1a" stroke-width="2"/>'),
 "polynomial": dict(words=["وحيدة الحد", "ثلاثية الحد", "درجة وحيدة الحد"], anim="bob", face=(50, 78, .3), only=M, body=card("x²+3x+2", "#9B6CD9", 18, 56)),
 "reciprocal": dict(words=["المقلوب", "النظير الضربي"], anim="bounce", face=(50, 78, .3), only=M, body=card("1/x", "#6CC27A", 30, 60)),
 "opposite": dict(words=["النظير الجمعي", "الأعداد المتعاكسة"], anim="bounce", face=(50, 78, .3), only=M, body=card("a , −a", "#F6B73C", 24, 58)),
 "inverse_ops": dict(words=["العمليات العكسية", "العملية العكسية"], anim="sun", face=(50, 50, .3), only=M,
   body='<path d="M20 40 C30 20 70 20 80 40 M72 32 L80 40 L88 32 M80 60 C70 80 30 80 20 60 M28 68 L20 60 L12 68" fill="none" stroke="#3b2a1a" stroke-width="4" stroke-linecap="round"/>'
        '<text direction="ltr" x="50" y="24" text-anchor="middle" font-size="16" font-weight="800" fill="#6CC27A" font-family="sans-serif">+</text><text direction="ltr" x="50" y="90" text-anchor="middle" font-size="16" font-weight="800" fill="#E8574A" font-family="sans-serif">−</text>'),
 "simplify": dict(words=["التبسيط", "أبسط صورة", "تبسيط الكسور"], anim="bounce", face=(50, 84, .3), only=M, body=card("6/8 → 3/4", "#6CB8FF", 18, 56)),
 "divisors": dict(words=["القاسم", "القواسم", "القاسم المشترك"], anim="bob", face=(50, 84, .3), only=M,
   body='<circle cx="30" cy="40" r="22" fill="#6CB8FF" opacity=".6" {OL}/><circle cx="70" cy="40" r="22" fill="#F6B73C" opacity=".6" {OL}/>'
        '<text direction="ltr" x="22" y="44" text-anchor="middle" font-size="11" font-weight="800" fill="#3b2a1a" font-family="sans-serif">4</text><text direction="ltr" x="50" y="44" text-anchor="middle" font-size="12" font-weight="800" fill="#3b2a1a" font-family="sans-serif">2</text><text direction="ltr" x="78" y="44" text-anchor="middle" font-size="11" font-weight="800" fill="#3b2a1a" font-family="sans-serif">3</text>'),
 "division_parts": dict(words=["المقسوم", "المقسوم عليه", "ناتج القسمة", "باقي القسمة", "التوزيع بالتساوي"], anim="bob", face=(50, 84, .3), only=M, body=card("12 ÷ 3", "#E8574A", 26, 58)),
 "brackets": dict(words=["الأقواس", "ترتيب العمليات", "أولويات العمليات"], anim="bob", face=(50, 84, .3), only=M, body=card("( 2+3 )×4", "#9CD86C", 18, 56)),
 "power": dict(words=["الأساس", "التكعيب", "التربيع", "القوى والأسس"], anim="bounce", face=(50, 84, .3), only=M, body=card("x³", "#9B6CD9", 34, 62)),
 "radical": dict(words=["العبارة الجذرية", "المرافق", "المرافق المركب"], anim="bob", face=(50, 84, .3), only=M, body=card("√x", "#6CB8FF", 32, 62)),
 "discriminant": dict(words=["المميز", "الصيغة العامة"], anim="bob", face=(50, 84, .3), only=M, body=card("b²−4ac", "#F6B73C", 22, 58)),
 "rational_expr": dict(words=["العبارة النسبية", "الدالة النسبية", "الدوال النسبية"], anim="bob", face=(50, 84, .3), only=M, body=card("(x+1)/(x−2)", "#6CC27A", 14, 56)),
 "factorial": dict(words=["المضروب"], anim="bounce", face=(50, 84, .3), only=M, body=card("n!", "#E8574A", 34, 62)),
 "pi": dict(words=["ط (π)", "النسبة التقريبية", "π"], anim="sun", face=(50, 84, .3), only=M, body=card("π", "#FFD25A", 40, 64)),
 "imaginary": dict(words=["الوحدة التخيلية", "المحور الحقيقي", "المحور التخيلي", "المستوى المركب", "نظرية ديموافر"], anim="sun", face=(70, 72, .3), only=M,
   body='<path d="M50 6 L50 94 M6 50 L94 50" stroke="#3b2a1a" stroke-width="3"/><path d="M50 50 L76 24" stroke="#E8574A" stroke-width="4" stroke-linecap="round"/><circle cx="76" cy="24" r="5" fill="#E8574A" {OL}/>'
        '<text direction="ltr" x="58" y="14" font-size="14" font-weight="800" fill="#3b2a1a" font-family="serif">i</text>'),
 "polar": dict(words=["القطب", "المحور القطبي", "الإحداثيات القطبية"], anim="sun", face=(76, 70, .3), only=M,
   body='<circle cx="30" cy="70" r="24" fill="none" stroke="#AEB8C4" stroke-width="2"/><circle cx="30" cy="70" r="44" fill="none" stroke="#AEB8C4" stroke-width="2"/><path d="M30 70 L98 70" stroke="#3b2a1a" stroke-width="3"/>'
        '<path d="M30 70 L66 30" stroke="#E8574A" stroke-width="4" stroke-linecap="round"/><circle cx="66" cy="30" r="5" fill="#E8574A" {OL}/><circle cx="30" cy="70" r="4" fill="#3b2a1a"/><path d="M48 70 A18 18 0 0 0 42 57" fill="none" stroke="#6CB8FF" stroke-width="3"/>'),
 "axis_z": dict(words=["المحور z", "الفضاء الثلاثي الأبعاد", "الإحداثيات في الفضاء"], anim="sun", face=(70, 76, .3), only=M,
   body='<path d="M40 60 L40 6 M40 60 L96 60 M40 60 L8 92" stroke="#3b2a1a" stroke-width="3"/><path d="M34 14 L40 6 L46 14 M88 54 L96 60 L88 66 M10 82 L8 92 L18 90" fill="none" stroke="#3b2a1a" stroke-width="3"/>'
        '<text direction="ltr" x="48" y="14" font-size="12" font-weight="800" fill="#E8574A" font-family="sans-serif">z</text><text direction="ltr" x="88" y="76" font-size="12" font-weight="800" fill="#3b2a1a" font-family="sans-serif">x</text><text direction="ltr" x="18" y="98" font-size="12" font-weight="800" fill="#3b2a1a" font-family="sans-serif">y</text>'),
 # ---------- graphs ----------
 "asymptote": dict(words=["خط التقارب", "خط التقارب الأفقي", "خط التقارب المائل", "خط التقارب الرأسي", "خطوط التقارب"], anim="sway", face=(70, 80, .3), only=M,
   body='<path d="M6 50 L94 50 M50 6 L50 94" stroke="#AEB8C4" stroke-width="2"/><path d="M56 8 C58 30 66 42 94 44" fill="none" stroke="#6CB8FF" stroke-width="4"/><path d="M44 92 C42 70 34 58 6 56" fill="none" stroke="#6CB8FF" stroke-width="4"/>'
        '<path d="M50 4 L50 96" stroke="#E8574A" stroke-width="2" stroke-dasharray="5 4"/>'),
 "horizontal_test": dict(words=["اختبار الخط الأفقي", "الدالة العكسية", "العلاقة العكسية", "الدالة المتباينة"], anim="sway", face=(30, 80, .3), only=M,
   body='<path d="M6 90 L94 90 M10 94 L10 6" stroke="#3b2a1a" stroke-width="3"/><path d="M14 84 C34 80 50 60 60 40 C68 24 80 14 92 10" fill="none" stroke="#6CB8FF" stroke-width="4"/><path d="M4 48 L96 48" stroke="#E8574A" stroke-width="3" stroke-dasharray="6 4"/><circle cx="58" cy="44" r="4" fill="#E8574A"/>'),
 "max_min": dict(words=["القيمة العظمى", "القيمة الصغرى", "القيم القصوى", "رأس القطع المكافئ"], anim="bounce", face=(50, 84, .3), only=M,
   body='<path d="M4 70 L96 70" stroke="#AEB8C4" stroke-width="2"/><path d="M8 90 C24 10 76 10 92 90" fill="none" stroke="#6CB8FF" stroke-width="4"/><circle cx="50" cy="30" r="6" fill="#E8574A" {OL}/>'),
 "zeros": dict(words=["أصفار الدالة", "جذور المعادلة", "نقاط التقاطع"], anim="bounce", face=(50, 30, .3), only=M,
   body='<path d="M4 60 L96 60" stroke="#3b2a1a" stroke-width="3"/><path d="M8 20 C22 100 46 100 54 60 C62 20 82 20 92 80" fill="none" stroke="#6CB8FF" stroke-width="4"/><circle cx="17" cy="60" r="5" fill="#E8574A" {OL}/><circle cx="54" cy="60" r="5" fill="#E8574A" {OL}/><circle cx="87" cy="60" r="5" fill="#E8574A" {OL}/>'),
 "variation": dict(words=["التغير الطردي", "التغير العكسي", "التغير المشترك", "التغير المركب", "العلاقة المتناسبة", "العلاقة غير المتناسبة", "العلاقة الخطية", "الكميات المتناسبة"], anim="sway", face=(30, 30, .3), only=M,
   body='<path d="M6 92 L94 92 M8 94 L8 6" stroke="#3b2a1a" stroke-width="3"/><path d="M8 92 L88 16" stroke="#6CB8FF" stroke-width="4"/><path d="M18 10 C22 50 40 74 92 80" fill="none" stroke="#E8574A" stroke-width="4"/>'),
 "domain": dict(words=["المجال", "المجال والمدى"], anim="bob", face=(50, 84, .3), only=M,
   body='<ellipse cx="24" cy="44" rx="18" ry="30" fill="#BFE3F2" {OL}/><ellipse cx="76" cy="44" rx="18" ry="30" fill="#FFF3C4" {OL}/>'
        '<path d="M28 28 L70 30 M28 44 L70 50 M28 60 L70 50" stroke="#3b2a1a" stroke-width="2"/><path d="M64 26 L70 30 L64 34" fill="none" stroke="#3b2a1a" stroke-width="2"/><circle cx="24" cy="28" r="3" fill="#3b2a1a"/><circle cx="24" cy="44" r="3" fill="#3b2a1a"/><circle cx="24" cy="60" r="3" fill="#3b2a1a"/>'),
 "matrix": dict(words=["العنصر", "الرتبة", "المحدد", "قاعدة كرامر", "العمليات الصفية", "الصورة الدرجية"], anim="bob", face=(50, 84, .3), only=M,
   body='<path d="M20 12 L12 12 L12 70 L20 70 M80 12 L88 12 L88 70 L80 70" fill="none" stroke="#3b2a1a" stroke-width="4"/>'
        '<text direction="ltr" x="32" y="34" text-anchor="middle" font-size="16" font-weight="800" fill="#3b2a1a" font-family="sans-serif">2</text><text direction="ltr" x="68" y="34" text-anchor="middle" font-size="16" font-weight="800" fill="#3b2a1a" font-family="sans-serif">1</text><text direction="ltr" x="32" y="60" text-anchor="middle" font-size="16" font-weight="800" fill="#3b2a1a" font-family="sans-serif">0</text><text direction="ltr" x="68" y="60" text-anchor="middle" font-size="16" font-weight="800" fill="#E8574A" font-family="sans-serif">3</text>'),
 "linprog": dict(words=["القيود", "الحل الأمثل", "البرمجة الخطية"], anim="bob", face=(36, 64, .3), only=M,
   body='<path d="M6 92 L94 92 M8 94 L8 6" stroke="#3b2a1a" stroke-width="3"/><path d="M8 30 L60 92 M8 70 L90 40" stroke="#6CB8FF" stroke-width="3"/><path d="M8 92 L8 70 L33 61 L60 92Z" fill="#9CD86C" opacity=".8"/><circle cx="33" cy="61" r="5" fill="#E8574A" {OL}/>'),
 "distance": dict(words=["المسافة بين نقطتين", "صيغة المسافة", "نقطة المنتصف", "صيغة نقطة المنتصف"], anim="bob", face=(50, 84, .3), only=M,
   body='<path d="M6 92 L94 92 M8 94 L8 6" stroke="#AEB8C4" stroke-width="2"/><circle cx="22" cy="70" r="6" fill="#6CB8FF" {OL}/><circle cx="80" cy="20" r="6" fill="#6CB8FF" {OL}/><path d="M22 70 L80 20" stroke="#E8574A" stroke-width="3"/><path d="M22 70 L80 70 L80 20" fill="none" stroke="#3b2a1a" stroke-width="2" stroke-dasharray="4 3"/>'),
 "venn_ops": dict(words=["التقاطع", "الاتحاد"], anim="bob", face=(50, 86, .3), only=M,
   body='<circle cx="36" cy="46" r="28" fill="#6CB8FF" opacity=".5" {OL}/><circle cx="64" cy="46" r="28" fill="#F6B73C" opacity=".5" {OL}/><path d="M50 22 C60 30 60 62 50 70 C40 62 40 30 50 22Z" fill="#E8574A"/>'),
 "elimination": dict(words=["الحذف", "الحذف بالجمع", "الحذف بالضرب", "التعويض المباشر", "حل نظام معادلتين"], anim="bob", face=(50, 86, .3), only=M,
   body='<rect x="10" y="10" width="80" height="70" rx="8" fill="#fff" {OL}/><text direction="ltr" x="50" y="34" text-anchor="middle" font-size="14" font-weight="800" fill="#3b2a1a" font-family="sans-serif">x + y = 5</text>'
        '<text direction="ltr" x="50" y="56" text-anchor="middle" font-size="14" font-weight="800" fill="#3b2a1a" font-family="sans-serif">x − y = 1</text><path d="M26 30 L36 26 M64 30 L74 26 M26 52 L36 48 M64 52 L74 48" stroke="#E8574A" stroke-width="2.4"/>'),
 # ---------- conics ----------
 "ellipse": dict(words=["القطع الناقص", "البؤرتان", "المحور الأكبر", "المحور الأصغر", "تحديد نوع القطع", "القطوع المخروطية"], anim="sun", face=(50, 84, .3), only=M,
   body='<ellipse cx="50" cy="46" rx="44" ry="28" fill="#E8F6FF" {OL}/><path d="M6 46 L94 46 M50 18 L50 74" stroke="#AEB8C4" stroke-width="2"/><circle cx="24" cy="46" r="4" fill="#E8574A"/><circle cx="76" cy="46" r="4" fill="#E8574A"/>'),
 "hyperbola": dict(words=["القطع الزائد", "المحور المرافق", "المحور القاطع"], anim="sway", face=(50, 86, .3), only=M,
   body='<path d="M6 8 C30 30 30 70 6 92 M94 8 C70 30 70 70 94 92" fill="none" stroke="#6CB8FF" stroke-width="4"/><path d="M10 10 L90 90 M90 10 L10 90" stroke="#AEB8C4" stroke-width="1.6" stroke-dasharray="4 3"/><circle cx="16" cy="50" r="4" fill="#E8574A"/><circle cx="84" cy="50" r="4" fill="#E8574A"/>'),
 "parabola_focus": dict(words=["البؤرة", "الاختلاف المركزي"], anim="sway", face=(50, 86, .3), only=M,
   body='<path d="M8 10 C24 90 76 90 92 10" fill="none" stroke="#6CB8FF" stroke-width="4"/><path d="M4 90 L96 90" stroke="#E8574A" stroke-width="3" stroke-dasharray="6 4"/><circle cx="50" cy="44" r="5" fill="#E8574A" {OL}/>'),
 # ---------- statistics ----------
 "survey": dict(words=["الاستطلاع", "الدراسة المسحية", "الدراسة التجريبية", "جمع البيانات بالاستطلاع", "العينة"], anim="bob", face=(30, 72, .3), only=M,
   body='<rect x="10" y="12" width="64" height="82" rx="6" fill="#fff" {OL}/><rect x="28" y="6" width="28" height="12" rx="4" fill="#AEB8C4" {OL}/>'
        '<rect x="20" y="30" width="10" height="10" fill="none" stroke="#3b2a1a" stroke-width="2"/><rect x="20" y="50" width="10" height="10" fill="none" stroke="#3b2a1a" stroke-width="2"/><path d="M21 52 L25 58 L32 48" fill="none" stroke="#6CC27A" stroke-width="3"/>'
        '<path d="M38 35 L64 35 M38 55 L64 55 M38 75 L58 75" stroke="#AEB8C4" stroke-width="3"/><path d="M78 70 L94 30 L98 32 L82 72 L76 76Z" fill="#FFD25A" {OL}/>'),
 "sector": dict(words=["القطاع", "القطاع الدائري"], anim="sun", face=(40, 60, .3), only=M,
   body='<circle cx="46" cy="54" r="40" fill="#BFE3F2" {OL}/><path d="M50 50 L50 8 A42 42 0 0 1 90 40Z" fill="#E8574A" {OL}/>'),
 "double_bar": dict(words=["التمثيل بالأعمدة المزدوجة", "التمثيلات البيانية", "اختيار التمثيل المناسب", "التدريج", "العنوان"], anim="bounce", face=(50, 20, .3), only=M,
   body='<path d="M6 92 L94 92 M8 94 L8 6" stroke="#3b2a1a" stroke-width="3"/><rect x="16" y="50" width="10" height="42" fill="#6CB8FF" {OL}/><rect x="26" y="36" width="10" height="56" fill="#F6B73C" {OL}/>'
        '<rect x="46" y="30" width="10" height="62" fill="#6CB8FF" {OL}/><rect x="56" y="44" width="10" height="48" fill="#F6B73C" {OL}/><rect x="76" y="60" width="10" height="32" fill="#6CB8FF" {OL}/><rect x="86" y="24" width="10" height="68" fill="#F6B73C" {OL}/>'),
 "outlier": dict(words=["القيمة المتطرفة", "التجمع", "الفجوة"], anim="bounce", face=(50, 30, .3), only=M,
   body='<path d="M4 80 L96 80" stroke="#3b2a1a" stroke-width="3"/><circle cx="16" cy="70" r="5" fill="#6CB8FF"/><circle cx="16" cy="58" r="5" fill="#6CB8FF"/><circle cx="28" cy="70" r="5" fill="#6CB8FF"/><circle cx="28" cy="58" r="5" fill="#6CB8FF"/><circle cx="28" cy="46" r="5" fill="#6CB8FF"/><circle cx="40" cy="70" r="5" fill="#6CB8FF"/>'
        '<circle cx="88" cy="70" r="6" fill="#E8574A" {OL}/>'),
 "quartiles": dict(words=["الأرباع", "التمثيل بالصندوق وطرفيه", "المدى الربيعي", "الربيع الأدنى", "الربيع الأعلى"], anim="bob", face=(50, 80, .3), only=M,
   body='<path d="M8 40 L28 40 M72 40 L92 40 M8 30 L8 50 M92 30 L92 50" stroke="#3b2a1a" stroke-width="3"/><rect x="28" y="24" width="44" height="32" fill="#BFE3F2" {OL}/><path d="M48 24 L48 56" stroke="#E8574A" stroke-width="4"/>'),
 "normal": dict(words=["التوزيع الطبيعي", "المنحنى الطبيعي", "التوزيع الملتوي", "القيمة المعيارية (z)", "القيمة المعيارية", "الإحصائي"], anim="sway", face=(50, 50, .3), only=M,
   body='<path d="M4 88 L96 88" stroke="#3b2a1a" stroke-width="3"/><path d="M6 86 C30 86 34 14 50 14 C66 14 70 86 94 86" fill="#E8F6FF" {OL}/><path d="M50 14 L50 88" stroke="#E8574A" stroke-width="2" stroke-dasharray="4 3"/>'),
 "binomial": dict(words=["تجربة ذات الحدين", "التوزيع ذو الحدين", "نظرية ذات الحدين", "مثلث باسكال"], anim="bounce", face=(50, 20, .3), only=M,
   body='<path d="M4 92 L96 92" stroke="#3b2a1a" stroke-width="3"/><rect x="10" y="80" width="12" height="12" fill="#6CB8FF" {OL}/><rect x="24" y="56" width="12" height="36" fill="#6CB8FF" {OL}/><rect x="38" y="36" width="12" height="56" fill="#6CB8FF" {OL}/>'
        '<rect x="52" y="36" width="12" height="56" fill="#6CB8FF" {OL}/><rect x="66" y="56" width="12" height="36" fill="#6CB8FF" {OL}/><rect x="80" y="80" width="12" height="12" fill="#6CB8FF" {OL}/>'),
 # ---------- logic, trigonometry, the rest ----------
 "logic_and_or": dict(words=["العبارة المركبة", "أداة الربط (و)", "أداة الربط (أو)", "النفي", "قيمة الصواب", "جداول الصواب", "الوصل والفصل"], anim="bob", face=(50, 84, .3), only=M, body=card("p ∧ q", "#9B6CD9", 26, 58)),
 "if_then": dict(words=["الفرض", "النتيجة", "العكس", "إذا وفقط إذا"], anim="bob", face=(50, 84, .3), only=M, body=card("p → q", "#6CB8FF", 28, 58)),
 "postulate": dict(words=["مسلمة المسطرة", "التبرير غير المباشر"], anim="bob", face=(30, 70, .3), only=M,
   body='<rect x="8" y="10" width="70" height="84" rx="4" fill="#fff" {OL}/><path d="M18 26 L60 26 M18 38 L66 38 M18 50 L56 50" stroke="#AEB8C4" stroke-width="2.4"/><path d="M48 74 L56 82 L72 64" fill="none" stroke="#6CC27A" stroke-width="5" stroke-linecap="round"/>'
        '<rect x="54" y="88" width="40" height="8" fill="#FFD25A" {OL}/>'),
 "trig_identity": dict(words=["متطابقات المقلوب", "متطابقات الزاويتين المتتامتين", "إثبات صحة المتطابقة", "تحويل أحد الطرفين", "متطابقات المجموع", "متطابقات الفرق"], anim="bob", face=(50, 84, .3), only=M,
   body=card("sin²+cos²=1", "#6CC27A", 14, 56)),
 "trig_solutions": dict(words=["الحل العام", "الحلول في فترة", "القيم الأساسية", "التردد", "الدوال الدورية"], anim="sway", face=(50, 86, .3), only=M,
   body='<path d="M4 50 L96 50" stroke="#3b2a1a" stroke-width="2"/><path d="M4 50 C14 14 24 14 30 50 C36 86 46 86 52 50 C58 14 68 14 74 50 C80 86 90 86 96 50" fill="none" stroke="#6CB8FF" stroke-width="4"/>'
        '<path d="M4 30 L96 30" stroke="#E8574A" stroke-width="2" stroke-dasharray="5 4"/><circle cx="12" cy="30" r="3.6" fill="#E8574A"/><circle cx="22" cy="30" r="3.6" fill="#E8574A"/><circle cx="56" cy="30" r="3.6" fill="#E8574A"/><circle cx="70" cy="30" r="3.6" fill="#E8574A"/>'),
 "heron": dict(words=["صيغة هيرون", "قانون الجيب", "قانون جيب التمام"], anim="wobble", face=(46, 66, .3), only=M,
   body='<path d="M8 86 L40 14 L94 86Z" fill="#FFF3C4" {OL}/><text direction="ltr" x="18" y="48" font-size="14" font-weight="800" fill="#3b2a1a" font-family="serif">a</text><text direction="ltr" x="72" y="46" font-size="14" font-weight="800" fill="#3b2a1a" font-family="serif">b</text><text direction="ltr" x="48" y="98" font-size="14" font-weight="800" fill="#3b2a1a" font-family="serif">c</text>'),
 "log_base": dict(words=["صيغة تغيير الأساس"], anim="bob", face=(50, 84, .3), only=M, body=card("logₐ b", "#F6B73C", 24, 58)),
 "limit": dict(words=["الصيغة غير المحددة", "التعويض التركيبي"], anim="bob", face=(50, 84, .3), only=M, body=card("lim 0/0", "#E8574A", 22, 58)),
 "induction": dict(words=["فرضية الاستقراء", "الخطوة الاستقرائية"], anim="wobble", face=(84, 70, .3), only=M,
   body='<path d="M2 92 L98 92" stroke="#3b2a1a" stroke-width="4"/><rect x="8" y="34" width="12" height="58" rx="2" fill="#6CB8FF" {OL} transform="rotate(32 14 92)"/><rect x="30" y="34" width="12" height="58" rx="2" fill="#6CB8FF" {OL} transform="rotate(20 36 92)"/>'
        '<rect x="52" y="34" width="12" height="58" rx="2" fill="#6CB8FF" {OL} transform="rotate(8 58 92)"/><rect x="76" y="34" width="12" height="58" rx="2" fill="#6CB8FF" {OL}/><text direction="ltr" x="82" y="28" text-anchor="middle" font-size="12" font-weight="800" fill="#3b2a1a" font-family="sans-serif">k+1</text>'),
 "price_commission": dict(words=["الثمن", "العمولة", "سعر البيع", "سعر الشراء", "الربح والخسارة في التجارة"], anim="wobble", face=(56, 40, .3), only=M,
   body='<path d="M8 50 L44 14 L90 14 L90 60 L54 96Z" fill="#9CD86C" {OL}/><circle cx="74" cy="30" r="6" fill="#fff" {OL}/><text direction="ltr" x="56" y="66" text-anchor="middle" font-size="22" font-weight="800" fill="#3b2a1a" font-family="sans-serif" transform="rotate(-45 56 60)">$</text>'),
 "transform_geo": dict(words=["التحويل الهندسي", "الإزاحة", "التكبير", "التصغير", "الانعكاس", "الدوران"], anim="bounce", face=(76, 60, .3), only=M,
   body='<path d="M8 80 L28 80 L18 60Z" fill="#AEB8C4" {OL}/><path d="M50 90 L90 90 L70 50Z" fill="#6CB8FF" {OL}/><path d="M30 70 L50 70 M44 64 L50 70 L44 76" fill="none" stroke="#E8574A" stroke-width="3"/>'),
 "center_height": dict(words=["ارتفاع المثلث", "الارتفاع في المثلث"], anim="sun", face=(50, 80, .3), only=M,
   body='<circle cx="50" cy="44" r="38" fill="#fff" {OL}/><circle cx="50" cy="44" r="4" fill="#E8574A"/><path d="M50 44 L84 28" stroke="#6CB8FF" stroke-width="3"/>'),
 "model_math": dict(words=["النمذجة", "النموذج", "المخطط"], anim="bob", face=(30, 70, .3), only=M,
   body='<rect x="8" y="20" width="40" height="60" rx="4" fill="#F6B73C" {OL}/><path d="M8 40 L48 40 M8 60 L48 60 M28 20 L28 80" stroke="#3b2a1a" stroke-width="2"/>'
        '<path d="M54 50 L64 50 M60 46 L64 50 L60 54" fill="none" stroke="#3b2a1a" stroke-width="2.4"/><text direction="ltr" x="82" y="56" text-anchor="middle" font-size="16" font-weight="800" fill="#3b2a1a" font-family="sans-serif">2×3</text>'),
 "predict_math": dict(words=["التنبؤ", "التخمين والتحقق"], anim="bounce", face=(30, 70, .3), only=M,
   body='<path d="M6 90 L94 90 M8 92 L8 8" stroke="#3b2a1a" stroke-width="3"/><path d="M10 80 L30 66 L50 60 L66 44" fill="none" stroke="#6CB8FF" stroke-width="4" stroke-linecap="round"/><path d="M66 44 L90 20" stroke="#E8574A" stroke-width="4" stroke-dasharray="5 4" stroke-linecap="round"/>'),
 "work_vector": dict(words=["الشغل", "التوافق الخطي"], anim="bounce", face=(30, 50, .3), only=M,
   body='<rect x="12" y="34" width="36" height="36" rx="4" fill="#C98A55" {OL}/><path d="M2 70 L98 70" stroke="#3b2a1a" stroke-width="3"/><path d="M48 52 L88 30 M80 28 L88 30 L84 38" fill="none" stroke="#E8574A" stroke-width="4" stroke-linecap="round"/>'
        '<path d="M56 84 L92 84 M86 80 L92 84 L86 88" fill="none" stroke="#6CB8FF" stroke-width="3"/>'),
}
ALIAS_ONLY = None
ALIASES = {"النظرية الأساسية في الجبر": ("math.variable", ("math",)), "المسلمة": ("math2.postulate", ("math",)), "المسلمات": ("math2.postulate", ("math",)), "النظرية": ("math2.postulate", ("math",)), "النظريات": ("math2.postulate", ("math",)), "المسلمات والنظريات": ("math2.postulate", ("math",)), "متجه الإزاحة": ("math.vector", ("math",)), }
