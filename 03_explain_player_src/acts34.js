/* ===== 🆕 batch 34 (Hareth: «ضيف خمس فعاليات جديدة تكون حلوة») · five GAMES =====
   🪃 throw (💡 Hareth's idea) · 🏗️ tower · 🧲 magnet · ⚙️ machine · ⚡ power. All the facts come from the factory (checked against the graph).
   The same rules as the batch-26 activities (each one broke something once):
   · every class starts with «g4-» · no CSS animation on a <g> that has a transform (moves are done by setting the attribute, frame by frame);
   · every word goes through cap() / VOICE (the age's way of talking) · 🆕 batch 41 (Hareth): the STUDENT plays, the video never plays a game for him (it waits: «🖐️ دورك»);
   · every move is explained (right → the reason · wrong → why) · a phone (≈380px) has its own layout · tapping always works (dragging is a bonus);
   · timers stop when the scene is gone (root.isConnected).
   🆕 batch 36: each game has the game frame (games36.js: a mission, progress dots, stars and the place's party); ⚡ power starts at night. */
const G4NS="http://www.w3.org/2000/svg";
/* a tiny tween: fn(t) from 0 to 1 over ms (at once with «reduce motion») */
function g4Tween(root,ms,fn,done){if(reduce||ms<=0){fn(1);if(done)done();return;}const t0=performance.now();
  const f=now=>{if(!root.isConnected)return;const t=Math.min(1,(now-t0)/ms);fn(t);if(t<1)requestAnimationFrame(f);else if(done)done();};requestAnimationFrame(f);}
