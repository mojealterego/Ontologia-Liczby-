import unittest
from fractions import Fraction as F

class DriftCertificates(unittest.TestCase):
    def test_z1(self): self.assertEqual(F(1,4)/(1-F(1,2)),F(1,2))
    def test_z2(self): self.assertEqual(F(3,8)/(1-F(1,4)),F(1,2))
    def test_z3(self): self.assertEqual(F(1,8)+F(1,8)/(1-F(1,2)),F(3,8))
    def test_z4(self): self.assertEqual(F(3,8)*(1+F(1,2)),F(9,16))
    def test_z6(self):
        for k in range(12): self.assertEqual(abs(F(k+1)-F(k)),F(1,2)/(1-F(1,2)))
    def test_z7(self):
        for k in range(12): self.assertEqual(F(3,4)/(1-F(1,4)),1)
    def test_z8(self): self.assertEqual(F(1,8)/(1-F(1,2)),F(1,4))
    def test_k1(self):
        x=F(1)
        for k in range(50):
            x=(1-F(1,k+2))*x+F(1,k+2)
            self.assertEqual(x,1)
    def test_t3_exact_affine(self):
        q=F(1,2); a=F(3); b=F(1,4)
        for n in range(1,20):
            lhs=q**n*a+sum((q**(n-1-j)*b for j in range(n)),F(0))
            self.assertEqual(lhs,q**n*a+b*(1-q**n)/(1-q))

if __name__=="__main__": unittest.main()
