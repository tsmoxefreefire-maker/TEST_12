/* ======================= THE NARRATOR + VIDEO MODE =======================
   · one place for words: a SHORT line that changes with the picture (types in once, then stays still);
   · names in the line are tappable: the same character lights up in the picture; a tooltip says what it is;
   · (batch 26: the «read aloud» button was removed — with no Arabic voice on the device it only said the numbers: «six, seven…»);
   · «📖 ليش؟» — the longer, simple «why» — opens by itself when the scene ends (and any time on tap);
   · 🎬 video mode: the scene plays by itself — everything dims, a spotlight and the camera move to what we talk about;
     at the end: «🖐️ جرّب بنفسك» and the scene becomes a playground;
   · hovering a character: each age reacts its own way (kids giggle in their own voice … seniors just show the name and meaning). */
let VIDEO=false,vTimer=0;
const byName=()=>{const m={};Object.entries(graph().names).forEach(([id,n])=>m[n]=id);return m;};
const meaningOf=id=>{const l=lesson();for(const c of l.concepts){const m=c.scenes[0];if(c.concept_id===id&&m&&m.paragraph)return m.paragraph.replace(/^«[^»]+»:\s*/,"").split(".")[0];}return "";};
/* 🆕 batch 37 (Hareth: «العنوان فيه لخبطات… العلامات اليمين والشمال»): a name is shown CLEAN — a chip or bold — without the «» marks; the words stay the same */
const t37=s=>String(s==null?"":s).replace(/«([^»]+)»/g,'<b class="t37-n">$1</b>').replace(/[«»]/g,"");
const t37svg=s=>String(s==null?"":s).replace(/«([^»]+)»/g,'<tspan class="t37-b">$1</tspan>').replace(/[«»]/g,"");   /* the same inside an SVG text (bubbles) */
function richText(t){const map=byName();return String(VOICE(t)||"").split(/(«[^»]+»)/).map(part=>{const m=part.match(/^«([^»]+)»$/);
    if(m&&map[m[1]]){const tip=meaningOf(map[m[1]]);return `<button class="kw" data-id="${map[m[1]]}" title="${tip.replace(/"/g,"")}">${m[1]}</button>`;}
    if(m)return `<span class="w t37-n">${m[1]}</span>`;                       /* a quoted word that is not a concept (a lesson title, a button's name): bold, no marks */
    return part.split(/(\s+)/).map(w=>w.trim()?`<span class="w">${w}</span>`:w).join("");}).join("")
    .replace(/(<button class="kw"[^>]*>[^<]*<\/button>)(<span class="w">[.،,:!؟؛)]+<\/span>)/g,'<span class="nwr">$1$2</span>')   /* «الساق». : the dot never jumps alone to the next line */
    .replace(/(<span class="w">[وفبلك]{1,2}ـ?<\/span>)(<span class="nwr">.*?<\/span><\/span>|<button class="kw"[^>]*>[^<]*<\/button>)/g,'<span class="nwr">$1$2</span>');}   /* و«الحروف» · فـ«الجذر» · لـ«الورقة»: the little prefix stays glued to its word */
function cap(t){const c=document.getElementById("cap");if(!c)return;c.innerHTML=richText(t);
  const words=[...c.querySelectorAll(".w,.kw")];
  if(!reduce){words.forEach((w,i)=>{w.classList.add("hid");setTimeout(()=>w.classList.remove("hid"),40+i*55);});}     /* types in once, then stays still */
  c.querySelectorAll(".kw").forEach(k=>{k.classList.add("pulse");k.addEventListener("click",ev=>{ev.stopPropagation();const root=document.getElementById("xs");if(!root)return;
      const nd=root.querySelector(`.xnode[data-id="${k.dataset.id}"]`);if(nd){focus(root,[k.dataset.id]);mood(root,k.dataset.id,"joy");say(root,k.dataset.id,"أنا هون! 👋");setTimeout(()=>mood(root,k.dataset.id,"happy"),1200);}
      showTip(k);sfx("pop");});});}
function showTip(k){document.querySelectorAll(".tip").forEach(x=>x.remove());const tip=k.getAttribute("title");if(!tip)return;
  const d=document.createElement("span");d.className="tip";d.textContent=tip;k.appendChild(d);setTimeout(()=>d.remove(),3500);}

