/* ================================================================ 🆕 batch 42 · THE LESSON'S PARTS, THREE NEW WAYS (explain_parts.py)
   Hareth: «مشهد أجزاء النبات… يصير في مشهد ثاني غيره، بس الهدف إنه يوصل المعلومة». The lessons take turns: 🧩 the puzzle ·
   🌱 build it from the ground up · ❓ what's missing? · 🎥 the camera tour. Same fact (the parts, and which needs which), another way.
   🌱 and ❓ are the student's (closed to the video, like every activity: batch 41); 🎥 is a film the video plays. */
function p42Lay(s,x0,x1,yb,yt){   /* the parts by level: the base at the bottom (yb), what sits on it higher up (yt) */
  const lv=s.levels,cols={};s.concepts.forEach(c=>{(cols[lv[c]]=cols[lv[c]]||[]).push(c);});
  const L=Object.keys(cols).map(Number).sort((a,b)=>a-b),pos={},floorY={};
  L.forEach((k,i)=>{const n=cols[k].length,y=L.length===1?(yb+yt)/2:yb-(i/(L.length-1))*(yb-yt);floorY[k]=y;
    cols[k].forEach((c,j)=>pos[c]=[x1-(j+1)/(n+1)*(x1-x0),y]);});
  return {pos,L,floorY};}
const p42Edges=(s,pos,cls)=>s.edges.map(([a,b])=>{const [p,q]=edgeEnds(pos[a],pos[b],42);return `<g class="xedge ${cls||""}" data-a="${a}" data-b="${b}">${flow(curve(p,q,0),"",0,false)}</g>`;}).join("");
const p42Lesson=()=>{try{return lesson().lesson_title;}catch(e){return "";}};

/* ---------------------------------------------------------------- 🌱 BUILD IT FROM THE GROUND UP */
function sceneBuildUp(s){const v=V(),n=s.concepts.length,nL=new Set(Object.values(s.levels)).size;
  const per=v?3:1,trayRows=v?Math.ceil(n/per):n,W=v?380:640;
  const stageH=Math.max(v?300:320,90+nL*(v?100:96)),H=v?stageH+trayRows*84+30:Math.max(stageH,40+n*82);
  const {pos,floorY}=p42Lay(s,v?20:30,v?W-20:430,stageH-60,70);
  const order=shuffle(s.concepts.map((_,i)=>i),[...s.concepts.join("")].reduce((a,c)=>a+c.charCodeAt(0),7));
  const tray=order.map((ci,j)=>v?[W-W*((j%per)+0.5)/per,stageH+44+Math.floor(j/per)*84]:[548,52+j*((H-80)/Math.max(1,n-1||1))]);
  const home={};order.forEach((ci,j)=>home[s.concepts[ci]]=tray[j]);
  const svg=`<svg class="xstage p42-build" id="xs" viewBox="0 0 ${W} ${H}" data-bubble="70" role="img" aria-label="${naEsc(VOICE("ابنيها من تحت"))}">${DEFS}
    ${Object.entries(floorY).map(([k,y])=>`<rect class="p42-floor" x="${v?14:22}" y="${y+40}" width="${v?W-28:420}" height="9" rx="4.5"/>`).join("")}
    <g id="p42Edges">${p42Edges(s,pos,"p42-off")}</g>
    ${s.concepts.map(c=>`<g class="p42-slot" data-id="${c}"><circle cx="${pos[c][0]}" cy="${pos[c][1]}" r="34"/><text x="${pos[c][0]}" y="${pos[c][1]+9}" text-anchor="middle">؟</text></g>`).join("")}
    ${v?`<rect class="tray" x="10" y="${stageH+4}" width="${W-20}" height="${trayRows*84+16}" rx="16"/>`:`<rect class="tray" x="470" y="16" width="156" height="${H-32}" rx="16"/>`}
    ${s.concepts.map(c=>node(c,home[c][0],home[c][1],58,"happy","piece p42-piece")).join("")}</svg>
    <p class="g4-count" id="p42Count" aria-live="polite">0 ${VOICE("من")} ${n}</p>`;
  return {svg,wire:root=>{const placed=new Set();let busy=false;
      gxStart(root,{kind:"build_up",target:s.order[0],total:n,goal:`${VOICE("ابني")} «${naEsc(p42Lesson())}» ${VOICE("من تحت لفوق")}: ${VOICE("كل جزء فوق اللي بيحتاجه")}`});
      const lit=()=>root.querySelectorAll("#p42Edges .xedge").forEach(e=>{const on=placed.has(e.dataset.a)&&placed.has(e.dataset.b);e.classList.toggle("p42-off",!on);e.classList.toggle("lit",on);});
      const tryPiece=el=>{const id=el.dataset.id;if(busy||placed.has(id))return;naTake(root);busy=true;
        const need=s.edges.filter(([a,b])=>b===id&&!placed.has(a)).map(([a])=>a);
        if(!need.length){const p0=g4Pos(el),t=pos[id];el.parentNode.appendChild(el);sfx("pick");
          g4Tween(root,520,u=>{const e=g4Ease(u);g4Move(el,p0[0]+(t[0]-p0[0])*e,p0[1]+(t[1]-p0[1])*e-Math.sin(e*Math.PI)*40,1,0);},()=>{
            placed.add(id);el.classList.add("placed");const sl=root.querySelector(`.p42-slot[data-id="${id}"]`);if(sl)sl.classList.add("filled");lit();
            mood(root,id,"laugh");say(root,id,s.says[id]||"");sfx("good");gxGood(root);cap("✨ "+naQ(id)+": "+(s.says[id]||""));
            document.getElementById("p42Count").textContent=`${placed.size} ${VOICE("من")} ${n}`;busy=false;
            if(placed.size===n){setTimeout(()=>{if(!root.isConnected)return;cap(VOICE("🎉 كل جزء قاعد فوق اللي بيحتاجه: هاي")+" «"+p42Lesson()+"» "+VOICE("كاملة!"));sfx("tada");if(!grown())sparkles();gxWin(root);},700);}});}
        else{sfx("nope");gxBad(root);mood(root,id,"o");
          cap(`🙃 ${naQ(id)} ${stNeeds(id)} ${need.map(naQ).join(" و")} ${VOICE("تحته أول")}.`);
          const p=g4Pos(el);g4Tween(root,420,u=>g4Move(el,p[0]+Math.sin(u*22)*7*(1-u),p[1],1,0),()=>{busy=false;mood(root,id,"happy");});}};
      root.querySelectorAll(".p42-piece").forEach(el=>{el.setAttribute("tabindex","0");el.setAttribute("role","button");el.addEventListener("click",()=>tryPiece(el));
        el.addEventListener("keydown",e=>{if(e.key==="Enter"||e.key===" "){e.preventDefault();tryPiece(el);}});});
      cap(VOICE("🌱 دوّر على الأساس: الجزء اللي ما بيحتاج إشي تحته."));}};}

