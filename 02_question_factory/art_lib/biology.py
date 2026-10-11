"""🆕 batch 41 · biology (الأحياء، الثانوي): the cell and its division, the nerves and the hormones, immunity, breathing, digestion and
the kidney, the skeleton and the muscles, the skin, the first cells of life, DNA → RNA → protein, plants (transport, ferns and mosses)
and the animal groups the books meet. For the science subjects only (a word like «الطور» or «الترجمة» means other things elsewhere)."""
F = "bio"
S = ("science",)
CELL = '<circle cx="50" cy="50" r="40" fill="#E9F7EF" {OL}/>'


def xch(x, y, c="#E2504C", r=0, s=1.0):
    """An X chromosome (two sister chromatids held at the middle)."""
    return (f'<g transform="translate({x} {y}) rotate({r}) scale({s})"><rect x="-3" y="-10" width="6" height="20" rx="3" fill="{c}" transform="rotate(28)" {{OL}}/>'
            f'<rect x="-3" y="-10" width="6" height="20" rx="3" fill="{c}" transform="rotate(-28)" {{OL}}/><circle r="2.6" fill="#3b2a1a"/></g>')


def vch(x, y, c="#E2504C", r=0):
    """One chromatid pulled away (a V)."""
    return f'<path d="M{x - 5} {y - 6} L{x} {y + 4} L{x + 5} {y - 6}" fill="none" stroke="{c}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round" transform="rotate({r} {x} {y})"/>'


