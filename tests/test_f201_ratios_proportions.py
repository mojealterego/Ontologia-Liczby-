"""F20.1: exact-rational regression checks for ratios and proportions.

Finite model checks are evidence for examples, not a formal proof of the text.
"""
from __future__ import annotations

from fractions import Fraction as F
from itertools import product
from pathlib import Path
import re
import unittest

SOURCE = Path(__file__).resolve().parents[1] / "manuscript/tom-01/F20/F20.1_UZUPELNIENIE_STRUKTURALNE_PROPORCJE.md"


def det(a: F, b: F, c: F, d: F) -> F:
    return a * d - b * c


def split(total: F, m: F, n: F) -> tuple[F, F]:
    if total <= 0 or m <= 0 or n <= 0:
        raise ValueError("positive inputs required")
    return total * m / (m + n), total * n / (m + n)


def barycenter(x: F, y: F, m: F, n: F) -> F:
    if m <= 0 or n <= 0:
        raise ValueError("positive weights required")
    return (m * x + n * y) / (m + n)


def ratio_error(a: F, b: F, da: F, db: F) -> F:
    if b == 0 or b + db == 0:
        raise ZeroDivisionError("undefined ratio")
    return (a + da) / (b + db) - a / b


class F201Tests(unittest.TestCase):
    def test_01_source_numbering_proofs_and_solutions(self):
        src = SOURCE.read_text(encoding="utf-8")
        for tag, count in (("D", 8), ("T", 10), ("K", 6), ("Z", 12)):
            actual = [int(n) for n in re.findall(rf"\*\*{tag}(\d+)\b", src)]
            self.assertEqual(actual, list(range(1, count + 1)), tag)
        self.assertEqual(len(re.findall(r"\*Dowód\.\*", src)), 10)
        self.assertEqual(len(re.findall(r"\*\*Rozwiązanie:\*\*", src)), 12)
        self.assertIn("585/1222", src)
        self.assertIn("nie jest to wydanie 0.20", src)

    def test_02_cross_multiplication_requires_nonzero_denominators(self):
        vals = [F(x) for x in range(-3, 4)]
        for a, b, c, d in product(vals, repeat=4):
            if b and d:
                self.assertEqual(a / b == c / d, det(a, b, c, d) == 0)
        self.assertEqual(det(F(0), F(0), F(1), F(0)), 0)

    def test_03_positive_scaling_equivalence(self):
        for a, b, t in product(range(1, 8), repeat=3):
            c, d = F(t * a), F(t * b)
            self.assertEqual(F(a, b), c / d)
            self.assertEqual(F(d, b), F(t))
        self.assertFalse(any(F(t) * 1 == -1 for t in range(1, 8)))

    def test_04_unique_partition(self):
        for s, m, n in product(range(1, 15), repeat=3):
            x, y = split(F(s), F(m), F(n))
            self.assertEqual(x + y, s)
            self.assertEqual(x / y, F(m, n))
            self.assertGreater(x, 0)
            self.assertGreater(y, 0)
        with self.assertRaises(ValueError):
            split(F(1), F(0), F(1))

    def test_05_chain_of_ratios(self):
        for m, n, p, q in product(range(1, 7), repeat=4):
            b = F(p * n)
            a = b * F(m, n)
            c = b * F(q, p)
            self.assertEqual(a / c, F(m * p, n * q))

    def test_06_rank_one_determinant(self):
        for c, d in product(range(-3, 4), repeat=2):
            if c == d == 0:
                continue
            for num in range(-4, 5):
                t = F(num, 3)
                a, b = t * c, t * d
                self.assertEqual(det(a, b, F(c), F(d)), 0)
                recovered = a / c if c else b / d
                self.assertEqual(recovered, t)

    def test_07_barycentric_bounds(self):
        for x, y, m, n in product(range(-4, 5), range(-4, 5), range(1, 7), range(1, 7)):
            z = barycenter(F(x), F(y), F(m), F(n))
            self.assertLessEqual(min(x, y), z)
            self.assertLessEqual(z, max(x, y))
            if x != y:
                self.assertLess(min(x, y), z)
                self.assertLess(z, max(x, y))

    def test_08_homogeneity(self):
        for k, t, x in product(range(-5, 6), range(1, 8), range(1, 8)):
            self.assertEqual(F(k) * (F(t) * F(x)), F(t) * (F(k) * F(x)))
        self.assertEqual(F(7, 3) * F(9, 14), F(3, 2))

    def test_09_mixture_fraction_and_bounds(self):
        for m1, m2 in product(range(1, 8), repeat=2):
            for w1, w2 in product((F(0), F(1, 10), F(1, 2), F(4, 5), F(1)), repeat=2):
                w = (m1 * w1 + m2 * w2) / (m1 + m2)
                self.assertLessEqual(min(w1, w2), w)
                self.assertLessEqual(w, max(w1, w2))
        self.assertEqual((F(200) * F(1, 10) + F(300) * F(1, 5)) / 500, F(4, 25))

    def test_10_quotient_perturbation_identity(self):
        for a, b, da, db in product(range(-3, 4), range(-4, 5), range(-2, 3), range(-2, 3)):
            if not b or not b + db:
                continue
            a, b, da, db = F(a), F(b), F(da, 10), F(db, 10)
            actual = ratio_error(a, b, da, db)
            expected = (b * da - a * db) / (b * (b + db))
            self.assertEqual(actual, expected)
            if abs(db) < abs(b):
                bound = (abs(b) * abs(da) + abs(a) * abs(db)) / (abs(b) * (abs(b) - abs(db)))
                self.assertLessEqual(abs(actual), bound)

    def test_11_affine_nonproportionality(self):
        self.assertEqual(F(2 * 1 + 1, 1), F(3))
        self.assertEqual(F(2 * 2 + 1, 2), F(5, 2))
        self.assertNotEqual(F(3), F(5, 2))
        self.assertEqual(3 * 1 + 2, 5)
        self.assertEqual(3 * 2 + 2, 8)

    def test_12_worked_examples_exact(self):
        self.assertEqual(det(F(14), F(21), F(10), F(15)), 0)
        self.assertEqual(split(F(360), F(7), F(11)), (F(140), F(220)))
        self.assertEqual(split(F(91), F(3), F(4)), (F(39), F(52)))
        self.assertEqual(barycenter(F(5), F(15), F(2), F(3)), F(11))
        self.assertEqual(ratio_error(F(3), F(4), F(1, 10), F(-1, 5)), F(5, 76))
        self.assertEqual((F(10) + F(3, 10) * 100) / 200, F(1, 5))


if __name__ == "__main__":
    unittest.main()
