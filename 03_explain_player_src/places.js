/* ===== 🆕 batch 35 (Hareth: «من خلال المكان… درس الكيمياء بختار إله مكان مخصص… نحط بالمكان أدواته، أشجار بتتحرك… وشخصيات ورا بتتكلم
   بس ما إلها دخل… وتفاعلي») · PLACES =====
   Every lesson lives in a PLACE: a garden, a lab, space, a classroom… — drawn in SVG, behind EVERY scene of the lesson
   (softly, at the edges, so the characters in the middle stay clear) and fully behind the cartoons.
   · which place: the JSON can say it ("place": "lab" on the book or on a lesson); else it follows the subject;
   · the props move (trees sway, clouds drift, bubbles rise, stars twinkle…) and answer a tap (a wiggle + their own sound);
   · little background extras (a bird, a robot, an astronaut…) idle and sometimes say a word or an emoji — NEVER a fact of the lesson;
   · quieter for the older stages; still with the light quality («خفيفة») and «reduce motion».
   🆕 batch 36 (Hareth: «الخلفية… الشجر الطيور الشمس… تتحرك وتتفاعل… والجرافيك تبعها حسنه»): depth (gradients like the characters, soft shadows,
   a second hill, grass on the horizon), the sun has a face, and life36.js adds the living things and the taps.
   Rules: every class starts with «pl-» · moving parts are an inner <g> (the outer one holds the place's transform) · no .xnode / .bub. */
const PLACE_OF_SUBJECT={science:"garden",math:"classroom",physics:"space",chemistry:"lab",geography:"map",history:"desert",language:"notebook",general:"room"};
const PLACE_NAMES={garden:"حديقة",lab:"مختبر",space:"فضاء",classroom:"صف",desert:"صحرا",map:"خريطة",notebook:"دفتر",room:"غرفة",sea:"بحر",city:"مدينة",kitchen:"مطبخ",forest:"غابة"};
const PLACE_TRY=(()=>{try{return new URLSearchParams(location.search).get("place");}catch(e){return null;}})();   /* ?place=lab: try a place on the whole page */
function placeNow(){const l=(typeof lesson==="function")?lesson():null,g=(typeof graph==="function")?graph():null;
  const z=PLACE_TRY?null:plZoneNow(l);if(z)return z;                                     /* 🆕 batch 39: a concept's scenes live in ITS little world (zones.js) */
  const p=PLACE_TRY||(l&&l.place)||(g&&g.place)||PLACE_OF_SUBJECT[(g||{}).subject]||"room";return PLACE_NAMES[p]||plRecipeOf(p)?p:"room";}
/* 🆕 batch 39: the zone of the concept on the screen (lesson.zones, from the factory) · a place made from pieces (a recipe, from the data) */
function plZoneNow(l){try{if(!l||!l.zones||typeof pathOf!=="function"||typeof POS==="undefined")return null;const here=pathOf()[POS];if(!here||here.c<0)return null;
  const c=l.concepts[here.c],z=c&&l.zones[c.concept_id];return z&&(PLACE_NAMES[z]||plRecipeOf(z))?z:null;}catch(e){return null;}}
function plRecipeOf(p){const g=(typeof graph==="function")?graph():null;const r=g&&g.places&&g.places[p];return r&&typeof r==="object"?r:null;}
const PLI="#3b2a1e";
let plUid=0;
/* 🆕 batch 41 (Hareth: «الدودة طالعة بالسما والحجر طالع بالسما»): how high a piece reaches above where it stands (measured once, kept) —
   so a thing hung on the wall or flying (a shelf, a clock, an owl…) is never pushed out of the top of the picture */
const PL_TOP={};
function plTop(kind,t,arg){const key=kind+":"+t;if(PL_TOP[key]!=null)return PL_TOP[key];let v=60;
  try{const s=document.createElementNS(svgNS,"svg");s.setAttribute("style","position:fixed;left:0;top:0;width:0;height:0;overflow:hidden;visibility:hidden;pointer-events:none");   /* fixed + 0×0: it never makes the page scroll (an RTL page scrolls to the LEFT) */
    s.innerHTML=`<g>${kind==="x"?PLX[t]():PLP[t](arg)}</g>`;document.body.appendChild(s);const b=s.firstChild.getBBox();v=Math.max(0,-b.y);s.remove();}catch(e){}
  return PL_TOP[key]=v;}
