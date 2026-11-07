import unittest
from fractions import Fraction

class CriticalResonance(unittest.TestCase):
    def test_exact_variation(self):
        count = 0
        for a in (1, 2, 3):
            for y0 in (-3, 0, 2):
                for p in (1, 2, 3, 4):
                    y = Fraction(y0)
                    history = []
                    for n in range(1, 25):
                        j = n - 1
                        u = Fraction(1, (j + 1) ** p)
                        history.append(u)
                        y = Fraction(n, n + a) * y + u
                        h = Fraction(1)
                        expected = Fraction(0)
                        for k in range(n - 1, -1, -1):
                            expected += h * history[k]
                            h *= Fraction(k + 1, k + 1 + a)
                        expected += h * y0
                        self.assertEqual(y, expected)
                        count += 1
        print("exact identities:", count)

    def test_closed_forms_a1(self):
        for n in range(1, 100):
            harmonic = sum((Fraction(1, k) for k in range(1, n + 1)), Fraction(0))
            y = Fraction(0)
            for j in range(n):
                y = Fraction(j + 1, j + 2) * y + Fraction(1, j + 1)
            self.assertEqual(y, Fraction(n, n + 1) + harmonic / Fraction(n + 1))

if __name__ == "__main__":
    unittest.main()
