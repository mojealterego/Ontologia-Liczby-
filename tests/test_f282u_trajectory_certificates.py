import unittest
from fractions import Fraction as F
from math import factorial

class TrajectoryCertificates(unittest.TestCase):
    def test_recurrence(self):
        d=F(4)
        for a, expected in [(F(1),F(3)),(F(1,2),F(2))]:
            d=d/2+a
            self.assertEqual(d,expected)
    def test_geometric(self):
        self.assertEqual(F(1,4)*sum((F(1,2)**i for i in range(3)),F(0)),F(7,16))
    def test_uniform(self):
        self.assertEqual(F(2,16)+F(3,4)*(1+F(1,4)),F(17,16))
    def test_local_certificate(self):
        self.assertEqual(F(1,8)+F(1,16)+F(1,16),F(1,4))
    def test_two_sided(self):
        self.assertEqual(F(1,2)-F(1,8),F(3,8))
        self.assertEqual(F(1,2)+F(1,8),F(5,8))
    def test_geometric_forcing(self):
        for n in range(1,18):
            d=F(0)
            for k in range(n):d=d/2+F(1,2**k)
            self.assertEqual(d,F(n,2**(n-1)))
    def test_variable_q(self):
        for n in range(1,12):
            d=F(6)
            for k in range(n):d/=k+2
            self.assertEqual(d,F(6,factorial(n+1)))
    def test_nonvanishing_product(self):
        for n in range(1,40):
            prod=F(1)
            for k in range(n):prod*=1-F(1,(k+2)**2)
            self.assertEqual(prod,F(n+2,2*(n+1)))
    def test_sharpness(self):
        for q in [F(0),F(1,4),F(1,2),F(3,4)]:
            x,y=F(3),F(0)
            for k in range(10):
                a=F(1,k+2)
                x,y=q*x,q*y-a
                expected=q**(k+1)*3+sum(q**(k-j)*F(1,j+2) for j in range(k+1))
                self.assertEqual(abs(x-y),expected)

if __name__=='__main__':unittest.main()