/* ---- what to look at in each step (the spotlight and the camera follow it) ---- */
function stepTargets(s,k){const N=id=>`.xnode[data-id="${id}"]`;const t=(s.steps[k]||"");
  switch(s.kind){
    case "overview":return k===0?[]:s.concepts.slice(0,3).map(N);
    case "tour":return k===0?[]:[N(s.order[k-1])].concat(((s.stops||[])[k-1]||{under:[]}).under.slice(0,2).map(N));   /* 🆕 batch 42: the camera visits one part per step */
    case "meet":{const f=(s.focus||[])[k]||"target";if(f==="ins")return [N(s.target)].concat(s.ins.slice(0,2).map(N));
      if(f.startsWith("out:"))return [N(s.target),N(f.slice(4))];return [N(s.target)];}
    case "world":return t.includes("🚿")?["#can","#roots","#stem"]:t.includes("☀️")?["#sun","#leaves"]:t.includes("💨")?["#win","#leaves"]:["#plant"];}
  return [];}
function svgBoxes(root,sels){const R=root.getBoundingClientRect(),vb=root.viewBox.baseVal;const sx=vb.width/R.width,sy=vb.height/R.height;
  return sels.map(q=>root.querySelector(q)).filter(Boolean).map(el=>{const r=el.getBoundingClientRect();return {x:vb.x+(r.left-R.left)*sx,y:vb.y+(r.top-R.top)*sy,w:r.width*sx,h:r.height*sy};});}
let FULL=null;
function camera(root,boxes){if(!FULL)return;let x0=FULL[0],y0=FULL[1],w=FULL[2],h=FULL[3];
  if(boxes&&boxes.length){const a=Math.min(...boxes.map(b=>b.x)),b2=Math.min(...boxes.map(b=>b.y)),c=Math.max(...boxes.map(b=>b.x+b.w)),d=Math.max(...boxes.map(b=>b.y+b.h));
    const pad=70,ratio=FULL[2]/FULL[3];w=Math.max(c-a+pad*2,FULL[2]*0.62);h=w/ratio;if(d-b2+pad*2>h){h=d-b2+pad*2;w=h*ratio;}   /* zoom in at most ×1.6: the place stays clear */
    w=Math.min(w,FULL[2]);h=Math.min(h,FULL[3]);
    /* centre on the thing; near an edge the frame may look only a LITTLE past the picture (15%) — the dark layer covers it, so no white strips */
    const mx=FULL[2]*0.15,my=FULL[3]*0.15;
    x0=Math.max(FULL[0]-mx,Math.min(FULL[0]+FULL[2]+mx-w,(a+c)/2-w/2));y0=Math.max(FULL[1]-my,Math.min(FULL[1]+FULL[3]+my-h,(b2+d)/2-h/2));}
  const vb=root.viewBox.baseVal,from=[vb.x,vb.y,vb.width,vb.height],to=[x0,y0,w,h];let t=0;cancelAnimationFrame(root.__cam||0);const t0=performance.now();
  const go=()=>{if(!root.isConnected)return;t=reduce?1:Math.min(1,(performance.now()-t0)/650);   /* by the clock (not by frames): same speed on a slow phone */const e=t<.5?2*t*t:1-Math.pow(-2*t+2,2)/2;
    root.setAttribute("viewBox",from.map((v,i)=>(v+(to[i]-v)*e).toFixed(1)).join(" "));placeBubble(root);   /* the bubble glides with the camera: same size, inside the frame */
    if(t<1)root.__cam=requestAnimationFrame(go);};go();}
/* 🔦 the spotlight: a SOFT light (feathered edges, not a hard white hole); the dark layer goes UNDER the speech bubble */
function spotlight(root,boxes){let g=root.querySelector("#spot");if(!boxes){if(g){g.classList.add("off");setTimeout(()=>{if(g.classList.contains("off"))g.remove();},380);}return;}
  if(!g){g=document.createElementNS(svgNS,"g");g.id="spot";g.setAttribute("pointer-events","none");}
  g.classList.remove("off");const lay=root.querySelector(":scope > #saylayer");if(lay)root.insertBefore(g,lay);else root.appendChild(g);
  const F=FULL,big=Math.max(F[2],F[3]);
  g.innerHTML=`<defs><filter id="spf" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="${(big/(document.body.dataset.q==="lo"?140:45)).toFixed(1)}"/></filter>
      <mask id="spm" maskUnits="userSpaceOnUse" x="${F[0]-big}" y="${F[1]-big}" width="${F[2]+2*big}" height="${F[3]+2*big}"><rect x="${F[0]-big}" y="${F[1]-big}" width="${F[2]+2*big}" height="${F[3]+2*big}" fill="white"/>
      <g filter="url(#spf)">${boxes.map(b=>`<ellipse cx="${b.x+b.w/2}" cy="${b.y+b.h/2}" rx="${b.w/2+34}" ry="${b.h/2+30}" fill="black"/>`).join("")}</g></mask></defs>
    <rect class="spotdim" x="${F[0]-big}" y="${F[1]-big}" width="${F[2]+2*big}" height="${F[3]+2*big}" mask="url(#spm)"/>`;}
