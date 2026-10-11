"""🆕 Five more GAMES to understand a concept (batch 34, Hareth: «ضيف خمس فعاليات جديدة تكون حلوة»). Everything from the graph only.

  throw    🪃 ارمي وطيّر    fling the right things to «X» (what it needs): it catches them; a wrong one bounces back (💡 Hareth's idea)
  tower    🏗️ ابني البرج     stack the chain: each block can only sit on the one it needs; a wrong block wobbles and falls
  magnet   🧲 المغناطيس      «X» is a magnet: the ones that NEED it are pulled to it and stick; the others do not move
  machine  ⚙️ الآلة الخربانة  a chain machine is missing its gear «X»: find the gear that fits, and the whole machine turns
  power    ⚡ وصّل الطاقة    light «X»: switch on the sources; a light goes on only when ALL it needs is lit

No points and no failing: a wrong move = an explanation. Plain Python, no AI.
Truth rule (like the other scenes): «X needs Y» is said only if the graph has that arrow, «X does NOT need Y» only if Y is not
before X at all (not even through a chain). check() re-checks every scene against the graph."""
import explain_activities as a1
import explain_generator as eg
import offline_generator as og
import variety
import audience as A

N, V = a1.N, a1.V
_ins, _outs, _needs, _rng = a1._ins, a1._outs, a1._needs, a1._rng


def _not_needs(g, x):
    """«ما بيحتاج» / «ما بتحتاج» (the page says «ما بيعتمد على» for the bigger grades)."""
    return "ما " + _needs(g, x)


def _reason(g, needer, needed):
    """«X بيحتاج Y: why.» — the why only when the graph's meaning names it."""
    why = eg._why(g, needed, needer)
    return f"«{N(g, needer)}» {_needs(g, needer)} «{N(g, needed)}»" + (f": {why}." if why else ".")


def _strangers(g, lesson, cid, key, k, also=()):
    """Up to k concepts with NO arrow to «cid» at all (not before it, not after it) — closest ones first (same lesson…)."""
    near = {cid} | g.ancestors(cid) | g.descendants(cid) | set(also)
    return [x for x in og.tiered(g, lesson, _rng(key, cid), exclude=near)][:k]


def _chain_down(g, cid, max_len=5):
    """The longest «needs» chain that ENDS at cid, bottom → top (base … cid). Ties: the graph's order."""
    best = {}
    def down(x, seen):
        if x in best:
            return best[x]
        path = [x]
        for p in _ins(g, x):
            if p in seen:
                continue
            q = down(p, seen | {p}) + [x]
            if len(q) > len(path):
                path = q
        best[x] = path
        return path
    return down(cid, {cid})[-max_len:]


def _chain_up(g, cid, max_len=3):
    """A chain going ON from cid (cid, what needs it, what needs that…)."""
    out, cur = [cid], cid
    while len(out) < max_len:
        nxt = [o for o in _outs(g, cur) if o not in out]
        if not nxt:
            break
        cur = max(nxt, key=lambda o: len(g.descendants(o)))     # the one that leads furthest
        out.append(cur)
    return out


def _by_stage(g, kids, junior, teen, senior):
    return {"kids": kids, "junior": junior, "teen": teen, "senior": senior}[A.stage(g)]


# ---------------------------------------------------------------- 🪃 throw (Hareth's idea: «ماسك اشي وفلتته فبصير يطير»)
def scene_throw(g, lesson, cid, used=None):
    """🪃 Balls with names; fling each one to «X». What X needs: it catches it (arrow + reason). Anything else: it bounces back."""
    ins = _ins(g, cid)[:3]
    if not ins:
        return None
    wrong = _strangers(g, lesson, cid, "throw", 2 if len(ins) < 3 else 1)
    if not wrong:
        return None
    me = N(g, cid)
    balls = [{"id": a, "ok": True, "say": "✅ " + _reason(g, cid, a)} for a in ins]
    balls += [{"id": w, "ok": False, "say": f"↩️ «{me}» {_not_needs(g, cid)} «{N(g, w)}»، فرجعت الكرة."} for w in wrong]
    rng = _rng("throw-order", cid)
    rng.shuffle(balls)
    names = eg._join([N(g, a) for a in ins])
    win = _by_stage(g, f"🎉 وصّلت لـ«{me}» كل اللي {V(me, 'بيحتاجه', 'بتحتاجه')}: {names}!",
                    f"🎉 وصّلت لـ«{me}» كل اللي {V(me, 'بيحتاجه', 'بتحتاجه')}: {names}!",
                    f"✅ كل اللي {V(me, 'بيحتاجه', 'بتحتاجه')} «{me}» وصل: {names}.",
                    f"✅ اكتملت متطلبات «{me}»: {names}.")
    return {"kind": "throw", "target": cid, "balls": balls, "win": win,
            "steps": [f"🪃 ارمي لـ«{me}» اللي {V(me, 'بيحتاجه', 'بتحتاجه')}!",
                      variety.say("throw.how", f"{lesson.id}:{cid}"),
                      f"اللي مش إله، «{me}» {V(me, 'بيرجّعها', 'بترجّعها')}."],
            "paragraph": f"«{me}» {_needs(g, cid)} {names}. "
                         + f"أما {eg._join([N(g, w) for w in wrong])} فما في سهم {V(N(g, wrong[0]), 'بينه', 'بينها') if len(wrong) == 1 else 'بينهم'} وبين «{me}»، فرجعت الكرة."}


