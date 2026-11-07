from fractions import Fraction
import unittest

class TestFQ(unittest.TestCase):
    def test_variation_and_constant(self):
        for a in (1,2,3,5):
            for c in (-3,0,2):
                for initial in (-7,0,4):
                    y=Fraction(initial); p=Fraction(1)
                    for n in range(1,61):
                        b=Fraction(n,n+a)
                        y=b*y+Fraction(c,n+a)
                        p*=b
                        self.assertEqual(y,Fraction(c,a)+(Fraction(initial)-Fraction(c,a))*p)
    def test_telescoping_product(self):
        for a in range(1,7):
            p=Fraction(1)
            for n in range(1,61):
                p*=Fraction(n,n+a)
                expected=Fraction(1)
                for k in range(1,a+1):
                    expected*=Fraction(k,n+k)
                self.assertEqual(p,expected)
    def test_variation_exact(self):
        for a in (1,2,4):
            for c in (-2,3):
                y=Fraction(5)
                for n in range(1,36):
                    y=Fraction(n,n+a)*y+Fraction(c,n*n)
                    p=Fraction(1)
                    for k in range(1,n+1):p*=Fraction(k,k+a)
                    total=Fraction(5)*p
                    for j in range(n):
                        tail=Fraction(1)
                        for k in range(j+2,n+1):tail*=Fraction(k,k+a)
                        total+=tail*Fraction(c,(j+1)**2)
                    self.assertEqual(y,total)
if __name__=='__main__':unittest.main()
