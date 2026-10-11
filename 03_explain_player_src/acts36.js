/* ===== 🆕 batch 36 (Hareth: «في فعاليات بتحس إنك بس بتلمس وتحط… بدها تكون حلوة كثير… الطالب يتعلم ويستمتع») · SIX ACTIVITIES, REMADE =====
   Each one now asks the student to DECIDE something (not just to tap everything), and answers with a little show:
   · 🍽️ recipe  → «أطعم X»: some of the food is not his! Right food → he eats it (يمّ!) and it sits by him with its arrow; wrong → «يع!» and why.
                  Take one back → he is hungry again (he needs ALL of them). The older stages: «جهّز الشروط» (no food words).
   · ⚖️ compare → the facts fall one at a time from the top; send each to «X», to «Y» or to «الاثنين» — its owner catches it.
   · 💡 teach   → your friend's head is full of ❓: every right answer turns one ❓ into 💡; a wrong one makes him more confused.
   · 🪜 ladder  → every rung is a CHOICE (the right one + wrong ones); a little climber goes down rung by rung.
   · 🧭 journey → the next stations are hidden (؟): choose where to go next from the cards; the spark travels there and it wakes up.
   · 🔮 what_if → FIRST guess who will get tired, THEN switch it off and see: each guess is checked (✅ / ❌ and why).
   All the facts come from the factory (checked against the graph). The game frame (mission, stars, the place's party) is games36.js.
   Same old rules: «na-» classes (+ «g36-») · the STUDENT plays (🆕 batch 41: the video never plays it for him, it waits) · every move explained ·
   tapping always works (dragging is a bonus) · a phone has its own layout · timers check root.isConnected. */
const g36Seed=id=>[...String(id)].reduce((a,c)=>a+c.charCodeAt(0),7);
function g36Opts(box,opts,onPick){box.innerHTML=opts.map((o,k)=>`<button class="na-opt g36-opt" data-k="${k}" data-id="${o.id}">${o.art?`<span class="g36-oart" aria-hidden="true">${o.art}</span>`:""}<span>${naEsc(o.label)}</span></button>`).join("");
  box.querySelectorAll(".na-opt").forEach(b=>b.addEventListener("click",()=>onPick(+b.dataset.k,b)));}
const g36Art=id=>{const ic=iconOf(id);const a=ic?dressed(id,artSVG(ic,"")):null;return a?a.replace("<svg ",'<svg width="30" height="30" '):"";};

