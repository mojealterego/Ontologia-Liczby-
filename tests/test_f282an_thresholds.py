import unittest
from fractions import Fraction as F

def cvar(a,b,alpha,v):
    assert a<b and 0<=alpha<1 and 0<=v<=1
    return a+(b-a)*min(F(1),v/(1-alpha))

def bounds(lo,hi,rho,delta):
    assert 0<=lo<=hi<=1 and rho>=0 and delta>0
    return max(F(0),lo-rho/delta),min(F(1),hi+rho/delta)

class ThresholdTests(unittest.TestCase):
    def test_exact_envelope(self):
        self.assertEqual(bounds(F(1,10),F(1,5),F(1,10),F(1)),(F(0),F(3,10)))
    def test_cvar_tail(self):
        self.assertEqual(cvar(F(0),F(10),F(1,2),F(1,4)),F(5))
    def test_saturation(self):
        self.assertEqual(cvar(F(0),F(10),F(1,2),F(3,4)),F(10))
    def test_endpoints(self):
        for lo_n in range(5):
            for hi_n in range(lo_n,5):
                lo,hi=F(lo_n,4),F(hi_n,4)
                l,u=bounds(lo,hi,F(1,8),F(1))
                for k in range(17):
                    v=l+(u-l)*F(k,16)
                    self.assertLessEqual(cvar(F(-2),F(6),F(3,4),l),cvar(F(-2),F(6),F(3,4),v))
                    self.assertLessEqual(cvar(F(-2),F(6),F(3,4),v),cvar(F(-2),F(6),F(3,4),u))
    def test_safe_equality(self):
        q=F(1,2)*F(6,10)
        self.assertEqual(q,F(3,10))
        self.assertEqual(cvar(F(0),F(10),F(1,2),q),F(6))
    def test_hit_radius(self):
        self.assertEqual(F(1,2)*F(8,10)-F(1,5),F(1,5))
    def test_negative_loss(self):
        self.assertEqual(cvar(F(-2),F(6),F(3,4),F(1,8)),F(2))

if __name__=="__main__": unittest.main()
