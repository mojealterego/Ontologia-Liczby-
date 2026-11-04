import unittest
from fractions import Fraction as F

def cvar(a,b,alpha,v):
    return a+(b-a)*min(F(1),v/(1-alpha))

def upper(u,rho,delta):
    return min(F(1),u+rho/delta)

class StrictCVaRTests(unittest.TestCase):
    def test_equality_not_strict(self):
        self.assertEqual(cvar(F(0),F(10),F(1,2),F(1,10)),F(2))
        self.assertFalse(cvar(F(0),F(10),F(1,2),upper(F(0),F(1,10),F(1)))>F(2))
    def test_open_boundary(self):
        for k in range(30):
            rho=F(k,100)
            self.assertEqual(cvar(F(0),F(10),F(1,2),upper(F(0),rho,F(1)))>F(2),rho>F(1,10))
    def test_radius_with_nominal_mass(self):
        for k in range(31):
            rho=F(k,100)
            self.assertEqual(cvar(F(0),F(10),F(1,2),upper(F(1,5),rho,F(2)))>F(6),rho>F(1,5))
    def test_margin_bound(self):
        a,b,alpha,u,delta=F(0),F(10),F(1,2),F(1,5),F(2)
        for i in range(20):
            for j in range(i,20):
                r1,r2=F(i,20),F(j,20)
                d=cvar(a,b,alpha,upper(u,r2,delta))-cvar(a,b,alpha,upper(u,r1,delta))
                self.assertGreaterEqual(d,0)
                self.assertLessEqual(d,(b-a)*(r2-r1)/(delta*(1-alpha)))
    def test_error_certificates(self):
        self.assertLessEqual(F(58,10)+F(1,10),F(6))
        self.assertGreater(F(63,10)-F(1,10),F(6))
    def test_saturation(self):
        self.assertEqual(cvar(F(0),F(10),F(1,2),F(3,4)),F(10))
    def test_negative_loss(self):
        self.assertEqual(cvar(F(-2),F(6),F(3,4),F(1,8)),F(2))
    def test_threshold_monotonicity(self):
        C=cvar(F(0),F(10),F(1,2),F(1,4))
        for k in range(20):
            self.assertEqual((F(k+1)-C)-(F(k)-C),F(1))

if __name__=='__main__': unittest.main()