/* a prop: the outer <g> puts it in its place, the inner one moves (CSS) */
const plAt=(type,x,y,sc,inner,anim,extra)=>`<g class="pl-prop${extra?" "+extra:""}" data-pl="${type}" transform="translate(${x.toFixed(1)} ${y.toFixed(1)}) scale(${sc.toFixed(3)})"><g class="pl-a pl-${anim||"still"}">${inner}</g></g>`;
const plEye=(x,y,r)=>`<g transform="translate(${x} ${y})"><g class="pl-blink"><ellipse rx="${r}" ry="${r*1.15}" fill="#fff" stroke="${PLI}" stroke-width="1.4"/><circle r="${r*0.55}" fill="${PLI}"/><circle cx="${r*0.22}" cy="${-r*0.3}" r="${r*0.2}" fill="#fff"/></g></g>`;
const plSmile=(x,y,w)=>`<path d="M${x-w} ${y} Q${x} ${y+w*0.9} ${x+w} ${y}" fill="none" stroke="${PLI}" stroke-width="1.6" stroke-linecap="round"/>`;
/* ---------- the props (drawn at 0,0 = where they stand; about 100 units tall at scale 1) ---------- */
const PLP={
  tree:c=>`<rect x="-7" y="-46" width="14" height="46" rx="5" fill="#9B6B3D" stroke="${PLI}" stroke-width="2"/><g stroke="${PLI}" stroke-width="2"><circle cx="0" cy="-70" r="30" fill="${c||"#5DBB63"}"/><circle cx="-24" cy="-56" r="20" fill="${c||"#5DBB63"}"/><circle cx="24" cy="-56" r="20" fill="${c||"#5DBB63"}"/></g><circle cx="-10" cy="-80" r="9" fill="#fff" opacity=".25"/><circle cx="12" cy="-62" r="4" fill="#E2504C"/><circle cx="-14" cy="-50" r="4" fill="#E2504C"/>`,
  pine:()=>`<rect x="-6" y="-24" width="12" height="24" fill="#8A5A30" stroke="${PLI}" stroke-width="2"/><path d="M0 -108 L30 -60 L14 -60 L36 -26 L-36 -26 L-14 -60 L-30 -60 Z" fill="#3E9E5A" stroke="${PLI}" stroke-width="2" stroke-linejoin="round"/>`,
  bush:()=>`<g stroke="${PLI}" stroke-width="2" fill="#6CC56F"><circle cx="-14" cy="-14" r="14"/><circle cx="12" cy="-16" r="16"/><circle cx="0" cy="-24" r="14"/></g><circle cx="-6" cy="-18" r="3" fill="#F5D547"/><circle cx="10" cy="-12" r="3" fill="#F28AA8"/>`,
  flower:c=>`<path d="M0 0 V-26" stroke="#3E9E5A" stroke-width="3"/><g transform="translate(0 -30)" stroke="${PLI}" stroke-width="1.5">${[0,72,144,216,288].map(a=>`<ellipse rx="5" ry="8" cy="-7" fill="${c||"#F28AA8"}" transform="rotate(${a})"/>`).join("")}<circle r="5" fill="#F5D547"/></g>`,
  grass:()=>`<path d="M-14 0 Q-12 -16 -8 -22 Q-7 -10 -4 0 Q-2 -20 2 -26 Q3 -10 6 0 Q8 -14 13 -18 Q11 -8 14 0 Z" fill="#7BCB6D"/>`,
  rock:()=>`<path d="M-22 0 Q-24 -16 -8 -20 Q6 -26 18 -14 Q26 -6 22 0 Z" fill="#B9B2A6" stroke="${PLI}" stroke-width="2"/>`,
  cloud:()=>`<g fill="#fff" stroke="#DCE7F2" stroke-width="2"><circle cx="-18" cy="-10" r="12"/><circle cx="0" cy="-16" r="16"/><circle cx="18" cy="-10" r="12"/><rect x="-30" y="-12" width="60" height="12" rx="6" stroke="none"/></g>`,
  sun:()=>`<circle class="pl-glow2" r="54" fill="url(#plSunGlow) #FFE9A0" opacity=".55"/><g class="pl-rays" stroke="#FFC93C" stroke-width="4" stroke-linecap="round">${[0,45,90,135,180,225,270,315].map(a=>`<line x1="${Math.cos(a*Math.PI/180)*28}" y1="${Math.sin(a*Math.PI/180)*28}" x2="${Math.cos(a*Math.PI/180)*38}" y2="${Math.sin(a*Math.PI/180)*38}"/>`).join("")}</g><circle r="22" fill="#FFD84D" stroke="#F2A93B" stroke-width="2"/><g class="pl-sunface" data-mood="happy"><g class="ch">${faceSVG(0,4,.62)}</g></g>`,   /* 🆕 batch 36: the sun has a face */
  flask:c=>`<path d="M-8 -46 V-30 L-24 -4 Q-26 0 -20 0 H20 Q26 0 24 -4 L8 -30 V-46 Z" fill="#EAF6FF" stroke="${PLI}" stroke-width="2" stroke-linejoin="round"/><path d="M-18 -10 L18 -10 L22 -3 Q22 0 18 0 H-18 Q-22 0 -22 -3 Z" fill="${c||"#7FD0A8"}" opacity=".9"/><rect x="-11" y="-50" width="22" height="6" rx="3" fill="#C9D6E2" stroke="${PLI}" stroke-width="2"/><g class="pl-bub"><circle cx="-6" cy="-14" r="3" fill="#fff" opacity=".8"/><circle cx="5" cy="-18" r="2.2" fill="#fff" opacity=".8"/><circle cx="0" cy="-24" r="1.8" fill="#fff" opacity=".8"/></g>`,
  tubes:()=>`<rect x="-30" y="-22" width="60" height="8" rx="3" fill="#C9A27A" stroke="${PLI}" stroke-width="2"/>${[-18,0,18].map((x,i)=>`<rect x="${x-5}" y="-46" width="10" height="40" rx="5" fill="#EAF6FF" stroke="${PLI}" stroke-width="1.6"/><rect x="${x-4}" y="-24" width="8" height="17" rx="4" fill="${["#F28AA8","#7FB7F2","#F5D547"][i]}"/>`).join("")}<rect x="-30" y="-4" width="60" height="4" fill="#C9A27A"/>`,
  burner:()=>`<rect x="-8" y="-22" width="16" height="22" rx="3" fill="#9AA5B1" stroke="${PLI}" stroke-width="2"/><g class="pl-flame"><path d="M0 -50 Q12 -36 6 -26 Q0 -20 -6 -26 Q-12 -36 0 -50 Z" fill="#FF9F43"/><path d="M0 -42 Q6 -34 3 -28 Q0 -25 -3 -28 Q-6 -34 0 -42 Z" fill="#FFE27A"/></g>`,
  planet:()=>`<circle r="26" fill="#F2A65A" stroke="${PLI}" stroke-width="2"/><path d="M-20 -8 Q0 -16 20 -8" fill="none" stroke="#D97E3B" stroke-width="3"/><path d="M-22 8 Q0 2 22 10" fill="none" stroke="#D97E3B" stroke-width="3"/><ellipse rx="44" ry="10" fill="none" stroke="#FFE27A" stroke-width="4" transform="rotate(-14)"/>`,
  star:()=>`<path d="M0 -10 L3 -3 L10 -3 L4 2 L6 9 L0 5 L-6 9 L-4 2 L-10 -3 L-3 -3 Z" fill="#FFE27A"/>`,
  rocket:()=>`<g transform="rotate(30)"><path d="M0 -50 Q14 -34 12 -6 H-12 Q-14 -34 0 -50 Z" fill="#F5F7FA" stroke="${PLI}" stroke-width="2"/><circle cy="-28" r="6" fill="#7FB7F2" stroke="${PLI}" stroke-width="2"/><path d="M-12 -14 L-20 0 L-12 -4 Z M12 -14 L20 0 L12 -4 Z" fill="#E2504C" stroke="${PLI}" stroke-width="1.6"/><g class="pl-flame"><path d="M-6 -4 Q0 14 6 -4 Z" fill="#FF9F43"/></g></g>`,
  board:()=>`<rect x="-70" y="-90" width="140" height="80" rx="6" fill="#2F5D50" stroke="#8A5A30" stroke-width="6"/><g fill="none" stroke="#EAF6E8" stroke-width="2.4" stroke-linecap="round" opacity=".9"><path d="M-54 -66 h18 M-45 -75 v18"/><path d="M-20 -62 l10 -10 l10 10"/><circle cx="30" cy="-66" r="9"/><path d="M-54 -34 h40"/><path d="M8 -38 l12 -12 l12 12 z"/></g><rect x="-30" y="-10" width="60" height="5" fill="#8A5A30"/>`,
  clock:()=>`<circle r="20" fill="#fff" stroke="${PLI}" stroke-width="3"/><g class="pl-hand"><line x1="0" y1="0" x2="0" y2="-14" stroke="${PLI}" stroke-width="2.5" stroke-linecap="round"/></g><line x1="0" y1="0" x2="9" y2="0" stroke="${PLI}" stroke-width="3" stroke-linecap="round"/><circle r="2.5" fill="#E2504C"/>`,
  books:()=>`<rect x="-24" y="-12" width="48" height="12" rx="2" fill="#E2504C" stroke="${PLI}" stroke-width="2"/><rect x="-20" y="-24" width="40" height="12" rx="2" fill="#7FB7F2" stroke="${PLI}" stroke-width="2"/><rect x="-22" y="-36" width="44" height="12" rx="2" fill="#F5D547" stroke="${PLI}" stroke-width="2"/>`,
  pyramid:()=>`<path d="M-60 0 L0 -70 L60 0 Z" fill="#E7C27D" stroke="#B58A45" stroke-width="2"/><path d="M0 -70 L60 0 L18 0 Z" fill="#D2A75E"/>`,
  palm:()=>`<path d="M0 0 Q-6 -40 4 -80" fill="none" stroke="#9B6B3D" stroke-width="9" stroke-linecap="round"/><g fill="#4FAE5B" stroke="${PLI}" stroke-width="1.6"><path d="M4 -80 Q-30 -96 -46 -74 Q-22 -82 4 -78 Z"/><path d="M4 -80 Q36 -98 50 -72 Q26 -84 4 -78 Z"/><path d="M4 -82 Q-6 -110 -30 -108 Q-8 -98 2 -80 Z"/><path d="M4 -82 Q22 -110 40 -100 Q20 -96 6 -80 Z"/></g>`,
  cactus:()=>`<path d="M-8 0 V-52 Q-8 -62 0 -62 Q8 -62 8 -52 V0 Z M8 -30 H16 V-44 Q16 -50 21 -50 Q26 -50 26 -44 V-26 Q26 -22 20 -22 H8 Z" fill="#5DBB63" stroke="${PLI}" stroke-width="2" stroke-linejoin="round"/>`,
  compass:()=>`<circle r="22" fill="#FFF7E6" stroke="${PLI}" stroke-width="2.5"/><g class="pl-needle"><path d="M0 -17 L5 0 L0 17 L-5 0 Z" fill="#E2504C" stroke="${PLI}" stroke-width="1.2"/><path d="M0 0 L5 0 L0 17 L-5 0 Z" fill="#9AA5B1"/></g><text y="-25" text-anchor="middle" font-size="9" font-weight="800" fill="${PLI}">N</text>`,
  boat:()=>`<path d="M-30 -12 H30 L20 0 H-20 Z" fill="#C9744B" stroke="${PLI}" stroke-width="2" stroke-linejoin="round"/><path d="M0 -12 V-52" stroke="${PLI}" stroke-width="2.5"/><path d="M2 -50 L26 -20 H2 Z" fill="#fff" stroke="${PLI}" stroke-width="2"/>`,
  waves:w=>`<path d="M${-w/2} 0 ${Array.from({length:Math.ceil(w/40)},(_,i)=>`q10 -8 20 0 t20 0`).join(" ")}" fill="none" stroke="#7FB7F2" stroke-width="3" stroke-linecap="round"/>`,
  mountain:()=>`<path d="M-50 0 L-10 -60 L10 -38 L24 -54 L56 0 Z" fill="#A9B8C9" stroke="#7F8FA3" stroke-width="2"/><path d="M-10 -60 L-20 -44 L-4 -46 L4 -40 L10 -38 Z" fill="#fff"/>`,
  pencil:()=>`<g transform="rotate(-30)"><rect x="-6" y="-60" width="12" height="48" fill="#F5D547" stroke="${PLI}" stroke-width="2"/><path d="M-6 -12 L0 0 L6 -12 Z" fill="#F2D3A0" stroke="${PLI}" stroke-width="2"/><rect x="-6" y="-66" width="12" height="7" rx="2" fill="#F28AA8" stroke="${PLI}" stroke-width="2"/></g>`,
  letter:t=>`<text text-anchor="middle" font-size="30" font-weight="900" fill="#7FB7F2" stroke="#fff" stroke-width="3" paint-order="stroke" font-family="Noto Kufi Arabic,sans-serif">${t}</text>`,
  window:()=>`<rect x="-36" y="-80" width="72" height="62" rx="6" fill="#BFE3FF" stroke="#8A5A30" stroke-width="5"/><path d="M0 -80 V-18 M-36 -49 H36" stroke="#8A5A30" stroke-width="4"/><g class="pl-drift"><circle cx="-16" cy="-62" r="7" fill="#fff"/><circle cx="-8" cy="-64" r="8" fill="#fff"/></g>`,
  lamp:()=>`<path d="M0 0 V-50" stroke="${PLI}" stroke-width="3"/><path d="M-16 -50 L-8 -74 H8 L16 -50 Z" fill="#F5D547" stroke="${PLI}" stroke-width="2" stroke-linejoin="round"/><ellipse class="pl-glow" cx="0" cy="-40" rx="30" ry="18" fill="#FFE27A" opacity=".25"/><rect x="-12" y="-4" width="24" height="4" rx="2" fill="${PLI}"/>`,
  pot:()=>`<path d="M-14 -16 H14 L10 0 H-10 Z" fill="#D97E3B" stroke="${PLI}" stroke-width="2"/><g class="pl-a pl-sway"><path d="M0 -16 Q-14 -34 -18 -46 Q-4 -38 0 -16 M0 -16 Q12 -36 20 -44 Q8 -30 0 -16 M0 -16 V-48" fill="#5DBB63" stroke="${PLI}" stroke-width="1.6"/></g>`,
  shelf:()=>`<rect x="-34" y="-50" width="68" height="6" fill="#9B6B3D" stroke="${PLI}" stroke-width="2"/>${[-26,-16,-6,6].map((x,i)=>`<rect x="${x}" y="${-74+i%2*4}" width="9" height="${24-i%2*4}" fill="${["#E2504C","#7FB7F2","#5DBB63","#F5D547"][i]}" stroke="${PLI}" stroke-width="1.4"/>`).join("")}<circle cx="22" cy="-58" r="7" fill="#C4A7E7" stroke="${PLI}" stroke-width="1.6"/>`,
  fish:c=>`<path d="M-16 0 Q0 -12 14 0 Q0 12 -16 0 Z M14 0 L24 -8 L24 8 Z" fill="${c||"#F5A97F"}" stroke="${PLI}" stroke-width="1.8" stroke-linejoin="round"/><circle cx="-8" cy="-2" r="2.2" fill="${PLI}"/>`,
  seaweed:()=>`<path d="M0 0 Q-10 -20 0 -40 Q10 -60 0 -80" fill="none" stroke="#3E9E5A" stroke-width="7" stroke-linecap="round"/>`,
  coral:()=>`<path d="M0 0 V-30 M0 -18 L-14 -34 M0 -22 L12 -40 M-14 -34 V-44 M12 -40 L18 -48" stroke="#F28AA8" stroke-width="7" stroke-linecap="round" fill="none"/>`,
  building:c=>`<rect x="-24" y="-110" width="48" height="110" fill="${c||"#B8C4D6"}" stroke="${PLI}" stroke-width="2"/>${[0,1,2,3,4].map(r=>[0,1].map(k=>`<rect x="${-14+k*16}" y="${-98+r*20}" width="10" height="12" fill="#FFE27A" opacity="${(r+k)%3?".95":".4"}"/>`).join("")).join("")}`,
  car:c=>`<path d="M-30 -10 Q-30 -22 -18 -22 L-10 -32 H12 L22 -22 Q30 -22 30 -10 Z" fill="${c||"#E2504C"}" stroke="${PLI}" stroke-width="2" stroke-linejoin="round"/><rect x="-6" y="-29" width="14" height="7" fill="#BFE3FF"/><circle cx="-16" cy="-8" r="7" fill="#3b3b3b" stroke="${PLI}" stroke-width="2"/><circle cx="16" cy="-8" r="7" fill="#3b3b3b" stroke="${PLI}" stroke-width="2"/>`,
  light:()=>`<rect x="-3" y="-60" width="6" height="60" fill="#7F8FA3"/><rect x="-10" y="-96" width="20" height="40" rx="5" fill="#3b3b3b"/><circle class="pl-red" cy="-86" r="6" fill="#E2504C"/><circle class="pl-green" cy="-66" r="6" fill="#4CB36E"/>`,
  potkit:()=>`<rect x="-22" y="-24" width="44" height="24" rx="6" fill="#9AA5B1" stroke="${PLI}" stroke-width="2"/><rect x="-26" y="-28" width="52" height="6" rx="3" fill="#7F8FA3" stroke="${PLI}" stroke-width="2"/><g class="pl-steam" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".8"><path d="M-8 -34 q-6 -8 0 -16 t0 -16"/><path d="M8 -34 q-6 -8 0 -16 t0 -16"/></g>`,
  fridge:()=>`<rect x="-22" y="-100" width="44" height="100" rx="6" fill="#F5F7FA" stroke="${PLI}" stroke-width="2"/><path d="M-22 -60 H22" stroke="${PLI}" stroke-width="2"/><rect x="12" y="-90" width="4" height="18" rx="2" fill="#9AA5B1"/><rect x="12" y="-50" width="4" height="18" rx="2" fill="#9AA5B1"/><circle cx="-8" cy="-80" r="5" fill="#F28AA8"/>`,
  mushroom:()=>`<rect x="-5" y="-14" width="10" height="14" rx="3" fill="#FFF3DC" stroke="${PLI}" stroke-width="1.6"/><path d="M-16 -12 Q-16 -30 0 -30 Q16 -30 16 -12 Z" fill="#E2504C" stroke="${PLI}" stroke-width="1.6"/><circle cx="-6" cy="-22" r="3" fill="#fff"/><circle cx="6" cy="-18" r="2.4" fill="#fff"/>`,
};
/* ---------- the background extras: they idle, and now and then say a word (never a fact) ---------- */
const PLX={
  bird:()=>`<ellipse cx="0" cy="-12" rx="14" ry="11" fill="#7FB7F2" stroke="${PLI}" stroke-width="1.8"/><path d="M12 -14 L20 -11 L12 -9 Z" fill="#F5A623" stroke="${PLI}" stroke-width="1.2"/>${plEye(4,-16,3.4)}<path d="M-6 -12 Q-12 -20 -16 -12" fill="#5C9BDB" stroke="${PLI}" stroke-width="1.4"/>`,
  robot:()=>`<rect x="-14" y="-34" width="28" height="22" rx="6" fill="#C9D6E2" stroke="${PLI}" stroke-width="1.8"/>${plEye(-5,-24,3.4)}${plEye(5,-24,3.4)}<rect x="-10" y="-12" width="20" height="12" rx="3" fill="#9AA5B1" stroke="${PLI}" stroke-width="1.8"/><path d="M0 -34 V-40" stroke="${PLI}" stroke-width="2"/><circle cy="-42" r="3" fill="#E2504C"/>`,
  astronaut:()=>`<circle cy="-26" r="14" fill="#F5F7FA" stroke="${PLI}" stroke-width="1.8"/><rect x="-9" y="-31" width="18" height="11" rx="5" fill="#2F3B52"/>${plEye(-4,-26,2.6)}${plEye(4,-26,2.6)}<rect x="-11" y="-14" width="22" height="14" rx="6" fill="#F5F7FA" stroke="${PLI}" stroke-width="1.8"/>`,
  kid:()=>`<circle cy="-30" r="12" fill="#F2C9A0" stroke="${PLI}" stroke-width="1.8"/><path d="M-12 -32 Q-10 -46 0 -44 Q10 -46 12 -32 Q4 -38 -12 -32 Z" fill="#5C3B23"/>${plEye(-4,-30,2.6)}${plEye(4,-30,2.6)}${plSmile(0,-24,3)}<rect x="-10" y="-18" width="20" height="18" rx="5" fill="#7FB7F2" stroke="${PLI}" stroke-width="1.8"/>`,
  camel:()=>`<path d="M-26 -18 Q-20 -40 -8 -26 Q0 -44 10 -26 Q22 -30 26 -40 L30 -40 Q30 -18 18 -14 L18 0 M-20 -14 V0 M-8 -14 V0 M8 -14 V0" fill="#D9A866" stroke="${PLI}" stroke-width="2" stroke-linecap="round"/>${plEye(28,-38,2.4)}`,
  owl:()=>`<ellipse cy="-18" rx="13" ry="16" fill="#B08968" stroke="${PLI}" stroke-width="1.8"/>${plEye(-5,-22,4)}${plEye(5,-22,4)}<path d="M-2 -16 L0 -12 L2 -16 Z" fill="#F5A623"/>`,
  cat:()=>`<ellipse cy="-12" rx="16" ry="12" fill="#F2B880" stroke="${PLI}" stroke-width="1.8"/><path d="M-12 -20 L-10 -32 L-3 -23 M12 -20 L10 -32 L3 -23" fill="#F2B880" stroke="${PLI}" stroke-width="1.8" stroke-linejoin="round"/>${plEye(-5,-15,2.8)}${plEye(5,-15,2.8)}<path d="M16 -8 Q28 -14 24 -26" fill="none" stroke="${PLI}" stroke-width="3" stroke-linecap="round"/>`,
  crab:()=>`<ellipse cy="-10" rx="16" ry="10" fill="#E2504C" stroke="${PLI}" stroke-width="1.8"/>${plEye(-5,-20,2.8)}${plEye(5,-20,2.8)}<path d="M-16 -12 Q-26 -20 -22 -28 M16 -12 Q26 -20 22 -28" fill="none" stroke="${PLI}" stroke-width="3" stroke-linecap="round"/>`,
  pigeon:()=>`<ellipse cy="-12" rx="13" ry="10" fill="#B8C4D6" stroke="${PLI}" stroke-width="1.8"/><circle cx="10" cy="-20" r="7" fill="#9AA5B1" stroke="${PLI}" stroke-width="1.6"/>${plEye(12,-21,2.2)}<path d="M17 -20 L22 -18 L17 -16 Z" fill="#F5A623"/>`,
  chef:()=>`<circle cy="-26" r="12" fill="#F2C9A0" stroke="${PLI}" stroke-width="1.8"/><path d="M-11 -34 Q-16 -46 -6 -46 Q0 -54 6 -46 Q16 -46 11 -34 Z" fill="#fff" stroke="${PLI}" stroke-width="1.6"/>${plEye(-4,-26,2.6)}${plEye(4,-26,2.6)}${plSmile(0,-20,3)}<rect x="-11" y="-14" width="22" height="14" rx="5" fill="#fff" stroke="${PLI}" stroke-width="1.8"/>`,
  snail:()=>`<path d="M-18 0 H14 Q20 0 20 -6 L22 -16" fill="#F2D3A0" stroke="${PLI}" stroke-width="1.8"/><circle cx="-2" cy="-12" r="11" fill="#E7A26A" stroke="${PLI}" stroke-width="1.8"/><path d="M-2 -12 m0 -5 a5 5 0 1 1 -5 5" fill="none" stroke="${PLI}" stroke-width="1.4"/>${plEye(22,-18,2.2)}`,
};
const PLX_SAY={bird:["🎵 تويت تويت","☀️ يوم حلو!","👋"],robot:["بيب بوب 🤖","🧪✨","👀"],astronaut:["👋 من الفضاء!","🚀","✨ واو!"],kid:["✏️","😄","🤔"],
  camel:["🐪 …","☀️ حر اليوم!"],owl:["هوو هوو 🦉","🌙"],cat:["مياو 😺","😴"],crab:["🦀 👋","🌊"],pigeon:["🕊️ كو كو","👋"],chef:["😋","🍲 ريحة طيبة!"],snail:["🐌 على مهلي…","😊"]};