/* ---------------------------------------------------------------- 🍽️ RECIPE → «أطعم X» (the older stages: «جهّز الشروط») */
function sceneRecipe(s){const v=V(),young=!grown(),n=s.needs.length;
  const items=shuffle(s.needs.map(x=>({id:x.id,ok:true,why:x.why})).concat((s.decoys||[]).map(x=>({id:x.id,ok:false,why:x.why}))),g36Seed(s.target)),m=items.length;
  const W=v?380:640,Z=v?100:118,IZ=v?60:64,cols=v?Math.min(3,m):2,rows=Math.ceil(m/cols);
  const H=v?204+rows*96+24:Math.max(360,92+rows*104);
  const T=v?[W/2,112]:[190,H/2+6];
  const tray=items.map((_,i)=>v?[W*((i%cols)+0.5)/cols,250+Math.floor(i/cols)*96]:[W-170+(i%2)*104,62+Math.floor(i/2)*((H-130)/Math.max(1,rows-1||1))]);
  if(!v&&rows===1)tray.forEach(p=>{p[1]=H/2;});
  const R=Z/2+14,slot=k=>{const a=v?Math.PI*(1+(n===1?0.5:k/(n-1))):(-Math.PI*0.28+Math.PI*0.56*(n===1?0.5:k/(n-1)));return [T[0]+Math.cos(a)*(R+IZ*0.36),T[1]+Math.sin(a)*(R+IZ*0.36)];};
  const C=2*Math.PI*R;
  const table=v?`<rect class="g36-table" x="14" y="204" width="${W-28}" height="${rows*96+8}" rx="18"/>`:`<rect class="g36-table" x="${W-232}" y="18" width="210" height="${H-36}" rx="22"/>`;
  const svg=`<svg class="xstage g36-recipe${young?"":" g36-lab"}" id="xs" viewBox="0 0 ${W} ${H}" data-bubble="78" role="img" aria-label="${naEsc(VOICE(young?"أطعم":"الشروط"))}">${DEFS}
    ${table}${items.map((_,i)=>`<ellipse class="g36-plate" cx="${tray[i][0]}" cy="${tray[i][1]+IZ*0.42}" rx="${IZ*0.55}" ry="${IZ*0.16}"/>`).join("")}
    <g id="naArr"></g>${s.needs.map((_,k)=>{const q=slot(k);return `<circle class="g36-slot" cx="${q[0].toFixed(1)}" cy="${q[1].toFixed(1)}" r="${(IZ*0.33).toFixed(1)}"/>`;}).join("")}
    <circle class="na-ring0" cx="${T[0]}" cy="${T[1]}" r="${R}"/><circle class="na-ring" cx="${T[0]}" cy="${T[1]}" r="${R}" stroke-dasharray="0 ${C.toFixed(1)}" style="opacity:0" transform="rotate(-90 ${T[0]} ${T[1]})"/>
    ${node(s.target,T[0],T[1],Z,"sad","star na-tgt").replace(`class="xname" y="${Z/2+18}"`,`class="xname" y="${Z/2+30}"`)}
    <g id="g36Items">${items.map((x,i)=>node(x.id,tray[i][0],tray[i][1],IZ,"happy","na-ing").replace('class="xnode','data-i="'+i+'" class="xnode')).join("")}</g></svg>
    <p class="na-count" id="naCount" aria-live="polite">0 ${VOICE("من")} ${n}</p>`;
  return {svg,wire:root=>{const eaten=new Map(),tried=new Set();let busy=false,wasAll=false;const tgt=root.querySelector(".na-tgt"),me=s.target;
      gxStart(root,{kind:"recipe",target:me,total:n,goal:young?`أطعم ${naQ(me)} كل اللي ${stFem(exName(me))?"بتحتاجه":"بيحتاجه"}`:`جهّز كل شروط ${naQ(me)}`});
      say(root,me,young?(stFem(exName(me))?"جوعانة! 😋 شو بتطعميني؟":"جوعان! 😋 شو بتطعميني؟"):"شو شروطي؟");
      const ring=()=>{const k=eaten.size;const r=root.querySelector(".na-ring");r.setAttribute("stroke-dasharray",`${(C*k/n).toFixed(1)} ${C.toFixed(1)}`);r.style.opacity=k?1:0;
        document.getElementById("naCount").textContent=`${k} ${VOICE("من")} ${n}`;gxSet(root,k);};
      const freeSlot=()=>{const used=new Set([...eaten.values()].map(e=>e.k));for(let k=0;k<n;k++)if(!used.has(k))return k;return 0;};
      const el=i=>root.querySelector(`.na-ing[data-i="${i}"]`);
      const home=(i,ms,cb)=>{const e=el(i),p=g4Pos(e),q=tray[i];g4Tween(root,ms,t=>{const u=g4Ease(t);g4Move(e,p[0]+(q[0]-p[0])*u,p[1]+(q[1]-p[1])*u-50*4*t*(1-t),1,0);},cb);};
      const eat=i=>{if(busy||eaten.has(i))return;const x=items[i],e=el(i);if(tried.has(i)&&!x.ok){cap(x.why);return;}busy=true;naTake(root);
        const p0=g4Pos(e),mouth=[T[0],T[1]+Z*0.12];mood(root,me,"o");sfx("pick");e.parentNode.appendChild(e);
        g4Tween(root,560,t=>{const u=g4Ease(t);g4Move(e,p0[0]+(mouth[0]-p0[0])*u,p0[1]+(mouth[1]-p0[1])*u-70*4*t*(1-t),1-0.35*u,0);},()=>{
          if(x.ok){const k=freeSlot(),q=slot(k);eaten.set(i,{k});e.classList.add("na-eaten");gxReact(root,me,true);if(young)say(root,me,"يمّ! 😋");
            sfx("good");cap(x.why);gxGood(root);
            g4Tween(root,320,t=>{const u=g4Ease(t);g4Move(e,mouth[0]+(q[0]-mouth[0])*u,mouth[1]+(q[1]-mouth[1])*u,0.65-0.05*u,0);},()=>{
              const a=g4Arrow(root.querySelector("#naArr"),T,q,R+2,IZ*0.31+4);a.dataset.i=i;ring();busy=false;
              const all=eaten.size===n;tgt.classList.toggle("na-ready",all);mood(root,me,all?"laugh":"happy");
              if(all){cap(s.ready);setTimeout(()=>{if(root.isConnected)sfx("tada");},220);if(!grown()&&!wasAll)sparkles();say(root,me,young?"شبعت! 😄 شكراً":"✅");gxWin(root);}
              wasAll=all;});}
          else{tried.add(i);mood(root,me,"angry");gxReact(root,me,false);if(young)say(root,me,"يع! 😝");sfx("nope");cap((young?"😝 ":"")+x.why);gxBad(root);e.classList.add("g4-no");
            home(i,560,()=>{busy=false;setTimeout(()=>{if(root.isConnected)mood(root,me,eaten.size?"happy":"sad");},500);});}});};
      /* take one back: he needs ALL of them (the old «turn one off» lesson) */
      const giveBack=i=>{if(busy)return;const k=eaten.get(i);if(!k)return;busy=true;naTake(root);eaten.delete(i);const e=el(i);e.classList.remove("na-eaten");
        const a=root.querySelector(`#naArr .g4-arr[data-i="${i}"]`);if(a)a.remove();tgt.classList.remove("na-ready");wasAll=false;ring();mood(root,me,"sad");sfx("off",{n:0});
        const miss=s.needs.filter(x=>![...eaten.keys()].some(j=>items[j].id===x.id)).map(x=>naQ(x.id));
        cap(VOICE(`⛔ شلت ${naQ(items[i].id)}: ${naQ(me)} ${stFem(exName(me))?"رجعت ناقصها":"رجع ناقصه"} ${miss.join(" و")}، لأنه ${stNeeds(me)} الكل مع بعض.`));
        home(i,480,()=>{busy=false;});};
      /* tap = eat (or give back) · drag to him = eat · drag elsewhere = back to the table */
      root.querySelectorAll(".na-ing").forEach(e=>{const i=+e.dataset.i;let d=null;e.style.touchAction="none";
        e.addEventListener("pointerdown",ev=>{if(busy)return;ev.preventDefault();try{e.setPointerCapture(ev.pointerId);}catch(_){}const p=g4Pt(root,ev),q=g4Pos(e);d={x0:p.x,y0:p.y,q,moved:0};});
        e.addEventListener("pointermove",ev=>{if(!d||eaten.has(i))return;const p=g4Pt(root,ev);d.moved=Math.max(d.moved,Math.hypot(p.x-d.x0,p.y-d.y0));if(d.moved>8)g4Move(e,d.q[0]+p.x-d.x0,d.q[1]+p.y-d.y0,1.08,0);});
        const up=ev=>{if(!d)return;const dd=d;d=null;if(eaten.has(i)){if(dd.moved<8)giveBack(i);return;}
          if(dd.moved<8){eat(i);return;}const p=g4Pos(e);if(Math.hypot(p[0]-T[0],p[1]-T[1])<Z*0.9){g4Move(e,p[0],p[1],1,0);eat(i);}else home(i,300);};
        e.addEventListener("pointerup",up);e.addEventListener("pointercancel",up);naKeys(e,()=>eaten.has(i)?giveBack(i):eat(i));});}};}

