/* ======================= 🎬 THE LESSON'S STORY · batch 38 (Hareth) =======================
   «الحكاية كلهم بطلعوا مع بعض… لو واحد بطلع، بقول ناقصني هيك، فبطلع الثاني… بتعرّفوا على بعض واحد واحد»
   + «كل مرحلة دراسية إلها مشهد مناسب إلها… الثانوي مشهد أكبر، مش زي الأطفال».
   ① ONE ORDER for every lesson of every graph (stPlan — from the graph's «needs» only, no AI, no word written by hand):
      the hero (the one at the end of the longest «needs» chain) comes ALONE → it says what it misses → the one it needs comes and gives →
      that one says what IT misses → … (like «اللفتة العملاقة»); a second need of the same one: «وكمان…»; then another thread of the lesson
      («وبمكان ثاني…»); then the ones that have no link at all (each tells who it is). Then the twist (the one everybody needs disappears) and the end.
   ② FOUR WAYS TO SHOW IT, one for every age (Hareth chose them, batch 38):
      🌈 kids   (1–4)  : a tale «كان يا ما كان» — the characters in the lesson's place: they walk in, hop, give a glowing ball;
      🧭 junior (5–7)  : a team of explorers — the same characters, calmer (small steps), «انضمّ للفريق»;
      🔬 teen   (8–9)  : an investigation board — each one is a card pinned on a cork board (القضية · دليل ١ · دليل ٢…), a red string from it
                         to what it depends on, a magnifier that goes to the card we are looking at;
      📐 senior (10–12): a documentary diagram that builds itself — a calm dark board, the question on top, one node + one thin arrow at a time,
                         the camera moves to the new part, the rest dims; at the end the whole map + the conclusion.
   The four share one video player (stShell + stPlay in story.js): ▶/⏸, the timeline with chapters, the subtitles, the sounds. */
const ST_PLACE={garden:"حديقة خضرا",classroom:"صف الأرقام",space:"الفضاء الواسع",lab:"مختبر صغير",map:"خريطة كبيرة",desert:"أرض قديمة",notebook:"دفتر ملوّن",room:"غرفة دافية",
  sea:"قاع البحر",city:"مدينة كبيرة",kitchen:"مطبخ صغير",forest:"غابة كبيرة",
  underground:"عالم تحت الأرض",cell:"خلية كبيرة",atoms:"عالم الذرات",sky:"سما ماطرة",motion:"طريق طويل",numbers:"عالم الأرقام",library:"مكتبة قديمة",
  ancient:"أرض قديمة",machine:"ورشة طاقة"};   /* batch 35: the story happens in the lesson's PLACE (places.js) · 🆕 batch 39: + the little worlds (zones.js) */
const stV=(id,m,f)=>stFem(exName(id))?f:m;
const stQ=id=>`«${exName(id)}»`;
const stMoral=c=>`${stW()?stW().end:"كل واحد بيحتاج اللي قبله"}: ${c}.`;
const ST_NTH=["الأول","الثاني","الثالث","الرابع","الخامس","السادس","السابع","الثامن","التاسع"];
const stAr=n=>String(n).replace(/\d/g,x=>"٠١٢٣٤٥٦٧٨٩"[x]);
const stSubj=()=>(graph()||{}).subject;
const stMean=(s,id)=>String(s.meaning[id]||"").replace(/^[•📌]\s*/u,"").trim();   /* what it is, in one short line (no leading bullet) */

/* ---------- 🆕 batch 39 (Hareth: «إذا اختفى… نخلّي إشي يخطفها، أرنب يمسكها ويخطفها، بعدين بترجع» + «لازم توصل فكرة شو بيصير لو اختفى»)
   THE THIEF of the twist (the little ones and the explorers): a mischievous character of the lesson's PLACE (never a concept, so it never
   confuses the lesson) runs in, grabs the one everybody needs and runs away — then the story STAYS on what happens without it (the others
   turn grey and sad, the line says it, they miss it) — somebody calls «we need it!» — the thief brings it back, says sorry, and runs off.
   Drawn facing right, around (0,0), about 60 units tall; the cartoon turns it to where it runs. ---------- */
const TH_O='stroke="#3b2a1a" stroke-width="2.2" stroke-linejoin="round"';
const TH_EYE=(x,y)=>`<circle cx="${x}" cy="${y}" r="3.2" fill="#fff" stroke="#3b2a1a" stroke-width="1.2"/><circle cx="${x+0.9}" cy="${y+0.3}" r="1.7" fill="#2B1D12"/><circle cx="${x+1.5}" cy="${y-0.5}" r=".6" fill="#fff"/>`;
const TH_LEGS=(c)=>`<path d="M-9 18 l-3 9 M-1 19 l0 9 M7 19 l1 9 M14 17 l4 8" stroke="${c||"#3b2a1a"}" stroke-width="3.4" stroke-linecap="round"/>`;
const ST_THIEF={
  rabbit:{n:"أرنب",f:0,svg:`<path d="M5 -20 Q1 -42 8 -44 Q15 -42 12 -19Z" fill="#EFE9E1" ${TH_O}/><path d="M7 -22 Q6 -37 9 -39 Q11 -36 10 -21Z" fill="#F4B6C2"/><path d="M14 -19 Q16 -40 23 -40 Q27 -35 19 -17Z" fill="#EFE9E1" ${TH_O}/><ellipse cx="-4" cy="9" rx="18" ry="13" fill="#EFE9E1" ${TH_O}/><circle cx="-21" cy="5" r="5.5" fill="#fff" ${TH_O}/>${TH_LEGS("#8C7B6B")}<circle cx="11" cy="-8" r="12.5" fill="#F6F1EA" ${TH_O}/>${TH_EYE(15,-11)}<ellipse cx="23" cy="-5" rx="2.4" ry="1.8" fill="#E57A8C"/><path d="M19 -1 q2 2 4 0" fill="none" stroke="#3b2a1a" stroke-width="1.4" stroke-linecap="round"/><circle cx="8" cy="-3" r="2.6" fill="#F4B6C2" opacity=".7"/>`},
  cat:{n:"قطة",f:1,svg:`<path d="M-20 4 Q-36 -2 -32 -18 Q-29 -24 -26 -18 Q-29 -6 -18 -1Z" fill="#F2A65A" ${TH_O}/><ellipse cx="-3" cy="9" rx="18" ry="12" fill="#F2A65A" ${TH_O}/>${TH_LEGS("#B86E2E")}<path d="M3 -18 L5 -31 L13 -21Z M15 -21 L23 -31 L24 -17Z" fill="#F2A65A" ${TH_O}/><circle cx="13" cy="-9" r="12.5" fill="#F7B56E" ${TH_O}/>${TH_EYE(9,-11)}${TH_EYE(18,-11)}<path d="M13 -5 l-2 -2 h4z" fill="#D4566B"/><path d="M13 -4 q-2 3 -4 1 M13 -4 q2 3 4 1 M3 -5 h-8 M3 -3 l-8 2 M23 -5 h8 M23 -3 l8 2" fill="none" stroke="#3b2a1a" stroke-width="1.2" stroke-linecap="round"/>`},
  ufo:{n:"صحن فضائي",f:0,svg:`<path d="M-8 -10 Q0 -30 10 -10Z" fill="#BFE9FF" ${TH_O}/>${TH_EYE(-2,-17)}${TH_EYE(5,-17)}<ellipse cx="1" cy="-6" rx="27" ry="9" fill="#9AA7B8" ${TH_O}/><ellipse cx="1" cy="-8" rx="17" ry="4" fill="#C6D0DC"/><circle cx="-16" cy="-4" r="2.4" fill="#FFD84D"/><circle cx="1" cy="-1" r="2.4" fill="#7BD389"/><circle cx="18" cy="-4" r="2.4" fill="#FF8FB1"/><path d="M-8 4 L-16 26 H18 L10 4Z" fill="#FFF3B0" opacity=".45"/>`},
  robot:{n:"روبوت",f:0,svg:`<path d="M2 -34 V-26" stroke="#3b2a1a" stroke-width="2.4"/><circle cx="2" cy="-36" r="3.2" fill="#FF6B6B" ${TH_O}/><rect x="-11" y="-26" width="26" height="18" rx="6" fill="#B9C4D0" ${TH_O}/>${TH_EYE(-3,-17)}${TH_EYE(7,-17)}<rect x="-15" y="-6" width="34" height="22" rx="6" fill="#8FA3B8" ${TH_O}/><rect x="-7" y="0" width="18" height="8" rx="3" fill="#6CB8FF"/><circle cx="-8" cy="21" r="6" fill="#4A5563" ${TH_O}/><circle cx="12" cy="21" r="6" fill="#4A5563" ${TH_O}/>`},
  octopus:{n:"أخطبوط",f:0,svg:`${[-16,-8,0,8,16].map((x,i)=>`<path d="M${x} 6 q${i%2?5:-5} 10 ${i%2?-2:2} 20" fill="none" stroke="#C86BD6" stroke-width="5.5" stroke-linecap="round"/>`).join("")}<ellipse cx="0" cy="-6" rx="19" ry="17" fill="#D884E3" ${TH_O}/>${TH_EYE(-6,-8)}${TH_EYE(6,-8)}<path d="M-4 1 q4 3 8 0" fill="none" stroke="#3b2a1a" stroke-width="1.5" stroke-linecap="round"/><circle cx="-12" cy="-16" r="2.4" fill="#F2B6F8"/>`},
  pigeon:{n:"حمامة",f:1,svg:`<path d="M-22 4 L-34 0 L-30 10Z" fill="#8C96A3" ${TH_O}/><ellipse cx="-4" cy="5" rx="19" ry="12" fill="#AEB7C2" ${TH_O}/><path d="M-12 0 Q-2 -10 8 2" fill="#C7CED7" ${TH_O}/><circle cx="12" cy="-9" r="9" fill="#9AA5B1" ${TH_O}/>${TH_EYE(14,-11)}<path d="M20 -9 L28 -7 L20 -5Z" fill="#F5A623" ${TH_O}/><path d="M-6 16 l-2 9 M2 16 l1 9" stroke="#E07A5F" stroke-width="2.8" stroke-linecap="round"/>`},
  crow:{n:"غراب",f:0,svg:`<path d="M-22 2 L-36 -2 L-32 10Z" fill="#2E3440" ${TH_O}/><ellipse cx="-4" cy="5" rx="19" ry="12" fill="#3B4252" ${TH_O}/><path d="M-14 -1 Q-3 -12 9 1" fill="#4C566A" ${TH_O}/><circle cx="12" cy="-9" r="9" fill="#3B4252" ${TH_O}/>${TH_EYE(14,-11)}<path d="M20 -10 L31 -7 L20 -4Z" fill="#E8B04A" ${TH_O}/><path d="M-6 16 l-2 9 M2 16 l1 9" stroke="#E8B04A" stroke-width="2.8" stroke-linecap="round"/>`},
  fox:{n:"ثعلب",f:0,svg:`<path d="M-20 4 Q-40 -4 -34 -16 Q-26 -14 -18 -2Z" fill="#E8833A" ${TH_O}/><path d="M-34 -16 Q-30 -10 -27 -12 Q-31 -16 -34 -16Z" fill="#fff"/><ellipse cx="-3" cy="9" rx="18" ry="11" fill="#E8833A" ${TH_O}/>${TH_LEGS("#7A3E12")}<path d="M2 -16 L4 -34 L13 -21Z M16 -21 L26 -33 L24 -14Z" fill="#E8833A" ${TH_O}/><path d="M2 -14 Q12 -26 26 -12 L32 -6 Q22 4 12 2 Q2 0 2 -14Z" fill="#F29A52" ${TH_O}/><path d="M18 -3 Q26 -2 32 -6 Q24 4 16 2Z" fill="#fff"/>${TH_EYE(13,-12)}<circle cx="32" cy="-6" r="2.2" fill="#2B1D12"/>`},
  plane:{n:"طيارة ورق",f:1,svg:`<path d="M-26 -2 L28 -14 L-8 10Z" fill="#FFFFFF" ${TH_O}/><path d="M-8 10 L28 -14 L-2 -1Z" fill="#E6EEF7" ${TH_O}/><path d="M-26 -2 L-2 -1 L-8 10Z" fill="#D6E2EF" ${TH_O}/>${TH_EYE(4,-6)}${TH_EYE(12,-8)}<path d="M-30 6 h-8 M-30 12 h-12" stroke="#9AB3CC" stroke-width="2" stroke-linecap="round" stroke-dasharray="3 3"/>`}};
const ST_THIEF_OF={garden:"rabbit",forest:"fox",kitchen:"cat",room:"cat",space:"ufo",lab:"robot",sea:"octopus",city:"pigeon",map:"crow",desert:"fox",classroom:"plane",notebook:"plane",
  underground:"rabbit",cell:"robot",atoms:"ufo",sky:"crow",motion:"fox",numbers:"plane",library:"plane",ancient:"fox",machine:"robot"};   /* a learned place (a recipe): the rabbit */
