/* ===== 🆕 batch 36 (Hareth: «الفعاليات… بتحس إنك بس بتلمس وتحط… أنا بحطها بحيث الطالب يتعلم ويستمتع… حسّنها») · THE GAME LAYER =====
   Every activity becomes a small GAME with the same friendly frame (all of it is shown, never a score that hurts):
   · 🎯 a MISSION at the top («أطعم «الجذر» كل اللي بيحتاجه») with its progress dots (●●○);
   · a right move: the dot fills (a little pop), «🔥 ٣ ورا بعض!» when he is on a roll, the PLACE cheers (the sun laughs, someone claps);
   · a mistake: never a red cross — the banner shakes softly and the place says «أوه» (the scene itself explains WHY);
   · the end: STARS by how many tries it took (⭐⭐⭐ «من أول مرة!» · ⭐⭐ · ⭐ «وصلت بالآخر، برافو!»), a BADGE for the little ones
     («طبّاخ «الجذر» الماهر»), confetti and a party in the place, and «🔁 العب كمان».
   The older stages: the same frame, quieter words, no confetti, no badge. 🆕 batch 41: the video never plays a game for him; his win
   (gxWin) is what lets the video go on (actWon in narrator.js).
   Rules: every class starts with «gx-» · events go to the place as «gx» (life36.js listens) · one game at a time (GX = the current one). */
const GX={root:null};
const GX_ICON={recipe:"🍽️",compare:"⚖️",teach:"💡",ladder:"🪜",journey:"🧭",what_if:"🔮",throw:"🪃",tower:"🏗️",magnet:"🧲",machine:"⚙️",power:"⚡",connect:"✏️"};
const GX_BADGE={recipe:"طبّاخ {t} الماهر",compare:"خبير المقارنة",teach:"أستاذ {t}",ladder:"بطل السلّم",journey:"دليل الرحلة",what_if:"العرّاف الذكي",
  throw:"الرامي الماهر",tower:"مهندس البرج",magnet:"صاحب المغناطيس",machine:"الميكانيكي الشاطر",power:"الكهربائي الشاطر",connect:"رسّام الأسهم"};
function gxSend(type){try{document.dispatchEvent(new CustomEvent("gx",{detail:{type}}));}catch(e){}}
function gxPips(){const m=GX.root&&GX.root.closest(".xwrap")&&GX.root.closest(".xwrap").querySelector(".gx-pips");if(!m)return;const n=Math.min(GX.total,12);
  m.innerHTML=Array.from({length:n},(_,i)=>`<i class="${i<GX.done?"on":""}${i===GX.done-1&&GX.pop?" pop":""}"></i>`).join("");GX.pop=false;
  m.setAttribute("aria-label",`${GX.done} ${VOICE("من")} ${GX.total}`);}
/* a new game starts (called by the activity's wire) */
function gxStart(root,o){const wrap=root&&root.closest(".xwrap");if(!wrap)return;Object.assign(GX,{root,kind:o.kind,total:Math.max(1,o.total||1),done:0,miss:0,combo:0,won:false,t:o.target,pop:false});
  wrap.querySelectorAll(".gx-mission,.gx-end,.gx-combo").forEach(x=>x.remove());
  const m=document.createElement("div");m.className="gx-mission";m.setAttribute("role","status");
  m.innerHTML=`<span class="gx-ic" aria-hidden="true">${GX_ICON[o.kind]||"🎯"}</span><b class="gx-goal">${richText(VOICE(o.goal||""))}</b><span class="gx-pips" role="img"></span>`;
  wrap.insertBefore(m,wrap.firstChild);gxPips();}
const gxMine=root=>GX.root&&GX.root===root&&root.isConnected;
/* a right move */
function gxGood(root){if(!gxMine(root)||GX.won)return;GX.done=Math.min(GX.total,GX.done+1);GX.combo++;GX.pop=true;gxPips();gxSend("good");
  if(GX.combo>=3&&GX.combo===Math.min(GX.total,GX.combo)&&!grown()){const wrap=root.closest(".xwrap");const c=document.createElement("div");c.className="gx-combo";
    c.textContent=`🔥 ${GX.combo} ${VOICE("ورا بعض!")}`;wrap.appendChild(c);setTimeout(()=>c.remove(),1500);}}
