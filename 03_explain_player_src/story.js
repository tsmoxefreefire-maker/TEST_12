/* ======================= 🎬 THE LESSON'S STORY — a real SVG cartoon (batch 32, Hareth: «المشهد كأنه فيديو: الشخصيات بتتحرك وبتتفاعل مع بعض والطالب بيتفرّج») =======================
   Made from the lesson's graph ONLY (the overview's arrows + the «meet» scenes' prerequisites and reasons, all checked by the factory):
   · the characters WALK in (they hop, squash & stretch, look where they go) and say who they are;
   · «B needs A»: A walks over to B and GIVES it a glowing ball → B lights up, says thanks, and the arrow B → A is drawn;
     a prerequisite from outside the lesson (water, soil, sun…) comes in as a guest and gives too;
   · the longest chain: one ball travels along it and every character lights up in turn;
   · «what if A disappears?»: A walks out, the ones who need it get sad and grey; A comes back and everything works again;
   · the end: everyone jumps.
   It plays like a VIDEO: ▶/⏸, a timeline you can drag (chapters marked), the time, subtitles inside the picture, a backdrop for every subject.
   Every frame is computed for a time t (frame(t)), so jumping anywhere on the timeline always shows the right picture.
   🆕 batch 38: HOW the lesson's story is told moved to story38.js (the characters now come ONE BY ONE, each called by the one that needs it,
   and every age has its own picture: a tale · an adventure · an investigation board · a documentary diagram). This file keeps the shared
   parts: the facts of the story (storyOf), the cartoon kit (stKit), the video player (stShell + stPlay), the characters' cartoon (stMake)
   and every concept's cartoon «تعرّف عليّ» (sceneCStory). */
const ST_THEME={science:"field",math:"board",physics:"space",chemistry:"lab",geography:"map",history:"desert",language:"paper",general:"room"};
const storyCache={};
/* «she» or «he» for the words (🆕 batch 40: + the feminine words without «ة» — الأرض، الشمس، الرياح… — and the plurals of things,
   which Arabic treats as «she»: «الحروف رجعت», «الأعداد رجعت»; the pattern «أفعال» = a plural: الأنهار، الأشجار، الأجزاء) */
const ST_FEM_W=new Set(["أرض","شمس","نار","ريح","رياح","سماء","حرب","يد","عين","أذن","دار","نفس","روح","بئر","حروف","جذور","بذور","كسور","فصول","عصور","طيور","شعوب","دروس","نجوم","غيوم","صخور","ثمار","زهور","خلايا","قوى"]);
const stFem=n=>{const w=String(n||"").trim().split(/\s+/)[0]||"",b=w.replace(/^(وال|بال|ال)/,"");return /(ة|ات)$/.test(w)||ST_FEM_W.has(b)||/^أ..ا.$/.test(b);};
/* 🆕 batch 33: the words of «needs» follow the subject (like the arrows, batch 28): maths «مبني على», history «بسبب» */
const stW=()=>{const k=(graph()||{}).subject;   /* f = the name is feminine (stFem) → the words agree («مبنية»، «صارت») */
  if(k==="math")return {one:f=>f?"مبنية على":"مبني على",many:"مبنيين على",askIn:(x,f)=>`${x} ${f?"مبنية":"مبني"} على شو؟`,askOut:f=>`شو مبني ${f?"عليها":"عليه"}؟`,chain:"شو مبني على شو",
    lost:(f,many)=>many?"ما بيزبطوا":f?"ما بتزبط":"ما بيزبط",wif:x=>`شو بيصير لو ما في ${x}؟`,back:"وكل إشي رجع يزبط",end:"كل إشي مبني على اللي قبله",intro:"على شو مبني، وشو مبني عليه"};
  if(k==="history")return {one:()=>"بسبب",many:"بسبب",askIn:(x,f)=>`ليش ${f?"صارت":"صار"} ${x}؟`,askOut:f=>`شو صار ${f?"بسببها":"بسببه"}؟`,chain:"شو صار بسبب شو",
    lost:(f,many)=>many?"ما كانوا صاروا":f?"ما كانت صارت":"ما كان صار",wif:(x,f)=>`شو لو ما ${f?"صارت":"صار"} ${x}؟`,back:"والأحداث رجعت تصير",end:"كل حدث صار بسبب اللي قبله",intro:"ليش صار، وشو صار بسببه"};
  return null;};
