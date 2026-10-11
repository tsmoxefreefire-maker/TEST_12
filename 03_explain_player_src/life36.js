/* ===== 🆕 batch 36 (Hareth: «الخلفية مثلاً الشجر، الطيور، الشمس… بشكل عام تتحرك وتتفاعل») · THE PLACES LIVE =====
   On top of places.js (batch 35):
   · LIVING THINGS that come and go by themselves: birds fly across the sky flapping their wings, butterflies flutter by the flowers,
     leaves fall from the trees, shooting stars in space, bubbles in the lab and the sea, a paper plane in the classroom, a tumbleweed in the desert…;
   · a TAP makes each thing do its own little show: leaves (and an apple) fall from a tree, the cloud rains, the flower blooms and a butterfly flies off,
     the sun shines and laughs, the rocket takes off and comes back, the flask bubbles over, the board draws a doodle, the lamp switches on…;
   · DEPTH with your finger: the far hills and the near things move a tiny bit apart when you move over the picture;
   · the place FEELS the game (games36.js): a right answer → the sun laughs and someone cheers · a mistake → «أوه» · the end → a party.
   Never a fact of the lesson (the place only decorates). The older stages: calmer (fewer things, no party). Light quality / «reduce motion»: all still.
   Rules: every class starts with «pl-» · moving parts are inner groups moved by CSS; the outer group holds the place · timers check isConnected. */
(function(){const d=document.querySelector("#c36defs defs");if(!d||document.getElementById("plSunGlow"))return;
  d.insertAdjacentHTML("beforeend",`<radialGradient id="plSunGlow"><stop offset="0" stop-color="#FFF3B0" stop-opacity=".95"/><stop offset=".55" stop-color="#FFE48A" stop-opacity=".35"/><stop offset="1" stop-color="#FFE48A" stop-opacity="0"/></radialGradient>`);})();
/* the soft shadow width under each kind of thing that stands on the ground (places.js P) */
const PL_SHADOW={tree:34,pine:30,bush:26,rock:22,palm:22,cactus:16,pyramid:54,mushroom:16,flask:22,tubes:30,burner:12,books:24,pot:14,fridge:24,lamp:14,potkit:24,light:10,seaweed:8,coral:12};
/* grass on the horizon (the line where the ground meets the sky looks soft, not cut) */
function plTufts(W,gy,S,c){let d="";const n=Math.ceil(W/(22*S));for(let i=0;i<=n;i++){const x=i*22*S,h=(6+((i*37)%7))*S;d+=`M${(x-6*S).toFixed(1)} ${gy+2} Q${(x-3*S).toFixed(1)} ${(gy-h*.6).toFixed(1)} ${(x-1*S).toFixed(1)} ${(gy-h).toFixed(1)} Q${x.toFixed(1)} ${(gy-h*.4).toFixed(1)} ${(x+3*S).toFixed(1)} ${(gy-h*.8).toFixed(1)} Q${(x+4*S).toFixed(1)} ${(gy-h*.3).toFixed(1)} ${(x+6*S).toFixed(1)} ${gy+2} Z `;}
  return `<path class="pl-tufts" d="${d}" fill="${c}"/>`;}
