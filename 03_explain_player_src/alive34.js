/* ===== 🆕 batch 34 (Hareth: «الأسهم ثابتة… خليها تنزل وتطلع وتتفاعل، وتكون حلوة») · ALIVE ARROWS =====
   Every «needs» arrow of every scene (path.xarrow) and of the cartoons (path.st-link):
   · draws itself in when it first appears (the line grows, then its head shows);
   · sways gently up and down like a rope — its two ends stay on the characters, so it never points somewhere else;
   · under the mouse / a tap it lights up and says what it means («النبتة بيحتاج الماء»), with a tiny sound.
   Rules: one loop for the whole page (requestAnimationFrame) · it only changes the arrow's middle point (the ends, the
   «M x y Q cx cy x y» shape and the word pill next to it stay as the scene made them) · an arrow the scene moves itself
   is noticed and followed · off with «تقليل الحركة», the light quality («خفيفة») and a hidden tab. */
const ARW={seen:new WeakMap(),last:0};
/* «M x y Q cx cy x y» → numbers (the shape curve() makes); any other shape is left alone */
function arwParse(d){const m=/^M\s*(-?[\d.]+)[ ,]+(-?[\d.]+)\s*Q\s*(-?[\d.]+)[ ,]+(-?[\d.]+)[ ,]+(-?[\d.]+)[ ,]+(-?[\d.]+)\s*$/.exec(d||"");return m?m.slice(1).map(Number):null;}
function arwStill(){return reduce||document.body.dataset.q==="lo"||document.hidden;}
/* the word pill that flow() puts right after the arrow (if there was room for it) */
function arwPill(p){const n=p.nextElementSibling;return n&&n.classList&&n.classList.contains("needs")?n:null;}
function arwTrans(g){const m=/translate\(\s*(-?[\d.]+)[ ,]+(-?[\d.]+)\s*\)/.exec(g.getAttribute("transform")||"");return m?[+m[1],+m[2]]:null;}
/* a NEW arrow (or one the scene has just moved): remember its shape, give it a fat see-through twin to catch the mouse, draw it in */
function arwBorn(p,i,old){const P=arwParse(p.getAttribute("d"));if(!P)return null;
  const st={P,d:p.getAttribute("d"),ph:(i*1.7)%(2*Math.PI),pill:arwPill(p),pb:null,pw:null,hit:old?old.hit:null};
  if(st.pill)st.pb=arwTrans(st.pill);
  if(!st.hit&&p.classList.contains("xarrow")&&p.parentNode){const h=document.createElementNS("http://www.w3.org/2000/svg","path");
    h.setAttribute("class","arw-hit");h.setAttribute("d",st.d);p.parentNode.insertBefore(h,p);st.hit=h;
    arwHover(p.parentNode.classList.contains("xedge")?p.parentNode:h,p);}   /* the whole arrow group listens: the twin, the line and its word pill */   /* BEFORE the arrow: the pill stays its next neighbour */
  else if(st.hit)st.hit.setAttribute("d",st.d);
  if(!old&&!reduce&&p.animate){try{const L=p.getTotalLength();if(L>8&&getComputedStyle(p).strokeDasharray==="none"){const mk=p.getAttribute("marker-end");
      if(mk)p.removeAttribute("marker-end");const a=p.animate([{strokeDasharray:`${L} ${L}`,strokeDashoffset:L},{strokeDasharray:`${L} ${L}`,strokeDashoffset:0}],{duration:620,delay:Math.min(i,8)*70,easing:"ease-out"});
      const back=()=>{if(mk&&p.isConnected)p.setAttribute("marker-end",mk);};a.onfinish=back;a.oncancel=back;}}catch(e){}}
  return st;}
/* the arrow says what it means: the word, or the whole sentence when the scene told us both ends (data-a = what is needed, data-b = who needs it) */
function arwSay(p){const e=p.closest(".xedge"),w=ARROW_WORD();const a=e&&e.dataset.a,b=e&&e.dataset.b;
  return a&&b&&typeof exName==="function"?`«${exName(b)}» ${w} «${exName(a)}»`:`➜ ${w}`;}
function arwTip(p,on){const root=p.ownerSVGElement;if(!root)return;let t=root.querySelector(".arw-tip");if(t)t.remove();
  const e=p.closest(".xedge");root.querySelectorAll(".xedge.arw-hot").forEach(x=>x.classList.remove("arw-hot"));if(!on)return;
  if(e)e.classList.add("arw-hot");let m;try{m=p.getPointAtLength(p.getTotalLength()/2);}catch(err){return;}
  const txt=arwSay(p).replace(/[«»]/g,""),w=Math.max(46,[...txt].length*7.2+22),vb=root.viewBox.baseVal;
  const x=Math.max(vb.x+w/2+4,Math.min(vb.x+vb.width-w/2-4,m.x)),y=Math.max(vb.y+18,m.y-24);
  t=document.createElementNS("http://www.w3.org/2000/svg","g");t.setAttribute("class","arw-tip");t.setAttribute("transform",`translate(${x.toFixed(1)} ${y.toFixed(1)})`);
  t.innerHTML=`<rect x="${(-w/2).toFixed(1)}" y="-14" width="${w.toFixed(1)}" height="26" rx="13"/><text y="4" text-anchor="middle"></text>`;t.querySelector("text").textContent=txt;root.appendChild(t);}
