/* ======================= 🆕 batch 39 · ZONES + PLACES FROM PIECES («ليغو الأماكن») =======================
   Hareth: «الخلفيات… لازم يكون في خلفيات مناسبة لكل درس ولكل مفهوم ولكل مادة» + «المادة الغريبة… مكان غرفة بدل مطبخ».
   · every LESSON has its place (the JSON's "place", else picked by the factory from the lesson's words: places_picker.py);
   · every CONCEPT can have its own little world (a ZONE) behind its scenes and its cartoon: the root → under the ground,
     the nucleus → inside the cell, the electron → the world of atoms, the water → the rainy sky, the speed → the road of motion…
     (lesson.zones = {concept: zone}, picked by the factory from the concept's words; no zone → the lesson's place);
   · a PLACE RECIPE (data, not code): {sky, ground, far, props, extras, skyItems} built from the same pieces (PLP / PLX).
     The library of recipes grows as DATA (place_library.py: today a file, tomorrow the database; later the model adds new ones,
     always from our pieces and always checked) — the code stays the same size.
   Like the places: soft behind a normal scene (only the edges, the middle belongs to the characters), full behind a cartoon;
   the pieces move (CSS) and answer a tap (places.js / life36.js). No .xnode, no fact of the lesson, every class starts with «pl-». */
Object.assign(PLACE_NAMES,{underground:"تحت الأرض",cell:"جوّا الخلية",atoms:"عالم الذرات",sky:"السما",motion:"طريق الحركة",numbers:"عالم الأرقام",
  library:"المكتبة",ancient:"أرض قديمة",machine:"ورشة الطاقة"});
