import unittest
from fractions import Fraction as F

class DriftCertificates(unittest.TestCase):
    def test_old_target(self): self.assertEqual(F(1,4)/(1-F(1,2)),F(1,2))
    def test_transport(self): self.assertEqual((F(1,4)+(F(1,2)+F(1,2))*F(1,2))/(1-F(1,2)),F(3,2))
    def test_sharp_translation(self): self.assertEqual(F(1)/(1-F(1,2)),2)
    def test_inexact_operator(self): self.assertEqual(F(1,4)+F(1,8)+F(1,8),F(1,2))
    def test_old_residual(self): self.assertEqual((F(1,8)+F(1,8))/(1-F(1,2)),F(1,2))
    def test_zero_contraction(self): self.assertEqual(F(5)-F(2),3)
    def test_tracking(self): self.assertEqual(F(1,2)*2+F(1,4)+F(1,4)/(1-F(1,2)),F(7,4))
    def test_same_target(self): self.assertEqual((F(0)+(F(1,2)+F(1,2))*F(0))/(1-F(1,2)),0)
    def test_computed_bound_grid(self):
        for q in [F(0),F(1,4),F(1,2),F(3,4)]:
            for p in [F(0),F(1,3),F(2,3)]:
                for w in [F(-2),F(0),F(3)]:
                    for c in [F(-1),F(0),F(2)]:
                        R=abs(w-q*w)
                        D=abs((p-q)*w+c)
                        V=(D+(p+q)*R/(1-q))/(1-p)
                        self.assertLessEqual(abs(c/(1-p)),V)

if __name__=="__main__": unittest.main()
