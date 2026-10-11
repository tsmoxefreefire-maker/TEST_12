"""🆕 batch 40 · living things: the animal groups, the habitats, the plants and the food chains (science, grades 1–9 and biology)."""
F = "sci"
D = {
 # ---------- the animal groups ----------
 "mammal": dict(words=["الثدييات", "ثديي", "ثدييات", "حيوان ثديي"], anim="bob", face=(58, 46, .7),
   body='<ellipse cx="46" cy="64" rx="30" ry="18" fill="#C9A27A" {OL}/><path d="M24 78 L24 94 M38 80 L38 94 M56 80 L56 94 M68 78 L68 94" stroke="#3b2a1a" stroke-width="5" stroke-linecap="round"/>'
        '<path d="M16 60 Q6 54 8 44" fill="none" stroke="#3b2a1a" stroke-width="3" stroke-linecap="round"/><circle cx="62" cy="44" r="18" fill="#D8B48C" {OL}/>'
        '<path d="M48 30 L50 20 L58 28Z M70 28 L78 20 L78 32Z" fill="#C9A27A" {OL}/><ellipse cx="70" cy="52" rx="6" ry="4" fill="#F4C7A1" {OL}/>'),
 "bird": dict(words=["الطيور", "طائر", "طيور", "الطائر"], anim="bob", face=(58, 40, .6),
   body='<path d="M20 60 C20 40 40 30 56 34 C74 36 82 52 76 66 C70 82 40 86 26 76Z" fill="#7CC6F2" {OL}/><path d="M30 58 C40 48 56 52 58 64 C48 70 36 68 30 58Z" fill="#5AA9DC" {OL}/>'
        '<path d="M78 42 L92 46 L78 50Z" fill="#F6B73C" {OL}/><path d="M20 62 L6 56 L10 70Z" fill="#5AA9DC" {OL}/><path d="M44 84 L42 94 M56 84 L58 94" stroke="#E8853C" stroke-width="3.4" stroke-linecap="round"/>'),
 "fish": dict(words=["الأسماك", "سمكة", "أسماك", "السمك"], anim="wiggle", face=(56, 50, .65),
   body='<path d="M14 50 C28 26 66 24 84 50 C66 76 28 74 14 50Z" fill="#F6A04D" {OL}/><path d="M14 50 L2 36 L4 64Z" fill="#F28A2E" {OL}/><path d="M44 34 C50 24 60 26 64 34" fill="#F28A2E" {OL}/>'
        '<path d="M34 40 Q40 50 34 60" fill="none" stroke="#C96A1E" stroke-width="2.4"/>'),
 "reptile": dict(words=["الزواحف", "زاحف", "زواحف", "سحلية", "الضب"], anim="wiggle", face=(72, 50, .5),
   body='<path d="M8 74 C20 70 26 62 34 60 L62 54 C72 44 92 46 92 54 C92 62 76 64 66 64 L40 70 C30 76 18 80 8 74Z" fill="#8BC34A" {OL}/>'
        '<path d="M40 66 L32 84 M56 60 L62 80 M44 58 L38 44 M58 56 L64 42" stroke="#558B2F" stroke-width="4" stroke-linecap="round"/><circle cx="48" cy="62" r="2.2" fill="#558B2F"/><circle cx="56" cy="60" r="2.2" fill="#558B2F"/>'),
 "amphibian": dict(words=["البرمائيات", "برمائي", "برمائيات", "الضفدع", "ضفدع", "ضفادع"], anim="bounce", face=(50, 48, .8),
   body='<ellipse cx="50" cy="66" rx="34" ry="24" fill="#6CC27A" {OL}/><circle cx="32" cy="34" r="12" fill="#6CC27A" {OL}/><circle cx="68" cy="34" r="12" fill="#6CC27A" {OL}/>'
        '<circle cx="32" cy="32" r="6" fill="#fff" {OL}/><circle cx="68" cy="32" r="6" fill="#fff" {OL}/><path d="M18 88 L8 94 M82 88 L92 94" stroke="#3E8E4C" stroke-width="5" stroke-linecap="round"/><ellipse cx="50" cy="74" rx="18" ry="10" fill="#B7E1A1"/>'),
 "insect": dict(words=["الحشرات", "حشرة", "حشرات", "النملة", "نملة"], anim="buzz", face=(50, 56, .62),
   body='<path d="M30 30 L22 14 M70 30 L78 14" stroke="#3b2a1a" stroke-width="3" stroke-linecap="round"/><circle cx="50" cy="36" r="14" fill="#E8574A" {OL}/><ellipse cx="50" cy="66" rx="26" ry="24" fill="#E8574A" {OL}/>'
        '<path d="M50 44 L50 90" stroke="#3b2a1a" stroke-width="2.6"/><circle cx="38" cy="62" r="4.5" fill="#3b2a1a"/><circle cx="62" cy="62" r="4.5" fill="#3b2a1a"/><circle cx="40" cy="80" r="3.5" fill="#3b2a1a"/><circle cx="60" cy="80" r="3.5" fill="#3b2a1a"/>'
        '<path d="M24 58 L10 52 M24 70 L8 72 M76 58 L90 52 M76 70 L92 72" stroke="#3b2a1a" stroke-width="3" stroke-linecap="round"/>'),
 "spider": dict(words=["العنكبوت", "عنكبوت", "العناكب"], anim="wiggle", face=(50, 54, .7),
   body='<path d="M30 46 L8 30 M28 56 L6 56 M30 64 L10 82 M70 46 L92 30 M72 56 L94 56 M70 64 L90 82" stroke="#3b2a1a" stroke-width="3.4" stroke-linecap="round" fill="none"/>'
        '<ellipse cx="50" cy="56" rx="24" ry="22" fill="#6B5B95" {OL}/><path d="M50 8 L50 34" stroke="#3b2a1a" stroke-width="1.6"/>'),
 "worm": dict(words=["الديدان", "دودة", "ديدان"], anim="wiggle", face=(76, 52, .5),
   body='<path d="M8 70 C18 54 30 54 38 66 C46 78 58 78 64 64 C68 54 78 48 86 52 C94 58 90 70 82 72 C74 74 72 66 68 72 C60 88 40 90 30 76 C24 68 18 70 14 76Z" fill="#F4A6A0" {OL}/>'
        '<path d="M26 64 L22 72 M48 76 L48 84 M58 74 L60 82" stroke="#D27C76" stroke-width="2.4" stroke-linecap="round"/>'),
 "snail": dict(words=["الرخويات", "حلزون", "الحلزون", "رخوي", "قوقع"], anim="wiggle", face=(76, 54, .5),
   body='<path d="M8 84 C30 82 60 84 92 80 C94 70 86 62 78 64 L70 72 L18 76 C10 78 6 82 8 84Z" fill="#F2C9A0" {OL}/><circle cx="44" cy="52" r="26" fill="#C98A55" {OL}/>'
        '<path d="M44 52 m0 -4 a4 4 0 1 1 -4 4 a9 9 0 1 1 9 9 a15 15 0 1 1 -15 -15" fill="none" stroke="#8B5A2B" stroke-width="3" stroke-linecap="round"/><path d="M82 64 L86 46 M88 66 L94 50" stroke="#3b2a1a" stroke-width="2.4" stroke-linecap="round"/>'),
 "starfish": dict(words=["شوكيات الجلد", "نجم البحر", "شوكي الجلد"], anim="sun", face=(50, 54, .62),
   body='<path d="M50 6 L61 36 L94 38 L68 58 L78 92 L50 72 L22 92 L32 58 L6 38 L39 36Z" fill="#F6A04D" {OL}/><circle cx="50" cy="22" r="2" fill="#C96A1E"/><circle cx="80" cy="42" r="2" fill="#C96A1E"/><circle cx="70" cy="80" r="2" fill="#C96A1E"/><circle cx="30" cy="80" r="2" fill="#C96A1E"/><circle cx="20" cy="42" r="2" fill="#C96A1E"/>'),
 "jellyfish": dict(words=["اللاسعات", "قنديل البحر", "لاسع", "اللاسعات"], anim="drip", face=(50, 36, .62),
   body='<path d="M28 82 Q24 70 30 60 M40 90 Q36 74 42 60 M58 90 Q64 74 58 60 M72 82 Q76 70 70 60" fill="none" stroke="#C86BD6" stroke-width="3.4" stroke-linecap="round"/>'
        '<path d="M14 54 C14 20 86 20 86 54 C76 62 24 62 14 54Z" fill="#E7A6F0" {OL}/>'),
 "seasponge": dict(words=["الإسفنجيات", "إسفنج البحر"], anim="bob", face=(50, 58, .7),
   body='<path d="M26 92 L30 26 C32 14 68 14 70 26 L74 92Z" fill="#F2C94C" {OL}/><circle cx="42" cy="40" r="4" fill="#D4A72C"/><circle cx="58" cy="46" r="5" fill="#D4A72C"/><circle cx="44" cy="76" r="4" fill="#D4A72C"/><circle cx="60" cy="80" r="3.4" fill="#D4A72C"/><ellipse cx="50" cy="24" rx="12" ry="4" fill="#B8902A"/>'),
 "crab": dict(words=["المفصليات", "سرطان البحر", "السلطعون", "مفصلي", "القشريات"], anim="wiggle", face=(50, 60, .66),
   body='<path d="M22 66 L8 76 M24 74 L12 88 M78 66 L92 76 M76 74 L88 88" stroke="#C0392B" stroke-width="4" stroke-linecap="round"/><path d="M26 54 L16 34 M74 54 L84 34" stroke="#C0392B" stroke-width="4" stroke-linecap="round"/>'
        '<path d="M8 32 C8 18 26 18 24 32 L16 30Z M92 32 C92 18 74 18 76 32 L84 30Z" fill="#E74C3C" {OL}/><ellipse cx="50" cy="64" rx="30" ry="20" fill="#E74C3C" {OL}/>'),
 "butterfly": dict(words=["الفراشة", "فراشة", "فراشات", "دورة حياة الفراشة"], anim="buzz", face=(50, 30, .45),
   body='<path d="M48 48 C30 14 6 20 10 42 C12 56 34 56 48 52Z M52 48 C70 14 94 20 90 42 C88 56 66 56 52 52Z" fill="#B9A2F0" {OL}/><path d="M48 54 C30 60 18 82 32 86 C42 88 48 70 48 58Z M52 54 C70 60 82 82 68 86 C58 88 52 70 52 58Z" fill="#F59BB8" {OL}/>'
        '<ellipse cx="50" cy="56" rx="5" ry="30" fill="#5B4A86" {OL}/><path d="M48 22 L40 8 M52 22 L60 8" stroke="#3b2a1a" stroke-width="2.4" stroke-linecap="round"/>'),
 "larva": dict(words=["اليرقة", "يرقة", "يرقات", "الشرنقة", "دودة القز"], anim="wiggle", face=(80, 56, .45),
   body='<circle cx="18" cy="66" r="11" fill="#9CD86C" {OL}/><circle cx="34" cy="62" r="12" fill="#9CD86C" {OL}/><circle cx="50" cy="60" r="12" fill="#9CD86C" {OL}/><circle cx="66" cy="60" r="12" fill="#9CD86C" {OL}/><circle cx="80" cy="56" r="13" fill="#7BC24A" {OL}/>'
        '<path d="M76 44 L72 34 M84 44 L88 34" stroke="#3b2a1a" stroke-width="2.4" stroke-linecap="round"/>'),
 "pupa": dict(words=["العذراء", "عذراء", "الخادرة"], anim="sway", face=(50, 56, .6),
   body='<path d="M50 6 L50 18" stroke="#6B4F3A" stroke-width="3"/><path d="M20 10 L80 10" stroke="#6B4F3A" stroke-width="5" stroke-linecap="round"/><path d="M50 18 C72 24 74 64 60 86 C56 94 44 94 40 86 C26 64 28 24 50 18Z" fill="#A5C66B" {OL}/>'
        '<path d="M40 40 Q50 46 60 40 M38 66 Q50 72 62 66" fill="none" stroke="#7E9E46" stroke-width="2.4"/>'),
 "tadpole": dict(words=["الشرغوف", "شرغوف", "أبو ذنيبة"], anim="wiggle", face=(64, 50, .62),
   body='<path d="M48 50 C36 40 22 60 10 50 C22 70 34 56 48 60Z" fill="#4E5D6C" {OL}/><circle cx="64" cy="54" r="22" fill="#5D6D7E" {OL}/>'),
 "mosquito": dict(words=["نواقل المرض", "ناقل المرض", "البعوض", "البعوضة", "الذباب", "الذبابة", "الحشرات الناقلة للأمراض"], anim="buzz", face=(54, 48, .5),
   body='<path d="M44 40 C30 20 12 22 14 34 C16 44 34 46 46 46Z M58 40 C70 20 88 22 86 34 C84 44 66 46 54 46Z" fill="#E3F2FD" {OL}/><ellipse cx="50" cy="62" rx="9" ry="22" fill="#7F8C99" {OL}/><circle cx="54" cy="46" r="11" fill="#9AA5B1" {OL}/>'
        '<path d="M62 50 L84 66" stroke="#3b2a1a" stroke-width="2.4" stroke-linecap="round"/><path d="M44 70 L28 92 M48 76 L40 96 M56 76 L62 96 M58 70 L74 92" stroke="#3b2a1a" stroke-width="2" stroke-linecap="round"/>'),
 "egg": dict(words=["البيضة", "بيضة", "البيض", "بيض"], anim="wobble", face=(50, 62, .7),
   body='<path d="M50 6 C76 6 88 44 86 62 C84 82 70 94 50 94 C30 94 16 82 14 62 C12 44 24 6 50 6Z" fill="#FFF4DC" {OL}/><ellipse cx="38" cy="34" rx="5" ry="9" fill="#fff"/>'),
 "camel": dict(words=["الجمل", "جمل", "الإبل", "إبل", "الناقة"], anim="bob", face=(80, 30, .45),
   body='<path d="M14 62 C14 46 22 40 30 44 C34 26 50 26 54 44 C60 34 68 40 70 50 L74 34 C74 22 92 20 92 30 L90 40 C86 46 82 52 80 60 C76 70 66 72 56 72 L24 72 C18 72 14 68 14 62Z" fill="#D9A866" {OL}/>'
        '<path d="M26 72 L24 94 M38 72 L38 94 M58 72 L58 94 M70 70 L72 94" stroke="#3b2a1a" stroke-width="5" stroke-linecap="round"/><path d="M14 58 Q6 62 8 72" fill="none" stroke="#3b2a1a" stroke-width="3" stroke-linecap="round"/>'),
 "cactus": dict(words=["الصبار", "صبار", "نبات الصبار", "نباتات الصحراء"], anim="sway", face=(50, 44, .7),
   body='<path d="M38 92 L38 22 C38 8 62 8 62 22 L62 92Z" fill="#5DB36B" {OL}/><path d="M38 58 L22 58 C14 58 14 48 14 40 L14 32 C14 26 24 26 24 32 L24 46 L38 46" fill="#5DB36B" {OL}/><path d="M62 50 L76 50 C82 50 84 44 84 38 L84 30 C84 24 74 24 74 30 L74 40 L62 40" fill="#5DB36B" {OL}/>'
        '<path d="M44 30 l-3 -2 M56 64 l3 -2 M46 76 l-3 2 M20 36 l-3 -1 M80 34 l3 -1" stroke="#2E6B38" stroke-width="2" stroke-linecap="round"/><path d="M30 94 L70 94 L66 84 L34 84Z" fill="#C98A55" {OL}/>'),
 "mushroom": dict(words=["الفطريات", "فطر", "الفطر", "فطريات", "عيش الغراب", "المحلل", "المحللات"], anim="bob", face=(50, 72, .6),
   body='<path d="M36 94 L38 56 L62 56 L64 94Z" fill="#FFF1D6" {OL}/><path d="M8 58 C8 18 92 18 92 58Z" fill="#E8574A" {OL}/><circle cx="30" cy="40" r="6" fill="#fff"/><circle cx="58" cy="32" r="7" fill="#fff"/><circle cx="76" cy="48" r="4.5" fill="#fff"/>'),
 "bacteria": dict(words=["البكتيريا", "بكتيريا", "الجراثيم", "جراثيم", "الميكروبات", "ميكروب", "البدائيات"], anim="wiggle", face=(50, 50, .7),
   body='<path d="M14 44 C14 28 86 28 86 44 L86 56 C86 72 14 72 14 56Z" fill="#9CD86C" {OL}/><path d="M86 50 C94 48 96 58 92 62 M14 50 C6 48 4 40 8 36 M30 70 L26 82 M52 72 L52 86 M70 70 L76 82" fill="none" stroke="#3b2a1a" stroke-width="2.4" stroke-linecap="round"/>'),
 "virus": dict(words=["الفيروسات", "فيروس", "الفيروس", "فيروسات"], anim="sun", face=(50, 52, .7),
   body='<g stroke="#3b2a1a" stroke-width="3" stroke-linecap="round"><path d="M50 18 L50 6 M50 82 L50 94 M18 50 L6 50 M82 50 L94 50 M27 27 L18 18 M73 27 L82 18 M27 73 L18 82 M73 73 L82 82"/></g>'
        '<circle cx="50" cy="6" r="4" fill="#E8574A"/><circle cx="50" cy="94" r="4" fill="#E8574A"/><circle cx="6" cy="50" r="4" fill="#E8574A"/><circle cx="94" cy="50" r="4" fill="#E8574A"/><circle cx="50" cy="50" r="32" fill="#B9A2F0" {OL}/>'),
 "protist": dict(words=["الطلائعيات", "طلائعي", "الأميبا", "البراميسيوم", "اليوجلينا"], anim="wiggle", face=(50, 50, .66),
   body='<path d="M20 50 C10 30 30 14 46 22 C60 8 84 18 80 36 C94 46 88 70 72 72 C70 88 46 92 38 80 C20 86 8 66 20 50Z" fill="#A8DADC" {OL}/><circle cx="62" cy="62" r="7" fill="#6FA8B3"/>'),
 # ---------- body plan ----------
 "vertebrate": dict(words=["الفقاريات", "فقاري", "العمود الفقري", "الهيكل الداخلي"], anim="bob", face=(50, 14, .4),
   body='<path d="M50 24 L50 92" stroke="#E8DCC4" stroke-width="6"/>' + "".join(f'<rect x="38" y="{26 + i * 11}" width="24" height="8" rx="3" fill="#F5EEDC" {{OL}}/>' for i in range(6))),
 "invertebrate": dict(words=["اللافقاريات", "لافقاري", "الهيكل الخارجي"], anim="wiggle", face=(50, 52, .7),
   body='<path d="M20 70 C20 40 36 24 50 24 C64 24 80 40 80 70 C70 82 30 82 20 70Z" fill="#F2A65A" {OL}/><path d="M24 54 Q50 46 76 54 M22 66 Q50 58 78 66" fill="none" stroke="#C67A2E" stroke-width="2.6"/>'),
 # ---------- what eats what ----------
 "foodchain": dict(words=["السلسلة الغذائية", "الشبكة الغذائية", "سلسلة غذائية", "شبكة غذائية", "هرم الطاقة"], anim="bob", face=(50, 64, .5),
   body='<circle cx="18" cy="30" r="12" fill="#6CC27A" {OL}/><circle cx="50" cy="30" r="12" fill="#D8B48C" {OL}/><circle cx="82" cy="30" r="12" fill="#E8853C" {OL}/>'
        '<path d="M31 30 L37 30 M63 30 L69 30" stroke="#3b2a1a" stroke-width="3" stroke-linecap="round"/><path d="M36 26 L40 30 L36 34 M68 26 L72 30 L68 34" fill="none" stroke="#3b2a1a" stroke-width="3"/>'
        '<rect x="28" y="50" width="44" height="34" rx="10" fill="#FFD25A" {OL}/>'),
 "producer": dict(words=["المنتج", "المنتجات", "المنتجون", "ذاتية التغذية", "ذاتي التغذية"], anim="sway", face=(50, 46, .7), only=["science"],
   body='<path d="M50 94 L50 54" stroke="#3E8E4C" stroke-width="5"/><path d="M50 60 C30 58 18 44 22 30 C38 30 50 42 50 60Z M50 52 C70 50 82 36 78 22 C62 22 50 34 50 52Z" fill="#6CC27A" {OL}/><circle cx="82" cy="12" r="8" fill="#FFD25A" {OL}/>'),
 "consumer": dict(words=["المستهلك", "المستهلكات", "آكلات النباتات", "آكل النباتات", "العواشب", "غير ذاتية التغذية"], anim="bob", face=(46, 44, .62), only=["science"],
   body='<path d="M34 30 Q30 8 38 6 Q44 8 40 30Z M50 30 Q52 8 60 8 Q66 12 56 32Z" fill="#EFE9E1" {OL}/><ellipse cx="50" cy="70" rx="30" ry="22" fill="#EFE9E1" {OL}/><circle cx="46" cy="44" r="18" fill="#EFE9E1" {OL}/>'
        '<path d="M70 54 C80 46 92 52 88 62 C80 66 74 62 70 58Z" fill="#6CC27A" {OL}/>'),
 "predator": dict(words=["المفترس", "المفترسات", "آكلات اللحوم", "آكل اللحوم", "اللواحم", "الأسد", "أسد"], anim="bob", face=(50, 50, .7),
   body='<circle cx="50" cy="50" r="40" fill="#C97A2E" {OL}/><circle cx="50" cy="52" r="28" fill="#F2B45A" {OL}/><path d="M30 28 L26 16 L38 24Z M70 28 L74 16 L62 24Z" fill="#F2B45A" {OL}/><ellipse cx="50" cy="64" rx="8" ry="5" fill="#8B5E3C"/>'),
 "prey": dict(words=["الفريسة", "فريسة", "الفرائس", "الغزال", "غزال"], anim="bounce", face=(52, 40, .6),
   body='<path d="M38 22 L30 6 M38 16 L28 14 M62 22 L70 6 M62 16 L72 14" stroke="#8B5E3C" stroke-width="3" stroke-linecap="round"/><ellipse cx="50" cy="72" rx="28" ry="16" fill="#D9A866" {OL}/><circle cx="52" cy="40" r="16" fill="#E6BB7E" {OL}/>'
        '<path d="M30 84 L28 96 M44 86 L44 96 M60 86 L60 96 M72 84 L74 96" stroke="#3b2a1a" stroke-width="4" stroke-linecap="round"/>'),
 "habitat": dict(words=["الموطن", "المواطن", "المواطن البرية", "المأوى", "العش", "الملجأ", "البيت الطبيعي"], anim="bob", face=(50, 64, .62), only=["science"],
   body='<path d="M10 66 C10 40 90 40 90 66 C90 88 10 88 10 66Z" fill="#B07A4A" {OL}/><path d="M16 60 Q30 54 40 62 M60 62 Q72 54 84 60 M24 76 Q50 70 76 76" fill="none" stroke="#8B5A2B" stroke-width="2.6"/>'
        '<ellipse cx="34" cy="50" rx="10" ry="12" fill="#BFE3F2" {OL}/><ellipse cx="54" cy="48" rx="10" ry="12" fill="#BFE3F2" {OL}/>'),
 "aquatic": dict(words=["المواطن المائية", "النباتات المائية", "البركة", "المياه العذبة", "الأحياء المائية"], anim="drip", face=(50, 62, .62),
   body='<ellipse cx="50" cy="66" rx="42" ry="22" fill="#7CC6F2" {OL}/><path d="M22 66 Q30 60 38 66 Q46 72 54 66 Q62 60 70 66" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>'
        '<path d="M70 50 C70 30 76 18 80 12 M78 50 C78 34 86 26 90 22" fill="none" stroke="#3E8E4C" stroke-width="3.4" stroke-linecap="round"/><ellipse cx="80" cy="12" rx="3" ry="7" fill="#8B5E3C"/><ellipse cx="26" cy="54" rx="12" ry="5" fill="#6CC27A" {OL}/>'),
 "forest": dict(words=["الغابة", "الغابات", "الغابة المطيرة", "الغابة المعتدلة", "نباتات الغابة", "إزالة الغابات"], anim="sway", face=(50, 60, .6),
   body='<path d="M22 92 L22 74 M78 92 L78 74" stroke="#8B5E3C" stroke-width="6"/><path d="M22 14 L40 46 L32 46 L44 72 L0 72 L12 46 L4 46Z" fill="#3E8E4C" {OL}/><path d="M78 14 L96 46 L88 46 L100 72 L56 72 L68 46 L60 46Z" fill="#3E8E4C" {OL}/>'
        '<path d="M50 92 L50 76" stroke="#8B5E3C" stroke-width="7"/><circle cx="50" cy="52" r="26" fill="#6CC27A" {OL}/>'),
 "desert": dict(words=["الصحراء", "الصحاري", "صحراء", "الصحراء الحارة", "الصحراء الباردة", "الكثبان الرملية", "المناخ الصحراوي"], anim="sway", face=(50, 70, .6),
   body='<circle cx="76" cy="20" r="12" fill="#FFD25A" {OL}/><path d="M0 72 C20 50 40 50 56 64 C70 52 86 52 100 62 L100 96 L0 96Z" fill="#F2C46D" {OL}/><path d="M18 84 Q30 80 42 84 M60 88 Q72 84 84 88" fill="none" stroke="#D9A44A" stroke-width="2.4"/>'),
 "polar": dict(words=["المناطق القطبية", "القطبية", "المناخ القطبي", "البطريق", "الدب القطبي"], anim="bob", face=(50, 40, .6),
   body='<path d="M0 84 L18 62 L34 72 L52 52 L70 70 L86 58 L100 74 L100 96 L0 96Z" fill="#E3F2FD" {OL}/><ellipse cx="50" cy="58" rx="20" ry="28" fill="#2F3B4C" {OL}/><ellipse cx="50" cy="62" rx="13" ry="20" fill="#fff"/><path d="M46 46 L50 52 L54 46Z" fill="#F6B73C"/><path d="M42 86 L38 92 M58 86 L62 92" stroke="#F6B73C" stroke-width="4" stroke-linecap="round"/>'),
 "hibernation": dict(words=["السبات", "البيات الشتوي", "السبات الشتوي"], anim="bob", face=(48, 60, .7),
   body='<path d="M6 92 C6 50 30 30 50 30 C70 30 94 50 94 92Z" fill="#8B6B4A" {OL}/><ellipse cx="50" cy="72" rx="26" ry="18" fill="#B08960" {OL}/><circle cx="34" cy="56" r="7" fill="#B08960" {OL}/><circle cx="64" cy="56" r="7" fill="#B08960" {OL}/>'
        '<text x="74" y="24" font-size="14" font-weight="800" fill="#7A6AC8" font-family="sans-serif">Z z</text>'),
 "migration": dict(words=["الهجرة", "هجرة الطيور", "الهجرة الموسمية"], anim="wind", face=(50, 70, .5), only=["science"],
   body='<path d="M10 30 Q18 22 26 30 Q34 22 42 30 M34 50 Q42 42 50 50 Q58 42 66 50 M58 22 Q66 14 74 22 Q82 14 90 22" fill="none" stroke="#3b2a1a" stroke-width="3.4" stroke-linecap="round"/>'
        '<path d="M14 74 C30 66 70 66 86 74" fill="none" stroke="#7CC6F2" stroke-width="4" stroke-linecap="round" stroke-dasharray="6 6"/><circle cx="50" cy="74" r="12" fill="#FFD25A" {OL}/>'),
 "camouflage": dict(words=["التمويه", "التخفي", "الحرباء", "المحاكاة"], anim="wiggle", face=(66, 46, .55),
   body='<path d="M10 62 C10 44 30 36 50 38 C66 30 90 36 90 52 C90 64 78 70 60 70 L30 72 C18 74 10 70 10 62Z" fill="#8BC34A" {OL}/><path d="M10 64 C2 68 2 80 12 80 C20 80 20 72 14 72" fill="none" stroke="#558B2F" stroke-width="3.4"/>'
        '<path d="M28 72 L24 88 M50 70 L50 88 M70 68 L74 86" stroke="#558B2F" stroke-width="4" stroke-linecap="round"/><circle cx="34" cy="54" r="5" fill="#AED581"/><circle cx="48" cy="48" r="4" fill="#689F38"/>'),
 "adaptation": dict(words=["التكيف", "التكيفات", "التكيف السلوكي", "التكيف التركيبي"], anim="bounce", face=(50, 56, .6),
   body='<circle cx="50" cy="56" r="34" fill="#A3D9A5" {OL}/><path d="M30 26 L20 8 L38 18Z" fill="#A3D9A5" {OL}/><path d="M70 26 L80 8 L62 18Z" fill="#A3D9A5" {OL}/><path d="M18 56 L4 50 M18 64 L4 70 M82 56 L96 50 M82 64 L96 70" stroke="#3b2a1a" stroke-width="3" stroke-linecap="round"/>'),
 "extinction": dict(words=["الانقراض", "الأنواع المهددة بالانقراض", "المنقرضة", "الديناصورات", "ديناصور"], anim="bob", face=(78, 30, .45),
   body='<path d="M8 84 C20 70 30 58 40 56 L60 52 C66 34 72 24 84 22 C94 22 96 34 88 38 L80 40 C76 52 74 62 66 70 L60 84" fill="#9CB89A" {OL}/><path d="M36 64 L34 94 M58 70 L60 94" stroke="#3b2a1a" stroke-width="6" stroke-linecap="round"/><path d="M40 56 L44 46 L50 54 L54 44 L60 52" fill="#7FA07C" {OL}/>'),
 "oryx": dict(words=["المها العربي", "المها", "الحياة الفطرية", "المحافظة على الحياة الفطرية", "المحميات"], anim="bob", face=(68, 40, .5),
   body='<path d="M60 26 L52 4 M70 26 L66 4" stroke="#6B4F3A" stroke-width="3" stroke-linecap="round"/><ellipse cx="44" cy="66" rx="30" ry="16" fill="#F4F0E6" {OL}/><circle cx="68" cy="40" r="13" fill="#F4F0E6" {OL}/>'
        '<path d="M60 46 L76 50" stroke="#3b2a1a" stroke-width="3"/><path d="M22 78 L20 96 M36 80 L36 96 M54 80 L54 96 M66 78 L68 96" stroke="#3b2a1a" stroke-width="4" stroke-linecap="round"/>'),
 "pinecone": dict(words=["المخروط", "المخروطيات", "مخاريط", "الصنوبر", "معراة البذور"], anim="wobble", face=(50, 56, .6), only=["science"],
   body='<path d="M50 6 C70 20 80 46 72 72 C66 88 34 88 28 72 C20 46 30 20 50 6Z" fill="#B07A4A" {OL}/><path d="M34 34 Q50 42 66 34 M28 50 Q50 58 72 50 M30 66 Q50 74 70 66" fill="none" stroke="#7A4E28" stroke-width="2.6"/><path d="M50 6 L50 0" stroke="#3E8E4C" stroke-width="3"/>'),
 "plantcell": dict(words=["الخلية النباتية", "خلية نباتية", "الجدار الخلوي"], anim="bob", face=(50, 56, .6),
   body='<rect x="10" y="12" width="80" height="76" rx="8" fill="#B7E1A1" {OL}/><rect x="18" y="20" width="64" height="60" rx="6" fill="#DCF2CF" stroke="#6CC27A" stroke-width="2"/><ellipse cx="66" cy="34" rx="9" ry="5" fill="#4CAF50"/><ellipse cx="32" cy="68" rx="8" ry="4.5" fill="#4CAF50"/><circle cx="34" cy="34" r="8" fill="#9C6FD6" {OL}/>'),
 "animalcell": dict(words=["الخلية الحيوانية", "خلية حيوانية"], anim="bob", face=(50, 58, .6),
   body='<path d="M50 8 C76 8 94 26 92 50 C90 76 72 92 48 92 C24 92 8 74 8 50 C8 26 26 8 50 8Z" fill="#F8C9C1" {OL}/><circle cx="66" cy="34" r="10" fill="#9C6FD6" {OL}/><ellipse cx="28" cy="40" rx="7" ry="4" fill="#E8853C"/><ellipse cx="72" cy="70" rx="7" ry="4" fill="#E8853C"/>'),
 "tissue": dict(words=["النسيج", "الأنسجة", "نسيج", "النسيج العضلي", "النسيج العصبي"], anim="bob", face=(50, 54, .55),
   body="".join(f'<rect x="{12 + (i % 4) * 19}" y="{14 + (i // 4) * 24}" width="18" height="22" rx="5" fill="#F8C9C1" {{OL}}/><circle cx="{21 + (i % 4) * 19}" cy="{25 + (i // 4) * 24}" r="3" fill="#9C6FD6"/>' for i in range(12))),
 "organism": dict(words=["المخلوقات الحية", "المخلوق الحي", "الكائنات الحية", "الكائن الحي", "المخلوقات", "حاجات المخلوقات الحية", "الحاجات الأساسية"], anim="bounce", face=(50, 54, .7),
   body='<circle cx="50" cy="56" r="34" fill="#FFD25A" {OL}/><path d="M50 22 L50 8" stroke="#3E8E4C" stroke-width="4"/><path d="M50 12 C58 4 70 6 72 14 C64 20 54 18 50 12Z" fill="#6CC27A" {OL}/><path d="M24 80 L14 92 M76 80 L86 92" stroke="#3b2a1a" stroke-width="4" stroke-linecap="round"/>'),
 "nonliving": dict(words=["الأشياء غير الحية", "غير الحية", "الجمادات", "العوامل غير الحية"], anim="bob", face=(50, 58, .62),
   body='<path d="M14 82 L24 40 L60 30 L88 52 L82 86Z" fill="#AEB8C4" {OL}/><path d="M30 50 L40 60 M62 46 L70 58" stroke="#8592A3" stroke-width="3" stroke-linecap="round"/>'),
 "ecosystem": dict(words=["النظام البيئي", "الأنظمة البيئية", "العوامل الحية", "الجماعة الحيوية", "المجتمع الحيوي", "البيئة"], anim="sway", face=(50, 56, .6), never=["digital"],
   body='<circle cx="50" cy="50" r="42" fill="#BFE3F2" {OL}/><path d="M8 58 C30 50 70 50 92 58 C90 80 72 92 50 92 C28 92 10 80 8 58Z" fill="#8BC34A" {OL}/><path d="M30 58 L30 40 M30 44 C22 40 20 32 24 28 C32 30 34 38 30 44" fill="#3E8E4C" stroke="#3E8E4C" stroke-width="3"/><circle cx="72" cy="28" r="8" fill="#FFD25A" {OL}/>'),
 "competition": dict(words=["التنافس", "المنافسة"], anim="wobble", face=(50, 70, .5), only=["science"],
   body='<circle cx="24" cy="40" r="16" fill="#E6BB7E" {OL}/><circle cx="76" cy="40" r="16" fill="#C9A27A" {OL}/><path d="M42 40 L58 40" stroke="#3b2a1a" stroke-width="3"/><circle cx="50" cy="26" r="8" fill="#6CC27A" {OL}/><rect x="30" y="62" width="40" height="26" rx="8" fill="#FFD25A" {OL}/>'),
 "classification": dict(words=["التصنيف", "تصنيف المخلوقات الحية", "المملكة", "الممالك", "الشعبة", "الطائفة", "الرتبة", "الفصيلة", "الجنس", "النوع", "الأنواع", "المفتاح الثنائي"], anim="bob", face=(50, 30, .45), only=["science"],
   body='<rect x="34" y="10" width="32" height="22" rx="6" fill="#FFD25A" {OL}/><path d="M50 32 L50 44 M24 44 L76 44 M24 44 L24 54 M76 44 L76 54" stroke="#3b2a1a" stroke-width="3" fill="none"/>'
        '<rect x="8" y="54" width="32" height="20" rx="6" fill="#6CC27A" {OL}/><rect x="60" y="54" width="32" height="20" rx="6" fill="#7CC6F2" {OL}/><path d="M16 74 L16 84 M32 74 L32 84 M68 74 L68 84 M84 74 L84 84" stroke="#3b2a1a" stroke-width="3"/>'),
 "lifecycle": dict(words=["دورة الحياة", "دورة حياة", "دورة حياة النبات", "دورة حياة الضفدع", "دورة حياة الحيوان", "التحول الكامل", "التحول الناقص", "التحول"], anim="sun", face=(50, 50, .6), only=["science"],
   body='<circle cx="50" cy="50" r="36" fill="none" stroke="#9CCFD8" stroke-width="6"/><path d="M86 50 L80 42 L92 42Z M14 50 L20 58 L8 58Z" fill="#3E8E4C"/><circle cx="50" cy="14" r="9" fill="#FFF4DC" {OL}/><circle cx="86" cy="50" r="9" fill="#9CD86C" {OL}/><circle cx="50" cy="86" r="9" fill="#A5C66B" {OL}/><circle cx="14" cy="50" r="9" fill="#B9A2F0" {OL}/><circle cx="50" cy="50" r="16" fill="#FFD25A" {OL}/>'),
 "nymph": dict(words=["الحورية", "حورية"], anim="wiggle", face=(66, 52, .5),
   body='<ellipse cx="44" cy="58" rx="30" ry="16" fill="#A1887F" {OL}/><circle cx="70" cy="52" r="13" fill="#A1887F" {OL}/><path d="M24 68 L16 82 M40 72 L36 86 M56 72 L60 86" stroke="#3b2a1a" stroke-width="3" stroke-linecap="round"/><path d="M76 42 L86 28 M68 40 L72 26" stroke="#3b2a1a" stroke-width="2.4" stroke-linecap="round"/>'),
 "beaver": dict(words=["سد القندس", "القندس", "قندس"], anim="bob", face=(50, 38, .55),
   body='<path d="M4 92 L96 92 L88 78 L12 78Z" fill="#8B5E3C" {OL}/><path d="M16 78 L22 66 L78 66 L84 78" fill="#A0724A" {OL}/><ellipse cx="50" cy="50" rx="22" ry="20" fill="#9B6B43" {OL}/><circle cx="50" cy="34" r="15" fill="#A97C50" {OL}/><rect x="45" y="42" width="10" height="7" rx="2" fill="#fff" {OL}/>'),
 "pollution": dict(words=["التلوث", "تلوث", "تلوث الهواء", "تلوث الماء", "تلوث التربة", "الملوثات"], anim="bob", face=(50, 72, .55),
   body='<rect x="16" y="50" width="22" height="44" fill="#8592A3" {OL}/><rect x="44" y="40" width="20" height="54" fill="#8592A3" {OL}/><path d="M24 50 C20 38 30 34 26 24 C34 28 40 20 36 12 M52 40 C48 28 58 24 54 14" fill="none" stroke="#5A5A5A" stroke-width="5" stroke-linecap="round"/><rect x="66" y="66" width="28" height="28" rx="6" fill="#AEB8C4" {OL}/>'),
 "recycle": dict(words=["إعادة التدوير", "التدوير", "إعادة الاستعمال", "إعادة الاستخدام", "التقليل", "النفايات", "القمامة"], anim="sun", face=(50, 52, .55),
   body='<path d="M50 10 L64 34 L56 34 L56 44 L44 44 L44 34 L36 34Z" fill="#4CAF50" {OL}/><path d="M86 74 L58 74 L62 66 L54 60 L60 50 L68 56 L72 48Z" fill="#4CAF50" {OL}/><path d="M14 74 L28 50 L32 58 L42 54 L46 66 L36 68 L40 76Z" fill="#4CAF50" {OL}/><circle cx="50" cy="56" r="14" fill="#C8E6C9" {OL}/>'),
 "naturalresources": dict(words=["الموارد الطبيعية", "الموارد", "الموارد المتجددة", "الموارد غير المتجددة", "المحافظة على الموارد"], anim="bob", face=(28, 76, .48),
   body='<path d="M30 54 L30 30" stroke="#8B5E3C" stroke-width="5"/><circle cx="30" cy="26" r="16" fill="#6CC27A" {OL}/><path d="M62 52 C62 52 50 66 50 74 C50 82 56 86 62 86 C68 86 74 82 74 74 C74 66 62 52 62 52Z" fill="#7CC6F2" {OL}/><path d="M78 40 L88 26 L92 44Z" fill="#AEB8C4" {OL}/><rect x="14" y="60" width="28" height="30" rx="8" fill="#FFD25A" {OL}/>'),
}

