"""🆕 batch 43 · the English book's themes (الإنجليزي): fixing and inviting, the youth centre and clubs, events, story plots and
mysteries (a detective, clues, treasure), time words (since, an appointment, a time capsule), people (celebrities, twins, a leader,
an inventor, athletes, a manager), jokes and laughter, wildlife and migration, dilemmas, fashion and inner beauty, lost property,
smoke signals, TV channels and audiences, roles, grammar cards (plurals, emphasis, quotes, reported questions, the 3rd conditional).
Only for English books (the same Arabic word can mean something else elsewhere)."""
F = "en2"
EN = ["english"]


def gcard(txt, color="#6CB8FF", size=18):
    return (f'<rect x="6" y="18" width="88" height="64" rx="12" fill="{color}" {{OL}}/><rect x="12" y="24" width="76" height="52" rx="8" fill="#fff"/>'
            f'<text direction="ltr" x="50" y="58" text-anchor="middle" font-size="{size}" font-weight="800" fill="#3b2a1a" font-family="sans-serif">{txt}</text>')


D = {
 "fix": dict(words=["يصلح", "إصلاح الأشياء", "يصلّح"], anim="wobble", face=(40, 64, .36), only=EN,
   body='<path d="M14 92 L54 52 C48 40 54 22 70 22 L62 32 L68 40 L78 32 C80 48 66 56 56 52 L22 96Z" fill="#AEB8C4" {OL}/><path d="M60 70 L90 70 L90 94 L60 94Z" fill="#E8574A" {OL}/>'),
 "invite": dict(words=["يدعو", "بطاقة الدعوة"], anim="bounce", face=(50, 62, .34), only=EN,
   body='<rect x="8" y="26" width="84" height="60" rx="6" fill="#fff" {OL}/><path d="M8 28 L50 60 L92 28" fill="none" stroke="#3b2a1a" stroke-width="2.6"/><path d="M50 22 C44 12 34 18 40 26 L50 34 L60 26 C66 18 56 12 50 22Z" fill="#E8574A" {OL}/>'),
 "youth_center": dict(words=["مركز الشباب", "النادي الرياضي", "الأنشطة الشبابية"], anim="bob", face=(36, 70, .32), only=EN,
   body='<path d="M6 40 L50 12 L94 40 L94 94 L6 94Z" fill="#F2D07A" {OL}/><rect x="38" y="64" width="24" height="30" fill="#8B5E3C" {OL}/><circle cx="74" cy="56" r="10" fill="#fff" {OL}/><path d="M74 46 L80 52 L78 60 L70 60 L68 52Z" fill="#3b2a1a"/>'
        '<rect x="14" y="50" width="16" height="12" fill="#6CB8FF" {OL}/>'),
 "drawing_art": dict(words=["الرسم", "الرسام", "اللوحة الفنية", "الفنون التشكيلية"], anim="sway", face=(50, 40, .34), only=EN + ["art"],
   body='<rect x="16" y="10" width="68" height="56" rx="3" fill="#fff" {OL}/><path d="M24 54 L40 34 L52 46 L62 38 L76 54Z" fill="#9CD86C"/><circle cx="66" cy="24" r="6" fill="#FFD25A"/>'
        '<path d="M30 66 L18 96 M70 66 L82 96 M50 66 L50 90" stroke="#8B5E3C" stroke-width="5" stroke-linecap="round"/>'),
 "plot": dict(words=["حبكة القصة", "الحبكة", "أحداث القصة", "عناصر القصة", "القصة القصيرة"], anim="bob", face=(50, 76, .3), only=EN + ["arabic"],
   body='<path d="M6 40 C22 32 38 34 50 42 C62 34 78 32 94 40 L94 90 C78 82 62 84 50 92 C38 84 22 82 6 90Z" fill="#fff" {OL}/><path d="M50 42 L50 92" stroke="#3b2a1a" stroke-width="2.4"/>'
        '<path d="M10 30 C30 30 40 4 50 4 C60 4 70 30 90 30" fill="none" stroke="#E8574A" stroke-width="4" stroke-linecap="round"/><circle cx="50" cy="4" r="4" fill="#E8574A"/>'),
 "club": dict(words=["نادٍ", "الاشتراك في نادٍ", "النادي", "العضوية", "نادي القراءة"], anim="bounce", face=(36, 54, .34), only=EN,
   body='<rect x="8" y="22" width="84" height="56" rx="8" fill="#6CB8FF" {OL}/><circle cx="32" cy="50" r="14" fill="#fff" {OL}/><path d="M54 40 L82 40 M54 52 L78 52 M54 64 L70 64" stroke="#fff" stroke-width="4" stroke-linecap="round"/>'),
 "event": dict(words=["حدث", "حدث رياضي", "الفعاليات", "المناسبات"], anim="bounce", face=(50, 66, .34), only=EN,
   body='<rect x="10" y="20" width="80" height="74" rx="6" fill="#fff" {OL}/><rect x="10" y="20" width="80" height="18" rx="6" fill="#E8574A" {OL}/><path d="M30 12 L30 28 M70 12 L70 28" stroke="#3b2a1a" stroke-width="5" stroke-linecap="round"/>'
        '<path d="M50 44 L56 58 L70 58 L58 66 L62 80 L50 72 L38 80 L42 66 L30 58 L44 58Z" fill="#FFD25A" {OL}/>'),
 "titles": dict(words=["الألقاب", "ألقاب الأشخاص", "الأسماء والألقاب"], anim="bob", face=(30, 56, .34), only=EN, body=gcard("Mr. · Dr.", "#9B6CD9", 16)),
 "plurals": dict(words=["الجمع المنتظم والشاذ", "الجمع", "صيغ الجمع", "المفرد والجمع"], anim="bounce", face=(20, 30, .3), only=EN,
   body='<circle cx="20" cy="40" r="14" fill="#E8574A" {OL}/><path d="M38 40 L50 40 M46 36 L50 40 L46 44" fill="none" stroke="#3b2a1a" stroke-width="2.4"/>'
        '<circle cx="64" cy="30" r="10" fill="#E8574A" {OL}/><circle cx="86" cy="30" r="10" fill="#E8574A" {OL}/><circle cx="64" cy="54" r="10" fill="#E8574A" {OL}/><circle cx="86" cy="54" r="10" fill="#E8574A" {OL}/>'
        '<text direction="ltr" x="20" y="82" text-anchor="middle" font-size="12" font-weight="800" fill="#3b2a1a" font-family="sans-serif">apple</text><text direction="ltr" x="76" y="82" text-anchor="middle" font-size="12" font-weight="800" fill="#3b2a1a" font-family="sans-serif">apples</text>'),
 "emphasis": dict(words=["أدوات التوكيد", "التوكيد", "التأكيد"], anim="bounce", face=(30, 66, .32), only=EN, body=gcard("so ! / such !", "#F6B73C", 16)),
 "changes_ba": dict(words=["التغيرات", "التغيير", "قبل وبعد"], anim="sway", face=(22, 52, .3), only=EN,
   body='<path d="M10 70 L10 52 L22 42 L34 52 L34 70Z" fill="#AEB8C4" {OL}/><path d="M42 56 L58 56 M52 50 L58 56 L52 62" fill="none" stroke="#3b2a1a" stroke-width="3"/>'
        '<path d="M64 70 L64 36 L80 22 L96 36 L96 70Z" fill="#F2D07A" {OL}/><rect x="74" y="50" width="12" height="20" fill="#8B5E3C" {OL}/>'),
 "watch_tv": dict(words=["شاهد", "المشاهدة", "القناة", "القنوات التلفزيونية"], anim="bob", face=(50, 46, .34), only=EN,
   body='<rect x="8" y="20" width="84" height="56" rx="8" fill="#3b3b5c" {OL}/><rect x="14" y="26" width="72" height="44" rx="4" fill="#BFE3F2"/><path d="M36 76 L28 92 M64 76 L72 92" stroke="#3b2a1a" stroke-width="4" stroke-linecap="round"/>'
        '<path d="M40 8 L50 18 L60 8" fill="none" stroke="#3b2a1a" stroke-width="3"/>'),
 "since": dict(words=["منذ"], anim="sun", face=(50, 62, .34), only=EN,
   body='<circle cx="50" cy="56" r="36" fill="#fff" {OL}/><path d="M50 56 L50 32 M50 56 L66 64" stroke="#3b2a1a" stroke-width="4" stroke-linecap="round"/>'
        '<path d="M14 30 C20 14 36 6 50 6 M14 30 L10 18 M14 30 L26 28" fill="none" stroke="#E8574A" stroke-width="4" stroke-linecap="round"/>'),
 "celebrities": dict(words=["المشاهير", "الشهرة", "النجوم المشاهير"], anim="sun", face=(50, 56, .38), only=EN,
   body='<path d="M50 6 L62 36 L94 38 L68 58 L78 90 L50 72 L22 90 L32 58 L6 38 L38 36Z" fill="#FFD25A" {OL}/><path d="M20 96 L80 96" stroke="#E8574A" stroke-width="5" stroke-linecap="round"/>'),
 "appointment": dict(words=["موعد", "المواعيد", "حجز موعد"], anim="bob", face=(36, 66, .32), only=EN,
   body='<rect x="8" y="20" width="66" height="70" rx="6" fill="#fff" {OL}/><rect x="8" y="20" width="66" height="16" rx="6" fill="#6CB8FF" {OL}/><path d="M24 12 L24 26 M58 12 L58 26" stroke="#3b2a1a" stroke-width="5" stroke-linecap="round"/>'
        '<circle cx="76" cy="72" r="18" fill="#FFD25A" {OL}/><path d="M76 72 L76 60 M76 72 L84 76" stroke="#3b2a1a" stroke-width="3" stroke-linecap="round"/>'),
 "progress": dict(words=["التقدم", "التطور", "مستوى التقدم"], anim="bounce", face=(30, 30, .32), only=EN,
   body='<rect x="6" y="56" width="88" height="20" rx="10" fill="#E8F2F8" {OL}/><rect x="6" y="56" width="62" height="20" rx="10" fill="#6CC27A" {OL}/>'
        '<path d="M50 40 L74 16 M64 16 L74 16 L74 26" fill="none" stroke="#6CC27A" stroke-width="5" stroke-linecap="round"/>'),
 "time_capsule": dict(words=["كبسولة زمنية", "كبسولة الزمن"], anim="bob", face=(50, 52, .34), only=EN,
   body='<rect x="20" y="20" width="60" height="70" rx="30" fill="#AEB8C4" {OL}/><path d="M20 50 L80 50" stroke="#3b2a1a" stroke-width="3"/><circle cx="50" cy="70" r="10" fill="#fff" {OL}/>'
        '<path d="M50 70 L50 64 M50 70 L54 72" stroke="#3b2a1a" stroke-width="2"/><path d="M4 96 L96 96" stroke="#8B5E3C" stroke-width="6"/>'),
 "common_problems": dict(words=["المشكلات الشائعة", "المشكلات", "حل المشكلات"], anim="wobble", face=(50, 62, .36), only=EN,
   body='<circle cx="50" cy="56" r="34" fill="#F7C9A4" {OL}/><text direction="ltr" x="20" y="26" font-size="22" font-weight="800" fill="#E8574A" font-family="sans-serif">?</text><text direction="ltr" x="74" y="20" font-size="18" font-weight="800" fill="#6CB8FF" font-family="sans-serif">?</text><text direction="ltr" x="84" y="50" font-size="16" font-weight="800" fill="#F6B73C" font-family="sans-serif">?</text>'),
 "smoke_signals": dict(words=["إشارات الدخان", "وسائل الاتصال القديمة"], anim="wind", face=(50, 84, .3), only=EN,
   body='<path d="M30 96 L70 96 M36 90 L64 90" stroke="#8B5E3C" stroke-width="6" stroke-linecap="round"/><path d="M50 88 C40 80 42 70 50 64 C52 72 60 74 58 82 C56 86 54 88 50 88Z" fill="#F6A23C" {OL}/>'
        '<circle cx="46" cy="48" r="10" fill="#C9D2DC" {OL}/><circle cx="56" cy="30" r="12" fill="#C9D2DC" {OL}/><circle cx="44" cy="12" r="9" fill="#C9D2DC" {OL}/>'),
 "millionaire": dict(words=["مليونير", "الثروة", "الأغنياء"], anim="bounce", face=(50, 66, .38), only=EN,
   body='<path d="M34 24 L66 24 L60 34 C80 44 86 70 76 84 C68 94 32 94 24 84 C14 70 20 44 40 34Z" fill="#C9A27A" {OL}/><path d="M34 24 L42 12 L50 20 L58 12 L66 24" fill="#C9A27A" {OL}/>'
        '<text direction="ltr" x="50" y="72" text-anchor="middle" font-size="24" font-weight="800" fill="#3E8E4C" font-family="sans-serif">$</text>'),
 "mystery": dict(words=["لغز", "أحداث غامضة", "التخمين", "الغموض", "قصص الغموض", "محقق", "التحقيق"], anim="wobble", face=(40, 40, .36), only=EN,
   body='<circle cx="40" cy="40" r="28" fill="#E8F6FF" {OL}/><path d="M60 60 L92 92" stroke="#8B5E3C" stroke-width="10" stroke-linecap="round"/>'
        '<text direction="ltr" x="40" y="52" text-anchor="middle" font-size="32" font-weight="800" fill="#6CB8FF" font-family="sans-serif">?</text><path d="M10 20 C14 8 30 4 40 6" fill="none" stroke="#3b2a1a" stroke-width="3"/>'),
 "regret": dict(words=["الندم", "التمني", "أتمنى لو"], anim="sway", face=None, only=EN,
   body='<circle cx="50" cy="54" r="38" fill="#B0A8C9" {OL}/><circle cx="36" cy="46" r="4" fill="#3b2a1a"/><circle cx="64" cy="46" r="4" fill="#3b2a1a"/><path d="M36 74 C44 66 56 66 64 74" fill="none" stroke="#3b2a1a" stroke-width="4" stroke-linecap="round"/>'
        '<path d="M64 54 C62 60 62 62 64 64 C66 62 66 60 64 54Z" fill="#7CC6F2" {OL}/><path d="M80 10 C88 14 92 22 90 30 M90 30 L84 26 M90 30 L94 24" fill="none" stroke="#3b2a1a" stroke-width="2.4"/>'),
 "third_conditional": dict(words=["الشرط الثالث", "الشرط الأول", "جمل الشرط"], anim="bob", face=(50, 84, .3), only=EN, body=gcard("If I had…", "#6CC27A", 18)),
 "quotes": dict(words=["الاقتباسات", "الاقتباس", "علامات التنصيص"], anim="bob", face=(50, 76, .3), only=EN,
   body='<rect x="8" y="16" width="84" height="64" rx="10" fill="#FFF3C4" {OL}/><text direction="ltr" x="50" y="66" text-anchor="middle" font-size="54" font-weight="800" fill="#C98A55" font-family="serif">“ ”</text>'),
 "reported": dict(words=["الأسئلة المنقولة", "الكلام غير المباشر"], anim="bob", face=(26, 40, .3), only=EN,
   body='<path d="M4 14 L50 14 C54 14 56 16 56 20 L56 46 C56 50 54 52 50 52 L24 52 L12 62 L14 52 L10 52 C6 52 4 50 4 46Z" fill="#6CB8FF" {OL}/>'
        '<path d="M58 60 L90 60 C94 60 96 62 96 66 L96 84 C96 88 94 90 90 90 L64 90 C60 90 58 88 58 84Z" fill="#FFD25A" {OL}/><path d="M46 56 C52 62 54 66 58 70" fill="none" stroke="#3b2a1a" stroke-width="3" stroke-dasharray="4 3"/><text direction="ltr" x="30" y="40" text-anchor="middle" font-size="18" font-weight="800" fill="#fff" font-family="sans-serif">?</text>'),
 "remote": dict(words=["الأماكن النائية", "المناطق النائية", "العزلة"], anim="sway", face=(50, 70, .3), only=EN,
   body='<rect x="2" y="56" width="96" height="42" fill="#4A90D9" {OL}/><path d="M30 62 C34 48 66 48 70 62Z" fill="#F2D07A" {OL}/><path d="M50 54 C50 40 52 28 56 20" fill="none" stroke="#8B5E3C" stroke-width="4" stroke-linecap="round"/>'
        '<path d="M56 20 C44 12 36 16 34 22 M56 20 C66 10 78 12 80 20" fill="none" stroke="#3E8E4C" stroke-width="5" stroke-linecap="round"/>'),
 "manager": dict(words=["المدير", "المدراء", "الإدارة", "مدير المدرسة"], anim="bob", face=(50, 30, .36), only=EN,
   body='<circle cx="50" cy="30" r="18" fill="#F7C9A4" {OL}/><path d="M20 96 C20 62 80 62 80 96Z" fill="#3b3b5c" {OL}/><path d="M50 62 L44 72 L50 92 L56 72Z" fill="#E8574A" {OL}/>'),
 "athletes": dict(words=["الرياضيون", "الرياضي", "الرياضيين", "الأبطال الرياضيون"], anim="bounce", face=(50, 66, .38), only=EN,
   body='<path d="M30 4 L44 46 L56 46 L70 4 L58 4 L50 30 L42 4Z" fill="#6CB8FF" {OL}/><circle cx="50" cy="66" r="24" fill="#FFD25A" {OL}/><text direction="ltr" x="50" y="74" text-anchor="middle" font-size="20" font-weight="800" fill="#B5651D" font-family="sans-serif">1</text>'),
 "sports_gear": dict(words=["المعدات الرياضية", "الأدوات الرياضية", "معدات الرياضة"], anim="bounce", face=(30, 70, .3), only=EN,
   body='<ellipse cx="30" cy="34" rx="22" ry="26" fill="#fff" stroke="#E8574A" stroke-width="5"/><path d="M14 22 L46 46 M14 34 L44 22 M18 50 L42 18" stroke="#AEB8C4" stroke-width="1.4"/><path d="M42 54 L60 90" stroke="#8B5E3C" stroke-width="6" stroke-linecap="round"/>'
        '<circle cx="78" cy="72" r="16" fill="#FFD25A" {OL}/><path d="M64 66 C72 70 84 70 92 66" fill="none" stroke="#fff" stroke-width="2.4"/>'),
 "competition_sport": dict(words=["المنافسة", "المسابقة الرياضية", "السباق"], anim="bounce", face=(50, 46, .34), only=EN,
   body='<path d="M28 10 L72 10 L68 44 C66 56 34 56 32 44Z" fill="#FFD25A" {OL}/><path d="M28 18 C14 18 14 38 30 40 M72 18 C86 18 86 38 70 40" fill="none" stroke="#3b2a1a" stroke-width="4"/>'
        '<rect x="44" y="56" width="12" height="16" fill="#F6B73C" {OL}/><rect x="30" y="72" width="40" height="14" rx="3" fill="#8B5E3C" {OL}/>'),
 "laughter": dict(words=["الفكاهة", "نكتة", "الضحك", "النكات", "روح الدعابة"], anim="bounce", face=None, only=EN,
   body='<circle cx="50" cy="50" r="44" fill="#FFD25A" {OL}/><path d="M26 42 L38 36 L26 30 M74 42 L62 36 L74 30" fill="none" stroke="#3b2a1a" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>'
        '<path d="M24 56 C30 84 70 84 76 56Z" fill="#fff" {OL}/><path d="M30 64 C40 70 60 70 70 64" fill="none" stroke="#E8574A" stroke-width="3"/><path d="M14 26 C10 32 10 36 14 38 M86 26 C90 32 90 36 86 38" fill="#7CC6F2" stroke="#3b2a1a" stroke-width="1.6"/>'),
 "wildlife": dict(words=["الموطن", "الحياة البرية", "الموائل الطبيعية", "الحيوانات البرية"], anim="sway", face=(50, 60, .34), only=EN,
   body='<rect x="2" y="2" width="96" height="96" rx="10" fill="#E6F4D8" {OL}/><path d="M14 98 L14 50 M86 98 L86 46" stroke="#8B5E3C" stroke-width="5"/><circle cx="14" cy="40" r="14" fill="#3E8E4C" {OL}/><circle cx="86" cy="36" r="14" fill="#3E8E4C" {OL}/>'
        '<path d="M36 80 C34 64 46 56 58 60 L66 52 L70 56 L64 66 C66 76 60 84 52 86 L46 98 M42 84 L40 98" fill="#C98A55" stroke="#3b2a1a" stroke-width="2.4"/>'),
 "migration": dict(words=["الهجرة", "هجرة الطيور", "هجرة الحيوانات"], anim="wind", face=(50, 74, .3), only=EN + ["science"],
   body='<rect x="2" y="2" width="96" height="96" rx="10" fill="#BFE3F2" {OL}/><path d="M16 30 L26 24 L36 30 M34 44 L44 38 L54 44 M52 58 L62 52 L72 58 M30 66 L40 60 L50 66 M70 30 L80 24 L90 30" fill="none" stroke="#3b2a1a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>'
        '<circle cx="80" cy="80" r="8" fill="#FFD25A" {OL}/>'),
 "dilemma": dict(words=["معضلة", "مواقف افتراضية", "اتخاذ القرار الصعب", "الخيارات"], anim="wobble", face=(50, 84, .3), only=EN,
   body='<path d="M50 98 L50 62 L18 30 M50 62 L82 30" fill="none" stroke="#C9A27A" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/>'
        '<text direction="ltr" x="18" y="22" text-anchor="middle" font-size="22" font-weight="800" fill="#E8574A" font-family="sans-serif">?</text><text direction="ltr" x="82" y="22" text-anchor="middle" font-size="22" font-weight="800" fill="#6CB8FF" font-family="sans-serif">?</text>'),
 "twins": dict(words=["التوائم", "التوأم", "التوأمان"], anim="bounce", face=(30, 40, .34), only=EN,
   body='<circle cx="30" cy="40" r="20" fill="#F7C9A4" {OL}/><circle cx="70" cy="40" r="20" fill="#F7C9A4" {OL}/><path d="M12 34 C14 18 46 18 48 34 C42 26 18 26 12 34Z M52 34 C54 18 86 18 88 34 C82 26 58 26 52 34Z" fill="#8B5E3C" {OL}/>'
        '<path d="M8 96 C8 70 52 70 52 96Z" fill="#6CB8FF" {OL}/><path d="M48 96 C48 70 92 70 92 96Z" fill="#6CB8FF" {OL}/>'),
 "leader": dict(words=["قائد", "القائد", "القيادة", "الشخصيات المؤثرة", "الشخصية المؤثرة"], anim="bob", face=(36, 50, .34), only=EN,
   body='<path d="M10 40 L46 40 L46 60 L10 60Z" fill="#E8574A" {OL}/><path d="M46 40 L86 18 L86 82 L46 60Z" fill="#F6B73C" {OL}/><path d="M18 60 L22 86 L34 86 L30 60" fill="#E8574A" {OL}/>'
        '<path d="M92 34 L98 30 M92 50 L100 50 M92 66 L98 70" stroke="#3b2a1a" stroke-width="3" stroke-linecap="round"/>'),
 "inventor": dict(words=["مخترع", "المخترع", "المخترعون", "الاختراعات"], anim="bob", face=(40, 40, .36), only=EN,
   body='<path d="M40 6 C18 6 8 24 14 40 C18 50 26 54 26 64 L54 64 C54 54 62 50 66 40 C72 24 62 6 40 6Z" fill="#FFD25A" {OL}/><rect x="26" y="64" width="28" height="14" rx="3" fill="#AEB8C4" {OL}/>'
        '<circle cx="78" cy="78" r="14" fill="#AEB8C4" {OL}/><circle cx="78" cy="78" r="5" fill="#fff" {OL}/><path d="M78 60 L78 64 M78 92 L78 96 M60 78 L64 78 M92 78 L96 78" stroke="#3b2a1a" stroke-width="5" stroke-linecap="round"/>'),
 "audience": dict(words=["الجمهور", "الجماهير", "المتفرجون"], anim="bounce", face=(50, 30, .3), only=EN,
   body='<rect x="20" y="6" width="60" height="30" rx="4" fill="#E8574A" {OL}/><circle cx="14" cy="60" r="9" fill="#AEB8C4" {OL}/><circle cx="38" cy="60" r="9" fill="#F6B73C" {OL}/><circle cx="62" cy="60" r="9" fill="#6CB8FF" {OL}/><circle cx="86" cy="60" r="9" fill="#9CD86C" {OL}/>'
        '<path d="M4 94 C4 74 24 74 24 94 M28 94 C28 74 48 74 48 94 M52 94 C52 74 72 74 72 94 M76 94 C76 74 96 74 96 94" fill="#C9D2DC" {OL}/>'),
 "roles": dict(words=["الأدوار", "لعب الأدوار", "التمثيل المسرحي", "المسرح"], anim="sway", face=None, only=EN + ["arabic"],
   body='<path d="M8 20 C8 14 46 14 46 20 C46 50 36 64 27 64 C18 64 8 50 8 20Z" fill="#FFD25A" {OL}/><path d="M18 32 C20 28 26 28 26 32 M30 32 C32 28 38 28 38 32 M18 46 C22 54 32 54 36 46" fill="none" stroke="#3b2a1a" stroke-width="2.6"/>'
        '<path d="M54 36 C54 30 92 30 92 36 C92 66 82 80 73 80 C64 80 54 66 54 36Z" fill="#6CB8FF" {OL}/><path d="M62 48 C64 52 70 52 72 48 M76 48 C78 52 84 52 86 48 M64 68 C68 60 78 60 82 68" fill="none" stroke="#3b2a1a" stroke-width="2.6"/>'),
 "survival": dict(words=["النجاة", "البقاء على قيد الحياة", "مهارات النجاة"], anim="sway", face=(50, 50, .34), only=EN,
   body='<circle cx="50" cy="50" r="42" fill="#E8574A" {OL}/><circle cx="50" cy="50" r="20" fill="#7CC6F2" {OL}/><path d="M50 8 L50 30 M50 70 L50 92 M8 50 L30 50 M70 50 L92 50" stroke="#fff" stroke-width="14"/><circle cx="50" cy="50" r="42" fill="none" {OL}/>'),
 "fashion": dict(words=["الموضة", "المظهر", "الأزياء", "الملابس العصرية"], anim="sway", face=(50, 60, .34), only=EN,
   body='<path d="M50 6 C56 6 58 14 50 18 L50 22 L90 46 C94 48 92 54 88 54 L12 54 C8 54 6 48 10 46 L50 22" fill="none" stroke="#3b2a1a" stroke-width="3"/>'
        '<path d="M34 54 L66 54 L80 96 L20 96Z" fill="#F59BB8" {OL}/><path d="M30 70 L70 70" stroke="#fff" stroke-width="3"/>'),
 "inner_beauty": dict(words=["الجمال الداخلي", "الجمال", "الجمال الحقيقي"], anim="bob", face=(46, 40, .34), only=EN,
   body='<ellipse cx="46" cy="44" rx="34" ry="40" fill="#BFE3F2" {OL}/><path d="M46 84 L46 94 M30 96 L62 96" stroke="#8B5E3C" stroke-width="5" stroke-linecap="round"/>'
        '<path d="M46 68 C34 60 30 52 34 46 C38 40 44 42 46 48 C48 42 54 40 58 46 C62 52 58 60 46 68Z" fill="#E8574A" {OL}/>'),
 "lost_found": dict(words=["المفقودات", "الأشياء المفقودة", "مكتب المفقودات"], anim="wobble", face=(50, 70, .34), only=EN,
   body='<path d="M10 44 L90 44 L84 94 L16 94Z" fill="#C98A55" {OL}/><path d="M10 44 L28 30 L72 30 L90 44" fill="#E6C08A" {OL}/>'
        '<rect x="22" y="20" width="18" height="24" rx="3" fill="#E8574A" {OL}/><circle cx="64" cy="30" r="10" fill="#6CB8FF" {OL}/><text direction="ltr" x="84" y="20" font-size="20" font-weight="800" fill="#3b2a1a" font-family="sans-serif">?</text>'),
 "treasure": dict(words=["كنز", "الكنز", "صندوق الكنز", "الكنوز"], anim="sun", face=(50, 70, .34), only=EN,
   body='<path d="M12 46 L88 46 L84 92 L16 92Z" fill="#8B5E3C" {OL}/><path d="M12 46 C12 26 88 26 88 46Z" fill="#A8774F" {OL}/><path d="M12 46 L88 46" stroke="#FFD25A" stroke-width="6"/>'
        '<rect x="44" y="40" width="12" height="16" rx="2" fill="#FFD25A" {OL}/><circle cx="30" cy="30" r="5" fill="#FFD25A" {OL}/><circle cx="70" cy="30" r="5" fill="#FFD25A" {OL}/><path d="M50 10 L54 18 L62 20 L54 22 L50 30 L46 22 L38 20 L46 18Z" fill="#fff" {OL}/>'),
 "review": dict(words=["مراجعة", "مراجعة العام", "مراجعة/تقييم", "التقييم الذاتي"], anim="bob", face=(30, 72, .3), only=EN,
   body='<rect x="10" y="10" width="66" height="84" rx="6" fill="#fff" {OL}/><path d="M20 28 L26 34 L36 22 M20 50 L26 56 L36 44 M20 72 L26 78 L36 66" fill="none" stroke="#6CC27A" stroke-width="4" stroke-linecap="round"/>'
        '<path d="M44 30 L66 30 M44 52 L66 52 M44 74 L66 74" stroke="#3b2a1a" stroke-width="3" stroke-linecap="round"/><path d="M80 70 L96 30 L100 32 L84 72 L78 76Z" fill="#FFD25A" {OL}/>'),
}
ALIAS_ONLY = None
ALIASES = {"كنزة صوفية": ("en.shirt", ("english",)), "كنزة": ("en.shirt", ("english",)), "سائح": ("soc.tourism", ("english",)), "الرسوم المتحركة": ("dig.animation", ("english",)), "الروبوتات": ("dig.robot", ("english",))}