/* ---------- the places: [background (cartoons only), props, extras] — x as a share of the width, standing on the ground ---------- */
function plScene(name,W,H,gy,full,lo){const u=++plUid,S=Math.max(0.55,Math.min(1.15,Math.min(W,H*1.4)/560));
  const sky=(a,b)=>`<defs><linearGradient id="plg${u}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="${a}"/><stop offset="1" stop-color="${b}"/></linearGradient></defs><rect class="pl-sky" width="${W}" height="${H}" fill="url(#plg${u})"/>`;
  const ground=(c,c2)=>`<rect class="pl-ground" x="0" y="${gy}" width="${W}" height="${H-gy+2}" fill="${c}"/>${c2?`<rect x="0" y="${gy}" width="${W}" height="4" fill="${c2}"/>`:""}`;
  const mid=fx=>!full&&fx>0.15&&fx<0.85;                                   /* behind a normal scene: only the edges (the middle belongs to the characters) */
  const up=(y,top,k)=>y>=gy?y:Math.min(gy,Math.max(y,top*k+4));         /* 🆕 batch 41: above the ground → inside the top of the picture */
  const P=(t,fx,dy,sc,arg,anim,extra)=>{if(mid(fx))return "";const k=(sc||1)*S*(full?1:0.85),sw=PL_SHADOW[t];   /* 🆕 batch 36: a soft shadow under what stands on the ground */
    const y=up(gy+(dy||0)*S,dy<0?plTop("p",t,arg):0,k);
    return (sw&&!(dy<-20)?`<ellipse class="pl-shadow" cx="${(fx*W).toFixed(1)}" cy="${(y+1).toFixed(1)}" rx="${(sw*k).toFixed(1)}" ry="${(sw*k*0.2).toFixed(1)}"/>`:"")+plAt(t,fx*W,y,k,PLP[t](arg),anim,extra);};
  const X=(t,fx,dy,sc)=>{if(mid(fx)){fx=fx<0.5?0.13:0.87;dy=Math.max(0,dy||0);}                 /* behind a normal scene: the extra steps aside, to the edge, on the ground */
    const k=(sc||1)*S*(full?1:0.85),y=up(gy+(dy||0)*S,dy<0?plTop("x",t):0,k);
    return `<g class="pl-x" data-pl="x-${t}" data-x="${t}" transform="translate(${(fx*W).toFixed(1)} ${y.toFixed(1)}) scale(${k.toFixed(3)})"><g class="pl-a pl-idle">${PLX[t]()}</g></g>`;};
  const skyY=fy=>Math.min(fy*H,Math.max(10*S,(gy-36*S)*Math.min(1,fy/0.3)));   /* 🆕 batch 41: a sky thing stays IN the sky (by the sky's height) */
  const sun=(fx,fy)=>plAt("sun",fx*W,skyY(fy),S*0.9,PLP.sun(),"spin");
  const cloud=(fx,fy,sc,k)=>plAt("cloud",fx*W,skyY(fy),(sc||1)*S,PLP.cloud(),"drift"+(k||""));
  const edge=f=>0.04+0.92*f;                                               /* 🆕 batch 41: small scattered things keep away from the edges */
  const stars=n=>Array.from({length:n},(_,i)=>plAt("star",edge(((i*137)%97)/97)*W,((i*71)%53)/53*Math.min(gy-20,H*0.6)+10,S*(0.5+(i%3)*0.25),PLP.star(),"twinkle"+(i%3))).join("");
  const res=plSwitch();res[1]+=plLife(name,W,H,gy,full,S);return res;                     /* 🆕 batch 36: birds, butterflies, falling leaves… (life36.js) */
  function plSwitch(){switch(name){
    case "garden":return [full?sky("#9FD8FF","#E8F7FF"):"",
      (full?sun(0.1,0.15)+cloud(0.38,0.12)+cloud(0.72,0.2,0.8,"2"):plAt("sun",W*0.95,H*0.1,S*0.55,PLP.sun(),"spin")+cloud(0.5,0.08,0.7))
      +(full?`<path class="pl-far pl-far2" d="M0 ${gy-26*S} Q${W*0.18} ${gy-78*S} ${W*0.4} ${gy-40*S} T${W*0.78} ${gy-56*S} T${W} ${gy-34*S} V${gy} H0 Z" fill="#CFEFC0"/>`:"")
      +`<path class="pl-far" d="M0 ${gy} Q${W*0.25} ${gy-50*S} ${W*0.5} ${gy-10*S} T${W} ${gy-20*S} V${H} H0 Z" fill="#BDE7A6"/>`+ground("#8ED081","#7BC46F")+plTufts(W,gy,S,"#6DBE63")
      +P("tree",0.07,0,1,null,"sway")+P("bush",0.2,0,0.8)+P("flower",0.28,0,0.9,"#F28AA8","sway")+P("grass",0.4,0,1)+P("grass",0.62,0,0.8)
      +P("flower",0.74,0,0.8,"#F5D547","sway")+P("tree",0.93,0,0.9,"#7CC96F","sway2")+P("rock",0.84,0,0.7),
      X("bird",0.08,-108*1.0,0.9)+X("snail",0.32,0,0.7)];
    case "lab":return [full?sky("#EEF3F8","#DCE6EF"):"",
      `<g class="pl-far"><rect x="0" y="${gy-90*S}" width="${W}" height="${90*S}" fill="#E4ECF4"/>${Array.from({length:Math.ceil(W/40)},(_,i)=>`<path d="M${i*40} ${gy-90*S} V${gy}" stroke="#D3DEE9" stroke-width="2"/>`).join("")}</g>`
      +ground("#CFD8E2","#B8C4D0")+`<rect x="0" y="${gy-4}" width="${W}" height="8" fill="#9AA5B1"/>`
      +P("flask",0.07,-4,1,"#7FD0A8","bubble")+P("tubes",0.19,-4,0.9)+P("burner",0.3,-4,0.9,null,"still")+P("flask",0.78,-4,0.8,"#F28AA8","bubble2")+P("shelf",0.92,-4,0.9),
      X("robot",0.62,-4,0.85)];
    case "space":return [full?sky("#1C2747","#2E3F6E"):`<rect class="pl-sky pl-night" width="${W}" height="${H}" fill="#24315A" opacity=".1"/>`,
      stars(full?18:10)+plAt("planet",W*0.86,skyY(0.2),S*0.9,PLP.planet(),"spin-slow")+plAt("rocket",W*0.12,skyY(0.24),S*0.8,PLP.rocket(),"bob")
      +(full?`<path class="pl-far" d="M0 ${gy} Q${W*0.5} ${gy-40*S} ${W} ${gy} V${H} H0 Z" fill="#8B93A8"/>`:"")+ground(full?"#9AA2B6":"#C9D0DD","#B1B8C9")
      +P("rock",0.18,0,0.8)+P("rock",0.7,0,0.6),
      X("astronaut",0.92,-40,0.9)];
    case "classroom":return [full?sky("#FFF7EA","#FDEFD8"):"",
      (full?plAt("board",W*0.5,gy-18*S,S*1.2,PLP.board(),"still","pl-far"):"")+plAt("clock",W*0.12,up(gy-120*S,plTop("p","clock"),S*0.9),S*0.9,PLP.clock(),"still")
      +ground("#E7C9A3","#D8B58A")+P("books",0.88,0,0.9)+P("pot",0.06,0,1),
      X("kid",0.8,0,0.9)];
    case "desert":return [full?sky("#FFD9A0","#FFF1D6"):"",
      (full?sun(0.84,0.16):"")+P("pyramid",0.7,0,full?1.2:0.9,null,"still","pl-far")+P("pyramid",0.86,0,full?0.8:0.6,null,"still","pl-far")
      +`<path class="pl-far" d="M0 ${gy} Q${W*0.3} ${gy-24*S} ${W*0.6} ${gy-6*S} T${W} ${gy-12*S} V${H} H0 Z" fill="#F2D9A6"/>`+ground("#EDCB8A","#E0B970")
      +P("palm",0.08,0,1,null,"sway")+P("cactus",0.3,0,0.7)+P("rock",0.52,0,0.6),
      X("camel",0.2,0,0.9)];
    case "map":return [full?sky("#CDEBFF","#EAF6FF"):"",
      plAt("compass",W*0.9,skyY(0.16),S,PLP.compass(),"still")+P("mountain",0.12,0,1,null,"still","pl-far")+P("mountain",0.24,0,0.7,null,"still","pl-far")
      +ground("#BFE0F5")+plAt("waves",W*0.5,gy+14*S,S,PLP.waves(W*1.2/S),"wave")+(full?plAt("boat",W*0.7,gy+6*S,S*0.9,PLP.boat(),"bob")
      +plAt("fish",W*0.4,gy+30*S,S*0.8,PLP.fish("#F5A97F"),"swim"):plAt("boat",W*0.93,gy+6*S,S*0.7,PLP.boat(),"bob")),
      X("crab",0.9,24,0.8)];
    case "notebook":return [`<rect class="pl-sky" width="${W}" height="${H}" fill="#FFFDF5" opacity="${full?1:0}"/>${Array.from({length:Math.ceil(H/26)},(_,i)=>`<path class="pl-far" d="M0 ${i*26+20} H${W}" stroke="#D5E6F7" stroke-width="1.5"/>`).join("")}<path class="pl-far" d="M${W-34} 0 V${H}" stroke="#F4B6B6" stroke-width="2"/>`,
      plAt("pencil",W*0.9,gy,S,PLP.pencil(),"wiggle")+["أ","ب","ت","ج"].map((t,i)=>plAt("letter",W*(0.06+i*0.05),H*(0.18+(i%2)*0.1),S*0.8,PLP.letter(t),"float"+(i%3))).join(""),
      X("owl",0.08,0,0.8)];
    case "sea":return [full?sky("#BFE8FF","#5BB4E5"):"",
      plAt("waves",W*0.5,gy-60*S,S,PLP.waves(W*1.2/S),"wave")+ground("#F4DFA8","#E8CB82")+P("seaweed",0.06,0,1,null,"sway")+P("coral",0.18,0,0.9)+P("seaweed",0.9,0,0.8,null,"sway2")+P("coral",0.8,0,0.7)
      +(full?plAt("fish",W*0.3,gy-40*S,S*0.9,PLP.fish("#F5A97F"),"swim")+plAt("fish",W*0.65,gy-80*S,S*0.7,PLP.fish("#9CCFD8"),"swim2"):""),
      X("crab",0.5,0,0.8)];
    case "city":return [full?sky("#CFE7FF","#F2F7FF"):"",
      P("building",0.05,0,1,"#B8C4D6","still","pl-far")+P("building",0.15,0,0.8,"#C9B8D6","still","pl-far")+P("building",0.86,0,1.1,"#D6C4B8","still","pl-far")+P("building",0.95,0,0.7,"#B8D6C9","still","pl-far")
      +ground("#A9B1BC","#8E97A3")+`<path d="M0 ${gy+14*S} H${W}" stroke="#fff" stroke-width="3" stroke-dasharray="18 14" opacity=".8"/>`+P("light",0.26,0,0.8)
      +plAt("car",0,gy+22*S,S*0.8,PLP.car("#E2504C"),"drive"),
      X("pigeon",0.74,0,0.8)];
    case "kitchen":return [full?sky("#FFF6EC","#FDEBD8"):"",
      `<g class="pl-far">${Array.from({length:Math.ceil(W/30)},(_,i)=>`<rect x="${i*30}" y="${gy-70*S}" width="28" height="28" fill="#fff" stroke="#EADFD2"/>`).join("")}</g>`+ground("#E9D3B6","#D9BE98")
      +P("fridge",0.07,0,1)+P("potkit",0.86,0,1,null,"still")+P("pot",0.95,0,0.8),
      X("chef",0.2,0,0.9)];
    case "forest":return [full?sky("#BFE6C8","#E9F7EC"):"",
      P("pine",0.04,0,1.1,null,"sway","pl-far")+P("pine",0.14,0,0.8,null,"sway2","pl-far")+P("pine",0.9,0,1,null,"sway")+P("pine",0.98,0,0.7,null,"sway2")+ground("#7FBF77","#6AAE64")+plTufts(W,gy,S,"#5FA95A")
      +P("mushroom",0.24,0,0.9)+P("mushroom",0.78,0,0.7)+P("bush",0.66,0,0.7),
      X("owl",0.14,-plTop("p","pine")*0.8*(full?1:0.85)+3,0.75)+X("snail",0.42,0,0.6)];   /* 🆕 batch 41: the owl PERCHES on the small pine's tip (it floated in the air) */
    default:if(typeof PL_ZONE!=="undefined"&&PL_ZONE[name])return PL_ZONE[name]({sky,ground,P,X,sun,cloud,stars,W,H,gy,S,full,lo,u,skyY,up,edge});   /* 🆕 batch 39: a concept's little world */
      if(plRecipeOf(name))return plRecipe(plRecipeOf(name),{sky,ground,P,X,sun,cloud,stars,W,H,gy,S,full,lo,u});                       /* 🆕 batch 39: a place made from pieces (data) */
      return [full?sky("#EAF2FB","#F7FAFD"):"",                                 /* room */
      plAt("window",W*0.84,gy-20*S,S,PLP.window(),"still")+P("shelf",0.14,-110,0.9)+ground("#E6D5C0","#D8C2A6")+P("lamp",0.06,0,1,null,"still")+P("pot",0.94,0,1),
      X("cat",0.24,0,0.9)];}}}