function arwHover(h,p){let off=0;
  h.addEventListener("pointerenter",e=>{if(e.pointerType!=="mouse")return;arwTip(p,true);const n=performance.now();if(n-ARW.last>500){ARW.last=n;sfx("step");}});
  h.addEventListener("pointerleave",e=>{if(e.pointerType==="mouse")arwTip(p,false);});
  h.addEventListener("pointerdown",e=>{if(e.pointerType==="mouse")return;arwTip(p,true);clearTimeout(off);off=setTimeout(()=>arwTip(p,false),1800);});}
/* the rope: only the middle point moves, across the line between the two ends */
function arwSway(p,st,t,amp){const [x1,y1,cx,cy,x2,y2]=st.P,L=Math.hypot(x2-x1,y2-y1)||1,nx=-(y2-y1)/L,ny=(x2-x1)/L;
  const o=amp*Math.min(1,L/140)*Math.sin(t*2*Math.PI/3.4+st.ph)*(p.closest(".lit,.arw-hot")?1.35:1);
  const d=`M${x1} ${y1} Q${(cx+nx*o).toFixed(1)} ${(cy+ny*o).toFixed(1)} ${x2} ${y2}`;
  if(d!==st.d){p.setAttribute("d",d);st.d=d;if(st.hit)st.hit.setAttribute("d",d);}
  if(st.pill&&st.pb){const tr=arwTrans(st.pill);if(st.pw&&tr&&(Math.abs(tr[0]-st.pw[0])>.2||Math.abs(tr[1]-st.pw[1])>.2))st.pb=tr;   /* the scene moved the word itself → follow it */
    const w=[st.pb[0]+nx*o/2,st.pb[1]+ny*o/2];st.pill.setAttribute("transform",`translate(${w[0].toFixed(1)} ${w[1].toFixed(1)})`);st.pw=w;}}
function arwTick(now){requestAnimationFrame(arwTick);const root=document.getElementById("xs");if(!root)return;
  const still=arwStill(),amp=V()?3.2:4.6,t=now/1000;
  root.querySelectorAll("path.xarrow, path.st-link").forEach((p,i)=>{let st=ARW.seen.get(p);const cur=p.getAttribute("d");
    if(!st||cur!==st.d){st=arwBorn(p,i,st);if(!st)return;ARW.seen.set(p,st);}
    if(still){const base=`M${st.P[0]} ${st.P[1]} Q${st.P[2]} ${st.P[3]} ${st.P[4]} ${st.P[5]}`;   /* still: back to the shape the scene made */
      if(st.d!==base){p.setAttribute("d",base);st.d=base;if(st.hit)st.hit.setAttribute("d",base);if(st.pill&&st.pb)st.pill.setAttribute("transform",`translate(${st.pb[0]} ${st.pb[1]})`);}return;}
    arwSway(p,st,t,amp);});}
requestAnimationFrame(arwTick);

/* ===== 🆕 batch 34 · nicer graphics: ONE hidden set of shared drawings tools for the whole page =====
   · «xgloss» (the younger stages): a «sticker» look — a white rim around the drawing, a soft shadow under it and a light from the top-left (a little 3D shine);
   · «xsoft» (the older stages): a clean, quiet shadow only (no shine: the big ones want it serious);
   · it lives in the page once (not inside each scene), so a scene without its own <defs> can still use it safely. */
(function(){if(document.getElementById("b34defs"))return;const s=document.createElementNS("http://www.w3.org/2000/svg","svg");
  s.setAttribute("id","b34defs");s.setAttribute("width","0");s.setAttribute("height","0");s.setAttribute("aria-hidden","true");s.style.position="absolute";
  s.innerHTML=`<defs>
    <filter id="xgloss" x="-20%" y="-20%" width="140%" height="145%" color-interpolation-filters="sRGB">
      <feMorphology in="SourceAlpha" operator="dilate" radius="2.6" result="d"/>
      <feFlood flood-color="#ffffff" result="w"/><feComposite in="w" in2="d" operator="in" result="rim"/>
      <feGaussianBlur in="d" stdDeviation="2.2" result="sb"/><feOffset in="sb" dy="2.4" result="so"/>
      <feFlood flood-color="#1b2a3a" flood-opacity=".22"/><feComposite in2="so" operator="in" result="shade"/>
      <feGaussianBlur in="SourceAlpha" stdDeviation="3" result="b"/>
      <feSpecularLighting in="b" surfaceScale="5" specularConstant=".95" specularExponent="20" lighting-color="#ffffff" result="s"><feDistantLight azimuth="225" elevation="45"/></feSpecularLighting>
      <feComposite in="s" in2="SourceAlpha" operator="in" result="s2"/>
      <feComposite in="SourceGraphic" in2="s2" operator="arithmetic" k1="0" k2="1" k3=".5" k4="0" result="lit"/>
      <feMerge><feMergeNode in="shade"/><feMergeNode in="rim"/><feMergeNode in="lit"/></feMerge></filter>
    <filter id="xsoft" x="-20%" y="-20%" width="140%" height="145%"><feDropShadow dx="0" dy="2" stdDeviation="2.2" flood-color="#1b2a3a" flood-opacity=".18"/></filter></defs>`;
  (document.body||document.documentElement).appendChild(s);})();