/* ---------------------------------------------------------------- ⚖️ COMPARE → the facts fall one at a time */
function sceneCompare(s){const v=V(),W=v?380:640,H=v?196:216,Z=v?76:90,A=s.target,B=s.other;
  const pa=[W*0.77,H/2-10],pb=[W*0.23,H/2-10];
  const svg=`<svg class="xstage" id="xs" viewBox="0 0 ${W} ${H}" role="img" aria-label="${naEsc(VOICE("قارن"))}">
    <ellipse class="na-venn na-va" cx="${W*0.62}" cy="${H/2}" rx="${W*0.25}" ry="${H*0.45}"/><ellipse class="na-venn na-vb" cx="${W*0.38}" cy="${H/2}" rx="${W*0.25}" ry="${H*0.45}"/>
    <text class="na-vlab" x="${W/2}" y="${H/2+5}" text-anchor="middle">${VOICE("الاثنين")}</text>
    ${node(A,pa[0],pa[1],Z,"happy","na-ca")}${node(B,pb[0],pb[1],Z,"happy","na-cb")}</svg>
    <div class="g36-lane" id="naTray" aria-live="polite"></div><p class="g36-left" id="g36Left"></p>
    <div class="na-zones">${[["a",exName(A)],["both",VOICE("الاثنين")],["b",exName(B)]].map(([k,t])=>`<div class="na-zone na-z-${k}" role="button" tabindex="0" data-side="${k}"><b class="na-zh">${naEsc(t)}</b><div class="na-zl"></div></div>`).join("")}</div>`;
  return {svg,wire:root=>{let at=0,busy=false;const tries={},F=s.facts,lane=document.getElementById("naTray");
      gxStart(root,{kind:"compare",target:A,total:F.length,goal:`ودّي كل بطاقة لمكانها: ${naQ(A)}، ${naQ(B)} ولا الاثنين`});
      const left=()=>{const k=F.length-at;document.getElementById("g36Left").textContent=k>1?`🃏 ${k-1} ${VOICE("بطاقات كمان بعدها")}`:"";};
      const show=()=>{if(at>=F.length){lane.innerHTML="";left();return;}const f=F[at];
        lane.innerHTML=`<div class="na-card na-picked g36-fall" role="button" tabindex="0" data-i="${at}" aria-pressed="true">${t37(naEsc(VOICE(f.fact)))}</div>`;left();
        const c=lane.firstElementChild;c.addEventListener("click",()=>{c.classList.remove("g36-wig");void c.offsetWidth;c.classList.add("g36-wig");sfx("pick");cap(VOICE("👇 هلأ اكبس على مكانها تحت."));});sfx("pick");};
      const owners=side=>side==="both"?[A,B]:[side==="a"?A:B];
      const place=(side,auto)=>{const i=at,f=F[i],card=lane.querySelector(".na-card");if(!card)return;busy=true;
        const z=document.querySelector(`.na-zone[data-side="${side}"]`),zr=z.getBoundingClientRect(),cr=card.getBoundingClientRect();
        card.classList.remove("g36-fall");card.style.transition="transform .45s ease-in, opacity .45s ease-in";card.style.transform=`translate(${(zr.left+zr.width/2-cr.left-cr.width/2).toFixed(0)}px,${(zr.top+18-cr.top).toFixed(0)}px) scale(.6)`;card.style.opacity=".2";
        setTimeout(()=>{if(!root.isConnected)return;const d=document.createElement("div");d.className="na-placed";d.innerHTML="✔️ "+t37(naEsc(VOICE(f.fact)));z.querySelector(".na-zl").appendChild(d);card.remove();
          cap((auto?"💡 ":"")+f.why);sfx(auto?"pick":"place");owners(side).forEach(id=>{mood(root,id,"laugh");gxReact(root,id,true);});if(!auto)gxGood(root);else gxSet(root,i+1);
          at++;busy=false;if(at>=F.length){show();setTimeout(()=>{if(!root.isConnected)return;cap(s.end_say);sfx("ready");if(!grown())sparkles();gxWin(root);},900);}else setTimeout(()=>{if(root.isConnected&&!busy)show();},500);},460);};
      const drop=side=>{naTake(root);if(busy||at>=F.length)return;const f=F[at];
        if(f.side===side){place(side,false);return;}
        tries[at]=(tries[at]||0)+1;const z=document.querySelector(`.na-zone[data-side="${side}"]`);z.classList.remove("na-nope");void z.offsetWidth;z.classList.add("na-nope");sfx("nope");gxBad(root);
        owners(side).forEach(id=>{mood(root,id,"o");gxReact(root,id,false);});
        const c=lane.querySelector(".na-card");if(c){c.classList.remove("g36-fall","g36-bounce");void c.offsetWidth;c.classList.add("g36-bounce");}
        if(tries[at]>=2)place(f.side,true);else cap(VOICE("🙂 مش هون. فكّر فيها كمان، وجرّب مكان ثاني."));};
      document.querySelectorAll(".na-zone").forEach(z=>{z.addEventListener("click",()=>drop(z.dataset.side));naKeys(z,()=>drop(z.dataset.side));});
      show();}};}

