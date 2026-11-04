from fractions import Fraction as F
import unittest

def cvar(p, x, alpha):
    h = 1 - alpha
    assert F(0) <= alpha < 1 and sum(p) == 1
    ordered = sorted(zip(x, p), reverse=True)
    remain = h
    value = F(0)
    for loss, mass in ordered:
        take = min(remain, mass)
        value += take * loss
        remain -= take
        if remain == 0:
            break
    return value / h

def aggregate(p, x, blocks):
    y = list(x)
    for block in blocks:
        mass = sum((p[i] for i in block), F(0))
        mean = sum((p[i] * x[i] for i in block), F(0)) / mass
        for i in block:
            y[i] = mean
    return y

class TestAggregationGap(unittest.TestCase):
    def test_two_point_exact(self):
        for r in [F(1,4), F(1,2), F(3,4)]:
            p = [r, 1-r]
            x = [F(1), F(5)]
            for alpha in [F(0), F(1,4), F(1,2), F(3,4)]:
                gap = cvar(p,x,alpha)-cvar(p,aggregate(p,x,[[0,1]]),alpha)
                expected = 4*(min(F(1),(1-r)/(1-alpha))-(1-r))
                self.assertEqual(gap, expected)
    def test_contraction(self):
        p = [F(1,6),F(1,3),F(1,2)]
        for a in range(-2,3):
            for b in range(-2,3):
                for c in range(-2,3):
                    x = list(map(F,[a,b,c]))
                    for alpha in [F(0),F(1,4),F(1,2),F(3,4)]:
                        self.assertLessEqual(cvar(p,aggregate(p,x,[[0,1],[2]]),alpha),cvar(p,x,alpha))
    def test_translation_scaling(self):
        p = [F(1,2)]*2
        x = [F(0),F(2)]
        for alpha in [F(0),F(1,4),F(1,2),F(3,4)]:
            gap = cvar(p,x,alpha)-cvar(p,aggregate(p,x,[[0,1]]),alpha)
            z = [3*v-7 for v in x]
            newgap = cvar(p,z,alpha)-cvar(p,aggregate(p,z,[[0,1]]),alpha)
            self.assertEqual(newgap,3*gap)
    def test_examples(self):
        p=[F(1,2),F(1,2)]
        x=[F(0),F(2)]
        self.assertEqual(cvar(p,x,F(1,4))-F(1),F(1,3))
        self.assertEqual(cvar(p,x,F(1,2))-F(1),F(1))
        self.assertEqual(cvar(p,x,F(0))-F(1),F(0))
    def test_nonadditivity(self):
        p=[F(1,2),F(1,2)]
        x=[F(0),F(2)]
        y=[F(2),F(0)]
        def gap(z):
            return cvar(p,z,F(1,2))-cvar(p,aggregate(p,z,[[0,1]]),F(1,2))
        self.assertEqual((gap(x),gap(y),gap([a+b for a,b in zip(x,y)])),(1,1,0))

if __name__ == "__main__":
    unittest.main()