const stNeeds=id=>{const w=stW();return w?w.one(stFem(exName(id))):(stFem(exName(id))?"بتحتاج":"بيحتاج");};
const stNeedsMany=()=>{const w=stW();return w?w.many:"بيحتاجوا";};
const stShort=t=>{t=String(t||"").replace(/^«[^»]+»:\s*/,"").replace(/^📌\s*/,"").trim();const c=t.split(/[.،؛]/)[0];return c.length>70?c.slice(0,68).replace(/\s+\S*$/,"")+"…":c;};
/* the story's facts: who is in it, who needs whom (and why) — only what the graph says */
function storyOf(l){if(storyCache[l.lesson_id])return storyCache[l.lesson_id];
  const ov=l.overview||{concepts:l.concepts.map(c=>c.concept_id),edges:[],levels:{}};
  const inLesson=new Set(ov.concepts),edges=[],why={},meaning={};
  (ov.edges||[]).forEach(([a,b])=>edges.push([a,b]));                                   /* [a,b]: b needs a */
  const guestsUse={};
  l.concepts.forEach(c=>{const m=c.scenes.find(x=>x.kind==="meet");const b=c.concept_id;
    meaning[b]=stShort(m&&m.steps&&m.steps[1]||(l.assemble&&l.assemble.says||{})[b]||"");
    if(!m)return;Object.entries(m.roles||{}).forEach(([a,r])=>{if((m.ins||[]).includes(a))why[a+">"+b]=stShort(r);});
    (m.ins||[]).forEach(a=>{if(!inLesson.has(a)){guestsUse[a]=(guestsUse[a]||0)+1;}});});
  const room=Math.max(0,9-ov.concepts.length);
  const guests=Object.keys(guestsUse).sort((x,y)=>guestsUse[y]-guestsUse[x]).slice(0,Math.min(3,room));
  l.concepts.forEach(c=>{const m=c.scenes.find(x=>x.kind==="meet");if(!m)return;(m.ins||[]).forEach(a=>{if(guests.includes(a)&&!edges.some(e=>e[0]===a&&e[1]===c.concept_id))edges.push([a,c.concept_id]);});});
  const lv={};ov.concepts.forEach(c=>lv[c]=(ov.levels||{})[c]||0);guests.forEach(g=>lv[g]=-1);
  const s={kind:"story",ids:ov.concepts.slice(),guests,edges,levels:lv,why,meaning,title:l.lesson_title,
    steps:[`🎬 ${VOICE("حكاية")} «${l.lesson_title}»: ${VOICE("تفرّج كيف المفاهيم بتساعد بعض")}.`],paragraph:ov.paragraph||""};
  storyCache[l.lesson_id]=s;return s;}

/* ---------- the backdrop: since batch 35 it is the lesson's PLACE (placeSVG in places.js: a garden, a lab, space…); ST_THEME stays as the subject's tag ---------- */

/* ---------- the cartoon kit: the script's words (who walks where, who says what, when) — shared by every cartoon ---------- */
function stKit(ids,pos,W,Z,k){const ev={mv:{},mood:{},talk:{},bub:[],glow:{},gray:{},out:{},orb:[],link:[],sub:[],chap:[],spark:[],cue:[],pulse:{}};
  ids.forEach(i=>{ev.mv[i]=[];ev.mood[i]=[[0,"happy"]];ev.talk[i]=[];ev.glow[i]=[];ev.gray[i]=[];ev.out[i]=[];ev.pulse[i]=[];});
  const d=x=>x*k,off=id=>[pos[id][0]<W/2?-70:W+70,pos[id][1]];   /* they walk in from the nearest side (nobody walks through the others) */
  const mv=(id,t0,t1,a,b)=>ev.mv[id].push([t0,t1,a,b]),mood=(id,t,m)=>ev.mood[id].push([t,m]);
  const sub=(t0,t1,txt)=>ev.sub.push([t0,t1,VOICE(txt)]),bub=(id,t0,t1,txt)=>ev.bub.push([t0,t1,id,VOICE(txt)]);
  const chap=(t,txt)=>ev.chap.push([t,txt]),cue=(t,n)=>ev.cue.push([t,n]);
  const near=(a,b)=>{const p=pos[a],q=pos[b],dx=p[0]-q[0],dy=p[1]-q[1],L=Math.hypot(dx,dy)||1,r=Z*1.05;return [q[0]+dx/L*r,q[1]+dy/L*r];};
  const N=id=>`«${exName(id)}»`,big=!grown();
  /* «b needs a»: a walks over to b and GIVES it a glowing ball → b lights up, says thanks, the arrow b → a is drawn, a walks back */
  const give=(a,b,T,line)=>{sub(T,T+d(4.3),line);mood(b,T,"o");bub(b,T+d(0.1),T+d(1.4),big?`${VOICE("بحتاجك")} يا ${N(a)}!`:`${N(a)}؟`);ev.talk[b].push([T+d(0.1),T+d(1.1)]);
    const np=near(a,b);mv(a,T+d(0.5),T+d(1.5),pos[a],np);cue(T+d(1.4),"step");
    ev.orb.push([T+d(1.6),T+d(2.5),a,b]);cue(T+d(1.6),"pick");cue(T+d(2.5),"good");
    ev.pulse[b].push(T+d(2.5));mood(b,T+d(2.5),"joy");ev.glow[b].push([T+d(2.5),T+d(3.5)]);bub(b,T+d(2.6),T+d(3.8),big?"شكراً! ✨":"✓");
    ev.link.push([T+d(2.7),a,b]);mv(a,T+d(2.9),T+d(3.8),np,pos[a]);mood(b,T+d(3.9),"happy");ev.spark.push([T+d(2.5),b]);return T+d(4.4);};
  /* walk in from outside (and stay outside until then) */
  const enter=(id,T,dur)=>{mv(id,-1,T,off(id),off(id));mv(id,T,T+d(dur||1.5),off(id),pos[id]);cue(T+d((dur||1.5)-0.1),"step");return T+d(dur||1.5);};
  return {ev,d,off,mv,mood,sub,bub,chap,cue,near,N,give,enter,big};}

/* ---------- the engine: from the script to a playing cartoon (the picture, the player, frame(t)) ----------
   🆕 batch 38: split in three, so every age's story (the characters in the place · the investigation board · the documentary diagram, story38.js)
   shares ONE video player: stShell (the frame: the picture + the title card + the subtitles + the controls) · stPlay (▶/⏸, the timeline,
   the subtitles, the chapters, the sounds, window.stCtl) · stMake (the characters: walk, hop, give the ball, talk). */
