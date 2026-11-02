"""Arithmetic regression tests for E1-04; no third-party dependencies."""
import unittest
from fractions import Fraction

class ElementaryAlgebra(unittest.TestCase):
    def test_square_identities(self):
        for a in range(-20,21):
            for b in range(-20,21):
                self.assertEqual((a+b)**2,a*a+2*a*b+b*b)
                self.assertEqual((a-b)**2,a*a-2*a*b+b*b)
                self.assertEqual((a-b)*(a+b),a*a-b*b)

    def test_cube_factorization(self):
        for a in range(-12,13):
            for b in range(-12,13):
                self.assertEqual(a**3+b**3,(a+b)*(a*a-a*b+b*b))
                self.assertEqual(a**3-b**3,(a-b)*(a*a+a*b+b*b))

    def test_distributivity(self):
        for a in range(-10,11):
            for b in range(-10,11):
                for c in (-9,-1,0,1,7):
                    self.assertEqual(a*(b+c),a*b+a*c)

    def test_degree_cancellation_counterexample(self):
        # (x^2+1)+(-x^2+x)=x+1
        for x in range(-100,101):
            self.assertEqual((x*x+1)+(-x*x+x),x+1)

    def test_domain_preservation(self):
        for x in range(-40,41):
            if x != 1:
                self.assertEqual(Fraction(x*x-1,x-1),x+1)
            else:
                with self.assertRaises(ZeroDivisionError):
                    Fraction(x*x-1,x-1)

    def test_rational_addition(self):
        for a in range(-5,6):
            for b in range(-5,6):
                for c in range(-5,6):
                    for d in (-3,-1,1,2,4):
                        if b:
                            self.assertEqual(Fraction(a,b)+Fraction(c,d),Fraction(a*d+b*c,b*d))

    def test_square_nonnegative(self):
        for a in range(-100,101):
            for b in (-100,-2,0,3,101):
                self.assertGreaterEqual((a-b)**2,0)
                self.assertGreaterEqual(a*a+b*b,2*a*b)

    def test_worked_examples(self):
        self.assertEqual(3*24+4*15,132)
        self.assertEqual((2+1)**2-2**2,5)
        self.assertEqual((2*3-5)*(2*3+5),11)
        self.assertEqual((2+2)*(2-4),-8)
        self.assertEqual(2**2-4*2+7,3)

    def test_invalid_cancellation_counterexample(self):
        for a in range(-5,6):
            if a != 0:
                self.assertEqual(Fraction(a,a),1)
        with self.assertRaises(ZeroDivisionError):
            Fraction(0,0)

if __name__=="__main__":
    unittest.main()
