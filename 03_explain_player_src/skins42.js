/* ================================================================ 🆕 batch 42 · THE SAME GAME, IN ANOTHER LOOK (skins)
   Hareth: «المشاهد بتتكرر من درس لدرس». The four games that come back most keep their rules (and their words), but each lesson
   dresses them differently, so two lessons in a row never look the same:
     🧭 the journey  → a road · a river with a boat · a railway with a train · space with a rocket
     🏗️ the tower    → blocks · a castle (battlements + a flag when it is built) · a shelf of books
     ⚖️ compare      → two circles · baskets · houses with a shared garden
     🧩 the puzzle   → shadows · picture frames on a wall · a sky of stars
   Which look: from the book, the lesson and the concept (always the same for the same scene; the next lesson gets the next look).
   ?skin=river on the link tries one look everywhere. Only drawing is added here (after the scene is built); nothing about the game
   changes. The colours are in b42.css (the page's own colour tokens: light and dark). */
const LOOKS={journey:["road","river","rail","space"],tower:["blocks","castle","books"],compare:["venn","baskets","houses"],assemble:["shadows","frames","sky"]};
const LOOK_TRY=(()=>{try{return new URLSearchParams(location.search).get("skin");}catch(e){return null;}})();
function lookOf(kind){const L=LOOKS[kind];if(!L)return null;if(LOOK_TRY&&L.includes(LOOK_TRY))return LOOK_TRY;
  const p=(pathOf()||[])[POS]||{},c=Math.max(0,p.c||0);return L[((EG*5+EL+c)%L.length+L.length)%L.length];}
const lkEl=(tag,attrs,html)=>{const e=document.createElementNS(svgNS,tag);for(const k in attrs)e.setAttribute(k,attrs[k]);if(html)e.innerHTML=html;return e;};
const lkBox=root=>{const v=(root.getAttribute("viewBox")||"0 0 640 400").split(/\s+/).map(Number);return {W:v[2],H:v[3]};};
const lkAt=el=>{const m=/translate\(([-\d.]+)[ ,]+([-\d.]+)\)/.exec(el.getAttribute("transform")||"");return m?[+m[1],+m[2]]:[0,0];};
const OL42='stroke="#3b2a1a" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"';
const LOOK_TRAVELLER={
  river:`<g class="sk-trav"><path d="M-17 1 L17 1 L11 11 L-11 11 Z" fill="#B97A45" ${OL42}/><path d="M0 -17 V1" ${OL42}/><path d="M2 -16 L14 -1 L2 -1 Z" fill="#fff" ${OL42}/></g>`,
  rail:`<g class="sk-trav"><rect x="-16" y="-11" width="24" height="15" rx="3" fill="#E2504C" ${OL42}/><rect x="3" y="-18" width="9" height="9" rx="2" fill="#E2504C" ${OL42}/><rect x="-12" y="-7" width="7" height="6" rx="1" fill="#D7ECFF" ${OL42}/><circle cx="-9" cy="7" r="4.2" fill="#3b2a1a"/><circle cx="4" cy="7" r="4.2" fill="#3b2a1a"/></g>`,
  space:`<g class="sk-trav" transform="rotate(-90)"><path d="M0 -17 C9 -8 9 6 5 11 L-5 11 C-9 6 -9 -8 0 -17Z" fill="#fff" ${OL42}/><circle cy="-3" r="3.6" fill="#6CB8FF" ${OL42}/><path d="M-5 9 L-10 16 L-4 13 Z M5 9 L10 16 L4 13 Z" fill="#E2504C" ${OL42}/><path d="M-3 12 L0 20 L3 12 Z" fill="#F5A623"/></g>`};

