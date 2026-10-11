/* ================================================================ 🔊 batch 44 · THE VOICE THAT READS THE EXPLANATION
   Hareth: «لما الكلام يمشي هو يحكي… لما يبطأ الشرح هو كمان بده يشرح». When the page comes from OUR server (/explain…) and the server
   has a voice (GET /tts/status → on), every line is read aloud: the narrator's line under the scene, and the story's subtitles.
   · the line WAITS for the voice: the next line (and the story's next moment) comes only when the voice has finished, then a short pause;
   · no voice (the published page, no key, the sound blocked, an error) → the page reads at its own speed, exactly as before;
   · «🔊 الصوت» in the controls: on / off (remembered on this device). The browser lets sound start only after a first tap: until then
     the button says «🔊 اكبس لتسمع».
   Rules: «tts-» classes · one voice at a time (a new line stops the old one) · every wait checks that the scene is still the same. */
const TTS={on:false,muted:false,blocked:false,a:null,seq:0,ready:null};
function ttsInit(){if(TTS.ready)return TTS.ready;
  try{TTS.muted=localStorage.getItem("ie_tts_muted")==="1";}catch(e){}
  const ours=/^https?:$/.test(location.protocol)&&/^\/explain(\/|$)/.test(location.pathname);   /* only our server has /tts */
  TTS.ready=!ours?Promise.resolve(false):fetch("/tts/status").then(r=>r.ok?r.json():null).then(j=>{TTS.on=!!(j&&j.on);ttsButton();
      if(ttsOn()&&typeof VIDEO!=="undefined"&&VIDEO&&STEP===0){try{renderScene();}catch(e){}}   /* the voice arrived after the first line: start it again, now spoken */
      return TTS.on;}).catch(()=>false);
  return TTS.ready;}
const ttsOn=()=>TTS.on&&!TTS.muted;
function ttsStop(){TTS.seq++;const a=TTS.a;TTS.a=null;if(a){try{a.pause();a.removeAttribute("src");a.load();}catch(e){}if(a.__fin)a.__fin(false);}}
/* read one line: resolves true when the voice has finished, false when there was no voice (the caller then waits its usual time) */
function ttsSay(text){const t=String(text||"").trim();if(!ttsOn()||!t)return Promise.resolve(false);
  ttsStop();const my=TTS.seq;
  return new Promise(res=>{const a=new Audio(`/tts?stage=${encodeURIComponent(stageNow())}&text=${encodeURIComponent(t)}`);TTS.a=a;let done=false;
    const fin=ok=>{if(done)return;done=true;clearTimeout(guard);if(TTS.a===a)TTS.a=null;res(ok&&my===TTS.seq);};a.__fin=fin;
    const guard=setTimeout(()=>fin(true),45000);                                     /* never stuck: a very long or lost clip */
    a.addEventListener("ended",()=>fin(true));a.addEventListener("error",()=>fin(false));
    const p=a.play();if(p&&p.catch)p.catch(err=>{if(err&&err.name==="NotAllowedError"){TTS.blocked=true;ttsButton();}fin(false);});
    if(p&&p.then)p.then(()=>{if(TTS.blocked){TTS.blocked=false;ttsButton();}});});}
/* the button in the narrator's controls */
function ttsButton(){const ctl=document.querySelector("#q .nctl");if(!ctl||!TTS.on)return;let b=document.getElementById("ttsb");
  if(!b){b=document.createElement("button");b.type="button";b.id="ttsb";b.className="chipbtn tts-b";ctl.insertBefore(b,ctl.firstChild);
    b.addEventListener("click",()=>{if(TTS.blocked){TTS.blocked=false;TTS.muted=false;}else{TTS.muted=!TTS.muted;if(TTS.muted)ttsStop();}
      try{localStorage.setItem("ie_tts_muted",TTS.muted?"1":"0");}catch(e){}ttsButton();sfx("pop");});}
  b.textContent=TTS.muted?"🔇 "+VOICE("الصوت"):TTS.blocked?"🔊 "+VOICE("اكبس لتسمع"):"🔊 "+VOICE("الصوت");
  b.setAttribute("aria-pressed",String(!TTS.muted));b.classList.toggle("tts-wait",TTS.blocked&&!TTS.muted);}
ttsInit();
