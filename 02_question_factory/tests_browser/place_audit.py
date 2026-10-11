"""🆕 batch 41 (Hareth: «في أشياء طالعة برّا… الدودة طالعة بالسما والحجر طالع بالسما»): every PLACE and every little WORLD (zone),
drawn at every size the page really uses (a normal scene, a concept's cartoon, the lesson's story · computer and phone · soft and full),
and every piece checked against where it belongs:
  · in the picture (not cut off by the frame);
  · a sky thing (sun, cloud, star, bird…) above the ground;
  · a thing that stands on the ground (tree, rock, camel…) ON the ground, not floating;
  · a thing under the ground (worm, pebble, roots in «under the ground») under the soil, never in the sky;
  · an owl sits ON something (a tree, a shelf), never in the air.
Used by tests_browser/test_batch41.py; alone: python tests_browser/place_audit.py"""
import pathlib

# where the page draws a place: (W, H, floor or None = a normal scene with the ground at 86%, full?)
SIZES = [(640, 300, None, False), (640, 400, None, False), (380, 250, None, False), (380, 560, None, False),   # behind a normal scene
         (760, 458, 150, True), (760, 720, 150, True), (380, 520, 120, True), (380, 900, 120, True),             # behind a concept's cartoon
         (760, 486, 172, True), (380, 534, 130, True), (380, 900, 130, True)]                                   # behind the lesson's story
SKY = {"cloud", "sun", "star", "planet", "rocket", "raincloud", "x-bird"}
ON_GROUND = {"tree", "pine", "bush", "grass", "rock", "flower", "cactus", "palm", "pyramid", "mushroom", "seaweed", "coral", "light", "car",
             "flag", "column", "obelisk", "bookshelf", "battery", "building", "x-camel", "x-robot", "x-snail", "x-cat", "x-crab", "x-chef", "x-kid", "x-pigeon"}
UNDER = {"worm", "pebble", "roots"}

JS = """([sizes,SKY,ON,UNDER])=>{const A=window.__ART,out=[];const box=document.createElement('div');box.style.cssText='position:absolute;left:0;top:0;opacity:0;pointer-events:none';document.body.appendChild(box);
  for(const name of Object.keys(A.PLACE_NAMES))for(const [W,H,floor,full] of sizes){
    box.innerHTML=`<svg xmlns="http://www.w3.org/2000/svg" width="${W}" height="${H}" viewBox="0 0 ${W} ${H}">${A.placeSVG(name,W,H,{full,floor:floor||undefined})}</svg>`;
    const pl=box.querySelector('.pl'),gy=+pl.dataset.gy,S=Math.max(0.55,Math.min(1.15,Math.min(W,H*1.4)/560));
    const soil=name==='underground'&&full?gy:null;   /* the soil's surface in «under the ground» */
    box.querySelectorAll('.pl-near [data-pl]').forEach(el=>{const t=el.dataset.pl,m=/translate\\(([-\\d.]+)[ ,]+([-\\d.]+)\\)\\s*scale\\(([-\\d.]+)\\)/.exec(el.getAttribute('transform')||'');if(!m)return;
      const x=+m[1],y=+m[2],k=+m[3],inner=el.querySelector('.pl-a')||el;let bb;try{bb=inner.getBBox();}catch(e){return;}
      const L=x+k*bb.x,T=y+k*bb.y,R=L+k*bb.width,B=T+k*bb.height,area=Math.max(1,(R-L)*(B-T));
      const inside=Math.max(0,Math.min(R,W)-Math.max(L,0))*Math.max(0,Math.min(B,H)-Math.max(T,0))/area;
      const where=`${name} ${W}x${H}${floor?' floor '+floor:''} ${full?'full':'soft'} · ${t}`;
      if(inside<0.6&&!el.querySelector('.pl-drive'))out.push(where+` · cut off by the frame (${Math.round(inside*100)}% inside)`);   /* the car / the ball drive ACROSS the picture */
      if(SKY.includes(t)&&B>gy+6)out.push(where+` · a sky thing below the ground (bottom ${B.toFixed(0)} > ground ${gy})`);
      if(ON.includes(t)&&y<gy-12*S)out.push(where+` · floats above the ground (stands at ${y.toFixed(0)}, ground ${gy})`);
      if(t==='x-owl'&&y<gy-12*S&&![...box.querySelectorAll('.pl-near .pl-prop')].some(o=>{const r=o.getBoundingClientRect(),q=box.firstChild.getBoundingClientRect();return Math.abs(r.top-q.top-y)<14&&r.left-q.left<x&&r.right-q.left>x;}))
        out.push(where+` · a bird sitting on nothing (in the air at ${y.toFixed(0)})`);   /* an owl is not a flying bird: it sits ON something */
      if(UNDER.includes(t)&&name==='underground'&&T<gy-14*S)out.push(where+` · under-the-ground thing above the soil (top ${T.toFixed(0)}, soil ${gy})`);});}
  box.remove();return out;}"""


def audit(pg):
    """[problems] for every place × size (an empty list = everything where it belongs)"""
    return pg.evaluate(JS, [SIZES, sorted(SKY), sorted(ON_GROUND), sorted(UNDER)])


if __name__ == "__main__":
    from playwright.sync_api import sync_playwright
    page = pathlib.Path(__file__).resolve().parent.parent / "player" / "explain.html"
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(); pg.route("**/fonts.*/**", lambda r: r.abort()); pg.goto(page.as_uri()); pg.wait_for_timeout(500)
        probs = audit(pg); b.close()
    print("\n".join(probs)); print(f"{len(probs)} problems")