/* the ground is not a flat colour any more (behind the cartoons): grass and little flowers, sand ripples, craters, floor tiles… */
function plGround(name,W,H,gy,S){const n=Math.max(6,Math.round(W/70)),rows=Math.max(1,Math.round((H-gy)/(46*S)));let o="";
  const at=(i,r)=>[((i*97+r*53)%100)/100*W,gy+18*S+(r+((i*31)%10)/10)*((H-gy-26*S)/rows)];
  for(let r=0;r<rows;r++)for(let i=0;i<n;i++){const [x,y]=at(i,r),k=(i+r)%4;if(y>H-8)continue;
    switch(name){
      case "garden":case "forest":o+=k===0?`<circle cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" r="${(2.4*S).toFixed(1)}" fill="${["#F59BB8","#F5D547","#fff"][i%3]}" opacity=".8"/>`
        :`<path d="M${(x-5*S).toFixed(1)} ${y.toFixed(1)} q2 -7 3 -9 q1 6 2 9 q1 -6 4 -8 q-1 6 1 8 z" fill="#5FAE58" opacity=".55"/>`;break;
      case "desert":case "sea":o+=k<2?`<path d="M${(x-14*S).toFixed(1)} ${y.toFixed(1)} q7 -5 14 0 t14 0" fill="none" stroke="${name==="sea"?"#D9BC78":"#D6AF6A"}" stroke-width="${(1.6*S).toFixed(1)}" opacity=".6"/>`
        :`<ellipse cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" rx="${(3.4*S).toFixed(1)}" ry="${(2*S).toFixed(1)}" fill="#C9A060" opacity=".55"/>`;break;
      case "space":if(k===0)o+=`<ellipse cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" rx="${(12*S).toFixed(1)}" ry="${(4*S).toFixed(1)}" fill="#7F879C" opacity=".55"/><ellipse cx="${x.toFixed(1)}" cy="${(y-1).toFixed(1)}" rx="${(9*S).toFixed(1)}" ry="${(2.6*S).toFixed(1)}" fill="#8F97AC" opacity=".6"/>`;break;
      default:break;}}
  if(name==="lab"||name==="kitchen"||name==="classroom"||name==="room"){const step=(name==="classroom"||name==="room"?60:44)*S;for(let x=step;x<W;x+=step)o+=`<path d="M${x.toFixed(1)} ${gy} L${(x+(x-W/2)*0.35).toFixed(1)} ${H}" stroke="#000" stroke-opacity=".06" stroke-width="2"/>`;
    for(let y=gy+24*S;y<H;y+=28*S)o+=`<path d="M0 ${y.toFixed(1)} H${W}" stroke="#000" stroke-opacity=".05" stroke-width="2"/>`;}
  return `<g class="pl-grounddeco">${o}</g>`;}
/* ---------- the living things ---------- */
const PLI6="#3b2a1e";
const PLV={
  bird:c=>`<g class="pl-flapbody"><ellipse rx="9" ry="6" fill="${c||"#5C9BDB"}" stroke="${PLI6}" stroke-width="1.4"/><path d="M8 -1 L14 1 L8 3 Z" fill="#F5A623"/><circle cx="4" cy="-2" r="1.4" fill="${PLI6}"/></g>
    <g class="pl-wing"><path d="M-2 -3 Q-8 -16 -16 -12 Q-10 -6 -2 -2 Z" fill="${c||"#5C9BDB"}" stroke="${PLI6}" stroke-width="1.3"/></g>`,
  butterfly:c=>`<g class="pl-bwing l"><path d="M0 0 Q-12 -14 -14 -4 Q-14 4 0 2 Z M0 2 Q-10 10 -6 12 Q-2 12 0 4 Z" fill="${c||"#F59BB8"}" stroke="${PLI6}" stroke-width="1.1"/></g>
    <g class="pl-bwing r"><path d="M0 0 Q12 -14 14 -4 Q14 4 0 2 Z M0 2 Q10 10 6 12 Q2 12 0 4 Z" fill="${c||"#F59BB8"}" stroke="${PLI6}" stroke-width="1.1"/></g><path d="M0 -4 V8" stroke="${PLI6}" stroke-width="2" stroke-linecap="round"/>`,
  leaf:c=>`<path d="M0 -6 Q6 0 0 7 Q-6 0 0 -6 Z" fill="${c||"#7CC96F"}" stroke="#4E9E5A" stroke-width="1"/>`,
  plane:()=>`<path d="M-16 0 L16 -6 L-4 4 Z" fill="#fff" stroke="#9AA5B1" stroke-width="1.4" stroke-linejoin="round"/><path d="M-4 4 L16 -6 L-2 8 Z" fill="#E6EEF5" stroke="#9AA5B1" stroke-width="1.2" stroke-linejoin="round"/>`,
  bubble:()=>`<circle r="5" fill="#fff" fill-opacity=".35" stroke="#fff" stroke-width="1.4" stroke-opacity=".9"/><circle cx="-1.6" cy="-1.8" r="1.3" fill="#fff"/>`,
  shoot:()=>`<path d="M0 0 L-46 -14" stroke="url(#plShootG) #fff" stroke-width="3" stroke-linecap="round"/><circle r="3" fill="#FFF7C2"/>`,
  weed:()=>`<g class="pl-rollin"><circle r="11" fill="none" stroke="#B58A45" stroke-width="2"/><path d="M-9 -4 Q0 -12 9 -3 M-8 5 Q0 -2 8 6 M-3 -10 Q4 0 -2 10" fill="none" stroke="#C99A55" stroke-width="1.6"/></g>`,
  jelly:()=>`<path d="M-12 0 Q-12 -14 0 -14 Q12 -14 12 0 Z" fill="#E6B8F2" stroke="#B57CC9" stroke-width="1.4"/><path d="M-8 0 q-2 8 0 14 M-3 0 q2 8 0 16 M3 0 q-2 8 0 14 M8 0 q2 8 0 12" fill="none" stroke="#B57CC9" stroke-width="1.4"/>`,
  atom:()=>`<circle r="4" fill="#F28AA8"/><g class="pl-orbit" fill="none" stroke="#7FB7F2" stroke-width="1.4"><ellipse rx="16" ry="6"/><ellipse rx="16" ry="6" transform="rotate(60)"/><ellipse rx="16" ry="6" transform="rotate(120)"/></g>`,
};
/* a thing crossing the whole picture (right ↔ left) at height y, now and then */
function plCross(kind,arg,W,y,dur,delay,rtl,sc,cls){return `<g class="pl-life ${cls||""}" transform="translate(0 ${y.toFixed(1)})"><g class="pl-cross${rtl?" pl-rtl":""}" style="--dx:${(W+120).toFixed(0)}px;animation-duration:${dur}s;animation-delay:${delay}s">
    <g class="pl-bobfly"><g transform="scale(${rtl?-sc:sc} ${sc})"><g class="pl-v-${kind}">${PLV[kind](arg)}</g></g></g></g></g>`;}