/* ---------------------------------------------------------------- 💡 TEACH → turn his ❓ into 💡 */
function sceneTeach(s){const v=V(),W=v?380:640,st=stageNow(),Z=v?90:104,TOP=v?58:62,H=(v?226:236)+TOP;
  const mate=st==="kids"?skin().name:st==="junior"?"صاحبك":"زميلك";
  const M=v?[92,104+TOP]:[180,108+TOP],T=v?[W-96,104+TOP]:[W-180,108+TOP];
  const person=`<svg class="ch" viewBox="0 0 100 100"><circle cx="50" cy="34" r="19" style="fill:var(--chip);stroke:var(--brand)" stroke-width="3"/><path d="M16 94 Q18 60 50 58 Q82 60 84 94 Z" style="fill:var(--chip);stroke:var(--brand)" stroke-width="3"/></svg>`;
  const mart=((st==="kids"||st==="junior")&&artSVG(skin().mascot,""))||person;
  const n=s.rounds.length,cw=v?150:176,cx=M[0]+(v?44:58),cy=v?38:40;
  const cloud=`<g class="g36-think" transform="translate(${cx} ${cy})"><circle class="g36-tb" cx="${-cw*0.42}" cy="${TOP*0.62}" r="4"/><circle class="g36-tb" cx="${-cw*0.33}" cy="${TOP*0.42}" r="6"/>
      <path class="g36-cloud" d="M-60 14 A18 18 0 0 1 -50 -12 A22 22 0 0 1 -12 -26 A24 24 0 0 1 30 -22 A20 20 0 0 1 62 0 A16 16 0 0 1 56 26 L-52 26 A14 14 0 0 1 -60 14 Z" transform="scale(${(cw/125).toFixed(2)} 1)"/>
      ${s.rounds.map((_,k)=>`<text class="g36-q" data-k="${k}" x="${(-cw*0.36+cw*0.72*(n===1?0.5:k/(n-1))).toFixed(1)}" y="10" text-anchor="middle">❓</text>`).join("")}</g>`;
  const svg=`<svg class="xstage" id="xs" viewBox="0 0 ${W} ${H}" data-bubble="70" role="img" aria-label="${naEsc(VOICE("اشرح لزميلك"))}">${cloud}
    <g class="xnode na-mate" data-id="__mate" transform="translate(${M[0]} ${M[1]})"><g class="xbody" data-mood="o">${mart.replace("<svg ",`<svg width="${Z}" height="${Z}" x="${-Z/2}" y="${-Z/2}" `)}</g><text class="xname" y="${Z/2+18}" text-anchor="middle">${naEsc(mate)}</text><g class="xsay"></g></g>
    ${node(s.target,T[0],T[1],Z,"happy","star")}</svg>
    <div class="na-chat" id="naChat" aria-live="polite"></div><div class="na-opts" id="naOpts"></div><div class="na-note" id="naNote" hidden></div>`;
  return {svg,wire:root=>{let r=0;const chat=document.getElementById("naChat"),opts=document.getElementById("naOpts");
      gxStart(root,{kind:"teach",target:s.target,total:n,goal:`خلّي ${mate} يفهم ${naQ(s.target)}: حوّل كل ❓ لـ 💡`});
      const q=k=>root.querySelector(`.g36-q[data-k="${k}"]`);
      const msg=(who,html)=>{chat.insertAdjacentHTML("beforeend",`<div class="na-msg na-${who}">${who==="them"?`<b>${naEsc(mate)}:</b> `:""}${html}</div>`);};
      const ask=()=>{const R=s.rounds[r];msg("them",t37(naEsc(VOICE(R.ask))));mood(root,"__mate","o");const e=q(r);if(e)e.classList.add("g36-now");
        opts.innerHTML=R.options.map((o,k)=>`<button class="na-opt" data-k="${k}">${t37(naEsc(VOICE(o.opt)))}</button>`).join("");
        opts.querySelectorAll(".na-opt").forEach(b=>b.addEventListener("click",()=>choose(+b.dataset.k,b)));};
      const end=()=>{const note=document.getElementById("naNote");note.hidden=false;note.innerHTML=richText(s.learnt);cap(s.learnt);sfx("ready");if(!grown())sparkles();
        root.querySelector(".g36-think").classList.add("g36-lit");say(root,"__mate",VOICE(st==="kids"?"هلأ فهمت! شكراً 😄":"هلأ وضحت. شكراً."));mood(root,"__mate","laugh");gxReact(root,"__mate",true);gxWin(root);};
      const choose=(k,b)=>{naTake(root);const R=s.rounds[r],o=R.options[k];msg("me",t37(naEsc(VOICE(o.opt))));const e=q(r);
        if(o.ok){opts.innerHTML="";msg("them",richText(o.reply));cap(o.reply);sfx("place");mood(root,"__mate","laugh");mood(root,s.target,"laugh");gxReact(root,"__mate",true);gxGood(root);
          if(e){e.textContent="💡";e.classList.remove("g36-now","g36-big");e.classList.add("g36-got");}r++;
          setTimeout(()=>{if(!root.isConnected)return;if(r<s.rounds.length)ask();else end();},1300);}
        else{b.disabled=true;b.classList.add("na-wrong");msg("them",richText(o.reply));cap(o.reply);sfx("nope");mood(root,"__mate","sad");gxReact(root,"__mate",false);gxBad(root);
          if(e){e.classList.remove("g36-big");void e.getBoundingClientRect();e.classList.add("g36-big");}}};
      ask();}};}

