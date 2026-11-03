import unittest
from fractions import Fraction as F

def certificate(q,p,rt,rs,d):
    if not (F(0)<=q<1 and F(0)<=p<1 and min(rt,rs,d)>=0):
        raise ValueError("invalid certified input")
    b2=rt/(1-q)+rs/(1-p)
    c1=(d+(p+q)*rt/(1-q))/(1-p)
    c2=(d+(p+q)*rs/(1-p))/(1-q)
    return min(b2,c1,c2)

class TwoResidualDrift(unittest.TestCase):
    def test_z1(self):
        self.assertEqual(F(1,4)/(1-F(1,2))+F(1,8)/(1-F(1,2)),F(3,4))
    def test_z4(self):
        self.assertEqual(F(3,4)/(1-F(1,4))+F(1,4)/(1-F(1,2)),F(3,2))
    def test_z5(self):
        self.assertEqual(certificate(F(0),F(0),F(2),F(5),F(3)),F(3))
    def test_z9(self):
        self.assertEqual(certificate(F(1,2),F(1,2),F(0),F(1),F(1,2)),F(1))
    def test_sharp_comparison(self):
        for q in [F(0),F(1,4),F(1,2),F(3,4)]:
            for p in [F(0),F(1,4),F(1,2),F(3,4)]:
                for d in [F(0),F(1,8),F(1),F(3)]:
                    self.assertEqual(certificate(q,p,F(0),d,d),d/(1-p))
    def test_sharp_two_residuals(self):
        for q in [F(0),F(1,2)]:
            for p in [F(0),F(1,2)]:
                for a in [F(0),F(1),F(3)]:
                    for b in [F(0),F(1),F(3)]:
                        rt=(1-q)*a
                        rs=(1-p)*b
                        self.assertEqual(rt/(1-q)+rs/(1-p),a+b)
    def test_negative_parameters_rejected(self):
        with self.assertRaises(ValueError):
            certificate(F(1),F(1,2),F(0),F(0),F(0))

if __name__ == "__main__":
    unittest.main()
