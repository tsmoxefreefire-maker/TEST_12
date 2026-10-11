/* ===== 🆕 batch 36 (Hareth: «الشخصيات لازم تتعدل الجرافيك تبعها بشكل أفضل بكثير») · CHARACTERS 2.0 =====
   Every drawing on the page (hand-made, a subject one or a Lego one) gets, without redrawing anything by hand:
   · DEPTH: each flat colour becomes a soft gradient (light from the top-left, a cool shade at the bottom-right) → round, painted bodies,
     and the dark brown outline takes the body's own deep colour (a green leaf → a deep green line): softer and more finished;
   · the new glossy EYES and soft CHEEKS (faceSVG in part3_core.js) use the shared iris / blush gradients made here;
   · little SHOES under the body (the younger stages), standing on the real bottom of the drawing;
   · it BREATHES (a tiny squash and stretch), bounces when it is happy, droops a little when it is sad, squishes when you point at it;
   · the arms (chars35.js) now come out of the real EDGE of the body (measured with the drawing's own outline), not from its box.
   Older stages: a milder shade, no shoes, no bouncing (serious). Light quality / «reduce motion»: no movement (the depth stays).
   Rules: every class starts with «ch-» or «c36» · the face is never shaded · tokens you throw or drag (CH_TOKEN) get no shoes. */
const C36NS="http://www.w3.org/2000/svg";
/* ---------- shared drawing tools for the whole page (one hidden <svg>) ---------- */
(function(){if(document.getElementById("c36defs"))return;const s=document.createElementNS(C36NS,"svg");
  s.setAttribute("id","c36defs");s.setAttribute("width","0");s.setAttribute("height","0");s.setAttribute("aria-hidden","true");s.style.position="absolute";
  s.innerHTML=`<defs><radialGradient id="c36iris" cx=".42" cy=".36" r=".7"><stop offset="0" stop-color="#A9784A"/><stop offset=".6" stop-color="#6B4423"/><stop offset="1" stop-color="#3E2614"/></radialGradient>
    <radialGradient id="c36blush"><stop offset="0" stop-color="#F27A9C" stop-opacity=".75"/><stop offset=".7" stop-color="#F59AB4" stop-opacity=".35"/><stop offset="1" stop-color="#F8B4C8" stop-opacity="0"/></radialGradient></defs>`;
  (document.body||document.documentElement).appendChild(s);})();