/* the progress, said again (after the student takes something back) — no sound, no combo */
function gxSet(root,n){if(!gxMine(root))return;GX.done=Math.max(0,Math.min(GX.total,n));gxPips();}
/* a mistake (the scene explains why) */
function gxBad(root){if(!gxMine(root)||GX.won)return;GX.miss++;GX.combo=0;gxSend("bad");
  const m=root.closest(".xwrap")&&root.closest(".xwrap").querySelector(".gx-mission");if(m){m.classList.remove("gx-shake");void m.offsetWidth;m.classList.add("gx-shake");}}
/* the end: stars, a badge (the little ones), confetti, the place's party */
function gxWin(root){if(!gxMine(root)||GX.won)return;GX.won=true;GX.done=GX.total;gxPips();gxSend("win");
  const wrap=root.closest(".xwrap"),m=wrap.querySelector(".gx-mission");if(m)m.classList.add("gx-done");
  const st=GX.miss===0?3:GX.miss<=2?2:1,g=grown();
  const msg=g?{3:"دقة كاملة",2:"ممتاز، أخطاء قليلة",1:"أنجزت المهمة"}[st]:{3:"من أول مرة! 🤩",2:"شاطر! قرّبت تكون كاملة 👍",1:"وصلت بالآخر، برافو! 💪"}[st];
  const badge=!g&&GX_BADGE[GX.kind]?GX_BADGE[GX.kind].replace("{t}",GX.t?exName(GX.t):""):"";
  setTimeout(()=>{if(!root.isConnected)return;wrap.querySelectorAll(".gx-end").forEach(x=>x.remove());const e=document.createElement("div");e.className="gx-end";e.setAttribute("role","status");
    e.innerHTML=`<span class="gx-stars" aria-label="${st} ${VOICE("من")} 3">${[1,2,3].map(i=>`<i class="${i<=st?"on":""}" style="animation-delay:${i*0.18}s">${g?"★":"⭐"}</i>`).join("")}</span>
      <span class="gx-msg">${badge?`<b>${GX_ICON[GX.kind]||"🏅"} ${badge}</b>`:""}<small>${msg}</small></span>
      <button type="button" class="chipbtn gx-again">🔁 ${VOICE("العب كمان")}</button><button type="button" class="gx-x" aria-label="${VOICE("سكّر")}">✕</button>`;
    root.after(e);                                                          /* right under the picture: it never covers what he just did */
    e.querySelector(".gx-again").addEventListener("click",()=>{sfx("flip");renderScene();const r=document.getElementById("xs");if(r)stopVideo(r);});e.querySelector(".gx-x").addEventListener("click",()=>e.remove());
    if(!g&&!reduce&&document.body.dataset.q!=="lo")gxConfetti(wrap);},700);
  actWon(root);}                                                            /* 🆕 batch 41: HE won → «ليش؟» and the video goes on */
function gxConfetti(wrap){const c=["#F59BB8","#F5D547","#7FB7F2","#7DD08A","#F5A623","#C4A7E7"];for(let i=0;i<34;i++){const p=document.createElement("i");p.className="gx-conf";
    p.style.left=(4+Math.random()*92)+"%";p.style.background=c[i%c.length];p.style.animationDelay=(Math.random()*0.5)+"s";p.style.setProperty("--cx",((Math.random()-.5)*80).toFixed(0)+"px");p.style.setProperty("--cr",(Math.random()*720-360).toFixed(0)+"deg");
    wrap.appendChild(p);setTimeout(()=>p.remove(),2600);}}
/* a character reacts to the move (the target jumps on a right one, shakes its head on a wrong one) */
function gxReact(root,id,good){const nd=root.querySelector(`.xnode[data-id="${id}"]`);if(!nd)return;const c=good?"gx-yay":"gx-nope";nd.classList.remove("gx-yay","gx-nope");void nd.getBoundingClientRect();nd.classList.add(c);setTimeout(()=>nd.classList.remove(c),900);}
