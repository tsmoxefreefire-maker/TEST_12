/* ================================================================ 🆕 batch 43 · TWO NEW ACTIVITIES (explain_activities3.py)
   Hareth: «ممكن تزيد لي فعالية فعاليتين جداد». For the concepts with FEW scenes (few arrows in the graph): they need only the
   concept's name and meaning. Both are the STUDENT's (closed to the video, like every activity since batch 41), the same game frame
   (games36.js: mission, dots, stars), no points, no failing — a wrong move gets an explanation.
   · 🕵️ who_am_i → a character hides behind «؟»; the clues come one by one; pick it from the cards. A wrong card says what THAT one is,
                  and opens one more clue. Right → the «؟» opens and the character jumps out: «أنا «X»!».
   · 🧩 sentence → the concept's meaning in 3–4 mixed pieces; tap them in order and the sentence is built under «X».
   Rules: classes start with «w43-» / «s43-» · tapping always works · a phone has its own layout · timers check root.isConnected. */

/* ---------------------------------------------------------------- 🕵️ WHO AM I? */
function sceneWhoAmI(s){const v=V(),W=v?380:640,H=v?250:230,T=[W/2,v?118:110],Z=v?104:112;
  const svg=`<svg class="xstage w43-who" id="xs" viewBox="0 0 ${W} ${H}" data-bubble="72" role="img" aria-label="${naEsc(VOICE("مين أنا؟"))}">${DEFS}
    <g class="w43-spot"><ellipse cx="${T[0]}" cy="${T[1]+Z*0.5}" rx="${Z*0.62}" ry="${Z*0.12}"/></g>
    ${node(s.target,T[0],T[1],Z,"happy","w43-hero w43-hidden")}
    <g class="w43-mys" transform="translate(${T[0]} ${T[1]})" aria-hidden="true"><path d="M${-Z*0.42} ${Z*0.44} C${-Z*0.5} ${-Z*0.1} ${-Z*0.34} ${-Z*0.5} 0 ${-Z*0.5} C${Z*0.34} ${-Z*0.5} ${Z*0.5} ${-Z*0.1} ${Z*0.42} ${Z*0.44} Z"/>
      <text y="${Z*0.12}" text-anchor="middle">؟</text></g></svg>
    <ol class="w43-clues" id="w43Clues">${s.clues.map((c,i)=>`<li class="w43-clue${i<s.start?" on":""}" data-i="${i}"><span class="w43-n">🔎 ${VOICE("دليل")} ${i+1}</span> <span class="w43-t">${t37(VOICE(c.say))}</span></li>`).join("")}</ol>
    <p class="g36-ask" id="w43Ask">${t37(VOICE("👇 مين أنا؟"))}</p><div class="na-opts g36-jopts w43-opts" id="w43Opts"></div>`;
  return {svg,wire:root=>{const box=document.getElementById("w43Opts"),list=document.getElementById("w43Clues");let shown=Math.min(s.start,s.clues.length),done=false;
      /* the answer is not given away by the top bar: its name and picture wait behind a «؟» until he finds it */
      const mask=on=>{const w=document.querySelector("#prog .where .t37-name");if(w){if(on){w.dataset.n=w.dataset.n||w.textContent;w.textContent="؟";}else if(w.dataset.n)w.textContent=w.dataset.n;}
        const st=document.querySelector("#prog .pstop.on");if(st)st.classList.toggle("w43-mask",on);};
      mask(true);
      gxStart(root,{kind:"who_am_i",target:s.target,total:1,goal:VOICE("اقرأ الأدلة وحزّر مين المخبّى")});
      const open=()=>{if(shown>=s.clues.length)return false;const li=list.querySelector(`.w43-clue[data-i="${shown}"]`);if(li){li.classList.add("on","w43-new");setTimeout(()=>li.classList.remove("w43-new"),900);}shown++;return true;};
      const opts=s.options.map(o=>Object.assign({},o,{label:exName(o.id),art:g36Art(o.id)}));
      g36Opts(box,opts,(j,b)=>{if(done)return;naTake(root);const o=opts[j];
        if(o.ok){done=true;box.querySelectorAll(".na-opt").forEach(x=>x.disabled=true);b.classList.add("g36-right");
          while(open());mask(false);root.querySelector(".w43-mys").classList.add("w43-gone");const hero=root.querySelector(".w43-hero");hero.classList.remove("w43-hidden");hero.classList.add("w43-pop");
          mood(root,s.target,"laugh");sfx("good");gxGood(root);say(root,s.target,grown()?`«${exName(s.target)}»`:`أنا «${exName(s.target)}»! 😄`);
          setTimeout(()=>{if(!root.isConnected)return;cap(s.win);sfx("tada");if(!grown())sparkles();gxWin(root);},650);}
        else{b.disabled=true;b.classList.add("na-wrong");sfx("nope");gxBad(root);const more=open();
          cap(o.why+(more?" "+VOICE("🔎 فتحتلك دليل جديد."):""));}});
      cap(VOICE("🕵️ اقرأ الأدلة تحت الصورة، واختار مين أنا."));}};}