D = {
 # ---------- the cell divides (mitosis) ----------
 "interphase": dict(words=["الطور البيني", "الكروماتين", "النيوكليوسوم"], only=S, anim="bob", face=(50, 78, .42),
   body=CELL + '<circle cx="50" cy="44" r="22" fill="#D7ECFF" {OL}/><path d="M38 40 q4 -8 8 0 t8 0 t8 0 M40 50 q4 -6 8 0 t8 0" fill="none" stroke="#8E6FD8" stroke-width="2.4" stroke-linecap="round"/>'),
 "prophase": dict(words=["الطور التمهيدي"], only=S, anim="bob", face=(50, 78, .42),
   body=CELL + '<circle cx="50" cy="46" r="24" fill="none" stroke="#9BB7D4" stroke-width="2" stroke-dasharray="4 4"/>'
        + xch(40, 38) + xch(60, 36, "#5B8DEF", 20) + xch(38, 56, "#5B8DEF", -15) + xch(60, 56, "#E2504C", 10)),
 "metaphase": dict(words=["الطور الاستوائي", "الخيوط المغزلية"], only=S, anim="bob", face=(50, 82, .4),
   body=CELL + '<path d="M14 50 L50 24 M14 50 L50 38 M14 50 L50 52 M14 50 L50 66 M86 50 L50 24 M86 50 L50 38 M86 50 L50 52 M86 50 L50 66" stroke="#9BB7D4" stroke-width="1.4"/>'
        + '<path d="M50 14 V80" stroke="#C9D8E8" stroke-width="1.6" stroke-dasharray="3 3"/>' + xch(50, 24, r=90, s=.85) + xch(50, 38, "#5B8DEF", 90, .85) + xch(50, 52, r=90, s=.85) + xch(50, 66, "#5B8DEF", 90, .85)
        + '<circle cx="14" cy="50" r="3.4" fill="#F5A623" {OL}/><circle cx="86" cy="50" r="3.4" fill="#F5A623" {OL}/>'),
 "anaphase": dict(words=["الطور الانفصالي"], only=S, anim="bob", face=(50, 80, .4),
   body='<ellipse cx="50" cy="50" rx="44" ry="36" fill="#E9F7EF" {OL}/><path d="M10 50 L30 32 M10 50 L30 50 M10 50 L30 66 M90 50 L70 32 M90 50 L70 50 M90 50 L70 66" stroke="#9BB7D4" stroke-width="1.4"/>'
        + vch(32, 32, r=90) + vch(32, 50, "#5B8DEF", 90) + vch(32, 66, r=90) + vch(68, 32, r=-90) + vch(68, 50, "#5B8DEF", -90) + vch(68, 66, r=-90)
        + '<path d="M44 50 H56" stroke="#9BB7D4" stroke-width="1.4" stroke-dasharray="2 3"/>'),
 "telophase": dict(words=["الطور النهائي", "انقسام السيتوبلازم"], only=S, anim="wobble", face=(50, 84, .38),
   body='<path d="M50 22 C38 8 6 14 6 50 C6 86 38 92 50 78 C62 92 94 86 94 50 C94 14 62 8 50 22Z" fill="#E9F7EF" {OL}/><path d="M50 22 C46 36 46 64 50 78" fill="none" stroke="#3b2a1a" stroke-width="1.6" stroke-dasharray="3 3"/>'
        '<circle cx="28" cy="48" r="13" fill="#D7ECFF" {OL}/><circle cx="72" cy="48" r="13" fill="#D7ECFF" {OL}/><path d="M22 46 q3 -5 6 0 t6 0 M66 46 q3 -5 6 0 t6 0" fill="none" stroke="#8E6FD8" stroke-width="2"/>'),
 "chromatids": dict(words=["الكروماتيدات الشقيقة", "الكروماتيدات", "القطعة المركزية", "العبور الجيني", "عدم الانفصال"], only=S, anim="wobble", face=(50, 84, .45),
   body='<g transform="translate(50 44) scale(2.6)"><rect x="-3" y="-12" width="6" height="24" rx="3" fill="#E2504C" transform="rotate(24)" {OL}/><rect x="-3" y="-12" width="6" height="24" rx="3" fill="#5B8DEF" transform="rotate(-24)" {OL}/><circle r="3" fill="#3b2a1a"/></g>'),
 # ---------- nerves ----------
 "neuron": dict(words=["الزوائد الشجيرية", "المحور", "النهايات العصبية", "الغمد الميليني", "الخلايا الدبقية", "الخلية العصبية الحركية", "الخلية العصبية الحسية"], only=("biology",), anim="sway", face=(22, 46, .4),
   body='<path d="M22 30 L10 14 M22 30 L4 34 M20 34 L8 50 M30 30 L34 12 M30 30 L44 20" stroke="#B58BD9" stroke-width="4" stroke-linecap="round"/>'
        '<circle cx="24" cy="44" r="15" fill="#D6B8F2" {OL}/><path d="M36 50 L84 74" stroke="#B58BD9" stroke-width="5" stroke-linecap="round"/>'
        '<rect x="44" y="50" width="12" height="8" rx="4" fill="#FFE7A3" transform="rotate(27 50 54)" {OL}/><rect x="60" y="58" width="12" height="8" rx="4" fill="#FFE7A3" transform="rotate(27 66 62)" {OL}/>'
        '<path d="M84 74 L94 70 M84 74 L92 84 M84 74 L80 88" stroke="#B58BD9" stroke-width="3.4" stroke-linecap="round"/>'),
 "impulse": dict(words=["الإشارات العصبية", "السيال العصبي", "جهد الفعل", "العتبة", "الإشارة العصبية"], only=S, anim="buzz", face=(24, 42, .42),
   body='<circle cx="24" cy="40" r="15" fill="#D6B8F2" {OL}/><path d="M37 46 L90 70" stroke="#B58BD9" stroke-width="5" stroke-linecap="round"/>'
        '<path d="M56 34 L48 54 L58 54 L50 74" fill="none" stroke="#F5C518" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/><path d="M56 34 L48 54 L58 54 L50 74" fill="none" stroke="#3b2a1a" stroke-width="1.4" stroke-linejoin="round"/>'
        '<path d="M70 52 l8 4 M76 46 l6 6" stroke="#F5C518" stroke-width="3" stroke-linecap="round"/>'),
 "synapse": dict(words=["التشابك العصبي", "الناقل العصبي", "النواقل العصبية", "الدوبامين", "التشابك العصبي والنواقل العصبية", "الوصلات الفجوية"], only=S, anim="bob", face=(30, 40, .42),
   body='<path d="M4 20 C20 18 40 26 46 40 C50 50 46 62 36 66 C24 70 10 64 4 60Z" fill="#D6B8F2" {OL}/><path d="M96 34 C80 34 64 40 60 52 C58 62 64 74 76 78 C86 80 92 78 96 76Z" fill="#B7E3C9" {OL}/>'
        '<circle cx="50" cy="46" r="2.6" fill="#E2504C"/><circle cx="54" cy="54" r="2.6" fill="#E2504C"/><circle cx="51" cy="60" r="2.4" fill="#E2504C"/><circle cx="56" cy="44" r="2.2" fill="#E2504C"/>'
        '<path d="M60 50 h4 M60 58 h5 M61 66 h4" stroke="#3b8a5a" stroke-width="2.4" stroke-linecap="round"/>'),
 "reflex": dict(words=["الفعل المنعكس", "المثير والاستجابة", "المستجيب", "الاستجابة الحركية", "القوس الانعكاسي"], only=S, anim="bounce", face=(36, 30, .42),
   body='<path d="M30 6 L40 50 C42 58 40 64 34 66 L26 92" fill="none" stroke="#F2C9A0" stroke-width="16" stroke-linecap="round"/><path d="M30 6 L40 50 C42 58 40 64 34 66 L26 92" fill="none" stroke="#3b2a1a" stroke-width="1.6"/>'
        '<rect x="56" y="44" width="34" height="12" rx="4" fill="#E2504C" transform="rotate(-20 72 50)" {OL}/><path d="M66 56 L84 86" stroke="#8B5A2B" stroke-width="5" stroke-linecap="round"/>'
        '<path d="M46 66 l10 -6 M48 74 l12 -4" stroke="#F5A623" stroke-width="3" stroke-linecap="round"/>'),
 "cerebellum": dict(words=["المخيخ", "المحافظة على وضعية الجسم", "التوازن الجسمي"], only=S, anim="wobble", face=(42, 40, .45),
   body='<path d="M50 12 C30 6 10 18 12 40 C8 56 22 66 40 64 C52 64 62 56 70 50 C84 46 90 30 80 20 C74 14 62 12 50 12Z" fill="#F7B5C4" {OL}/>'
        '<path d="M58 62 C62 78 80 84 90 72 C96 62 86 52 72 54 C66 56 60 58 58 62Z" fill="#E98AA4" {OL}/><path d="M66 64 Q76 62 84 66 M64 70 Q76 70 86 74" fill="none" stroke="#C25A79" stroke-width="2"/>'
        '<path d="M48 64 L46 88" stroke="#F7B5C4" stroke-width="8" stroke-linecap="round"/>'),
 # ---------- hormones and glands ----------
 "hormone": dict(words=["الهرمون", "الهرمونات", "الإشارات الهرمونية", "الإشارات الكيميائية", "الإنسولين", "الجلوكاجون", "الإنسولين والجلوكاجون", "الأدرينالين",
                        "الثيروكسين", "الكورتيزول", "الإستروجين والبروجسترون", "التستوستيرون", "الأوكسيتوسين", "البرولاكتين", "الميلاتونين", "الألدوستيرون",
                        "الكالسيتونين", "هرمون جار الدرقية", "الهرمون المضاد لإدرار البول", "الغدد الصماء", "الفيرمونات"], only=S, anim="drip", face=(50, 66, .5),
   body='<path d="M50 6 C50 6 18 46 18 64 C18 82 32 94 50 94 C68 94 82 82 82 64 C82 46 50 6 50 6Z" fill="#7FD6C9" {OL}/>'
        '<rect x="32" y="34" width="36" height="22" rx="3" fill="#fff" {OL}/><path d="M32 36 L50 48 L68 36" fill="none" stroke="#3b2a1a" stroke-width="2"/>'),
 "plant_hormone": dict(words=["الهرمون النباتي", "الهرمونات النباتية", "الأكسين", "الجبريلين", "السيتوكاينين", "الإيثيلين"], only=S, anim="grow", face=(50, 74, .42),
   body='<path d="M50 94 L50 46" stroke="#5DBB63" stroke-width="5" stroke-linecap="round"/><path d="M50 62 C34 60 24 48 26 36 C40 36 50 46 50 62Z" fill="#7CC96F" {OL}/>'
        '<path d="M50 54 C64 50 74 38 72 26 C58 28 50 38 50 54Z" fill="#7CC96F" {OL}/><path d="M50 30 C50 30 40 18 40 12 C40 6 45 4 50 4 C55 4 60 6 60 12 C60 18 50 30 50 30Z" fill="#7FD6C9" {OL}/>'
        '<path d="M30 92 H70" stroke="#8B5A2B" stroke-width="5" stroke-linecap="round"/>'),
 "tropism": dict(words=["الانتحاء", "الانتحاء الأرضي", "الانتحاء الضوئي", "الانتحاءات"], only=S, anim="sway", face=(64, 34, .42),
   body='<path d="M0 54 H100 V100 H0Z" fill="#B88A5A"/><path d="M0 54 H100" stroke="#3b2a1a" stroke-width="2"/><path d="M40 54 C40 40 50 26 66 22" fill="none" stroke="#5DBB63" stroke-width="5" stroke-linecap="round"/>'
        '<path d="M66 22 C70 14 80 12 86 18 C80 22 72 24 66 22Z" fill="#7CC96F" {OL}/><path d="M40 54 C40 68 34 80 36 94 M40 64 C46 70 50 78 48 88" fill="none" stroke="#F5E0B8" stroke-width="3.4" stroke-linecap="round"/>'
        '<path d="M88 4 l-4 6 M96 10 l-6 3" stroke="#F5A623" stroke-width="3" stroke-linecap="round"/><path d="M14 66 v18 M10 78 l4 6 l4 -6" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>'),
 "thyroid": dict(words=["الغدة الدرقية", "تضخم الغدة الدرقية", "الغدة الجار درقية", "الغدد جارات الدرقية"], only=S, anim="wobble", face=(50, 56, .4),
   body='<rect x="44" y="4" width="12" height="92" rx="6" fill="#E3EEF7" {OL}/><path d="M44 30 h12 M44 42 h12 M44 72 h12 M44 84 h12" stroke="#9BB7D4" stroke-width="2"/>'
        '<path d="M50 52 C46 40 34 28 22 34 C12 40 14 64 26 70 C36 74 46 64 50 58 C54 64 64 74 74 70 C86 64 88 40 78 34 C66 28 54 40 50 52Z" fill="#E98AA4" {OL}/>'),
 "pituitary": dict(words=["الغدة النخامية", "الفص الأمامي والخلفي للنخامية", "تحت المهاد", "الغدة الصنوبرية"], only=S, anim="wobble", face=(40, 36, .42),
   body='<path d="M50 10 C30 4 8 16 10 40 C6 58 22 70 42 68 C58 68 74 62 84 50 C96 36 88 16 70 12 C62 10 56 10 50 10Z" fill="#F7B5C4" {OL}/>'
        '<path d="M52 66 L54 76" stroke="#E98AA4" stroke-width="5" stroke-linecap="round"/><circle cx="54" cy="82" r="8" fill="#F5A623" {OL}/><circle cx="54" cy="82" r="13" fill="none" stroke="#F5A623" stroke-width="1.6" stroke-dasharray="3 3"/>'),
 "gland": dict(words=["الغدة", "الغدد", "الغدة الزعترية", "الغدد العرقية", "الغدد الدهنية", "الغدد اللعابية"], only=S, anim="drip", face=(46, 46, .45),
   body='<path d="M46 12 C24 12 12 30 16 50 C20 72 40 80 56 74 C76 68 86 48 78 30 C72 18 60 12 46 12Z" fill="#F6C1D4" {OL}/>'
        '<path d="M56 74 C60 82 64 88 70 92" fill="none" stroke="#3b2a1a" stroke-width="3"/><circle cx="76" cy="94" r="3.4" fill="#7FD6C9" {OL}/><circle cx="84" cy="86" r="2.6" fill="#7FD6C9" {OL}/>'),
 # ---------- immunity and the lymph ----------
 "lymphocyte": dict(words=["الخلايا اللمفية", "الخلايا البائية", "الخلايا التائية", "الخلايا البائية والتائية", "الخلايا القاتلة الطبيعية", "الأجسام المضادة", "المستضد", "الإنترفيرون", "المناعة المكتسبة", "خلايا الدم البيضاء"], only=S, anim="bounce", face=(50, 66, .45),
   body='<circle cx="50" cy="52" r="34" fill="#F4F7FB" {OL}/><circle cx="50" cy="46" r="20" fill="#B9A2F0" {OL}/>'
        '<path d="M86 22 l-6 8 M86 22 l-10 2 M86 22 l2 -6" stroke="#5B8DEF" stroke-width="3" stroke-linecap="round"/><path d="M14 84 l6 -8 M14 84 l10 -2 M14 84 l-2 6" stroke="#5B8DEF" stroke-width="3" stroke-linecap="round"/>'
        '<path d="M88 76 l-8 -4 M88 76 l-2 -9 M88 76 l6 2" stroke="#5B8DEF" stroke-width="3" stroke-linecap="round"/>'),
 "phagocyte": dict(words=["البلعمة", "البلعمة والالتهاب", "الأقدام الكاذبة", "الخلايا البلعمية", "الأميبا"], only=S, anim="wiggle", face=(40, 58, .45),
   body='<path d="M44 14 C64 10 70 24 80 26 C94 30 92 46 84 52 C96 62 86 84 66 80 C54 92 30 90 22 78 C8 74 6 54 16 46 C10 30 26 16 44 14Z" fill="#CDE9F7" {OL}/>'
        '<circle cx="40" cy="50" r="10" fill="#9CCFD8" {OL}/><circle cx="74" cy="40" r="7" fill="#7CC96F" {OL}/><path d="M70 34 l-4 -4 M80 36 l4 -4 M78 46 l4 4 M68 44 l-4 4" stroke="#3b8a5a" stroke-width="2" stroke-linecap="round"/>'),
 "inflammation": dict(words=["الالتهاب", "الالتهابات", "التورم"], only=S, anim="wobble", face=(48, 62, .45),
   body='<path d="M30 96 L30 46 C30 24 70 24 70 46 L70 96Z" fill="#F2C9A0" {OL}/><ellipse cx="50" cy="54" rx="22" ry="20" fill="#F28A8A" opacity=".7"/>'
        '<path d="M20 20 q4 -6 0 -12 M50 14 q4 -6 0 -12 M80 20 q4 -6 0 -12" fill="none" stroke="#E2504C" stroke-width="3" stroke-linecap="round"/>'),
 "allergy": dict(words=["الحساسية", "الربو", "الأكزيما", "حمى القش"], only=S, anim="bounce", face=(50, 58, .55),
   body='<circle cx="50" cy="56" r="34" fill="#FFD25A" {OL}/><path d="M76 40 l14 -8 M78 52 l16 0 M76 64 l14 8" stroke="#9CCFD8" stroke-width="4" stroke-linecap="round"/>'
        '<circle cx="18" cy="24" r="6" fill="#F5D547" {OL}/><circle cx="30" cy="12" r="4" fill="#F5D547" {OL}/><path d="M14 24 h8 M18 20 v8" stroke="#E3A70F" stroke-width="1.6"/>'),
 "lymph": dict(words=["اللمف", "الأوعية اللمفاوية", "الشعيرات اللمفاوية", "القناة الصدرية", "الطحال", "اللوزتان", "الجهاز اللمفاوي", "العقد اللمفاوية", "الجهاز الليمفاوي"], only=S, anim="sway", face=(50, 50, .45),
   body='<path d="M50 4 V96 M50 30 L20 12 M50 30 L80 12 M50 64 L18 84 M50 64 L82 84" stroke="#7CC96F" stroke-width="5" stroke-linecap="round"/>'
        '<ellipse cx="50" cy="48" rx="16" ry="12" fill="#A8DDA0" {OL}/><ellipse cx="28" cy="18" rx="7" ry="5" fill="#A8DDA0" {OL}/><ellipse cx="74" cy="80" rx="7" ry="5" fill="#A8DDA0" {OL}/><ellipse cx="26" cy="80" rx="7" ry="5" fill="#A8DDA0" {OL}/>'),
 # ---------- breathing ----------
 "alveoli": dict(words=["الحويصلات الهوائية", "الأكياس الهوائية", "السعة الحيوية", "تبادل الغازات"], only=S, anim="bob", face=(50, 62, .42),
   body='<path d="M50 2 V30" stroke="#E98AA4" stroke-width="6" stroke-linecap="round"/><path d="M50 30 L34 44 M50 30 L66 44" stroke="#E98AA4" stroke-width="4" stroke-linecap="round"/>'
        + "".join(f'<circle cx="{x}" cy="{y}" r="11" fill="#F7B5C4" {{OL}}/>' for x, y in ((30, 52), (44, 46), (58, 46), (72, 52), (24, 68), (38, 64), (52, 62), (66, 64), (80, 68), (36, 82), (52, 80), (68, 82)))
        + '<path d="M18 60 Q30 74 44 70 T80 76" fill="none" stroke="#E2504C" stroke-width="1.8"/><path d="M20 74 Q36 88 56 84 T84 82" fill="none" stroke="#5B8DEF" stroke-width="1.8"/>'),
 "bronchi": dict(words=["الشعب الهوائية", "القصيبات الهوائية", "الشعيبات الهوائية", "القصبة الهوائية والشعب"], only=S, anim="sway", face=(50, 30, .4),
   body='<rect x="44" y="2" width="12" height="40" rx="6" fill="#F7D3DD" {OL}/><path d="M44 10 h12 M44 18 h12 M44 26 h12 M44 34 h12" stroke="#E98AA4" stroke-width="1.6"/>'
        '<path d="M50 42 L28 58 L16 70 M28 58 L30 76 M16 70 L8 82 M16 70 L18 86 M50 42 L72 58 L84 70 M72 58 L70 76 M84 70 L92 82 M84 70 L82 86 M30 76 L24 90 M30 76 L36 90 M70 76 L64 90 M70 76 L76 90" fill="none" stroke="#E98AA4" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>'),
 "larynx": dict(words=["الحنجرة", "الأحبال الصوتية", "البلعوم", "لسان المزمار"], only=S, anim="wobble", face=(50, 74, .4),
   body='<rect x="34" y="6" width="32" height="88" rx="14" fill="#F7D3DD" {OL}/><path d="M36 40 C44 48 56 48 64 40" fill="none" stroke="#E98AA4" stroke-width="3"/>'
        '<path d="M42 30 L50 44 L58 30" fill="none" stroke="#C25A79" stroke-width="3" stroke-linejoin="round"/><path d="M74 24 q8 6 0 12 M82 20 q10 10 0 20" fill="none" stroke="#5B8DEF" stroke-width="3" stroke-linecap="round"/>'),
 "diaphragm": dict(words=["الحجاب الحاجز", "الشهيق", "الزفير", "الحاجز العرضي", "الشهيق والزفير"], only=S, anim="bob", face=(50, 46, .4),
   body='<path d="M44 34 C30 24 14 36 14 58 C14 70 22 74 32 70 C40 68 44 62 44 54Z" fill="#F28AA8" {OL}/><path d="M56 34 C70 24 86 36 86 58 C86 70 78 74 68 70 C60 68 56 62 56 54Z" fill="#F28AA8" {OL}/>'
        '<path d="M50 6 V36" stroke="#C0392B" stroke-width="4" stroke-linecap="round"/><path d="M8 84 C26 64 74 64 92 84" fill="none" stroke="#C98A55" stroke-width="7" stroke-linecap="round"/>'
        '<path d="M50 92 v-12 M44 86 l6 -6 l6 6" fill="none" stroke="#5B8DEF" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>'),
 # ---------- digestion and the kidney ----------
 "enzyme": dict(words=["الإنزيم", "الإنزيمات", "الإنزيمات الهاضمة", "الأميليز", "الموقع النشط", "المثبطات", "المثبط", "الإنزيمات المعتمدة على السايكلين", "إنزيم الربط", "الليبيز", "الببسين"], only=S, anim="bounce", face=(36, 66, .45),
   body='<path d="M14 48 C14 22 34 10 52 10 C70 10 86 22 88 40 L62 40 L62 56 L88 56 C86 76 70 90 50 90 C30 90 14 74 14 48Z" fill="#7CC6F2" {OL}/>'
        '<path d="M64 42 L94 42 L94 54 L64 54Z" fill="#F5A623" {OL}/><circle cx="92" cy="48" r="5" fill="#F5A623" {OL}/>'),
 "villi": dict(words=["الخملات", "الامتصاص", "الخملة"], only=("biology",), anim="sway", face=(50, 90, .3),
   body='<path d="M4 96 V72 H96 V96Z" fill="#F7B5C4" {OL}/>' + "".join(f'<path d="M{x} 72 C{x} 42 {x + 14} 42 {x + 14} 72" fill="#F7B5C4" {{OL}}/><path d="M{x + 7} 70 V52" stroke="#E2504C" stroke-width="1.6"/>' for x in (8, 26, 44, 62, 80))
        + '<circle cx="22" cy="20" r="4" fill="#F5D547" {OL}/><circle cx="54" cy="14" r="4" fill="#7CC96F" {OL}/><circle cx="80" cy="24" r="4" fill="#F5D547" {OL}/><path d="M22 28 v8 M54 22 v8 M80 32 v6" stroke="#3b2a1a" stroke-width="1.6" stroke-dasharray="2 2"/>'),
 "peristalsis": dict(words=["الحركة الدودية", "البلع"], only=S, anim="wiggle", face=(50, 50, .38),
   body='<path d="M30 2 C30 30 38 40 38 50 C38 60 30 70 30 98 M70 2 C70 30 62 40 62 50 C62 60 70 70 70 98" fill="none" stroke="#E98AA4" stroke-width="8" stroke-linecap="round"/>'
        '<path d="M30 2 C30 30 38 40 38 50 C38 60 30 70 30 98 M70 2 C70 30 62 40 62 50 C62 60 70 70 70 98" fill="none" stroke="#3b2a1a" stroke-width="1.4"/>'
        '<circle cx="50" cy="76" r="11" fill="#E9A54D" {OL}/><path d="M24 44 l6 4 M24 56 l6 -4 M76 44 l-6 4 M76 56 l-6 -4" stroke="#C25A79" stroke-width="2.4" stroke-linecap="round"/>'),
 "bile": dict(words=["العصارة الصفراوية", "المرارة", "حصى المرارة", "الكبد والمرارة"], only=S, anim="drip", face=(46, 52, .45),
   body='<path d="M60 10 C78 14 84 34 76 52 C68 72 58 88 42 88 C24 88 16 70 22 54 C28 40 40 34 46 22 C50 14 54 8 60 10Z" fill="#8DC26F" {OL}/>'
        '<path d="M60 10 C62 4 70 2 74 6" fill="none" stroke="#3b2a1a" stroke-width="3"/><circle cx="76" cy="84" r="3.4" fill="#8DC26F" {OL}/><circle cx="84" cy="74" r="2.6" fill="#8DC26F" {OL}/>'),
 "nephron": dict(words=["الوحدة الأنبوبية الكلوية (النفرون)", "النفرون", "الكبيبة", "إعادة الامتصاص", "الوحدة الأنبوبية الكلوية"], only=S, anim="bob", face=(28, 26, .36),
   body='<circle cx="28" cy="24" r="16" fill="#F6C1D4" {OL}/><path d="M20 18 q4 6 8 0 t8 0 M18 28 q5 6 10 0 t10 0" fill="none" stroke="#E2504C" stroke-width="1.8"/>'
        '<path d="M44 26 C60 26 64 34 56 42 C48 50 60 56 70 52 L70 86 C70 94 58 94 58 86 L58 62 C50 66 40 60 44 50" fill="none" stroke="#E9A54D" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>'
        '<path d="M84 20 V96" stroke="#E9A54D" stroke-width="7" stroke-linecap="round"/><path d="M70 30 H84" stroke="#E9A54D" stroke-width="5"/>'),
 # ---------- the skeleton and the muscles ----------
 "joint": dict(words=["الأربطة", "الغضروف", "الغضاريف", "الرضفة", "الأربطة والأوتار", "المفاصل المتحركة"], only=S, anim="wobble", face=(50, 50, .38),
   body='<path d="M36 4 L40 36 C30 40 30 50 40 50 L60 50 C70 50 70 40 60 36 L64 4Z" fill="#F5EEDC" {OL}/><path d="M38 96 L42 64 C32 60 32 50 42 50 L58 50 C68 50 68 60 58 64 L62 96Z" fill="#F5EEDC" {OL}/>'
        '<path d="M36 48 C44 44 56 44 64 48 C56 54 44 54 36 48Z" fill="#9CCFD8" {OL}/><path d="M30 34 C26 46 26 54 32 66 M70 34 C74 46 74 54 68 66" fill="none" stroke="#E2504C" stroke-width="4" stroke-linecap="round"/>'),
 "spine": dict(words=["الفقرات", "العمود الفقري", "الهيكل المحوري", "الفقرة"], only=S, anim="wobble", face=(50, 50, .36),
   body="".join(f'<rect x="{36 + (2 if i % 2 else 0)}" y="{4 + i * 12}" width="26" height="9" rx="4" fill="#F5EEDC" {{OL}}/><path d="M{30 + (2 if i % 2 else 0)} {8 + i * 12} h6 M{62 + (2 if i % 2 else 0)} {8 + i * 12} h6" stroke="#3b2a1a" stroke-width="2"/>' for i in range(8))
        + "".join(f'<rect x="{40 + (2 if i % 2 else 0)}" y="{13 + i * 12}" width="18" height="3" rx="1.5" fill="#9CCFD8"/>' for i in range(7))),
 "ribcage": dict(words=["الأضلاع", "القفص الصدري", "الحزام الصدري", "الحزام الحوضي", "الهيكل الطرفي", "عظم القص"], only=S, anim="wobble", face=(50, 30, .36),
   body='<path d="M50 6 V90" stroke="#F5EEDC" stroke-width="8" stroke-linecap="round"/><path d="M50 6 V90" stroke="#3b2a1a" stroke-width="1.4"/>'
        + "".join(f'<path d="M50 {18 + i * 14} C{30 - i * 2} {14 + i * 14} {16 - i} {30 + i * 14} {26 + i * 2} {42 + i * 14} M50 {18 + i * 14} C{70 + i * 2} {14 + i * 14} {84 + i} {30 + i * 14} {74 - i * 2} {42 + i * 14}" fill="none" stroke="#E9D9B8" stroke-width="6" stroke-linecap="round"/>'
                  f'<path d="M50 {18 + i * 14} C{30 - i * 2} {14 + i * 14} {16 - i} {30 + i * 14} {26 + i * 2} {42 + i * 14} M50 {18 + i * 14} C{70 + i * 2} {14 + i * 14} {84 + i} {30 + i * 14} {74 - i * 2} {42 + i * 14}" fill="none" stroke="#3b2a1a" stroke-width="1.8"/>' for i in range(4))),
 "fracture": dict(words=["الكسور", "الكسر", "كسور العظام", "الكساح", "هشاشة العظام"], only=S, anim="wobble", face=(50, 74, .4),
   body='<path d="M10 30 C4 22 12 12 20 18 C24 10 34 14 32 22 L48 40 L44 46 L60 54 L66 60 L80 74 C88 70 96 80 88 86 C94 92 84 100 78 92 C74 98 64 92 70 86 L54 70 L58 64 L42 56 L36 50 L22 36 C14 40 6 34 10 30Z" fill="#F5EEDC" {OL}/>'
        '<path d="M48 40 L44 46 L60 54 L54 70" fill="none" stroke="#E2504C" stroke-width="2.4" stroke-linejoin="round"/>'),
 "muscle_fiber": dict(words=["الليف العضلي", "الأكتين والميوسين", "نظرية انزلاق الخيوط", "الانقباض العضلي", "القطعة العضلية", "التشنج العضلي", "الألياف العضلية"], only=S, anim="bounce", face=(50, 84, .36),
   body='<rect x="4" y="18" width="92" height="56" rx="10" fill="#F4B6B6" {OL}/>'
        + "".join(f'<path d="M{x} 18 V74" stroke="#C25A5A" stroke-width="2"/>' for x in (24, 50, 76))
        + "".join(f'<path d="M{a} {y} H{b}" stroke="#E2504C" stroke-width="3" stroke-linecap="round"/>' for y in (30, 46, 62) for a, b in ((26, 44), (56, 74)))
        + "".join(f'<path d="M{a} {y} H{b}" stroke="#7A4E9F" stroke-width="5" stroke-linecap="round"/>' for y in (38, 54) for a, b in ((36, 64),))),
 # ---------- the skin ----------
 "skin": dict(words=["البشرة", "الأدمة", "بصيلة الشعر", "الشعرة", "الشعر", "الزهم", "طبقات الجلد", "الجلد", "الأظافر", "الكيراتين", "الميلانين", "حب الشباب", "الحروق ودرجاتها", "الحروق"], only=S, anim="sway", face=(30, 52, .36),
   body='<path d="M4 24 H96 V40 H4Z" fill="#F7D6B5" {OL}/><path d="M4 40 H96 V74 H4Z" fill="#F2B8A0" {OL}/><path d="M4 74 H96 V96 H4Z" fill="#F7E9C9" {OL}/>'
        '<path d="M64 4 C66 14 64 22 66 32 L68 58" fill="none" stroke="#3b2a1a" stroke-width="2.4"/><ellipse cx="68" cy="62" rx="5" ry="7" fill="#C98A55" {OL}/>'
        '<path d="M80 64 C76 56 86 52 84 46" fill="none" stroke="#7FD6C9" stroke-width="3"/><circle cx="84" cy="66" r="4" fill="#7FD6C9" {OL}/>'
        '<circle cx="18" cy="84" r="5" fill="#FFE7A3" {OL}/><circle cx="32" cy="86" r="4" fill="#FFE7A3" {OL}/>'),
 # ---------- the first cells of life ----------
 "egg_cell": dict(words=["البويضة", "المشيج", "الأمشاج", "الإباضة", "الخلية الجنسية", "الخلايا الجنسية"], only=S, anim="bob", face=(50, 56, .55),
   body='<circle cx="50" cy="50" r="42" fill="#FFF4D6" {OL}/><circle cx="50" cy="50" r="34" fill="#FFE7A3" {OL}/><circle cx="62" cy="38" r="9" fill="#F5C26B" {OL}/>'
        + "".join(f'<circle cx="{50 + 44 * c}" cy="{50 + 44 * s}" r="4" fill="#F7B5C4" {{OL}}/>' for c, s in ((1, 0), (0.7, 0.7), (0, 1), (-0.7, 0.7), (-1, 0), (-0.7, -0.7), (0, -1), (0.7, -0.7)))),
 "fertilization": dict(words=["الإخصاب", "عملية الإخصاب", "الإخصاب الخارجي", "الإخصاب الداخلي"], only=S, anim="bob", face=(60, 60, .45),
   body='<circle cx="60" cy="56" r="34" fill="#FFE7A3" {OL}/><circle cx="66" cy="46" r="8" fill="#F5C26B" {OL}/>'
        '<ellipse cx="22" cy="40" rx="6" ry="4" fill="#9CCFD8" {OL}/><path d="M16 40 C10 36 6 44 2 40" fill="none" stroke="#3b2a1a" stroke-width="2"/>'
        '<ellipse cx="18" cy="72" rx="6" ry="4" fill="#9CCFD8" {OL}/><path d="M12 72 C6 68 4 76 0 72" fill="none" stroke="#3b2a1a" stroke-width="2"/>'
        '<ellipse cx="30" cy="56" rx="6" ry="4" fill="#9CCFD8" {OL}/><path d="M24 56 C18 52 14 60 10 56" fill="none" stroke="#3b2a1a" stroke-width="2"/>'),
 "zygote": dict(words=["الزيجوت", "البيضة المخصبة", "الانقسام الأول", "التفلج"], only=S, anim="wobble", face=(50, 80, .38),
   body='<circle cx="50" cy="50" r="42" fill="#FFF4D6" {OL}/><circle cx="36" cy="48" r="20" fill="#FFE7A3" {OL}/><circle cx="64" cy="48" r="20" fill="#FFE7A3" {OL}/>'
        '<circle cx="36" cy="46" r="5" fill="#F5C26B"/><circle cx="64" cy="46" r="5" fill="#F5C26B"/>'),
 "blastula": dict(words=["البلاستيولا", "الكيسة الأريمية", "الجاسترولا", "الطبقات الجنينية", "التوتية", "النمو الجنيني"], only=S, anim="bob", face=(50, 52, .45),
   body='<circle cx="50" cy="50" r="42" fill="#FFF4D6" {OL}/>'
        + "".join(f'<circle cx="{50 + 33 * c:.1f}" cy="{50 + 33 * s:.1f}" r="9" fill="#FFE7A3" {{OL}}/>' for c, s in ((1, 0), (.87, .5), (.5, .87), (0, 1), (-.5, .87), (-.87, .5), (-1, 0), (-.87, -.5), (-.5, -.87), (0, -1), (.5, -.87), (.87, -.5)))),
 "fetus": dict(words=["الحبل السري", "المشيمة", "الأمنيون", "الكيس الرهلي", "الكيس المحي", "فترة الحمل", "الجنين", "الولادة", "الانغراس"], only=S, anim="bob", face=(46, 42, .5),
   body='<circle cx="50" cy="52" r="44" fill="#E3F2FD" {OL}/><circle cx="46" cy="38" r="18" fill="#F7C6A5" {OL}/><path d="M34 52 C26 66 36 82 54 80 C70 78 74 62 64 52 C58 46 46 48 40 50Z" fill="#F7C6A5" {OL}/>'
        '<path d="M58 66 C70 72 80 76 88 70" fill="none" stroke="#E98AA4" stroke-width="4" stroke-linecap="round"/>'),
 # ---------- DNA → RNA → protein ----------
 "rna": dict(words=["RNA الرسول", "الكودون", "النسخ", "الحمض النووي الريبوزي", "mRNA"], only=S, anim="wiggle", face=(50, 82, .38),
   body='<path d="M8 30 C24 18 40 42 56 30 S84 18 94 30" fill="none" stroke="#8E6FD8" stroke-width="6" stroke-linecap="round"/>'
        + "".join(f'<rect x="{x - 5}" y="34" width="10" height="16" rx="3" fill="{c}" {{OL}}/><text x="{x}" y="64" text-anchor="middle" font-size="11" font-weight="800" fill="#3b2a1a" direction="ltr">{t}</text>' for x, c, t in ((16, "#E2504C", "A"), (32, "#5DBB63", "U"), (48, "#F5A623", "G"), (64, "#5B8DEF", "C"), (80, "#E2504C", "A")))),
 "trna": dict(words=["RNA الناقل", "الأحماض الأمينية", "الحمض الأميني", "tRNA"], only=S, anim="bob", face=(50, 46, .4),
   body='<path d="M50 30 C30 30 18 40 22 54 C26 66 40 62 42 72 L42 90 L58 90 L58 72 C60 62 74 66 78 54 C82 40 70 30 50 30Z" fill="#C9B6F5" {OL}/>'
        '<rect x="38" y="88" width="24" height="10" rx="3" fill="#F5A623" {OL}/><path d="M50 30 V12" stroke="#8E6FD8" stroke-width="4"/><circle cx="50" cy="10" r="8" fill="#7CC96F" {OL}/>'),
 "ribosome": dict(words=["الترجمة", "RNA الرايبوسومي", "الرايبوسومات", "الرايبوسوم", "بناء البروتين", "تصنيع البروتين"], only=S, anim="bob", face=(50, 40, .45),
   body='<ellipse cx="50" cy="38" rx="32" ry="22" fill="#B9A2F0" {OL}/><ellipse cx="50" cy="68" rx="38" ry="16" fill="#D6C8F7" {OL}/>'
        '<path d="M2 66 H98" stroke="#E2504C" stroke-width="3" stroke-dasharray="6 3"/>' + "".join(f'<circle cx="{x}" cy="{y}" r="5" fill="{c}" {{OL}}/>' for x, y, c in ((72, 12, "#7CC96F"), (82, 6, "#F5A623"), (92, 10, "#5B8DEF")))),
 "replication": dict(words=["التضاعف شبه المحافظ", "قطع أوكازاكي", "الشريط الرئيس", "الشريط المتأخر", "إنزيم الهيليكيز", "تضاعف DNA", "تضاعف الحمض النووي"], only=S, anim="wiggle", face=(16, 50, .36),
   body='<path d="M4 44 H40 M4 56 H40" stroke="#5B8DEF" stroke-width="4"/>' + "".join(f'<path d="M{x} 44 V56" stroke="#F5A623" stroke-width="3"/>' for x in (10, 20, 30))
        + '<path d="M40 44 C56 40 70 24 96 16 M40 56 C56 60 70 76 96 84" fill="none" stroke="#5B8DEF" stroke-width="4" stroke-linecap="round"/>'
        '<path d="M58 34 C70 28 80 22 92 20 M58 66 C70 72 80 78 92 80" fill="none" stroke="#E2504C" stroke-width="4" stroke-linecap="round" stroke-dasharray="10 4"/>'
        '<circle cx="44" cy="50" r="7" fill="#7CC96F" {OL}/>'),
 "nucleotide": dict(words=["النيوكليوتيد", "النيوكليوتيدات", "القواعد النيتروجينية", "قاعدة تشارجاف", "القاعدة النيتروجينية"], only=S, anim="bob", face=(50, 82, .36),
   body='<circle cx="20" cy="30" r="13" fill="#F5D547" {OL}/><text x="20" y="35" text-anchor="middle" font-size="13" font-weight="800" fill="#3b2a1a" direction="ltr">P</text>'
        '<path d="M32 36 L44 44" stroke="#3b2a1a" stroke-width="3"/><path d="M50 32 L64 42 L60 58 L40 58 L36 42Z" fill="#F7B5C4" {OL}/>'
        '<path d="M62 50 L72 50" stroke="#3b2a1a" stroke-width="3"/><rect x="72" y="38" width="22" height="24" rx="4" fill="#7CC6F2" {OL}/><text x="83" y="55" text-anchor="middle" font-size="13" font-weight="800" fill="#3b2a1a" direction="ltr">A</text>'),
 "mutation": dict(words=["الطفرة", "الطفرات", "الطفرة النقطية", "طفرة الإزاحة", "المواد المطفرة", "الطفرات الكروموسومية"], only=S, anim="buzz", face=(50, 84, .36),
   body='<path d="M10 20 H90 M10 60 H90" stroke="#5B8DEF" stroke-width="5" stroke-linecap="round"/>'
        + "".join(f'<path d="M{x} 20 V60" stroke="{"#E2504C" if x == 50 else "#F5A623"}" stroke-width="{6 if x == 50 else 4}"/>' for x in (18, 34, 50, 66, 82))
        + '<path d="M60 4 L52 18 L60 18 L54 32" fill="none" stroke="#F5C518" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>'),
 "pedigree": dict(words=["سجل النسب", "مخطط السلالة", "شجرة العائلة الوراثية"], only=S, anim="bob", face=(50, 86, .3),
   body='<rect x="16" y="8" width="18" height="18" fill="#7CC6F2" {OL}/><circle cx="74" cy="17" r="10" fill="#fff" {OL}/><path d="M34 17 H64 M50 17 V42 M22 42 H78 M22 42 V52 M50 42 V52 M78 42 V52" fill="none" stroke="#3b2a1a" stroke-width="2.4"/>'
        '<circle cx="22" cy="62" r="10" fill="#7CC6F2" {OL}/><rect x="41" y="52" width="18" height="18" fill="#fff" {OL}/><rect x="69" y="52" width="18" height="18" fill="#7CC6F2" {OL}/>'),
 # ---------- cells: transport, energy ----------
 "osmosis": dict(words=["الخاصية الأسموزية", "الأسموزية", "الانتشار الغشائي", "النقل السلبي"], only=S, anim="drip", face=(50, 30, .3),
   body='<path d="M14 20 V82 C14 92 24 96 32 96 L68 96 C76 96 86 92 86 82 V20" fill="none" stroke="#3b2a1a" stroke-width="3"/><path d="M50 50 V96" stroke="#8E6FD8" stroke-width="3" stroke-dasharray="4 3"/>'
        '<path d="M16 56 H48 V94 H30 C22 94 16 90 16 82Z" fill="#7CC6F2" opacity=".75"/><path d="M52 44 H84 V82 C84 90 78 94 70 94 H52Z" fill="#7CC6F2" opacity=".75"/>'
        '<circle cx="64" cy="64" r="4" fill="#F5A623"/><circle cx="74" cy="76" r="4" fill="#F5A623"/><circle cx="62" cy="84" r="4" fill="#F5A623"/><path d="M34 70 h18 M46 64 l6 6 l-6 6" fill="none" stroke="#3b2a1a" stroke-width="2.4"/>'),
 "active_transport": dict(words=["النقل النشط", "المضخات الغشائية", "مضخة الصوديوم والبوتاسيوم"], only=S, anim="bounce", face=(50, 50, .34),
   body='<path d="M0 30 H40 M60 30 H100 M0 70 H40 M60 70 H100" stroke="#F5C26B" stroke-width="10" stroke-linecap="round"/><rect x="38" y="20" width="24" height="60" rx="8" fill="#B9A2F0" {OL}/>'
        '<circle cx="50" cy="8" r="6" fill="#E2504C" {OL}/><circle cx="50" cy="92" r="6" fill="#E2504C" {OL}/><path d="M50 84 V70 M44 76 l6 -6 l6 6" fill="none" stroke="#3b2a1a" stroke-width="2"/>'
        '<rect x="72" y="42" width="22" height="16" rx="3" fill="#F5D547" {OL}/><text x="83" y="54" text-anchor="middle" font-size="9" font-weight="800" fill="#3b2a1a" direction="ltr">ATP</text>'),
 "membrane": dict(words=["النموذج الفسيفسائي المائع", "الغشاء البلازمي", "الغشاء الخلوي", "طبقة الدهون المفسفرة", "الدهون المفسفرة"], only=S, anim="sway", face=(50, 50, .34),
   body="".join(f'<circle cx="{x}" cy="26" r="6" fill="#7CC6F2" {{OL}}/><path d="M{x - 2} 32 V46 M{x + 2} 32 V46" stroke="#F5C26B" stroke-width="2"/>'
                f'<circle cx="{x}" cy="74" r="6" fill="#7CC6F2" {{OL}}/><path d="M{x - 2} 68 V54 M{x + 2} 68 V54" stroke="#F5C26B" stroke-width="2"/>' for x in (8, 22, 36, 64, 78, 92))
        + '<rect x="42" y="16" width="16" height="68" rx="8" fill="#B9A2F0" {OL}/>'),
 "atp": dict(words=["ATP", "جزيء الطاقة"], only=S, anim="buzz", face=(50, 78, .4),
   body='<rect x="12" y="26" width="70" height="44" rx="8" fill="#5DBB63" {OL}/><rect x="82" y="38" width="8" height="20" rx="2" fill="#3b2a1a"/>'
        '<text x="47" y="56" text-anchor="middle" font-size="24" font-weight="800" fill="#fff" direction="ltr">ATP</text><path d="M56 6 L48 20 L56 20 L50 32" fill="none" stroke="#F5C518" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>'),
 "krebs": dict(words=["حلقة كربس", "دورة كربس", "سلسلة نقل الإلكترونات", "التنفس الخلوي الهوائي", "الأيض", "البناء والهدم"], only=S, anim="sun", face=(50, 52, .45),
   body='<circle cx="50" cy="50" r="32" fill="#FFF4D6" {OL}/><path d="M50 18 A32 32 0 0 1 82 50" fill="none" stroke="#E2504C" stroke-width="4"/><path d="M76 42 l6 8 l6 -8" fill="none" stroke="#E2504C" stroke-width="4" stroke-linejoin="round"/>'
        '<path d="M50 82 A32 32 0 0 1 18 50" fill="none" stroke="#5B8DEF" stroke-width="4"/><path d="M24 58 l-6 -8 l-6 8" fill="none" stroke="#5B8DEF" stroke-width="4" stroke-linejoin="round"/>'
        + "".join(f'<circle cx="{x}" cy="{y}" r="6" fill="{c}" {{OL}}/>' for x, y, c in ((50, 18, "#F5A623"), (82, 50, "#7CC96F"), (50, 82, "#F5A623"), (18, 50, "#7CC96F")))),
 "fermentation": dict(words=["التخمر الكحولي", "تخمر حمض اللاكتيك", "التخمر", "الخميرة", "التنفس اللاهوائي"], only=S, anim="bob", face=(50, 74, .45),
   body='<path d="M38 4 H62 V30 L84 82 C88 92 82 96 74 96 H26 C18 96 12 92 16 82 L38 30Z" fill="#E3F2FD" {OL}/><path d="M28 60 H72 L82 84 C84 90 80 92 74 92 H26 C20 92 16 90 18 84Z" fill="#F5D88A"/>'
        + "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" {{OL}}/>' for x, y, r in ((44, 50, 3), (56, 42, 4), (50, 30, 3), (60, 22, 2.6), (46, 14, 3)))
        + "".join(f'<circle cx="{x}" cy="{y}" r="4" fill="#C9A06A" {{OL}}/>' for x, y in ((36, 80), (54, 84), (66, 78)))),
 "chloroplast_parts": dict(words=["الثايلاكويد", "الجرانا", "اللحمة (الستروما)", "الستروما", "البلاستيدة الخضراء"], only=S, anim="bob", face=(50, 80, .36),
   body='<ellipse cx="50" cy="50" rx="46" ry="30" fill="#BDE7A6" {OL}/><ellipse cx="50" cy="50" rx="40" ry="24" fill="#D4F0C4"/>'
        + "".join(f'<rect x="{x}" y="{y}" width="14" height="5" rx="2.5" fill="#4FA35A" {{OL}}/>' for x in (22, 43, 64) for y in (34, 40, 46, 52, 58))),
 # ---------- plants ----------
 "xylem_phloem": dict(words=["الخشب", "اللحاء", "الخشب واللحاء", "الأنسجة الوعائية", "الحزم الوعائية", "النقل في النبات"], only=S, anim="sway", face=(50, 50, .34),
   body='<rect x="22" y="2" width="56" height="96" rx="18" fill="#BDE7A6" {OL}/><rect x="32" y="8" width="14" height="84" rx="6" fill="#7CC6F2" {OL}/><rect x="54" y="8" width="14" height="84" rx="6" fill="#F5C26B" {OL}/>'
        '<path d="M39 70 V30 M33 38 l6 -8 l6 8" fill="none" stroke="#1F5F99" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>'
        '<path d="M61 30 V70 M55 62 l6 8 l6 -8" fill="none" stroke="#A86B1F" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>'),
 "stomata": dict(words=["الثغور", "الثغر", "البشرة والخلايا الحارسة", "الخلايا الحارسة", "النتح"], only=S, anim="bob", face=(50, 86, .3),
   body='<rect x="4" y="4" width="92" height="92" rx="14" fill="#D4F0C4" {OL}/><path d="M50 16 C26 16 22 50 50 84 C78 50 74 16 50 16Z" fill="#7CC96F" {OL}/>'
        '<path d="M50 24 C40 34 40 66 50 76 C60 66 60 34 50 24Z" fill="#2E5E36"/><path d="M50 30 q-4 -10 2 -18 M56 24 q4 -8 0 -16" fill="none" stroke="#7CC6F2" stroke-width="2.4" stroke-linecap="round"/>'),
 "fern": dict(words=["السراخس", "السرخس", "الأبواغ", "الأبواغ الداخلية", "البثرات البوغية", "الطور البوغي", "الطور المشيجي", "تعاقب الأجيال", "الجذمور", "أشباه الجذور", "الحزازيات الصولجانية"], only=S, anim="sway", face=(50, 90, .3),
   body='<path d="M50 96 C50 70 46 40 30 10" fill="none" stroke="#4FA35A" stroke-width="4" stroke-linecap="round"/>'
        + "".join(f'<ellipse cx="{50 - k * 3 - 8:.1f}" cy="{86 - k * 9}" rx="{14 - k}" ry="4" fill="#7CC96F" transform="rotate(-20 {50 - k * 3 - 8:.1f} {86 - k * 9})" {{OL}}/>'
                  f'<ellipse cx="{50 - k * 3 + 10:.1f}" cy="{84 - k * 9}" rx="{13 - k}" ry="4" fill="#7CC96F" transform="rotate(25 {50 - k * 3 + 10:.1f} {84 - k * 9})" {{OL}}/>' for k in range(1, 8))
        + "".join(f'<circle cx="{x}" cy="{y}" r="1.8" fill="#A0522D"/>' for x, y in ((36, 76), (38, 67), (56, 74), (58, 65)))),
 "moss": dict(words=["الحزازيات", "الحزاز", "النباتات اللاوعائية"], only=S, anim="sway", face=(50, 84, .36),
   body='<path d="M4 96 C10 70 30 66 50 70 C70 66 90 70 96 96Z" fill="#6CBF5A" {OL}/>'
        + "".join(f'<path d="M{x} 70 V{y}" stroke="#8B6B3D" stroke-width="2"/><ellipse cx="{x}" cy="{y - 4}" rx="3" ry="5" fill="#C9A06A" {{OL}}/>' for x, y in ((26, 30), (42, 22), (58, 28), (74, 34)))
        + "".join(f'<circle cx="{x}" cy="{y}" r="4" fill="#4FA35A"/>' for x, y in ((16, 84), (30, 78), (46, 82), (62, 78), (78, 84)))),
 "seed_leaves": dict(words=["ذوات الفلقتين", "ذوات الفلقة الواحدة", "الفلقة", "الفلقات"], only=S, anim="grow", face=(50, 84, .34),
   body='<path d="M0 74 H100 V100 H0Z" fill="#B88A5A"/><path d="M30 74 V44" stroke="#5DBB63" stroke-width="4"/><path d="M30 46 C20 44 14 36 16 28 C26 30 30 38 30 46Z M30 46 C40 44 46 36 44 28 C34 30 30 38 30 46Z" fill="#7CC96F" {OL}/>'
        '<path d="M72 74 V30" stroke="#5DBB63" stroke-width="4"/><path d="M72 32 C66 22 70 10 76 6 C80 16 78 26 72 32Z" fill="#9BD67F" {OL}/>'
        '<text x="30" y="92" text-anchor="middle" font-size="12" font-weight="800" fill="#fff">2</text><text x="72" y="92" text-anchor="middle" font-size="12" font-weight="800" fill="#fff">1</text>'),
 "flower_parts": dict(words=["السبلات والبتلات", "الكربلة (المدقة)", "المدقة", "الأسدية", "الإخصاب المزدوج", "الإندوسبيرم", "الكيس الجنيني", "أجزاء الزهرة"], only=S, anim="sway", face=(50, 46, .36),
   body='<path d="M50 96 V64" stroke="#5DBB63" stroke-width="4"/><path d="M50 66 C30 70 20 56 26 46 C34 50 44 56 50 66Z M50 66 C70 70 80 56 74 46 C66 50 56 56 50 66Z" fill="#7CC96F" {OL}/>'
        + "".join(f'<ellipse cx="{50 + 22 * c:.1f}" cy="{40 + 18 * s:.1f}" rx="13" ry="9" fill="#F28AA8" transform="rotate({a} {50 + 22 * c:.1f} {40 + 18 * s:.1f})" {{OL}}/>' for c, s, a in ((1, 0, 0), (-1, 0, 0), (.5, -.9, 60), (-.5, -.9, -60)))
        + '<path d="M50 52 V24" stroke="#F5A623" stroke-width="4"/><circle cx="50" cy="22" r="4" fill="#F5A623" {OL}/><path d="M42 50 L36 30 M58 50 L64 30" stroke="#E3A70F" stroke-width="2"/><circle cx="36" cy="28" r="3" fill="#F5D547" {OL}/><circle cx="64" cy="28" r="3" fill="#F5D547" {OL}/>'),
 # ---------- animals ----------
 "sea_urchin": dict(words=["قنفذ البحر", "خيار البحر", "الأقدام الأنبوبية", "الجهاز الوعائي المائي"], only=S, anim="wobble", face=(50, 58, .45),
   body="".join(f'<path d="M50 56 L{50 + 46 * c:.1f} {56 + 40 * s:.1f}" stroke="#7A4E9F" stroke-width="3" stroke-linecap="round"/>' for c, s in ((1, 0), (.9, -.45), (.6, -.8), (.2, -.98), (-.2, -.98), (-.6, -.8), (-.9, -.45), (-1, 0), (.95, .3), (-.95, .3)))
        + '<path d="M14 66 C14 40 30 28 50 28 C70 28 86 40 86 66 C86 76 76 84 50 84 C24 84 14 76 14 66Z" fill="#B58BD9" {OL}/>'),
 "flatworm": dict(words=["البلاناريا", "الديدان المسطحة", "الخلايا اللهبية", "التجدد"], only=S, anim="wiggle", face=(50, 30, .4),
   body='<path d="M50 6 C66 6 74 18 70 30 C80 34 70 40 66 46 C70 66 64 88 50 94 C36 88 30 66 34 46 C30 40 20 34 30 30 C26 18 34 6 50 6Z" fill="#E9B58C" {OL}/>'
        '<path d="M50 40 V84" stroke="#C98A55" stroke-width="2" stroke-dasharray="3 3"/>'),
 "arachnid": dict(words=["العنكبيات", "العقارب", "القراد", "الرئات الكتابية", "العقرب"], only=S, anim="wiggle", face=(50, 56, .4),
   body='<path d="M50 30 C50 18 44 8 34 8 C26 8 26 18 32 18" fill="none" stroke="#8B5A2B" stroke-width="5" stroke-linecap="round"/><path d="M30 18 l-6 -4 M30 18 l-4 6" stroke="#8B5A2B" stroke-width="3" stroke-linecap="round"/>'
        '<ellipse cx="50" cy="56" rx="18" ry="26" fill="#A87449" {OL}/><circle cx="50" cy="30" r="10" fill="#A87449" {OL}/>'
        + "".join(f'<path d="M{34 if d < 0 else 66} {44 + i * 10} L{12 if d < 0 else 88} {40 + i * 12}" stroke="#8B5A2B" stroke-width="3" stroke-linecap="round"/>' for d in (-1, 1) for i in range(4))),
 "bivalve": dict(words=["ذوات المصراعين", "المحار", "المصراعان", "بلح البحر"], only=S, anim="bob", face=(50, 56, .45),
   body='<path d="M8 56 C8 26 30 10 50 10 C70 10 92 26 92 56Z" fill="#E8C3A0" {OL}/><path d="M8 56 C14 80 34 92 50 92 C66 92 86 80 92 56Z" fill="#D9A97E" {OL}/>'
        '<path d="M50 12 L24 54 M50 12 L38 54 M50 12 L62 54 M50 12 L76 54" stroke="#B5835A" stroke-width="2"/><circle cx="50" cy="60" r="5" fill="#fff" {OL}/>'),
 "mollusk": dict(words=["رأسية القدم", "الأخطبوط", "الحبار"], only=S, anim="wiggle", face=(50, 42, .45),
   body='<path d="M50 10 C72 10 82 26 80 44 C78 58 66 62 50 62 C34 62 22 58 20 44 C18 26 28 10 50 10Z" fill="#E98AA4" {OL}/>'
        + "".join(f'<path d="M{x} 58 C{x - 6} 70 {x + 6} 80 {x - 2} 94" fill="none" stroke="#E98AA4" stroke-width="7" stroke-linecap="round"/>' for x in (28, 40, 52, 64, 76))),
 "phage": dict(words=["العاثية", "العاثيات", "البريون", "الدورة الاندماجية", "الدورة التحللية", "آكلات البكتيريا"], only=S, anim="bob", face=(50, 22, .4),
   body='<path d="M50 2 L70 12 L70 32 L50 42 L30 32 L30 12Z" fill="#B9A2F0" {OL}/><rect x="45" y="42" width="10" height="30" fill="#9AA5B1" {OL}/>'
        '<path d="M44 72 L24 92 M50 72 L40 96 M56 72 L76 92 M50 72 L60 96" stroke="#3b2a1a" stroke-width="3" stroke-linecap="round"/><path d="M40 72 H60" stroke="#3b2a1a" stroke-width="4"/>'),
 "feather": dict(words=["الريش", "الريش الزغبي", "الريش الكفافي", "الريشة"], only=S, anim="sway", face=(46, 46, .38),
   body='<path d="M82 6 C50 10 26 40 22 74 L50 52 C66 40 78 24 82 6Z" fill="#9FD0F5" {OL}/><path d="M82 6 C70 30 40 60 14 94" fill="none" stroke="#3b2a1a" stroke-width="3" stroke-linecap="round"/>'
        '<path d="M70 18 L58 16 M62 30 L48 30 M52 42 L38 44 M42 54 L30 58" stroke="#5AA9DC" stroke-width="2"/>'),
 # ---------- health ----------
 "heart": dict(words=["الأذينان", "البطينان", "حجرات القلب", "صمامات القلب", "منظم النبض", "النبض", "الدورة الدموية الكبرى والصغرى"], only=S, anim="bounce", face=(50, 54, .45),
   body='<path d="M50 92 C22 74 8 54 12 34 C16 16 36 12 50 28 C64 12 84 16 88 34 C92 54 78 74 50 92Z" fill="#E2504C" {OL}/><path d="M50 30 V84 M20 52 H80" stroke="#B5362B" stroke-width="2.4" stroke-dasharray="4 3"/>'
        '<path d="M38 26 V6 M50 28 V4 M62 26 V8" stroke="#5B8DEF" stroke-width="5" stroke-linecap="round"/>'),
 "heart_attack": dict(words=["النوبة القلبية", "الذبحة الصدرية", "الجلطة", "أمراض القلب", "تصلب الشرايين", "ارتفاع ضغط الدم"], only=S, anim="bounce", face=(50, 50, .5),
   body='<path d="M50 90 C20 70 6 50 10 32 C14 16 34 10 50 26 C66 10 86 16 90 32 C94 50 80 70 50 90Z" fill="#E2504C" {OL}/>'
        '<path d="M14 54 H34 L40 40 L48 68 L56 46 L62 54 H86" fill="none" stroke="#fff" stroke-width="3.4" stroke-linejoin="round" stroke-linecap="round"/>'),
 "headache": dict(words=["الصداع النصفي", "الصداع", "الصرع", "التصلب المتعدد"], only=S, anim="wobble", face=(50, 60, .55),
   body='<circle cx="50" cy="58" r="34" fill="#F2C9A0" {OL}/><path d="M20 10 L30 24 L22 26 L32 40" fill="none" stroke="#E2504C" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>'
        '<path d="M80 10 L70 24 L78 26 L68 40" fill="none" stroke="#E2504C" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>'),
 "cancer": dict(words=["السرطان", "الأورام", "الورم", "المواد المسرطنة", "الخلايا السرطانية"], only=S, anim="wobble", face=(50, 70, .4),
   body="".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}" {{OL}}/>' for x, y, r, c in ((30, 30, 14, "#E9F7EF"), (70, 28, 12, "#E9F7EF"), (22, 64, 12, "#E9F7EF"), (50, 50, 16, "#F28A8A"), (66, 62, 13, "#F28A8A"), (44, 74, 12, "#F28A8A"), (78, 82, 9, "#F28A8A")))
        + "".join(f'<circle cx="{x}" cy="{y}" r="4" fill="#B5462B"/>' for x, y in ((50, 48), (66, 60), (44, 72)))),
 # ---------- the scientific way ----------
 "hypothesis": dict(words=["الفرضية", "الفرضيات", "النظرية العلمية", "النظرية الخلوية", "فرضيات كوخ", "المبدأ الرئيس في علم الأحياء", "الاستدلال"], only=S, anim="bob", face=(50, 46, .45),
   body='<path d="M50 6 C28 6 16 22 16 38 C16 52 26 60 32 68 L32 78 H68 L68 68 C74 60 84 52 84 38 C84 22 72 6 50 6Z" fill="#FFE27A" {OL}/><rect x="34" y="80" width="32" height="8" rx="3" fill="#9AA5B1" {OL}/><rect x="38" y="90" width="24" height="6" rx="3" fill="#9AA5B1" {OL}/>'
        '<text x="50" y="40" text-anchor="middle" font-size="24" font-weight="800" fill="#B58A1A">؟</text>'),
 "variables": dict(words=["المتغير المستقل والمتغير التابع", "المتغير المستقل", "المتغير التابع", "المجموعة الضابطة", "المتغيرات"], only=S, anim="bob", face=(64, 70, .36),
   body='<path d="M14 6 V86 H96" fill="none" stroke="#3b2a1a" stroke-width="3" stroke-linecap="round"/><path d="M8 14 L14 6 L20 14 M88 80 L96 86 L88 92" fill="none" stroke="#3b2a1a" stroke-width="3" stroke-linejoin="round"/>'
        '<path d="M18 78 L36 62 L52 54 L70 34 L88 22" fill="none" stroke="#5B8DEF" stroke-width="4" stroke-linecap="round"/>' + "".join(f'<circle cx="{x}" cy="{y}" r="4" fill="#F5A623" {{OL}}/>' for x, y in ((36, 62), (52, 54), (70, 34)))
        + '<text x="54" y="99" text-anchor="middle" font-size="10" font-weight="800" fill="#3b2a1a" direction="ltr">x</text><text x="5" y="48" text-anchor="middle" font-size="10" font-weight="800" fill="#3b2a1a" direction="ltr">y</text>'),
 "cladogram": dict(words=["المخطط التفرعي", "علم تطور السلالات", "شجرة التطور", "التصنيف الحديث", "التسمية الثنائية"], only=S, anim="sway", face=(50, 90, .3),
   body='<path d="M50 96 V76 M50 76 L14 10 M50 76 L86 10 M32 43 L50 10 M68 43 L68 10 M23 26 L32 10" fill="none" stroke="#5DBB63" stroke-width="4" stroke-linecap="round"/>'
        + "".join(f'<circle cx="{x}" cy="8" r="6" fill="{c}" {{OL}}/>' for x, c in ((14, "#F28AA8"), (32, "#F5D547"), (50, "#7CC6F2"), (68, "#B58BD9"), (86, "#F5A623")))),
}
ALIAS_ONLY = ("science",)
ALIASES = {"المحور": ("bio.neuron", ("biology",)), 
    # fish, reptiles, mammals: the animal's own drawing (one concept = one drawing)
    "الخياشيم": "sci.fish", "الخط الجانبي": "sci.fish", "المثانة العوامة": "sci.fish", "الزعانف": "sci.fish", "الحراشف": "sci.fish",
    "التماسيح": "sci.reptile", "السحالي والأفاعي": "sci.reptile", "الحيتانيات": "sci.mammal", "القوارض": "sci.mammal", "الرئيسات": "sci.mammal",
    "ذوات الأقدام الألف": "bio.flatworm", "ذوات الأقدام المئة": "bio.flatworm",
    "الحبليات": "bio.spine", "الحبل الظهري": "bio.spine", "الحبل العصبي الظهري الأنبوبي": "bio.spine", "الشقوق البلعومية": "sci.fish", "الذيل خلف الشرجي": "sci.fish",
    "الجهاز السمبثاوي": "bio.impulse", "الجهاز جار السمبثاوي": "bio.impulse", "الجهاز السمبثاوي وجار السمبثاوي": "bio.impulse", "السحايا": "body.brain",
    "الحالب والمثانة": "body.kidney", "الحوصلة والقانصة": "body.stomach", "الحوصلة": "body.stomach", "القانصة": "body.stomach",
    "الإسهال": "body.stomach", "الإمساك": "body.stomach", "الارتجاع المريئي": "body.stomach", "التهاب الزائدة الدودية": "bio.inflammation",
    "الالتهاب الرئوي": "bio.alveoli", "التهاب الشعب الهوائية": "bio.bronchi", "السل": "bio.alveoli", "الإدمان": "bio.synapse", "العقار": "bio.synapse",
    "الاتزان الداخلي": "bio.cerebellum", "الثبات الداخلي": "bio.cerebellum", "نقطة الضبط": "bio.cerebellum", "مركز التحكم": "bio.pituitary",
    "تكون الحيوانات المنوية": "bio.fertilization", "دورة الحيض": "bio.egg_cell", "المبيضان": "bio.egg_cell",
    "الكلوروفيل": "bio.chloroplast_parts", "الكاروتين": "bio.chloroplast_parts",
    "الانشطار الثنائي": "bio.telophase", "التبرعم": "bio.zygote", "السايكلين": "bio.interphase", "نقاط التفتيش": "bio.interphase",
    "الخلايا الجذعية": "bio.blastula", "الخلايا البرنشيمية": "bio.xylem_phloem", "الخلايا الكولنشيمية": "bio.xylem_phloem", "الخلايا الإسكلرنشيمية": "bio.xylem_phloem",
    "الطبقة الشمعية": "bio.stomata", "الجذور والسيقان والأوراق": "bio.xylem_phloem",
    "الإنترون والإكسون": "bio.rna", "عوامل النسخ": "bio.rna", "المشغل (الأوبرون)": "bio.rna", "RNA": "bio.rna",
    "متلازمة داون": "bio.chromatids", "متلازمة تيرنر": "bio.chromatids", "متلازمة كلاينفلتر": "bio.chromatids", "المهق": "bio.pedigree",
    "السيادة المشتركة": "bio.pedigree", "السيادة غير التامة": "bio.pedigree", "التليف الكيسي": "bio.pedigree",
    "رفض الأعضاء المزروعة": "bio.lymphocyte", "الخلايا المطوقة": "sci.jellyfish", "الدوارات": "sci.jellyfish",
    "طور الميدوسا": "sci.jellyfish", "طور البوليب": "sci.jellyfish", "قناديل البحر": "sci.jellyfish", "قنديل البحر": "sci.jellyfish", "الخلايا اللاسعة": "sci.jellyfish",
    "بطنية القدم": "sci.snail", "الرداء": "sci.snail", "القدم العضلية": "sci.snail", "شوكيات الجلد": "sci.starfish", "الجلد الشوكي": "sci.starfish", "الأسكارس": "sci.worm", "العلق": "sci.worm", "الأوتار": "bio.joint", "الأغشية": "bio.membrane",
    "الأعين المركبة": "sci.insect", "الانسلاخ": "sci.insect", "الرأس الصدري": "bio.arachnid",
    "علم الأحياء": "bio.cladogram", "العلم": "bio.hypothesis", "علم التشريح": "body.skeleton", "علم وظائف الأعضاء": "body.skeleton",
    "المستويات التشريحية": "body.skeleton", "الوضع التشريحي": "body.skeleton", "مستويات التنظيم في الجسم": "body.skeleton", "التنظيم": "body.skeleton",
    "قانونا الديناميكا الحرارية": "bio.krebs", "السعر الحراري": "chem.u_calorie",
}