/* the bubble / the subtitles: the name in bold, never «» (batch 37) — also when a long name is cut over two lines */
const stBold=x=>String(x).replace(/«([^»]+)»/g,'<tspan class="t37-b">$1</tspan>').replace(/«([^»]*)$/,'<tspan class="t37-b">$1</tspan>').replace(/^([^«]*)»/,'<tspan class="t37-b">$1</tspan>').replace(/[«»]/g,"");
function stShell(o){const {W,H,DUR,ev}=o;const byT=(a,b)=>a[0]-b[0];ev.chap.sort(byT);ev.sub.sort(byT);   /* the script may be written in any order */
  ev.sub.forEach((x,i)=>{const n=ev.sub[i+1];if(n&&x[1]>n[0])x[1]=Math.max(x[0]+0.2,n[0]);});   /* 🆕 batch 45: a line ends when the next one starts (the voice reads them one by one, never cut) */
  return `<div class="st-screen" data-kind="${o.kind||"story"}" data-look="${o.look||"cast"}" data-tale="${o.tale||""}" data-theme="${o.theme}" data-place="${o.place||placeNow()}" data-dur="${DUR.toFixed(1)}" data-chap='${JSON.stringify(ev.chap.map(c=>[+c[0].toFixed(2),c[1]])).replace(/'/g,"&#39;")}'><svg class="xstage st-svg" id="xs" viewBox="0 0 ${W} ${H}" role="img" aria-label="${o.label||VOICE("حكاية الدرس")}">${DEFS}${o.body}
      <g class="st-title" opacity="1"><rect width="${W}" height="${H}" fill="#0E1A20" opacity=".55"/><text x="${W/2}" y="${H/2-14}" text-anchor="middle" class="st-tt1">${o.tt1||`🎬 ${VOICE("حكاية")}`}</text><text x="${W/2}" y="${H/2+26}" text-anchor="middle" class="st-tt2">${o.title}</text></g></svg>
    <div class="st-sub" id="stSub" aria-live="polite"></div>
    <button type="button" class="st-big" id="stBig" aria-label="${VOICE("شغّل")}">▶</button></div>
    <div class="st-ctl" role="group" aria-label="${VOICE("التحكم بالفيديو")}"><button type="button" class="st-pp" id="stPP" aria-label="${VOICE("شغّل / وقّف")}">▶</button>
      <div class="st-tl"><input type="range" id="stSeek" min="0" max="${Math.round(DUR*10)}" value="0" step="1" aria-label="${VOICE("مكان الفيديو")}"><div class="st-ticks">${ev.chap.map(([t,txt])=>`<i style="inset-inline-start:${(100*t/DUR).toFixed(2)}%" title="${txt}"></i>`).join("")}</div></div>
      <span class="st-time" id="stTime">0:00 / ${Math.floor(DUR/60)}:${String(Math.round(DUR%60)).padStart(2,"0")}</span><span class="st-chap" id="stChap"></span></div>`;}
/* the player: draw(t) paints the picture; the player paints the rest (title card, subtitles, chapter, time) and runs the clock.
   🆕 batch 39: opt.gate(spec, resume) — «🖐️ دورك»: when the STUDENT plays the story (not the auto video), it stops at ev.gate[i][0] and asks;
   in the auto video it does not stop: the story itself shows the answer (like an example). opt.tap(id) — a tap on a .st-tap (a card, a node). */