Object.entries({rabbit:"الأرنب",cat:"القطة",ufo:"الصحن الفضائي",robot:"الروبوت",octopus:"الأخطبوط",pigeon:"الحمامة",crow:"الغراب",fox:"الثعلب",plane:"طيارة الورق"}).forEach(([k,v])=>{ST_THIEF[k].al=v;});   /* 🆕 batch 40: «فرجعت طيارة الورق» (not «الطيارة ورق») */
const stThief=()=>ST_THIEF[ST_THIEF_OF[placeNow()]||"rabbit"];
/* 🆕 batch 40 (Hareth: «الأرنب شفته بيخطف التربة، بس واقعياً… بيقدر يمسك التفاح، ما بيقدر يمسك التربة… لازم يكون في منطق»):
   the one everybody needs still vanishes (that is the lesson), but the WAY it vanishes fits what it is:
   · a thing you can hold (a fruit, a seed, a battery, a number card…) → the thief of the place grabs it and runs (as before);
   · water / a liquid → a thirsty SPONGE soaks it all up (and squeezes it back);   · light / the sun → a big CLOUD covers it (and moves away);
   · soil / sand → a MOLE pulls it down under the ground (and pushes it back up);   · air / a gas → a BALLOON sucks it all in (and lets it out);
   · something nobody can carry (a force, energy, a process, a river, a planet, a people…) → «💭 imagine there were no …» (a thought cloud).
   Read from the concept's NAME (any graph, any subject), and from its picture (water drop, sun, air, soil). */
const ST_AGENT={
  sponge:{n:"إسفنجة",f:1,svg:`<rect x="-19" y="-30" width="38" height="9" rx="3" fill="#5DBB63" ${TH_O}/><rect x="-19" y="-23" width="38" height="44" rx="7" fill="#FFD84D" ${TH_O}/><circle cx="-11" cy="-15" r="2.6" fill="#E5B52A"/><circle cx="12" cy="-13" r="3.2" fill="#E5B52A"/><circle cx="-12" cy="12" r="3" fill="#E5B52A"/><circle cx="11" cy="13" r="2.2" fill="#E5B52A"/><circle cx="0" cy="15" r="1.8" fill="#E5B52A"/>${TH_EYE(-6,-6)}${TH_EYE(6,-6)}<path d="M-5 4 q5 5 10 0" fill="none" stroke="#3b2a1a" stroke-width="1.8" stroke-linecap="round"/><path d="M-9 21 v8 M9 21 v8" stroke="#3b2a1a" stroke-width="3.4" stroke-linecap="round"/>`},
  cloud:{n:"غيمة",f:1,svg:`<path d="M-30 12 Q-42 12 -41 1 Q-40 -11 -28 -11 Q-26 -26 -10 -25 Q0 -36 13 -27 Q30 -30 32 -13 Q45 -11 43 1 Q42 12 30 12Z" fill="#AEB8C4" ${TH_O}/><path d="M-26 -9 Q-22 -18 -12 -18" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round" opacity=".7"/>${TH_EYE(-7,-4)}${TH_EYE(8,-4)}<path d="M-3 5 q3 -3 6 0" fill="none" stroke="#3b2a1a" stroke-width="1.8" stroke-linecap="round"/>`},
  mole:{n:"خُلد",f:0,svg:`<path d="M-32 28 Q0 6 32 28Z" fill="#8B5E3C" ${TH_O}/><ellipse cx="0" cy="4" rx="17" ry="20" fill="#6B4F3A" ${TH_O}/><ellipse cx="-2" cy="11" rx="10" ry="11" fill="#A68A6D"/><path d="M-3 -10 q2.5 -2.5 5 0 M5 -10 q2.5 -2.5 5 0" fill="none" stroke="#1E140C" stroke-width="1.8" stroke-linecap="round"/><ellipse cx="14" cy="-4" rx="5.5" ry="4" fill="#F48FB1" ${TH_O}/><ellipse cx="13" cy="12" rx="6" ry="4.5" fill="#F4C7A1" ${TH_O}/><path d="M18 9 l5 -2 M18 12 l6 0 M18 15 l5 2" stroke="#3b2a1a" stroke-width="1.6" stroke-linecap="round"/>`},
  balloon:{n:"بالون",f:0,svg:`<path d="M0 19 q-5 8 1 14 q5 6 -1 12" fill="none" stroke="#3b2a1a" stroke-width="1.6"/><path d="M0 18 C-23 14 -25 -27 0 -29 C25 -27 23 14 0 18Z" fill="#FF6B6B" ${TH_O}/><path d="M-3 18 L3 18 L0 23Z" fill="#E04848" ${TH_O}/><ellipse cx="-9" cy="-15" rx="4" ry="7.5" fill="#fff" opacity=".45"/>${TH_EYE(-5,-6)}${TH_EYE(6,-6)}<path d="M-4 4 q4 4 8 0" fill="none" stroke="#3b2a1a" stroke-width="1.8" stroke-linecap="round"/>`},
  think:{n:"",f:0,svg:`<circle cx="-28" cy="30" r="3.2" fill="#fff" ${TH_O}/><circle cx="-20" cy="20" r="5.2" fill="#fff" ${TH_O}/><path d="M-26 6 Q-37 4 -35 -7 Q-34 -19 -20 -17 Q-16 -31 0 -29 Q14 -35 22 -23 Q37 -23 35 -8 Q41 4 28 8 Q20 16 6 12 Q-4 18 -14 12 Q-24 14 -26 6Z" fill="#FFFFFF" ${TH_O}/><text x="0" y="0" text-anchor="middle" font-size="19" font-weight="800" fill="#7A6AC8">؟</text>`}};
const ST_WAY_WORDS=[   /* checked in this order: nobody can carry a process, a force or a river even if its name has «ماء» or «ضوء» in it */
  ["think",["قوة","قوى","جاذبية","طاقة","حركة","سرعة","تسارع","حرارة","صوت","زمن","وقت","احتكاك","كهرباء","كهربائية","مغناطيسية","ضغط","كتلة","وزن","موجة","موجات","إزاحة","مسافة","موقع",
    "تلقيح","إنبات","انتشار","تبخر","تكاثف","بناء","تمثيل","تنفس","هضم","نمو","تكاثر","انتقال","تفاعل","ذوبان","انصهار","تجمد","احتراق","دورة","تخمير","تجارة","زراعة","هجرة","تكيف","تحلل","إنتاج",
    "نهر","نيل","بحر","بحار","محيط","محيطات","جبل","جبال","هرم","أهرام","أهرامات","كوكب","كواكب","أرض","قارة","قارات","مدينة","دولة","وطن","غابة","صحراء","شجرة","أشجار","سفينة","سفن","مجرة","نجم","نجوم","قمر","مناخ","طقس","بيئة","نظام",
    "فراعنة","فرعون","ملك","ملوك","شعب","إنسان","مجتمع","حضارة","تاريخ","حيوان","حيوانات","مخلوق","مخلوقات","كائن","كائنات","سكان","جيش",
    "عدوى","مرض","أمراض","مناعة","جراثيم","جرثومة","بكتيريا","فيروس","فيروسات","ميكروب","ميكروبات","وقاية","صحة","تغذية","عادات","نظافة","تطعيم","تلوث","انقراض","تعاون","حقوق","أمن","سلامة","تجوية","تعرية","ترسيب","صهارة"]],   /* 🆕 batch 40: + what nobody can carry in health, ecology, society */
  ["sponge",["ماء","مياه","مي","سائل","سوائل","عصير","حليب"]],
  ["cloud",["ضوء","شمس","أشعة","نور"]],
  ["balloon",["هواء","أكسجين","غاز","غازات","بخار"]],
  ["mole",["تربة","رمل","رمال","طين"]]];
const ST_WAY_OF_ART={"💧":"sponge","☀️":"cloud","💨":"balloon","🟫":"mole"};
const stWay=b=>{const toks=String(exName(b)).replace(/[«»،,.:؛()]/g," ").split(/\s+/).filter(Boolean).map(w=>{for(const p of ["وال","بال","فال","كال","لل","ال"])if(w.startsWith(p)&&w.length>p.length+1)return w.slice(p.length);return w;});
  const has=k=>toks.some(t=>t===k||(k.length>=3&&t.startsWith(k))||["ة","ات","ان","ين","ي","ية"].some(e=>t===k+e));
  for(const [way,words] of ST_WAY_WORDS)if(words.some(has))return way;
  return ST_WAY_OF_ART[icBase(iconOf(b))]||"carry";};
/* «give it back!» said to the thief: to a «she» it is «رجّعيه» (not «رجّعه») */
const stGiveBack=(th,b)=>th.f?stV(b,"رجّعيه","رجّعيها"):stV(b,"رجّعه","رجّعها");
/* «we need it!», the subject's way */
const stNeedIt=b=>{const k=stSubj();return k==="math"?`إحنا مبنيين ${stV(b,"عليه","عليها")}`:k==="history"?`إحنا صرنا ${stV(b,"بسببه","بسببها")}`:`إحنا ${stV(b,"بنحتاجه","بنحتاجها")}`;};

/* ---------- ① the order: who comes, who calls whom (any graph) ---------- */
function stPlan(s){const ids=s.guests.concat(s.ids),inL=new Set(s.ids),pre={},nxt={};
  ids.forEach(i=>{pre[i]=[];nxt[i]=[];});
  s.edges.forEach(([a,b])=>{if(pre[b]&&nxt[a]&&a!==b){pre[b].push(a);nxt[a].push(b);}});   /* [a,b]: b needs a */
  const dm={},depth=(id,seen)=>{if(dm[id]!=null)return dm[id];seen=seen||new Set();if(seen.has(id))return 0;seen.add(id);let m=0;pre[id].forEach(p=>{m=Math.max(m,1+depth(p,seen));});seen.delete(id);return dm[id]=m;};
  const linked=i=>pre[i].length>0||nxt[i].length>0;
  /* who goes first: the longest chain of needs behind it · then a concept of the lesson before a guest · then the lesson's order */
  const rank=(x,y)=>depth(y)-depth(x)||(inL.has(y)?1:0)-(inL.has(x)?1:0)||ids.indexOf(x)-ids.indexOf(y);
  const hero=ids.filter(linked).sort(rank)[0]||s.ids[0]||ids[0];
  const chain=[hero];if(linked(hero)){let x=hero;while(pre[x].length){x=pre[x].slice().sort(rank)[0];if(chain.includes(x))break;chain.unshift(x);}}   /* base → … → hero */
  const on=new Set([hero]),done=new Set(),beats=[];
  /* x is on stage: each thing it needs, the deepest first — a new one is CALLED (and then calls its own), one already there just helps (a link);
     the ones with nothing behind them (soil, water…) that x needs come TOGETHER (up to 3), so the tale never drags */
  const bring=(x,lead)=>{let asked=0;const ask=()=>{beats.push({t:"ask",x,again:asked>0,lead:!!lead&&!asked});asked++;},leaves=[];
    pre[x].slice().sort(rank).forEach(p=>{const key=p+">"+x;if(done.has(key))return;
      if(on.has(p)){done.add(key);beats.push({t:"link",a:p,b:x});return;}
      if(!pre[p].length){leaves.push(p);return;}
      done.add(key);ask();on.add(p);beats.push({t:"call",as:[p],b:x});bring(p,false);});
    const fresh=leaves.filter(p=>{const key=p+">"+x;if(done.has(key))return false;if(on.has(p)){done.add(key);beats.push({t:"link",a:p,b:x});return false;}return true;});
    for(let i=0;i<fresh.length;i+=3){const g=fresh.slice(i,i+3);g.forEach(p=>{done.add(p+">"+x);on.add(p);});ask();beats.push({t:"call",as:g,b:x});}};
  if(linked(hero))bring(hero,true);
  for(;;){const rest=ids.filter(i=>!on.has(i)&&linked(i));if(!rest.length)break;const h=rest.sort(rank)[0];on.add(h);beats.push({t:"other",id:h});bring(h,true);}   /* another thread of the lesson */
  ids.filter(i=>!on.has(i)).forEach(i=>{on.add(i);beats.push({t:"lone",id:i});});                                                                         /* no link at all */
  /* the twist: the one that the most others need, and everyone who needs it (directly or through others) */
  const reach=a=>{const out=[],seen=new Set([a]),q=[a];while(q.length){const x=q.shift();nxt[x].forEach(n=>{if(!seen.has(n)){seen.add(n);out.push(n);q.push(n);}});}return out;};
  const base=ids.slice().sort((x,y)=>reach(y).length-reach(x).length)[0],hurt=base?reach(base):[];
  return {hero,chain:chain.length>=2?chain:[],beats,base,hurt};}

/* ---------- the words: the subject's way («بيحتاج» · maths «مبني على» · history «بسبب») and the age's way ---------- */
const stMiss=(x,again)=>{const k=stSubj();
  if(k==="math")return again?`${stV(x,"مبني","مبنية")} على إشي ثاني كمان`:`${stV(x,"مبني","مبنية")} على إشي`;
  if(k==="history")return again?`${stV(x,"إله","إلها")} سبب ثاني كمان`:`${stV(x,"صار","صارت")} بسبب إشي`;
  return again?`${stV(x,"ناقصه","ناقصها")} إشي ثاني كمان`:`${stV(x,"ناقصه","ناقصها")} إشي`;};
/* what the character itself says (its bubble) when it misses something · kid = the little ones (a few emoji) */
const stMe=(x,again,lead,kid)=>{const k=stSubj(),e=s=>kid?s:"";
  if(k==="math")return again?`وكمان ${stV(x,"مبني","مبنية")} على إشي ثاني!`:lead?`على شو أنا ${stV(x,"مبني","مبنية")}؟${e(" 🤔")}`:`وأنا كمان ${stV(x,"مبني","مبنية")} على إشي!${e(" 🤔")}`;
  if(k==="history")return again?"وفي سبب ثاني كمان!":lead?`ليش صرت؟${e(" 🤔")}`:`وأنا كمان صرت بسبب إشي!${e(" 🤔")}`;
  if(!kid)return again?"ولسا ناقصني حدا!":lead?"لازم ألاقي اللي بيساعدني!":"وأنا كمان بدي حدا يساعدني!";
  return again?"وكمان ناقصني إشي ثاني!":lead?"مين بيساعدني؟ 🥺":"وأنا كمان ناقصني إشي! 🥺";};