/* 🆕 batch 39: a place RECIPE → the picture, from the same pieces: {sky:[top,bottom], ground:[ground,edge], far:"hills"|"wall"|"tiles"|"",
   farColor, skyItems:["sun","clouds","stars"], props:[[piece, x 0..1, dy, scale, colour, motion]], extras:[[extra, x 0..1, dy, scale]]}.
   Unknown pieces are skipped (the library is checked when a recipe is saved: place_library.py). */
function plRecipe(r,{sky,ground,P,X,sun,cloud,stars,W,H,gy,S,full,lo}){const sk=r.sky||["#EAF2FB","#F7FAFD"],gr=r.ground||["#E6D5C0","#D8C2A6"],fc=r.farColor||"#E4ECF4";
  const far=r.far==="hills"?`<path class="pl-far" d="M0 ${gy} Q${W*0.25} ${gy-50*S} ${W*0.5} ${gy-10*S} T${W} ${gy-20*S} V${H} H0 Z" fill="${fc}"/>`
    :r.far==="wall"?`<g class="pl-far"><rect x="0" y="${gy-90*S}" width="${W}" height="${90*S}" fill="${fc}"/></g>`
    :r.far==="tiles"?`<g class="pl-far">${Array.from({length:Math.ceil(W/30)},(_,i)=>`<rect x="${i*30}" y="${gy-70*S}" width="28" height="28" fill="#fff" stroke="${fc}"/>`).join("")}</g>`:"";
  const items=(r.skyItems||[]).map(k=>k==="sun"?(full?sun(0.86,0.15):""):k==="clouds"?(full?cloud(0.3,0.12)+cloud(0.7,0.2,0.8,"2"):""):k==="stars"?stars(full?14:8):"").join("");
  const props=(r.props||[]).filter(p=>Array.isArray(p)&&PLP[p[0]]).map(([t,fx,dy,sc,arg,anim])=>P(t,+fx||0,+dy||0,+sc||1,arg||null,anim||"still")).join("");
  const extras=(r.extras||[]).filter(x=>Array.isArray(x)&&PLX[x[0]]).map(([t,fx,dy,sc])=>X(t,+fx||0,+dy||0,+sc||1)).join("");
  return [full?sky(sk[0],sk[1]):"",items+far+ground(gr[0],gr[1])+props,extras];}
