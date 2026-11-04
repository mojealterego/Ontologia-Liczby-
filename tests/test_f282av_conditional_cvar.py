import unittest
from fractions import Fraction as F

def cvar(losses, masses, alpha):
    h = 1 - alpha
    assert F(0) < h <= 1 and sum(masses) == 1
    remaining, total = h, F(0)
    for x, p in sorted(zip(losses, masses), reverse=True):
        take = min(p, remaining)
        total += take*x
        remaining -= take
        if remaining == 0:
            break
    return total/h

def conditional(losses, masses, blocks):
    result = list(losses)
    for block in blocks:
        w = sum(masses[i] for i in block)
        mean = sum(masses[i]*losses[i] for i in block)/w
        for i in block:
            result[i] = mean
    return result

class TestF282AV(unittest.TestCase):
    def test_contraction(self):
        p = [F(1,4), F(1,4), F(1,2)]
        for a in [F(0), F(1,4), F(1,2), F(3,4)]:
            for x in range(-2, 3):
                for y in range(-2, 3):
                    z = [F(x), F(y), F(1)]
                    self.assertLessEqual(cvar(conditional(z,p,[[0,1],[2]]),p,a), cvar(z,p,a))
    def test_expectation_bounds(self):
        p=[F(1,4),F(3,4)]
        x=[F(8),F(0)]
        self.assertEqual(cvar(x,p,F(1,2)),4)
        self.assertEqual(cvar(conditional(x,p,[[0,1]]),p,F(1,2)),2)
    def test_diversification(self):
        p=[F(1,2)]*2
        x=[F(2),F(0)]
        y=[F(0),F(2)]
        a=F(1,2)
        self.assertEqual(cvar(x,p,a)+cvar(y,p,a)-cvar([u+v for u,v in zip(x,y)],p,a),2)
    def test_common_maximizer(self):
        p=[F(1,2)]*2
        self.assertEqual(cvar([F(2),F(0)],p,F(1,2))+cvar([F(4),F(0)],p,F(1,2))-cvar([F(6),F(0)],p,F(1,2)),0)
    def test_stability(self):
        p=[F(1,2)]*2
        self.assertEqual(abs(cvar([F(1),F(5)],p,F(1,2))-cvar([F(2),F(4)],p,F(1,2))),1)
    def test_translation(self):
        p=[F(1,2)]*2
        self.assertEqual(cvar([F(3),F(7)],p,F(1,2)),cvar([F(1),F(5)],p,F(1,2))+2)

if __name__ == "__main__":
    unittest.main()