const stHello=(a,b,kid)=>{const k=stSubj();
  if(k==="math")return `أنا ${stQ(a)}! ${stV(b,"إنت مبني","إنتِ مبنية")} عليّ${kid?" 💪":""}`;
  if(k==="history")return `أنا ${stQ(a)}! أنا السبب${kid?" ✋":""}`;
  return kid?`أنا ${stQ(a)}! أنا بساعدك 💪`:`أنا ${stQ(a)}، أنا معك!`;};
/* the investigation / the diagram: the question about one of them */
const stCase=h=>stW()?stW().askIn(stQ(h),stFem(exName(h))):`على شو ${stV(h,"بيعتمد","بتعتمد")} ${stQ(h)}؟`;
const stAskS=x=>{const k=stSubj();return k==="math"?`على شو ${stV(x,"مبني","مبنية")}؟`:k==="history"?`ليش ${stV(x,"صار","صارت")}؟`:`على شو ${stV(x,"بيعتمد","بتعتمد")}؟`;};
const stAlone=x=>{const k=stSubj();return k==="math"?stV(x,"مش مبني من فراغ","مش مبنية من فراغ"):k==="history"?stV(x,"ما صار من فراغ","ما صارت من فراغ"):stV(x,"ما بيشتغل لحاله","ما بتشتغل لحالها");};
const stAgain=x=>{const k=stSubj();return k==="math"?`وفي أساس ثاني ${stV(x,"مبني","مبنية")} عليه ${stQ(x)}`:k==="history"?`وفي سبب ثاني ورا ${stQ(x)}`:`وفي عنصر ثاني ${stV(x,"بيعتمد","بتعتمد")} عليه ${stQ(x)}`;};
const stRel=(as,b,whys)=>{const w=[...new Set(as.map(a=>whys[a+">"+b]).filter(Boolean))].slice(0,2).join("، ");return `${stQ(b)} ${stNeeds(b)} ${as.map(stQ).join(" و")}${w?`: ${w}`:""}`;};
const stNth=ns=>ns.map(n=>ST_NTH[n-1]||stAr(n)).join(" و");
/* 🆕 batch 45: the first one of «the climb» asks who needs it */
const stWho=(b,kid)=>{const k=stSubj();if(k==="math")return `أنا ${stQ(b)}! مين مبني عليّ؟${kid?" 🤗":""}`;if(k==="history")return `أنا ${stQ(b)}! شو رح يصير بسببي؟${kid?" 🤗":""}`;
  return kid?`أنا ${stQ(b)}! مين بيحتاجني؟ 🤗`:`أنا ${stQ(b)}، مين بيحتاجني؟`;};
const stHelloMany=(b,kid)=>{const k=stSubj();if(k==="math")return `${stV(b,"إنت مبني","إنتِ مبنية")} علينا!${kid?" 💪":""}`;if(k==="history")return `إحنا السبب!${kid?" ✋":""}`;return kid?"إحنا هون! 💪":"إحنا معك!";};
const stLostWord=hurt=>stW()?stW().lost(stFem(exName(hurt[0])),hurt.length>1):VOICE(hurt.length>1?"ما بيقدروا":stFem(exName(hurt[0]))?"ما بتقدر":"ما بيقدر");
const stLost=(hurt,base,mark)=>`${mark?mark+" ":""}${hurt.slice(0,3).map(stQ).join(" و")} ${stW()?stW().lost(stFem(exName(hurt[0])),hurt.length>1):VOICE(hurt.length>1?"ما بيقدروا":stFem(exName(hurt[0]))?"ما بتقدر":"ما بيقدر")} ${stFem(exName(base))?"بدونها":"بدونه"}!`;
const ST_TONE={
  kids:{ch:["البداية","المشكلة","الرحلة","المفاجأة","النهاية السعيدة"],
    open:(h,place)=>`📖 كان يا ما كان، ب${place}، ${stV(h,"عاش","عاشت")} ${stQ(h)}.`,
    hi:h=>`أنا ${stQ(h)}! 👋`,
    problem:h=>`😟 بيوم من الأيام، ${stQ(h)} ${stV(h,"حسّ","حسّت")} إنه ${stMiss(h)}…`,
    lead:h=>`📖 و${stQ(h)} كمان ${stMiss(h)}…`,
    ask:x=>`📖 بس ${stQ(x)} كمان ${stMiss(x)}…`,
    again:x=>`📖 و${stQ(x)} ${stMiss(x,true)}…`,
    me:(x,again,lead)=>stMe(x,again,lead,true),
    come:as=>as.length>1?`📖 وفجأة… إجوا ${as.map(stQ).join(" و")}!`:`📖 وفجأة… ${stV(as[0],"إجى","إجت")} ${stQ(as[0])}!`,
    hello:(as,b)=>as.length>1?stHelloMany(b,true):stHello(as[0],b,true),thanks:()=>"شكراً! ✨",
    also:(a,b)=>`📖 و${stQ(b)} كمان ${stNeeds(b)} ${stQ(a)}`,
    other:h=>`📖 وبمكان ثاني، ${stV(h,"كان عايش","كانت عايشة")} ${stQ(h)}…`,
    lone:(id,m)=>`📖 وكمان كان في ${stQ(id)}${m?`: ${m}`:""}`,
    twist:b=>`😱 فجأة، ${stV(b,"اختفى","اختفت")} ${stQ(b)}!`,
    thief:(th,b)=>`😱 فجأة… ${th.f?"إجت":"إجى"} ${th.n} ${th.f?"شقية":"شقي"} و${th.f?"خطفت":"خطف"} ${stQ(b)}!`,
    help:"إلحقوني! 😱",miss:b=>`وين ${stQ(b)}؟ 😢`,
    without:(b,hurt)=>`😟 بدون ${stQ(b)}، ${hurt.slice(0,3).map(stQ).join(" و")} ${stLostWord(hurt)}!`,
    call:(th,b)=>`يا ${th.n}! ${stGiveBack(th,b)}… ${stNeedIt(b)}! 🙏`,
    /* 🆕 batch 40: the way it vanishes fits the thing */
    take:(w,th,b)=>({carry:()=>ST_TONE.kids.thief(th,b),sponge:()=>`😱 فجأة… إجت إسفنجة عطشانة ونشّفت ${stQ(b)} ${stV(b,"كله","كلها")}!`,cloud:()=>`😱 فجأة… إجت غيمة كبيرة وغطّت ${stQ(b)}!`,
      mole:()=>`😱 فجأة… طلع خُلد من تحت الأرض وسحب ${stQ(b)} لتحت!`,balloon:()=>`😱 فجأة… إجى بالون وشفط ${stQ(b)} ${stV(b,"كله","كلها")}!`,think:()=>`💭 تخيّلوا لو ما في ${stQ(b)}…`})[w](),
    call2:(w,th,b)=>w==="think"?`${stNeedIt(b)}! 🙏`:w==="cloud"?`يا غيمة! تحرّكي… ${stNeedIt(b)}! 🙏`:ST_TONE.kids.call(th,b),
    ret:(w,th,b)=>({carry:()=>ST_TONE.kids.returns(th,b),sponge:()=>`📖 فعصرت الإسفنجة حالها ورجّعت ${stQ(b)}…`,cloud:()=>`📖 فتحرّكت الغيمة، و${stV(b,"بيّن","بيّنت")} ${stQ(b)} من جديد…`,
      mole:()=>`📖 فطلع الخُلد ورجّع ${stQ(b)}…`,balloon:()=>`📖 فرجع البالون وطلّع ${stQ(b)}…`,think:()=>`😮‍💨 بس لا تخافوا… ${stQ(b)} ${stV(b,"موجود","موجودة")}!`})[w](),
    called:(c,b)=>`📖 ${stQ(c)} ${stV(c,"نادى","نادت")}: ${stNeedIt(b)}!`,
    sorry:th=>th.f?"آسفة! 🙈":"آسف! 🙈",returns:(th,b)=>`📖 ${th.f?"فرجعت":"فرجع"} ${th.al||"ال"+th.n} ${th.f?"ومعها":"ومعه"} ${stQ(b)}…`,
    back:b=>`🙌 ${stV(b,"رجع","رجعت")} ${stQ(b)}، والكل فرح!`,
    end:h=>`🎉 ومن يومها، ${stQ(h)} ${stV(h,"وأصحابه","وأصحابها")} صاروا يساعدوا بعض.`,
    moral:c=>`💡 العبرة: ${stMoral(c)}`,
    /* 🆕 batch 45: the two new tales (🚶 the climb · 🎉 the gathering) */
    chJ:"الطريق لفوق",chP:"مين بيساعد؟",
    jOpen:(b,place)=>`📖 كان يا ما كان، ب${place}، ${stV(b,"كان","كانت")} ${stQ(b)}… والحكاية بتبلش ${stV(b,"منه","منها")}.`,
    jHi:b=>stWho(b,true),jMore:as=>`📖 وكان في كمان ${as.map(stQ).join(" و")}.`,
    jArrive:x=>`📖 وبعدين ${stV(x,"وصل","وصلت")} ${stQ(x)}…`,jLast:h=>`📖 وأخيراً ${stV(h,"وصل","وصلت")} ${stQ(h)}، ${stV(h,"بطل","بطلة")} حكايتنا!`,
    pOpen:place=>`📖 بيوم حلو، اجتمعوا الأصحاب كلهم ب${place}! 🎈`,pHero:h=>`📖 وكان بينهم ${stQ(h)}…`,
    pOther:h=>`📖 وبزاوية ثانية، ${stQ(h)} كمان ${stV(h,"بدّه","بدّها")} مساعدة…`},
  junior:{ch:["البداية","المهمة","المغامرة","المفاجأة","النهاية"],
    open:(h,place)=>`🧭 مغامرة ب${place}: ${stV(h,"بطلنا","بطلتنا")} ${stQ(h)}.`,
    hi:h=>`أنا ${stQ(h)}!`,
    problem:h=>`🗺️ ${stQ(h)} ${stV(h,"عنده","عندها")} مهمة… بس ${stMiss(h)}!`,
    lead:h=>`🧭 و${stQ(h)} كمان ${stMiss(h)}…`,
    ask:x=>`🧭 بس ${stQ(x)} كمان ${stMiss(x)}…`,
    again:x=>`🧭 و${stQ(x)} ${stMiss(x,true)}…`,
    me:(x,again,lead)=>stMe(x,again,lead,false),
    come:as=>as.length>1?`🧭 انضمّوا للفريق: ${as.map(stQ).join(" و")}`:`🧭 ${stV(as[0],"انضمّ","انضمّت")} للفريق: ${stQ(as[0])}`,
    hello:(as,b)=>as.length>1?stHelloMany(b,false):stHello(as[0],b,false),thanks:()=>"شكراً!",
    also:(a,b)=>`🧭 و${stQ(b)} كمان ${stNeeds(b)} ${stQ(a)}`,
    other:h=>`🧭 وعلى طريق ثاني: ${stQ(h)}…`,
    lone:(id,m)=>`🧭 وكمان بالفريق: ${stQ(id)}${m?`: ${m}`:""}`,
    twist:b=>`⚡ فجأة ${stV(b,"اختفى","اختفت")} ${stQ(b)}!`,
    thief:(th,b)=>`⚡ فجأة ${th.f?"خطفت":"خطف"} ${th.n} ${stQ(b)} ${th.f?"وهربت":"وهرب"}!`,
    help:"ساعدوني!",miss:b=>`وين ${stQ(b)}؟`,
    without:(b,hurt)=>`🧭 بدون ${stQ(b)}، ${hurt.slice(0,3).map(stQ).join(" و")} ${stLostWord(hurt)}!`,
    call:(th,b)=>`يا ${th.n}، ${stGiveBack(th,b)}! ${stNeedIt(b)}!`,
    take:(w,th,b)=>({carry:()=>ST_TONE.junior.thief(th,b),sponge:()=>`⚡ فجأة نشّفت إسفنجة ${stQ(b)}!`,cloud:()=>`⚡ فجأة غطّت غيمة كبيرة ${stQ(b)}!`,
      mole:()=>`⚡ فجأة سحب خُلد ${stQ(b)} لتحت الأرض!`,balloon:()=>`⚡ فجأة شفط بالون ${stQ(b)} وطار!`,think:()=>`💭 تخيّلوا لو ${stV(b,"اختفى","اختفت")} ${stQ(b)}…`})[w](),
    call2:(w,th,b)=>w==="think"?`${stNeedIt(b)}!`:w==="cloud"?`يا غيمة، تحرّكي! ${stNeedIt(b)}!`:ST_TONE.junior.call(th,b),
    ret:(w,th,b)=>({carry:()=>ST_TONE.junior.returns(th,b),sponge:()=>`🧭 وعصرت الإسفنجة حالها ورجّعت ${stQ(b)}…`,cloud:()=>`🧭 وتحرّكت الغيمة، و${stV(b,"بيّن","بيّنت")} ${stQ(b)}…`,
      mole:()=>`🧭 وطلع الخُلد ورجّع ${stQ(b)}…`,balloon:()=>`🧭 ورجع البالون وطلّع ${stQ(b)}…`,think:()=>`🧭 بس ${stQ(b)} ${stV(b,"موجود","موجودة")}، ما ${stV(b,"اختفى","اختفت")}!`})[w](),
    called:(c,b)=>`🧭 ${stQ(c)} ${stV(c,"نادى","نادت")}: ${stNeedIt(b)}!`,
    sorry:th=>th.f?"آسفة!":"آسف!",returns:(th,b)=>`🧭 ${th.f?"ورجعت":"ورجع"} ${th.al||"ال"+th.n} ${th.f?"ومعها":"ومعه"} ${stQ(b)}…`,
    back:b=>`✨ ${stV(b,"رجع","رجعت")} ${stQ(b)}، والمغامرة كملت!`,
    end:h=>`🏁 ${stQ(h)} ${stV(h,"خلّص","خلّصت")} المهمة بمساعدة الفريق كله!`,
    moral:c=>`💡 العبرة: ${stMoral(c)}`,
    chJ:"الصعود",chP:"الفريق",
    jOpen:(b,place)=>`🧭 مغامرة ب${place} بتبلش من تحت: من ${stQ(b)}.`,
    jHi:b=>stWho(b,false),jMore:as=>`🧭 وعلى نفس الأرض: ${as.map(stQ).join(" و")}.`,
    jArrive:x=>`🧭 ${stV(x,"وصل","وصلت")} ${stQ(x)}…`,jLast:h=>`🧭 وآخر واحد ${stV(h,"وصل","وصلت")}: ${stQ(h)}، ${stV(h,"بطل","بطلة")} المهمة!`,
    pOpen:place=>`🧭 الفريق كله تجمّع ب${place}، والمهمة على وشك تبلش.`,pHero:h=>`🧭 ${stV(h,"قائد","قائدة")} الفريق: ${stQ(h)}…`,
    pOther:h=>`🧭 وبالفريق كمان: ${stQ(h)}… ${stV(h,"بدّه","بدّها")} مساعدة.`},
  teen:{ch:["القضية","الأدلة","الاختبار","الحل"],tt:"🕵️ ملف قضية",
    open:h=>`🕵️ القضية: ${stCase(h)}`,
    problem:h=>`🔍 ${stQ(h)} ${stAlone(h)}… لازم نلاقي الدليل.`,
    lead:h=>`🔍 ${stCase(h)}`,
    ask:x=>`🔍 و${stQ(x)} ${stV(x,"نفسه","نفسها")}… ${stAskS(x)}`,
    again:x=>`🔍 في دليل ثاني كمان عن ${stQ(x)}…`,
    found:(ns,as,b,whys)=>`🔍 الدليل ${stNth(ns)}: ${stRel(as,b,whys)}`,
    also:(a,b)=>`🧵 خيط جديد: ${stQ(b)} كمان ${stNeeds(b)} ${stQ(a)}`,
    other:h=>`🗂️ ملف ثاني: ${stCase(h)}`,
    lone:(id,m)=>`📎 معلومة إضافية: ${stQ(id)}${m?`: ${m}`:""}`,
    twist:b=>`🧪 اختبار: شو لو شلنا ${stQ(b)} من اللوح؟`,
    back:b=>`✅ ${stV(b,"رجع","رجعت")} ${stQ(b)}، وكل الخيوط رجعت مشدودة.`,
    end:h=>`✅ انحلّت القضية: ${stQ(h)} ${stNeeds(h)} سلسلة كاملة من الأدلة.`,
    moral:c=>`📌 الخلاصة: ${stMoral(c)}`},
  senior:{ch:["السؤال","التتبّع","الفرضية","الاستنتاج"],tt:"مخطط الدرس",
    open:h=>`السؤال: ${stCase(h)}`,
    problem:h=>`${stQ(h)} ${stV(h,"ما بيتحقق لوحده","ما بتتحقق لوحدها")}؛ خلّينا نتتبّع اللي ${stV(h,"قبله","قبلها")}.`,
    lead:h=>`سؤال فرعي: ${stCase(h)}`,
    ask:x=>`الخطوة التالية: ${stQ(x)}… ${stAskS(x)}`,
    again:x=>`${stAgain(x)}…`,
    found:(ns,as,b,whys)=>stRel(as,b,whys),
    also:(a,b)=>`علاقة إضافية: ${stQ(b)} ${stNeeds(b)} ${stQ(a)}`,
    other:h=>`سؤال فرعي: ${stCase(h)}`,
    lone:(id,m)=>`عنصر مستقل: ${stQ(id)}${m?`: ${m}`:""}`,
    twist:b=>`⚠️ فرضية: لو غاب ${stQ(b)}…`,
    back:b=>`✔️ بعودة ${stQ(b)} بترجع السلسلة كاملة.`,
    end:h=>`📌 الاستنتاج: ${stQ(h)} ${stNeeds(h)} سلسلة كاملة، مش عنصر واحد.`,
    moral:c=>`📌 ${stMoral(c)}`}};

