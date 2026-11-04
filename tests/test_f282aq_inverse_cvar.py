"""F28.2-AQ: exact arithmetic regression tests for inverse CVaR calibration."""
import unittest
from fractions import Fraction as F

def cvar(a, b, u, alpha):
    assert a < b and 0 <= u <= 1 and 0 <= alpha < 1
    return a + (b-a)*min(F(1), u/(1-alpha))

def safe_levels(a, b, u, tau):
    assert a < b and a <= tau < b and 0 <= u <= 1
    q=(tau-a)/(b-a)
    if u == 0:
        return ("all", None)
    if u > q:
        return ("empty", None)
    return ("interval", 1-u/q)

class TestInverseCVaR(unittest.TestCase):
    def test_piecewise_and_saturation(self):
        self.assertEqual(cvar(F(0),F(1),F(1,2),F(0)), F(1,2))
        self.assertEqual(cvar(F(0),F(1),F(1,2),F(1,2)), F(1))
        self.assertEqual(cvar(F(0),F(1),F(1,2),F(3,4)), F(1))
    def test_safe_intervals(self):
        self.assertEqual(safe_levels(F(0),F(100),F(1,5),F(40)), ("interval",F(1,2)))
        self.assertEqual(safe_levels(F(0),F(1),F(3,5),F(1,2)), ("empty",None))
        self.assertEqual(safe_levels(F(0),F(1),F(0),F(0)), ("all",None))
    def test_inverse_equivalence_grid(self):
        for ui in range(11):
            u=F(ui,10)
            for ai in range(10):
                alpha=F(ai,10)
                for ti in range(10):
                    tau=F(ti,10)
                    self.assertEqual(cvar(F(0),F(1),u,alpha)<=tau,
                                     u <= (1-alpha)*tau)
    def test_examples(self):
        self.assertEqual(cvar(F(2),F(10),F(1,5),F(1,2)), F(26,5))
        self.assertEqual(F(1,5)*F(3,5),F(3,25))
        self.assertEqual(F(1)-F(3,10),F(7,10))
    def test_nonconvex(self):
        a=F(0);b=F(1);u=F(1,2)
        self.assertGreater(cvar(a,b,u,F(1,2)),
          F(1,3)*cvar(a,b,u,F(0))+F(2,3)*cvar(a,b,u,F(3,4)))
    def test_stability(self):
        q=F(1,4);u=F(1,8);v=F(3,16)
        self.assertEqual(abs((1-u/q)-(1-v/q)),abs(u-v)/q)

if __name__=="__main__":
    unittest.main()