# ---------------------------------------------------------------- 🏗️ tower
def scene_tower(g, lesson, cid, used=None):
    """🏗️ Stack the chain that ends at «X»: each block sits only on the one it needs. A wrong block wobbles and falls (and says why)."""
    blocks = _chain_down(g, cid, 5)
    if len(blocks) < 3:
        return None
    me = N(g, cid)
    out = [{"id": blocks[0], "why": f"«{N(g, blocks[0])}» تحت الكل: {V(N(g, blocks[0]), 'هو', 'هي')} الأساس."}]
    for i in range(1, len(blocks)):
        out.append({"id": blocks[i], "why": _reason(g, blocks[i], blocks[i - 1])})
    chain = " ← ".join(f"«{N(g, b)}»" for b in blocks)
    win = _by_stage(g, f"🎉 البرج وقف! {chain}", f"🎉 البرج وقف! {chain}", f"✅ البرج ثابت: {chain}", f"✅ البناء متماسك: {chain}")
    return {"kind": "tower", "target": cid, "blocks": out, "win": win,
            "steps": [f"🏗️ ابني برج «{me}»!",
                      "اكبس على قطعة (أو اسحبها) لتنزل فوق البرج. كل قطعة بتقعد بس فوق اللي بتحتاجه.",
                      "القطعة الغلط بتتهزّ وبتوقع، وبتحكيلك ليش."],
            "paragraph": f"برج «{me}» ما بيوقف إلا هيك: {chain}. كل طابق بيحتاج اللي تحته."}


# ---------------------------------------------------------------- 🧲 magnet
def scene_magnet(g, lesson, cid, used=None):
    """🧲 «X» is a magnet: drag it around; the ones that NEED «X» are pulled to it and stick (arrow + reason); the others stay."""
    outs = _outs(g, cid)[:3]
    if not outs:
        return None
    wrong = _strangers(g, lesson, cid, "magnet", 2 if len(outs) < 3 else 1)
    if not wrong:
        return None
    me = N(g, cid)
    items = [{"id": o, "ok": True, "say": "🧲 " + _reason(g, o, cid)} for o in outs]
    items += [{"id": w, "ok": False, "say": f"😐 «{N(g, w)}» {_not_needs(g, w)} «{me}»، فما {V(N(g, w), 'انشد', 'انشدّت')}."} for w in wrong]
    _rng("magnet-order", cid).shuffle(items)
    names = eg._join([N(g, o) for o in outs])
    win = _by_stage(g, f"🎉 لقطت كل اللي {V(me, 'بيحتاجوه', 'بيحتاجوها')}: {names}!", f"🎉 لقطت كل اللي {V(me, 'بيحتاجوه', 'بيحتاجوها')}: {names}!",
                    f"✅ كل اللي {V(me, 'بيحتاجوه', 'بيحتاجوها')} انشدّوا: {names}.", f"✅ كل اللي {V(me, 'بيعتمدوا عليه', 'بيعتمدوا عليها')} انجذبوا: {names}.")
    return {"kind": "magnet", "target": cid, "items": items, "win": win,
            "steps": [variety.say("magnet.title", f"{lesson.id}:{cid}", eg._she(me), me=me),
                      f"حرّك «{me}» قريب من كل واحد (أو اكبس عليه): اللي {V(me, 'بيحتاجه', 'بيحتاجها')} بينشدّ وبيلزق.",
                      variety.say("magnet.end", f"{lesson.id}:{cid}")],
            "paragraph": (f"{names} بيحتاجوا «{me}»، فانشدّوا {V(me, 'إله', 'إلها')}. " if len(outs) > 1 else
                          f"«{N(g, outs[0])}» {_needs(g, outs[0])} «{me}»، ف{V(N(g, outs[0]), 'انشدّ', 'انشدّت')} {V(me, 'إله', 'إلها')}. ")
                         + f"أما {eg._join([N(g, w) for w in wrong])} فما في سهم {V(N(g, wrong[0]), 'بينه', 'بينها') if len(wrong) == 1 else 'بينهم'} وبين «{me}»."}


