import unittest
from fractions import Fraction
from math import cos, pi, sin

class Transition(unittest.TestCase):
    def test_telescope_exact(self):
        for N in range(1, 65):
            y = Fraction(3, 7)
            for k in range(N):
                y = Fraction(k + 1, k + 2) * y + 1
            target = (Fraction(3, 7) + sum(range(2, N + 2))) / Fraction(N + 1)
            self.assertEqual(y, target)

    def test_profile(self):
        for lam in (0, pi, 2 * pi, 3.0):
            H = .5 if lam == 0 else sin(lam) / lam + (cos(lam) - 1) / lam ** 2
            for N in (50, 100, 500, 2000):
                y = sum((k + 2) * cos(k * lam / N) for k in range(N)) / (N * (N + 1))
                self.assertLessEqual(abs(y - H), (4 + abs(lam)) / N + 1e-12)

    def test_initial_scale(self):
        for N in (10, 100, 1000):
            y = (N * N + N * (N + 3) / 2) / (N * (N + 1))
            self.assertLess(abs(y - 1.5), 3 / N)

if __name__ == "__main__":
    unittest.main()
