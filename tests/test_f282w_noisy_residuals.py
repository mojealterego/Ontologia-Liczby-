import unittest
from fractions import Fraction as F

class Certificates(unittest.TestCase):
    def test_z1(self): self.assertEqual((F(2)/(1+F(1,2)),F(4)/(1-F(1,2))),(F(4,3),F(8)))
    def test_z2(self): self.assertEqual((F(4)/(1+F(1,4)),F(6)/(1-F(1,4))),(F(16,5),F(8)))
    def test_z3(self): self.assertEqual((7-2,7+2),(5,9))
    def test_z4(self): self.assertEqual((F(1,2)*8+1,F(1,2)*5),(5,F(5,2)))
    def test_z5(self): self.assertEqual(sum((F(1,2)**j for j in range(6)),F(0)),F(63,32))
    def test_z6(self): self.assertEqual(F(9,27),F(1,3))
    def test_z7(self): self.assertEqual((max(4-1,5-1),min(4+1,5+1)),(4,5))
    def test_z8(self): self.assertEqual((F(4)/(1+F(1,2)),F(5)/(1-F(1,2))),(F(8,3),10))
    def test_sharp(self):
        for q in [F(0),F(1,5),F(1,2),F(9,10)]:
            y=F(6)
            for s in (-1,1):
                r=abs(y-s*q*y)
                self.assertLessEqual(r/(1+q),y)
                self.assertLessEqual(y,r/(1-q))
    def test_propagation(self):
        for q in [F(0),F(1,3),F(3,4)]:
            for n in range(1,15):
                ds=[F((i*3)%5,7) for i in range(n)]
                e=F(5)
                for d in ds: e=q*e+d
                closed=q**n*5+sum((q**(n-1-j)*ds[j] for j in range(n)),F(0))
                self.assertEqual(e,closed)

if __name__ == "__main__":
    unittest.main()
