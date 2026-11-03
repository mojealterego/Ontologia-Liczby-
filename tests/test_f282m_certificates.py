import unittest
from fractions import Fraction as F

class ResidualCertificates(unittest.TestCase):
    def test_upper_sharpness(self):
        for q in [F(0), F(1,4), F(1,2), F(3,4)]:
            for a in [F(1), F(2), F(4)]:
                for d in [F(0), (1-q)*a/2]:
                    y=q*a+d
                    r=abs(a-y)
                    self.assertEqual((r+d)/(1-q), a)
    def test_lower_sharpness(self):
        for q in [F(0), F(1,4), F(1,2)]:
            for a in [F(1), F(2)]:
                d=F(1,8)
                r=abs(a-(-q*a-d))
                self.assertEqual((r-d)/(1+q),a)
    def test_example_z2(self):
        self.assertEqual((F(1,4)-F(1,8))/(1+F(1,2)),F(1,12))
        self.assertEqual((F(1,4)+F(1,8))/(1-F(1,2)),F(3,4))
    def test_example_z10(self):
        self.assertEqual(F(1)+F(1,4)+F(1,2),F(7,4))
    def test_example_z8(self):
        r=abs(F(2)-F(5,4));d=F(1,4);q=F(1,2)
        self.assertEqual((r+d)/(1-q),2)
        self.assertEqual((r-d)/(1+q),F(1,3))

if __name__ == "__main__":
    unittest.main()
