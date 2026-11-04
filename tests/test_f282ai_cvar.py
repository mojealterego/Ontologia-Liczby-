import unittest
from fractions import Fraction as F

def cvar(losses, probs, alpha):
    assert F(0) <= alpha < F(1)
    assert sum(probs) == 1 and all(p > 0 for p in probs)
    # Convex piecewise-linear objective attains minimum at an observed loss.
    return min(t + sum(p * max(F(0), l-t) for p,l in zip(probs,losses))/(1-alpha) for t in losses)

class TestF282AI(unittest.TestCase):
    def test_mean(self):
        self.assertEqual(cvar([F(-2),F(4)],[F(1,2)]*2,F(0)),F(1))
    def test_tail(self):
        self.assertEqual(cvar([F(0),F(100)],[F(99,100),F(1,100)],F(99,100)),F(100))
    def test_partial_atom(self):
        self.assertEqual(cvar([F(0),F(100)],[F(99,100),F(1,100)],F(95,100)),F(20))
    def test_examples(self):
        self.assertEqual(cvar([F(0),F(10)],[F(3,4),F(1,4)],F(1,2)),F(5))
        self.assertEqual(cvar([F(0),F(10)],[F(3,4),F(1,4)],F(3,4)),F(10))
    def test_translation(self):
        for k in range(-5,6):
            l=[F(-2),F(4)]
            self.assertEqual(cvar([x+k for x in l],[F(1,2)]*2,F(1,2)),cvar(l,[F(1,2)]*2,F(1,2))+k)
    def test_monotone_alpha(self):
        losses=[F(-3),F(0),F(7)]
        p=[F(1,4),F(1,2),F(1,4)]
        vals=[cvar(losses,p,F(i,20)) for i in range(20)]
        self.assertEqual(vals,sorted(vals))
    def test_lipschitz(self):
        p=[F(1,3)]*3
        for a in range(-3,4):
            l=[F(a),F(0),F(2)]
            m=[v+F(1,4) for v in l]
            self.assertLessEqual(abs(cvar(l,p,F(2,3))-cvar(m,p,F(2,3))),F(1,4))
    def test_minimax(self):
        p=[F(1,2)]*2
        vals=[cvar([F(x,10),F(2)-F(x,10)],p,F(1,2)) for x in range(21)]
        self.assertEqual(min(vals),F(1))
        self.assertEqual(vals.index(min(vals)),10)

if __name__ == "__main__":
    unittest.main()