/* where the cards / the nodes stand: one column per level (right → left: the order we learn in); the phone: one row per level (wraps);
   no levels (no links) → a grid. Returns the picture's width, where its drawing ends, and every one's centre. */
function stGridPos(ids,lv,v,cw,ch,top,gx,gy,far){const W=v?380:760,lvls=[...new Set(ids.map(i=>lv[i]))].sort((a,b)=>a-b),pos={};let H;
  if(!v&&lvls.length>1){const per=Math.max(...lvls.map(L=>ids.filter(i=>lv[i]===L).length)),span=Math.min((W-40-cw)/(lvls.length-1),cw+(far||200));
    lvls.forEach((L,ci)=>{const g=ids.filter(i=>lv[i]===L);g.forEach((id,j)=>{pos[id]=[W/2+((lvls.length-1)/2-ci)*span,top+ch/2+(j+(per-g.length)/2)*(ch+gy)];});});
    H=top+per*(ch+gy);}
  else{const n=Math.max(1,Math.floor((W-16+gx)/(cw+gx))),rows=[];
    (v?lvls:[null]).forEach(L=>{const g=L===null?ids.slice():ids.filter(i=>lv[i]===L);for(let i=0;i<g.length;i+=n)rows.push(g.slice(i,i+n));});
    rows.forEach((r,ri)=>r.forEach((id,j)=>{pos[id]=[W/2+((r.length-1)/2-j)*(cw+gx),top+ch/2+ri*(ch+gy)];}));
    H=top+rows.length*(ch+gy);}
  return {W,H,pos};}
/* a character's drawing alone (no name, no bubble): for the cards and the nodes */
const stArt=(id,size,dy)=>{const ic=iconOf(id);let a=ic?dressed(id,artSVG(ic,"")):null;if(!a)a=`<svg class="ch" viewBox="0 0 100 100">${ARTS.blob(colorOf(id))}</svg>`;
  return a.replace("<svg ",`<svg width="${size}" height="${size}" x="${-size/2}" y="${-size/2+(dy||0)}" `);};