/* ---------- colours ---------- */
function c36Hex(c){if(!c)return null;c=String(c).trim().toLowerCase();if(/^#[0-9a-f]{3}$/.test(c))c="#"+c[1]+c[1]+c[2]+c[2]+c[3]+c[3];return /^#[0-9a-f]{6}$/.test(c)?c:null;}
function c36Mix(a,b,t){const p=x=>[1,3,5].map(i=>parseInt(x.slice(i,i+2),16));const A=p(a),B=p(b);return "#"+A.map((v,i)=>Math.round(v+(B[i]-v)*t).toString(16).padStart(2,"0")).join("");}
/* one gradient per colour (and per strength), made once, shared by every drawing */
function c36Grad(hex,mild){const id=`c36${mild?"m":"g"}${hex.slice(1)}`;if(document.getElementById(id))return id;const defs=document.querySelector("#c36defs defs");if(!defs)return null;
  const g=document.createElementNS(C36NS,"linearGradient");g.setAttribute("id",id);g.setAttribute("x1",".18");g.setAttribute("y1","0");g.setAttribute("x2",".82");g.setAttribute("y2","1");
  const lo=mild?.2:.38,hi=mild?.12:.22;
  g.innerHTML=`<stop offset="0" stop-color="${c36Mix(hex,"#ffffff",lo)}"/><stop offset=".48" stop-color="${hex}"/><stop offset="1" stop-color="${c36Mix(hex,"#24364a",hi)}"/>`;
  defs.appendChild(g);return id;}
/* every flat colour inside el → its gradient (never the face, the arms, the shoes or a see-through highlight) */
const C36_KEEP=".sface,.ch-arms,.ch-feet,defs,clipPath,mask,pattern,.pl-say,text";
function shadeInto(el,mild){if(!el)return;el.querySelectorAll("path,circle,ellipse,rect,polygon").forEach(sh=>{if(sh.dataset.c36||sh.closest(C36_KEEP))return;
    const op=parseFloat(sh.getAttribute("opacity")||"1"),fo=parseFloat(sh.getAttribute("fill-opacity")||"1");const hex=c36Hex(sh.getAttribute("fill"));
    if(!hex||op<.95||fo<.95)return;const id=c36Grad(hex,mild);if(!id)return;sh.dataset.c36=hex;sh.setAttribute("fill",`url(#${id}) ${hex}`);
    if(C36_INK.test(sh.getAttribute("stroke")||""))sh.setAttribute("stroke",c36Mix(hex,"#1f1208",.62));});}   /* the outline takes the body's own deep colour (softer, more finished) */
const C36_INK=/^#3b2a1[ae]$/i;
/* ---------- the drawing's REAL outline (in its own 0…100 units), measured once per drawing ---------- */
const C36_EDGES=new Map();
function c36Shapes(sv){return [...sv.querySelectorAll("path,circle,ellipse,rect,polygon")].filter(sh=>!sh.closest(".sface,.ch-arms,.ch-feet,defs")&&sh.getAttribute("fill")!=="none"&&typeof sh.isPointInFill==="function");}
function c36Edges(sv){if(sv.__c36e!==undefined)return sv.__c36e;
  const key=sv.innerHTML.length+":"+sv.innerHTML.replace(/url\(#c36[gm][0-9a-f]+\) /g,"").slice(0,160);if(C36_EDGES.has(key))return (sv.__c36e=C36_EDGES.get(key));
  const S=sv.getScreenCTM(),shapes=S?c36Shapes(sv):[];const done=e=>{C36_EDGES.set(key,e);sv.__c36e=e;return e;};if(!shapes.length)return done(null);
  /* each shape: the way back from the drawing's units to its own, and its box in the drawing's units (only those can hold a point) */
  const info=shapes.map(sh=>{const m=sh.getScreenCTM();if(!m)return null;const toSv=S.inverse().multiply(m);let b;try{b=sh.getBBox();}catch(e){return null;}
    const cs=[[b.x,b.y],[b.x+b.width,b.y],[b.x,b.y+b.height],[b.x+b.width,b.y+b.height]].map(([x,y])=>new DOMPoint(x,y).matrixTransform(toSv));
    return {sh,inv:toSv.inverse(),x0:Math.min(...cs.map(p=>p.x)),x1:Math.max(...cs.map(p=>p.x)),y0:Math.min(...cs.map(p=>p.y)),y1:Math.max(...cs.map(p=>p.y))};}).filter(Boolean);
  if(!info.length)return done(null);
  const T=Math.max(0,Math.min(...info.map(i=>i.y0))),B=Math.min(100,Math.max(...info.map(i=>i.y1)));
  const row=y=>{const on=info.filter(i=>i.y0<=y&&i.y1>=y);if(!on.length)return null;
    const inside=x=>on.some(i=>i.x0<=x&&i.x1>=x&&(()=>{try{return i.sh.isPointInFill(new DOMPoint(x,y).matrixTransform(i.inv));}catch(e){return false;}})());
    let l=null,r=null;for(let x=2;x<=98;x+=2)if(inside(x)){if(l===null)l=x;r=x;}if(l===null)return null;
    while(l>0&&inside(l-.5))l-=.5;while(r<100&&inside(r+.5))r+=.5;return [l,r];};
  const H=B-T;let sh=null;for(const f of [.58,.5,.66,.44,.72]){const y=T+H*f,w=row(y);if(w&&w[1]-w[0]>=14){sh={y,l:w[0],r:w[1]};break;}}   /* the shoulders: high enough, wide enough */
  const fw=row(T+H*.94)||row(T+H*.86)||[46,54];
  return done({top:T,bottom:B,sh,feet:{y:B,l:fw[0],r:fw[1]}});}
/* ---------- little shoes (the younger stages) ---------- */
function feetInto(sv){if(sv.querySelector(".ch-feet"))return;const e=c36Edges(sv);if(!e)return;
  const cx=(e.feet.l+e.feet.r)/2,half=Math.max(5.5,Math.min(13,(e.feet.r-e.feet.l)*.32)),y=Math.min(97,e.feet.y+1.5);
  const shoe=(x,side)=>`<g class="ch-foot ${side}" style="transform-origin:${x.toFixed(1)}px ${(y-2).toFixed(1)}px"><ellipse cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" rx="7.6" ry="4.6" fill="#6A4330" stroke="#3b2a1e" stroke-width="2"/><ellipse cx="${(x-2.2).toFixed(1)}" cy="${(y-1.6).toFixed(1)}" rx="2.6" ry="1.2" fill="#fff" opacity=".45"/></g>`;
  const g=document.createElementNS(C36NS,"g");g.setAttribute("class","ch-feet");g.innerHTML=shoe(cx-half,"l")+shoe(cx+half,"r");sv.insertBefore(g,sv.firstChild);}
/* ---------- it breathes (one inner group holds everything, so the outer ones keep their own moves) ---------- */
function c36Wrap(sv,i){if(sv.querySelector(":scope > .ch-breathe"))return;const g=document.createElementNS(C36NS,"g");g.setAttribute("class","ch-breathe");
  g.style.animationDelay=`-${((i*0.73)%3.6).toFixed(2)}s`;[...sv.childNodes].forEach(c=>{if(c.nodeName!=="defs")g.appendChild(c);});sv.appendChild(g);}
/* ---------- all of it, for every character in a scene ---------- */
function charsUp(root){if(!root)return;const mild=grown();
  root.querySelectorAll(".pl .pl-near").forEach(n=>shadeInto(n,mild));          /* the place's props too (also the cartoons' own place) */
  root.querySelectorAll(".xbody>svg.ch").forEach((sv,i)=>{if(sv.dataset.c36)return;sv.dataset.c36="1";shadeInto(sv,mild);
    const nd=sv.closest(".xnode");const box=sv.getBoundingClientRect();
    const token=!nd||nd.matches(CH_TOKEN);if(!mild&&!token&&box.width>=44)feetInto(sv);
    if(!token)c36Wrap(sv,i);});}                                             /* a token in your hand stays still (no breathing under your finger) */
try{window.__CH36={art:artSVG,arms:armsInto,up:charsUp,icons:()=>{const o=[];DATA.graphs.forEach(g=>g.lessons.forEach(l=>Object.values(l.icons||{}).forEach(i=>{if(!o.includes(i))o.push(i);})));return o;}};}catch(e){}   /* for the browser check only (the before/after gallery) */