# ---------------------------------------------------------------- ⚙️ machine
def scene_machine(g, lesson, cid, used=None):
    """⚙️ A machine of gears in a chain (…→ a → X → o → …) is missing its gear «X». The right gear fits and the whole machine turns."""
    below = _chain_down(g, cid, 3)                         # … a, X
    above = _chain_up(g, cid, 3)                           # X, o, …
    route = below[:-1] + above
    if len(below) < 2 or len(above) < 2 or len(route) < 3:
        return None
    gap = len(below) - 1
    prev, nxt = route[gap - 1], route[gap + 1]
    wrong = [x for x in og.tiered(g, lesson, _rng("machine", cid), exclude=set(route) | g.ancestors(nxt))][:2]   # never one that «nxt» really needs
    if not wrong:
        return None
    me = N(g, cid)
    options = [{"id": cid, "ok": True, "say": "⚙️ " + _reason(g, cid, prev) + " " + _reason(g, nxt, cid)}]
    options += [{"id": w, "ok": False, "say": f"🔩 «{N(g, w)}» مش {V(N(g, w), 'مكانه', 'مكانها')} هون: «{N(g, nxt)}» {_not_needs(g, nxt)} «{N(g, w)}»."} for w in wrong]
    _rng("machine-order", cid).shuffle(options)
    links = [_reason(g, route[i + 1], route[i]) for i in range(len(route) - 1)]
    win = _by_stage(g, "🎉 الآلة اشتغلت! كل سن بيلف التاني.", "🎉 الآلة اشتغلت! كل سن بيلف التاني.", "✅ الآلة اشتغلت: السلسلة كاملة.", "✅ اكتملت السلسلة، والآلة تعمل.")
    return {"kind": "machine", "target": cid, "route": route, "gap": gap, "options": options, "says": links, "win": win,
            "steps": ["⚙️ الآلة خربانة! في سن ناقص.",
                      "اختار السن اللي بيركب بالفراغ (اكبس عليه أو اسحبه).",
                      "السن الصح بيخلّي الآلة كلها تلف."],
            "paragraph": " ".join(links)}


# ---------------------------------------------------------------- ⚡ power
def scene_power(g, lesson, cid, used=None):
    """⚡ Light «X»: the sources have switches; a light goes on only when ALL it needs (in the picture) is lit. One switch is a decoy."""
    anc = [x for x in g.ancestors(cid) if og.is_entity(g, x)]
    if len(anc) < 2:
        return None
    direct = set(_ins(g, cid))
    second = {p for a in direct for p in _ins(g, a)}
    keep = sorted(direct | second, key=lambda x: (g.depth(x), x))[:5]
    if len(keep) < 2:
        return None
    nodes = keep + [cid]
    edges = [[a, b] for a in nodes for b in nodes if a != b and g.is_prereq(a, b)]
    sources = [x for x in nodes if x != cid and not any(e[1] == x for e in edges)]
    decoy = (_strangers(g, lesson, cid, "power", 1, also=nodes) or [None])[0]
    if decoy:
        nodes = [decoy] + nodes
        sources = sources + [decoy]
    if len([s for s in sources if s != decoy]) < 1:
        return None
    me = N(g, cid)
    says = {}
    for x in nodes:
        needs_here = [e[0] for e in edges if e[1] == x]
        if needs_here:
            says[x] = f"💡 «{N(g, x)}» {V(N(g, x), 'ضوّا', 'ضوّت')}، لأنه كل اللي {V(N(g, x), 'بيحتاجه', 'بتحتاجه')} شغّال: {eg._join([N(g, n) for n in needs_here])}."
        else:
            says[x] = f"🔌 شغّلت «{N(g, x)}»."
    if decoy:
        dn = N(g, decoy)
        says[decoy] = f"🔌 «{dn}» {V(dn, 'ضوّا', 'ضوّت')}، بس «{me}» {_not_needs(g, cid)} «{dn}»، فما {V(me, 'استفاد', 'استفادت')} {V(dn, 'منه', 'منها')}."
    win = _by_stage(g, f"🎉 {V(me, 'ضوّا', 'ضوّت')} «{me}»!", f"🎉 {V(me, 'ضوّا', 'ضوّت')} «{me}»!", f"✅ {V(me, 'ضوّا', 'ضوّت')} «{me}»: كل اللي {V(me, 'بيحتاجه', 'بتحتاجه')} شغّال.", f"✅ «{me}» تحقّق: كل متطلباته متحققة.")
    return {"kind": "power", "target": cid, "nodes": nodes, "edges": edges, "sources": sources, "decoy": decoy, "says": says, "win": win,
            "steps": [variety.say("power.title", f"{lesson.id}:{cid}", eg._she(me), me=me),
                      "شغّل المفاتيح. الضو بيمشي بالأسهم، وكل لمبة بتضوي بس لما كل اللي بتحتاجه يضوي.",
                      variety.say("power.end", f"{lesson.id}:{cid}")],
            "paragraph": f"«{me}» {_needs(g, cid)} {eg._join([N(g, e[0]) for e in edges if e[1] == cid])}"
                         + ((("، وهدول بدورهم بيحتاجوا اللي قبلهم" if len(direct & set(nodes)) > 1 else
                              V(N(g, next(iter(direct & set(nodes)))), "، وهو بدوره بيحتاج اللي قبله", "، وهي بدورها بتحتاج اللي قبلها")))
                            if len(edges) > len([e for e in edges if e[1] == cid]) else "")
                         + ". الضو ما بيوصل إلا لما يكون كل إشي قبله شغّال."}