function stPlay(root,DUR,ev,k,draw,opt){const d=x=>x*k;opt=opt||{};
  const title=root.querySelector(".st-title"),subEl=document.getElementById("stSub"),pp=document.getElementById("stPP"),bigB=document.getElementById("stBig"),seek=document.getElementById("stSeek"),timeEl=document.getElementById("stTime"),chapEl=document.getElementById("stChap");
  const clamp=(x,a,b)=>Math.max(a,Math.min(b,x)),fmt=t=>`${Math.floor(t/60)}:${String(Math.floor(t%60)).padStart(2,"0")}`;
  const lastOf=(arr,t)=>{let x=null;for(const e of arr){if(e[0]<=t)x=e;else break;}return x;};
  const byT=(a,b)=>a[0]-b[0];ev.sub.sort(byT);ev.chap.sort(byT);
  let t=0,playing=false,last=0,raf=0,seeking=false,ended=false;
  const gates=(ev.gate||[]).slice().sort((a,b)=>a[0]-b[0]),passed=new Set(),video=()=>typeof VIDEO!=="undefined"&&VIDEO;
  /* 🆕 batch 44: the voice reads each subtitle; if it is still speaking when the subtitle should end, the story WAITS for it */
  let voice=null;const sayNow=(text,end)=>{const v={end,done:false};voice=v;ttsSay(text).then(()=>{v.done=true;});};
  function frame(t){
    title.setAttribute("opacity",String(clamp(1-(t-d(1.2))/d(0.8),0,1)));
    draw(t);
    const st=lastOf(ev.sub.map(x=>[x[0],x]),t),sv=st&&t<st[1][1]?st[1][2]:"";if(subEl.dataset.v!==sv){subEl.dataset.v=sv;if(sv&&playing&&ttsOn())sayNow(sv,st[1][1]);subEl.innerHTML=sv.replace(/[&<>]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;"}[c])).replace(/«([^»]+)»/g,"<b>$1</b>").replace(/[«»]/g,"");subEl.classList.toggle("on",!!sv);}
    const ch=lastOf(ev.chap,t);chapEl.textContent=ch?ch[1]:"";
    timeEl.textContent=`${fmt(t)} / ${fmt(DUR)}`;if(!seeking)seek.value=String(Math.round(t*10));}
  const setPlay=on=>{playing=on;pp.textContent=on?"⏸":"▶";pp.setAttribute("aria-pressed",String(on));bigB.hidden=on||t>0&&!ended;root.closest(".st-screen")&&root.closest(".st-screen").classList.toggle("playing",on);};
  const tick=now=>{if(!root.isConnected){cancelAnimationFrame(raf);return;}if(!playing)return;
    if(voice&&!voice.done&&t>=voice.end-0.05){last=now;raf=requestAnimationFrame(tick);return;}   /* hold this moment until the voice finishes */
    const dt=Math.min(0.1,(now-last)/1000);last=now;const t0=t;t=Math.min(DUR,t+dt);
    if(opt.gate&&!video()){const gi=gates.findIndex((g,i)=>!passed.has(i)&&g[0]>t0&&g[0]<=t);   /* the student's turn: stop here and ask */
      if(gi>=0){passed.add(gi);t=gates[gi][0];ev.cue.forEach(([ct,n])=>{if(ct>t0&&ct<=t)sfx(n);});frame(t);pause();opt.gate(gates[gi][1],()=>{if(root.isConnected)play();});return;}}
    ev.cue.forEach(([ct,n])=>{if(ct>t0&&ct<=t)sfx(n);});frame(t);
    if(t>=DUR){ended=true;setPlay(false);bigB.hidden=false;bigB.textContent="↺";if(typeof VIDEO!=="undefined"&&VIDEO)endOfScene(root,true);return;}raf=requestAnimationFrame(tick);};
  const play=()=>{if(ended||t>=DUR){t=0;ended=false;bigB.textContent="▶";}setPlay(true);last=performance.now();cancelAnimationFrame(raf);raf=requestAnimationFrame(tick);};
  const pause=()=>{setPlay(false);cancelAnimationFrame(raf);if(voice){voice=null;ttsStop();}};
  pp.addEventListener("click",()=>{playing?pause():play();});
  bigB.addEventListener("click",()=>{play();});
  seek.addEventListener("input",()=>{seeking=true;if(voice){voice=null;ttsStop();}t=+seek.value/10;ended=false;bigB.textContent="▶";frame(t);});
  seek.addEventListener("change",()=>{seeking=false;});
  root.addEventListener("click",e=>{if(e.target.closest(".xnode"))return;
    const tp=opt.tap&&e.target.closest(".st-tap");if(tp&&+(getComputedStyle(tp).opacity)>0.5){pause();opt.tap(tp.dataset.id);return;}   /* 🆕 batch 39: a card / a node tells about itself */
    playing?pause():play();});   /* tap the picture = play / pause (like a video) */
  const pageBtn=document.getElementById("play");if(pageBtn)pageBtn.addEventListener("click",()=>setTimeout(()=>{if(!root.isConnected)return;(typeof VIDEO!=="undefined"&&VIDEO)?play():pause();},0));   /* the page's «⏸ وقّف / ▶ شغّل» drives the story too: one control, not two */
  frame(0);setPlay(false);
  current.storyCtl=window.stCtl={play,pause,get t(){return t;},DUR,seek:x=>{t=x;frame(t);},subs:ev.sub,chap:ev.chap};   /* for the browser check (window.stCtl) */
  setTimeout(()=>{if(root.isConnected&&typeof VIDEO!=="undefined"&&VIDEO&&!reduce)play();},60);}
/* the characters' cartoon (the little ones' tale, the explorers' adventure, every concept's «تعرّف عليّ») — o.hop: how high they hop (1 = a lot) */
function stMake(o){const {ids,pos,W,H,floor,Z,theme,edges,title,ev,DUR,lo,k}=o;const d=x=>x*k,HOP=o.hop==null?1:o.hop;
  const dep={};ids.forEach(id=>dep[id]=(o.scale&&o.scale[id])||0.92+0.16*((pos[id][1]-floor)/(H-floor)));        /* closer to us (lower) = a little bigger */
  const byT=(a,b)=>a[0]-b[0];ids.forEach(id=>{ev.mood[id].sort(byT);ev.mv[id].sort(byT);});ev.bub.sort(byT);   /* the script may be written in any order */
  const TH=o.thief&&ev.mv.__thief?ev.mv.__thief.sort(byT):null;   /* 🆕 batch 39: the thief of the twist (story38.js) */
  /* 🆕 batch 40: HOW it vanishes fits the thing (Hareth: «الأرنب ما بيقدر يمسك التربة»): an actor can shrink (ev.sz) and fade (ev.fade),
     the agent can swell (ev.thsz) and appear / disappear (ev.thfade) — a sponge soaks the water up, a cloud covers the sun, a mole pulls the soil down… */
  ["sz","fade"].forEach(n=>{ev[n]=ev[n]||{};Object.values(ev[n]).forEach(a=>a.sort(byT));});ev.thsz=(ev.thsz||[]).sort(byT);ev.thfade=(ev.thfade||[]).sort(byT);
  const gid=`stg${Math.random().toString(36).slice(2,7)}`;
  const actorSVG=id=>`<g class="sa" data-id="${id}"><ellipse class="sa-sh" rx="${Z*0.42}" ry="${Z*0.11}" cy="${Z*0.46}"/><g class="sa-glow" opacity="0"><circle r="${Z*0.62}" fill="url(#${gid}g)"/></g><g class="sa-b">${node(id,0,0,Z,"happy","st-node")}</g></g>`;
  const body=`<defs><radialGradient id="${gid}g"><stop offset="0" stop-color="#FFE27A" stop-opacity=".85"/><stop offset="1" stop-color="#FFE27A" stop-opacity="0"/></radialGradient>
        <radialGradient id="${gid}o"><stop offset="0" stop-color="#fff"/><stop offset=".35" stop-color="#FFE27A"/><stop offset="1" stop-color="#FFB020" stop-opacity="0"/></radialGradient></defs>
      <g class="st-bg">${placeSVG(placeNow(),W,H,{floor,lo,full:true})}</g>
      <g class="st-links">${edges.map(([a,b],i)=>{const [p,q]=edgeEnds(pos[b],pos[a],Z*0.56);return `<path class="st-link" data-i="${i}" data-a="${a}" data-b="${b}" d="${curve(p,q,16)}" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1" style="opacity:0"/>`;}).join("")}</g>
      <g class="st-actors">${ids.slice().sort((a,b)=>pos[a][1]-pos[b][1]).map(actorSVG).join("")}</g>
      <g class="st-orbs">${[0,1,2].map(i=>`<g class="st-orb" data-o="${i}" opacity="0"><circle r="16" fill="url(#${gid}o)"/><circle r="6" fill="#fff"/></g>`).join("")}${lo?"":[0,1,2,3,4,5].map(i=>`<circle class="st-trail" data-t="${i}" r="${4-i*0.5}" fill="#FFE27A" opacity="0"/>`).join("")}</g>
      <g class="st-sparks">${Array.from({length:14},(_,i)=>`<path class="st-spark" data-s="${i}" d="M0 -6 L1.6 -1.6 L6 0 L1.6 1.6 L0 6 L-1.6 1.6 L-6 0 L-1.6 -1.6Z" fill="${["#FFD84D","#7BD389","#6CB8FF","#FF8FB1"][i%4]}" opacity="0"/>`).join("")}</g>
      <g class="st-thieves">${TH?`<g class="st-thief" data-k="${o.thief.kind}" data-way="${o.thief.way||"carry"}"><g class="st-thief-b">${o.thief.svg}</g></g>`:""}</g>
      <g class="st-bubs"></g>`;
  const svg=stShell({W,H,DUR,ev,kind:o.kind,look:"cast",tale:o.tale,theme,title,label:o.label,body});
  return {svg,stepMs:1e9,story:{DUR},wire:root=>{
    const A={};root.querySelectorAll(".sa").forEach(g=>{const id=g.dataset.id;A[id]={g,b:g.querySelector(".sa-b"),body:g.querySelector(".xbody"),glow:g.querySelector(".sa-glow"),pup:[...g.querySelectorAll(".spupil")],m:"",gr:false,o:1};});
    const bubL=root.querySelector(".st-bubs"),orbs=[...root.querySelectorAll(".st-orb")],trails=[...root.querySelectorAll(".st-trail")],sparks=[...root.querySelectorAll(".st-spark")],links=[...root.querySelectorAll(".st-link")];
    const ease=u=>u<.5?2*u*u:1-Math.pow(-2*u+2,2)/2,clamp=(x,a,b)=>Math.max(a,Math.min(b,x));
    const where=(id,t)=>{let p=pos[id],hop=0,sq=1,moving=null;for(const [t0,t1,a,b] of ev.mv[id]){if(t<t0)break;if(t>=t1){p=b;continue;}const u=(t-t0)/(t1-t0),e=ease(u);p=[a[0]+(b[0]-a[0])*e,a[1]+(b[1]-a[1])*e];
        const hops=Math.max(1,Math.round(Math.hypot(b[0]-a[0],b[1]-a[1])/70)),ph=(u*hops)%1;hop=Math.sin(Math.PI*ph)*(Z*0.22)*HOP;sq=ph<.12||ph>.88?1-0.1*HOP:1+0.05*HOP;moving=[b[0]-a[0],b[1]-a[1]];break;}return {p,hop,sq,moving};};
    const lastOf=(arr,t)=>{let x=null;for(const e of arr){if(e[0]<=t)x=e;else break;}return x;};
    const inAny=(arr,t)=>arr.some(([a,b])=>t>=a&&t<b);
    const tw=(arr,t)=>{let v=1;if(!arr)return v;for(const [t0,t1,a,b] of arr){if(t<t0)break;if(t>=t1){v=b;continue;}v=a+(b-a)*ease((t-t0)/(t1-t0));break;}return v;};   /* 🆕 batch 40: a value that changes smoothly */
    let bubKey="",thDir=1;const thG=root.querySelector(".st-thief"),thB=root.querySelector(".st-thief-b");
    stPlay(root,DUR,ev,k,t=>{
      if(thG){const w=where("__thief",t);if(w.moving&&Math.abs(w.moving[0])>1)thDir=w.moving[0]<0?-1:1;const s=Z/50*tw(ev.thsz,t),fl=o.thief.way==="carry"||o.thief.way==null;   /* it faces where it runs */
        thG.setAttribute("transform",`translate(${w.p[0].toFixed(1)} ${w.p[1].toFixed(1)})`);thB.setAttribute("transform",`translate(0 ${(fl?-w.hop:0).toFixed(1)}) scale(${((fl?thDir:1)*s).toFixed(3)} ${s.toFixed(3)})`);
        const tf=tw(ev.thfade,t).toFixed(2);if(thG.__o!==tf){thG.__o=tf;thG.style.opacity=tf;}}
      ids.forEach(id=>{const a=A[id];if(!a)return;const w=where(id,t);let sc=dep[id]*tw(ev.sz[id],t);
        for(const p0 of ev.pulse[id]){const u=(t-p0)/0.5;if(u>=0&&u<1)sc*=1+0.18*Math.sin(Math.PI*u)*Math.max(HOP,0.5);}
        const jump=ev.pulse[id].reduce((h,p0)=>{const u=(t-p0)/0.5;return u>=0&&u<1?Math.max(h,Math.sin(Math.PI*u)*Z*0.3*HOP):h;},0);
        a.g.setAttribute("transform",`translate(${w.p[0].toFixed(1)} ${w.p[1].toFixed(1)})`);
        a.b.setAttribute("transform",`translate(0 ${(-w.hop-jump).toFixed(1)}) scale(${(sc*(2-w.sq)).toFixed(3)} ${(sc*w.sq).toFixed(3)})`);
        const out=inAny(ev.out[id],t)?0:+tw(ev.fade[id],t).toFixed(2);if(out!==a.o){a.o=out;a.g.style.opacity=out;}
        const gr=inAny(ev.gray[id],t);if(gr!==a.gr){a.gr=gr;a.g.classList.toggle("st-gray",gr);}
        const gl=ev.glow[id].reduce((x,[g0,g1])=>t>=g0&&t<g1?Math.max(x,Math.sin(Math.PI*(t-g0)/(g1-g0))):x,0);a.glow.setAttribute("opacity",gl.toFixed(2));
        let m=(lastOf(ev.mood[id],t)||[0,"happy"])[1];if(inAny(ev.talk[id],t)&&Math.floor(t*6.5)%2)m="o";
        if(m!==a.m&&a.body){a.m=m;a.body.dataset.mood=m;}
        /* the eyes look where it walks (or at the one it helps) */
        const look=w.moving?[Math.sign(w.moving[0])*1.6,Math.sign(w.moving[1])*1.1]:[0,0];a.pup.forEach(pu=>pu.setAttribute("transform",`translate(${look[0]} ${look[1]})`));});
      ev.link.forEach(([t0,a,b])=>{const i=edges.findIndex(e=>e[0]===a&&e[1]===b);const L=links[i];if(!L)return;const o=clamp(1-(t-t0)/0.7,0,1);
        L.setAttribute("stroke-dashoffset",o.toFixed(3));L.style.opacity=o>=1?0:1;if((o<0.05)!==L.__head){L.__head=o<0.05;if(L.__head)L.setAttribute("marker-end","url(#xhead)");else L.removeAttribute("marker-end");}});   /* the head appears when the line arrives */
      let oi=0;const lead=[];ev.orb.forEach(([t0,t1,a,b])=>{if(t<t0||t>=t1||oi>=orbs.length)return;const u=ease((t-t0)/(t1-t0));const p=where(a,t).p,q=where(b,t).p;
        const mx=(p[0]+q[0])/2,my=Math.min(p[1],q[1])-60,x=(1-u)*(1-u)*p[0]+2*(1-u)*u*mx+u*u*q[0],y=(1-u)*(1-u)*(p[1]-Z*0.2)+2*(1-u)*u*my+u*u*(q[1]-Z*0.2);
        orbs[oi].setAttribute("opacity","1");orbs[oi].setAttribute("transform",`translate(${x.toFixed(1)} ${y.toFixed(1)})`);if(!oi)lead.push([t0,t1,p,q,mx,my]);oi++;});
      for(let i=oi;i<orbs.length;i++)orbs[i].setAttribute("opacity","0");
      trails.forEach((c,i)=>{const L=lead[0];if(!L){c.setAttribute("opacity","0");return;}const [t0,t1,p,q,mx,my]=L;const tt=t-0.05*(i+1);const u=ease(clamp((tt-t0)/(t1-t0),0,1));
        const x=(1-u)*(1-u)*p[0]+2*(1-u)*u*mx+u*u*q[0],y=(1-u)*(1-u)*(p[1]-Z*0.2)+2*(1-u)*u*my+u*u*(q[1]-Z*0.2);c.setAttribute("cx",x.toFixed(1));c.setAttribute("cy",y.toFixed(1));c.setAttribute("opacity",String((0.7-i*0.1).toFixed(2)));});
      let si=0;ev.spark.forEach(([t0,id])=>{const u=(t-t0)/1.1;if(u<0||u>=1)return;const c=where(id,t).p;for(let j=0;j<7&&si<sparks.length;j++,si++){const ang=j/7*Math.PI*2+0.4,r=Z*0.4+u*Z*0.75;
        sparks[si].setAttribute("transform",`translate(${(c[0]+Math.cos(ang)*r).toFixed(1)} ${(c[1]-Z*0.2+Math.sin(ang)*r).toFixed(1)}) rotate(${(u*180).toFixed(0)}) scale(${(1.2-u*0.6).toFixed(2)})`);sparks[si].setAttribute("opacity",(1-u).toFixed(2));}});
      for(let i=si;i<sparks.length;i++)sparks[i].setAttribute("opacity","0");
      const bs=ev.bub.filter(([t0,t1])=>t>=t0&&t<t1).slice(-2),key=bs.map(b=>b[0]+b[2]).join("|");
      if(key!==bubKey){bubKey=key;bubL.innerHTML=bs.map(([t0,t1,id,txt])=>{const L=lines(txt,17,3),w=Math.min(W-16,Math.max(...L.map(x=>x.replace(/[«»]/g,"").length))*8.6+28),h=L.length*19+16;return `<g class="st-bub" data-for="${id}"><rect x="${-w/2}" y="${-h}" width="${w}" height="${h}" rx="12"/><path d="M-8 -1 L0 11 L8 -1Z"/>${L.map((x,i)=>`<text y="${-h+21+i*19}" text-anchor="middle">${stBold(x)}</text>`).join("")}</g>`;}).join("");}   /* 🆕 batch 38: the name in bold, no «» (the teen / secondary bubbles still had them) */
      bubL.querySelectorAll(".st-bub").forEach(g=>{const w=where(g.dataset.for,t);const bw=+g.querySelector("rect").getAttribute("width");const x=clamp(w.p[0],bw/2+6,W-bw/2-6);g.setAttribute("transform",`translate(${x.toFixed(1)} ${(w.p[1]-Z*0.62-w.hop).toFixed(1)})`);});});}};}

/* ---------- 🎬 the lesson's story: since batch 38 it lives in story38.js (one order for every graph, a way of showing it for every age) ---------- */

/* ======================= 🎬 EVERY CONCEPT'S CARTOON (batch 33, Hareth: «كل مشهد SVG بيتحرك زي الفيديو، لكل مفهوم، حتى لمادة جديدة») =======================
   It takes the place of «تعرّف عليّ» (the same facts: the concept, what it needs, who needs it, and why — from the «meet» scene the factory checked):
   · the concept walks in and tells who it is (its facts as subtitles, it talks);
   · each thing it NEEDS walks in and GIVES it a glowing ball (the arrow is drawn);
   · then the concept walks over to each one that needs IT and gives it a ball (it helps them);
   · «what if it disappears?»: it walks out, the ones who need it turn grey and sad; it comes back;
   · the summary, everyone jumps. Any graph, any subject: no word is written by hand. */
const cstoryCache={};
function cstoryOf(l,c,m){const key=l.lesson_id+"|"+c.concept_id;if(cstoryCache[key])return cstoryCache[key];
  const ins=(m.ins||[]).slice(0,3),outs=(m.outs||[]).slice(0,3);
  const facts=(m.steps||[]).filter(x=>/^📌/.test(x)).map(stShort).filter(Boolean).slice(0,3);
  const why={};Object.entries(m.roles||{}).forEach(([a,r])=>why[a]=stShort(r));
  const s={kind:"cstory",target:m.target,ins,outs,why,facts,edges:ins.map(a=>[a,m.target]).concat(outs.map(o=>[m.target,o])),
    steps:[`🎬 ${VOICE("تفرّج على")} «${exName(m.target)}»: ${stW()?stW().intro:VOICE("شو بيحتاج، ومين بيحتاجه")}.`],paragraph:m.paragraph||""};
  cstoryCache[key]=s;return s;}
/* 🆕 batch 42 (Hareth: «التكرار»): the lines that are not facts, in other words — for the little ones and the juniors (the older keep
   the plain line). Each concept always gets the same form (its id decides); two concepts side by side mostly not. */
const cvPick=(key,id,arr)=>arr[[...(key+"|"+id)].reduce((a,c)=>(a*31+c.charCodeAt(0))>>>0,7)%arr.length];
const CV={greet:[n=>`أهلاً! أنا ${n} 👋`,n=>`مرحبا! اسمي ${n} 👋`,n=>`هاي! أنا ${n}، تعال نتعرّف 👋`,n=>`يا هلا! أنا ${n} 👋`],
  askIn:[(n,f,x)=>`${VOICE("شو")} ${stNeeds(x)} ${n}${VOICE("؟")}`,(n,f)=>`بدون شو ما ${f?"بتقدر":"بيقدر"} ${n}؟`,n=>`مين بيساعد ${n}؟`,(n,f)=>`شو لازم يكون موجود عشان ${n}؟`],
  askOut:[f=>`${VOICE("مين")} ${VOICE(f?"بيحتاجها":"بيحتاجه")}${VOICE("؟")}`,f=>`ولمين ${f?"هي مهمة":"هو مهم"}؟`,f=>`مين ${f?"بيستناها":"بيستناه"}؟`],
  wif:[(n,f)=>`${VOICE("شو بيصير لو")} ${f?"اختفت":"اختفى"} ${n}؟`,(n,f)=>`تخيّل ${n} ${f?"راحت":"راح"}… شو بيصير؟`,(n,f)=>`لو ${f?"غابت":"غاب"} ${n}، مين بيزعل؟`],
  back:["وكل إشي رجع يشتغل","والكل رجع مبسوط","وصار كل إشي تمام"]};
function sceneCStory(s){const v=V(),lo=document.body.dataset.q==="lo",kid=stageNow()==="kids",k=speedNow(),theme=ST_THEME[(graph()||{}).subject]||"room";
  const X=s.target,fem=stFem(exName(X)),ins=s.ins,outs=s.outs,ids=[X].concat(ins,outs),side=Math.max(1,ins.length,outs.length);
  const W=v?380:760,Z=v?62:78,floor=v?120:150;
  const H=(v?floor+70+(ins.length?112:0)+112+(outs.length?112:0)+20:Math.max(400,floor+60+side*108))+(v?64:58);
  /* the concept in the middle; what it needs on the right (it comes first), who needs it on the left; phone: above / below */
  const pos={};const mid=v?floor+70+(ins.length?112:0):floor+50+side*54;
  pos[X]=[W/2,mid];
  ins.forEach((a,i)=>pos[a]=v?[W-W*(i+0.5)/ins.length,floor+70]:[W-110,floor+58+(i+0.5)*(side*108/ins.length)-54*0+(side-ins.length)*0]);
  outs.forEach((o,i)=>pos[o]=v?[W-W*(i+0.5)/outs.length,mid+112]:[110,floor+58+(i+0.5)*(side*108/outs.length)]);
  if(!v){ins.forEach((a,i)=>pos[a][1]=floor+4+(i+0.5)*(side*108/ins.length));outs.forEach((o,i)=>pos[o][1]=floor+4+(i+0.5)*(side*108/outs.length));}
  const scale={};ids.forEach(id=>scale[id]=id===X?1.22:0.98);
  let T=0;const K=stKit(ids,pos,W,Z,k),{ev,d,mv,mood,sub,bub,chap,cue,N}=K;
  /* 0 · the title + the concept walks in and tells who it is */
  chap(0,VOICE("البداية"));sub(0,d(2.2),`🎬 ${N(X)}`);T=d(1.3);
  chap(T,VOICE("تعرّف عليّ"));T=K.enter(X,T,1.6);
  bub(X,T,T+d(1.6),kid?cvPick("greet",X,CV.greet)(N(X)):N(X));ev.talk[X].push([T,T+d(1.2)]);cue(T,"pop");T+=d(1.4);
  s.facts.forEach(f=>{sub(T,T+d(3.4),`${N(X)}: ${f}`);ev.talk[X].push([T,T+d(2.2)]);ev.pulse[X].push(T+d(0.1));T+=d(3.5);});
  if(!s.facts.length)T+=d(1);
  /* 1 · what it needs: each one walks in and gives */
  const young=["kids","junior"].includes(stageNow());
  if(ins.length){chap(T,stW()?stW().askIn(N(X),fem):young?cvPick("askIn",X,CV.askIn)(N(X),fem,X):`${VOICE("شو")} ${stNeeds(X)} ${N(X)}${VOICE("؟")}`);
    ins.forEach(a=>{T=K.enter(a,T,1.3)+d(0.2);T=K.give(a,X,T,`${N(X)} ${stNeeds(X)} ${N(a)}${s.why[a]?`: ${s.why[a]}`:""}`);});}
  /* 2 · who needs it: they wait (curious), the concept walks over and gives */
  if(outs.length){chap(T,stW()?stW().askOut(fem):young?cvPick("askOut",X,CV.askOut)(fem):`${VOICE("مين")} ${VOICE(fem?"بيحتاجها":"بيحتاجه")}${VOICE("؟")}`);
    outs.forEach(o=>{T=K.enter(o,T,1.3);mood(o,T,"o");T+=d(0.3);T=K.give(X,o,T,`${N(o)} ${stNeeds(o)} ${N(X)}${s.why[o]?`: ${s.why[o]}`:""}`);});}
  /* 3 · what if it disappears? (only when someone needs it) */
  if(outs.length){chap(T,VOICE("شو لو اختفى؟"));sub(T,T+d(2.2),`🤔 ${stW()?stW().wif(N(X),fem):young?cvPick("wif",X,CV.wif)(N(X),fem):`${VOICE("شو بيصير لو")} ${fem?"اختفت":"اختفى"} ${N(X)}؟`}`);
    mv(X,T+d(0.6),T+d(1.8),pos[X],[pos[X][0],-90]);ev.out[X].push([T+d(1.5),T+d(4.2+outs.length*0.6)]);cue(T+d(0.7),"flip");
    outs.forEach((o,i)=>{const t=T+d(2.0+i*0.6);mood(o,t,"sad");ev.gray[o].push([t,T+d(4.2+outs.length*0.6)]);cue(t,"bad");});
    sub(T+d(2.2),T+d(4.1+outs.length*0.6),`😟 ${outs.map(N).join(" و")} ${stW()?stW().lost(stFem(exName(outs[0])),outs.length>1):VOICE(outs.length>1?"ما بيقدروا":stFem(exName(outs[0]))?"ما بتقدر":"ما بيقدر")} ${fem?"بدونها":"بدونه"}!`);
    const back=T+d(4.2+outs.length*0.6);mv(X,back,back+d(1.2),[pos[X][0],-90],pos[X]);
    outs.forEach((o,i)=>{mood(o,back+d(1.2+i*0.2),"joy");mood(o,back+d(2.4+i*0.2),"happy");});cue(back+d(1.2),"good");ev.spark.push([back+d(1.2),X]);
    sub(back,back+d(2.6),`✨ ${fem?"رجعت":"رجع"} ${N(X)}… ${stW()?stW().back:young?cvPick("back",X,CV.back):VOICE("وكل إشي رجع يشتغل")}!`);T=back+d(2.8);}
  /* 4 · the summary (only what the graph says) */
  const parts=[];if(ins.length)parts.push(`${N(X)} ${stNeeds(X)} ${ins.map(N).join(" و")}`);if(outs.length)parts.push(`${outs.map(N).join(" و")} ${outs.length>1?stNeedsMany():stNeeds(outs[0])} ${N(X)}`);
  chap(T,VOICE("الخلاصة"));sub(T,T+d(3.4),parts.length?`💡 ${parts.join("، و")}.`:`💡 ${N(X)}${s.facts[0]?": "+s.facts[0]:""}.`);
  ids.forEach((id,i)=>{ev.pulse[id].push(T+d(0.2+i*0.12));mood(id,T+d(0.2),"joy");});ev.spark.push([T+d(0.3),X]);cue(T+d(0.3),"tada");
  T+=d(3.8);
  return stMake({ids,pos,W,H,floor,Z,theme,edges:s.edges,title:exName(X),ev,DUR:T,lo,k,scale,kind:"cstory",label:`${VOICE("تعرّف عليّ")}: ${exName(X)}`});}
SCENES.cstory=sceneCStory;SNAME.cstory="🎬 تعرّف عليّ";