/* the camera goes to the NEW thing of this step (not to the middle between two characters) */
function cameraTargets(s,k){const N=id=>`.xnode[data-id="${id}"]`;const f=(s.focus||[])[k]||"";
  if(s.kind==="meet"){if(f==="ins")return s.ins.slice(0,2).map(N);if(f.startsWith("out:"))return [N(f.slice(4))];return [N(s.target)];}
  if(s.kind==="tour")return k===0?[]:[N(s.order[k-1])];   /* 🆕 batch 42: the camera goes close to THIS part */
  return stepTargets(s,k);}
function videoStep(root,s,k){if(!VIDEO)return;if(HANDS[s.kind]){spotlight(root,null);camera(root,null);return;}   /* 🆕 batch 41: an activity is the student's: no light on the answer */
  const sel=stepTargets(s,k);if((s.kind==="overview"||s.kind==="tour")&&k===0){spotlight(root,null);camera(root,null);return;}
  let camSel=cameraTargets(s,k);const vb=root.viewBox.baseVal;
  const spk=root.__lastSay&&`.xnode[data-id="${root.__lastSay[0]}"]`;if(camSel&&camSel.length&&spk&&!camSel.includes(spk)&&root.querySelector(spk))camSel=camSel.concat([spk]);   /* who is talking stays in the picture with its bubble */const keep=[vb.x,vb.y,vb.width,vb.height];
  root.setAttribute("viewBox",FULL.join(" "));                              /* measure in the full picture… */
  const boxes=svgBoxes(root,sel),camBoxes=camSel?svgBoxes(root,camSel):null;
  root.setAttribute("viewBox",keep.join(" "));                              /* …then glide from where we are */
  spotlight(root,boxes.length?boxes:null);camera(root,camBoxes&&camBoxes.length?camBoxes:null);}
function stopVideo(root,keepWhy){VIDEO=false;clearTimeout(vTimer);ttsStop();const pb=document.getElementById("play");if(pb){pb.textContent="▶️ شغّل";pb.setAttribute("aria-pressed","false");}
  if(root){spotlight(root,null);camera(root,null);}}
function endOfScene(root,auto){stopVideo(root);if(actOpen()){yourTurn(root);return;}   /* 🆕 batch 41: an activity is not over until HE played it */
  const why=document.getElementById("why");if(why){why.hidden=false;why.classList.add("pop2");}
  const tr=document.getElementById("tryit");if(tr)tr.hidden=false;
  if(auto&&!reduce)autoNext(root);}                 /* 🆕 batch 31: the VIDEO reached the end by itself → it goes on by itself */
/* ---- 🆕 batch 31 (Hareth): the video goes on BY ITSELF, scene after scene, with no «skip» from the student ----
   · the end of a scene: a short countdown «المشهد الجاي بعد ٥…» (time to read «ليش؟», longer for the little ones), then the next scene plays;
   · 🆕 batch 41 (Hareth: «الفعاليات… الطالب هو اللي بيلعب فيها مو أوتوماتيك»): an ACTIVITY (a game, the puzzle, the sliders…) never plays
     by itself and the video never skips it: it says the mission, then «🖐️ دورك!» and WAITS (no countdown). When he wins (gxWin) or says
     «✓ خلصت», «ليش؟» opens and the video goes on. (It used to solve it for him as an «example», or move on after 12 seconds.);
   · the last scene of the lesson: a summary card (what he met) — it never jumps into the next lesson by itself;
   · ⏸ always there: «وقّف» in the countdown, and any touch on the scene stops it (the old rule). */
