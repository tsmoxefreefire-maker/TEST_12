/* ================================================================ 👗 batch 45 · THE CLOTHES (a TRIAL)
   Hareth: «بدي أغيّر ملابس الزهرة… بس للتجربة… الزهرة والجذر والثمرة… ثلاث ملابس لكل واحد».
   A button in the corner «👗 الملابس» → for each one: nothing, or one of 3 outfits. The outfit is a LAYER ON TOP of the drawing (the drawing
   itself never changes), so it goes with the character into EVERY scene (the story, «تعرّف عليّ», the big picture, the games) and moves with it.
   A new choice replaces the old one everywhere (the scene on screen is drawn again at once, at the same moment); the choice is kept on this device.
   Only for these three, only when the drawing is theirs (🌸 🫚 🍎) — another book's «root» (maths…) is never dressed.
   Rules: «ow45-» classes · the outfits are drawn in the drawing's own 100×100 box, the same outline as the characters. */
const OW_O='stroke="#3b2a1a" stroke-width="2.2" stroke-linejoin="round" stroke-linecap="round"';
const OUTFITS={
  flower:{ic:"🌸",name:"الزهرة",o:[
    {n:"👑 تاج",svg:`<path d="M37 31 L35 15 L43 23 L50 11 L57 23 L65 15 L63 31 Z" fill="#FFD54A" ${OW_O}/><circle cx="50" cy="25" r="2.4" fill="#E53935" stroke="#3b2a1a" stroke-width="1"/><circle cx="41" cy="27" r="1.6" fill="#42A5F5"/><circle cx="59" cy="27" r="1.6" fill="#42A5F5"/>`},
    {n:"🕶️ نظارة",svg:`<path d="M48.5 46 Q50 44.5 51.5 46" fill="none" ${OW_O}/><rect x="34.5" y="41.5" width="14" height="10.5" rx="4.5" fill="#263238" ${OW_O}/><rect x="51.5" y="41.5" width="14" height="10.5" rx="4.5" fill="#263238" ${OW_O}/><path d="M37 44.5 l4 -1.5 M54 44.5 l4 -1.5" stroke="#fff" stroke-width="1.4" stroke-linecap="round" opacity=".7"/>`},
    {n:"🎀 بابيون",svg:`<path d="M50 75 L38 69 L38 81 Z M50 75 L62 69 L62 81 Z" fill="#7E57C2" ${OW_O}/><rect x="46.5" y="71.5" width="7" height="7" rx="2" fill="#9575CD" ${OW_O}/>`}]},
  root:{ic:"🫚",name:"الجذر",o:[
    {n:"🎩 قبعة طويلة",svg:`<rect x="36" y="2" width="28" height="16" rx="2" fill="#37474F" ${OW_O}/><rect x="36.5" y="12" width="27" height="4" fill="#E53935"/><ellipse cx="50" cy="18.5" rx="25" ry="4" fill="#455A64" ${OW_O}/>`},
    {n:"🧣 شال",svg:`<rect x="20" y="62" width="60" height="9" rx="4.5" fill="#E53935" ${OW_O}/><path d="M60 69 L59 85 L68 85 L68 69 Z" fill="#E53935" ${OW_O}/><path d="M30 62.5 v8 M42 62.5 v8 M54 62.5 v8 M70 62.5 v8 M59.5 77 h8" stroke="#FFF59D" stroke-width="2.4"/>`},
    {n:"🧢 كاب",svg:`<path d="M29 20 Q30 4 50 4 Q70 4 71 20 Z" fill="#1E88E5" ${OW_O}/><path d="M68 19 Q80 17 88 21 Q80 24 66 22 Z" fill="#1565C0" ${OW_O}/><circle cx="50" cy="4.5" r="2" fill="#1565C0" stroke="#3b2a1a" stroke-width="1"/><path d="M40 8 Q38 14 38 20 M60 8 Q62 14 62 20" fill="none" stroke="#90CAF9" stroke-width="1.4"/>`}]},
  fruit:{ic:"🍎",name:"الثمرة",o:[
    {n:"🎓 قبعة تخرّج",svg:`<path d="M35 18 L35 27 Q50 32 65 27 L65 18 Z" fill="#263238" ${OW_O}/><path d="M50 7 L78 15 L50 23 L22 15 Z" fill="#37474F" ${OW_O}/><path d="M50 15 L74 18 L74 29" fill="none" stroke="#FFC107" stroke-width="1.8" stroke-linecap="round"/><circle cx="74" cy="30" r="2.2" fill="#FFC107" stroke="#3b2a1a" stroke-width="1"/>`},
    {n:"🎀 فيونكة",svg:`<path d="M30 23 L17 15 L19 33 Z M30 23 L43 13 L41 31 Z" fill="#F06292" ${OW_O}/><circle cx="30" cy="23" r="4" fill="#EC407A" ${OW_O}/>`},
    {n:"🤠 قبعة كاوبوي",svg:`<path d="M36 20 Q34 6 43 5 Q50 9 57 5 Q66 6 64 20 Z" fill="#A1662F" ${OW_O}/><rect x="35.5" y="15" width="29" height="4" fill="#5D4037"/><path d="M14 19 Q24 25 50 24 Q76 25 86 19 Q82 28 50 29 Q18 28 14 19 Z" fill="#8D5524" ${OW_O}/>`}]}};
