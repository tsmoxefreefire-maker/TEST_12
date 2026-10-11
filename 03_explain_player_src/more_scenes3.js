/* ===== 🆕 five new activities (batch 26): 🧪 recipe · ✏️ connect · ⚖️ compare · 🧑‍🏫 teach · 🪜 ladder =====
   🆕 batch 36: recipe, compare, teach and ladder were remade as games (acts36.js); ✏️ connect and the shared helpers stay here.
   Rules from the old mistakes (each one broke something before):
   · every class name starts with «na-» (the questions game also has .face .tail .lifted .card .on .done … on this page);
   · no CSS animation on a <g> that has a transform (only opacity, or an inner group);
   · no <button> inside a <button> (cards are <div role="button">, their words are plain text);
   · every word goes through VOICE / richText (the age's way of talking); « و» stays glued (richText);
   · the STUDENT does every move: video mode only plays the captions, it never plays the activity for him;
   · every move is explained (right → the reason · wrong → why it is wrong), and «💡 ساعدني» / a second try always opens the way;
   · a phone (≈380px) has its own layout; touch works by TAPPING (dragging is a bonus); timers check root.isConnected. */
const naTake=root=>{if(VIDEO)stopVideo(root);};                    /* the student touched it → the scene is his */
const naEsc=t=>String(t).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;");
const naQ=id=>"«"+exName(id)+"»";
function naEnds(a,b,ra,rb){const dx=b[0]-a[0],dy=b[1]-a[1],d=Math.hypot(dx,dy)||1;return [[a[0]+dx/d*ra,a[1]+dy/d*ra],[b[0]-dx/d*rb,b[1]-dy/d*rb]];}
function naKeys(el,fn){el.addEventListener("keydown",e=>{if(e.key==="Enter"||e.key===" "){e.preventDefault();fn();}});}

/* ✏️ CONNECT — the student draws the «needs» arrows himself: drag from the one who needs to what it needs (or tap them in order).
   Right → the arrow stays + the reason. Reversed → it is explained (the commonest mistake). No link → said so. */
