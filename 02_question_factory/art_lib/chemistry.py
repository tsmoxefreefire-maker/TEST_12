"""🆕 batch 41 · chemistry (الكيمياء، الثانوي): molecular shapes and bonds, the atom's models and its levels, organic families and big
molecules, heat, solutions and the lab, electricity from reactions, equilibrium — real drawings where there is a thing, and CARDS with
the symbol where the concept IS a symbol (a formula, a functional group, a unit, an equation: «–OH», «C₆H₁₂O₆», «2H₂ + O₂ → 2H₂O»).
For the science subjects only."""
from . import card

F = "chem"
S = ("science",)
CF = (50, 74, 0.62)                                                  # the face on a card (under the symbol)


def at(x, y, r=11, c="#7CC6F2"):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}" {{OL}}/>'


def bond(x1, y1, x2, y2, w=4):
    return f'<path d="M{x1} {y1} L{x2} {y2}" stroke="#3b2a1a" stroke-width="{w}" stroke-linecap="round"/>'


def ltr_card(t, fill):
    return card(t, fill, 26 if len(t) <= 4 else 22, ltr=True)


def periodic(hi):
    """A small periodic table with one block lit (hi = s / p / d / f / rep / hal)."""
    cells = []
    for r in range(7):
        for c in range(18):
            if r == 0 and 0 < c < 17: continue
            if r in (1, 2) and 1 < c < 12: continue
            blk = "s" if c < 2 else "p" if c > 11 else "d"
            lit = (hi == blk) or (hi == "rep" and blk in "sp") or (hi == "hal" and c in (16, 17))
            cells.append(f'<rect x="{6 + c * 4.9:.1f}" y="{14 + r * 7}" width="4.3" height="6.2" rx=".8" fill="{"#F5A623" if lit else "#DCE6F0"}"/>')
    for r in range(2):
        for c in range(14):
            cells.append(f'<rect x="{20.7 + c * 4.9:.1f}" y="{68 + r * 7}" width="4.3" height="6.2" rx=".8" fill="{"#F5A623" if hi == "f" else "#E8DCF5"}"/>')
    return '<rect x="2" y="8" width="96" height="78" rx="8" fill="#fff" {OL}/>' + "".join(cells)


