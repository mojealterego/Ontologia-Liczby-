import unittest
from fractions import Fraction as F

class Tracking(unittest.TestCase):
    def test_z1(self):
        b=F(0)
        for n in range(1,20):
            b=b/2+F(1,4)
            self.assertEqual(b,F(1,2)*(1-F(1,2)**n))
    def test_z2(self):
        b=F(4); b=b/2+F(1,4)
        self.assertEqual(b,F(9,4))
        b=b/4+F(1,4)
        self.assertEqual(b,F(13,16))
    def test_z3(self):
        b=F(0)
        for n in range(1,20):
            b=b/2+F(1,2)**n
            self.assertEqual(b,F(n)*F(1,2)**n)
    def test_z5(self):
        b=F(2)
        for n in range(1,20):
            b=b/4+F(3,4)
            self.assertEqual(b,1+F(1,4)**n)
    def test_z6(self):
        self.assertEqual((F(1,4)-F(1,8))/(1+F(1,2)),F(1,12))
        self.assertEqual((F(1,4)+F(1,8))/(1-F(1,2)),F(3,4))
    def test_z7(self):
        self.assertEqual(F(1,10)/(1-F(1,2)),F(1,5))
    def test_z8(self):
        for k in range(20):
            self.assertEqual(F(1,k+1)-F(1,k+2),F(1,(k+1)*(k+2)))
    def test_t7_sharpness(self):
        for q in (F(0),F(1,4),F(1,2),F(3,4)):
            for a in (F(0),F(1),F(4)):
                for d,v in ((F(0),F(0)),(F(1,8),F(1,4))):
                    self.assertEqual(abs(q*a+d+v),q*a+d+v)

if __name__=='__main__': unittest.main()
