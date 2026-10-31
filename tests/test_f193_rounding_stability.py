"""F19.3: exact rational tests for nearest-even quantization and error bounds.

Finite checks supplement, but do not replace, mathematical proofs.
"""
from __future__ import annotations

from fractions import Fraction as F
from itertools import product
from pathlib import Path
import re
import unittest

SOURCE = Path(__file__).resolve().parents[1] / (
    "manuscript/tom-01/F19/F19.3_UZUPELNIENIE_ZAOKRAGLENIE_I_STABILNOSC.md"
)
if not SOURCE.is_file():
    SOURCE = Path(__file__).with_name("F19.3_UZUPELNIENIE_ZAOKRAGLENIE_I_STABILNOSC.md")


def nearest_even(x: F, h: F) -> F:
    if h <= 0:
        raise ValueError("positive step required")
    t = x / h
    n = t.numerator // t.denominator
    r = t - n
    return h * (n + (r > F(1, 2) or (r == F(1, 2) and n % 2 != 0)))


def nearest_even_integer_certificate(a: int, q: int, u: int, v: int) -> F:
    if q <= 0 or u <= 0 or v <= 0:
        raise ValueError("q,u,v must be positive")
    n, r = divmod(a * v, q * u)
    return F(u, v) * (n + (2 * r > q * u or (2 * r == q * u and n % 2 != 0)))


