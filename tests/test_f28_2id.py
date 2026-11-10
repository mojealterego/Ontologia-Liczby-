from fractions import Fraction as F
import unittest

def bounds(rows):
    lo = max((max(F(0), alpha) / u for ell,u,alpha,beta,g,a in rows), default=F(0))
    hi = max((max(F(0), beta) / ell for ell,u,alpha,beta,g,a in rows), default=F(0))
    q = max((max(F(0), a) / g for ell,u,alpha,beta,g,a in rows), default=F(0))
    return lo, q, hi

class IntervalCertificates(unittest.TestCase):
    def test_exhaustive_rationals(self):
        count=0
        for gnum in range(1,9):
            g=F(gnum,3)
            for anum in range(-6,7):
                a=F(anum,4)
                for eg in (F(0),F(1,6),F(1,3)):
                    for ea in (F(0),F(1,4),F(1,2)):
                        ell=g-eg
                        if ell<=0: continue
                        row=(ell,g+eg,a-ea,a+ea,g,a)
                        low,q,high=bounds([row])
                        self.assertLessEqual(low,q)
                        self.assertLessEqual(q,high)
                        count+=1
        self.assertGreater(count,2000)

    def test_active_direction(self):
        rows=[(F(1),F(1),F(3,5),F(4,5),F(1),F(7,10)),
              (F(1),F(1),F(1,5),F(1,2),F(1),F(2,5))]
        lo,q,hi=bounds(rows)
        self.assertEqual(q,F(7,10))
        self.assertGreater(F(3,5),F(1,2))

    def test_infinite_radius(self):
        self.assertEqual(bounds([(F(1),F(2),F(-3),F(-1),F(3,2),F(-2))]),(0,0,0))

    def test_shrinking_intervals(self):
        old=[(F(1),F(3),F(0),F(2),F(2),F(1))]
        new=[(F(3,2),F(5,2),F(1,2),F(3,2),F(2),F(1))]
        a,_,b=bounds(old); c,_,d=bounds(new)
        self.assertLessEqual(a,c)
        self.assertLessEqual(d,b)

if __name__=="__main__":
    unittest.main()