const OW={pick:{},open:false};
try{OW.pick=JSON.parse(localStorage.getItem("ie_outfit45")||"{}")||{};}catch(e){OW.pick={};}
const owSave=()=>{try{localStorage.setItem("ie_outfit45",JSON.stringify(OW.pick));}catch(e){}};
/* is this concept one of the three (its own drawing)? */
const owIs=id=>{const w=OUTFITS[id];return !!w&&typeof iconOf==="function"&&(()=>{try{return icBase(iconOf(id))===w.ic;}catch(e){return false;}})();};
/* the drawing + the outfit on top (the drawing is never changed) */
function dressed(id,a){const k=OW.pick[id];if(!a||k==null||!owIs(id))return a;const o=OUTFITS[id].o[k];if(!o)return a;
  const i=a.lastIndexOf("</svg>");return i<0?a:`${a.slice(0,i)}<g class="ow45" data-ow="${id}:${k}">${o.svg}</g>${a.slice(i)}`;}
/* which of the three are in this book */
const owHere=()=>{const g=(typeof graph==="function"&&graph())||{},seen=new Set();(g.lessons||[]).forEach(l=>Object.keys(l.icons||{}).forEach(id=>{const w=OUTFITS[id];if(w&&icBase(l.icons[id])===w.ic)seen.add(id);}));return Object.keys(OUTFITS).filter(id=>seen.has(id));};
/* the scene on screen is drawn again at once, at the same moment (the story keeps its time) */
function owRedraw(){const c=window.stCtl,t=c&&document.querySelector("#xs.st-svg")?c.t:null;try{renderScene();}catch(e){}
  if(t!=null&&window.stCtl&&window.stCtl!==c){try{window.stCtl.seek(t);}catch(e){}}}
function owPanel(){let p=document.getElementById("ow45p");const here=owHere();if(!OW.open||!here.length){if(p)p.remove();return;}
  if(!p){p=document.createElement("div");p.id="ow45p";p.className="ow45-panel";p.setAttribute("role","dialog");p.setAttribute("aria-label","الملابس");document.body.appendChild(p);
    p.addEventListener("click",e=>{const b=e.target.closest("[data-ow]");if(b){const [id,k]=b.dataset.ow.split(":");if(k==="-")delete OW.pick[id];else OW.pick[id]=+k;owSave();owPanel();owRedraw();sfx("pop");}
      else if(e.target.closest(".ow45-x")){OW.open=false;owPanel();owButton();}});}
  const pic=id=>{const ic=iconOf(id);let a=ic?artSVG(ic,""):"";a=dressed(id,a)||"";return a.replace("<svg ",'<svg width="58" height="58" ');};
  p.innerHTML=`<div class="ow45-top"><b>👗 ${VOICE("الملابس")}</b><span class="ow45-tr">${VOICE("تجربة")}</span><button type="button" class="ow45-x" aria-label="${VOICE("سكّر")}">✕</button></div>`+
    here.map(id=>{const w=OUTFITS[id],k=OW.pick[id];return `<div class="ow45-row"><div class="ow45-pic">${pic(id)}<span>${VOICE(w.name)}</span></div><div class="ow45-ch">`+
      `<button type="button" class="ow45-o${k==null?" ow45-on":""}" data-ow="${id}:-" aria-pressed="${k==null}">${VOICE("بلا")}</button>`+
      w.o.map((o,i)=>`<button type="button" class="ow45-o${k===i?" ow45-on":""}" data-ow="${id}:${i}" aria-pressed="${k===i}">${VOICE(o.n)}</button>`).join("")+`</div></div>`;}).join("");}
/* the button in the corner (next to «🔊 الصوت» and «الجودة»): only in a book that has one of the three */
function owButton(){const bar=document.querySelector(".modebar");if(!bar)return;let b=document.getElementById("ow45b");const here=owHere();
  if(!here.length){if(b)b.remove();OW.open=false;owPanel();return;}
  if(!b){b=document.createElement("button");b.type="button";b.id="ow45b";b.className="ow45-b";bar.insertBefore(b,bar.firstChild);
    b.addEventListener("click",()=>{OW.open=!OW.open;owPanel();owButton();sfx("pop");});}
  b.textContent="👗 "+VOICE("الملابس");b.setAttribute("aria-pressed",String(OW.open));owPanel();}