/* ---------- the new pieces (drawn at 0,0 = where they stand; about 100 units tall at scale 1) ---------- */
Object.assign(PLP,{
  worm:()=>`<path d="M-22 -4 q6 -10 12 0 t12 0 t12 0" fill="none" stroke="#E8919B" stroke-width="7" stroke-linecap="round"/><path d="M-22 -4 q6 -10 12 0 t12 0 t12 0" fill="none" stroke="${PLI}" stroke-width="1.2" stroke-dasharray="1 5"/><circle cx="14" cy="-6" r="1.6" fill="${PLI}"/>`,
  pebble:c=>`<ellipse cx="0" cy="-6" rx="11" ry="7" fill="${c||"#A79C8E"}" stroke="${PLI}" stroke-width="1.6"/><ellipse cx="-3" cy="-8" rx="4" ry="2" fill="#fff" opacity=".35"/>`,
  roots:()=>`<path d="M0 0 C-4 20 6 34 -2 56 M0 0 C6 18 18 26 16 48 M0 0 C-10 14 -22 22 -24 40 M-2 56 l-6 10 M16 48 l6 10" fill="none" stroke="#9B6B3D" stroke-width="3" stroke-linecap="round"/>`,
  mito:()=>`<ellipse rx="22" ry="12" fill="#F7A889" stroke="${PLI}" stroke-width="1.8"/><path d="M-16 0 q4 -8 8 0 t8 0 t8 0 t8 0" fill="none" stroke="#B5462B" stroke-width="2"/>`,
  vesicle:c=>`<circle r="9" fill="${c||"#BFE6D6"}" stroke="${PLI}" stroke-width="1.4"/><circle cx="-3" cy="-3" r="2.4" fill="#fff" opacity=".6"/>`,
  er:()=>`<path d="M-30 0 q8 -12 15 0 t15 0 t15 0 t15 0" fill="none" stroke="#B9A2F0" stroke-width="5" stroke-linecap="round"/><path d="M-30 10 q8 -12 15 0 t15 0 t15 0 t15 0" fill="none" stroke="#C9B6F5" stroke-width="4" stroke-linecap="round"/>`,
  atom:c=>`<g class="pl-orbit"><ellipse rx="30" ry="11" fill="none" stroke="${c||"#7FD6C9"}" stroke-width="1.6"/><circle cx="30" cy="0" r="3.2" fill="#FFE27A"/></g><g class="pl-orbit pl-orbit2"><ellipse rx="30" ry="11" fill="none" stroke="${c||"#7FD6C9"}" stroke-width="1.6" transform="rotate(60)"/><circle cx="15" cy="9.5" r="3.2" fill="#FFE27A" transform="rotate(60)"/></g><circle r="7" fill="#F28AA8" stroke="${PLI}" stroke-width="1.4"/><circle cx="-2" cy="-2" r="2" fill="#fff" opacity=".6"/>`,
  particle:c=>`<circle r="5" fill="${c||"#9CCFD8"}" opacity=".85"/><circle cx="-1.5" cy="-1.5" r="1.4" fill="#fff" opacity=".7"/>`,
  raincloud:()=>`<g stroke="${PLI}" stroke-width="2" fill="#E6EDF5"><circle cx="-16" cy="-6" r="13"/><circle cx="4" cy="-14" r="17"/><circle cx="22" cy="-6" r="12"/></g><rect x="-28" y="-6" width="60" height="12" rx="6" fill="#E6EDF5"/>${[-18,-4,10,24].map((x,i)=>`<path class="pl-rain pl-rain${i%3}" d="M${x} 12 q-2 5 0 8 q2 -3 0 -8Z" fill="#62A8EE"/>`).join("")}`,
  rainbow:()=>`${["#F28AA8","#F5B85A","#F5D547","#7BD389","#6CB8FF"].map((c,i)=>`<path d="M${-60+i*7} 0 A${60-i*7} ${60-i*7} 0 0 1 ${60-i*7} 0" fill="none" stroke="${c}" stroke-width="7" opacity=".55"/>`).join("")}`,
  ball:c=>`<g class="pl-rollspin"><circle cy="-12" r="12" fill="${c||"#F2B33D"}" stroke="${PLI}" stroke-width="2"/><path d="M-12 -12 H12 M0 -24 V0" stroke="${PLI}" stroke-width="1.4" opacity=".45"/></g><path d="M-30 -14 h-12 M-28 -8 h-18 M-30 -2 h-10" stroke="#9AA5B1" stroke-width="2" stroke-linecap="round" opacity=".7"/>`,
  ruler:n=>`<rect x="-60" y="-12" width="120" height="12" rx="2" fill="#F5D88A" stroke="${PLI}" stroke-width="1.6"/>${Array.from({length:13},(_,i)=>`<path d="M${-60+i*10} -12 v${i%5===0?7:4}" stroke="${PLI}" stroke-width="1.2"/>`).join("")}`,
  flag:c=>`<path d="M0 0 V-70" stroke="${PLI}" stroke-width="3"/><path d="M0 -70 L26 -62 L0 -54Z" fill="${c||"#E2504C"}" stroke="${PLI}" stroke-width="1.6"/>`,
  sym:t=>`<text text-anchor="middle" y="-6" font-size="30" font-weight="800" fill="#4F7BA6" opacity=".6" font-family="system-ui,sans-serif" direction="ltr">${t}</text>`,
  numline:()=>`<path d="M-120 -8 H120" stroke="${PLI}" stroke-width="2.4" marker-end="url(#xhead)"/>${Array.from({length:9},(_,i)=>`<path d="M${-96+i*24} -14 V-2" stroke="${PLI}" stroke-width="2"/><text x="${-96+i*24}" y="14" text-anchor="middle" font-size="11" font-weight="700" fill="#5C6A77" direction="ltr">${i}</text>`).join("")}`,
  bookshelf:()=>`<rect x="-34" y="-110" width="68" height="110" rx="3" fill="#A87449" stroke="${PLI}" stroke-width="2"/>${[0,1,2].map(r=>`<rect x="-30" y="${-104+r*36}" width="60" height="30" fill="#7A4E2D"/>${[0,1,2,3,4,5].map(i=>`<rect x="${-28+i*10}" y="${-102+r*36+(i%3)*2}" width="8" height="${28-(i%3)*2}" rx="1" fill="${["#E2504C","#4F7BA6","#F2B33D","#5DBB63","#9B6BD6","#E8833A"][(i+r)%6]}"/>`).join("")}`).join("")}`,
  column:()=>`<rect x="-14" y="-104" width="28" height="8" fill="#EAD9B5" stroke="${PLI}" stroke-width="1.8"/><rect x="-10" y="-96" width="20" height="90" fill="#F3E6C8" stroke="${PLI}" stroke-width="1.8"/>${[-5,0,5].map(x=>`<path d="M${x} -94 V-8" stroke="#D9C59C" stroke-width="1.4"/>`).join("")}<rect x="-15" y="-8" width="30" height="8" fill="#EAD9B5" stroke="${PLI}" stroke-width="1.8"/>`,
  obelisk:()=>`<path d="M-9 0 L-6 -96 L0 -108 L6 -96 L9 0Z" fill="#E8C98A" stroke="${PLI}" stroke-width="1.8"/><path d="M-3 -80 h6 M-2 -66 l4 4 M-3 -50 h6 M0 -40 v8" stroke="#A7834A" stroke-width="1.6"/>`,
  scroll:()=>`<rect x="-40" y="-36" width="80" height="34" fill="#F6E7C1" stroke="${PLI}" stroke-width="1.8"/><circle cx="-40" cy="-19" r="8" fill="#EAD3A0" stroke="${PLI}" stroke-width="1.6"/><circle cx="40" cy="-19" r="8" fill="#EAD3A0" stroke="${PLI}" stroke-width="1.6"/><path d="M-26 -28 h10 M-24 -20 l6 4 M-10 -28 v10 M2 -26 a4 4 0 1 0 0.1 0 M14 -28 l6 10 M26 -26 h-6" stroke="#A7834A" stroke-width="1.6" fill="none"/>`,
  gear:c=>`<g class="pl-gear"><path d="${Array.from({length:8},(_,i)=>{const a=i*Math.PI/4,b=a+0.22,r1=22,r2=29;return `${i?"L":"M"}${(Math.cos(a-0.22)*r1).toFixed(1)} ${(Math.sin(a-0.22)*r1).toFixed(1)} L${(Math.cos(a-0.12)*r2).toFixed(1)} ${(Math.sin(a-0.12)*r2).toFixed(1)} L${(Math.cos(b-0.1)*r2).toFixed(1)} ${(Math.sin(b-0.1)*r2).toFixed(1)} L${(Math.cos(b)*r1).toFixed(1)} ${(Math.sin(b)*r1).toFixed(1)}`;}).join(" ")}Z" fill="${c||"#B9C4D0"}" stroke="${PLI}" stroke-width="1.8"/><circle r="8" fill="#8FA3B8" stroke="${PLI}" stroke-width="1.6"/></g>`,
  bulb:()=>`<path d="M0 0 V-14" stroke="${PLI}" stroke-width="2"/><rect x="-6" y="-22" width="12" height="9" rx="2" fill="#9AA5B1" stroke="${PLI}" stroke-width="1.4"/><circle class="pl-glowbulb" cy="-36" r="14" fill="#FFE27A" stroke="${PLI}" stroke-width="1.8"/><path d="M-4 -34 q4 -6 8 0" fill="none" stroke="#E0A800" stroke-width="1.6"/>`,
  battery:()=>`<rect x="-8" y="-50" width="16" height="6" rx="2" fill="#C8CDD2" stroke="${PLI}" stroke-width="1.4"/><rect x="-16" y="-44" width="32" height="44" rx="5" fill="#5DBB63" stroke="${PLI}" stroke-width="1.8"/><text y="-16" text-anchor="middle" font-size="16" font-weight="900" fill="#fff" direction="ltr">+</text>`,
  wire:()=>`<path d="M-80 -6 Q-40 -30 0 -6 T80 -6" fill="none" stroke="#E2504C" stroke-width="3" stroke-linecap="round"/><path d="M-80 2 Q-40 -22 0 2 T80 2" fill="none" stroke="#3B4252" stroke-width="3" stroke-linecap="round"/>`});