const g4Ease=t=>t<.5?2*t*t:1-Math.pow(-2*t+2,2)/2;
function g4Move(el,x,y,sc,rot){el.setAttribute("transform",`translate(${x.toFixed(1)} ${y.toFixed(1)})${sc&&sc!==1?` scale(${sc.toFixed(3)})`:""}${rot?` rotate(${rot.toFixed(1)})`:""}`);}
function g4Pos(el){const m=/translate\(\s*(-?[\d.]+)[ ,]+(-?[\d.]+)/.exec(el.getAttribute("transform")||"");return m?[+m[1],+m[2]]:[0,0];}
/* the pointer in the picture's own units */
function g4Pt(svg,e){const p=svg.createSVGPoint();p.x=e.clientX;p.y=e.clientY;const m=svg.getScreenCTM();return m?p.matrixTransform(m.inverse()):{x:0,y:0};}
const g4Q=naQ,g4V=(id,m,f)=>stFem(exName(id))?f:m;
/* an arrow «a needs b» drawn into a layer (from the one who needs to what it needs, like everywhere) */
function g4Arrow(layer,pa,pb,ra,rb,cls){const [p,q]=naEnds(pa,pb,ra,rb);const g=document.createElementNS(G4NS,"g");g.setAttribute("class","xedge lit g4-arr "+(cls||""));g.innerHTML=flow(curve(p,q,14),"",0,false);layer.appendChild(g);return g;}

/* ---------------------------------------------------------------- 🪃 THROW (Hareth: «ماسك اشي وفلتته فبصير يطير في الجو»)
   Fling a ball to «X». Aimed roughly at X → it flies in a real arc and X catches it (what X needs) or bounces it back (anything else).
   Aimed away → it falls and comes back («صوّب عليه»). A tap = a perfect throw (phones, keyboards, the video). */
function sceneThrow(s){const v=V(),n=s.balls.length,W=v?380:640,H=v?470:360,Z=v?96:110,BZ=v?58:62;
  const X=v?[W/2,118]:[W-130,H/2-14];
  const rack=s.balls.map((b,i)=>v?[W*(i+0.5)/n,H-74]:[78+(i%2)*104,58+Math.floor(i/2)*((H-110)/Math.max(1,Math.ceil(n/2)-1||1))]);
  if(!v&&n<=2)rack.forEach((p,i)=>{p[0]=110;p[1]=H/2-60+i*120;});
  const svg=`<svg class="xstage g4-throw" id="xs" viewBox="0 0 ${W} ${H}" data-bubble="78" role="img" aria-label="${naEsc(VOICE("ارمي وطيّر"))}">${DEFS}
    <circle class="g4-catch" cx="${X[0]}" cy="${X[1]}" r="${(Z*0.78).toFixed(1)}"/><g id="g4Arr"></g>
    ${node(s.target,X[0],X[1],Z,"happy","star g4-x")}
    <g id="g4Balls">${s.balls.map((b,i)=>node(b.id,rack[i][0],rack[i][1],BZ,"happy","g4-ball").replace('class="xnode','data-i="'+i+'" class="xnode')).join("")}</g>
    <path class="g4-aim" id="g4Aim" d="" /></svg>
    <p class="g4-count" id="g4Count" aria-live="polite">0 ${VOICE("من")} ${s.balls.filter(b=>b.ok).length}</p>`;
  return {svg,wire:root=>{const need=s.balls.filter(b=>b.ok).length;let got=0,busy=false;const done=new Set();
      gxStart(root,{kind:"throw",target:s.target,total:need,goal:`وصّل لـ${g4Q(s.target)} كل اللي ${g4V(s.target,"بيحتاجه","بتحتاجه")}`});   /* 🆕 batch 36: the game frame (games36.js) */
      const dock=k=>{const a=(v?Math.PI*(0.15+0.7*k/Math.max(1,need-1||1)):Math.PI*(0.6+0.8*k/Math.max(1,need-1||1)));return [X[0]+Math.cos(a)*(Z*0.95),X[1]+Math.sin(a)*(Z*0.95)*(v?1:-1)*(v?1:1)];};
      const count=()=>{document.getElementById("g4Count").textContent=`${got} ${VOICE("من")} ${need}`;};
      /* the flight: an arc from where the ball is to the catching ring of X */
      const fly=(i,hit)=>{const b=s.balls[i],el=root.querySelector(`.g4-ball[data-i="${i}"]`);if(!el||busy||done.has(i))return;busy=true;naTake(root);
        const p0=g4Pos(el),p1=hit?[X[0]+(p0[0]<X[0]?-Z*0.35:Z*0.35),X[1]]:[p0[0]+(v?0:120),H+60],h=v?150:130;sfx("pick");el.classList.add("g4-flying");
        g4Tween(root,hit?760:900,t=>{const x=p0[0]+(p1[0]-p0[0])*t,y=p0[1]+(p1[1]-p0[1])*t-h*4*t*(1-t);g4Move(el,x,y,1,t*360*(hit?1:1.4));},()=>{
          if(!hit){cap(`💨 ${VOICE("ما وصلت…")} ${VOICE("صوّب على")} ${g4Q(s.target)} ${VOICE("وفلّتها")}.`);sfx("off",{n:0});
            g4Tween(root,500,t=>g4Move(el,rack[i][0],rack[i][1]+(1-t)*40,1,0),()=>{el.classList.remove("g4-flying");busy=false;});return;}
          if(b.ok){done.add(i);const k=got++;const q=dock(k);mood(root,s.target,"laugh");sfx("good");cap(b.say);count();gxGood(root);gxReact(root,s.target,true);
            g4Tween(root,380,t=>{const e=g4Ease(t);g4Move(el,p1[0]+(q[0]-p1[0])*e,p1[1]+(q[1]-p1[1])*e,1-0.3*e,0);},()=>{el.classList.remove("g4-flying");el.classList.add("g4-in");
              g4Arrow(root.querySelector("#g4Arr"),X,q,Z/2+4,BZ*0.36+6);busy=false;
              if(got===need){cap(s.win);setTimeout(()=>{if(root.isConnected)sfx("tada");},250);if(!grown())sparkles();mood(root,s.target,"laugh");gxWin(root);}
              else setTimeout(()=>{if(root.isConnected)mood(root,s.target,"happy");},900);});}
          else{done.add(i);mood(root,s.target,"o");sfx("nope");cap(b.say);el.classList.add("g4-no");gxBad(root);gxReact(root,s.target,false);
            g4Tween(root,620,t=>{const x=p1[0]+(rack[i][0]-p1[0])*t,y=p1[1]+(rack[i][1]-p1[1])*t-90*4*t*(1-t);g4Move(el,x,y,1,-t*360);},()=>{el.classList.remove("g4-flying");busy=false;setTimeout(()=>{if(root.isConnected)mood(root,s.target,"happy");},700);});}});};
      /* dragging = pulling the ball; letting go flings it the way it was moving */
      root.querySelectorAll(".g4-ball").forEach(el=>{const i=+el.dataset.i;let drag=null;
        el.addEventListener("pointerdown",e=>{if(busy||done.has(i))return;e.preventDefault();el.setPointerCapture&&el.setPointerCapture(e.pointerId);const p=g4Pt(root,e);drag={x0:p.x,y0:p.y,t0:performance.now(),hist:[[p.x,p.y,performance.now()]],moved:0};el.classList.add("g4-held");});
        el.addEventListener("pointermove",e=>{if(!drag)return;const p=g4Pt(root,e);drag.hist.push([p.x,p.y,performance.now()]);if(drag.hist.length>6)drag.hist.shift();drag.moved=Math.max(drag.moved,Math.hypot(p.x-drag.x0,p.y-drag.y0));
          g4Move(el,rack[i][0]+(p.x-drag.x0),rack[i][1]+(p.y-drag.y0),1.08,0);const a=root.querySelector("#g4Aim");a.setAttribute("d",`M${rack[i][0]} ${rack[i][1]} L${(rack[i][0]+(p.x-drag.x0)).toFixed(1)} ${(rack[i][1]+(p.y-drag.y0)).toFixed(1)}`);});
        const up=e=>{if(!drag)return;const d=drag;drag=null;el.classList.remove("g4-held");root.querySelector("#g4Aim").setAttribute("d","");
          if(d.moved<8){g4Move(el,rack[i][0],rack[i][1],1,0);fly(i,true);return;}            /* a tap: a perfect throw */
          const h=d.hist,a=h[0],b=h[h.length-1],dt=Math.max(1,b[2]-a[2]),vx=(b[0]-a[0])/dt,vy=(b[1]-a[1])/dt,sp=Math.hypot(vx,vy);
          const here=g4Pos(el),to=Math.atan2(X[1]-here[1],X[0]-here[0]),dir=Math.atan2(vy,vx);let diff=Math.abs(to-dir);if(diff>Math.PI)diff=2*Math.PI-diff;
          rack[i]=[rack[i][0],rack[i][1]];el.setAttribute("transform",`translate(${here[0]} ${here[1]})`);
          fly(i,sp<0.25?Math.hypot(X[0]-here[0],X[1]-here[1])<Z:diff<0.75);};               /* aimed at X (±43°) → it gets there */
        el.addEventListener("pointerup",up);el.addEventListener("pointercancel",up);
        el.addEventListener("keydown",e=>{if(e.key==="Enter"||e.key===" "){e.preventDefault();fly(i,true);}});});}};}

/* ---------------------------------------------------------------- 🏗️ TOWER
   The chain that ends at «X», as bricks in a tray (mixed). A brick only stays on the one it needs; a wrong one wobbles and falls back. */
function sceneTower(s){const v=V(),n=s.blocks.length,BW=v?190:210,BH=v?50:54,W=v?380:640,H=v?110+n*BH+40+Math.ceil(n/2)*(BH+14)+10:Math.max(120+n*BH,90+n*(BH*0.86+12));
  const base=v?[W/2,96+n*BH]:[W*0.34,H-46];const order=s.blocks.map((_,i)=>i);for(let i=order.length-1;i>0;i--){const j=(i*7+3)%(i+1);[order[i],order[j]]=[order[j],order[i]];}
  if(order.every((x,i)=>x===i))order.reverse();                                              /* never already in the right order */
  const slot=j=>v?[W*(j%2===0?0.27:0.73),base[1]+56+Math.floor(j/2)*(BH+14)]:[W-128,64+j*(BH*0.86+12)];
  const brick=(i,j)=>{const b=s.blocks[i],c=colorOf(b.id),p=slot(j);return `<g class="g4-brick" data-i="${i}" tabindex="0" role="button" aria-label="${naEsc(exName(b.id))}" transform="translate(${p[0]} ${p[1]})${v?"":" scale(.86)"}">
      <rect x="${-BW/2}" y="${-BH/2}" width="${BW}" height="${BH}" rx="12" style="fill:color-mix(in srgb,${c} 26%,var(--panel));stroke:color-mix(in srgb,${c} 70%,var(--ink))"/>
      <rect class="g4-shine" x="${-BW/2+6}" y="${-BH/2+5}" width="${BW-12}" height="${BH*0.28}" rx="8"/>
      ${node(b.id,BW/2-30,0,40,"happy","g4-mini")}<text class="g4-bt" x="${BW/2-58}" y="6" text-anchor="start">${naEsc(exName(b.id))}</text></g>`;};   /* RTL: the picture on the right, the name reads leftwards from it */
  const svg=`<svg class="xstage g4-tower" id="xs" viewBox="0 0 ${W} ${H}" role="img" aria-label="${naEsc(VOICE("ابني البرج"))}">
    <rect class="g4-ground" x="${base[0]-BW/2-30}" y="${base[1]+BH/2}" width="${BW+60}" height="12" rx="6"/>
    ${s.blocks.map((_,k)=>`<rect class="g4-ghost" x="${base[0]-BW/2}" y="${base[1]-k*BH-BH/2}" width="${BW}" height="${BH}" rx="12"/>`).join("")}
    ${order.map((i,j)=>brick(i,j)).join("")}</svg>
    <p class="g4-count" id="g4Count" aria-live="polite">0 ${VOICE("من")} ${n}</p>`;
  return {svg,wire:root=>{let k=0,busy=false;
      gxStart(root,{kind:"tower",target:s.target,total:n,goal:`ابني برج ${g4Q(s.target)} لفوق: كل قطعة فوق اللي ${VOICE("بتحتاجها")}`});
      const top=()=>[base[0],base[1]-k*BH];
      const tryBrick=el=>{const i=+el.dataset.i;if(busy||el.classList.contains("g4-set"))return;busy=true;naTake(root);
        const p0=g4Pos(el),t=top(),above=[t[0],t[1]-BH*2.2];sfx("pick");el.parentNode.appendChild(el);
        g4Tween(root,420,u=>{const e=g4Ease(u);g4Move(el,p0[0]+(above[0]-p0[0])*e,p0[1]+(above[1]-p0[1])*e,v?1:0.86+0.14*e,0);},()=>{
          g4Tween(root,260,u=>g4Move(el,t[0],above[1]+(t[1]-above[1])*u*u,1,0),()=>{
            if(i===k){el.classList.add("g4-set");k++;sfx("good");cap(s.blocks[i].why);gxGood(root);document.getElementById("g4Count").textContent=`${k} ${VOICE("من")} ${n}`;
              g4Tween(root,220,u=>g4Move(el,t[0],t[1]+Math.sin(u*Math.PI)*4,1,0),()=>{busy=false;
                if(k===n){cap(s.win);setTimeout(()=>{if(root.isConnected)sfx("tada");},200);if(!grown())sparkles();root.classList.add("g4-won");gxWin(root);}});}
            else{const y=s.blocks[i].id,want=s.blocks[k].id,under=k?s.blocks[k-1].id:null;sfx("nope");gxBad(root);
              cap(k===0?`🙃 ${g4Q(y)} ${g4V(y,"مش هو","مش هي")} ${VOICE("الأساس")}: ${i===1?`${g4Q(y)} ${stNeeds(y)} ${g4Q(want)}`:VOICE("في قطع لازم تكون تحته")}. ${VOICE("دوّر على اللي تحت الكل.")}`
                 :i===k+1?`🙃 ${g4Q(y)} ${g4V(y,"ما بيقعد","ما بتقعد")} ${VOICE("فوق")} ${g4Q(under)}: ${g4Q(y)} ${stNeeds(y)} ${g4Q(want)} ${VOICE("تحته أول")}.`
                 :`🙃 ${g4Q(y)} ${g4V(y,"مكانه","مكانها")} ${VOICE("أعلى من هيك")}. ${VOICE("اللي بيقعد فوق")} ${g4Q(under)} ${VOICE("هو اللي بيحتاجه")}.`);
              g4Tween(root,700,u=>g4Move(el,t[0]+u*(v?40:90),t[1]+u*u*60,1,Math.sin(u*18)*12*(1-u)+u*35),()=>{const j=order.indexOf(i),p=slot(j);
                g4Tween(root,380,u=>{const e=g4Ease(u);g4Move(el,t[0]+(v?40:90)+(p[0]-t[0]-(v?40:90))*e,t[1]+60+(p[1]-t[1]-60)*e,v?1:1-0.14*e,35*(1-e));},()=>{busy=false;});});}});});};
      root.querySelectorAll(".g4-brick").forEach(el=>{el.addEventListener("click",()=>tryBrick(el));el.addEventListener("keydown",e=>{if(e.key==="Enter"||e.key===" "){e.preventDefault();tryBrick(el);}});});}};}

/* ---------------------------------------------------------------- 🧲 MAGNET
   «X» is a magnet. Bring it close to someone (drag it, or tap the one): whoever NEEDS «X» is pulled in and sticks (the arrow is drawn);
   the others do not move («ما إله علاقة»). */
function sceneMagnet(s){const v=V(),n=s.items.length,W=v?380:640,H=v?440:360,Z=v?92:104,IZ=v?62:66;
  const C=[W/2,H/2-6],R=v?Math.min(150,W/2-50):Math.min(H/2-50,200);
  const at=s.items.map((_,i)=>{const a=-Math.PI/2+2*Math.PI*(i+0.5)/n;return [C[0]+Math.cos(a)*(v?R:R*1.45),C[1]+Math.sin(a)*R];});
  const svg=`<svg class="xstage g4-magnet" id="xs" viewBox="0 0 ${W} ${H}" data-bubble="78" role="img" aria-label="${naEsc(VOICE("المغناطيس"))}">${DEFS}
    <circle class="g4-field" cx="${C[0]}" cy="${C[1]}" r="${(Z*0.9).toFixed(1)}"/><circle class="g4-field g4-f2" cx="${C[0]}" cy="${C[1]}" r="${(Z*1.25).toFixed(1)}"/>
    <g id="g4Arr"></g>${s.items.map((b,i)=>node(b.id,at[i][0],at[i][1],IZ,"happy","g4-it").replace('class="xnode','data-i="'+i+'" class="xnode')).join("")}
    <g class="g4-mag" id="g4Mag" transform="translate(${C[0]} ${C[1]})" tabindex="0" role="button" aria-label="${naEsc(exName(s.target))}">${node(s.target,0,0,Z,"happy","star g4-x")}<text class="g4-magicon" x="${Z*0.42}" y="${-Z*0.36}" text-anchor="middle">🧲</text></g></svg>
    <p class="g4-count" id="g4Count" aria-live="polite">0 ${VOICE("من")} ${s.items.filter(b=>b.ok).length}</p>`;
  return {svg,wire:root=>{const need=s.items.filter(b=>b.ok).length;let got=0,busy=false;const done=new Set(),mag=root.querySelector("#g4Mag");
      gxStart(root,{kind:"magnet",target:s.target,total:need,goal:`اجذب بـ${g4Q(s.target)} كل اللي ${g4V(s.target,"بيحتاجوه","بيحتاجوها")}`});
      const dock=k=>{const a=Math.PI*(v?0.2+0.6*k/Math.max(1,need-1||1):0.75+0.5*k/Math.max(1,need-1||1));return [C[0]+Math.cos(a)*Z*0.98*(v?1:1),C[1]+Math.sin(a)*Z*0.98*(v?1:-1)];};
      const feel=(i)=>{if(done.has(i))return;const b=s.items[i],el=root.querySelector(`.g4-it[data-i="${i}"]`);done.add(i);
        if(b.ok){const q=dock(got++),p=at[i];sfx("connect",{n:got});cap(b.say);mood(root,b.id,"laugh");gxGood(root);
          g4Tween(root,520,t=>{const e=t*t;g4Move(el,p[0]+(q[0]-p[0])*e,p[1]+(q[1]-p[1])*e,1-0.25*e,0);},()=>{el.classList.add("g4-in");sfx("good");
            g4Arrow(root.querySelector("#g4Arr"),q,C,IZ*0.38+4,Z/2+6);document.getElementById("g4Count").textContent=`${got} ${VOICE("من")} ${need}`;
            if(got===need){cap(s.win);setTimeout(()=>{if(root.isConnected)sfx("tada");},250);if(!grown())sparkles();mood(root,s.target,"laugh");gxWin(root);}});}
        else{sfx("nope");cap(b.say);el.classList.add("g4-no");gxBad(root);const p=at[i];g4Tween(root,420,t=>g4Move(el,p[0]+Math.sin(t*20)*5*(1-t),p[1],1,0));}};
      const near=(x,y)=>at.map((p,i)=>[i,Math.hypot(p[0]-x,p[1]-y)]).filter(([i,d])=>!done.has(i)&&d<(v?96:110)).map(([i])=>i);
      /* drag the magnet: anyone it comes close to «feels» it; let go → it slides home */
      let drag=null;
      mag.addEventListener("pointerdown",e=>{if(busy)return;e.preventDefault();naTake(root);mag.setPointerCapture&&mag.setPointerCapture(e.pointerId);const p=g4Pt(root,e);drag={dx:p.x-C[0],dy:p.y-C[1]};mag.classList.add("g4-held");});
      mag.addEventListener("pointermove",e=>{if(!drag)return;const p=g4Pt(root,e),x=Math.max(30,Math.min(W-30,p.x-drag.dx)),y=Math.max(30,Math.min(H-30,p.y-drag.dy));g4Move(mag,x,y,1,0);near(x,y).forEach(feel);});
      const home=()=>{const p=g4Pos(mag);g4Tween(root,380,t=>{const e=g4Ease(t);g4Move(mag,p[0]+(C[0]-p[0])*e,p[1]+(C[1]-p[1])*e,1,0);},()=>{busy=false;});};
      const up=()=>{if(!drag)return;drag=null;mag.classList.remove("g4-held");busy=true;home();};
      mag.addEventListener("pointerup",up);mag.addEventListener("pointercancel",up);
      /* tap someone → the magnet goes to it and back */
      const visit=i=>{if(busy||done.has(i))return;busy=true;naTake(root);const p=at[i],q=[C[0]+(p[0]-C[0])*0.55,C[1]+(p[1]-C[1])*0.55];
        g4Tween(root,420,t=>{const e=g4Ease(t);g4Move(mag,C[0]+(q[0]-C[0])*e,C[1]+(q[1]-C[1])*e,1,0);},()=>{feel(i);setTimeout(()=>{if(root.isConnected)home();},380);});};
      root.querySelectorAll(".g4-it").forEach(el=>{el.addEventListener("click",()=>visit(+el.dataset.i));el.addEventListener("keydown",e=>{if(e.key==="Enter"||e.key===" "){e.preventDefault();visit(+el.dataset.i);}});});}};}

/* ---------------------------------------------------------------- ⚙️ MACHINE
   A row of gears: … → a → [ ? ] → o → … The machine is stuck. The right gear (the concept) fits, and every gear turns; a wrong one clunks out. */
function g4Gear(r,teeth){let d="";for(let i=0;i<teeth*2;i++){const a=Math.PI*i/teeth,rr=i%2?r:r+7,a2=Math.PI*(i+1)/teeth;
    d+=(i?"L":"M")+(Math.cos(a)*rr).toFixed(1)+" "+(Math.sin(a)*rr).toFixed(1)+" L"+(Math.cos(a2)*rr).toFixed(1)+" "+(Math.sin(a2)*rr).toFixed(1)+" ";}return d+"Z";}
function sceneMachine(s){const v=V(),n=s.route.length,W=v?380:640,R=v?(n>4?30:34):(n>4?44:50),GZ=R*1.25;
  const half=id=>Math.max(R+12,[...String(exName(id))].length*3.7+10);   /* a long name at either end stays inside the picture («الحمض النووي (DNA)») */
  const m0=half(s.route[0]),m1=half(s.route[n-1]),step=v?0:(W-m0-m1)/(n-1);const pos=s.route.map((_,i)=>v?[i%2?W*0.66:W*0.34,70+i*(R*2+30)]:[W-m0-i*step,128+(i%2?28:-14)]);
  const H=v?Math.max(...pos.map(p=>p[1]))+R+150:340;const OZ=v?56:62;const opts=s.options;
  const oPos=opts.map((_,i)=>[W*(i+0.5)/opts.length,H-(v?62:58)]);
  const svg=`<svg class="xstage g4-machine" id="xs" viewBox="0 0 ${W} ${H}" data-bubble="78" role="img" aria-label="${naEsc(VOICE("الآلة الخربانة"))}">${DEFS}
    <path class="g4-belt" d="M${pos.map(p=>p.join(" ")).join(" L")}"/><g id="g4Arr"></g>
    ${s.route.map((id,i)=>`<g class="g4-gear${i===s.gap?" g4-gap":""}" data-i="${i}" transform="translate(${pos[i][0]} ${pos[i][1]})"><g class="g4-teeth"><path d="${g4Gear(R,9)}"/><circle r="${(R*0.32).toFixed(1)}" class="g4-hub"/></g>
      ${i===s.gap?`<circle class="g4-hole" r="${(R*0.95).toFixed(1)}"/><text class="g4-qm" y="10" text-anchor="middle">؟</text>`:node(id,0,0,GZ,"sad","g4-gnode").replace(`class="xname" y="${GZ/2+18}"`,`class="xname" y="${(R+26).toFixed(1)}"`)}</g>`).join("")}
    <g id="g4Opts">${opts.map((o,i)=>node(o.id,oPos[i][0],oPos[i][1],OZ,"happy","g4-opt").replace('class="xnode','data-i="'+i+'" class="xnode')).join("")}</g></svg>`;
  return {svg,wire:root=>{let won=false,busy=false,spin=0,raf=0;const tried=new Set();
      gxStart(root,{kind:"machine",target:s.target,total:1,goal:"صلّح الآلة: لاقي السن الناقص ⚙️"});
      /* the stuck machine shows its links that already work (the ones not touching the hole) */
      const link=(i,cls)=>g4Arrow(root.querySelector("#g4Arr"),pos[i+1],pos[i],R+6,R+8,cls);
      for(let i=0;i<n-1;i++)if(i!==s.gap&&i+1!==s.gap)link(i);
      const turn=()=>{if(!root.isConnected)return;spin+=reduce?0:1.6;root.querySelectorAll(".g4-gear .g4-teeth").forEach((g,i)=>g.setAttribute("transform",`rotate(${(i%2?-spin:spin).toFixed(1)})`));raf=requestAnimationFrame(turn);};
      const pick=i=>{const o=opts[i],el=root.querySelector(`.g4-opt[data-i="${i}"]`);if(won||busy||tried.has(i))return;busy=true;naTake(root);
        const p0=oPos[i],p1=pos[s.gap];sfx("pick");el.parentNode.appendChild(el);
        g4Tween(root,520,t=>{const e=g4Ease(t);g4Move(el,p0[0]+(p1[0]-p0[0])*e,p0[1]+(p1[1]-p0[1])*e-60*4*t*(1-t),1+(GZ/OZ-1)*e,0);},()=>{
          if(o.ok){won=true;el.classList.add("g4-fit");root.querySelector(".g4-gap").classList.add("g4-filled");sfx("good");cap(o.say);gxGood(root);
            if(s.gap>0)link(s.gap-1);if(s.gap<n-1)link(s.gap);
            root.querySelectorAll(".g4-gnode").forEach(g=>mood(root,g.dataset.id,"laugh"));mood(root,o.id,"laugh");root.classList.add("g4-run");turn();
            setTimeout(()=>{if(!root.isConnected)return;cap(s.win);sfx("tada");if(!grown())sparkles();gxWin(root);},1600);}
          else{tried.add(i);sfx("nope");cap(o.say);el.classList.add("g4-no");gxBad(root);
            g4Tween(root,560,t=>{const x=p1[0]+(p0[0]-p1[0])*t+Math.sin(t*16)*6*(1-t),y=p1[1]+(p0[1]-p1[1])*t-50*4*t*(1-t);g4Move(el,x,y,GZ/OZ+(1-GZ/OZ)*t,0);},()=>{busy=false;});}});};
      root.querySelectorAll(".g4-opt").forEach(el=>{el.addEventListener("click",()=>pick(+el.dataset.i));el.addEventListener("keydown",e=>{if(e.key==="Enter"||e.key===" "){e.preventDefault();pick(+el.dataset.i);}});});}};}

/* ---------------------------------------------------------------- ⚡ POWER
   Bulbs joined by wires (the «needs» of the graph). The sources have switches. A bulb lights only when EVERYTHING it needs is lit.
   Goal: light «X». One switch is a decoy: it lights itself, and helps nobody. */
function scenePower(s){const v=V(),W=v?380:640,Z=v?58:66,TZ=v?78:90;
  const ins=x=>s.edges.filter(e=>e[1]===x).map(e=>e[0]);const lv={};const L=x=>lv[x]!==undefined?lv[x]:(lv[x]=ins(x).length?1+Math.max(...ins(x).map(L)):0);s.nodes.forEach(L);
  const cols=[...new Set(s.nodes.map(x=>lv[x]))].sort((a,b)=>a-b),maxPer=Math.max(...cols.map(c=>s.nodes.filter(x=>lv[x]===c).length));
  const H=v?90+cols.length*(Z+70)+20:Math.max(300,80+maxPer*(Z+56));const pos={};
  cols.forEach((c,ci)=>{const g=s.nodes.filter(x=>lv[x]===c);g.forEach((id,j)=>{pos[id]=v?[W*(j+0.5)/g.length,70+ci*(Z+70)]:[W-80-ci*((W-160)/Math.max(1,cols.length-1)),(H-30)*(j+0.5)/g.length+10];});});
  const svg=`<svg class="xstage g4-power" id="xs" viewBox="0 0 ${W} ${H}" data-bubble="78" role="img" aria-label="${naEsc(VOICE("وصّل الطاقة"))}">
    <rect class="g36-night" width="${W}" height="${H}" rx="14"/>${Array.from({length:9},(_,i)=>`<circle class="g36-nstar" cx="${((i*97)%100)/100*W}" cy="${12+((i*53)%40)/100*H}" r="${1.4+(i%3)*0.6}" style="animation-delay:${(i*0.37).toFixed(2)}s"/>`).join("")}
    ${s.edges.map(([a,b])=>{const [p,q]=edgeEnds(pos[a],pos[b],(a===s.target?TZ:Z)/2+4);return `<path class="g4-wire" data-a="${a}" data-b="${b}" d="${curve(p,q,v?0:14)}"/>`;}).join("")}
    ${s.nodes.map(id=>`<circle class="g4-halo" data-id="${id}" cx="${pos[id][0]}" cy="${pos[id][1]}" r="${((id===s.target?TZ:Z)*0.62).toFixed(1)}"/>`).join("")}
    ${s.nodes.map(id=>node(id,pos[id][0],pos[id][1],id===s.target?TZ:Z,"sad",(id===s.target?"star ":"")+"g4-bulb sleep")).join("")}</svg>
    <div class="g4-sws" role="group" aria-label="${naEsc(VOICE("المفاتيح"))}">${s.sources.map(id=>`<button class="g4-sw" data-id="${id}" aria-pressed="false"><span class="g4-led" aria-hidden="true"></span>🔌 ${naEsc(exName(id))}</button>`).join("")}</div>`;
  return {svg,wire:root=>{const on=new Set();let lit=new Set(),won=false;const counted=new Set();
      gxStart(root,{kind:"power",target:s.target,total:s.sources.filter(x=>x!==s.decoy).length,goal:`ضوّي ${g4Q(s.target)} وطلّع النهار ☀️`});   /* 🆕 batch 36: it starts at NIGHT; lighting it brings the day */
      const order=s.nodes.slice().sort((a,b)=>lv[a]-lv[b]);
      const update=(changed)=>{const now=new Set();order.forEach(x=>{const need=ins(x);if(s.sources.includes(x)?on.has(x):need.length&&need.every(a=>now.has(a)))now.add(x);});
        const fresh=order.filter(x=>now.has(x)&&!lit.has(x));lit=now;
        s.nodes.forEach(x=>{const nd=root.querySelector(`.g4-bulb[data-id="${x}"]`),h=root.querySelector(`.g4-halo[data-id="${x}"]`);const y=lit.has(x);
          nd.classList.toggle("sleep",!y);nd.classList.toggle("g4-lit",y);h.classList.toggle("g4-on",y);mood(root,x,y?"laugh":"sad");});
        root.querySelectorAll(".g4-wire").forEach(w=>w.classList.toggle("g4-live",lit.has(w.dataset.a)));
        fresh.forEach((x,k)=>setTimeout(()=>{if(root.isConnected)sfx("on",{n:k});},k*160));
        const last=fresh[fresh.length-1];
        if(lit.has(s.target)&&!won){won=true;cap(s.says[s.target]);root.classList.add("g36-day");setTimeout(()=>{if(!root.isConnected)return;sfx("tada");cap(s.win);gxWin(root);},fresh.length*160+1500);if(!grown())sparkles();return;}   /* first WHY it lit, then the win */
        if(!lit.has(s.target))won=false;
        if(changed===s.decoy&&on.has(s.decoy))cap(s.says[s.decoy]);
        else if(last)cap(s.says[last]);
        else if(!on.has(changed))cap(`⛔ ${VOICE("طفّيت")} ${g4Q(changed)}… ${VOICE("واللي بيحتاجوه طفوا كمان.")}`);};
      document.querySelectorAll(".g4-sw").forEach(b=>b.addEventListener("click",()=>{naTake(root);const id=b.dataset.id,val=!on.has(id);if(val)on.add(id);else on.delete(id);
        b.setAttribute("aria-pressed",String(val));if(!val)sfx("off",{n:0});
        if(val&&!counted.has(id)){counted.add(id);if(id===s.decoy){gxBad(root);gxReact(root,id,false);}else gxGood(root);}update(id);}));}};}

SCENES.throw=sceneThrow;SNAME.throw="🪃 ارمي وطيّر";SCENES.tower=sceneTower;SNAME.tower="🏗️ ابني البرج";SCENES.magnet=sceneMagnet;SNAME.magnet="🧲 المغناطيس";
SCENES.machine=sceneMachine;SNAME.machine="⚙️ الآلة الخربانة";SCENES.power=scenePower;SNAME.power="⚡ وصّل الطاقة";