/* the place as SVG for a picture of W×H (gy = where the ground is). full = behind a cartoon · soft = behind any other scene */
function placeSVG(name,W,H,o){o=o||{};const gy=o.floor||Math.round(H*0.86),full=!!o.full,lo=!!o.lo;const [bg,props,extras]=plScene(name,W,H,gy,full,lo);
  return `<g class="pl pl-${name}${full?" pl-full":" pl-soft"}" data-place="${name}" data-w="${W}" data-h="${H}" data-gy="${gy}" aria-hidden="true"><g class="pl-bg">${bg}</g><g class="pl-near"><g class="pl-props">${props}</g><g class="pl-extras">${extras}</g></g></g>`;}
/* put the lesson's place behind a scene (not where the scene already draws its own world) */
const PLACE_SKIP={world:1,lens:1,play:1,story:1,cstory:1,custom:1};
function placeInto(root,kind){if(!root||PLACE_SKIP[kind]||root.querySelector(".pl"))return;const vb=root.viewBox.baseVal;if(!vb||!vb.width)return;
  const g=document.createElementNS("http://www.w3.org/2000/svg","g");g.innerHTML=placeSVG(placeNow(),vb.width,vb.height,{lo:document.body.dataset.q==="lo"});
  const pl=g.firstElementChild;pl.setAttribute("transform",`translate(${vb.x} ${vb.y})`);const defs=root.querySelector(":scope > defs");
  root.insertBefore(pl,defs?defs.nextSibling:root.firstChild);
  if(typeof shadeInto==="function")shadeInto(pl.querySelector(".pl-near"),grown());}   /* 🆕 batch 36: the props get the same depth as the characters */