/* ---------------------------------------------------------------- 🪜 LADDER → every rung is a choice; a little climber goes down */
function sceneLadder(s){const v=V(),n=s.rungs.length,W=v?380:640,G=v?128:140,TZ=v?94:100,Z=v?68:72;const H=72+G*n+82;
  const ids=[s.target].concat(s.rungs.map(r=>r.id));const dx=v?72:112;
  const pos=ids.map((id,k)=>[W/2+(k%2?-dx:dx),66+k*G]);const rail=v?160:200;
  const climber=!grown()?((artSVG(skin().mascot,"")||"").replace("<svg ",'<svg width="46" height="46" x="-23" y="-40" ')):"";
  const svg=`<svg class="xstage" id="xs" viewBox="0 0 ${W} ${H}" data-bubble="74" role="img" aria-label="${naEsc(VOICE("السلّم"))}">${DEFS}
    <path class="na-rail" d="M${W/2-rail} 26 V${H-30} M${W/2+rail} 26 V${H-30}"/>${ids.slice(1).map((_,k)=>`<path class="na-rungline" d="M${W/2-rail} ${66+(k+1)*G} H${W/2+rail}"/>`).join("")}
    ${ids.slice(1).map((id,k)=>`<g class="na-slot" data-k="${k+1}"><circle cx="${pos[k+1][0]}" cy="${pos[k+1][1]}" r="${Z/2-4}"/><text x="${pos[k+1][0]}" y="${pos[k+1][1]+9}" text-anchor="middle">؟</text></g>`).join("")}
    <g id="naArrows"></g>${ids.map((id,k)=>node(id,pos[k][0],pos[k][1],k?Z:TZ,"happy",k?"na-hid":"star")).join("")}
    ${climber?`<g class="g36-climb" id="g36Climb" transform="translate(${W/2} ${66+12})"><g class="g36-cb">${climber}</g></g>`:""}</svg>
    <p class="g36-ask" id="g36Ask"></p><div class="na-opts g36-lopts" id="naOpts"></div>
    <div class="row center na-lrow"><button class="btn na-ask" id="naAsk" hidden>${s.mode==="why"?"❓ "+VOICE("ليش؟"):"⏭️ "+VOICE("وبعدين؟")}</button><button class="btn ghost" id="naReset" hidden>↺ ${VOICE("من الأول")}</button></div>`;
  return {svg,wire:root=>{let k=0,busy=false;const ask=document.getElementById("naAsk"),reset=document.getElementById("naReset"),box=document.getElementById("naOpts"),q=document.getElementById("g36Ask");
      gxStart(root,{kind:"ladder",target:s.target,total:n,goal:s.mode==="why"?`انزل السلّم لآخره: مين ورا ${naQ(s.target)}؟`:`انزل السلّم لآخره: شو بيجي بعد ${naQ(s.target)}؟`});
      const up=(a,b)=>s.mode==="why"?[a,b]:[b,a];
      const climbTo=i=>{const c=root.querySelector("#g36Climb");if(!c)return;const p=g4Pos(c),y=66+i*G+12;g4Tween(root,700,t=>g4Move(c,W/2,p[1]+(y-p[1])*g4Ease(t),1,Math.sin(t*Math.PI*4)*6),null);};
      const open=()=>{const r=s.rungs[k];const [a,b]=up(ids[k],ids[k+1]),ia=ids.indexOf(a),ib=ids.indexOf(b);
        root.querySelector(`.xnode[data-id="${ids[k+1]}"]`).classList.remove("na-hid");root.querySelector(`.na-slot[data-k="${k+1}"]`).classList.add("na-found");
        const sg=pos[ib][0]>pos[ia][0]?1:-1,p=[pos[ia][0]+sg*((ia?Z:TZ)/2+6),pos[ia][1]],qq=[pos[ib][0]-sg*((ib?Z:TZ)/2+12),pos[ib][1]];
        const g=document.createElementNS(svgNS,"g");g.setAttribute("class","xedge lit na-arr");g.innerHTML=flow(curve(p,qq,14),"");root.querySelector("#naArrows").appendChild(g);
        say(root,a,r.short);cap(r.because);mood(root,ids[k+1],"laugh");gxReact(root,ids[k+1],true);sfx("rung",{n:k,down:s.mode==="why"});k++;climbTo(k);
        if(k>=n){box.innerHTML="";q.textContent="";ask.hidden=true;setTimeout(()=>{if(!root.isConnected)return;cap(s.end_say);sfx("ready");if(!grown())sparkles();reset.hidden=false;gxWin(root);},1500);}
        else setTimeout(()=>{if(root.isConnected)offer();},900);};
      const offer=()=>{busy=false;const r=s.rungs[k],wrong=r.wrong||[];
        if(!wrong.length){box.innerHTML="";q.textContent="";ask.hidden=false;return;}                 /* nothing wrong to offer on this rung: the old «ليش؟ / وبعدين؟» */
        ask.hidden=true;const prev=ids[k];q.innerHTML=t37(VOICE(s.mode==="why"?`👇 ${naQ(prev)} ${stNeeds(prev)} مين؟`:`👇 مين ${ARROW_WORD()} ${naQ(prev)}؟`));
        const opts=shuffle([{id:r.id,ok:true}].concat(wrong.map(w=>({id:w.id,ok:false,say:w.say}))),g36Seed(r.id)+k).map(o=>Object.assign(o,{label:exName(o.id),art:g36Art(o.id)}));
        g36Opts(box,opts,(j,b)=>{if(busy)return;naTake(root);const o=opts[j];
          if(o.ok){busy=true;b.classList.add("g36-right");sfx("good");gxGood(root);setTimeout(()=>{if(root.isConnected)open();},350);}
          else{b.disabled=true;b.classList.add("na-wrong");cap(o.say);sfx("nope");gxBad(root);const sl=root.querySelector(`.na-slot[data-k="${k+1}"]`);if(sl){sl.classList.remove("g36-wobble");void sl.getBoundingClientRect();sl.classList.add("g36-wobble");}}});};
      ask.addEventListener("click",()=>{naTake(root);if(k>=n||busy)return;busy=true;gxGood(root);open();});
      reset.addEventListener("click",()=>{renderScene();});
      offer();}};}