/* ---------------------------------------------------------------- ❓ WHAT'S MISSING? */
function sceneMissing(s){const v=V(),nL=new Set(Object.values(s.levels)).size,W=v?380:640,H=Math.max(v?380:330,90+nL*(v?110:100));
  const {pos}=p42Lay(s,v?24:60,v?W-24:W-60,H-62,62);
  const svg=`<svg class="xstage p42-miss" id="xs" viewBox="0 0 ${W} ${H}" data-bubble="74" role="img" aria-label="${naEsc(VOICE("شو ناقص؟"))}">${DEFS}
    <g id="p42Edges">${p42Edges(s,pos,"")}</g>
    ${s.concepts.map(c=>node(c,pos[c][0],pos[c][1],70,"happy","p42-part")).join("")}<g id="p42Hole"></g></svg>
    <p class="g36-ask" id="p42Ask"></p><div class="na-opts g36-jopts" id="p42Opts"></div>`;
  return {svg,wire:root=>{const box=document.getElementById("p42Opts"),q=document.getElementById("p42Ask");let r=0,busy=false;
      gxStart(root,{kind:"missing",target:s.rounds[0].id,total:s.rounds.length,goal:`${VOICE("رجّع الجزء الناقص لصورة")} «${naEsc(p42Lesson())}»`});
      const nd=id=>root.querySelector(`.xnode[data-id="${id}"]`);
      const hide=id=>{const p=pos[id];nd(id).classList.add("g36-hidden");root.querySelector("#p42Hole").innerHTML=`<g class="p42-hole"><circle cx="${p[0]}" cy="${p[1]}" r="38"/><text x="${p[0]}" y="${p[1]+12}" text-anchor="middle">؟</text></g>`;
        root.querySelectorAll("#p42Edges .xedge").forEach(e=>{const touch=e.dataset.a===id||e.dataset.b===id;e.classList.toggle("dim",touch);e.classList.remove("lit");});
        s.edges.filter(([a])=>a===id).forEach(([,b])=>{nd(b).classList.add("tired");mood(root,b,"sad");});};
      const back=id=>{nd(id).classList.remove("g36-hidden");root.querySelector("#p42Hole").innerHTML="";mood(root,id,"laugh");
        root.querySelectorAll("#p42Edges .xedge").forEach(e=>{const touch=e.dataset.a===id||e.dataset.b===id;e.classList.remove("dim");e.classList.toggle("lit",touch);});
        s.edges.filter(([a])=>a===id).forEach(([,b])=>{nd(b).classList.remove("tired");mood(root,b,"laugh");});};
      const round=()=>{const R=s.rounds[r];hide(R.id);busy=false;
        const sad=s.edges.filter(([a])=>a===R.id).map(([,b])=>b);
        if(sad.length)say(root,sad[0],VOICE("في إشي ناقصني! 😢"));
        q.innerHTML=t37(VOICE(`👇 ${sad.length?`${sad.map(naQ).join(" و")} ${sad.length>1?"زعلانين":stFem(exName(sad[0]))?"زعلانة":"زعلان"}… `:""}مين الجزء الناقص؟`));
        const opts=shuffle(R.options.map(id=>({id,ok:id===R.id})),r*7+3).map(o=>Object.assign(o,{label:exName(o.id),art:g36Art(o.id)}));
        g36Opts(box,opts,(j,b)=>{if(busy)return;naTake(root);const o=opts[j];
          if(o.ok){busy=true;box.querySelectorAll(".na-opt").forEach(x=>x.disabled=true);b.classList.add("g36-right");back(R.id);sfx("good");gxGood(root);
            cap("✅ "+naQ(R.id)+(R.say?": "+R.say:"")+". "+R.why);
            setTimeout(()=>{if(!root.isConnected)return;r++;if(r<s.rounds.length)round();else{box.innerHTML="";q.textContent="";cap(VOICE("🎉 رجعت كل الأجزاء، والكل رجع يشتغل!"));sfx("tada");if(!grown())sparkles();gxWin(root);}},1700);}
          else{b.disabled=true;b.classList.add("na-wrong");sfx("nope");gxBad(root);mood(root,o.id,"o");
            cap(`🙂 ${naQ(o.id)} ${VOICE(g4V(o.id,"موجود","موجودة"))} ${VOICE("بالصورة. دوّر على المكان الفاضي ومين زعلان.")}`);}});};
      round();}};}

