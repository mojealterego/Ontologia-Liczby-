from fractions import Fraction
import unittest

def iterative(y0, p, n):
    y = Fraction(y0)
    for j in range(n):
        y = Fraction(j+1,j+2)*y + Fraction((-1)**j, (j+2)**p)
    return y

def closed(y0, p, n):
    return (Fraction(y0)+sum((Fraction((-1)**j, (j+2)**p)*(j+2) for j in range(n)), Fraction(0)))/(n+1)

class OscillatoryTests(unittest.TestCase):
    def test_exact_identity(self):
        for p in range(5):
            for y0 in range(-3,4):
                for n in range(31):
                    self.assertEqual(iterative(y0,p,n),closed(y0,p,n))
    def test_p_zero_subsequences(self):
        for m in range(1,50):
            self.assertEqual(closed(0,0,2*m),Fraction(-m,2*m+1))
            self.assertEqual(closed(0,0,2*m+1),Fraction(m+2,2*m+2))
    def test_p_one(self):
        for n in range(100):
            self.assertEqual(closed(0,1,n),Fraction(1-(-1)**n,2*(n+1)))

if __name__ == '__main__':
    unittest.main()