/* ---------------------------------------------------------------- 🧭 JOURNEY → choose the next station (the ones ahead are hidden) */
function sceneJourney(s){const v=V(),n=s.route.length;
  const W=v?380:Math.max(640,n*160),H=v?Math.max(460,n*135+60):320;
  const pos=s.route.map((x,i)=>v?[i%2?120:260,90+i*((H-160)/(n-1))]:[W-90-i*((W-180)/(n-1)),200+(i%2?-24:24)]);
  const segs=pos.slice(1).map((p,i)=>{const [a,b]=edgeEnds(pos[i],p,46);return curve(a,b,v?0:26);});
  const mover=s.traveller!=="spark";const ti=mover?iconOf(s.traveller):null;
  const tart=mover?((ti?dressed(s.traveller,artSVG(ti,"")):null)||`<svg class="ch" viewBox="0 0 100 100">${ARTS.blob(colorOf(s.traveller))}</svg>`):"";
  const svg=`<svg class="xstage" id="xs" viewBox="0 0 ${W} ${H}" data-bubble="84" role="img" aria-label="رحلة">${DEFS}
    ${segs.map((d,i)=>`<path class="xroad" data-i="${i}" d="${d}"/><path class="xglow" data-i="${i}" d="${d}"/>`).join("")}
    ${s.route.map((x,i)=>i?`<g class="g36-hole" data-i="${i}"><circle cx="${pos[i][0]}" cy="${pos[i][1]}" r="34"/><text x="${pos[i][0]}" y="${pos[i][1]+10}" text-anchor="middle">؟</text></g>`:"").join("")}
    ${s.route.map((x,i)=>node(x,pos[i][0],pos[i][1],76,i===0?"happy":"sad",i===0?"woke":"sleep g36-hidden")).join("")}
    ${mover?`<g id="trav"><g class="xbody" data-mood="laugh">${tart.replace("<svg ",'<svg width="40" height="40" x="-20" y="-20" ')}</g></g>`:`<g id="trav" class="g36-spark"><circle r="9"/><circle r="4" class="g36-sc"/></g>`}</svg>
    <p class="g36-ask" id="g36Ask"></p><div class="na-opts g36-jopts" id="naOpts"></div>`;
  let at=0,busy=false;
  return {svg,wire:root=>{const trav=root.querySelector("#trav"),box=document.getElementById("naOpts"),q=document.getElementById("g36Ask");
      gxStart(root,{kind:"journey",target:s.target,total:n-1,goal:mover?`ودّي ${naQ(s.traveller)} لآخر محطة`:`ودّي الشرارة ✨ لآخر محطة`});
      root.querySelectorAll(".xglow").forEach(g=>{const L=g.getTotalLength();g.style.strokeDasharray=L;g.style.strokeDashoffset=L;});
      const road=i=>root.querySelector(`.xglow[data-i="${i}"]`);
      {const p0=road(0).getPointAtLength(0);trav.setAttribute("transform",`translate(${p0.x} ${p0.y})`);}
      const arrive=i=>{at=i;busy=false;root.querySelector(`.xroad[data-i="${i-1}"]`).classList.add("lit");const hole=root.querySelector(`.g36-hole[data-i="${i}"]`);if(hole)hole.remove();
        const nd=root.querySelector(`.xnode[data-id="${s.route[i]}"]`);nd.classList.remove("sleep","g36-hidden");nd.classList.add("woke");mood(root,s.route[i],"laugh");sfx("pop");gxReact(root,s.route[i],true);
        say(root,s.route[i],mover?"وصلتني! 😄":"صار دوري! 😄");cap("📍 "+s.stops[i].say);
        if(i===n-1){box.innerHTML="";q.textContent="";sfx("tada");sparkles();gxWin(root);setTimeout(()=>{if(root.isConnected)cap("🏁 "+(mover?"«"+exName(s.traveller)+"» وصل لآخر محطة: ":"صارت كل المراحل: ")+s.route.map(exName).join(" ← "));},1600);}
        else setTimeout(()=>{if(root.isConnected)offer();},700);};
      const go=i=>{busy=true;sfx("step");const g=road(i-1),L=g.getTotalLength();const t0=performance.now();
        const step=()=>{if(!g.isConnected)return;const t=Math.min(1,(performance.now()-t0)/850);g.style.strokeDashoffset=String(L*(1-t));
          const pt=g.getPointAtLength(L*t);trav.setAttribute("transform",`translate(${pt.x} ${pt.y})`);
          if(t<1&&!reduce)requestAnimationFrame(step);else{g.style.strokeDashoffset="0";arrive(i);}};step();};
      const wobble=()=>{const p=g4Pos(trav);g4Tween(root,420,t=>trav.setAttribute("transform",`translate(${(p[0]+Math.sin(t*20)*6*(1-t)).toFixed(1)} ${p[1]})`));};
      const offer=()=>{if(at>=n-1)return;const st=s.stops[at+1],wrong=st.wrong||[],here=s.route[at];
        q.innerHTML=t37(VOICE(`👇 لوين بعدين؟ مين ${ARROW_WORD()} ${naQ(here)}؟`));
        const opts=shuffle([{id:s.route[at+1],ok:true}].concat(wrong.map(w=>({id:w.id,ok:false,say:w.say}))),g36Seed(here)+at).map(o=>Object.assign(o,{label:exName(o.id),art:g36Art(o.id)}));
        g36Opts(box,opts,(j,b)=>{if(busy)return;naTake(root);const o=opts[j];
          if(o.ok){box.querySelectorAll(".na-opt").forEach(x=>x.disabled=true);b.classList.add("g36-right");gxGood(root);go(at+1);}
          else{b.disabled=true;b.classList.add("na-wrong");cap(o.say);sfx("nope");gxBad(root);wobble();}});};
      root.querySelectorAll(".xnode").forEach((nd,i)=>nd.addEventListener("click",()=>{if(i===at+1&&!busy)cap(VOICE("👇 اختار من البطاقات: مين المحطة الجاية؟"));}));
      say(root,s.route[0],mover?"وين أروح بعدين؟ اختار 👇":"مين بعدي؟ اختار 👇");
      cap(mover?"«"+exName(s.traveller)+"» رح يمشي من «"+exName(s.route[0])+"». اختار المحطة الجاية كل مرة.":"كل مرحلة بتصحى لما يكون اللي بتحتاجه موجود. اختار مين الجاي.");
      offer();}};}