/* a thing hovering around one spot (butterflies, a jellyfish, an atom) */
function plHover(kind,arg,x,y,sc,delay,cls){return `<g class="pl-life ${cls||""}" transform="translate(${x.toFixed(1)} ${y.toFixed(1)}) scale(${sc.toFixed(2)})"><g class="pl-hover" style="animation-delay:${delay}s"><g class="pl-v-${kind}">${PLV[kind](arg)}</g></g></g>`;}
/* leaves falling from a tree now and then */
function plLeaves(x,y,sc,c,n){let o="";for(let i=0;i<n;i++)o+=`<g class="pl-life" transform="translate(${(x+(i%2?14:-16)*sc).toFixed(1)} ${(y-62*sc).toFixed(1)}) scale(${sc.toFixed(2)})"><g class="pl-fall" style="--fall:${(58*sc+30).toFixed(0)}px;animation-delay:${(i*3.7+1.5).toFixed(1)}s">${PLV.leaf(c)}</g></g>`;return o;}
function plLife(name,W,H,gy,full,S){const deco=full?plGround(name,W,H,gy,S):"";if(document.body.dataset.q==="lo"||reduce)return deco;return deco+plLife2(name,W,H,gy,full,S);}
function plLife2(name,W,H,gy,full,S){const g=grown(),top=Math.min(gy*0.45,H*0.32);
  const birds=(n,c)=>Array.from({length:g?1:n},(_,i)=>plCross("bird",c,W,top*(0.35+0.3*(i%2))+8,13+i*5,1.5+i*6.5,i%2===1,S*(0.75+0.15*(i%2)),"pl-flyer")).join("");
  const flies=(xs,c)=>g?"":xs.map((fx,i)=>plHover("butterfly",c[i%c.length],fx*W,gy-(50+i*16)*S,S*0.9,i*1.3,"pl-flutter")).join("");
  switch(name){
    case "garden":return birds(2)+flies(full?[0.24,0.78]:[0.2,0.82],["#F59BB8","#F5D547"])+plLeaves(0.07*W,gy,S*(full?1:0.85),"#7CC96F",2)+plLeaves(0.93*W,gy,S*(full?0.9:0.77),"#9AD67A",2);
    case "forest":return birds(2,"#B08968")+flies([0.3,0.7],["#F5D547"])+plLeaves(0.9*W,gy,S*(full?1:0.85),"#5FA95A",2);
    case "desert":return (g?"":`<g class="pl-life" transform="translate(0 ${(gy-10*S).toFixed(1)})"><g class="pl-cross pl-roll" style="--dx:${(W+120).toFixed(0)}px;animation-duration:16s;animation-delay:4s"><g transform="scale(${S.toFixed(2)})">${PLV.weed()}</g></g></g>`)+birds(1,"#9B6B3D");
    case "space":return `<defs class="pl-life"><linearGradient id="plShootG" x1="0" x2="1"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset="1" stop-color="#FFF7C2"/></linearGradient></defs>`
      +[0,1].map(i=>`<g class="pl-life" transform="translate(${(W*(0.3+i*0.4)).toFixed(1)} ${(H*(0.1+i*0.08)).toFixed(1)})"><g class="pl-shooting" style="animation-delay:${2+i*5.5}s">${PLV.shoot()}</g></g>`).join("");
    case "lab":return (full?plHover("atom",null,W*0.5,H*0.18,S*1.1,0,"pl-spinatom"):"")+[0.05,0.12,0.9,0.96].map((fx,i)=>`<g class="pl-life" transform="translate(${(fx*W).toFixed(1)} ${(gy-30*S).toFixed(1)}) scale(${(S*0.8).toFixed(2)})"><g class="pl-riseup" style="animation-delay:${i*1.6}s">${PLV.bubble()}</g></g>`).join("");
    case "sea":return [0.1,0.3,0.7,0.9].map((fx,i)=>`<g class="pl-life" transform="translate(${(fx*W).toFixed(1)} ${(gy-10*S).toFixed(1)}) scale(${(S*0.9).toFixed(2)})"><g class="pl-riseup pl-tall" style="animation-delay:${i*1.4}s">${PLV.bubble()}</g></g>`).join("")
      +(g?"":plHover("jelly",null,W*0.9,H*0.3,S,0.5,"pl-floaty"));
    case "classroom":case "notebook":return g?"":plCross("plane",null,W,top*0.7+10,12,3,false,S,"pl-glider");
    case "map":return birds(2,"#F5F7FA");
    case "city":return birds(2,"#9AA5B1");
    case "room":return flies([0.88],["#C4A7E7"]);
    default:return "";}}
