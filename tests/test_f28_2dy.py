"""Exact rational regression checks for F28.2-DY."""
from fractions import Fraction as F
from itertools import combinations_with_replacement
import unittest

def variance(values):
    n = len(values)
    mean = sum(values, F(0)) / n
    return sum(((x - mean) ** 2 for x in values), F(0)) / n

def bounds(values):
    n = len(values)
    assert n % 2 == 0 and n > 0
    left, right = values[:n // 2], values[n // 2:]
    ml = sum(left, F(0)) / len(left)
    mr = sum(right, F(0)) / len(right)
    between = (ml - mr) ** 2 / 4
    span = (max(values) - min(values)) ** 2 / 4
    return between, variance(values), span

class QuantileBoundsTests(unittest.TestCase):
    def test_exact_enumeration(self):
        count = 0
        for n in (2, 4, 6, 8):
            for tup in combinations_with_replacement(range(5), n):
                values = [F(x) for x in tup]
                lower, error, upper = bounds(values)
                self.assertLessEqual(lower, error)
                self.assertLessEqual(error, upper)
                self.assertEqual(error, variance(values[:n//2]) / 2
                                 + variance(values[n//2:]) / 2 + lower)
                count += 1
        self.assertGreater(count, 500)

    def test_counterexample(self):
        values = [F(0), F(1), F(2), F(3)]
        self.assertEqual(bounds(values), (F(1), F(5, 4), F(9, 4)))

    def test_two_level(self):
        self.assertEqual(bounds([F(0), F(0), F(3), F(3)]),
                         (F(9, 4), F(9, 4), F(9, 4)))

    def test_linear_example(self):
        values = [F(1, 8), F(3, 8), F(5, 8), F(7, 8)]
        lower, error, upper = bounds(values)
        self.assertEqual(lower, F(1, 16))
        self.assertEqual(error, F(5, 64))
        self.assertEqual(upper, F(9, 64))

if __name__ == "__main__":
    unittest.main()