/* ---------------------------------------------------------------- 🔮 WHAT IF → guess first, then switch it off and check */
function sceneWhatIf(s){const v=V(),all=[s.target].concat(s.affected),n=all.length,calm=s.calm||[];
  const W=v?380:Math.max(640,(n+1)*150),H=v?Math.max(460,n*130+80):330;const pos={};
  all.forEach((x,i)=>pos[x]=v?[i%2?130:250,80+i*((H-200)/Math.max(1,n-1))]:[W-90-i*((W-250)/Math.max(1,n-1)),190]);
  calm.forEach(x=>pos[x]=v?[W/2,H-60]:[70,90]);
  const svg=`<svg class="xstage" id="xs" viewBox="0 0 ${W} ${H}" data-bubble="78" role="img" aria-label="شو بيصير لو">${DEFS}
    ${s.edges.map(([a,b])=>{const [p,q]=edgeEnds(pos[b],pos[a],48);return `<g class="xedge" data-b="${b}">${flow(curve(p,q,v?0:22),"")}</g>`;}).join("")}
    ${all.map((x,i)=>node(x,pos[x][0],pos[x][1],i===0?96:74,"happy",i===0?"star":"g36-guess")).join("")}${calm.map(x=>node(x,pos[x][0],pos[x][1],58,"happy","calm g36-guess")).join("")}
    <g id="g36Marks"></g></svg>
    <div class="xswitch"><button class="switch on" id="sw" role="switch" aria-checked="true"><span class="knob"></span></button><b id="swl"><b class="t37-n">${exName(s.target)}</b> شغّال ✅</b></div>`;
  let on=true,busy=false,judged=false;const guess=new Set();
  return {svg,wire:root=>{const sw=document.getElementById("sw"),cands=s.affected.concat(calm);
      gxStart(root,{kind:"what_if",target:s.target,total:cands.length,goal:`توقّع: مين بيتعب لو اختفى ${naQ(s.target)}؟ وبعدين طفّيه وشوف`});
      const mark=(x,txt,cls)=>{const p=pos[x],g=root.querySelector("#g36Marks");let m=g.querySelector(`[data-id="${x}"]`);if(!m){m=document.createElementNS(svgNS,"g");m.dataset.id=x;g.appendChild(m);}
        m.setAttribute("class","g36-mark "+(cls||""));m.innerHTML=`<circle cx="${p[0]+30}" cy="${p[1]-30}" r="13"/><text x="${p[0]+30}" y="${p[1]-25}" text-anchor="middle">${txt}</text>`;};
      const unmark=x=>{const m=root.querySelector(`#g36Marks [data-id="${x}"]`);if(m)m.remove();};
      root.querySelectorAll(".g36-guess").forEach(nd=>nd.addEventListener("click",()=>{if(judged||!on||busy)return;naTake(root);const x=nd.dataset.id;
        if(guess.has(x)){guess.delete(x);unmark(x);nd.classList.remove("g36-picked");sfx("off",{n:0});}else{guess.add(x);mark(x,"🔮","g36-pmark");nd.classList.add("g36-picked");sfx("pick");}
        cap(guess.size?`🔮 ${VOICE("توقعت")}: ${[...guess].map(naQ).join(" و")}. ${VOICE("هلأ طفّي المفتاح وشوف!")}`:VOICE("🔮 اكبس على اللي بتتوقع إنهم رح يتعبوا."));}));
      const judge=()=>{judged=true;let right=0;cands.forEach(x=>{const hit=s.affected.includes(x),g=guess.has(x);
          if(hit===g){right++;mark(x,"✅","g36-ok");gxGood(root);}else{mark(x,"❌","g36-no");gxBad(root);}});
        const missed=s.affected.filter(x=>!guess.has(x)),wrong=calm.filter(x=>guess.has(x));
        let t=right===cands.length?"🎯 توقعت كله صح! ":`توقعت ${right} من ${cands.length}. `;
        if(missed.length)t+=`${missed.map(naQ).join(" و")} كمان تعب، لأنه بيحتاج اللي قبله. `;
        if(wrong.length)t+=`${wrong.map(naQ).join(" و")} ما بيحتاج ${naQ(s.target)}، فضل مبسوط.`;
        cap(VOICE(t));gxWin(root);};
      sw.addEventListener("click",()=>{if(busy)return;busy=true;naTake(root);on=!on;sw.classList.toggle("on",on);sw.setAttribute("aria-checked",String(on));
        document.getElementById("swl").innerHTML=`<b class="t37-n">${naEsc(exName(s.target))}</b> ${on?"شغّال ✅":"مطفي ⛔"}`;
        root.querySelector(`.xnode[data-id="${s.target}"]`).classList.toggle("gone",!on);sfx(on?"bloom":"whoosh");say(root,null,"");
        s.affected.forEach((x,i)=>setTimeout(()=>{if(!root.isConnected)return;root.querySelector(`.xnode[data-id="${x}"]`).classList.toggle("tired",!on);mood(root,x,on?"laugh":"sad");
            const e=root.querySelector(`.xedge[data-b="${x}"]`);if(e)e.classList.toggle("dim",!on);say(root,x,on?"رجعت! 😄":(i===0?"وين راح؟ 😢":"وأنا كمان! 😢"));sfx(on?"pop":"bad");
            if(i===s.affected.length-1){busy=false;
              if(!on&&!judged&&guess.size){setTimeout(()=>{if(root.isConnected)judge();},500);return;}
              cap(on?"رجع «"+exName(s.target)+"»، فرجعوا كلهم مبسوطين 😄":"شايف؟ كل واحد بيحتاج اللي قبله، فتعبوا ورا بعض."+(calm.length?" بس «"+exName(calm[0])+"» ما بيحتاجه، فضل مبسوط 😎":"")+(judged?"":" "+VOICE("(المرة الجاية: توقّع أول 🔮)")));}},500+i*700));});
      cap(VOICE("🔮 قبل ما تطفي: اكبس على اللي بتتوقع إنهم رح يتعبوا، وبعدين طفّي المفتاح."));}};}

SCENES.recipe=sceneRecipe;SCENES.compare=sceneCompare;SCENES.teach=sceneTeach;SCENES.ladder=sceneLadder;SCENES.journey=sceneJourney;SCENES.what_if=sceneWhatIf;
SNAME.recipe="🍽️ أطعم / الشروط";
