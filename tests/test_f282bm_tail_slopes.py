from fractions import Fraction as F
import unittest
from itertools import product

def H(law,t):
    assert 0<=t<=1 and sum(law.values())==1
    r=t;v=F(0)
    for x,p in sorted(law.items(),reverse=True):
        take=min(r,p);v+=x*take;r-=take
        if r==0:break
    return v

def slopes(law):
    return [(sum(p for y,p in law.items() if y>x),x) for x in sorted(law,reverse=True)]

class TailSlopes(unittest.TestCase):
    def test_piecewise(self):
        d={F(-2):F(1,4),F(1):F(1,2),F(5):F(1,4)}
        self.assertEqual([H(d,F(i,4)) for i in range(5)],[F(0),F(5,4),F(3,2),F(7,4),F(5,4)])
    def test_concavity_exhaustive(self):
        n=0
        for p,q in product([F(1,4),F(1,2),F(3,4)],repeat=2):
            a={F(-2):p,F(4):1-p};b={F(0):q,F(6):1-q}
            for d in (a,b):
                for i in range(1,8):
                    t=F(i,8)
                    self.assertGreaterEqual(2*H(d,t),H(d,t-F(1,8))+H(d,t+F(1,8)))
                    n+=1
        self.assertEqual(n,126)
    def test_slope_breakpoints(self):
        d={F(-2):F(1,4),F(1):F(1,2),F(5):F(1,4)}
        for t,x in slopes(d):
            if t==1:continue
            if t<1:
                step=F(1,100)
                self.assertEqual((H(d,t+step)-H(d,t))/step,x)
    def test_translation(self):
        d={F(0):F(1,4),F(4):F(3,4)}
        for c,t in product([-3,0,5],[F(1,4),F(1,2),F(1)]):
            moved={x+c:p for x,p in d.items()}
            self.assertEqual(H(moved,t)-H(d,t),t*c)
if __name__=='__main__':unittest.main()