function sceneConnect(s){const v=V(),W=v?380:640,H=v?480:390,c=[W/2,v?H/2:H/2-4],others=s.nodes.slice(1),n=others.length,TZ=v?96:104,OZ=v?64:70;
  const slots=v?[[296,80],[84,400],[296,400],[84,80],[190,54]]:[[544,80],[96,290],[544,290],[96,80],[588,186],[52,186]];   /* the corners first: far from the middle one */
  const pos={};pos[s.target]=c;shuffle(slots.slice(0,n),[...s.target].reduce((a,ch)=>a+ch.charCodeAt(0),7)).forEach((p,i)=>pos[others[i]]=p);   /* mixed: the place never tells who needs whom */
  const size=id=>id===s.target?TZ:OZ;
  const svg=`<svg class="xstage" id="xs" viewBox="0 0 ${W} ${H}" data-bubble="78" role="img" aria-label="${naEsc(VOICE("ارسم الأسهم"))}">${DEFS}<g id="naArrows"></g>
    ${node(s.target,c[0],c[1],TZ,"happy","star na-cn")}${others.map(id=>node(id,pos[id][0],pos[id][1],OZ,"happy","na-cn")).join("")}
    <g id="naTop" pointer-events="none"><line class="na-rubber" x1="0" y1="0" x2="0" y2="0" visibility="hidden"/></g></svg>
    <div class="row center na-crow"><span class="na-count" id="naCount" aria-live="polite"></span><button class="chipbtn na-help" id="naHelp">💡 ${VOICE("ساعدني")}</button></div>`;
  const req=s.links.map((l,k)=>k).filter(k=>s.links[k].required);
  return {svg,wire:root=>{let sel=null,drag=null;const drawn=new Set();const rub=root.querySelector(".na-rubber");
      gxStart(root,{kind:"connect",target:s.target,total:req.length,goal:"ارسم كل الأسهم: من اللي بيحتاج للي بيحتاجه"});   /* 🆕 batch 36: the game frame */
      const count=()=>{document.getElementById("naCount").textContent=`✏️ ${req.filter(k=>drawn.has(k)).length} ${VOICE("من")} ${req.length}`;};count();
      const toSvg=e=>{const pt=root.createSVGPoint();pt.x=e.clientX;pt.y=e.clientY;return pt.matrixTransform(root.getScreenCTM().inverse());};
      const hit=p=>{let best=null,bd=1e9;s.nodes.forEach(id=>{const q=pos[id],d=Math.hypot(p.x-q[0],p.y-q[1]);if(d<size(id)/2+18&&d<bd){bd=d;best=id;}});return best;};
      const select=id=>{sel=id;root.querySelectorAll(".na-cn").forEach(nd=>nd.classList.toggle("na-sel",nd.dataset.id===id));};
      const arrow=(a,b,cls)=>{const [p,q]=naEnds(pos[a],pos[b],size(a)/2+6,size(b)/2+12);const g=document.createElementNS(svgNS,"g");g.setAttribute("class","xedge lit na-arr "+(cls||""));
        g.innerHTML=flow(curve(p,q,16),"");root.querySelector("#naArrows").appendChild(g);return g;};
      const wrong=(a,b)=>{const [p,q]=naEnds(pos[a],pos[b],size(a)/2+6,size(b)/2+12);const l=document.createElementNS(svgNS,"line");
        l.setAttribute("class","na-wrongline");[["x1",p[0]],["y1",p[1]],["x2",q[0]],["y2",q[1]]].forEach(([k,x])=>l.setAttribute(k,x.toFixed(1)));
        root.querySelector("#naTop").appendChild(l);setTimeout(()=>l.remove(),900);};
      const finish=()=>{cap(s.end_say);sfx("ready");if(!grown())sparkles();gxWin(root);document.getElementById("naHelp").hidden=true;root.querySelectorAll(".na-ghost").forEach(x=>x.remove());};
      const attempt=(a,b)=>{const k=s.links.findIndex(l=>l.from===a&&l.to===b),r=s.links.findIndex(l=>l.from===b&&l.to===a);
        if(k>=0){if(drawn.has(k)){cap(VOICE("هاد السهم مرسوم ✔️"));return;}drawn.add(k);root.querySelectorAll(".na-ghost").forEach(x=>x.remove());
          arrow(a,b,s.links[k].required?"":"na-bonus");cap(s.links[k].ok_say);sfx("connect",{n:drawn.size});mood(root,a,"laugh");mood(root,b,"laugh");count();if(s.links[k].required)gxGood(root);
          if(s.links[k].required&&req.every(x=>drawn.has(x)))setTimeout(()=>{if(root.isConnected)finish();},900);}
        else if(r>=0){wrong(a,b);cap(s.links[r].rev_say);sfx("nope");gxBad(root);}
        else{wrong(a,b);cap(`🙂 ما في سهم مباشر بين ${naQ(a)} و${naQ(b)}.`);sfx("nope");gxBad(root);}};
      const rubber=(a,p)=>{if(!a){rub.setAttribute("visibility","hidden");return;}rub.setAttribute("visibility","visible");rub.setAttribute("x1",a[0]);rub.setAttribute("y1",a[1]);rub.setAttribute("x2",p[0].toFixed(1));rub.setAttribute("y2",p[1].toFixed(1));};
      root.querySelectorAll(".na-cn").forEach(nd=>{nd.style.touchAction="none";});
      root.addEventListener("pointerdown",e=>{const id=hit(toSvg(e));if(!id){if(sel)select(null);return;}naTake(root);e.preventDefault();
        if(sel&&sel!==id){const a=sel;select(null);attempt(a,id);return;}
        select(id);drag={id};try{root.setPointerCapture(e.pointerId);}catch(_){}});
      root.addEventListener("pointermove",e=>{if(drag){const p=toSvg(e);rubber(pos[drag.id],[p.x,p.y]);}});
      root.addEventListener("pointerup",e=>{if(!drag)return;const from=drag.id,id=hit(toSvg(e));drag=null;rubber(null);
        if(id&&id!==from){select(null);attempt(from,id);}
        else if(id===from){sfx("pick");cap(`👉 اخترت ${naQ(from)}. ${VOICE("هلأ اكبس على المفهوم الثاني.")}`);}});
      root.addEventListener("pointercancel",()=>{drag=null;rubber(null);});
      document.getElementById("naHelp").addEventListener("click",()=>{naTake(root);const k=req.find(x=>!drawn.has(x));if(k===undefined)return;const l=s.links[k];
        root.querySelectorAll(".na-ghost").forEach(x=>x.remove());arrow(l.from,l.to,"na-ghost");sfx("pick");cap(`💡 ${VOICE("جرّب")}: ${VOICE("من")} ${naQ(l.from)} ${VOICE("لـ")}${naQ(l.to)}.`);});}};}

SCENES.recipe=sceneRecipe;SNAME.recipe="🧪 الوصفة";SCENES.connect=sceneConnect;SNAME.connect="✏️ ارسم الأسهم";SCENES.compare=sceneCompare;SNAME.compare="⚖️ قارن";
SCENES.teach=sceneTeach;SNAME.teach="🧑‍🏫 علّم صاحبك";SCENES.ladder=sceneLadder;SNAME.ladder="🪜 السلّم";