const LOOK_DRAW={
  journey(root,s,sk){
    const roads=[...root.querySelectorAll(".xroad")];
    roads.forEach(r=>{const d=r.getAttribute("d"),at=r;
      if(sk==="river")at.parentNode.insertBefore(lkEl("path",{d,class:"sk-water"}),at);
      if(sk==="rail"){at.parentNode.insertBefore(lkEl("path",{d,class:"sk-ties"}),at);at.parentNode.insertBefore(lkEl("path",{d,class:"sk-rails"}),at);at.parentNode.insertBefore(lkEl("path",{d,class:"sk-rails2"}),at);}});
    if(sk==="space"){const {W,H}=lkBox(root),g=lkEl("g",{class:"sk-stars","aria-hidden":"true"});
      for(let i=0;i<16;i++){const x=(37+i*173)%(W-20)+10,y=(23+i*97)%(H-30)+12;g.appendChild(lkEl("path",{d:`M${x} ${y-4} L${x+1.2} ${y-1.2} L${x+4} ${y} L${x+1.2} ${y+1.2} L${x} ${y+4} L${x-1.2} ${y+1.2} L${x-4} ${y} L${x-1.2} ${y-1.2} Z`,class:"sk-star"}));}
      root.insertBefore(g,root.querySelector(".xroad"));}
    const trav=root.querySelector("#trav.g36-spark");
    if(trav&&LOOK_TRAVELLER[sk]){trav.innerHTML=LOOK_TRAVELLER[sk];trav.classList.add("sk-vehicle");}},
  tower(root,s,sk){
    const ghosts=[...root.querySelectorAll(".g4-ghost")];if(!ghosts.length)return;
    const gx=+ghosts[0].getAttribute("x"),gw=+ghosts[0].getAttribute("width"),gh=+ghosts[0].getAttribute("height"),top=Math.min(...ghosts.map(g=>+g.getAttribute("y")));
    root.querySelectorAll(".g4-brick").forEach(b=>{const r=b.querySelector("rect");const x=+r.getAttribute("x"),y=+r.getAttribute("y"),w=+r.getAttribute("width"),h=+r.getAttribute("height");
      if(sk==="castle")r.after(lkEl("path",{class:"sk-stone",d:`M${x+w*0.3} ${y+5} V${y+h-5} M${x+w*0.62} ${y+5} V${y+h*0.5} M${x+8} ${y+h*0.5} H${x+w-8}`}));
      if(sk==="books")r.after(lkEl("path",{class:"sk-spine",d:`M${x+16} ${y+4} V${y+h-4} M${x+26} ${y+4} V${y+h-4} M${x+w-12} ${y+4} V${y+h-4}`}));});
    if(sk==="castle"){const g=lkEl("g",{class:"sk-battle"});for(let i=0;i<5;i++)g.appendChild(lkEl("rect",{x:gx+6+i*(gw-12)/5+((gw-12)/5-16)/2,y:top-10,width:16,height:11,rx:2}));root.appendChild(g);
      root.appendChild(lkEl("g",{class:"sk-flag",transform:`translate(${gx+gw/2} ${top-10})`},'<path d="M0 0 V-36"/><path d="M0 -36 L24 -29 L0 -22 Z"/>'));}
    if(sk==="books"){const g=lkEl("g",{class:"sk-shelf"});ghosts.forEach(gg=>{const y=+gg.getAttribute("y");g.appendChild(lkEl("rect",{x:gx-10,y:y+gh-2,width:gw+20,height:6,rx:2,class:"sk-board"}));});
      g.appendChild(lkEl("rect",{x:gx-14,y:top-4,width:6,height:ghosts.length*gh+8,rx:2,class:"sk-board"}));g.appendChild(lkEl("rect",{x:gx+gw+8,y:top-4,width:6,height:ghosts.length*gh+8,rx:2,class:"sk-board"}));
      root.insertBefore(g,ghosts[0]);}},
  compare(root,s,sk){
    const zones=document.querySelector(".na-zones");if(zones)zones.dataset.skin=sk;if(sk==="venn")return;
    const {W,H}=lkBox(root),pa=[W*0.77,H/2-10],pb=[W*0.23,H/2-10],mid=[W/2,H/2];
    root.querySelectorAll(".na-venn").forEach(e=>e.classList.add("sk-hide"));
    const lab=root.querySelector(".na-vlab"),g=lkEl("g",{class:"sk-cmp","aria-hidden":"true"});
    if(sk==="baskets"){const bk=(x,y,w,cls)=>`<g class="sk-basket ${cls}" transform="translate(${x} ${y})"><path d="M${-w/2} 0 L${w/2} 0 L${w*0.38} ${w*0.42} L${-w*0.38} ${w*0.42} Z"/><path class="sk-weave" d="M${-w*0.44} ${w*0.12} H${w*0.44} M${-w*0.41} ${w*0.26} H${w*0.41} M${-w*0.15} 0 L${-w*0.12} ${w*0.42} M${w*0.15} 0 L${w*0.12} ${w*0.42}"/><path class="sk-handle" d="M${-w*0.36} 0 C${-w*0.3} ${-w*0.5} ${w*0.3} ${-w*0.5} ${w*0.36} 0"/></g>`;
      g.innerHTML=bk(pa[0],pa[1]+30,96,"sk-a")+bk(pb[0],pb[1]+30,96,"sk-b")+bk(mid[0],mid[1]+22,74,"sk-both");if(lab)lab.setAttribute("y",mid[1]+64);}
    if(sk==="houses"){const hs=(x,y,cls)=>`<g class="sk-house ${cls}" transform="translate(${x} ${y})"><path class="sk-roof" d="M-62 -40 L0 -86 L62 -40 Z"/><rect class="sk-wall" x="-52" y="-40" width="104" height="80" rx="6"/></g>`;
      g.innerHTML=hs(pa[0],pa[1],"sk-a")+hs(pb[0],pb[1],"sk-b")+`<g class="sk-garden"><ellipse cx="${mid[0]}" cy="${mid[1]+40}" rx="${W*0.11}" ry="16"/><path d="M${mid[0]-18} ${mid[1]+34} q4 -16 8 0 M${mid[0]+8} ${mid[1]+36} q4 -14 8 0"/><circle cx="${mid[0]-14}" cy="${mid[1]+22}" r="5" class="sk-fl"/><circle cx="${mid[0]+12}" cy="${mid[1]+24}" r="5" class="sk-fl"/></g>`;
      if(lab)lab.setAttribute("y",mid[1]+8);}
    root.insertBefore(g,root.querySelector(".xnode"));},
  assemble(root,s,sk){
    const sh=[...root.querySelectorAll(".shadow")];if(!sh.length||sk==="shadows")return;
    const g=lkEl("g",{class:"sk-asm","aria-hidden":"true"}),pos={};sh.forEach(e=>pos[e.dataset.id]=lkAt(e));
    const P=Object.values(pos);let near=1e9;P.forEach((a,i)=>P.slice(i+1).forEach(b=>{near=Math.min(near,Math.hypot(a[0]-b[0],a[1]-b[1]));}));
    const hf=Math.max(30,Math.min(46,near/2-6));                     /* close shadows → smaller frames / rings: they never overlap */
    if(sk==="frames")sh.forEach(e=>{const [x,y]=pos[e.dataset.id];g.insertAdjacentHTML("beforeend",`<path class="sk-string" d="M${x-hf*0.65} ${y-hf} L${x} ${y-hf-14} L${x+hf*0.65} ${y-hf}"/><circle class="sk-nail" cx="${x}" cy="${y-hf-14}" r="3"/><rect class="sk-frame" x="${x-hf}" y="${y-hf}" width="${2*hf}" height="${2*hf}" rx="6"/>`);});
    if(sk==="sky"){(s.edges||[]).forEach(([a,b])=>{if(pos[a]&&pos[b])g.insertAdjacentHTML("beforeend",`<path class="sk-link" d="M${pos[a][0]} ${pos[a][1]} L${pos[b][0]} ${pos[b][1]}"/>`);});
      sh.forEach((e,i)=>{const [x,y]=pos[e.dataset.id];g.insertAdjacentHTML("beforeend",`<circle class="sk-ring" cx="${x}" cy="${y}" r="${hf}"/>`+[0,1,2].map(k=>{const a=(i*1.7+k*2.1),px=x+Math.cos(a)*(hf+10),py=y+Math.sin(a)*(hf+8);return `<circle class="sk-star" cx="${px.toFixed(1)}" cy="${py.toFixed(1)}" r="${k===1?2.6:1.8}"/>`;}).join(""));});}
    root.insertBefore(g,sh[0]);
    const tray=root.querySelector(".tray");if(tray)tray.classList.add("sk-tray-"+sk);}};

/* every scene of these four kinds: built as before, then dressed */
Object.keys(LOOKS).forEach(kind=>{const make=SCENES[kind];if(!make||make.looked)return;
  const dressed=s=>{const out=make(s);if(!out||typeof out.wire!=="function")return out;const sk=lookOf(kind),w=out.wire;
    out.wire=root=>{try{if(root&&root.setAttribute){root.setAttribute("data-skin",sk);LOOK_DRAW[kind](root,s,sk);}}catch(e){}return w(root);};return out;};
  dressed.looked=true;SCENES[kind]=dressed;});