/* ---------- ② 🌈 kids · 🧭 junior: the characters in the lesson's place ---------- */
function stCast(s,P,tale){const v=V(),lo=document.body.dataset.q==="lo",st=stageNow(),kid=st!=="junior",tone=ST_TONE[kid?"kids":"junior"];
  const k=speedNow(),theme=ST_THEME[stSubj()]||"room";
  const ids=s.guests.concat(s.ids),lv=s.levels;
  const cols=[...new Set(ids.map(i=>lv[i]))].sort((a,b)=>a-b),per=Math.max(...cols.map(L=>ids.filter(i=>lv[i]===L).length));
  /* the picture grows with the cast: room for every character and its name (computer: columns · phone: rows) */
  const W=v?380:760,Z=v?62:78,floor=v?130:172,H=(v?Math.max(470,floor+60+cols.length*112):Math.max(428,floor+50+per*104))+(v?64:58);   /* + room for the subtitles */
  const pos={};
  cols.forEach((L,ci)=>{const g=ids.filter(i=>lv[i]===L);g.forEach((id,j)=>{
    if(v){const x=W-W*(j+0.5)/g.length;pos[id]=[x,floor+70+ci*112];}
    else{const x=cols.length===1?W/2+(j-(g.length-1)/2)*130:W-80-ci*((W-160)/(cols.length-1));const y=floor+58+j*104+(g.length===1?(per-1)*52:0);pos[id]=[x,y];}});});
  let T=0;const K=stKit(ids,pos,W,Z,k),{ev,d,off,mv,mood,sub,bub,chap,cue,N}=K;const place=ST_PLACE[placeNow()]||ST_PLACE.room,hero=P.hero;
  const say=(id,t0,t1,txt)=>{bub(id,t0,t1,txt);ev.talk[id].push([t0,t0+(t1-t0)*0.75]);};
  let asked=false,called=false;
  /* the beats every tale shares: «ناقصني…» (ask) · one already there helps too (link) */
  const askBeat=b=>{const x=b.x;if(!asked)chap(T,tone.ch[1]);
      const L=b.again?2.1:2.4;mood(x,T,b.lead?"sad":"o");ev.pulse[x].push(T+d(0.2));say(x,T+d(0.25),T+d(L-0.4),tone.me(x,b.again,b.lead));
      sub(T,T+d(L),x===hero&&!asked?tone.problem(x):b.lead?tone.lead(x):b.again?tone.again(x):tone.ask(x));cue(T+d(0.3),b.lead?"bad":"pop");asked=true;T+=d(L);};
  const linkBeat=b=>{const why=s.why[b.a+">"+b.b];T=K.give(b.a,b.b,T,`${tone.also(b.a,b.b)}${why?`: ${why}`:""}`);};
  /* 🆕 batch 45: the ones it needs are ALREADY in the picture → they walk over (up to 3 together), give the glowing ball, the arrows, back to their places */
  const help=(as,x)=>{const np={},m=as.length-1,dur=5.25+m*0.35;sub(T,T+d(dur-0.1),stRel(as,x,s.why));mood(x,T,"o");
    as.forEach((a,i)=>{np[a]=K.near(a,x);mv(a,T+d(0.3+i*0.2),T+d(1.3+i*0.2),pos[a],np[a]);});cue(T+d(1.2),"step");T+=d(1.35+m*0.2);
    say(as[0],T,T+d(1.3),tone.hello(as,x));T+=d(0.7);
    as.forEach((a,i)=>ev.orb.push([T+d(i*0.15),T+d(0.8+i*0.15),a,x]));cue(T,"pick");T+=d(0.8+m*0.15);cue(T,"good");
    ev.pulse[x].push(T);mood(x,T,"joy");ev.glow[x].push([T,T+d(1)]);ev.spark.push([T,x]);say(x,T+d(0.15),T+d(1.25),tone.thanks(x));
    as.forEach((a,i)=>{ev.link.push([T+d(0.2+i*0.1),a,x]);mv(a,T+d(0.5),T+d(1.4),np[a],pos[a]);});mood(x,T+d(1.4),"happy");T+=d(2.4);called=true;};
  const loneBeat=(id,walk)=>{const m=stMean(s,id);if(walk)T=K.enter(id,T,1.3);else ev.pulse[id].push(T+d(0.2));sub(walk?T-d(0.6):T,T+d(3),tone.lone(id,m));say(id,T+d(walk?0:0.2),T+d(1.4),tone.hi(id));T+=d(3.1);};
  if(tale==="journey"){
  /* 🆕 batch 45 · 🚶 THE CLIMB: the tale starts from the BOTTOM (one that needs nothing) and goes up: each one that arrives finds the ones it
     needs already there — they walk over and give; the hero arrives last. Every arrow of the lesson is still drawn, each one once. */
    const pre={},has=new Set();ids.forEach(i=>pre[i]=[]);
    s.edges.forEach(([a,b])=>{if(pre[a]&&pre[b]&&a!==b){has.add(a);has.add(b);if(!pre[b].includes(a))pre[b].push(a);}});
    const on=new Set(),order=[];let rest=ids.filter(i=>has.has(i)),last=null;
    while(rest.length){const there=x=>pre[x].filter(p=>on.has(p)).length;let r=rest.filter(x=>there(x)===pre[x].length);
      if(!r.length)r=[rest.slice().sort((x,y)=>there(y)-there(x))[0]];   /* a circle: the one with most of its needs already there */
      const sc=x=>(x===hero?100:0)+(pre[x].length?10:0)-(last&&pre[x].includes(last)?5:0);   /* the hero last · the bottom ones first · then one that needs the one who just came */
      r.sort((x,y)=>sc(x)-sc(y)||ids.indexOf(x)-ids.indexOf(y));const x=r[0];order.push(x);on.add(x);last=x;rest=rest.filter(i=>i!==x);}
    const roots=order.filter(x=>!pre[x].length),first=roots[0],shown=new Set(),done=new Set();
    chap(0,tone.ch[0]);
    if(first){sub(0,d(3.6),tone.jOpen(first,place));T=K.enter(first,d(0.8),1.6);say(first,T,T+d(1.7),tone.jHi(first));cue(T,"pop");T+=d(2.0);shown.add(first);}
    else{sub(0,d(3.4),tone.jOpen(hero,place));T=K.enter(hero,d(0.8),1.6);say(hero,T,T+d(1.6),tone.hi(hero));cue(T,"pop");T+=d(1.9);shown.add(hero);}   /* (no links at all) */
    const more=roots.filter(x=>x!==first);
    for(let i=0;i<more.length;i+=3){const g=more.slice(i,i+3);sub(T,T+d(2.6),tone.jMore(g));g.forEach((a,j)=>{K.enter(a,T+d(j*0.25),1.3);shown.add(a);});say(g[0],T+d(1.5),T+d(2.5),tone.hi(g[0]));T+=d(2.7);}
    let up=false;order.filter(x=>pre[x].length).forEach(x=>{if(!up){chap(T,tone.chJ);up=true;}
      sub(T,T+d(2.4),x===hero?tone.jLast(x):tone.jArrive(x));T=K.enter(x,T+d(0.1),1.4);shown.add(x);
      mood(x,T,"o");ev.pulse[x].push(T);say(x,T+d(0.1),T+d(1.2),tone.me(x,false,true));cue(T+d(0.1),"pop");T+=d(1.3);
      const as=pre[x].filter(p=>shown.has(p));for(let i=0;i<as.length;i+=3){const g=as.slice(i,i+3);g.forEach(a=>done.add(a+">"+x));help(g,x);}});
    s.edges.forEach(([a,b])=>{if(a!==b&&shown.has(a)&&shown.has(b)&&!done.has(a+">"+b)){done.add(a+">"+b);linkBeat({a,b});called=true;}});   /* (a circle: the arrow that was left) */
    ids.filter(i=>!shown.has(i)).forEach(i=>{shown.add(i);loneBeat(i,true);});}
  else if(tale==="party"){
  /* 🆕 batch 45 · 🎉 THE GATHERING: everybody is in the place from the start; then the hero finds it can't do it alone, and one by one
     the ones it needs (already there) walk over and give — the same order of needs as the classic tale, a different picture. */
    chap(0,tone.ch[0]);sub(0,d(3.4),tone.pOpen(place));
    ids.forEach((id,i)=>K.enter(id,d(0.6+Math.min(i,8)*0.22),1.3));T=Math.max(d(3.5),d(0.6+Math.min(ids.length-1,8)*0.22+1.4));cue(T-d(0.2),"pop");
    sub(T,T+d(2.6),tone.pHero(hero));ev.pulse[hero].push(T+d(0.1));say(hero,T+d(0.2),T+d(1.8),tone.hi(hero));T+=d(2.7);
    if(!P.beats.some(b=>b.t!=="lone")&&stMean(s,hero)){sub(T,T+d(2.8),`${N(hero)}: ${stMean(s,hero)}`);T+=d(2.9);}
    P.beats.forEach(b=>{
      if(b.t==="ask")askBeat(b);
      else if(b.t==="call"){if(!called)chap(T,tone.chP);help(b.as,b.b);}
      else if(b.t==="link")linkBeat(b);
      else if(b.t==="other"){sub(T,T+d(2.4),tone.pOther(b.id));mood(b.id,T,"o");ev.pulse[b.id].push(T+d(0.2));say(b.id,T+d(0.3),T+d(1.8),tone.hi(b.id));T+=d(2.5);}
      else if(b.t==="lone")loneBeat(b.id,false);});}
  else{
  /* 1 · the beginning: the hero comes ALONE (everybody else waits outside until somebody needs them) */
  chap(0,tone.ch[0]);sub(0,d(3.4),tone.open(hero,place));
  T=K.enter(hero,d(0.8),1.6);say(hero,T,T+d(1.6),tone.hi(hero));cue(T,"pop");T+=d(1.9);
  if(!P.beats.some(b=>b.t!=="lone")&&stMean(s,hero)){sub(T,T+d(2.8),`${N(hero)}: ${stMean(s,hero)}`);T+=d(2.9);}
  /* 2 · one by one: «ناقصني…» → the one it needs comes and gives → it says what IT misses → … */
  P.beats.forEach(b=>{
    if(b.t==="ask")askBeat(b);
    else if(b.t==="call"){const as=b.as,x=b.b,np={},m=as.length-1;if(!called){chap(T,tone.ch[2]);called=true;}
      sub(T,T+d(2.1),tone.come(as,x));
      as.forEach((a,i)=>{np[a]=K.near(a,x);mv(a,-1,T+d(i*0.25),off(a),off(a));mv(a,T+d(i*0.25),T+d(1.3+i*0.25),off(a),np[a]);});cue(T+d(1.2),"step");T+=d(1.3+m*0.25);   /* it walks in, straight to the one who needs it */
      say(as[0],T,T+d(1.4),tone.hello(as,x));T+=d(0.75);
      as.forEach((a,i)=>ev.orb.push([T+d(i*0.15),T+d(0.8+i*0.15),a,x]));cue(T,"pick");T+=d(0.8+m*0.15);cue(T,"good");   /* it GIVES the glowing ball */
      sub(T-d(0.5),T+d(3.1),stRel(as,x,s.why));
      ev.pulse[x].push(T);mood(x,T,"joy");ev.glow[x].push([T,T+d(1)]);ev.spark.push([T,x]);say(x,T+d(0.15),T+d(1.25),tone.thanks(x));
      as.forEach((a,i)=>{ev.link.push([T+d(0.2+i*0.1),a,x]);mv(a,T+d(0.5),T+d(1.4),np[a],pos[a]);});mood(x,T+d(1.4),"happy");T+=d(3.1);}   /* the arrow, then it goes to its place */
    else if(b.t==="link")linkBeat(b);
    else if(b.t==="other"){sub(T,T+d(2.8),tone.other(b.id));T=K.enter(b.id,T+d(0.2),1.5);say(b.id,T,T+d(1.5),tone.hi(b.id));T+=d(1.7);}
    else if(b.t==="lone")loneBeat(b.id,true);});}
  /* 3 · the twist (🆕 batch 39): a thief of the place grabs the one everybody needs → the story STAYS on what happens without it →
       somebody calls «we need it!» → the thief brings it back. The point is the middle part (what happens if it is missing), not the chase. */
  const B=P.base,hurt=P.hurt,TH="__thief";let thief=null;
  if(hurt.length&&called){chap(T,tone.ch[3]);
    /* 🆕 batch 40: the way it vanishes fits what it is (stWay): carry · sponge · cloud · mole · balloon · think */
    const way=stWay(B),th=way==="carry"?stThief():ST_AGENT[way];
    const P0=pos[B],side=P0[0]<W/2?-1:1,away=[side<0?-110:W+110,P0[1]],grab=[P0[0]-side*Z*0.8,P0[1]],up=p=>[p[0],p[1]-Z*0.62];
    pos[TH]=away;ev.mv[TH]=[];ev.thsz=[];ev.thfade=[];ev.sz={};ev.fade={};ev.sz[B]=[];ev.fade[B]=[];
    thief={kind:way==="carry"?(ST_THIEF_OF[placeNow()]||"rabbit"):way,svg:th.svg,way};
    const sz=(t0,t1,x,y)=>ev.sz[B].push([t0,t1,x,y]),fade=(t0,t1,x,y)=>ev.fade[B].push([t0,t1,x,y]);
    const thsz=(t0,t1,x,y)=>ev.thsz.push([t0,t1,x,y]),thfade=(t0,t1,x,y)=>ev.thfade.push([t0,t1,x,y]);
    sub(T,T+d(3.6),tone.take(way,th,B));
    let t,gone,park;   /* park = where it waits while it is away (to come back from there) */
    if(way==="carry"){                                                                               /* the thief runs in, grabs it, runs away with it */
      mv(TH,-1,T+d(0.5),away,away);mv(TH,T+d(0.5),T+d(1.8),away,grab);cue(T+d(1.7),"step");
      t=T+d(1.9);mood(B,t,"o");ev.pulse[B].push(t);cue(t,"flip");
      mv(B,t,t+d(0.35),P0,up(grab));bub(B,t+d(0.3),t+d(1.6),tone.help);t+=d(0.45);
      mv(TH,t,t+d(1.3),grab,away);mv(B,t,t+d(1.3),up(grab),up(away));cue(t,"step");t+=d(1.3);gone=t-d(0.2);park=up(away);}
    else if(way==="sponge"||way==="balloon"){                                                        /* it soaks / sucks it all in (it gets smaller and goes INTO it) */
      const nr=[P0[0]-side*Z*0.78,P0[1]-(way==="balloon"?Z*0.55:0)];
      mv(TH,-1,T+d(0.5),away,away);mv(TH,T+d(0.5),T+d(1.8),away,nr);cue(T+d(1.7),"step");
      t=T+d(1.9);mood(B,t,"o");ev.pulse[B].push(t);cue(t,"flip");bub(B,t+d(0.1),t+d(1.2),tone.help);
      mv(B,t+d(0.7),t+d(1.7),P0,nr);sz(t+d(0.7),t+d(1.7),1,0.15);fade(t+d(1.3),t+d(1.7),1,0);thsz(t+d(0.7),t+d(1.7),1,1.3);cue(t+d(0.9),"pick");t+=d(1.8);
      const off=way==="balloon"?[away[0],P0[1]-Z*2]:away;mv(TH,t,t+d(1.4),nr,off);cue(t,"step");t+=d(1.4);gone=t-d(1.5);park=nr;
      ev.__back=()=>{mv(TH,t,t+d(1.3),off,nr);cue(t+d(1.2),"step");t+=d(1.35);thsz(t,t+d(0.9),1.3,1);mv(B,t,t+d(0.9),nr,P0);sz(t,t+d(0.9),0.15,1);fade(t,t+d(0.4),0,1);cue(t,"pop");t+=d(1.0);
        bub(TH,t,t+d(1.4),tone.sorry(th));mv(TH,t+d(1.0),t+d(2.2),nr,off);};}
    else if(way==="cloud"){                                                                          /* a big cloud comes over it and covers it */
      const cx=Math.max(Z*1.45,Math.min(W-Z*1.45,P0[0])),top=[cx,P0[1]-Z*1.25],over=[cx,P0[1]-Z*0.2],gone0=[away[0],P0[1]-Z*1.9];   /* it stays inside the picture */
      mv(TH,-1,T+d(0.4),gone0,gone0);mv(TH,T+d(0.4),T+d(1.8),gone0,top);thsz(T,T+d(0.1),1.25,1.25);
      t=T+d(1.9);mood(B,t,"o");bub(B,t,t+d(1.1),tone.help);
      mv(TH,t+d(0.6),t+d(1.6),top,over);thsz(t+d(0.6),t+d(1.6),1.25,1.7);fade(t+d(0.9),t+d(1.6),1,0);cue(t+d(1.2),"flip");t+=d(1.8);gone=t-d(0.2);park=P0;
      ev.__back=()=>{mv(TH,t,t+d(1.3),over,top);thsz(t,t+d(1.3),1.7,1.25);fade(t+d(0.2),t+d(1.1),0,1);cue(t+d(0.4),"pop");t+=d(1.4);
        bub(TH,t,t+d(1.4),tone.sorry(th));mv(TH,t+d(1.0),t+d(2.3),top,gone0);};}
    else if(way==="mole"){                                                                           /* a mole pops up and pulls it down under the ground */
      const hole=[P0[0]-side*Z*0.85,P0[1]+Z*0.1],low=[hole[0],hole[1]+Z*0.35],deep=[P0[0],P0[1]+Z*0.5];
      mv(TH,-1,T+d(0.6),low,low);thfade(-1,T+d(0.6),0,0);mv(TH,T+d(0.6),T+d(1.3),low,hole);thfade(T+d(0.6),T+d(1.1),0,1);cue(T+d(0.9),"pop");
      t=T+d(1.5);mood(B,t,"o");ev.pulse[B].push(t);bub(B,t,t+d(1.2),tone.help);
      mv(B,t+d(0.7),t+d(1.6),P0,deep);sz(t+d(0.7),t+d(1.6),1,0.75);fade(t+d(1.0),t+d(1.6),1,0);cue(t+d(0.8),"flip");
      mv(TH,t+d(1.4),t+d(2.0),hole,low);thfade(t+d(1.4),t+d(2.0),1,0);t+=d(2.1);gone=t-d(0.4);park=deep;
      ev.__back=()=>{mv(TH,t,t+d(0.6),low,hole);thfade(t,t+d(0.5),0,1);cue(t+d(0.3),"pop");t+=d(0.7);
        mv(B,t,t+d(0.9),deep,P0);sz(t,t+d(0.9),0.75,1);fade(t,t+d(0.5),0,1);t+=d(1.0);
        bub(TH,t,t+d(1.4),tone.sorry(th));mv(TH,t+d(1.3),t+d(1.9),hole,low);thfade(t+d(1.3),t+d(1.9),1,0);};}
    else{                                                                                            /* «💭 imagine there were no …»: a thought cloud, it fades away like a dream */
      const sky=[P0[0],-90],tb=[P0[0]+side*Z*0.2,P0[1]-Z*1.45];
      mv(TH,-1,T+d(0.3),sky,sky);thfade(-1,T+d(0.3),0,0);mv(TH,T+d(0.3),T+d(1.5),sky,tb);thfade(T+d(0.3),T+d(1.0),0,1);cue(T+d(1.2),"pop");
      t=T+d(1.7);mood(B,t,"o");fade(t,t+d(1.4),1,0.12);t+=d(1.6);gone=t-d(0.3);park=P0;
      ev.__back=()=>{thsz(t,t+d(0.45),1,1.45);thfade(t+d(0.15),t+d(0.45),1,0);cue(t+d(0.2),"pop");fade(t+d(0.2),t+d(0.9),0.12,1);t+=d(1.0);};}
    /* what happens WITHOUT it: the ones who need it turn grey and sad, one by one, and say they miss it — the line says why */
    const gap=Math.min(0.6,2/hurt.length),hold=3.4+hurt.length*gap,gs=[];
    hurt.forEach((h,i)=>{const tt=t+d(0.3+i*gap);gs.push([h,tt]);mood(h,tt,"sad");if(i<4)cue(tt,"bad");if(i<2)say(h,tt+d(0.1),tt+d(1.7),tone.miss(B));});
    sub(t,t+d(hold),tone.without(B,hurt));t+=d(hold);
    /* somebody calls: «we need it!» */
    const caller=hurt.includes(hero)?hero:hurt[0];say(caller,t,t+d(2.2),tone.call2(way,th,B));sub(t,t+d(2.4),tone.called(caller,B));t+=d(2.4);
    /* it comes back (the way it went) */
    sub(t,t+d(1.8),tone.ret(way,th,B));
    if(way==="carry"){mv(TH,t,t+d(1.3),away,grab);mv(B,t,t+d(1.3),park,up(grab));ev.out[B].push([gone,t+d(0.15)]);cue(t+d(1.2),"step");t+=d(1.35);
      mv(B,t,t+d(0.4),up(grab),P0);bub(TH,t+d(0.2),t+d(1.6),tone.sorry(th));t+=d(0.5);mv(TH,t+d(0.9),t+d(2.1),grab,away);}
    else{ev.__back();delete ev.__back;}
    mood(B,t,"happy");
    gs.forEach(([h,tt])=>ev.gray[h].push([tt,t]));
    hurt.forEach((h,i)=>{mood(h,t+d(0.2+i*0.2),"joy");mood(h,t+d(1.6+i*0.2),"happy");ev.pulse[h].push(t+d(0.2+i*0.15));});cue(t+d(0.2),"good");ev.spark.push([t,B]);
    sub(t,t+d(2.8),tone.back(B));T=t+d(3.0);}
  /* 4 · the happy end + the lesson of the story (العبرة) */
  chap(T,tone.ch[tone.ch.length-1]);sub(T,T+d(3),tone.end(hero));
  ids.forEach((id,i)=>{ev.pulse[id].push(T+d(0.2+i*0.12));mood(id,T+d(0.2),"joy");});ev.spark.push([T+d(0.3),hero]);cue(T+d(0.3),"tada");T+=d(3.1);
  if(P.chain.length>=2){sub(T,T+d(3.6),tone.moral(P.chain.map(stQ).join(" ← ")));T+=d(3.8);}
  const scale={};scale[hero]=1.14;   /* the hero is a little bigger */
  return stMake({ids,pos,W,H,floor,Z,theme,edges:s.edges,title:s.title,ev,DUR:T,lo,k,scale,hop:kid?1:0.4,thief,tale:tale||"classic"});}   /* the explorers walk calmly (small steps) */