/* 🆕 batch 37 (Hareth: «لما أسوي جرافيك عالي الخلفية بتظلها ثابتة…»): the quality was switched → every place on the screen gets its living
   things at once (high) or drops them (light) — no need to wait for the next scene */
function plRequality(){document.querySelectorAll("svg .pl").forEach(pl=>{pl.querySelectorAll(".pl-life,.pl-fx").forEach(x=>x.remove());
  if(document.body.dataset.q==="lo"||reduce)return;const W=+pl.dataset.w,H=+pl.dataset.h,gy=+pl.dataset.gy,props=pl.querySelector(".pl-props");if(!W||!H||!props)return;
  const S=Math.max(0.55,Math.min(1.15,Math.min(W,H*1.4)/560));props.insertAdjacentHTML("beforeend",plLife2(pl.dataset.place,W,H,gy,pl.classList.contains("pl-full"),S));
  if(typeof shadeInto==="function")shadeInto(props,grown());});}
/* ---------- a tap: each thing's own little show ---------- */
function plPos(t){const m=/translate\(([-\d.]+) ([-\d.]+)\)(?: scale\(([-\d.]+)\))?/.exec(t.getAttribute("transform")||"");return m?[+m[1],+m[2],+(m[3]||1)]:[0,0,1];}
/* something short-lived put in the place (it removes itself) */
function plSpawn(t,html,ms){const host=t.closest(".pl-props")||t.closest(".pl");if(!host)return null;const g=document.createElementNS("http://www.w3.org/2000/svg","g");g.setAttribute("class","pl-fx");g.innerHTML=html;host.appendChild(g);
  setTimeout(()=>{if(g.isConnected)g.remove();},ms||2400);return g;}
