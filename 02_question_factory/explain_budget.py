"""🆕 batch 35 (Hareth: «لما تروح مفهوم بتعطيه فعاليات كثير فبتضل تعيد المعلومة كثير… بدها تتعدل»). Measured before: the same «X needs Y»
was said in 5.4 of the ~6 scenes of a concept.

THE FACT BUDGET — every scene is a list of FACTS (one «needs» arrow, one piece of a meaning, one comparison, one process…):
  · the cartoon («تعرّف عليّ») teaches first: the meaning + what it needs + who needs it;
  · ONE practice (an activity or a game) may say those facts a SECOND time (learn → practise) — never a third;
  · any other scene must bring something NEW: at least half of its facts never said before in this concept
    (chains are also counted for the whole lesson, so the same chain is not walked again for the next concept);
  · at most 4 scenes per concept (+ a film / a slider: they show something no other scene shows).
No AI: plain Python, from the scenes' own data."""
import offline_generator as og

CHAINS = {"journey", "ladder", "tower", "machine", "power", "what_if"}     # scenes that walk a chain (counted for the lesson too)
PRACTICE = {"recipe", "connect", "compare", "teach", "ladder", "throw", "tower", "magnet", "machine", "power"}
UNIQUE = {"play", "slider"}                                                # they show a process / a rule: never a repeat
RECALL = {"who_am_i", "sentence"}                                          # 🆕 batch 43: the student finds / builds the meaning again (a second time, never a third)
MAX_SCENES = 4


def _pieces(g, x):
    d = g.concepts[x].description if x in g.concepts else ""
    return [p.strip(" .") for p in (og.fragments(d) or ([d] if d else [])) if p.strip(" .")]


def _ins(g, x):
    return [p for p in g.prereq_in.get(x, []) if og.is_entity(g, p)]


def _outs(g, x):
    return [n for n in g.prereq_out.get(x, []) if og.is_entity(g, n)]


def _edges_in_text(g, t, text):
    """«…» names in a sentence → the arrows they stand for (around the concept t)."""
    out = set()
    for y in _ins(g, t):
        if f"«{g.concepts[y].text}»" in text:
            out.add(("e", y, t))
    for y in _outs(g, t):
        if f"«{g.concepts[y].text}»" in text:
            out.add(("e", t, y))
    return out


def facts(g, s) -> set:
    """What a scene SAYS, as a set of facts: ("e", a, b) = «b needs a» · ("f", x, piece) = a piece of x's meaning ·
    ("s", a, b) = a and b compared · ("p", x, verb) = a process (film) · ("r", x) = a rule (slider) · ("b", a, b) = a becomes b."""
    k, t = s["kind"], s.get("target")
    ins = {("e", a, t) for a in _ins(g, t)} if t else set()
    outs = {("e", t, o) for o in _outs(g, t)} if t else set()
    order = [("f", t, p) for p in _pieces(g, t)] if t else []          # in the meaning's own order (the cartoon shows the first three)
    mean = set(order)
    if k == "meet":
        return {("e", a, t) for a in s.get("ins", [])} | {("e", t, o) for o in s.get("outs", [])} | set(order[:3])
    if k == "interview":
        return mean | ins | outs
    if k == "flip":
        return set(order[:2]) | ins | outs
    if k == "lens":
        out = set()
        for f in s.get("facts", []):
            e = _edges_in_text(g, t, f)
            out |= e or {("f", t, f.strip(" ."))}
        return out
    if k == "dialogue":
        return {("e", s["with"], t)} | set(order[:1])
    if k == "recipe":
        return {("e", n["id"], t) for n in s["needs"]}
    if k == "connect":
        return {("e", l["to"], l["from"]) for l in s["links"] if l["required"]}
    if k == "compare":
        return {("s", t, s["other"])} | {("f", f["ref"], f["fact"]) for f in s["facts"] if f["type"] == "def"}
    if k == "teach":
        out = set()
        for r in s["rounds"]:
            for op in r["options"]:
                if op["ok"]:
                    out.add(("f", t, op["opt"]) if r["rel"] == "def" else ("e", op["id"], t) if r["rel"] == "needs" else ("e", t, op["id"]))
        return out
    if k == "ladder":
        ids = [t] + [r["id"] for r in s["rungs"]]
        return {("e", ids[i + 1], ids[i]) if s["mode"] == "why" else ("e", ids[i], ids[i + 1]) for i in range(len(ids) - 1)}
    if k in ("journey", "machine"):
        r = s["route"]
        return {("e", r[i], r[i + 1]) for i in range(len(r) - 1)}
    if k == "what_if":
        return {("e", a, b) for a, b in s.get("edges", [])} or {("e", t, x) for x in s.get("affected", [])}
    if k == "before_after":
        return {("b", s["before"], t)} if s.get("mode") == "becomes" else {("e", s["before"], t)}
    if k == "throw":
        return {("e", b["id"], t) for b in s["balls"] if b["ok"]}
    if k == "magnet":
        return {("e", t, b["id"]) for b in s["items"] if b["ok"]}
    if k == "tower":
        ids = [b["id"] for b in s["blocks"]]
        return {("e", ids[i], ids[i + 1]) for i in range(len(ids) - 1)}
    if k == "power":
        return {("e", a, b) for a, b in s["edges"]}
    if k == "play":
        return {("p", t, s.get("verb", ""))}
    if k == "slider":
        return {("r", t)}
    if k == "who_am_i":
        return {("f", t, _pieces(g, t)[c["piece"]]) if c["type"] == "def" else ("e", c["ref"], t) if c["type"] == "needs" else ("e", t, c["ref"])
                for c in s.get("clues", []) if c["type"] != "def" or c["piece"] < len(_pieces(g, t))}
    if k == "sentence":
        p = s.get("piece", -1)
        return {("f", t, _pieces(g, t)[p])} if isinstance(p, int) and 0 <= p < len(_pieces(g, t)) else {("f", t, "*")}
    return {("?", k, t)}


class Budget:
    """Counts what was said in ONE concept (and the chains of the whole lesson)."""

    def __init__(self, lesson_chains: dict):
        self.seen = {}                     # fact → how many times it was said in this concept
        self.chains = lesson_chains        # fact → said by a chain scene earlier in this lesson
        self.practised = False

    def _new_ratio(self, f, pool):
        return (sum(1 for x in f if x not in pool) / len(f)) if f else 0

    def ok(self, g, s) -> bool:
        """May this scene come in? (see the rules on top)"""
        if not s:
            return False
        k, f = s["kind"], facts(g, s)
        if k in UNIQUE:
            return True
        if k in RECALL:
            return all(self.seen.get(x, 0) < 2 for x in f)                     # a second time is fine (it is how he remembers it)
        if k in CHAINS and self._new_ratio(f, self.chains) < 0.5:
            return False                                                       # this lesson already walked (most of) this chain
        if k in PRACTICE and not self.practised and all(self.seen.get(x, 0) < 2 for x in f):
            return True                                                        # the one practice: a second time is fine
        if k not in CHAINS and any(self.seen.get(x, 0) >= 2 for x in f):
            return False                                                       # a third time — only a chain may pass a known link on its way
        return self._new_ratio(f, self.seen) >= 0.5                            # anything else: mostly new

    def take(self, g, s):
        f = facts(g, s)
        for x in f:
            self.seen[x] = self.seen.get(x, 0) + 1
        if s["kind"] in CHAINS:
            for x in f:
                self.chains[x] = True
        if s["kind"] in PRACTICE and not self.practised:
            self.practised = True