def lower(x: F, h: F) -> F:
    return (x // h) * h


def upper(x: F, h: F) -> F:
    return -lower(-x, h)


def margin(x: F, h: F) -> F:
    t = x / h
    n = t.numerator // t.denominator
    r = t - n
    return h * abs(r - F(1, 2))


class F193Tests(unittest.TestCase):
    def test_01_source_numbering_and_proofs(self):
        src = SOURCE.read_text(encoding="utf-8")
        for tag, count in (("D", 8), ("T", 12), ("K", 6), ("Z", 12)):
            actual = [int(n) for n in re.findall(rf"\*\*{tag}(\d+)\b", src)]
            self.assertEqual(actual, list(range(1, count + 1)), tag)
        self.assertEqual(len(re.findall(r"\*Dowód\.\*", src)), 12)
        self.assertEqual(len(re.findall(r"\*\*Rozwiązanie:\*\*", src)), 12)
        self.assertIn("585/1222", src)

    def test_02_integer_certificate_negative_and_positive(self):
        for a in range(-59, 60):
            for q in range(1, 19):
                for u, v in ((1, 1), (1, 10), (1, 100), (3, 8), (2, 3)):
                    self.assertEqual(nearest_even(F(a, q), F(u, v)),
                                     nearest_even_integer_certificate(a, q, u, v))

    def test_03_error_bound_and_exact_ties(self):
        for h in (F(1), F(1, 10), F(3, 7)):
            for k in range(-40, 41):
                x = h * F(k, 8)
                e = abs(nearest_even(x, h) - x)
                self.assertLessEqual(e, h / 2)
                self.assertEqual(e == h / 2, x / h - F(x // h) == F(1, 2))

    def test_04_monotonicity_oddness_and_idempotence(self):
        for h in (F(1), F(1, 7), F(3, 10)):
            xs = [F(i, 20) for i in range(-160, 161)]
            rounded = [nearest_even(x, h) for x in xs]
            self.assertEqual(rounded, sorted(rounded))
            for x, y in zip(xs, rounded):
                self.assertEqual(nearest_even(-x, h), -y)
                self.assertEqual(nearest_even(y, h), y)

    def test_05_even_translation_and_nontie_odd_translation(self):
        h = F(3, 10)
        for x in (F(-17, 10), F(-3, 20), F(1, 7), F(7, 4)):
            for m in range(-8, 9):
                self.assertEqual(nearest_even(x + 2 * m * h, h),
                                 nearest_even(x, h) + 2 * m * h)
                if margin(x, h) != 0:
                    self.assertEqual(nearest_even(x + m * h, h),
                                     nearest_even(x, h) + m * h)
        self.assertNotEqual(nearest_even(F(3, 2), F(1)), nearest_even(F(1, 2), F(1)) + 1)

    def test_06_exact_cells(self):
        h = F(1, 10)
        for n in range(-15, 16):
            a, b = h * F(2 * n - 1, 2), h * F(2 * n + 1, 2)
            self.assertEqual(nearest_even((a + b) / 2, h), n * h)
            self.assertEqual(nearest_even(a, h) == n * h, n % 2 == 0)
            self.assertEqual(nearest_even(b, h) == n * h, n % 2 == 0)

    def test_07_stability_margin(self):
        h = F(1, 10)
        for x in (F(i, 1000) for i in range(-500, 501)):
            d = margin(x, h)
            if d == 0:
                continue
            for shift in (-d / 2, d / 2):
                self.assertEqual(nearest_even(x + shift, h), nearest_even(x, h))

    def test_08_double_rounding_and_sufficient_condition(self):
        h, g, x = F(1, 10), F(1, 100), F(251, 1000)
        self.assertEqual(nearest_even(x, h), F(3, 10))
        self.assertEqual(nearest_even(nearest_even(x, g), h), F(1, 5))
        for x in (F(i, 1000) for i in range(-700, 701)):
            y = nearest_even(x, g)
            if margin(x, h) and abs(y - x) < margin(x, h):
                self.assertEqual(nearest_even(y, h), nearest_even(x, h))

    def test_09_relative_error_with_magnitude_bound(self):
        h = F(1, 10)
        for a in range(-200, 201):
            x = F(a, 1000)
            if abs(x) >= F(1, 20):
                self.assertLessEqual(abs(nearest_even(x, h) - x) / abs(x),
                                     h / (2 * F(1, 20)))
        self.assertEqual(abs(nearest_even(F(1, 40), h) - F(1, 40)) / F(1, 40), 1)

    def test_10_subtraction_condition_exact_sharpness(self):
        eps = F(1, 10000)
        for x, y in ((F(1), F(999999, 1000000)), (F(-3), F(7, 2)),
                     (F(7, 4), F(5, 4)), (F(-2), F(-3))):
            kappa = (abs(x) + abs(y)) / abs(x - y)
            dx, dy = eps * abs(x), -eps * abs(y)
            error = abs((x + dx) - (y + dy) - (x - y)) / abs(x - y)
            self.assertEqual(error, eps * kappa)

    def test_11_outward_enclosure_and_minimality(self):
        h = F(1, 7)
        vals = [F(i, 11) for i in range(-15, 16)]
        for a in vals:
            for b in vals:
                if a > b:
                    continue
                l, u = lower(a, h), upper(b, h)
                self.assertLessEqual(l, a)
                self.assertGreaterEqual(u, b)
                self.assertLess(u - l - (b - a), 2 * h)
                self.assertGreater(l + h, a)
                self.assertLess(u - h, b)

    def test_12_accumulation_bound(self):
        h = F(1)
        for entries in product((F(49, 100), F(-49, 100), F(51, 100)), repeat=5):
            s = q = F(0)
            for n, a in enumerate(entries, 1):
                s += a
                q = nearest_even(q + a, h)
                self.assertLessEqual(abs(q - s), n * h / 2)
        self.assertEqual(sum((F(49, 100),) * 3), F(147, 100))

    def test_13_rounded_addition_bound(self):
        h = F(1)
        for x in (F(i, 20) for i in range(-30, 31)):
            for y in (F(j, 20) for j in range(-30, 31)):
                lhs = nearest_even(nearest_even(x, h) + nearest_even(y, h), h)
                self.assertLessEqual(abs(lhs - (x + y)), h)

    def test_14_nonadditivity_and_nonexpansiveness_counterexamples(self):
        x, y = F(49, 100), F(51, 100)
        self.assertNotEqual(nearest_even(x + x, F(1)), 2 * nearest_even(x, F(1)))
        self.assertGreater(abs(nearest_even(y, F(1)) - nearest_even(x, F(1))), abs(y - x))

    def test_15_naive_interval_rounding_failure(self):
        a, b = F(1, 10), F(1, 5)
        self.assertEqual((nearest_even(a, F(1)), nearest_even(b, F(1))), (0, 0))
        self.assertEqual((lower(a, F(1)), upper(b, F(1))), (0, 1))

    def test_16_quoted_worked_examples(self):
        self.assertEqual(nearest_even(F(-1, 4), F(1, 10)), F(-1, 5))
        self.assertEqual(nearest_even(F(249, 1000), F(1, 100)), F(1, 4))
        self.assertEqual(margin(F(13, 50), F(1, 10)), F(1, 100))
        self.assertEqual(nearest_even(F(5, 8), F(1, 100)), F(31, 50))
        self.assertEqual(lower(F(7, 50), F(1, 10)), F(1, 10))
        self.assertEqual(upper(F(17, 50), F(1, 10)), F(2, 5))

    def test_17_invalid_steps(self):
        for h in (F(0), F(-1, 10)):
            with self.assertRaises(ValueError):
                nearest_even(F(1), h)
        for params in ((1, 0, 1, 10), (1, 2, 0, 10), (1, 2, 1, 0)):
            with self.assertRaises(ValueError):
                nearest_even_integer_certificate(*params)


if __name__ == "__main__":
    unittest.main()
