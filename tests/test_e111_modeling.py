"""E1-11: exact arithmetic checks for selected modeling claims.
Run: python3 -m unittest discover -s tests -p 'test_e111_modeling.py' -v
No third-party dependencies; these checks do not constitute formal proof review.
"""
from fractions import Fraction as F
import unittest


def affine_two_points(x1, y1, x2, y2):
    if x1 == x2:
        raise ValueError("distinct abscissas required")
    a = F(y2 - y1, x2 - x1)
    b = F(y1) - a * x1
    return a, b


def regression(points):
    n = len(points)
    if n < 2:
        raise ValueError("at least two observations")
    xb = sum(F(x) for x, _ in points) / n
    yb = sum(F(y) for _, y in points) / n
    denom = sum((F(x) - xb) ** 2 for x, _ in points)
    if denom == 0:
        raise ValueError("x values must not all be equal")
    a = sum((F(x) - xb) * (F(y) - yb) for x, y in points) / denom
    b = yb - a * xb
    return a, b


class TestModeling(unittest.TestCase):
    def test_t1_affine_unique(self):
        self.assertEqual(affine_two_points(1, 5, 4, 14), (F(3), F(2)))

    def test_t1_reject_duplicate_x(self):
        with self.assertRaises(ValueError):
            affine_two_points(1, 5, 1, 7)

    def test_t2_proportional(self):
        for x in range(-5, 6):
            self.assertEqual(3 * x, F(3) * x)

    def test_t4_inverse(self):
        for x in range(1, 50):
            self.assertEqual(x * F(60, x), 60)

    def test_t5_mixture(self):
        self.assertEqual((2 * F(1, 10) + 3 * F(1, 5)) / 5, F(4, 25))

    def test_t6_convex_bounds(self):
        for a in range(0, 11):
            for b in range(0, 11):
                mix = (2 * F(a, 10) + 3 * F(b, 10)) / 5
                self.assertLessEqual(min(F(a, 10), F(b, 10)), mix)
                self.assertLessEqual(mix, max(F(a, 10), F(b, 10)))

    def test_t8_units(self):
        self.assertEqual(F(72, 1) / F(36, 10), 20)

    def test_t9_breakeven(self):
        for q in range(0, 101):
            self.assertEqual((20 * q - (400 + 12 * q)) >= 0, q >= 50)

    def test_t11_error_bound(self):
        for delta in range(-10, 11):
            x = F(4) + F(delta, 100)
            self.assertLessEqual(abs((4 * x + 2) - (4 * 4 + 2)), F(2, 5))

    def test_t13_mean_least_squares(self):
        ys = [F(2), F(4), F(9)]
        s = lambda c: sum((y - c) ** 2 for y in ys)
        self.assertEqual(s(F(5)), 26)
        for n in range(-10, 101):
            self.assertGreaterEqual(s(F(n, 10)), s(F(5)))

    def test_t14_regression(self):
        self.assertEqual(regression([(0, 1), (1, 2), (2, 5)]), (F(2), F(2, 3)))

    def test_t15_t16_residuals(self):
        points = [(0, 1), (1, 2), (2, 5)]
        a, b = regression(points)
        residuals = [F(y) - a * x - b for x, y in points]
        self.assertEqual(residuals, [F(1, 3), F(-2, 3), F(1, 3)])
        self.assertEqual(sum(residuals), 0)
        self.assertEqual(sum(x * r for (x, _), r in zip(points, residuals)), 0)
        self.assertEqual(sum(r * r for r in residuals), F(2, 3))

    def test_t17_geometric(self):
        x = F(3)
        for n in range(20):
            self.assertEqual(x, 3 * 2 ** n)
            x *= 2

    def test_t18_arithmetic(self):
        x = F(25)
        for n in range(6):
            self.assertEqual(x, 25 - 4 * n)
            x -= 4

    def test_t20_nonidentifiability(self):
        for c in range(-10, 11):
            f = lambda x: 2 * x + c * (x - 1) * (x - 2)
            self.assertEqual(f(1), 2)
            self.assertEqual(f(2), 4)
        self.assertNotEqual(2 * 3, 2 * 3 + (3 - 1) * (3 - 2))

    def test_t21_balance(self):
        self.assertEqual(10 + sum([3, 2]) - sum([1, 4]), 10)

    def test_p4_evaporation(self):
        solute = 2 * F(15, 100) + 3 * F(25, 100)
        self.assertEqual(solute / 4, F(2625, 10000))

    def test_z33_growth(self):
        self.assertEqual(F(1000) * F(105, 100) ** 2, F(2205, 2))

    def test_k4_equal_distance_average_speed(self):
        distance = F(60)
        total_time = distance / 30 + distance / 60
        self.assertEqual(2 * distance / total_time, 40)

    def test_p1_tariffs(self):
        for q in range(0, 50):
            self.assertEqual(10 + 2 * q <= 4 + 3 * q, q >= 6)


if __name__ == "__main__":
    unittest.main()