/* ---------- 🆕 batch 39: the board and the diagram answer the student (Hareth: «المحقق… خلّيها تفاعلية») ----------
   · a tap on a card / a node → a little window: what it is, what it needs, who needs it (the video waits);
   · «🖐️ دورك» (only when the STUDENT plays the story; the auto video shows the answer like an example): before up to 3 evidences / nodes
     appear, it stops and asks «على شو بيعتمد X؟» with the right one + up to 2 wrong ones from the graph (one that needs X instead — the
     reverse —, one with no direct link), and every wrong choice is explained. Light on purpose: the activities after the story practise more. */
const stLinks=s=>{const pre={},nxt={};s.guests.concat(s.ids).forEach(i=>{pre[i]=[];nxt[i]=[];});s.edges.forEach(([a,b])=>{if(pre[b]&&nxt[a]&&a!==b){pre[b].push(a);nxt[a].push(b);}});
  const walk=(m,x)=>{const out=new Set(),q=[x];while(q.length){const y=q.shift();(m[y]||[]).forEach(z=>{if(!out.has(z)&&z!==x){out.add(z);q.push(z);}});}return out;};
  return {pre,nxt,anc:x=>walk(pre,x),desc:x=>walk(nxt,x)};};
function stChoices(s,L,x,a){const ids=s.guests.concat(s.ids),anc=L.anc(x),desc=L.desc(x);
  const rev=ids.filter(i=>i!==x&&i!==a&&desc.has(i)),other=ids.filter(i=>i!==x&&i!==a&&!anc.has(i)&&!desc.has(i));
  const wrong=[rev[0],other[0],other[1],rev[1]].filter(Boolean).filter((v,i,arr)=>arr.indexOf(v)===i).slice(0,2);
  if(!wrong.length)return null;
  const opts=[{id:a,ok:true,why:stRel([a],x,s.why)}].concat(wrong.map(w=>({id:w,ok:false,
    why:desc.has(w)?`${stQ(w)} ${stV(w,"هو اللي","هي اللي")} ${stNeeds(w)} ${stQ(x)}، مش العكس`:`${stQ(w)} ${stV(w,"ما إله","ما إلها")} علاقة مباشرة مع ${stQ(x)}`})));
  const h=[...(x+a)].reduce((n,c)=>n+c.charCodeAt(0),0);   /* a fixed mix (the right one is not always first) */
  return opts.map((o,i)=>[(h*7+i*13)%17,o]).sort((p,q)=>p[0]-q[0]).map(p=>p[1]);}
function stAsk(root,o,done){const scr=root.closest(".st-screen");if(!scr){done();return;}
  const box=document.createElement("div");box.className="st-ask";box.setAttribute("role","dialog");box.setAttribute("aria-label",VOICE(o.q).replace(/[«»]/g,""));
  box.innerHTML=`<b class="sa-q">${t37(VOICE(o.q))}</b><div class="sa-opts">${o.opts.map((p,i)=>`<button type="button" class="sa-opt" data-i="${i}" aria-label="${exName(p.id)}"><svg viewBox="-30 -36 60 60" width="46" height="46" aria-hidden="true">${stArt(p.id,50,0)}</svg><span>${exName(p.id)}</span></button>`).join("")}</div>
    <p class="sa-why" aria-live="polite"></p><button type="button" class="sa-show">${VOICE("👀 ورجيني الجواب")}</button>`;
  scr.appendChild(box);sfx("pop");let wrong=0,fin=false;const why=box.querySelector(".sa-why");
  const finish=right=>{if(fin)return;fin=true;box.classList.add("sa-done");box.querySelectorAll(".sa-opt").forEach((b,j)=>{b.disabled=true;if(o.opts[j].ok)b.classList.add("ok");});
    why.innerHTML=t37(VOICE((right?"✔ ":"👉 ")+o.opts.find(p=>p.ok).why));setTimeout(()=>{box.remove();done();},Math.round(2200*speedNow()));};
  box.querySelectorAll(".sa-opt").forEach(b=>b.addEventListener("click",()=>{const i=+b.dataset.i,p=o.opts[i];
    if(p.ok){sfx("good");finish(true);}else{sfx("bad");wrong++;b.classList.add("no");b.disabled=true;why.innerHTML=t37(VOICE("✗ "+p.why));if(wrong>=2)setTimeout(()=>finish(false),Math.round(1400*speedNow()));}}));
  box.querySelector(".sa-show").addEventListener("click",()=>finish(false));
  box.addEventListener("click",e=>e.stopPropagation());}
function stInfo(root,s,L,id){const scr=root.closest(".st-screen");if(!scr)return;const old=scr.querySelector(".st-info");if(old)old.remove();
  const k=stSubj(),A=k==="math"?["مبني على","مبني عليه"]:k==="history"?["صار بسبب","صار بسببه"]:[VOICE("بيحتاج"),VOICE("بيحتاجه")],pre=L.pre[id]||[],nxt=L.nxt[id]||[],m=stMean(s,id);
  const box=document.createElement("div");box.className="st-info";box.setAttribute("role","dialog");box.setAttribute("aria-label",exName(id));
  box.innerHTML=`<button type="button" class="si-x" aria-label="${VOICE("سكّر")}">✕</button><b class="si-n">${exName(id)}</b>${m?`<p class="si-m">${m}</p>`:""}
    ${pre.length?`<p><i>${A[0]}:</i> ${pre.map(exName).join("، ")}</p>`:""}${nxt.length?`<p><i>${A[1]}:</i> ${nxt.map(exName).join("، ")}</p>`:""}
    <button type="button" class="si-go">${VOICE("▶ كمّل")}</button>`;
  scr.appendChild(box);sfx("pop");box.addEventListener("click",e=>e.stopPropagation());
  box.querySelector(".si-x").addEventListener("click",()=>box.remove());
  box.querySelector(".si-go").addEventListener("click",()=>{box.remove();window.stCtl&&window.stCtl.play();});}

