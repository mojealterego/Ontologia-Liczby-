import unittest
from fractions import Fraction as F

class DriftCertificates(unittest.TestCase):
    def test_z1(self):
        self.assertEqual(F(1,4)/(1-F(1,2)),F(1,2))
    def test_z2(self):
        for n in range(1,20):
            b=F(0)
            for _ in range(n): b=b/2+F(1,2)
            self.assertEqual(b,1-F(1,2)**n)
    def test_z3(self):
        self.assertEqual(F(1,8)+F(3,16)/(1-F(1,4)),F(3,8))
    def test_z4(self):
        self.assertEqual(F(3,8)/(1-F(1,4)),F(1,2))
    def test_z5(self):
        for a,b in [(F(1,3),F(2,3)),(F(-2),F(1)),(F(0),F(0))]:
            self.assertEqual(abs(2*b-2*a),2*abs(b-a))
    def test_z6(self):
        for n in range(20): self.assertEqual(F(2)*F(1,2)**n,F(2)**(1-n))
    def test_bound(self):
        q=F(1,2); B=F(2); x=F(2)
        for k in range(20):
            x=q*x+F(1,8)
            B=q*B+F(1,8)
            self.assertLessEqual(abs(x),B)

if __name__=='__main__':
    unittest.main()