# other names of the drawings the page already had (one concept = one drawing) — for the sciences only
ALIAS_ONLY = ("science",)
ALIASES = {
 "الجذور": "🫚", "الأوراق": "🍃", "الورقة النباتية": "🍃", "الأزهار": "🌸", "الثمار": "🍎", "البذور": "🌰", "البادرة": "🌱", "الإنبات": "🌱",
 "النبات": "🪴", "النباتات": "🪴", "النباتات المنزلية": "🪴", "الأشجار": "🌳", "الشجرة": "🌳", "النباتات الزهرية": "🌸", "مغطاة البذور": "🌸",
 "صنع النبات غذاءه": "🍃", "صنع الغذاء": "🍃", "البناء الضوئي": "🍃", "التمثيل الضوئي": "🍃", "عملية البناء الضوئي": "🍃",
 "النحلة": "🐝", "النحل": "🐝", "التلقيح": "🐝", "الماء": "💧", "المياه": "💧", "الهواء": "💨", "التربة": "🟫", "الدبال": "🟫", "الطين": "🟫", "الطمي": "🟫",
 "الشمس": "☀️", "ضوء الشمس": "☀️", "الخلية": "🦠", "الخلايا": "🦠", "القلب": "❤️", "الحيوانات": "🐾", "الحيوان": "🐾", "المحيط": "🌊", "البحر": "🌊", "البحار": "🌊",
 "المحيطات": "🌊", "المياه المالحة": "🌊", "الحمض النووي": "sec:dna", "الكروموسومات": "sec:chromosome", "الجينات": "sec:gene", "الجين": "sec:gene",
 "النواة": "sec:nucleus", "الميتوكندريا": "sec:mito", "البلاستيدات الخضراء": "sec:chloroplast", "الفجوة العصارية": "sec:vacuole", "الغشاء البلازمي": "sec:membrane",
 "الغشاء الخلوي": "sec:membrane", "السيتوبلازم": "sec:cytoplasm", "الثعلب": "🦊", "البومة": "🦉", "النهر": "hist:river", "الأنهار": "hist:river", "حبة اللقاح": "🐝", "حبوب اللقاح": "🐝", "الكتلة الحشوية": "sci.snail", "الملف اللولبي": "mat.generator",
}