/* ---------- ② 🔬 teen: the investigation board ---------- */
function stBoard(s,P){const v=V(),lo=document.body.dataset.q==="lo",k=speedNow(),d=x=>x*k,tone=ST_TONE.teen,theme=ST_THEME[stSubj()]||"room";
  const ids=s.guests.concat(s.ids),cw=v?100:118,ch=v?96:112,hero=P.hero;
  const G=stGridPos(ids,s.levels,v,cw,ch,v?62:72,v?12:26,v?30:28,110),{W,pos}=G,H=G.H+(v?70:66);
  const ev={sub:[],chap:[],cue:[],show:{},stamp:[],focus:[],link:[],out:{},gray:{},pulse:{},gate:[]};ids.forEach(i=>{ev.out[i]=[];ev.gray[i]=[];ev.pulse[i]=[];});
  const L=stLinks(s);
  const sub=(t0,t1,x)=>ev.sub.push([t0,t1,VOICE(x)]),chap=(t,x)=>ev.chap.push([t,x]),cue=(t,n)=>ev.cue.push([t,n]);
  const tag={},kind={},q={};let T=0,n=0,files=1;
  const show=(id,t,tg,kd)=>{ev.show[id]=t;tag[id]=tg;kind[id]=kd;cue(t+d(0.45),"pick");};
  const look=(t,id)=>ev.focus.push([t,id]),stamp=(t0,t1,id,txt,cls)=>ev.stamp.push([t0,t1,id,txt,cls]);
  /* the case: the hero's card is pinned first */
  chap(0,tone.ch[0]);sub(0,d(3.4),tone.open(hero));show(hero,d(1.4),VOICE("القضية"),"hero");look(d(2.1),hero);T=d(3.5);
  if(!P.beats.some(b=>b.t!=="lone")&&stMean(s,hero)){sub(T,T+d(2.8),`${stQ(hero)}: ${stMean(s,hero)}`);T+=d(2.9);}
  let asked=false,found=false;
  P.beats.forEach(b=>{
    if(b.t==="ask"){const x=b.x;look(T,x);q[x]=T;ev.pulse[x].push(T+d(0.2));cue(T+d(0.2),"pop");
      sub(T,T+d(2.6),x===hero&&!asked?tone.problem(x):b.lead?tone.lead(x):b.again?tone.again(x):tone.ask(x));asked=true;T+=d(2.6);}
    else if(b.t==="call"){const as=b.as,x=b.b,ns=[],m=as.length-1;if(!found){chap(T,tone.ch[1]);found=true;}
      const ch=as.length===1&&ev.gate.length<3?stChoices(s,L,x,as[0]):null;if(ch)ev.gate.push([T-d(0.05),{q:`🖐️ ${VOICE("دورك يا محقق")}: ${stCase(x)}`,opts:ch}]);   /* just before: the line that tells the answer is not on yet */   /* 🆕 batch 39: the student finds the evidence */
      as.forEach((a,i)=>{n++;ns.push(n);show(a,T+d(i*0.3),`${VOICE("دليل")} ${stAr(n)}`,"ev");ev.link.push([T+d(0.8+i*0.3),a,x]);});look(T+d(0.2),as[0]);
      if(q[x]!=null){stamp(q[x],T+d(1.4+m*0.3),x,"؟","bd-q");delete q[x];}
      cue(T+d(0.8),"step");ev.pulse[x].push(T+d(1.6+m*0.3));
      sub(T,T+d(4.2+m*0.3),tone.found(ns,as,x,s.why));T+=d(4.4+m*0.3);}
    else if(b.t==="link"){look(T,b.b);ev.link.push([T+d(0.2),b.a,b.b]);cue(T+d(0.2),"step");ev.pulse[b.b].push(T+d(1));sub(T,T+d(3.2),tone.also(b.a,b.b));T+=d(3.3);}
    else if(b.t==="other"){files++;show(b.id,T,`${VOICE("ملف")} ${stAr(files)}`,"file");look(T+d(0.3),b.id);sub(T,T+d(2.8),tone.other(b.id));T+=d(3);}
    else if(b.t==="lone"){show(b.id,T,VOICE("معلومة"),"info");look(T+d(0.3),b.id);sub(T,T+d(3.2),tone.lone(b.id,stMean(s,b.id)));T+=d(3.3);}});
  Object.keys(q).forEach(x=>stamp(q[x],T,x,"؟","bd-q"));
  /* the test: the card everybody depends on is taken off the board… the strings go loose, the others get a ✕; it comes back */
  const B=P.base,hurt=P.hurt;
  if(hurt.length&&found){chap(T,tone.ch[2]);sub(T,T+d(2.4),tone.twist(B));look(T,B);cue(T+d(0.7),"flip");
    const gap=Math.min(0.5,2/hurt.length),end=T+d(4.6+hurt.length*gap);ev.out[B].push([T+d(0.7),end]);
    hurt.forEach((h,i)=>{const t=T+d(1.8+i*gap);ev.gray[h].push([t,end]);stamp(t,end,h,"✕","bd-x");cue(t,"bad");});
    sub(T+d(2.4),end,stLost(hurt,B,"❌"));sub(end,end+d(2.6),tone.back(B));cue(end+d(0.4),"good");hurt.forEach(h=>ev.pulse[h].push(end+d(0.6)));T=end+d(2.8);}
  /* solved: a green stamp on the case */
  chap(T,tone.ch[3]);look(T,hero);stamp(T+d(0.3),1e9,hero,"✔","bd-ok");cue(T+d(0.3),"tada");ids.forEach((id,i)=>ev.pulse[id].push(T+d(0.4+i*0.1)));
  sub(T,T+d(3.2),tone.end(hero));T+=d(3.3);
  if(P.chain.length>=2){sub(T,T+d(3.6),tone.moral(P.chain.map(stQ).join(" ← ")));T+=d(3.8);}
  const DUR=T;
  /* ---- the picture ---- */
  const gid=`bd${Math.random().toString(36).slice(2,7)}`,rot={};ids.forEach((id,i)=>{rot[id]=((id.length*37+i*53)%9)-4;});
  const pinY=id=>pos[id][1]-ch/2+8;
  /* a string: from the pin of the one that depends, to the pin of what it depends on — or, when that card is ABOVE it (the phone's rows),
     to the middle of its lower edge, so the string never runs over a card's words */
  const strPath=(a,b)=>{const up=pos[a][1]<pos[b][1]-ch*0.5&&Math.abs(pos[a][0]-pos[b][0])<cw*1.2,p=[pos[b][0],pinY(b)],q2=[pos[a][0],up?pos[a][1]+ch/2-1:pinY(a)],L=Math.hypot(q2[0]-p[0],q2[1]-p[1]),c=[(p[0]+q2[0])/2,(p[1]+q2[1])/2+16+L*0.1];   /* a string sags a little */
    const c1=[(p[0]+c[0])/2,(p[1]+c[1])/2],c2=[(c[0]+q2[0])/2,(c[1]+q2[1])/2],m=[(c1[0]+c2[0])/2,(c1[1]+c2[1])/2],f=x=>x.toFixed(1);   /* cut in two halves: the arrow sits in the middle */
    return `M${f(p[0])} ${f(p[1])} Q${f(c1[0])} ${f(c1[1])} ${f(m[0])} ${f(m[1])} Q${f(c2[0])} ${f(c2[1])} ${f(q2[0])} ${f(q2[1])}`;};
  const card=id=>{const L=lines(exName(id),v?11:13,2),two=L.length>1,art=two?(v?34:40):(v?40:46);
    return `<g class="sa st-tap bd-card bd-t-${kind[id]||"info"}" data-id="${id}" style="opacity:0"><g class="sa-b">
      <rect class="bd-shadow" x="${-cw/2+3}" y="${-ch/2+5}" width="${cw}" height="${ch}" rx="3"/><rect class="bd-paper" x="${-cw/2}" y="${-ch/2}" width="${cw}" height="${ch}" rx="3"/>
      <rect class="bd-band" x="${-cw/2}" y="${ch/2-20}" width="${cw}" height="20" rx="3"/><text class="bd-tag" y="${ch/2-6}" text-anchor="middle">${tag[id]||""}</text>
      <g class="bd-art">${stArt(id,art,two?-22:-14)}</g>
      ${L.map((x,i)=>`<text class="bd-name" y="${ch/2-27-(L.length-1-i)*15}" text-anchor="middle">${x}</text>`).join("")}
      <g class="bd-stamp" opacity="0" transform="rotate(-12)"><text y="14" text-anchor="middle"></text></g></g></g>`;};
  const lw=Math.min(W-40,s.title.length*9.5+64);
  const body=`<defs><pattern id="${gid}c" width="22" height="22" patternUnits="userSpaceOnUse"><rect width="22" height="22" fill="#C99C68"/><circle cx="4" cy="5" r="1.3" fill="#A8773F" opacity=".55"/><circle cx="14" cy="10" r="1.1" fill="#E4C08F" opacity=".8"/><circle cx="8" cy="17" r="1.5" fill="#996A38" opacity=".45"/><circle cx="18" cy="3" r=".9" fill="#EDD0A4" opacity=".9"/><circle cx="19" cy="18" r="1" fill="#A8773F" opacity=".5"/></pattern>
      <radialGradient id="${gid}v" cx=".5" cy=".45" r=".78"><stop offset=".6" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".3"/></radialGradient>
      <marker id="${gid}m" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto"><path d="M2 1.5 L8 5 L2 8.5" fill="none" stroke="#8E241D" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></marker></defs>
    <g class="st-bg bd-bg"><rect width="${W}" height="${H}" fill="${lo?"#C99C68":`url(#${gid}c)`}"/>${lo?"":`<rect width="${W}" height="${H}" fill="url(#${gid}v)"/>`}
      <rect x="4.5" y="4.5" width="${W-9}" height="${H-9}" rx="10" fill="none" stroke="#6E4524" stroke-width="9"/><rect x="9" y="9" width="${W-18}" height="${H-18}" rx="6" fill="none" stroke="rgba(0,0,0,.22)" stroke-width="2"/>
      <g transform="translate(${W/2} ${v?33:38}) rotate(-1.2)"><rect class="bd-label" x="${-lw/2}" y="-15" width="${lw}" height="30"/><rect class="bd-tape" x="${-lw/2-14}" y="-8" width="30" height="13" transform="rotate(-20 ${-lw/2} 0)"/><rect class="bd-tape" x="${lw/2-16}" y="-8" width="30" height="13" transform="rotate(18 ${lw/2} 0)"/><text class="bd-ltxt" y="6" text-anchor="middle">🗂️ ${s.title}</text></g></g>
    <g class="st-actors bd-cards">${ids.map(card).join("")}</g>
    <g class="st-links bd-strs">${s.edges.map(([a,b],i)=>`<path class="st-link bd-str" data-i="${i}" data-a="${a}" data-b="${b}" d="${strPath(a,b)}" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1" style="opacity:0"/>`).join("")}</g>
    <g class="bd-pins">${ids.map(id=>`<g class="bd-pin bd-p-${kind[id]||"info"}" data-id="${id}" transform="scale(0)"><circle r="6.5" class="bd-pinhead"/><circle r="2.2" cx="-1.8" cy="-1.8" fill="#fff" opacity=".75"/></g>`).join("")}</g>
    <g class="bd-lens" opacity="0"><path d="M11 11 L23 23" class="bd-handle"/><circle r="15" class="bd-glass"/></g>`;
  const svg=stShell({W,H,DUR,ev,kind:"story",look:"board",place:"board",theme,title:s.title,tt1:tone.tt,label:VOICE("حكاية الدرس"),body});
  return {svg,stepMs:1e9,story:{DUR},wire:root=>{
    const C={},PN={};root.querySelectorAll(".bd-card").forEach(g=>{C[g.dataset.id]={g,b:g.querySelector(".sa-b"),st:g.querySelector(".bd-stamp"),stT:g.querySelector(".bd-stamp text"),gr:null,sk:""};});
    root.querySelectorAll(".bd-pin").forEach(g=>{PN[g.dataset.id]=g;});
    const strs=[...root.querySelectorAll(".bd-str")],lens=root.querySelector(".bd-lens");
    const ease=u=>u<.5?2*u*u:1-Math.pow(-2*u+2,2)/2,eo=u=>1-Math.pow(1-u,3),clamp=(x,a,b)=>Math.max(a,Math.min(b,x)),inAny=(arr,t)=>arr.some(([a,b])=>t>=a&&t<b);
    const byT=(a,b)=>a[0]-b[0];ev.focus.sort(byT);
    stPlay(root,DUR,ev,k,t=>{
      ids.forEach(id=>{const c=C[id],t0=ev.show[id];let op=0,sc=1,dy=0,r=rot[id];
        if(t0!=null&&t>=t0){const u=clamp((t-t0)/d(0.55),0,1),e=eo(u);op=Math.min(1,u*2.2);sc=1.22-0.22*e;dy=-16*(1-e);r=rot[id]+9*(1-e);}   /* it is put on the board */
        for(const [o0,o1] of ev.out[id]){if(t>=o0&&t<o1+d(0.5)){const u=t<o1?clamp((t-o0)/d(0.5),0,1):1-clamp((t-o1)/d(0.5),0,1);dy+=30*eo(u);r+=14*u;op*=1-0.65*u;}}   /* unpinned: it slips down */
        for(const p0 of ev.pulse[id]){const u=(t-p0)/0.5;if(u>=0&&u<1)sc*=1+0.07*Math.sin(Math.PI*u);}
        c.g.style.opacity=op.toFixed(2);c.g.setAttribute("transform",`translate(${pos[id][0]} ${(pos[id][1]+dy).toFixed(1)})`);
        c.b.setAttribute("transform",`translate(0 ${-ch/2+8}) rotate(${r.toFixed(2)}) translate(0 ${ch/2-8}) scale(${sc.toFixed(3)})`);   /* it turns around its pin */
        const gr=inAny(ev.gray[id],t);if(gr!==c.gr){c.gr=gr;c.g.classList.toggle("st-gray",gr);}
        const sp=ev.stamp.filter(x=>x[2]===id&&t>=x[0]&&t<x[1]).pop(),key=sp?sp[3]+sp[4]:"";
        if(key!==c.sk){c.sk=key;c.st.setAttribute("class","bd-stamp "+(sp?sp[4]:""));c.stT.textContent=sp?sp[3]:"";}
        c.st.setAttribute("opacity",sp?clamp((t-sp[0])/0.25,0,1).toFixed(2):"0");
        const pu=t0==null?0:clamp((t-t0-d(0.4))/d(0.18),0,1);PN[id].setAttribute("transform",`translate(${pos[id][0]} ${pinY(id).toFixed(1)}) scale(${(inAny(ev.out[id],t)?0:pu).toFixed(2)})`);});
      ev.link.forEach(([t0,a,b])=>{const i=s.edges.findIndex(e=>e[0]===a&&e[1]===b),L=strs[i];if(!L)return;const o=clamp(1-(t-t0)/d(0.7),0,1);
        L.setAttribute("stroke-dashoffset",o.toFixed(3));L.style.opacity=o>=1?0:1;
        const sl=inAny(ev.out[a],t)||inAny(ev.out[b],t);if(sl!==L.__sl){L.__sl=sl;L.classList.toggle("bd-slack",sl);}
        const hd=o<0.05;if(hd!==L.__hd){L.__hd=hd;if(hd)L.setAttribute("marker-mid",`url(#${gid}m)`);else L.removeAttribute("marker-mid");}});
      /* the magnifier goes to the card we are looking at */
      const side=id=>pos[id][0]<W/2?1:-1,fs=ev.focus.filter(f=>f[0]<=t),at=id=>id&&pos[id]?[pos[id][0]+side(id)*(cw/2+12),pos[id][1]-ch*0.12]:null;   /* beside the card, on the side with room */
      if(!fs.length||!at(fs[fs.length-1][1]))lens.setAttribute("opacity","0");
      else{const cur=fs[fs.length-1],pc=at(cur[1]),pp=(fs.length>1&&at(fs[fs.length-2][1]))||pc,u=ease(clamp((t-cur[0])/d(0.6),0,1)),x=pp[0]+(pc[0]-pp[0])*u,y=pp[1]+(pc[1]-pp[1])*u;
        lens.setAttribute("opacity",clamp((t-fs[0][0])/0.4,0,1).toFixed(2));lens.setAttribute("transform",`translate(${x.toFixed(1)} ${y.toFixed(1)}) rotate(${lo?0:(-8+6*Math.sin(t*1.3)).toFixed(1)}) scale(${side(cur[1])} 1)`);}},{gate:(g,go)=>stAsk(root,g,go),tap:id=>stInfo(root,s,L,id)});}};}