SHAPE_FACE = (50, 52, .3)
D = {
 # ---------- the shapes of molecules ----------
 "linear": dict(words=["الشكل الخطي", "الجزيء الخطي"], only=S, anim="bob", face=SHAPE_FACE,
   body=bond(16, 52, 84, 52, 5) + at(16, 52, 10, "#E2504C") + at(84, 52, 10, "#E2504C") + at(50, 52, 14, "#3b4252")),
 "trigonal": dict(words=["الشكل المثلث المستوي", "المثلث المستوي"], only=S, anim="bob", face=SHAPE_FACE,
   body=bond(50, 52, 50, 14) + bond(50, 52, 17, 71) + bond(50, 52, 83, 71) + at(50, 14, 10, "#F5D547") + at(17, 71, 10, "#F5D547") + at(83, 71, 10, "#F5D547") + at(50, 52, 14, "#7CC6F2")),
 "bent": dict(words=["الشكل المنحني", "الجزيء المنحني"], only=S, anim="bob", face=(50, 46, .3),
   body=bond(50, 46, 22, 74) + bond(50, 46, 78, 74) + at(22, 74, 10, "#fff") + at(78, 74, 10, "#fff") + at(50, 46, 15, "#E2504C")
        + '<circle cx="40" cy="22" r="3" fill="#3b2a1a"/><circle cx="46" cy="18" r="3" fill="#3b2a1a"/><circle cx="54" cy="18" r="3" fill="#3b2a1a"/><circle cx="60" cy="22" r="3" fill="#3b2a1a"/>'),
 "pyramidal": dict(words=["الشكل الهرمي", "الهرم الثلاثي"], only=S, anim="bob", face=(50, 42, .3),
   body=bond(50, 42, 18, 74) + bond(50, 42, 50, 86) + bond(50, 42, 82, 74) + at(18, 74, 9, "#fff") + at(50, 86, 9, "#fff") + at(82, 74, 9, "#fff") + at(50, 42, 14, "#7CC96F")
        + '<circle cx="46" cy="16" r="3" fill="#3b2a1a"/><circle cx="54" cy="16" r="3" fill="#3b2a1a"/>'),
 "tetrahedral": dict(words=["الشكل رباعي الأوجه", "رباعي الأوجه", "زاوية الرابطة", "زوايا الروابط"], only=S, anim="bob", face=SHAPE_FACE,
   body=bond(50, 52, 50, 12) + bond(50, 52, 16, 74) + bond(50, 52, 84, 74) + '<path d="M50 52 L62 86 L70 80Z" fill="#3b2a1a"/>'
        + at(50, 12, 9, "#fff") + at(16, 74, 9, "#fff") + at(84, 74, 9, "#fff") + at(68, 86, 9, "#fff") + at(50, 52, 14, "#3b4252")
        + '<path d="M42 34 A20 20 0 0 0 34 60" fill="none" stroke="#F5A623" stroke-width="2.4"/>'),
 # ---------- bonds ----------
 "bond_types": dict(words=["الروابط الأحادية والثنائية والثلاثية", "الرابطة الأحادية", "الرابطة التساهمية الأحادية"], only=S, anim="bob", face=(50, 92, .3),
   body="".join(at(22, y, 8, "#7CC6F2") + at(78, y, 8, "#7CC6F2") + "".join(bond(30, y + d, 70, y + d, 3) for d in ds) for y, ds in ((16, (0,)), (44, (-3, 3)), (72, (-5, 0, 5))))),
 "double_bond": dict(words=["الرابطة الثنائية", "الروابط الثنائية", "الرابطة التساهمية الثنائية"], only=S, anim="bob", face=(50, 80, .34),
   body=bond(30, 40, 70, 40) + bond(30, 52, 70, 52) + at(24, 46, 16, "#3b4252") + at(76, 46, 16, "#E2504C")),
 "triple_bond": dict(words=["الرابطة الثلاثية", "الروابط الثلاثية", "الرابطة التساهمية الثلاثية"], only=S, anim="bob", face=(50, 80, .34),
   body=bond(30, 36, 70, 36) + bond(30, 46, 70, 46) + bond(30, 56, 70, 56) + at(24, 46, 16, "#5B8DEF") + at(76, 46, 16, "#5B8DEF")),
 "sigma_pi": dict(words=["الرابطة سيجما", "الرابطة باي", "التهجين", "الأفلاك المهجنة", "التداخل بين الأفلاك"], only=S, anim="sway", face=(50, 50, .3),
   body='<ellipse cx="34" cy="50" rx="22" ry="12" fill="#9FD0F5" {OL}/><ellipse cx="66" cy="50" rx="22" ry="12" fill="#F5D547" {OL}/>'
        '<ellipse cx="34" cy="20" rx="9" ry="14" fill="#B58BD9" opacity=".8" {OL}/><ellipse cx="66" cy="20" rx="9" ry="14" fill="#B58BD9" opacity=".8" {OL}/>'
        '<ellipse cx="34" cy="80" rx="9" ry="14" fill="#B58BD9" opacity=".8" {OL}/><ellipse cx="66" cy="80" rx="9" ry="14" fill="#B58BD9" opacity=".8" {OL}/>'
        '<path d="M43 20 H57 M43 80 H57" stroke="#7A4E9F" stroke-width="2" stroke-dasharray="3 2"/>'),
 "hydrogen_bond": dict(words=["الرابطة الهيدروجينية", "الروابط الهيدروجينية", "القوى بين الجزيئية", "قوى ثنائية القطب", "قوى التشتت", "قوى لندن"], only=S, anim="sway", face=(30, 34, .3),
   body=at(30, 34, 13, "#E2504C") + bond(30, 34, 14, 52, 3) + bond(30, 34, 46, 52, 3) + at(14, 54, 7, "#fff") + at(48, 54, 7, "#fff")
        + '<path d="M54 58 L66 66" stroke="#5B8DEF" stroke-width="3" stroke-dasharray="3 3" stroke-linecap="round"/>'
        + at(72, 70, 13, "#E2504C") + bond(72, 70, 88, 52, 3) + bond(72, 70, 88, 88, 3) + at(90, 50, 7, "#fff") + at(90, 90, 7, "#fff")),
 "metallic_bond": dict(words=["الرابطة الفلزية", "الروابط الفلزية", "بحر الإلكترونات", "الفلزات والرابطة الفلزية"], only=S, anim="buzz", face=(50, 50, .3),
   body='<rect x="6" y="10" width="88" height="80" rx="12" fill="#E3EAF2" {OL}/>' + "".join(at(x, y, 9, "#B8C4D0") + f'<text x="{x}" y="{y + 4}" text-anchor="middle" font-size="11" font-weight="800" fill="#3b2a1a">+</text>' for x in (24, 50, 76) for y in (28, 72) if not (x == 50 and y == 28))
        + "".join(f'<circle cx="{x}" cy="{y}" r="2.6" fill="#5B8DEF"/>' for x, y in ((14, 50), (36, 48), (62, 52), (86, 46), (38, 18), (64, 86), (88, 82), (12, 84), (50, 64)))),
 "chemical_bond": dict(words=["الرابطة الكيميائية", "الروابط الكيميائية", "تكوين الروابط"], only=S, anim="bob", face=(50, 82, .34),
   body='<circle cx="36" cy="46" r="26" fill="#9FD0F5" opacity=".85" {OL}/><circle cx="64" cy="46" r="26" fill="#F5D547" opacity=".85" {OL}/><circle cx="50" cy="40" r="3.4" fill="#3b2a1a"/><circle cx="50" cy="52" r="3.4" fill="#3b2a1a"/>'),
 "electronegativity": dict(words=["الكهروسالبية", "الرابطة القطبية", "الجزيئات القطبية", "قطبية الجزيء"], only=S, anim="bob", face=(68, 76, .3),
   body='<path d="M20 46 C20 30 34 26 50 30 C70 22 92 30 92 46 C92 62 70 70 50 62 C34 66 20 62 20 46Z" fill="#9FD0F5" opacity=".6" {OL}/>' + at(32, 46, 10, "#fff") + at(70, 46, 15, "#E2504C")
        + '<text x="32" y="22" text-anchor="middle" font-size="13" font-weight="800" fill="#3b2a1a" direction="ltr">δ+</text><text x="72" y="20" text-anchor="middle" font-size="13" font-weight="800" fill="#3b2a1a" direction="ltr">δ−</text>'),
 "alloy": dict(words=["السبيكة", "السبائك", "السبائك الاستبدالية", "السبائك البينية"], only=S, anim="bob", face=(50, 92, .3),
   body="".join(at(x, y, 9, "#F5A623" if (x, y) in ((32, 30), (68, 66)) else "#B8C4D0") for x in (14, 32, 50, 68, 86) for y in (12, 30, 48, 66, 84) if (x, y) != (50, 84))
        + "".join(f'<circle cx="{x}" cy="{y}" r="4" fill="#5DBB63" {{OL}}/>' for x, y in ((41, 21), (59, 57), (23, 75)))),
 # ---------- organic and big molecules ----------
 "benzene": dict(words=["البنزين (الحلقي)", "البنزين الحلقي", "حلقة البنزين", "المركبات الأروماتية", "الهيدروكربونات الأروماتية"], only=S, anim="sun", face=(50, 50, .34),
   body='<path d="M50 10 L84 30 L84 70 L50 90 L16 70 L16 30Z" fill="#E8F1FA" {OL}/><circle cx="50" cy="50" r="22" fill="none" stroke="#3b2a1a" stroke-width="3"/>'),
 "structural": dict(words=["الصيغة البنائية", "الصيغ البنائية", "صيغة لويس البنائية"], only=S, anim="bob", face=(50, 50, .3),
   body=bond(50, 50, 50, 16) + bond(50, 50, 50, 84) + bond(50, 50, 16, 50) + bond(50, 50, 84, 50)
        + "".join(at(x, y, 10, "#fff") + f'<text x="{x}" y="{y + 4.5}" text-anchor="middle" font-size="12" font-weight="800" fill="#3b2a1a" direction="ltr">H</text>' for x, y in ((50, 14), (50, 86), (14, 50), (86, 50)))
        + at(50, 50, 14, "#3b4252")),
 "polymer": dict(words=["البوليمر", "البوليمرات", "البلمرة", "البلمرة بالإضافة", "البلمرة بالتكثيف", "المونومر", "المونومرات", "وحدة البناء", "البلاستيك الحراري", "البلاستيك المتصلد"], only=S, anim="wiggle", face=(16, 50, .3),
   body="".join(bond(16 + i * 17, 50 + (8 if i % 2 else -8), 33 + i * 17, 50 + (-8 if i % 2 else 8), 3) for i in range(4))
        + "".join(at(16 + i * 17, 50 + (8 if i % 2 else -8), 9 if i else 12, "#F5A623" if i == 0 else "#9FD0F5") for i in range(5))
        + '<circle cx="16" cy="42" r="17" fill="none" stroke="#F5A623" stroke-width="2" stroke-dasharray="3 3"/>'),
 "glucose": dict(words=["الجلوكوز", "الجلكوز", "السكريات الأحادية", "سكر الجلوكوز"], only=S, anim="bob", face=(50, 56, .32),
   body='<path d="M30 30 L56 22 L80 36 L76 66 L50 74 L26 60Z" fill="#FFF0B3" {OL}/>' + at(56, 22, 6, "#E2504C")
        + '<text x="56" y="14" text-anchor="middle" font-size="11" font-weight="800" fill="#3b2a1a" direction="ltr">O</text>'
        + "".join(f'<path d="M{x} {y} l{dx} {dy}" stroke="#3b2a1a" stroke-width="2"/>' for x, y, dx, dy in ((30, 30, -10, -10), (80, 36, 10, -8), (76, 66, 10, 8), (50, 74, 0, 12), (26, 60, -10, 8)))),
 "starch": dict(words=["النشا", "السليلوز", "الجلايكوجين", "الكربوهيدرات المعقدة", "السكريات المتعددة"], only=S, anim="wiggle", face=(50, 84, .3),
   body="".join(f'<path d="M{x} 40 L{x + 9} 34 L{x + 18} 40 L{x + 18} 52 L{x + 9} 58 L{x} 52Z" fill="#FFF0B3" {{OL}}/>' for x in (4, 28, 52, 76))
        + "".join(bond(x, 46, x + 6, 46, 2.4) for x in (22, 46, 70))),
 "peptide": dict(words=["الببتيد", "الببتيدات", "الرابطة الببتيدية", "عديد الببتيد"], only=S, anim="wiggle", face=(50, 84, .3),
   body="".join(bond(14 + i * 18, 46, 32 + i * 18, 46, 3) for i in range(4))
        + "".join(at(14 + i * 18, 46, 9, c) + f'<text x="{14 + i * 18}" y="{50}" text-anchor="middle" font-size="9" font-weight="800" fill="#3b2a1a" direction="ltr">{t}</text>'
                  for i, (c, t) in enumerate((("#F28AA8", "G"), ("#7CC96F", "A"), ("#F5D547", "V"), ("#9FD0F5", "L"), ("#B58BD9", "S"))))),
 "lipid": dict(words=["الليبيدات", "الأحماض الدهنية", "الستيرويدات", "الشموع", "الدهون الثلاثية", "الدهون المشبعة وغير المشبعة"], only=S, anim="sway", face=(50, 22, .32),
   body=at(50, 20, 15, "#9FD0F5") + '<path d="M44 34 L38 44 L46 52 L38 62 L46 72 L38 82 L44 92 M56 34 L62 44 L54 52 L62 62 L54 72 L62 82 L56 92" fill="none" stroke="#F5A623" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>'),
 "isomers": dict(words=["المتشكلات", "المتشكلات البنائية", "المتشكلات الفراغية", "المتشكلات الهندسية (سيس-ترانس)", "الكيرالية", "المتشكلات الضوئية"], only=S, anim="wobble", face=(50, 92, .3),
   body='<path d="M50 4 V96" stroke="#9AA5B1" stroke-width="2" stroke-dasharray="4 4"/>'
        + bond(26, 46, 26, 18, 3) + bond(26, 46, 10, 62, 3) + bond(26, 46, 40, 64, 3) + at(26, 16, 7, "#E2504C") + at(10, 64, 7, "#7CC96F") + at(40, 66, 7, "#F5D547") + at(26, 46, 10, "#3b4252")
        + bond(74, 46, 74, 18, 3) + bond(74, 46, 90, 62, 3) + bond(74, 46, 60, 64, 3) + at(74, 16, 7, "#E2504C") + at(90, 64, 7, "#7CC96F") + at(60, 66, 7, "#F5D547") + at(74, 46, 10, "#3b4252")),
 "allotropes": dict(words=["التآصل", "المتآصلات", "الجرافيت والألماس"], only=S, anim="bob", face=(74, 84, .3),
   body='<path d="M26 10 L44 30 L26 90 L8 30Z" fill="#CFEFFF" {OL}/><path d="M8 30 H44 M26 10 L20 30 L26 90 L32 30Z" fill="none" stroke="#5AA9DC" stroke-width="1.6"/>'
        + "".join(f'<path d="M56 {y} L94 {y}" stroke="#3b4252" stroke-width="5" stroke-linecap="round"/>' for y in (22, 40, 58))),
 "cracking": dict(words=["التكسير الحراري", "التكسير الحفزي", "تكرير النفط"], only=S, anim="buzz", face=(50, 30, .3),
   body="".join(at(10 + i * 16, 30, 7, "#3b4252") for i in range(6)) + "".join(bond(10 + i * 16, 30, 26 + i * 16, 30, 3) for i in range(5) if i != 2)
        + '<path d="M44 20 L48 30 L44 40" fill="none" stroke="#E2504C" stroke-width="3"/>'
        + '<path d="M50 96 C36 90 36 74 46 66 C46 76 54 76 52 66 C62 72 66 90 50 96Z" fill="#F5A623" {OL}/>'),
 # ---------- the atom ----------
 "proton": dict(words=["البروتون", "البروتونات"], only=S, anim="bounce", face=(50, 58, .55),
   body=at(50, 52, 38, "#F28A8A") + '<text x="50" y="40" text-anchor="middle" font-size="26" font-weight="800" fill="#fff">+</text>'),
 "neutron": dict(words=["النيوترون", "النيوترونات"], only=S, anim="bob", face=(50, 58, .55),
   body=at(50, 52, 38, "#B8C4D0") + '<text x="50" y="40" text-anchor="middle" font-size="22" font-weight="800" fill="#fff" direction="ltr">0</text>'),
 "bohr": dict(words=["نموذج بور الذري", "نموذج بور", "مستويات الطاقة", "الحالة المستقرة", "مستويات الطاقة الرئيسية"], only=S, anim="sun", face=(50, 50, .3),
   body='<circle cx="50" cy="50" r="24" fill="none" stroke="#9AA5B1" stroke-width="2"/><circle cx="50" cy="50" r="42" fill="none" stroke="#9AA5B1" stroke-width="2"/>'
        + at(50, 50, 12, "#F28A8A") + "".join(f'<circle cx="{x}" cy="{y}" r="4.5" fill="#5B8DEF" {{OL}}/>' for x, y in ((74, 50), (26, 50), (50, 8), (92, 50), (50, 92), (20, 20)))),
 "rutherford": dict(words=["نموذج رذرفورد", "تجربة رذرفورد", "صفيحة الذهب"], only=S, anim="sun", face=(50, 50, .3),
   body='<ellipse cx="50" cy="50" rx="44" ry="16" fill="none" stroke="#9AA5B1" stroke-width="2"/><ellipse cx="50" cy="50" rx="44" ry="16" fill="none" stroke="#9AA5B1" stroke-width="2" transform="rotate(60 50 50)"/>'
        '<ellipse cx="50" cy="50" rx="44" ry="16" fill="none" stroke="#9AA5B1" stroke-width="2" transform="rotate(-60 50 50)"/>' + at(50, 50, 7, "#F28A8A")
        + "".join(f'<circle cx="{x}" cy="{y}" r="4" fill="#5B8DEF" {{OL}}/>' for x, y in ((94, 50), (28, 12), (28, 88)))),
 "dalton": dict(words=["نظرية دالتون الذرية", "نموذج دالتون", "النظرية الذرية"], only=S, anim="bounce", face=(50, 54, .55),
   body='<circle cx="50" cy="50" r="40" fill="#9AA5B1" {OL}/><ellipse cx="36" cy="34" rx="12" ry="8" fill="#fff" opacity=".45"/>'),
 "lewis": dict(words=["نموذج لويس", "التمثيل النقطي للإلكترونات", "تراكيب لويس", "التوزيع الإلكتروني للغاز النبيل", "قاعدة الثمانية"], only=S, anim="bob", face=(50, 84, .36),
   body='<rect x="14" y="8" width="72" height="72" rx="14" fill="#F5D547" {OL}/><text x="50" y="56" text-anchor="middle" font-size="30" font-weight="800" fill="#3b2a1a" direction="ltr">Ne</text>'
        + "".join(f'<circle cx="{x}" cy="{y}" r="3.2" fill="#3b2a1a"/>' for x, y in ((44, 20), (56, 20), (44, 68), (56, 68), (24, 38), (24, 50), (76, 38), (76, 50)))),
 "orbitals": dict(words=["المستويات الفرعية (الأفلاك)", "الأفلاك", "المستويات الفرعية", "الفلك s", "الفلك p"], only=S, anim="sway", face=(50, 50, .3),
   body='<circle cx="50" cy="50" r="12" fill="#F5D547" {OL}/><ellipse cx="50" cy="24" rx="10" ry="18" fill="#9FD0F5" opacity=".85" {OL}/><ellipse cx="50" cy="76" rx="10" ry="18" fill="#9FD0F5" opacity=".85" {OL}/>'
        '<ellipse cx="24" cy="50" rx="18" ry="10" fill="#F28AA8" opacity=".85" {OL}/><ellipse cx="76" cy="50" rx="18" ry="10" fill="#F28AA8" opacity=".85" {OL}/>'),
 "aufbau": dict(words=["مبدأ أوفباو", "مبدأ باولي للاستبعاد", "قاعدة هوند", "التوزيع الإلكتروني", "الترتيب الإلكتروني"], only=S, anim="bob", face=(78, 86, .3),
   body="".join(f'<rect x="{x}" y="{y}" width="16" height="16" fill="#fff" {{OL}}/>' for x, y in ((10, 74), (10, 50), (34, 50), (52, 50), (70, 50), (10, 26), (34, 26), (52, 26), (70, 26)))
        + "".join(f'<path d="M{x + 5} {y + 13} V{y + 3} M{x + 2} {y + 6} l3 -3 l3 3" fill="none" stroke="#E2504C" stroke-width="2"/>' for x, y in ((10, 74), (10, 50), (34, 50), (52, 50), (70, 50)))
        + "".join(f'<path d="M{x + 11} {y + 3} V{y + 13} M{x + 8} {y + 10} l3 3 l3 -3" fill="none" stroke="#5B8DEF" stroke-width="2"/>' for x, y in ((10, 74), (10, 50)))
        + '<text x="38" y="86" font-size="11" font-weight="800" fill="#3b2a1a" direction="ltr">1s</text><text x="88" y="62" font-size="11" font-weight="800" fill="#3b2a1a" direction="ltr">2p</text>'),
 "excited": dict(words=["الحالة المثارة", "الإثارة", "انبعاث الضوء من الذرة", "طيف الانبعاث"], only=S, anim="bounce", face=(24, 84, .3),
   body='<path d="M10 86 H60 M10 58 H60 M10 34 H60 M10 16 H60" stroke="#9AA5B1" stroke-width="3" stroke-linecap="round"/>'
        '<path d="M30 80 C30 60 32 44 34 22" fill="none" stroke="#F5A623" stroke-width="3" stroke-dasharray="4 3"/><path d="M28 28 l6 -8 l5 8" fill="none" stroke="#F5A623" stroke-width="3" stroke-linejoin="round"/>'
        '<circle cx="34" cy="16" r="5" fill="#5B8DEF" {OL}/><path d="M66 40 q4 -6 8 0 t8 0 t8 0" fill="none" stroke="#B58BD9" stroke-width="3"/>'),
 "photoelectric": dict(words=["التأثير الكهروضوئي", "الفوتون", "الفوتونات"], only=S, anim="buzz", face=(30, 84, .3),
   body='<rect x="4" y="70" width="70" height="22" rx="4" fill="#B8C4D0" {OL}/><path d="M10 10 q5 6 10 0 t10 0 t10 0 L46 52" fill="none" stroke="#B58BD9" stroke-width="3"/><path d="M40 50 l6 6 l2 -8" fill="none" stroke="#B58BD9" stroke-width="3" stroke-linejoin="round"/>'
        '<circle cx="80" cy="34" r="6" fill="#5B8DEF" {OL}/><path d="M56 68 L76 40" stroke="#5B8DEF" stroke-width="2" stroke-dasharray="3 3"/>'),
 "uncertainty": dict(words=["مبدأ هايزنبرج للشك", "مبدأ عدم التأكد", "السحابة الإلكترونية", "النموذج الميكانيكي الكمي"], only=S, anim="wobble", face=(50, 54, .3),
   body='<circle cx="50" cy="50" r="42" fill="#9FD0F5" opacity=".35"/><circle cx="50" cy="50" r="28" fill="#9FD0F5" opacity=".4"/><circle cx="50" cy="50" r="14" fill="#9FD0F5" opacity=".55"/>'
        + at(50, 50, 7, "#F28A8A") + '<text x="78" y="28" text-anchor="middle" font-size="22" font-weight="800" fill="#3b2a1a">؟</text>'
        + "".join(f'<circle cx="{x}" cy="{y}" r="2" fill="#5B8DEF"/>' for x, y in ((24, 30), (70, 66), (36, 74), (66, 22), (20, 58), (80, 50)))),
 "cathode_tube": dict(words=["أنبوب الأشعة المهبطية", "الأشعة المهبطية", "اكتشاف الإلكترون"], only=S, anim="buzz", face=(50, 76, .3),
   body='<path d="M14 34 C14 26 22 22 30 22 L70 22 C78 22 86 26 86 34 L86 62 C86 70 78 74 70 74 L30 74 C22 74 14 70 14 62Z" fill="#E8F4FB" {OL}/>'
        '<rect x="18" y="38" width="8" height="20" rx="2" fill="#9AA5B1" {OL}/><rect x="74" y="38" width="8" height="20" rx="2" fill="#9AA5B1" {OL}/><path d="M26 48 H74" stroke="#7FD6C9" stroke-width="5" stroke-linecap="round"/>'
        '<path d="M22 22 V10 M78 22 V10" stroke="#3b2a1a" stroke-width="2"/>'),
 "atomic_radius": dict(words=["نصف القطر الذري", "نصف قطر الذرة", "نصف القطر الأيوني"], only=S, anim="bob", face=(50, 74, .32),
   body='<circle cx="50" cy="44" r="38" fill="#E8F4FB" {OL}/>' + at(50, 44, 8, "#F28A8A") + '<path d="M50 44 H86" stroke="#E2504C" stroke-width="3"/><path d="M80 38 l7 6 l-7 6" fill="none" stroke="#E2504C" stroke-width="3" stroke-linejoin="round"/>'
        '<text x="68" y="38" text-anchor="middle" font-size="12" font-weight="800" fill="#3b2a1a" direction="ltr">r</text>'),
 "block_s": dict(words=["عناصر المستوى s", "عناصر الفئة s"], only=S, anim="bob", face=(50, 50, .3), body=periodic("s")),
 "block_p": dict(words=["عناصر المستوى p", "عناصر الفئة p"], only=S, anim="bob", face=(50, 50, .3), body=periodic("p")),
 "block_d": dict(words=["عناصر المستوى d", "عناصر الفئة d", "العناصر الانتقالية", "الفلزات الانتقالية"], only=S, anim="bob", face=(50, 30, .3), body=periodic("d")),
 "block_f": dict(words=["عناصر المستوى f", "عناصر الفئة f", "العناصر الانتقالية الداخلية", "اللانثانيدات والأكتينيدات"], only=S, anim="bob", face=(50, 46, .3), body=periodic("f")),
 "representative": dict(words=["العناصر الممثلة", "العناصر الرئيسة"], only=S, anim="bob", face=(50, 50, .3), body=periodic("rep")),
 "halogens": dict(words=["الهالوجينات والغازات النبيلة", "الهالوجينات", "الغازات النبيلة", "الغازات الخاملة"], only=S, anim="bob", face=(46, 50, .3), body=periodic("hal")),
 # ---------- heat ----------
 "calorimeter": dict(words=["المسعر", "المسعر الحراري", "الكيمياء الحرارية", "كمية الحرارة"], only=S, anim="bob", face=(50, 72, .38),
   body='<rect x="16" y="34" width="68" height="60" rx="8" fill="#E8F4FB" {OL}/><rect x="12" y="26" width="76" height="10" rx="4" fill="#9AA5B1" {OL}/><path d="M22 56 H78 V86 C78 90 74 90 70 90 H30 C26 90 22 90 22 86Z" fill="#9FD0F5" opacity=".8"/>'
        '<rect x="58" y="4" width="8" height="66" rx="4" fill="#fff" {OL}/><circle cx="62" cy="72" r="6" fill="#E2504C" {OL}/><path d="M62 70 V40" stroke="#E2504C" stroke-width="3"/><path d="M36 8 V70 M30 70 H42" stroke="#3b2a1a" stroke-width="2.4"/>'),
 "energy_diagram": dict(words=["المحتوى الحراري", "التغير في المحتوى الحراري", "المعقد المنشط", "التفاعلات الماصة والطاردة للحرارة"], only=S, anim="bob", face=(52, 22, .3),
   body='<path d="M10 4 V90 H96" fill="none" stroke="#3b2a1a" stroke-width="2.6"/><path d="M14 62 H30 C42 62 44 18 52 18 C60 18 64 76 74 76 H92" fill="none" stroke="#E2504C" stroke-width="3.4" stroke-linecap="round"/>'
        '<path d="M86 62 V74 M82 70 l4 5 l4 -5" fill="none" stroke="#5B8DEF" stroke-width="2.4"/><text x="80" y="58" text-anchor="middle" font-size="11" font-weight="800" fill="#5B8DEF" direction="ltr">ΔH</text>'),
 # ---------- solutions and the lab ----------
 "dilution": dict(words=["التخفيف", "الإذابة", "الامتزاج", "المذيب والمذاب", "عملية الذوبان"], only=S, anim="drip", face=(64, 76, .36),
   body='<path d="M40 40 H90 V86 C90 92 86 96 80 96 H50 C44 96 40 92 40 86Z" fill="#E8F4FB" {OL}/><path d="M42 62 H88 V86 C88 90 84 94 80 94 H50 C46 94 42 90 42 86Z" fill="#C9B6F5"/>'
        '<path d="M8 10 L32 16 L28 28 Z" fill="#9FD0F5" {OL}/><path d="M30 24 C40 30 50 40 56 56" fill="none" stroke="#7CC6F2" stroke-width="4" stroke-linecap="round"/>'),
 "tyndall": dict(words=["تأثير تندال", "المخاليط الغروية", "الغروي", "المعلق والغروي"], only=S, anim="bob", face=(66, 80, .3),
   body='<rect x="4" y="38" width="22" height="16" rx="3" fill="#F5D547" {OL}/><path d="M26 40 L96 30 L96 62 L26 52Z" fill="#FFF3B0" opacity=".85"/>'
        '<rect x="44" y="20" width="40" height="72" rx="6" fill="#E8F4FB" opacity=".7" {OL}/>' + "".join(f'<circle cx="{x}" cy="{y}" r="1.8" fill="#9AA5B1"/>' for x, y in ((52, 44), (60, 50), (70, 40), (76, 54), (56, 70), (72, 78)))),
 "brownian": dict(words=["الحركة البراونية", "نظرية الحركة الجزيئية", "حركة الجسيمات"], only=S, anim="buzz", face=(80, 22, .3),
   body='<path d="M12 80 L30 58 L22 40 L44 30 L52 54 L70 44 L62 22 L82 18" fill="none" stroke="#F5A623" stroke-width="2.6" stroke-dasharray="4 3" stroke-linejoin="round"/>' + at(80, 18, 10, "#F5A623")
        + "".join(f'<circle cx="{x}" cy="{y}" r="3" fill="#9FD0F5" {{OL}}/>' for x, y in ((20, 24), (40, 70), (64, 72), (88, 52), (10, 50), (52, 12), (34, 90)))),
 "titration": dict(words=["المعايرة", "نقطة النهاية", "نقطة التكافؤ", "السحاحة"], only=("chemistry",), anim="drip", face=(50, 84, .3),
   body='<rect x="44" y="2" width="12" height="50" rx="3" fill="#E8F4FB" {OL}/><path d="M46 10 H54 V50 H46Z" fill="#9FD0F5"/><path d="M50 52 V60" stroke="#3b2a1a" stroke-width="3"/>'
        '<path d="M50 64 C48 66 48 68 50 70 C52 68 52 66 50 64Z" fill="#9FD0F5"/><path d="M40 72 H60 L80 94 H20Z" fill="#F7B5D9" {OL}/><path d="M42 72 V66 H58 V72" fill="none" stroke="#3b2a1a" stroke-width="2.4"/>'),
 "ph_scale": dict(words=["مقياس pH", "الرقم الهيدروجيني", "الرقم الهيدروكسيدي pOH", "الوسط الحمضي والقاعدي", "الأس الهيدروجيني", "pH"], only=S, anim="bob", face=(50, 84, .3),
   body="".join(f'<rect x="{4 + i * 13}" y="20" width="13" height="40" fill="{c}"/>' for i, c in enumerate(("#E2504C", "#F28A4A", "#F5C518", "#7CC96F", "#3FA7A0", "#5B8DEF", "#7A4E9F")))
        + '<rect x="4" y="20" width="91" height="40" rx="3" fill="none" {OL}/><text x="10" y="14" font-size="10" font-weight="800" fill="#3b2a1a" direction="ltr">0</text><text x="46" y="14" font-size="10" font-weight="800" fill="#3b2a1a" direction="ltr">7</text><text x="84" y="14" font-size="10" font-weight="800" fill="#3b2a1a" direction="ltr">14</text>'),
 "salt_crystal": dict(words=["الملح", "الملح المائي", "الملح اللامائي", "تميؤ الأملاح", "الشبكة البلورية"], only=S, anim="bob", face=(50, 88, .3),
   body="".join(at(14 + c * 24, 14 + r * 24, 9 if (r + c) % 2 else 6, "#7CC96F" if (r + c) % 2 else "#B58BD9") for r in range(4) for c in range(4))
        + "".join(f'<path d="M{14 + c * 24} 14 V86 M14 {14 + c * 24} H86" stroke="#3b2a1a" stroke-width="1"/>' for c in range(4))),
 "precipitate": dict(words=["الراسب", "تفاعلات الترسيب", "المادة الراسبة"], only=S, anim="drip", face=(50, 44, .3),
   body='<path d="M34 4 H66 V82 C66 92 58 96 50 96 C42 96 34 92 34 82Z" fill="#E8F4FB" {OL}/><path d="M36 30 H64 V82 C64 90 58 94 50 94 C42 94 36 90 36 82Z" fill="#CDE9F7"/>'
        '<path d="M37 78 C44 74 56 74 63 78 V84 C63 90 58 94 50 94 C42 94 37 90 37 84Z" fill="#F5D547"/>' + "".join(f'<circle cx="{x}" cy="{y}" r="2" fill="#E3A70F"/>' for x, y in ((46, 60), (54, 66), (44, 70), (58, 56)))),
 "chromatography": dict(words=["الكروماتوجرافيا", "الكروماتوغرافيا", "الفصل بالكروماتوجرافيا"], only=S, anim="bob", face=(50, 90, .3),
   body='<path d="M18 30 H82 V88 C82 92 78 96 74 96 H26 C22 96 18 92 18 88Z" fill="#E8F4FB" {OL}/><path d="M20 76 H80 V88 C80 92 76 94 72 94 H28 C24 94 20 92 20 88Z" fill="#9FD0F5"/>'
        '<rect x="38" y="6" width="24" height="76" fill="#fff" {OL}/><circle cx="50" cy="66" r="3" fill="#3b2a1a"/><ellipse cx="50" cy="50" rx="5" ry="4" fill="#E2504C"/><ellipse cx="50" cy="36" rx="5" ry="4" fill="#F5D547"/><ellipse cx="50" cy="22" rx="5" ry="4" fill="#5B8DEF"/>'),
 "distillation": dict(words=["التقطير", "التقطير التجزيئي", "التقطير البسيط", "جهاز التقطير"], only=S, anim="drip", face=(20, 66, .3),
   body='<circle cx="20" cy="62" r="16" fill="#E8F4FB" {OL}/><path d="M6 66 C10 78 30 78 34 66Z" fill="#C9B6F5"/><path d="M16 46 V36 L80 58" fill="none" stroke="#3b2a1a" stroke-width="5" stroke-linecap="round"/>'
        '<path d="M34 42 L74 56" stroke="#7CC6F2" stroke-width="12" stroke-linecap="round" opacity=".6"/><path d="M80 58 V64" stroke="#3b2a1a" stroke-width="3"/>'
        '<path d="M68 70 H92 L88 94 H72Z" fill="#E8F4FB" {OL}/><path d="M70 84 H90 L88 94 H72Z" fill="#C9B6F5"/><path d="M14 96 C8 90 10 84 16 80 C16 86 22 86 20 80 C26 84 26 92 20 96Z" fill="#F5A623" {OL}/>'),
 "filtration": dict(words=["الترشيح", "ورق الترشيح", "قمع الترشيح"], only=S, anim="drip", face=(50, 30, .3),
   body='<path d="M14 10 H86 L56 50 V66 H44 V50Z" fill="#E8F4FB" {OL}/><path d="M22 14 H78 L52 46 H48Z" fill="#fff" {OL}/><path d="M28 18 H72 L54 40 H46Z" fill="#C9A06A" opacity=".75"/>'
        '<path d="M50 68 C48 72 48 74 50 76 C52 74 52 72 50 68Z" fill="#9FD0F5"/><path d="M26 80 H74 L70 96 H30Z" fill="#E8F4FB" {OL}/><path d="M28 88 H72 L70 96 H30Z" fill="#9FD0F5"/>'),
 "crystallization": dict(words=["التبلور", "البلورات الكيميائية", "التبخير والتبلور"], only=S, anim="bob", face=(50, 84, .3),
   body='<path d="M6 60 C6 84 94 84 94 60Z" fill="#E8F4FB" {OL}/>' + "".join(f'<path d="M{x} {y} l7 -14 l7 14 l-7 6Z" fill="#CFEFFF" {{OL}}/>' for x, y in ((18, 64), (34, 60), (52, 64), (70, 60)))),
 "sublimation": dict(words=["التسامي والترسب", "التسامي", "الترسب الغازي"], only=S, anim="bob", face=(32, 82, .3),
   body='<rect x="12" y="66" width="40" height="28" rx="4" fill="#F5F5F5" {OL}/><path d="M24 62 C20 46 34 40 30 24 M40 62 C36 46 50 40 46 24" fill="none" stroke="#9AA5B1" stroke-width="3" stroke-dasharray="4 3"/>'
        + "".join(f'<circle cx="{x}" cy="{y}" r="4" fill="#E3EAF2" {{OL}}/>' for x, y in ((28, 14), (44, 10), (60, 18), (76, 12), (70, 30)))
        + '<path d="M84 30 C92 48 84 60 70 70" fill="none" stroke="#5B8DEF" stroke-width="2.6"/><path d="M68 62 l2 9 l8 -3" fill="none" stroke="#5B8DEF" stroke-width="2.6" stroke-linejoin="round"/>'),
 "viscosity": dict(words=["اللزوجة", "السوائل اللزجة"], only=S, anim="drip", face=(40, 26, .32),
   body='<path d="M10 20 C10 8 70 8 70 20 C70 30 10 30 10 20Z" fill="#9AA5B1" {OL}/><path d="M68 18 L96 6" stroke="#9AA5B1" stroke-width="8" stroke-linecap="round"/>'
        '<path d="M30 28 C30 44 36 52 34 66 C33 76 40 84 44 94 C46 84 50 74 48 62 C46 50 50 40 50 28Z" fill="#F5B53D" {OL}/>'),
 "surface_tension": dict(words=["التوتر السطحي", "الخاصية السطحية"], only=S, anim="bob", face=(50, 36, .34),
   body='<path d="M0 66 C20 60 30 72 50 66 S80 60 100 66 V100 H0Z" fill="#9FD0F5" {OL}/><ellipse cx="50" cy="40" rx="16" ry="10" fill="#3b4252" {OL}/>'
        '<path d="M36 40 L16 64 M38 46 L28 66 M64 40 L84 64 M62 46 L72 66" stroke="#3b2a1a" stroke-width="2.4" stroke-linecap="round"/><path d="M10 66 q6 -4 12 0 M78 66 q6 -4 12 0" fill="none" stroke="#5B8DEF" stroke-width="2"/>'),
 "capillary": dict(words=["الخاصية الشعرية", "الأنابيب الشعرية", "الخاصة الشعرية"], only=S, anim="bob", face=(32, 82, .3),
   body='<path d="M8 50 H92 V88 C92 92 88 96 84 96 H16 C12 96 8 92 8 88Z" fill="#E8F4FB" {OL}/><path d="M10 64 H90 V88 C90 92 86 94 82 94 H18 C14 94 10 92 10 88Z" fill="#9FD0F5"/>'
        '<rect x="44" y="4" width="10" height="84" rx="3" fill="#fff" {OL}/><path d="M46 20 H52 V86 H46Z" fill="#7CC6F2"/><rect x="66" y="26" width="16" height="62" rx="3" fill="#fff" {OL}/><path d="M68 50 H80 V86 H68Z" fill="#7CC6F2"/>'),
 "phase_diagram": dict(words=["مخطط الحالة الفيزيائية والنقطة الثلاثية", "مخطط الحالة", "النقطة الثلاثية", "تغير الحالة الفيزيائية"], only=S, anim="bob", face=(70, 74, .3),
   body='<path d="M10 4 V92 H96" fill="none" stroke="#3b2a1a" stroke-width="2.6"/><path d="M14 88 C30 80 40 66 46 56 C56 46 74 30 92 20 M46 56 C44 40 42 22 40 8" fill="none" stroke="#5B8DEF" stroke-width="3"/>'
        '<circle cx="46" cy="56" r="4" fill="#E2504C" {OL}/><text x="26" y="44" text-anchor="middle" font-size="10" font-weight="800" fill="#3b2a1a">صلب</text><text x="68" y="28" text-anchor="middle" font-size="10" font-weight="800" fill="#3b2a1a">سائل</text><text x="74" y="72" text-anchor="middle" font-size="10" font-weight="800" fill="#3b2a1a">غاز</text>'),
 "avogadro": dict(words=["مبدأ أفوجادرو", "الحجم المولاري"], only=S, anim="bob", face=(28, 42, .32),
   body='<ellipse cx="28" cy="40" rx="22" ry="28" fill="#F28AA8" {OL}/><ellipse cx="72" cy="40" rx="22" ry="28" fill="#9FD0F5" {OL}/><path d="M28 68 V96 M72 68 V96" stroke="#3b2a1a" stroke-width="1.6"/>'
        + "".join(f'<circle cx="{x}" cy="{y}" r="2.6" fill="#fff" {{OL}}/>' for x, y in ((64, 28), (78, 36), (68, 50), (80, 22)))
        + "".join(f'<circle cx="{x}" cy="{y}" r="2.6" fill="#fff" {{OL}}/>' for x, y in ((20, 24), (36, 26), (18, 60), (38, 58)))),
 # ---------- electricity from reactions ----------
 "galvanic": dict(words=["الأنود", "الكاثود", "الجسر الملحي", "الخلية الجلفانية", "الخلية الكهروكيميائية", "الخلايا الكهروكيميائية", "التحليل الكهربائي"], only=S, anim="buzz", face=(50, 18, .3),
   body='<path d="M4 48 H44 V90 C44 94 40 96 36 96 H12 C8 96 4 94 4 90Z" fill="#9FD0F5" {OL}/><path d="M56 48 H96 V90 C96 94 92 96 88 96 H64 C60 96 56 94 56 90Z" fill="#F7D3B5" {OL}/>'
        '<rect x="18" y="34" width="8" height="46" fill="#9AA5B1" {OL}/><rect x="74" y="34" width="8" height="46" fill="#C98A55" {OL}/><path d="M34 64 V44 C34 36 66 36 66 44 V64" fill="none" stroke="#F5F0E1" stroke-width="7"/><path d="M34 64 V44 C34 36 66 36 66 44 V64" fill="none" stroke="#3b2a1a" stroke-width="1.4"/>'
        '<path d="M22 34 V18 H78 V34" fill="none" stroke="#3b2a1a" stroke-width="2.4"/><circle cx="50" cy="18" r="8" fill="#FFE27A" {OL}/>'),
 "battery": dict(words=["البطارية الأولية", "البطارية الثانوية", "بطارية الرصاص الحمضية", "البطاريات", "البطارية", "البطارية الجافة", "خلايا الوقود"], only=S, anim="buzz", face=(50, 60, .45),
   body='<rect x="26" y="16" width="48" height="78" rx="8" fill="#5DBB63" {OL}/><rect x="40" y="8" width="20" height="10" rx="3" fill="#9AA5B1" {OL}/><rect x="26" y="16" width="48" height="22" rx="8" fill="#F5D547" {OL}/>'
        '<text x="50" y="33" text-anchor="middle" font-size="16" font-weight="800" fill="#3b2a1a">+</text>'),
 "redox": dict(words=["العامل المؤكسد", "العامل المختزل", "عدد التأكسد", "الأكسدة والاختزال", "تفاعلات الأكسدة والاختزال", "الأكسدة", "الاختزال"], only=S, anim="bounce", face=(20, 70, .3),
   body=at(20, 60, 16, "#F5D547") + at(80, 60, 16, "#9FD0F5") + '<path d="M34 46 C44 26 58 26 66 44" fill="none" stroke="#E2504C" stroke-width="3"/><path d="M60 40 l7 6 l2 -9" fill="none" stroke="#E2504C" stroke-width="3" stroke-linejoin="round"/>'
        + '<circle cx="50" cy="30" r="6" fill="#5B8DEF" {OL}/><text x="50" y="18" text-anchor="middle" font-size="11" font-weight="800" fill="#3b2a1a" direction="ltr">e⁻</text>'
        + '<text x="80" y="66" text-anchor="middle" font-size="14" font-weight="800" fill="#3b2a1a" direction="ltr">−</text>'),
 "activity_series": dict(words=["سلسلة النشاط الكيميائي", "سلسلة النشاط", "نشاط الفلزات"], only=S, anim="bob", face=(78, 84, .3),
   body="".join(f'<rect x="{6 + i * 4}" y="{6 + i * 13}" width="{60 - i * 6}" height="11" rx="3" fill="{c}" {{OL}}/><text x="{14 + i * 4}" y="{15 + i * 13}" font-size="9" font-weight="800" fill="#3b2a1a" direction="ltr">{t}</text>'
                 for i, (t, c) in enumerate((("K", "#E2504C"), ("Na", "#F28A4A"), ("Ca", "#F5C518"), ("Mg", "#C5E1A5"), ("Zn", "#B8C4D0"), ("Fe", "#C98A55"), ("Cu", "#E3A16B"))))),
 "electrolyte": dict(words=["المواد الإلكتروليتية وغير الإلكتروليتية", "المواد الإلكتروليتية", "المحاليل الإلكتروليتية", "الإلكتروليت"], only=S, anim="buzz", face=(50, 86, .3),
   body='<path d="M14 44 H86 V88 C86 92 82 96 78 96 H22 C18 96 14 92 14 88Z" fill="#CDE9F7" {OL}/><rect x="30" y="34" width="8" height="48" fill="#9AA5B1" {OL}/><rect x="62" y="34" width="8" height="48" fill="#9AA5B1" {OL}/>'
        '<path d="M34 34 V16 H66 V34" fill="none" stroke="#3b2a1a" stroke-width="2.4"/><circle cx="50" cy="16" r="9" fill="#FFE27A" {OL}/><path d="M50 2 v4 M38 6 l3 3 M62 6 l-3 3" stroke="#F5A623" stroke-width="2.4" stroke-linecap="round"/>'
        '<text x="46" y="64" font-size="10" font-weight="800" fill="#3b2a1a" direction="ltr">+</text><text x="50" y="78" font-size="10" font-weight="800" fill="#3b2a1a" direction="ltr">−</text>'),
 # ---------- equilibrium and how fast ----------
 "equilibrium": dict(words=["ثابت الاتزان", "مبدأ لوتشاتلييه", "الاتزان المتجانس", "الاتزان غير المتجانس", "حساب تراكيز الاتزان", "الاتزان الديناميكي"], only=S, anim="sway", face=(50, 70, .34),
   body='<path d="M50 60 L36 92 H64Z" fill="#9AA5B1" {OL}/><rect x="8" y="52" width="84" height="8" rx="4" fill="#C98A55" {OL}/>'
        '<path d="M26 24 H74 M68 18 L76 24 M74 34 H26 M32 40 L24 34" fill="none" stroke="#3b2a1a" stroke-width="3" stroke-linecap="round"/>'
        + at(18, 44, 7, "#F28AA8") + at(82, 44, 7, "#9FD0F5")),
 "surface_area": dict(words=["مساحة السطح", "طبيعة المواد المتفاعلة"], only=S, anim="bob", face=(28, 66, .3),
   body='<rect x="8" y="44" width="40" height="40" rx="4" fill="#B8C4D0" {OL}/>' + "".join(f'<rect x="{x}" y="{y}" width="8" height="8" rx="1.5" fill="#B8C4D0" {{OL}}/>' for x, y in ((60, 76), (72, 76), (84, 76), (66, 64), (78, 64), (72, 52), (60, 88 - 2), (84, 86)))),
 "acid_base": dict(words=["نموذج أرهينيوس", "نموذج برونستد-لوري", "المواد المترددة", "الأحماض والقواعد", "الحمض المرافق والقاعدة المرافقة"], only=S, anim="bounce", face=(20, 66, .3),
   body=at(20, 60, 16, "#F28A8A") + at(80, 60, 16, "#9FD0F5") + '<path d="M34 50 C46 32 56 32 66 50" fill="none" stroke="#3b2a1a" stroke-width="3"/><path d="M60 46 l7 6 l2 -9" fill="none" stroke="#3b2a1a" stroke-width="3" stroke-linejoin="round"/>'
        + '<circle cx="50" cy="32" r="9" fill="#F5D547" {OL}/><text x="50" y="36" text-anchor="middle" font-size="10" font-weight="800" fill="#3b2a1a" direction="ltr">H⁺</text>'),
 # ---------- the science of chemistry ----------
 "chemistry": dict(words=["الكيمياء", "فروع الكيمياء", "علم الكيمياء", "الكيمياء العضوية", "الكيمياء التحليلية"], only=S, anim="bob", face=(50, 72, .4),
   body='<path d="M40 4 H60 V32 L84 80 C88 90 82 96 72 96 H28 C18 96 12 90 16 80 L40 32Z" fill="#E8F4FB" {OL}/><path d="M26 64 H74 L82 82 C84 90 80 92 72 92 H28 C20 92 16 90 18 82Z" fill="#7FD6C9"/>'
        + "".join(f'<circle cx="{x}" cy="{y}" r="3" fill="#fff" {{OL}}/>' for x, y in ((44, 54), (56, 46), (50, 36)))),
 "model": dict(words=["النماذج العلمية", "نموذج الكرة والعصا", "النماذج الجزيئية"], only=S, anim="sway", face=(50, 50, .3),
   body=bond(50, 50, 20, 24) + bond(50, 50, 80, 24) + bond(50, 50, 50, 86) + at(20, 24, 11, "#fff") + at(80, 24, 11, "#fff") + at(50, 86, 11, "#7CC96F") + at(50, 50, 16, "#E2504C")),
 "quant_data": dict(words=["البيانات الكمية", "البيانات النوعية", "القياسات الكمية"], only=S, anim="bob", face=(50, 30, .3),
   body='<path d="M8 6 V90 H96" fill="none" stroke="#3b2a1a" stroke-width="2.6"/>' + "".join(f'<rect x="{x}" y="{y}" width="14" height="{90 - y}" rx="2" fill="{c}" {{OL}}/>' for x, y, c in ((18, 60, "#9FD0F5"), (38, 40, "#F5D547"), (58, 52, "#F28AA8"), (78, 24, "#7CC96F")))),
 # ---------- CARDS: the concept IS a symbol ----------
 "f_molecular": dict(words=["الصيغة الجزيئية", "الصيغ الجزيئية"], only=S, anim="bob", face=CF, body=ltr_card("C₆H₁₂O₆", "#9FD0F5")),
 "f_empirical": dict(words=["الصيغة الأولية", "الصيغة الأبسط"], only=S, anim="bob", face=CF, body=ltr_card("CH₂O", "#F5D547")),
 "f_condensed": dict(words=["الصيغة البنائية المكثفة"], only=S, anim="bob", face=CF, body=ltr_card("CH₃CH₂OH", "#B58BD9")),
 "f_unit": dict(words=["وحدة الصيغة الكيميائية", "وحدة الصيغة"], only=S, anim="bob", face=CF, body=ltr_card("NaCl", "#7FD6C9")),
 "g_alcohol": dict(words=["الكحول", "الكحولات"], only=S, anim="bob", face=CF, body=ltr_card("R–OH", "#F28AA8")),
 "g_hydroxyl": dict(words=["مجموعة الهيدروكسيل", "المجموعة الوظيفية", "المجموعات الوظيفية"], only=S, anim="bob", face=CF, body=ltr_card("–OH", "#F5D547")),
 "g_aldehyde": dict(words=["الألدهيد", "الألدهيدات"], only=S, anim="bob", face=CF, body=ltr_card("R–CHO", "#9FD0F5")),
 "g_ketone": dict(words=["الكيتون", "الكيتونات"], only=S, anim="bob", face=CF, body=ltr_card("R–CO–R", "#B58BD9")),
 "g_carbonyl": dict(words=["مجموعة الكربونيل"], only=S, anim="bob", face=CF, body=ltr_card("C=O", "#7FD6C9")),
 "g_ether": dict(words=["الإيثر", "الإيثرات"], only=S, anim="bob", face=CF, body=ltr_card("R–O–R", "#F28AA8")),
 "g_ester": dict(words=["الإستر", "الإسترات", "الأسترات"], only=S, anim="bob", face=CF, body=ltr_card("R–COO–R", "#F5D547")),
 "g_amide": dict(words=["الأميد", "الأميدات"], only=S, anim="bob", face=CF, body=ltr_card("–CONH₂", "#9FD0F5")),
 "g_alkyl_halide": dict(words=["هاليد الألكيل", "هاليدات الألكيل"], only=S, anim="bob", face=CF, body=ltr_card("R–X", "#B58BD9")),
 "g_aryl_halide": dict(words=["هاليد الأريل", "هاليدات الأريل"], only=S, anim="bob", face=CF, body=ltr_card("Ar–X", "#7FD6C9")),
 "g_alkyl": dict(words=["المجموعة البديلة (الألكيل)", "مجموعة الألكيل", "المجموعة البديلة"], only=S, anim="bob", face=CF, body=ltr_card("–CH₃", "#F28AA8")),
 "c_ethene": dict(words=["الإيثين", "الألكينات"], only=S, anim="bob", face=CF, body=ltr_card("C₂H₄", "#F5D547")),
 "c_ethyne": dict(words=["الإيثاين", "الألكاينات"], only=S, anim="bob", face=CF, body=ltr_card("C₂H₂", "#9FD0F5")),
 "c_homologous": dict(words=["السلسلة المتجانسة", "الألكانات"], only=S, anim="bob", face=CF, body=ltr_card("CₙH₂ₙ₊₂", "#B58BD9")),
 "r_addition": dict(words=["الهدرجة", "الهلجنة", "الإماهة", "نزع الهيدروجين", "تفاعلات الإضافة"], only=S, anim="bob", face=CF, body=ltr_card("C=C + H₂", "#7FD6C9")),
 "eq_balanced": dict(words=["المعادلة الموزونة", "المعادلة اللفظية", "المواد المتفاعلة", "المواد الناتجة", "حساب كمية الناتج", "وزن المعادلات", "المعادلة الكيميائية"], only=S, anim="bob", face=CF, body=ltr_card("2H₂+O₂→2H₂O", "#F5D547")),
 "coefficient": dict(words=["المعامل", "المعاملات", "معاملات المعادلة"], only=("chemistry",), anim="bob", face=CF, body=ltr_card("2 H₂O", "#B58BD9")),
 "u_molarity": dict(words=["المولارية", "التركيز المولاري"], only=S, anim="bob", face=CF, body=ltr_card("mol/L", "#9FD0F5")),
 "u_molality": dict(words=["المولالية"], only=S, anim="bob", face=CF, body=ltr_card("mol/kg", "#B58BD9")),
 "u_joule": dict(words=["الجول", "وحدة الجول"], only=S, anim="bob", face=CF, body=ltr_card("J", "#F28AA8")),
 "u_calorie": dict(words=["السعر", "السعرة", "الكالوري"], only=S, anim="bob", face=CF, body=ltr_card("cal", "#F5D547")),
 "u_stp": dict(words=["الظروف المعيارية STP", "الظروف المعيارية", "STP"], only=S, anim="bob", face=CF, body=ltr_card("STP", "#7FD6C9")),
 "k_planck": dict(words=["ثابت بلانك", "الكم", "الكمّ", "طاقة الكم"], only=S, anim="bob", face=CF, body=ltr_card("E = hν", "#9FD0F5")),
 "k_debroglie": dict(words=["معادلة دي برولي", "الطبيعة الموجية للإلكترون"], only=S, anim="bob", face=CF, body=ltr_card("λ = h/mv", "#B58BD9")),
 "n_atomic": dict(words=["العدد الذري", "الأعداد الذرية"], only=S, anim="bob", face=CF, body=ltr_card("Z", "#F28AA8")),
 "n_mass": dict(words=["العدد الكتلي", "الأعداد الكتلية"], only=S, anim="bob", face=CF, body=ltr_card("A", "#F5D547")),
 "n_amu": dict(words=["وحدة الكتل الذرية", "الكتلة الذرية", "متوسط الكتلة الذرية"], only=S, anim="bob", face=CF, body=ltr_card("amu", "#7FD6C9")),
 "w_gamma": dict(words=["أشعة جاما", "إشعاع جاما"], only=S, anim="bob", face=CF, body=ltr_card("γ", "#B58BD9")),
 "w_uv": dict(words=["الأشعة فوق البنفسجية"], only=S, anim="bob", face=CF, body=ltr_card("UV", "#9FD0F5")),
 "a_oxy": dict(words=["الأحماض الأكسجينية"], only=S, anim="bob", face=CF, body=ltr_card("HNO₃", "#F28AA8")),
 "a_binary": dict(words=["الأحماض الثنائية", "الأحماض الهيدروجينية"], only=S, anim="bob", face=CF, body=ltr_card("HCl", "#F5D547")),
 "a_poly": dict(words=["الأحماض أحادية البروتون ومتعددة البروتونات", "الأحماض متعددة البروتونات"], only=S, anim="bob", face=CF, body=ltr_card("H₂SO₄", "#7FD6C9")),
 "resonance": dict(words=["الرنين", "التراكيب الرنينية"], only=S, anim="bob", face=CF, body=ltr_card("A↔B", "#9FD0F5")),
}
ALIAS_ONLY = ("science",)
ALIASES = {
    "التصبن": "body.hygiene", "النموذج": "chem.model", "الصابون والمنظفات": "body.hygiene", "البادئات": "chem.g_alkyl", "المجموعة": "mat.periodic", "الدورة": "mat.periodic",
    "الإنزيم": "bio.enzyme", "المثبط": "bio.enzyme", "الموقع النشط": "bio.enzyme", "ATP": "bio.atp", "RNA": "bio.rna", "النيوكليوتيد": "bio.nucleotide",
    "القواعد النيتروجينية": "bio.nucleotide", "الخاصية الأسموزية": "bio.osmosis", "المواد المسرطنة": "bio.cancer", "الفرضية": "bio.hypothesis",
    "المتغير المستقل": "bio.variables", "المتغير التابع": "bio.variables",
}