const AUTO_SPEED={kids:1.7,junior:1.4,teen:1.2,senior:1.05};   /* reading time by age (اجتهاد): the little ones read slower · 🆕 batch 44 (Hareth: «الكلام اللي تحت كثير سريع… الطالب ما بيلحق يقرا»): ~+20–30%, the story's moments with it */
const HANDS={assemble:1,recipe:1,connect:1,compare:1,teach:1,slider:1,lens:1,flip:1,ladder:1,throw:1,tower:1,magnet:1,machine:1,power:1,journey:1,what_if:1,before_after:1,build_up:1,missing:1,who_am_i:1,sentence:1};   /* the ACTIVITIES: + the 5 games (batch 34) · batch 36: the journey and «what if» are choices · batch 41: «before / after» (he drags it) · 🆕 batch 42: 🌱 build it up, ❓ what's missing */
let goT=0,ACT_DONE=false;                                   /* 🆕 batch 41: ACT_DONE = the student finished THIS scene's activity */
const actOpen=()=>{const p=pathOf(),h=p&&p[POS];return !!(h&&HANDS[h.s.kind])&&!ACT_DONE;};
/* «🖐️ دورك!» — under the picture, it stays until he finishes (never a countdown): the mission is his */
function yourTurn(root){if(!actOpen()||!root||!root.isConnected)return;const narr=document.querySelector("#q .narr");if(!narr||document.getElementById("turn"))return;
  const d=document.createElement("div");d.id="turn";d.className="yourturn";d.setAttribute("role","status");
  const st=pathOf()[POS].s.steps||[],how=st.length>=3?t37(VOICE(st[1])):VOICE("العب إنت، والفيديو بيستناك");   /* step 2 of an activity = how to play */
  d.innerHTML=`<span class="yt-t">🖐️ <b>${VOICE("دورك!")}</b> ${how}</span><button type="button" class="chipbtn" id="turnDone">✓ ${VOICE("خلصت")}</button>`;
  narr.after(d);d.querySelector("#turnDone").addEventListener("click",()=>{sfx("pop");actWon(root);});}
/* he finished (he won the game, or he says so): «ليش؟» opens and the video goes on (a countdown he can stop) */
function actWon(root){const cur=document.getElementById("xs");if(ACT_DONE||!root||root!==cur||!root.isConnected)return;ACT_DONE=true;
  const t=document.getElementById("turn");if(t)t.remove();
  setTimeout(()=>{if(root.isConnected&&document.getElementById("xs")===root)endOfScene(root,true);},GX.won?1300:150);}   /* the stars and the party first */
const speedNow=()=>AUTO_SPEED[stageNow()]||1;
function stopGo(){clearInterval(goT);goT=0;const g=document.getElementById("goNext");if(g)g.remove();}
function countdown(sec,msg,go){stopGo();const narr=document.querySelector("#q .narr");if(!narr)return;
  const d=document.createElement("div");d.id="goNext";d.className="gonext";d.setAttribute("role","status");
  d.innerHTML=`<span class="gn-t">${msg} <b id="gnSec">${sec}</b></span><button type="button" class="chipbtn" id="gnStop">⏸ وقّف</button><button type="button" class="chipbtn gn-go" id="gnGo">▶ هلأ</button><i class="gn-bar"><i style="animation-duration:${sec}s"></i></i>`;
  narr.after(d);let left=sec;
  d.querySelector("#gnStop").addEventListener("click",()=>{stopGo();sfx("pop");});
  d.querySelector("#gnGo").addEventListener("click",()=>{stopGo();go();});
  goT=setInterval(()=>{left--;const e=document.getElementById("gnSec");if(e)e.textContent=Math.max(0,left);if(left<=0){stopGo();go();}},1000);}
function autoNext(root){const p=pathOf(),s=p[POS].s,last=POS>=p.length-1,k=speedNow();
  const words=String(s.paragraph||"").split(/\s+/).filter(Boolean).length;
  const read=Math.round(Math.min(14,Math.max(5,words*.32*k)));
  const next=()=>{if(last){lessonEnd();return;}POS++;STEP=0;renderAll2();};
  if(!root.isConnected)return;
  if(actOpen()){yourTurn(root);return;}                     /* 🆕 batch 41: never past an activity he has not played */
  if(last)countdown(read,"🎉 ملخّص الدرس بعد",next);
  else countdown(read,"المشهد الجاي بعد",next);}