Object.assign(PL_SHADOW,{bookshelf:30,column:16,obelisk:12,battery:14,flag:6,pebble:10});
Object.assign(PL_SOUND,{worm:"pop",pebble:"step",roots:"flip",mito:"bloom",vesicle:"pop",er:"flip",atom:"sparkle",particle:"pop",raincloud:"flip",rainbow:"bloom",
  ball:"step",ruler:"step",flag:"pop",sym:"ding",numline:"step",bookshelf:"flip",column:"step",obelisk:"step",scroll:"flip",gear:"step",bulb:"sparkle",battery:"ding",wire:"step"});

/* ---------- the zones (the little world of a concept): ctx = the place tools of plScene (places.js) ---------- */
const PL_ZONE={
  /* 🆕 batch 41 (Hareth: «الدودة طالعة بالسما والحجر طالع بالسما»): the soil starts AT the ground line (gy) — the same line every place uses —
     and what lives under the ground (stones, worms, roots) has a DEPTH in the soil, never a height in the sky; the flower and the grass on top */
  underground:({sky,P,W,H,gy,S,full})=>{const deep=H-gy,at=(t,fx,f,sc,arg,anim)=>P(t,fx,deep*f/S,sc,arg,anim);   /* f = how deep (0 = the surface, 1 = the bottom) */
    const rk=Math.min(full?S*1.1:S*0.8,(deep-6)/70);                          /* the roots always fit in the soil there is */
    return [full?sky("#B7E3FF","#E8F6FF")+`<rect class="pl-ground" x="0" y="${gy}" width="${W}" height="${deep}" fill="#9C7149"/>${[0.3,0.55,0.8].map((f,i)=>{const y=gy+deep*f;return `<path class="pl-far" d="M0 ${y} Q${W*0.3} ${y-10} ${W*0.55} ${y+6} T${W} ${y-4} V${H} H0Z" fill="${["#8E6440","#7F5737","#704B2F"][i]}"/>`;}).join("")}<rect x="0" y="${gy-6}" width="${W}" height="8" fill="#7BC46F"/>${plTufts(W,gy-4,S,"#6DBE63")}`
        :`<rect class="pl-ground" x="0" y="${gy}" width="${W}" height="${deep+2}" fill="#9C7149" opacity=".55"/>`,
      (full?plAt("roots",W*0.22,gy,rk,PLP.roots(),"sway")+plAt("roots",W*0.7,gy,rk*0.82,PLP.roots(),"sway2")+P("flower",0.22,0,0.8,"#F28AA8","sway")+P("grass",0.7,0,0.9)
        +at("pebble",0.08,0.22,1)+at("pebble",0.9,0.4,0.8,"#B9B2A6")+at("pebble",0.6,0.72,0.7,"#8E8578")+at("worm",0.84,0.62,0.9,null,"wiggle")+at("worm",0.14,0.5,0.7,null,"wiggle")
       :plAt("roots",W*0.06,gy,rk,PLP.roots(),"sway")+plAt("roots",W*0.95,gy,rk*0.88,PLP.roots(),"sway2")+at("pebble",0.1,0.62,0.8)+at("pebble",0.88,0.7,0.7,"#B9B2A6")+at("worm",0.9,0.45,0.7,null,"wiggle")),
      ""];},
  cell:({sky,P,W,H,gy,S,full,lo,u,edge})=>[full?`<defs><radialGradient id="plz${u}" cx=".5" cy=".5" r=".75"><stop offset="0" stop-color="#F3FBF4"/><stop offset=".7" stop-color="#DDF2E3"/><stop offset="1" stop-color="#BFE3C9"/></radialGradient></defs><rect class="pl-sky" width="${W}" height="${H}" fill="url(#plz${u})"/><rect x="10" y="10" width="${W-20}" height="${H-20}" rx="60" fill="none" stroke="#8FCB9E" stroke-width="10" opacity=".55"/><rect x="22" y="22" width="${W-44}" height="${H-44}" rx="50" fill="none" stroke="#8FCB9E" stroke-width="3" stroke-dasharray="4 8" opacity=".6"/>`:`<rect x="6" y="6" width="${W-12}" height="${H-12}" rx="40" fill="none" stroke="#8FCB9E" stroke-width="6" opacity=".35"/>`,
    plAt("mito",W*0.1,H*0.22,S*0.9,PLP.mito(),"float0")+plAt("mito",W*0.9,H*0.7,S*0.8,PLP.mito(),"float1")+plAt("er",W*0.88,H*0.2,S,PLP.er(),"sway")+plAt("er",W*0.12,H*0.78,S*0.8,PLP.er(),"sway2")
    +[[0.06,0.5,"#BFE6D6"],[0.94,0.42,"#F5D8A8"],[0.2,0.1,"#D8C8F5"],[0.78,0.9,"#BFE6D6"]].map(([fx,fy,c],i)=>plAt("vesicle",W*fx,H*fy,S*(0.8+0.2*(i%2)),PLP.vesicle(c),"float"+(i%3))).join("")
    +(full?Array.from({length:14},(_,i)=>plAt("particle",W*edge(((i*137)%97)/97),H*edge(((i*71)%53)/53),S*0.5,PLP.particle(i%2?"#9CCFD8":"#F2B6C2"),"float"+(i%3))).join(""):""),""],
  atoms:({W,H,gy,S,full,lo,u,edge})=>[full?`<defs><linearGradient id="plz${u}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1D2B4F"/><stop offset="1" stop-color="#2D4373"/></linearGradient></defs><rect class="pl-sky" width="${W}" height="${H}" fill="url(#plz${u})"/>${Array.from({length:Math.ceil(W/40)},(_,i)=>`<path d="M${i*40} 0 V${H}" stroke="#ffffff" stroke-opacity=".05"/>`).join("")}`:`<rect class="pl-sky pl-night" width="${W}" height="${H}" fill="#24315A" opacity=".08"/>`,
    plAt("atom",W*0.1,H*0.2,S*1.1,PLP.atom(),"float0")+plAt("atom",W*0.9,H*0.25,S*0.9,PLP.atom("#F2B6C2"),"float1")+plAt("atom",W*0.88,H*0.78,S*0.8,PLP.atom("#FFE27A"),"float2")+plAt("atom",W*0.12,H*0.8,S*0.75,PLP.atom(),"float1")
    +Array.from({length:full?16:8},(_,i)=>{const fx=edge(((i*137)%97)/97),fy=edge(((i*71)%53)/53);return full||fx<0.18||fx>0.82?plAt("particle",W*fx,H*fy,S*0.45,PLP.particle(["#9CCFD8","#F2B6C2","#FFE27A"][i%3]),"twinkle"+(i%3)):"";}).join(""),""],
  sky:({sky,ground,P,X,cloud,W,H,gy,S,full,lo,skyY})=>[full?sky("#9FD0F5","#DDF0FF"):"",
    (full?plAt("rainbow",W*0.5,gy-10*S,S*2.2,PLP.rainbow(),"still","pl-far"):"")+plAt("raincloud",W*0.12,skyY(0.16),S*1.1,PLP.raincloud(),"drift2")+plAt("raincloud",W*0.86,skyY(0.12),S*0.9,PLP.raincloud(),"bob")
    +(full?cloud(0.5,0.1,0.8)+`<path class="pl-far" d="M0 ${gy} Q${W*0.3} ${gy-30*S} ${W*0.6} ${gy-8*S} T${W} ${gy-16*S} V${H} H0 Z" fill="#BDE7A6"/>`:"")+ground("#8ED081","#7BC46F")+plTufts(W,gy,S,"#6DBE63")
    +P("flower",0.06,0,0.9,"#F5D547","sway")+P("grass",0.92,0,1),
    X("bird",0.9,-110,0.8)],
  motion:({sky,ground,P,X,W,H,gy,S,full,lo})=>[full?sky("#EAF4FF","#F8FBFF"):"",
    (full?`<path class="pl-far" d="M0 ${gy-60*S} H${W}" stroke="#D5E3F2" stroke-width="2" stroke-dasharray="10 10"/>`:"")+ground("#B9C2CC","#9AA5B1")+`<path d="M0 ${gy+16*S} H${W}" stroke="#fff" stroke-width="3" stroke-dasharray="22 16" opacity=".85"/>`
    +plAt("ruler",W*0.5,gy+(full?40:30)*S,S*(full?1.6:1),PLP.ruler(),"still")+P("flag",0.05,0,1,"#5DBB63")+P("flag",0.95,0,1,"#E2504C")
    +(full?plAt("ball",0,gy,S*0.9,PLP.ball(),"drive"):""),
    ""],
  numbers:({ground,P,W,H,gy,S,full,lo})=>[`<rect class="pl-sky" width="${W}" height="${H}" fill="#FBFDFF" opacity="${full?1:0}"/>${Array.from({length:Math.ceil(W/24)},(_,i)=>`<path class="pl-far" d="M${i*24} 0 V${H}" stroke="#DCE8F5" stroke-width="1"/>`).join("")}${Array.from({length:Math.ceil(H/24)},(_,i)=>`<path class="pl-far" d="M0 ${i*24} H${W}" stroke="#DCE8F5" stroke-width="1"/>`).join("")}`.replace(/class="pl-far"/g,full?'class="pl-far"':'class="pl-far" opacity=".5"'),
    ["+","−","×","÷","=","½","٣","٧"].map((t,i)=>{const fx=[0.06,0.94,0.1,0.9,0.05,0.95,0.14,0.86][i],fy=[0.15,0.2,0.45,0.5,0.75,0.72,0.3,0.36][i];return plAt("sym",W*fx,H*fy,S*(0.9+0.2*(i%2)),PLP.sym(t),"float"+(i%3));}).join("")
    +(full?plAt("numline",W*0.5,gy+22*S,S*1.4,PLP.numline(),"still"):""),""],
  library:({sky,ground,P,X,W,H,gy,S,full,lo})=>[full?sky("#FFF4E4","#FBE9D2"):"",
    ground("#D9B98F","#C9A57A")+P("bookshelf",0.07,0,1.1)+P("bookshelf",0.93,0,1)+P("lamp",0.2,0,0.9,null,"still")
    +["ك","ل","م","ة"].map((t,i)=>plAt("letter",W*(0.16+i*0.07+(i>1?0.45:0)),H*(0.14+(i%2)*0.1),S*0.8,PLP.letter(t),"float"+(i%3))).join(""),
    X("owl",0.93,-plTop("p","bookshelf")*(full?1:0.85)+3,0.7)],   /* 🆕 batch 41: the owl sits ON the bookshelf (not in the air) */
  ancient:({sky,ground,P,X,sun,W,H,gy,S,full,lo,skyY})=>[full?sky("#FFD9A0","#FFF1D6"):"",
    (full?sun(0.82,0.15):"")+`<path class="pl-far" d="M0 ${gy} Q${W*0.3} ${gy-20*S} ${W*0.6} ${gy-6*S} T${W} ${gy-10*S} V${H} H0 Z" fill="#F2D9A6"/>`+ground("#EDCB8A","#E0B970")
    +P("column",0.05,0,1)+P("column",0.15,0,0.9)+P("obelisk",0.9,0,1)+plAt("scroll",W*(full?0.5:0.86),full?skyY(0.14):Math.max(gy-120*S,40*S),S*(full?1.2:0.8),PLP.scroll(),"float1")+P("palm",0.78,0,0.8,null,"sway"),
    X("camel",0.3,0,0.8)],
  machine:({sky,ground,P,X,W,H,gy,S,full,lo,up})=>[full?sky("#E9EEF4","#D7DFE8"):"",
    (full?`<g class="pl-far"><rect x="0" y="${gy-100*S}" width="${W}" height="${100*S}" fill="#DCE3EB"/></g>`:"")+ground("#AEB8C3","#96A1AD")
    +plAt("gear",W*0.08,H*0.2,S*1.1,PLP.gear(),"still")+plAt("gear",W*0.16,H*0.32,S*0.7,PLP.gear("#F2B33D"),"still")+plAt("gear",W*0.92,H*0.18,S*0.9,PLP.gear("#9FD0F5"),"still")
    +(full?plAt("wire",W*0.5,up(gy-150*S,plTop("p","wire"),S*1.6),S*1.6,PLP.wire(),"still","pl-far"):"")+P("battery",0.06,0,1)+P("bulb",0.94,0,1,null,"still"),
    X("robot",0.8,0,0.8)]};