/* ---------- ② 📐 senior: the documentary diagram that builds itself ---------- */
function stDoc(s,P){const v=V(),lo=document.body.dataset.q==="lo",k=speedNow(),d=x=>x*k,tone=ST_TONE.senior,theme=ST_THEME[stSubj()]||"room";
  const ids=s.guests.concat(s.ids),R=v?24:29,cw=v?104:140,ch=v?92:104,top=v?80:88,hero=P.hero;
  const G=stGridPos(ids,s.levels,v,cw,ch,top,v?8:20,v?16:18,170),{W,pos}=G,H=G.H+(v?70:64);
  const ev={sub:[],chap:[],cue:[],draw:{},idx:{},link:[],focus:[],cam:[],out:{},gray:{},glow:[],n:[],gate:[]};ids.forEach(i=>{ev.out[i]=[];ev.gray[i]=[];});
  const L=stLinks(s);
  const sub=(t0,t1,x)=>ev.sub.push([t0,t1,VOICE(x)]),chap=(t,x)=>ev.chap.push([t,x]),cue=(t,n)=>ev.cue.push([t,n]);
  const cx0=W/2,cy0=(top+G.H)/2,hh=(G.H-top)/2,zMax=v?1.25:1.4;let T=0,n=0;
  const draw=(id,t)=>{if(ev.draw[id]!=null)return;ev.draw[id]=t;ev.idx[id]=++n;ev.n.push([t,n]);cue(t,"pick");};
  const focus=(t,list)=>ev.focus.push([t,list]);
  /* the camera: closer to the part we talk about (never showing an empty side), back to the whole map between the parts */
  const camAt=(t,list)=>{const xs=list.map(i=>pos[i][0]),ys=list.map(i=>pos[i][1]),x0=Math.min(...xs),x1=Math.max(...xs),y0=Math.min(...ys),y1=Math.max(...ys);
    const z=Math.max(1,Math.min(zMax,(W*0.86)/(x1-x0+cw+40),(hh*2*0.9+40)/(y1-y0+ch+40)));
    const cx=Math.max(W/2/z,Math.min(W-W/2/z,(x0+x1)/2)),cy=Math.max(top+hh/z,Math.min(G.H-hh/z,(y0+y1)/2));ev.cam.push([t,cx,cy,z]);};
  const fit=t=>ev.cam.push([t,cx0,cy0,1]);
  chap(0,tone.ch[0]);sub(0,d(3.4),tone.open(hero));draw(hero,d(1.7));focus(d(1.7),[hero]);camAt(d(1.7),[hero]);T=d(3.6);
  if(!P.beats.some(b=>b.t!=="lone")&&stMean(s,hero)){sub(T,T+d(2.8),`${stQ(hero)}: ${stMean(s,hero)}`);T+=d(2.9);}
  let asked=false,traced=false;
  P.beats.forEach(b=>{
    if(b.t==="ask"){const x=b.x;focus(T,[x]);camAt(T,[x]);sub(T,T+d(2.6),x===hero&&!asked?tone.problem(x):b.lead?tone.lead(x):b.again?tone.again(x):tone.ask(x));asked=true;T+=d(2.6);}
    else if(b.t==="call"){const as=b.as,x=b.b,m=as.length-1;if(!traced){chap(T,tone.ch[1]);traced=true;}
      const ch=as.length===1&&ev.gate.length<3?stChoices(s,L,x,as[0]):null;if(ch)ev.gate.push([T-d(0.05),{q:`${VOICE("توقّع")}: ${stCase(x)}`,opts:ch}]);   /* 🆕 batch 39: predict before the arrow is drawn */
      focus(T,as.concat([x]));camAt(T,as.concat([x]));as.forEach((a,i)=>{draw(a,T+d(0.3+i*0.3));ev.link.push([T+d(1.0+i*0.3),a,x]);});sub(T,T+d(4.2+m*0.3),tone.found(null,as,x,s.why));T+=d(4.4+m*0.3);}
    else if(b.t==="link"){focus(T,[b.a,b.b]);camAt(T,[b.a,b.b]);ev.link.push([T+d(0.4),b.a,b.b]);sub(T,T+d(3.2),tone.also(b.a,b.b));T+=d(3.3);}
    else if(b.t==="other"){focus(T,[b.id]);camAt(T,[b.id]);draw(b.id,T+d(0.3));sub(T,T+d(2.8),tone.other(b.id));T+=d(3);}
    else if(b.t==="lone"){focus(T,[b.id]);camAt(T,[b.id]);draw(b.id,T+d(0.3));sub(T,T+d(3.2),tone.lone(b.id,stMean(s,b.id)));T+=d(3.3);}});
  focus(T,null);fit(T);
  /* the hypothesis: without the one everybody depends on, the others are marked (amber, dashed); it comes back */
  const B=P.base,hurt=P.hurt;
  if(hurt.length&&traced){chap(T,tone.ch[2]);const gap=Math.min(0.45,2/hurt.length),end=T+d(4.6+hurt.length*gap);sub(T,T+d(2.4),tone.twist(B));
    ev.out[B].push([T+d(0.6),end]);hurt.forEach((h,i)=>ev.gray[h].push([T+d(1.6+i*gap),end]));sub(T+d(2.4),end,stLost(hurt,B,""));sub(end,end+d(2.6),tone.back(B));T=end+d(2.8);}
  /* the conclusion: the whole map, the main chain lights up from the base to the question */
  chap(T,tone.ch[3]);focus(T,null);fit(T);P.chain.slice(1).forEach((x,i)=>ev.glow.push([T+d(0.4+i*0.45),P.chain[i],x]));
  sub(T,T+d(3.4),tone.end(hero));T+=d(3.5);
  if(P.chain.length>=2){sub(T,T+d(3.6),tone.moral(P.chain.map(stQ).join(" ← ")));T+=d(3.8);}
  const DUR=T;
  /* ---- the picture ---- */
  const gid=`sd${Math.random().toString(36).slice(2,7)}`,total=ids.length;
  const nodeSVG=id=>{const L=lines(exName(id),v?12:15,2),sc=id===hero?1.12:1;
    return `<g class="sa st-tap sd-node${id===hero?" sd-hero":""}" data-id="${id}" transform="translate(${pos[id][0]} ${pos[id][1]})" style="opacity:0"><g class="sa-b" transform="scale(${sc})">
      <circle class="sd-halo" r="${R+9}"/><circle class="sd-ring" r="${R}" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1" transform="rotate(-90)"/>
      <g class="sd-icon" opacity="0">${stArt(id,R*1.4,0)}</g>
      <g class="sd-name" opacity="0">${L.map((x,i)=>`<text y="${R+19+i*16}" text-anchor="middle">${x}</text>`).join("")}</g>
      <g class="sd-badge" opacity="0" transform="translate(${(R*0.78).toFixed(1)} ${(-R*0.78).toFixed(1)})"><circle r="9"/><text y="3.8" text-anchor="middle">${stAr(ev.idx[id]||0)}</text></g></g></g>`;};
  const linkSVG=([a,b],i)=>{const [p,q2]=edgeEnds(pos[b],pos[a],R+7),mx=(p[0]+q2[0])/2,my=(p[1]+q2[1])/2;
    return `<path class="st-link sd-link" data-i="${i}" data-a="${a}" data-b="${b}" d="M${p[0].toFixed(1)} ${p[1].toFixed(1)} L${q2[0].toFixed(1)} ${q2[1].toFixed(1)}" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1" style="opacity:0"/>${v?"":`<text class="sd-rel" data-i="${i}" x="${mx.toFixed(1)}" y="${(my-7).toFixed(1)}" text-anchor="middle" opacity="0">${ARROW_WORD()}</text>`}`;};
  const body=`<defs><linearGradient id="${gid}b" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#18262F"/><stop offset="1" stop-color="#0D161B"/></linearGradient>
      <pattern id="${gid}g" width="28" height="28" patternUnits="userSpaceOnUse"><path d="M28 0 H0 V28" fill="none" stroke="rgba(150,200,210,.07)" stroke-width="1"/></pattern>
      <radialGradient id="${gid}v" cx=".5" cy=".5" r=".72"><stop offset=".55" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".38"/></radialGradient>
      <marker id="${gid}h" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M1.5 1.5 L8.5 5 L1.5 8.5" fill="none" stroke="#A9CBD3" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></marker>
      <clipPath id="${gid}c"><rect x="0" y="${top-16}" width="${W}" height="${G.H-top+16}"/></clipPath></defs>
    <g class="st-bg sd-bg"><rect width="${W}" height="${H}" fill="url(#${gid}b)"/><rect width="${W}" height="${H}" fill="url(#${gid}g)"/>${lo?"":`<rect width="${W}" height="${H}" fill="url(#${gid}v)"/>`}<line class="sd-rule" x1="24" x2="${W-24}" y1="${top-24}" y2="${top-24}"/></g>
    <g class="sd-head"><text class="sd-q" x="${W/2}" y="${v?32:38}" text-anchor="middle">${stBold(VOICE(tone.open(hero)))}</text><text class="sd-n" x="${W/2}" y="${v?54:62}" text-anchor="middle"></text></g>
    <g clip-path="url(#${gid}c)"><g class="sd-cam"><g class="st-links sd-links">${s.edges.map(linkSVG).join("")}</g><g class="st-actors sd-nodes">${ids.map(nodeSVG).join("")}</g></g></g>`;
  const svg=stShell({W,H,DUR,ev,kind:"story",look:"doc",place:"doc",theme,title:s.title,tt1:tone.tt,label:VOICE("حكاية الدرس"),body});
  return {svg,stepMs:1e9,story:{DUR},wire:root=>{
    const N_={};root.querySelectorAll(".sd-node").forEach(g=>{N_[g.dataset.id]={g,ring:g.querySelector(".sd-ring"),icon:g.querySelector(".sd-icon"),name:g.querySelector(".sd-name"),badge:g.querySelector(".sd-badge"),halo:g.querySelector(".sd-halo"),cl:""};});
    const links=[...root.querySelectorAll(".sd-link")],rels=[...root.querySelectorAll(".sd-rel")],cam=root.querySelector(".sd-cam"),nEl=root.querySelector(".sd-n");
    const ease=u=>u<.5?2*u*u:1-Math.pow(-2*u+2,2)/2,clamp=(x,a,b)=>Math.max(a,Math.min(b,x)),inAny=(arr,t)=>arr.some(([a,b])=>t>=a&&t<b);
    const byT=(a,b)=>a[0]-b[0];ev.cam.sort(byT);ev.focus.sort(byT);let nTxt=null;
    stPlay(root,DUR,ev,k,t=>{
      /* the camera */
      let cx=cx0,cy=cy0,z=1;for(const [t0,x,y,zz] of ev.cam){if(t<t0)break;const u=ease(clamp((t-t0)/d(0.9),0,1));cx+=(x-cx)*u;cy+=(y-cy)*u;z+=(zz-z)*u;}
      cam.setAttribute("transform",`translate(${cx0} ${cy0}) scale(${z.toFixed(4)}) translate(${(-cx).toFixed(1)} ${(-cy).toFixed(1)})`);
      let fl=null;for(const f of ev.focus){if(f[0]<=t)fl=f[1];else break;}
      ids.forEach(id=>{const o=N_[id],t0=ev.draw[id];if(t0==null||t<t0){o.g.style.opacity="0";return;}o.g.style.opacity="1";
        const u=clamp((t-t0)/d(0.8),0,1);o.ring.setAttribute("stroke-dashoffset",(1-ease(u)).toFixed(3));   /* the circle draws itself */
        o.icon.setAttribute("opacity",clamp((t-t0-d(0.3))/d(0.4),0,1).toFixed(2));o.name.setAttribute("opacity",clamp((t-t0-d(0.5))/d(0.4),0,1).toFixed(2));o.badge.setAttribute("opacity",clamp((t-t0-d(0.7))/d(0.3),0,1).toFixed(2));
        const isNew=t-t0<d(2.2);o.halo.setAttribute("opacity",isNew&&!lo?(0.55*Math.sin(Math.PI*clamp((t-t0)/d(2.2),0,1))).toFixed(2):"0");
        const cl=[fl&&!fl.includes(id)?"sd-dim":"",inAny(ev.out[id],t)?"sd-off":"",inAny(ev.gray[id],t)?"sd-hurt":""].filter(Boolean).join(" ");
        if(cl!==o.cl){o.cl=cl;o.g.setAttribute("class",`sa st-tap sd-node${id===hero?" sd-hero":""} ${cl}`);}});
      ev.link.forEach(([t0,a,b])=>{const i=s.edges.findIndex(e=>e[0]===a&&e[1]===b),L=links[i];if(!L)return;const o=clamp(1-(t-t0)/d(0.8),0,1);
        L.setAttribute("stroke-dashoffset",o.toFixed(3));L.style.opacity=o>=1?0:1;
        const hd=o<0.05;if(hd!==L.__hd){L.__hd=hd;if(hd)L.setAttribute("marker-end",`url(#${gid}h)`);else L.removeAttribute("marker-end");}
        const on=ev.glow.some(([g0,ga,gb])=>t>=g0&&ga===a&&gb===b);
        const cl=["st-link","sd-link",fl&&!(fl.includes(a)&&fl.includes(b))?"sd-dim":"",inAny(ev.out[a],t)||inAny(ev.out[b],t)?"sd-off":"",on?"sd-on":""].filter(Boolean).join(" ");if(L.getAttribute("class")!==cl)L.setAttribute("class",cl);
        const rl=rels.find(r=>r.dataset.i===String(i));if(rl)rl.setAttribute("opacity",o>=1?"0":((1-o)*(fl&&!(fl.includes(a)&&fl.includes(b))?0.35:0.9)).toFixed(2));});
      let cnt=0;for(const [t0,c] of ev.n){if(t0<=t)cnt=c;else break;}const txt=cnt?`${VOICE("العناصر")}: ${stAr(cnt)} / ${stAr(total)}`:"";if(txt!==nTxt){nTxt=txt;nEl.textContent=txt;}},{gate:(g,go)=>stAsk(root,g,go),tap:id=>stInfo(root,s,L,id)});}};}

/* ---------- 🎬 the lesson's story: the order, then the age's way of showing it ---------- */
/* 🆕 batch 45 (Hareth: «لازم نزيد هياكل ثانية للحكاية»): the little ones and the explorers have THREE tales — the classic one (the hero
   alone, the others are called in), 🚶 the climb (from the bottom up) and 🎉 the gathering (everybody there, who helps whom). The lessons of a
   book take them in turn (lesson 1 the classic, lesson 2 the climb, lesson 3 the gathering, …): the same lesson always tells the same tale.
   (?tale=classic|journey|party in the address: one tale, for a check.) Same characters, same place, same moves, same twist and end. */
const ST_TALES=["classic","journey","party"];
const stTale=s=>{let q=null;try{q=new URLSearchParams(location.search).get("tale");}catch(e){}if(ST_TALES.includes(q))return q;
  const ls=(graph()||{}).lessons||[];let i=ls.findIndex(l=>storyCache[l.lesson_id]===s);if(i<0)i=Math.max(0,ls.indexOf(lesson()));return ST_TALES[i%ST_TALES.length];};
function sceneStory(s){const P=stPlan(s),st=stageNow();
  if(st==="teen")return stBoard(s,P);
  if(st==="senior")return stDoc(s,P);
  return stCast(s,P,stTale(s));}
SCENES.story=sceneStory;SNAME.story="🎬 حكاية الدرس";
window.stPlan=stPlan;   /* for the browser check: the order on made-up graphs */
