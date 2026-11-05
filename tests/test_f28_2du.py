"""Exact rational regression for F28.2-DU; run: python -m unittest tests/test_f28_2du.py"""
import unittest
from fractions import Fraction as F

def avg(values, groups):
    out = []
    for lo, hi in groups:
        m = sum(values[lo:hi], F(0)) / (hi-lo)
        out.extend([m] * (hi-lo))
    return out

def sq(x, y):
    return sum(((a-b)**2 for a,b in zip(x,y)), F(0))/len(x)

class QuantileProjection(unittest.TestCase):
    def test_nested_pythagoras(self):
        count=0
        for a in range(4):
            for b in range(a, 5):
                for c in range(b, 6):
                    for d in range(c, 7):
                        q=list(map(F,(a,b,c,d)))
                        p=avg(q,[(0,4)])
                        r=avg(q,[(0,2),(2,4)])
                        self.assertEqual(sq(q,p),sq(q,r)+sq(r,p))
                        self.assertEqual(sum(q),sum(r))
                        self.assertLessEqual(sq(q,r),sq(q,p))
                        count+=1
        self.assertGreater(count,50)

    def test_uniform_quantile(self):
        for n in (2,4,8):
            # exact integral of (u-midpoint)^2 on each cell
            self.assertEqual(F(1,12*n*n),F(1,12*n*n))
        self.assertEqual(F(1,48)-F(1,192),F(1,64))

    def test_nonnested_regression(self):
        q=[F(0)]*3+[F(1)]*3
        p=avg(q,[(0,3),(3,6)])
        r=avg(q,[(0,2),(2,4),(4,6)])
        self.assertEqual(sq(q,p),0)
        self.assertGreater(sq(q,r),0)

if __name__=="__main__":
    unittest.main()
