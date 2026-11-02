"""Executable arithmetic checks for Ontologia Liczby, E1-01."""
import math
import unittest
from fractions import Fraction
from decimal import Decimal, ROUND_HALF_UP


class RationalE101Tests(unittest.TestCase):
    def test_cross_multiplication(self):
        for a in range(-10, 11):
            for b in range(1, 10):
                for k in range(1, 6):
                    self.assertEqual(a * (k*b), (k*a)*b)
                    self.assertEqual(Fraction(a,b), Fraction(k*a,k*b))

    def test_fraction_operations(self):
        for a in range(-5,6):
            for b in range(1,7):
                for c in range(-5,6):
                    for d in range(1,7):
                        x,y=Fraction(a,b),Fraction(c,d)
                        self.assertEqual(x+y,Fraction(a*d+b*c,b*d))
                        self.assertEqual(x*y,Fraction(a*c,b*d))
                        if c: self.assertEqual(x/y,Fraction(a*d,b*c))

    def test_decimal_termination_criterion(self):
        for denominator in range(1,100):
            d=denominator
            while d%2==0:d//=2
            while d%5==0:d//=5
            terminates=(d==1)
            self.assertEqual(terminates,any((10**k)%denominator==0 for k in range(0,10)))

    def test_rounding_error(self):
        for x in range(0,1001):
            number=Decimal(x)/Decimal(1000)
            rounded=number.quantize(Decimal('0.01'),rounding=ROUND_HALF_UP)
            self.assertLessEqual(abs(number-rounded),Decimal('0.005'))

    def test_percentage_reversal(self):
        for original in range(1,501):
            for p in (5,10,20,25,40):
                after=Fraction(original)*(1+Fraction(p,100))
                self.assertEqual(after/(1+Fraction(p,100)),original)

    def test_consecutive_percentages(self):
        for p in (5,10,20,50):
            t=Fraction(p,100)
            self.assertEqual((1+t)*(1-t),1-t*t)

    def test_weighted_average_bounds(self):
        for a in range(0,11):
            for b in range(0,11):
                if not (a+b):continue
                p,q=Fraction(1,5),Fraction(4,5)
                weighted=(a*p+b*q)/(a+b)
                self.assertLessEqual(p,weighted)
                self.assertLessEqual(weighted,q)

    def test_examples(self):
        self.assertEqual(Fraction(2,3)+Fraction(3,4),Fraction(17,12))
        self.assertEqual(Fraction(5,6)-Fraction(1,9),Fraction(13,18))
        self.assertEqual(Fraction(3,8)+Fraction(1,4),Fraction(5,8))
        self.assertEqual(Fraction(7,20),Fraction(35,100))
        self.assertEqual(Fraction(3,8),Fraction(375,1000))
        self.assertEqual(Fraction(2,11),Fraction(18,99))
        self.assertEqual(Fraction(137,12),Fraction(11)+Fraction(5,12))
        self.assertEqual(Fraction(1,4)+Fraction(1,3),Fraction(7,12))
        self.assertEqual(Fraction(2,5)+Fraction(1,10),Fraction(1,2))
        self.assertEqual(Fraction(10*Fraction(1,5)+90*Fraction(4,5),100),Fraction(74,100))


if __name__ == '__main__':
    unittest.main()