/* tap a prop → it wiggles and makes its sound · tap an extra → it hops and says something (not a fact) */
/* the sounds come from the age's own sound set (sound.js): soft for the big ones, playful for the little ones */
const PL_SOUND={tree:"flip",pine:"flip",bush:"flip",flower:"pop",flask:"sparkle",tubes:"sparkle",burner:"step",planet:"bloom",rocket:"bloom",star:"ding",board:"step",clock:"step",
  pyramid:"pop",palm:"flip",compass:"step",boat:"pop",waves:"pop",fish:"pop",pencil:"step",letter:"pop",window:"pop",lamp:"ding",pot:"pop",car:"pop",light:"step",potkit:"sparkle",mushroom:"pop",seaweed:"flip",coral:"pop",cloud:"flip",sun:"ding",cactus:"pop",rock:"step",grass:"flip",fridge:"step",building:"step",mountain:"step",shelf:"step",books:"step"};
const PLX_SOUND={};                                                       /* every extra: the little giggle of the characters */
function plSay(x,txt,ms){const root=x.ownerSVGElement;if(!root)return;const old=x.querySelector(".pl-say");if(old)old.remove();
  const w=Math.max(34,[...txt].length*8+18),g=document.createElementNS("http://www.w3.org/2000/svg","g");g.setAttribute("class","pl-say");g.setAttribute("transform","translate(0 -58)");
  g.innerHTML=`<rect x="${-w/2}" y="-14" width="${w}" height="24" rx="12"/><path d="M-5 9 L0 16 L5 9 Z"/><text y="4" text-anchor="middle"></text>`;g.querySelector("text").textContent=txt;x.appendChild(g);
  setTimeout(()=>{if(g.isConnected)g.remove();},ms||1800);}