MAKERS = [scene_throw, scene_tower, scene_magnet, scene_machine, scene_power]
KINDS = ("throw", "tower", "magnet", "machine", "power")


def pick(g, lesson, cid, i, used):
    """ONE of the five games per concept, a different one for each concept (each lesson starts somewhere else);
    the next one when the graph has not enough for it."""
    ids = [l.id for l in g.lessons()]
    start = (i + 3 * (ids.index(lesson.id) if lesson.id in ids else 0)) % len(MAKERS)
    for maker in MAKERS[start:] + MAKERS[:start]:
        s = maker(g, lesson, cid, used)
        if s:
            return s
    return None


def check(g, s) -> list:
    """The picture must never teach something wrong."""
    k, t, errors = s["kind"], s.get("target"), []
    if k in ("throw", "magnet"):
        for b in s["balls" if k == "throw" else "items"]:
            x = b["id"]
            if k == "throw":
                ok = g.is_prereq(x, t) if b["ok"] else (x not in g.ancestors(t) and x != t)
            else:
                ok = g.is_prereq(t, x) if b["ok"] else (x not in g.descendants(t) and x != t)
            if not ok:
                errors.append(f"{k}: {x} ({'ok' if b['ok'] else 'wrong'}) is not true")
    elif k == "tower":
        ids = [b["id"] for b in s["blocks"]]
        errors += [f"tower: {ids[i]} → {ids[i + 1]} is not a link" for i in range(len(ids) - 1) if not g.is_prereq(ids[i], ids[i + 1])]
        if not ids or ids[-1] != t:
            errors.append("tower: the top is not the concept")
    elif k == "machine":
        r = s["route"]
        errors += [f"machine: {r[i]} → {r[i + 1]} is not a link" for i in range(len(r) - 1) if not g.is_prereq(r[i], r[i + 1])]
        if r[s["gap"]] != t:
            errors.append("machine: the gap is not the concept")
        for o in s["options"]:
            if o["ok"] != (o["id"] == t):
                errors.append(f"machine: option {o['id']} marked wrong way")
            nxt = r[s["gap"] + 1] if s["gap"] + 1 < len(r) else None
            if not o["ok"] and nxt and o["id"] in g.ancestors(nxt):
                errors.append(f"machine: {nxt} really needs {o['id']}")
    elif k == "power":
        errors += [f"power: {a} → {b} is not a link" for a, b in s["edges"] if not g.is_prereq(a, b)]
        if s.get("decoy") and s["decoy"] in g.ancestors(t):
            errors.append("power: the decoy is needed")
        if t not in s["nodes"]:
            errors.append("power: the concept is not in the picture")
    ids = [b["id"] for b in s.get("balls", []) + s.get("items", []) + s.get("blocks", []) + s.get("options", [])] + s.get("route", []) + s.get("nodes", [])
    errors += [f"{k}: unknown concept {x}" for x in ids if x not in g.concepts or not og.is_entity(g, x)]
    return errors