function lessonEnd(){stopGo();const l=lesson(),g=graph();const q=document.getElementById("q");if(!q)return;
  const old=document.getElementById("lsum");if(old)old.remove();
  const nextL=EL+1<(DATA.graphs[EG].lessons||[]).length;
  const d=document.createElement("div");d.id="lsum";d.className="lsum";d.setAttribute("role","region");d.setAttribute("aria-label","ملخّص الدرس");
  d.innerHTML=`<b class="ls-h">🎉 خلصت درس <span class="t37-name">${l.lesson_title}</span></b><p class="ls-p">${VOICE("تعرّفت على")}:</p>
    <div class="ls-c">${l.concepts.map(c=>`<span class="ls-chip">${c.title}</span>`).join("")}</div>
    <div class="ls-b"><button type="button" class="btn ghost" id="lsAgain">↺ من الأول</button>${nextL?`<button type="button" class="btn" id="lsNext">الدرس الجاي ←</button>`:""}</div>`;
  const narr=q.querySelector(".narr");(narr||q.firstChild).after(d);d.scrollIntoView({block:"nearest",behavior:reduce?"auto":"smooth"});
  sfx("tada");if(!grown())sparkles();cap("🎉 "+VOICE("برافو!")+" خلصت «"+l.lesson_title+"».");
  d.querySelector("#lsAgain").addEventListener("click",()=>{POS=0;STEP=0;renderAll2();});
  const nb=d.querySelector("#lsNext");if(nb)nb.addEventListener("click",()=>{EL++;POS=0;STEP=0;renderAll2();window.scrollTo({top:0});});}
/* ---- 👆 hovering a character, by age (batch 26):
   kids: the eyes go ^ ^, it hops and giggles in its OWN voice · junior: it leans, curious, a soft «همم؟» ·
   teen: it glows + one light tick + its name and meaning · senior: no sound, only its name and meaning (a small label). ---- */
let lastHover=0;
function hoverTip(root,n){let L=root.querySelector(":scope > #hvlayer");if(!n){if(L)L.innerHTML="";return;}
  const id=n.dataset.id,txt=meaningOf(id);if(!txt||!graph().names[id])return;
  if(!L){L=document.createElementNS(svgNS,"g");L.id="hvlayer";L.setAttribute("pointer-events","none");}
  const lay=root.querySelector(":scope > #saylayer");if(lay)root.insertBefore(L,lay);else root.appendChild(L);   /* under the speech bubble, above everything else */
  const ls=[exName(id)].concat(lines(VOICE(txt),30,2)),LH=17,h=12+ls.length*LH;
  L.innerHTML=`<g class="hvtip">${'<rect rx="9" height="'+h+'"/>'}${ls.map((l,i)=>`<text class="${i?"":"hvn"}" y="${18+i*LH}" text-anchor="middle">${l}</text>`).join("")}</g>`;
  const g=L.firstChild;let w=0;g.querySelectorAll("text").forEach(t=>{try{w=Math.max(w,t.getComputedTextLength());}catch(e){}});w=Math.max(90,Math.ceil(w||ls.join("").length*7)+24);
  g.querySelector("rect").setAttribute("width",w);g.querySelectorAll("text").forEach(t=>t.setAttribute("x",w/2));
  const vb=root.viewBox.baseVal,sp=nodeSpot(root,n);let top=sp.y-sp.r-h-8;if(top<vb.y+4)top=Math.min(vb.y+vb.height-h-4,sp.y+sp.r+26);
  const left=Math.max(vb.x+4,Math.min(vb.x+vb.width-4-w,sp.x-w/2));g.setAttribute("transform",`translate(${left.toFixed(1)} ${top.toFixed(1)})`);}
function giggles(root){const st=stageNow();
  root.querySelectorAll(".xnode").forEach(n=>{let before=null;
    const on=()=>{const b=n.querySelector(".xbody");if(!b)return;
      if(st==="kids"){if(b.dataset.mood==="joy")return;before=b.dataset.mood;b.dataset.mood="joy";n.classList.add("hop");}
      else n.classList.add("hv-"+st);
      if(st==="teen"||st==="senior")hoverTip(root,n);
      const now=Date.now();if(now-lastHover>(st==="kids"?900:450)){lastHover=now;if(soundOn)try{SOUND.hover(n.dataset.id);}catch(e){}}};
    const off=()=>{const b=n.querySelector(".xbody");if(st==="kids"){if(b&&b.dataset.mood==="joy")b.dataset.mood=before||"happy";n.classList.remove("hop");}else n.classList.remove("hv-"+st);hoverTip(root,null);};
    n.addEventListener("pointerenter",e=>{if(e.pointerType==="mouse")on();});n.addEventListener("pointerleave",e=>{if(e.pointerType==="mouse")off();});
    if(st==="kids")n.addEventListener("pointerdown",e=>{if(e.pointerType!=="mouse"){on();setTimeout(off,900);}});});}