function plClass(el,c,ms){if(!el)return;el.classList.remove(c);void el.getBoundingClientRect();el.classList.add(c);setTimeout(()=>el.classList.remove(c),ms||1200);}
const PL_FX={
  tree:t=>{const [x,y,k]=plPos(t);let o="";for(let i=0;i<4;i++)o+=`<g transform="translate(${(x+(i-1.5)*14*k).toFixed(1)} ${(y-66*k).toFixed(1)}) scale(${k.toFixed(2)})"><g class="pl-drop" style="--fall:${(66*k).toFixed(0)}px;animation-delay:${i*0.12}s">${PLV.leaf(i%2?"#9AD67A":"#6CC27A")}</g></g>`;
    if(t.dataset.pl==="tree")o+=`<g transform="translate(${(x+12*k).toFixed(1)} ${(y-62*k).toFixed(1)}) scale(${k.toFixed(2)})"><g class="pl-apple" style="--fall:${(62*k).toFixed(0)}px"><circle r="5" fill="#E2504C" stroke="${PLI6}" stroke-width="1.2"/><path d="M0 -5 V-8" stroke="#6B4423" stroke-width="1.4"/></g></g>`;
    plSpawn(t,o,2600);},
  cloud:t=>{const [x,y,k]=plPos(t);let o="";for(let i=0;i<12;i++)o+=`<g transform="translate(${(x+(-24+(i*13)%48)*k).toFixed(1)} ${(y+2).toFixed(1)})"><path class="pl-rain" style="animation-delay:${(i*0.11)%0.9}s" d="M0 0 v7" stroke="#7FB7F2" stroke-width="2.4" stroke-linecap="round"/></g>`;plSpawn(t,o,2000);},
  flower:t=>{plClass(t.querySelector(".pl-a"),"pl-bloom",900);const [x,y,k]=plPos(t);plSpawn(t,`<g transform="translate(${x.toFixed(1)} ${(y-34*k).toFixed(1)}) scale(${(k*0.9).toFixed(2)})"><g class="pl-away">${PLV.butterfly(["#F59BB8","#F5D547","#C4A7E7"][Math.floor(Math.random()*3)])}</g></g>`,2600);},
  sun:t=>{plClass(t,"pl-shine",1600);plMood(t,"laugh",1600);},
  flask:t=>{const [x,y,k]=plPos(t);let o="";for(let i=0;i<6;i++)o+=`<g transform="translate(${(x+(i%3-1)*6*k).toFixed(1)} ${(y-48*k).toFixed(1)}) scale(${(k*0.7).toFixed(2)})"><g class="pl-burst" style="animation-delay:${i*0.12}s">${PLV.bubble()}</g></g>`;plSpawn(t,o,2000);},
  rocket:t=>plClass(t.querySelector(".pl-a"),"pl-launch",2700),
  boat:t=>plClass(t.querySelector(".pl-a"),"pl-sail",2200),
  fish:t=>plClass(t.querySelector(".pl-a"),"pl-dart",1100),
  planet:t=>plClass(t.querySelector(".pl-a"),"pl-whirl",1200),
  compass:t=>plClass(t.querySelector(".pl-needle"),"pl-whirl",1200),
  clock:t=>plClass(t.querySelector(".pl-hand"),"pl-whirl",1200),
  star:t=>{const [x,y]=plPos(t);plSpawn(t,`<g transform="translate(${x.toFixed(1)} ${y.toFixed(1)})"><g class="pl-shooting pl-now">${PLV.shoot()}</g></g>`,1600);},
  board:t=>{const [x,y,k]=plPos(t);const d=["M-14 -2 l5 -14 l5 14 l-13 -9 h16 z","M-12 -8 a6 6 0 1 1 12 0 a6 6 0 1 1 12 0 q0 10 -12 16 q-12 -6 -12 -16","M-14 -8 a14 14 0 1 0 28 0 M-6 -12 v2 M6 -12 v2 M-6 -2 q6 6 12 0"][Math.floor(Math.random()*3)];
    plSpawn(t,`<g transform="translate(${(x+30*k).toFixed(1)} ${(y-50*k).toFixed(1)}) scale(${(k*1.2).toFixed(2)})"><path class="pl-chalk" d="${d}" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" pathLength="1"/></g>`,3000);},
  pencil:t=>{const [x,y,k]=plPos(t);plSpawn(t,`<path class="pl-chalk" d="M${(x-60*k).toFixed(1)} ${(y-4).toFixed(1)} q10 -10 20 0 t20 0 t20 0" fill="none" stroke="#7FB7F2" stroke-width="2.4" stroke-linecap="round" pathLength="1"/>`,2600);},
  lamp:t=>plClass(t,"pl-on",2500),
  light:t=>plClass(t,"pl-swap",2500),
  building:t=>plClass(t,"pl-on",2500),
  window:t=>plClass(t,"pl-on",2500),
  letter:t=>{const tx=t.querySelector("text");if(tx){const c=["#F28AA8","#7FB7F2","#5DBB63","#F5A623","#C4A7E7"];tx.setAttribute("fill",c[Math.floor(Math.random()*c.length)]);}plClass(t.querySelector(".pl-a"),"pl-jump",700);},
  potkit:t=>{plClass(t.querySelector(".pl-steam"),"pl-puff",1200);plClass(t.querySelector(".pl-a"),"pl-jump",700);},
  mushroom:t=>plClass(t.querySelector(".pl-a"),"pl-jump",700),
  car:t=>{const x=t.closest(".pl-prop");if(x)plSay(x,"بيب بيب 🚗",1300);},
};
PL_FX.pine=PL_FX.tree;PL_FX.palm=PL_FX.tree;PL_FX.bush=PL_FX.flower;PL_FX.tubes=PL_FX.flask;PL_FX.coral=PL_FX.flask;PL_FX.seaweed=PL_FX.flask;
/* the extras: the bird flies away and comes back; the others hop (places.js) */
const PLX_FX={bird:t=>plClass(t.querySelector(".pl-a"),"pl-flyaway",2600),pigeon:t=>plClass(t.querySelector(".pl-a"),"pl-flyaway",2600),owl:t=>plClass(t.querySelector(".pl-a"),"pl-turn",1200)};
function plTapFx(t){if(reduce||document.body.dataset.q==="lo")return;const f=t.dataset.x?PLX_FX[t.dataset.x]:PL_FX[t.dataset.pl];if(f)f(t);}
/* the sun's (or anyone's) face for a moment */
function plMood(el,m,ms){const f=el.querySelector(".pl-sunface");if(!f)return;f.dataset.mood=m;clearTimeout(f.__t);f.__t=setTimeout(()=>{f.dataset.mood="happy";},ms||1400);}
/* ---------- depth with your finger: the far layer and the near layer move a little apart ---------- */
let plPx=false;
document.addEventListener("pointermove",e=>{if(plPx||reduce||document.body.dataset.q==="lo")return;const xs=document.getElementById("xs");const pl=xs&&xs.querySelector(".pl");if(!pl)return;plPx=true;
  requestAnimationFrame(()=>{plPx=false;const r=xs.getBoundingClientRect();if(!r.width)return;const px=Math.max(-1,Math.min(1,(e.clientX-r.left)/r.width*2-1)),py=Math.max(-1,Math.min(1,(e.clientY-r.top)/r.height*2-1));
    pl.style.setProperty("--px",px.toFixed(3));pl.style.setProperty("--py",py.toFixed(3));});},{passive:true});
