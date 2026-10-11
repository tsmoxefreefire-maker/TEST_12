/* ===== 🆕 batch 35 (Hareth: «حسّن لي الجرافيك… الشخصيات») · the characters get little ARMS (the younger stages) =====
   Every drawing (made by hand, a subject one or a Lego one) gets two small arms with round white gloves, BEHIND the body:
   they are placed from the drawing's real outline (measured on the screen), so they fit a flower, a stem or a cloud alike.
   Not on the game tokens you throw or drag (CH_TOKEN). 🆕 batch 36: they start at the body's REAL edge at shoulder height (chars36.js measures the outline). They wave hello now and then, wave when you point at the character (kids) and move when it talks. The older stages keep it serious: no arms.
   Rules: «ch-arm» classes · drawn first (behind the body) · still with the light quality and «reduce motion». */
const CH_INK="#3b2a1e";
const CH_TOKEN=".g4-mini,.g4-ball,.g4-it,.g4-opt,.piece,.na-ing";   /* things you throw / drag / pick: a token, not a character → no arms (they would wobble in your hand) */
function armsInto(root){if(!root||grown())return;
  root.querySelectorAll(".xnode .xbody>svg.ch").forEach((sv,i)=>{if(sv.querySelector(".ch-arms"))return;
    const nd=sv.closest(".xnode");if(!nd||nd.matches(CH_TOKEN))return;
    const box=sv.getBoundingClientRect();if(box.width<44||box.height<44)return;                      /* too small for arms (a brick, a tiny icon) */
    let L=Infinity,T=Infinity,R=-Infinity,B=-Infinity;
    [...sv.children].forEach(c=>{if(c.classList&&(c.classList.contains("sface")||c.tagName==="defs"))return;const r=c.getBoundingClientRect();
      if(r.width&&r.height){L=Math.min(L,r.left);T=Math.min(T,r.top);R=Math.max(R,r.right);B=Math.max(B,r.bottom);}});
    if(!isFinite(L))return;
    const k=100/box.width,bx=(L-box.left)*k,by=(T-box.top)*k,bw=(R-L)*k,bh=(B-T)*k;            /* the drawing's outline, in its own 0…100 units */
    if(bw<20||bh<20)return;
    let sy=by+bh*0.6,lx=bx+bw*0.14,rx=bx+bw*0.86;const reach=Math.max(11,Math.min(17,bw*0.22));
    const e=typeof c36Edges==="function"?c36Edges(sv):null;if(e&&e.sh){sy=e.sh.y;lx=e.sh.l+2.5;rx=e.sh.r-2.5;}   /* 🆕 batch 36: from the body's real edge (a leaf, a drop…), not its box */
    const arm=(side,x)=>{const d=side==="l"?-1:1,hx=x+d*reach,hy=sy+reach*0.55;
      return `<g class="ch-arm ${side}" style="transform-origin:${x.toFixed(1)}px ${sy.toFixed(1)}px;animation-delay:-${((i*1.37+(side==="r"?0:0.6))%9).toFixed(2)}s">
        <path d="M${x.toFixed(1)} ${sy.toFixed(1)} Q${(x+d*reach*0.55).toFixed(1)} ${(sy-2).toFixed(1)} ${hx.toFixed(1)} ${hy.toFixed(1)}" fill="none" stroke="${CH_INK}" stroke-width="4.6" stroke-linecap="round"/>
        <circle cx="${hx.toFixed(1)}" cy="${hy.toFixed(1)}" r="5.2" fill="#fff" stroke="${CH_INK}" stroke-width="2"/></g>`;};
    const g=document.createElementNS("http://www.w3.org/2000/svg","g");g.setAttribute("class","ch-arms");g.innerHTML=arm("l",lx)+arm("r",rx);
    sv.insertBefore(g,sv.firstChild);});}