document.addEventListener("pointerdown",e=>{const t=e.target.closest&&e.target.closest(".pl [data-pl]");if(!t)return;
  const a=t.querySelector(".pl-a");if(a){a.classList.remove("pl-poke");void a.getBoundingClientRect();a.classList.add("pl-poke");setTimeout(()=>a.classList.remove("pl-poke"),650);}
  const x=t.dataset.x;if(x){const says=PLX_SAY[x]||["👋"];plSay(t,grown()?"👋":says[Math.floor(Math.random()*says.length)]);sfx(PLX_SOUND[x]||"giggle");}
  else sfx(PL_SOUND[t.dataset.pl]||"pop");
  if(typeof plTapFx==="function")plTapFx(t);});                              /* 🆕 batch 36: leaves fall, the cloud rains, the rocket takes off… */
/* the extras chat by themselves now and then (the little ones' places only, at good quality, not with «reduce motion») */
setInterval(()=>{if(reduce||document.hidden||document.body.dataset.q==="lo"||grown())return;const xs=[...document.querySelectorAll("#xs .pl-x")];if(!xs.length)return;
  if(Math.random()<0.55){const x=xs[Math.floor(Math.random()*xs.length)],says=PLX_SAY[x.dataset.x]||["👋"];plSay(x,says[Math.floor(Math.random()*says.length)],1700);}},5200);
