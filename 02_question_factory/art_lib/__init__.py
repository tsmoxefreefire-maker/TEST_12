"""🆕 batch 40 · the family files of the growing library of drawings (art_library.py reads them).
Each family file has:  F = its short name ·  D = {name: {words, body, face, anim, only?, never?}} ·  ALIASES = {concept name: drawing key}.
Every drawing: a 100×100 box, our outline «{OL}», our colours, and OUR face (the page adds it at face = (x, y, size)), so it moves,
blinks and changes mood like every character. The little helpers below keep one style for the cards and the people."""

INK = "#3b2a1a"


def card(text, fill="#FFD25A", size=34, ty=47, ink=INK, font="sans-serif", ltr=False):
    """A card with a symbol on it (letters, marks, digits, signs): one drawing serves many concepts of language and maths."""
    return (f'<rect x="14" y="8" width="72" height="84" rx="14" fill="{fill}" {{OL}}/>'
            f'<rect x="22" y="15" width="56" height="44" rx="9" fill="#fff" opacity=".85"/>'
            f'<text x="50" y="{ty}" text-anchor="middle" font-size="{size}" font-weight="800" fill="{ink}" font-family="{font}"'
            f'{' direction="ltr" unicode-bidi="embed"' if ltr else ''}{fit(text)}>{text}</text>')   # English / code: left to right («-ing», not «ing-»)


def fit(text):
    """A long symbol is squeezed into the card's window (never spills out)."""
    n = len(text.replace("&gt;", ">").replace("&lt;", "<").replace(" ", "")) + sum(text.count(a) for a in "↔→←⇌")   # 🆕 batch 41: an arrow is as wide as two letters («A↔B» spilled out)
    return ' textLength="52" lengthAdjust="spacingAndGlyphs"' if n >= 4 else ""


CARD_FACE = (50, 74, 0.62)


def person(skin="#F2C9A0", shirt="#6CB8FF", extra="", hair="", legs="#4A5568"):
    """A simple person (head + body) for the family, the jobs and the people of the lessons. The face goes on the head (50, 34)."""
    return (f'<path d="M30 96 L32 66 C34 56 66 56 68 66 L70 96Z" fill="{shirt}" {{OL}}/>'
            f'<path d="M38 96 L38 86 M62 96 L62 86" stroke="{legs}" stroke-width="5" stroke-linecap="round"/>'
            f'{hair}<circle cx="50" cy="34" r="20" fill="{skin}" {{OL}}/>{extra}')


PERSON_FACE = (50, 37, 0.62)


def shape(path, fill):
    return f'<path d="{path}" fill="{fill}" {{OL}}/>'
