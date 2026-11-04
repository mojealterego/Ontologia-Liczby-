import unittest
from fractions import Fraction as F
from itertools import product

def cvar(losses, probs, alpha):
    h = 1 - alpha
    assert h > 0 and sum(probs) == 1 and all(p >= 0 for p in probs)
    remaining = h
    total = F(0)
    for loss, p in sorted(zip(losses, probs), reverse=True):
        w = min(remaining, p)
        total += w * loss
        remaining -= w
    assert remaining == 0
    return total / h

def primal_cvar(losses, probs, alpha):
    h = 1 - alpha
    return min(t + sum(p * max(F(0), x - t) for x, p in zip(losses, probs)) / h
               for t in sorted(set(losses)))

class TailTests(unittest.TestCase):
    def test_exact_minimization(self):
        for n in range(1, 5):
            for losses in product((F(-1), F(0), F(2)), repeat=n):
                for weights in product((0, 1, 2), repeat=n):
                    if sum(weights) == 0:
                        continue
                    probs = tuple(F(w, sum(weights)) for w in weights)
                    for alpha in (F(0), F(1, 3), F(3, 4)):
                        self.assertEqual(cvar(losses, probs, alpha), primal_cvar(losses, probs, alpha))

    def test_ties(self):
        self.assertEqual(cvar((F(1), F(1), F(5)), (F(1, 4), F(1, 2), F(1, 4)), F(1, 2)), F(3))

    def test_zero_mass(self):
        self.assertEqual(cvar((F(100), F(0)), (F(0), F(1)), F(9, 10)), F(0))

    def test_permutation(self):
        self.assertEqual(cvar((F(2), F(8), F(0)), (F(1, 4), F(1, 4), F(1, 2)), F(1, 2)), F(5))

    def test_translation_scale(self):
        x = (F(-1), F(2), F(7))
        p = (F(1, 2), F(1, 3), F(1, 6))
        a = F(2, 3)
        self.assertEqual(cvar(tuple(v + 3 for v in x), p, a), cvar(x, p, a) + 3)
        self.assertEqual(cvar(tuple(2 * v for v in x), p, a), 2 * cvar(x, p, a))

    def test_monotone_alpha(self):
        x = (F(-1), F(2), F(7))
        p = (F(1, 2), F(1, 3), F(1, 6))
        seq = [cvar(x, p, F(k, 10)) for k in range(10)]
        self.assertEqual(seq, sorted(seq))

if __name__ == "__main__":
    unittest.main()