/* ---------------------------------------------------------------- 🎥 THE CAMERA TOUR (a film: one part per step, from the base up) */
function sceneTour(s){const v=V(),nL=new Set(Object.values(s.levels)).size,W=v?380:640,H=Math.max(v?380:330,90+nL*(v?110:100));
  const {pos}=p42Lay(s,v?24:60,v?W-24:W-60,H-62,62);
  const svg=`<svg class="xstage p42-tour" id="xs" viewBox="0 0 ${W} ${H}" data-bubble="74" role="img" aria-label="${naEsc(VOICE("جولة الكاميرا"))}">${DEFS}
    <g id="p42Edges">${p42Edges(s,pos,"")}</g>${s.concepts.map(c=>node(c,pos[c][0],pos[c][1],72,"happy","p42-part")).join("")}</svg>`;
  return {svg,wire:root=>{root.querySelectorAll(".xnode").forEach(n=>n.addEventListener("click",()=>{const id=n.dataset.id;sfx("pop");say(root,id,s.says[id]||"");mood(root,id,"laugh");}));},
    onStep:(root,k)=>{const seen=new Set(s.order.slice(0,k));say(root,null,"");
      root.querySelectorAll(".xnode").forEach(n=>{const id=n.dataset.id;n.classList.toggle("sleep",k>0&&!seen.has(id));n.classList.toggle("woke",seen.has(id));});
      root.querySelectorAll("#p42Edges .xedge").forEach(e=>{const on=k>0&&seen.has(e.dataset.a)&&seen.has(e.dataset.b);e.classList.toggle("lit",on);e.classList.toggle("dim",k>0&&!on);});
      if(k>0){const id=s.order[k-1];mood(root,id,"laugh");focus(root,[id].concat((s.stops[k-1]||{}).under||[]));}else focus(root,null);}};}

SCENES.build_up=sceneBuildUp;SNAME.build_up="🌱 ابنيها من تحت";SCENES.missing=sceneMissing;SNAME.missing="❓ شو ناقص؟";SCENES.tour=sceneTour;SNAME.tour="🎥 جولة الكاميرا";
