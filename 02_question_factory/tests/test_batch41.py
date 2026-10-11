"""🆕 batch 41 (Hareth: «الأشياء اللي بتقدر تسويها سويها»): the weakest subjects of the Saudi curriculum get their drawings —
biology and chemistry (the cell dividing, the nerves and the hormones, the shapes of molecules, the atom's models, the lab…, and CARDS
where the concept IS a symbol: «–OH», «C₆H₁₂O₆», «2H₂+O₂→2H₂O») — and a word that means two things never gets the wrong one.
python -m unittest tests.test_batch41"""
import os
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
import art_coverage  # noqa: E402
import art_library  # noqa: E402
import build_all_books  # noqa: E402
import explain_generator as eg  # noqa: E402
import offline_generator as og  # noqa: E402
from graph_reader import Graph  # noqa: E402


def icon(name, subject):
    return og.icon_for(name, "", subject)


class Batch41(unittest.TestCase):
    def test_the_library_is_clean_and_bigger(self):
        self.assertEqual(art_library.problems(), [])
        fams = {r["family"] for r in art_library.drawings().values()}
        self.assertTrue({"biology", "chemistry"} <= fams)
        self.assertGreaterEqual(len(art_library.drawings()), 800)

    def test_biology_and_chemistry_are_covered(self):
        res = art_coverage.measure(art_coverage.saudi_concepts())
        for sk in ("biology", "chemistry"):
            r = res[sk]
            self.assertGreaterEqual(r["own"] / len(r["names"]), 0.90, f"{sk}: most concepts have a drawing of their own (it was 47% / 57%)")
        n = sum(len(r["names"]) for r in res.values())
        self.assertGreaterEqual(sum(r["own"] for r in res.values()) / n, 0.75, "all subjects together")

    def test_the_drawings_mean_the_concept(self):
        for name, subject, want in (("الطور الاستوائي", "biology", "lib:bio.metaphase"), ("التشابك العصبي", "biology", "lib:bio.synapse"),
                                    ("الإنسولين", "biology", "lib:bio.hormone"), ("الحويصلات الهوائية", "biology", "lib:bio.alveoli"),
                                    ("الشكل رباعي الأوجه", "chemistry", "lib:chem.tetrahedral"), ("نموذج بور الذري", "chemistry", "lib:chem.bohr"),
                                    ("الكحول", "chemistry", "lib:chem.g_alcohol"), ("الصيغة الجزيئية", "chemistry", "lib:chem.f_molecular"),
                                    ("رباعي أوجه السيليكا", "earth science", "lib:chem.tetrahedral")):
            self.assertEqual(icon(name, subject), want, name)

    def test_a_word_with_two_meanings_never_gets_the_wrong_drawing(self):
        wrong = (("المحور", "science", "lib:bio.neuron"),                 # the Earth's axis (science grade 2), not an axon
                 ("المحور الرئيس", "physics", "lib:bio.neuron"),          # a lens's axis
                 ("العجلة والمحور", "science", "lib:bio.neuron"),         # wheel and axle
                 ("المعايرة", "physics", "lib:chem.titration"),          # calibrating an instrument, not a titration
                 ("الامتصاص", "science", "lib:bio.villi"),               # light being absorbed (science grade 5)
                 ("طيف الامتصاص", "physics", "lib:bio.villi"),
                 ("الأوتار المهتزة", "physics", "lib:bio.joint"),         # vibrating strings, not tendons
                 ("التداخل في الأغشية الرقيقة", "physics", "lib:bio.membrane"),
                 ("المكثف الكهربائي", "physics", "lib:chem.distillation"),  # a capacitor, not a condenser
                 ("معامل الانكسار", "physics", "lib:chem.eq_balanced"),
                 ("الإعصار القمعي", "science", "lib:chem.filtration"),    # a funnel-shaped tornado
                 ("المناطق القطبية", "science", "lib:chem.electronegativity"),  # the polar regions, not polarity
                 ("الترسيب", "earth science", "lib:chem.precipitate"),     # the sediments of a river
                 ("الأملاح المعدنية", "science", "lib:chem.salt_crystal"))   # the minerals in food
        for name, subject, bad in wrong:
            self.assertNotEqual(icon(name, subject), bad, name)
        self.assertEqual(icon("الامتصاص", "biology"), "lib:bio.villi", "…but in a biology book it IS the villi")

    def test_one_concept_one_drawing_the_old_ones_stay(self):
        for name, want in (("اللاسعات", "lib:sci.jellyfish"), ("طور الميدوسا", "lib:sci.jellyfish"), ("بطنية القدم", "lib:sci.snail"),
                           ("الديدان الحلقية", "lib:sci.worm"), ("شوكيات الجلد", "lib:sci.starfish")):
            self.assertEqual(icon(name, "science"), want, name)
        self.assertNotIn("bio.jellyfish", art_library.drawings(), "the jellyfish was drawn already: no second one")

    def test_the_twelve_books_did_not_change(self):
        used = set()
        for b in build_all_books.BOOKS:
            G = Graph.load(os.path.join(ROOT, b))
            for les in G.lessons():
                used |= set(eg._icons(G, les).values())
        self.assertFalse({k for k in used if k.startswith(("lib:bio.", "lib:chem."))}, "the 12 books keep their pictures (checked one by one: 0 of 107 changed)")


if __name__ == "__main__":
    unittest.main()