/* ---------- the place feels the game (games36.js sends «gx») ---------- */
document.addEventListener("gx",e=>{const xs=document.getElementById("xs"),pl=xs&&xs.querySelector(".pl");if(!pl||reduce)return;const type=e.detail&&e.detail.type;
  const suns=[...pl.querySelectorAll('[data-pl="sun"]')],extras=[...pl.querySelectorAll(".pl-x")];const one=a=>a[Math.floor(Math.random()*a.length)];
  if(type==="good"){suns.forEach(s=>plMood(s,"laugh",1500));plClass(pl,"pl-cheer",900);if(extras.length&&!grown()){const x=one(extras);plClass(x.querySelector(".pl-a"),"pl-poke",650);plSay(x,one(["👏","🎉","😄","👍","🌟"]),1300);}}
  else if(type==="bad"){suns.forEach(s=>plMood(s,"o",1300));if(extras.length&&!grown())plSay(one(extras),one(["😮","🤔","أوه!"]),1200);}
  else if(type==="win"){suns.forEach(s=>{plMood(s,"laugh",3200);plClass(s,"pl-shine",1800);});if(!grown()){plClass(pl,"pl-party",3200);extras.forEach((x,i)=>setTimeout(()=>{if(x.isConnected){plClass(x.querySelector(".pl-a"),"pl-poke",650);plSay(x,one(["🎉","👏","🥳","🌟"]),1500);}},i*260));}}});
