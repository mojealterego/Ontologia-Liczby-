from fractions import Fraction as F
import unittest

def q(gaps, supports):
    assert len(gaps) == len(supports) and all(g > 0 for g in gaps)
    return max([F(0)] + [max(F(0), s) / g for s, g in zip(supports, gaps)])

class TestHZ(unittest.TestCase):
    def test_joint_bound(self):
        n = 0
        for a in range(1, 12):
            for b in range(1, 12):
                for e in range(-3, 4):
                    g, delta = F(a, 3), F(e, 20)
                    if g + delta <= 0:
                        continue
                    s = F(b - 5, 3)
                    old = q([g], [s])
                    new = q([g + delta], [s + delta])
                    E = abs(delta)
                    m = min(g, g + delta)
                    B = E / m + max(F(0), s) * E / (g * m)
                    self.assertLessEqual(abs(new - old), B)
                    n += 1
        self.assertEqual(n, 847)

    def test_zero_and_finite_radius(self):
        self.assertEqual(q([F(2)], [F(-1)]), 0)
        self.assertEqual(q([F(2)], [F(4)]), 2)

    def test_gap_collapse(self):
        self.assertEqual(q([F(1, 100)], [F(1)]), 100)

if __name__ == "__main__":
    unittest.main()