/* ---------------------------------------------------------------- 🧩 BUILD THE SENTENCE */
function sceneSentence(s){const v=V(),W=v?380:640,H=v?200:190,T=[W/2,v?96:92],Z=v?100:104,n=s.chunks.length;
  const order=shuffle(s.chunks.map((_,i)=>i),[...String(s.target)].reduce((a,c)=>a+c.charCodeAt(0),11));
  if(order.every((x,i)=>x===i))order.push(order.shift());                    /* never already in order */
  const svg=`<svg class="xstage s43-sen" id="xs" viewBox="0 0 ${W} ${H}" data-bubble="70" role="img" aria-label="${naEsc(VOICE("ركّب الجملة"))}">${DEFS}
    ${node(s.target,T[0],T[1],Z,"o","s43-hero")}</svg>
    <div class="s43-line" id="s43Line" aria-live="polite">${s.chunks.map((_,i)=>`<span class="s43-slot" data-i="${i}">${i===0?"①":i===1?"②":i===2?"③":"④"}</span>`).join("")}</div>
    <div class="s43-tray" id="s43Tray">${order.map(i=>`<button type="button" class="na-opt s43-chunk" data-i="${i}">${naEsc(s.chunks[i])}</button>`).join("")}</div>`;
  return {svg,wire:root=>{let pos=0,busy=false;const line=document.getElementById("s43Line");
      gxStart(root,{kind:"sentence",target:s.target,total:n,goal:`${VOICE("ركّب جملة")} «${naEsc(exName(s.target))}» ${VOICE("بالترتيب")}`});
      say(root,s.target,grown()?VOICE("رتّب تعريفي"):VOICE("جملتي تخربطت! رتّبها 🙏"));
      document.querySelectorAll("#s43Tray .s43-chunk").forEach(b=>b.addEventListener("click",()=>{if(busy||pos>=n)return;naTake(root);
        const txt=s.chunks[+b.dataset.i];
        if(txt===s.chunks[pos]){const sl=line.querySelector(`.s43-slot[data-i="${pos}"]`);sl.textContent=txt;sl.classList.add("on","s43-new");setTimeout(()=>sl.classList.remove("s43-new"),700);
          b.disabled=true;b.classList.add("s43-used");pos++;sfx("good");gxGood(root);mood(root,s.target,pos===n?"laugh":"happy");
          if(pos===n){busy=true;line.classList.add("s43-done");say(root,s.target,s.sentence);setTimeout(()=>{if(!root.isConnected)return;cap(s.win);sfx("tada");if(!grown())sparkles();gxWin(root);},600);}
          else cap(`✅ ${VOICE("صح!")} ${VOICE("شو بيجي بعد")} «${s.chunks[pos-1]}»؟`);}
        else{sfx("nope");gxBad(root);mood(root,s.target,"o");b.classList.remove("s43-shake");void b.offsetWidth;b.classList.add("s43-shake");
          cap(pos===0?VOICE("🙂 مش هاي أول قطعة. دوّر على بداية الجملة."):`🙂 ${VOICE("مش هاي. شو بيجي بعد")} «${s.chunks[pos-1]}»؟`);}}));
      cap(VOICE("🧩 اكبس أول قطعة من الجملة."));}};}

SCENES.who_am_i=sceneWhoAmI;SNAME.who_am_i="🕵️ مين أنا؟";SCENES.sentence=sceneSentence;SNAME.sentence="🧩 ركّب الجملة";
Object.assign(GX_ICON,{who_am_i:"🕵️",sentence:"🧩"});Object.assign(GX_BADGE,{who_am_i:"المحقق الذكي",sentence:"بطل الجمل"});
