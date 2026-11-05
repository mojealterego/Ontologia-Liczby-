from fractions import Fraction as F
import unittest
from itertools import product

def h(d,t):
    assert 0<t<=1 and sum(d.values())==1
    left=t;result=F(0)
    for x,p in sorted(d.items(),reverse=True):
        q=min(left,p);result+=x*q;left-=q
        if not left:break
    return result

def mixture(a,b,e):
    z={x:(1-e)*a.get(x,F(0))+e*b.get(x,F(0)) for x in set(a)|set(b)}
    return {x:p for x,p in z.items() if p}

class Contamination(unittest.TestCase):
    def test_bounds_exhaustive(self):
        checked=0
        for p,q in product([F(1,4),F(1,2),F(3,4)],repeat=2):
            a={F(0):p,F(4):1-p};b={F(-2):q,F(7):1-q}
            for e,t in product([F(0),F(1,5),F(1,2),F(1)], [F(1,5),F(1,2),F(1)]):
                c=mixture(a,b,e)
                assert abs(h(c,t)-h(a,t))<=min(F(1),e/t)*9
                checked+=1
        self.assertEqual(checked,108)
    def test_sharp_small_contamination(self):
        for e in [F(1,10),F(1,4),F(1,2)]:
            a={F(0):F(1)};b={F(8):F(1)}
            c=mixture(a,b,e)
            for t in [e,F(1)]:
                self.assertEqual(h(c,t)-h(a,t),8*min(e,t))
    def test_convexity_in_distribution_of_h(self):
        a={F(0):F(1)};b={F(10):F(1)}
        for e in [F(1,4),F(1,2)]:
            for t in [F(1,4),F(1,2),F(1)]:
                self.assertGreaterEqual(h(mixture(a,b,e),t), (1-e)*h(a,t)+e*h(b,t))
    def test_mean_identity(self):
        a={F(-2):F(1,2),F(4):F(1,2)}
        b={F(1):F(1)}
        for e in [F(0),F(1,3),F(1)]:
            self.assertEqual(h(mixture(a,b,e),F(1)),F(1))
if __name__=='__main__':unittest.main()
