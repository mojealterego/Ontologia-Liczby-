"""Finite, exact checks of selected claims in MSC 00A09; not a formal proof."""
import itertools
import math
import unittest
from fractions import Fraction


def bayes_positive(prevalence, sensitivity, specificity):
    numerator = sensitivity * prevalence
    denominator = numerator + (1 - specificity) * (1 - prevalence)
    if denominator <= 0:
        raise ValueError("positive-test probability must be positive")
    return numerator / denominator


def aggregate(successes, trials):
    if trials <= 0 or not (0 <= successes <= trials):
        raise ValueError("invalid denominator or success count")
    return Fraction(successes, trials)


class PopularizationMathematicsTests(unittest.TestCase):
    def test_t01_counterexample(self):
        self.assertTrue(all(n % 2 == 1 for n in [3, 5, 7, 9]))
        self.assertTrue(any(n > 1 and any(n % d == 0 for d in range(2, n)) for n in [3, 5, 7, 9]))

    def test_t02_exhaustive_finite(self):
        s = set(range(12))
        checked = {n for n in s if n * (n + 1) % 2 == 0}
        self.assertEqual(s, checked)

    def test_t03_finite_samples_cannot_identify_function(self):
        for n in range(1, 40):
            f = lambda k: 0
            g = lambda k, n=n: int(k == n)
            self.assertTrue(all(f(k) == g(k) for k in range(n)))
            self.assertNotEqual(f(n), g(n))

    def test_t04_opposite_percent_changes(self):
        for p in [Fraction(1, 100), Fraction(1, 10), Fraction(1, 2), Fraction(9, 10)]:
            self.assertEqual((1 + p) * (1 - p), 1 - p * p)
            self.assertLess((1 + p) * (1 - p), 1)

    def test_t05_percentage_points(self):
        p, q = Fraction(12, 100), Fraction(15, 100)
        self.assertEqual(100 * (q - p), 3)
        self.assertEqual((q - p) / p, Fraction(1, 4))

    def test_t06_rounding_bound(self):
        for n in range(0, 100001):
            u = n / 1000
            r = math.floor(u + 0.5)
            self.assertLessEqual(abs(u - r), 0.5 + 1e-12)

    def test_t07_log_ratio(self):
        for x, y in [(2, 20), (20, 200), (3, 30), (1, 1000)]:
            self.assertAlmostEqual(math.log10(x) - math.log10(y), math.log10(x / y))

    def test_t08_circle_area(self):
        self.assertEqual(Fraction(4 * 4, 2 * 2), 4)

    def test_t09_truncated_axis(self):
        self.assertEqual(Fraction(100 - 90, 95 - 90), 2)
        self.assertEqual(Fraction(100, 95), Fraction(20, 19))

    def test_t10_unit_dimension(self):
        distance_km = Fraction(150)
        time_hours = Fraction(5, 2)
        self.assertEqual(distance_km / time_hours, 60)

    def test_t11_bayes_base_rate(self):
        p, s, c = Fraction(1, 100), Fraction(99, 100), Fraction(95, 100)
        self.assertEqual(bayes_positive(p, s, c), Fraction(1, 6))

    def test_t11_rejects_impossible_positive(self):
        with self.assertRaises(ValueError):
            bayes_positive(Fraction(0), Fraction(0), Fraction(1))

    def test_t12_simpson(self):
        self.assertGreater(aggregate(9, 10), aggregate(80, 100))
        self.assertGreater(aggregate(10, 100), aggregate(0, 10))
        self.assertLess(aggregate(19, 110), aggregate(80, 110))

    def test_t13_bernoulli_variance_bound(self):
        for p in [Fraction(i, 100) for i in range(101)]:
            self.assertLessEqual(p * (1 - p), Fraction(1, 4))
        self.assertEqual(Fraction(1, 4 * 400) / Fraction(1, 10) ** 2, Fraction(1, 16))

    def test_t14_union_bound_by_exhaustive_sets(self):
        universe = set(range(6))
        subsets = [set(i for i in universe if mask & (1 << i)) for mask in range(64)]
        for a, b in itertools.product(subsets, repeat=2):
            self.assertLessEqual(len(a | b), len(a) + len(b))

    def test_k10_zero_events_possible(self):
        self.assertGreater(Fraction(99, 100) ** 10, 0)
        self.assertLess(Fraction(99, 100) ** 10, 1)

    def test_z15_pie_chart_angles(self):
        self.assertEqual(Fraction(25, 100) * 360, 90)
        self.assertEqual(Fraction(75, 100) * 360, 270)

    def test_invalid_denominator(self):
        for successes, trials in [(1, 0), (-1, 10), (11, 10)]:
            with self.assertRaises(ValueError):
                aggregate(successes, trials)


if __name__ == "__main__":
    unittest.main()
