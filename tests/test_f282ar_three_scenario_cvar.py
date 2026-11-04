"""Exact rational checks for F28.2-AR."""
import unittest
from fractions import Fraction as F

def cvar_three(losses, probabilities, alpha):
    assert len(losses) == len(probabilities) == 3
    assert F(0) <= alpha < F(1)
    assert sum(probabilities) == 1 and all(p >= 0 for p in probabilities)
    h = 1 - alpha
    remain = h
    total = F(0)
    for loss, probability in sorted(zip(losses, probabilities), reverse=True):
        take = min(remain, probability)
        total += take * loss
        remain -= take
    assert remain == 0
    return total / h

def closed(a, b, c, pa, pb, pc, alpha):
    assert a < b < c and pa + pb + pc == 1
    h = 1 - alpha
    if h <= pc:
        return c
    if h <= pc + pb:
        return b + (c-b)*pc/h
    return a + ((b-a)*pb + (c-a)*pc)/h

class TestThreeScenarioCVaR(unittest.TestCase):
    def test_formula_grid(self):
        for pa in [F(i, 8) for i in range(9)]:
            for pb in [F(j, 8) for j in range(9) if pa + F(j, 8) <= 1]:
                pc = 1-pa-pb
                for alpha in [F(k, 20) for k in range(20)]:
                    self.assertEqual(cvar_three((F(0), F(2), F(8)), (pa,pb,pc),alpha),
                                     closed(F(0),F(2),F(8),pa,pb,pc,alpha))
    def test_exercises(self):
        p=(F(1,2),F(1,4),F(1,4)); l=(F(0),F(2),F(8))
        self.assertEqual(cvar_three(l,p,F(1,2)), F(5))
        self.assertEqual(cvar_three(l,p,F(3,4)), F(8))
        self.assertEqual(cvar_three(l,p,F(0)), F(5,2))
        self.assertEqual(cvar_three((F(0),F(3),F(9)),(F(2,3),F(1,3),F(0)),F(1,2)),F(2))
    def test_monotonicity(self):
        p=(F(1,2),F(2,5),F(1,10)); l=(F(0),F(1),F(10))
        values=[cvar_three(l,p,F(i,100)) for i in range(100)]
        self.assertTrue(all(x<=y for x,y in zip(values,values[1:])))
    def test_lipschitz(self):
        p=(F(1,2),F(2,5),F(1,10)); l=(F(0),F(1),F(10))
        shifted=(F(1,7),F(6,7),F(71,7))
        for i in range(100):
            alpha=F(i,100)
            self.assertLessEqual(abs(cvar_three(l,p,alpha)-cvar_three(shifted,p,alpha)),F(1,7))
    def test_counterexample(self):
        p=(F(1,2),F(2,5),F(1,10)); l=(F(0),F(1),F(10))
        self.assertEqual(cvar_three(l,p,F(9,10)),F(10))
        self.assertEqual(cvar_three(l,p,F(4,5)),F(11,2))
        self.assertEqual(cvar_three(l,p,F(3,4)),F(23,5))

if __name__ == "__main__":
    unittest.main()
