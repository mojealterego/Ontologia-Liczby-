import unittest
from fractions import Fraction as F

def risk(alpha,u,rho,delta,a,b):
    assert F(0)<=alpha<F(1) and F(0)<=u<=F(1) and rho>=0 and delta>0 and a<=b
    v=min(F(1),u+rho/delta)
    return a+(b-a)*min(F(1),v/(1-alpha))

class TestF282AL(unittest.TestCase):
    def test_z1(self): self.assertEqual(risk(F(1,2),F(0),F(1,4),F(1),F(0),F(2)),F(1))
    def test_z2(self): self.assertEqual(risk(F(3,4),F(1,8),F(1,16),F(1),F(1),F(5)),F(4))
    def test_z3(self): self.assertEqual(F(2)*(1-F(3,4)-F(1,8)),F(1,4))
    def test_z4(self): self.assertEqual(risk(F(1,2),F(0),F(1,2),F(2),F(-1),F(3)),F(1))
    def test_z5(self): self.assertEqual(risk(F(1,2),F(3,4),F(0),F(1),F(2),F(6)),F(6))
    def test_z6(self): self.assertEqual(risk(F(0),F(1,4),F(1,4),F(1),F(0),F(8)),F(4))
    def test_monotonicity(self):
        for u in [F(i,8) for i in range(9)]:
            seq=[risk(F(1,2),u,F(j,16),F(1),F(0),F(2)) for j in range(17)]
            self.assertEqual(seq,sorted(seq))
    def test_upper_bound(self):
        for u in [F(i,8) for i in range(9)]:
            for rho in [F(j,16) for j in range(17)]:
                nominal=risk(F(1,2),u,F(0),F(1),F(0),F(2))
                self.assertLessEqual(risk(F(1,2),u,rho,F(1),F(0),F(2)),min(F(2),nominal+F(4)*rho))

if __name__=='__main__': unittest.main()
