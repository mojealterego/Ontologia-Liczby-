"""Testy F28.2-BC: arytmetyka dokładna Fraction, bez zależności zewnętrznych."""
from fractions import Fraction as F
import unittest

def cvar(values, weights, alpha):
    assert len(values)==len(weights)>0
    assert sum(weights)==1 and all(w>0 for w in weights)
    assert F(0)<=alpha<F(1)
    pairs=sorted(zip(values,weights), reverse=True)
    remaining=1-alpha
    total=F(0)
    for v,w in pairs:
        take=min(remaining,w)
        total+=take*v
        remaining-=take
        if remaining==0: break
    return total/(1-alpha)

class TestSensitivity(unittest.TestCase):
    def test_examples(self):
        x=[F(0),F(10)]; p=[F(1,2)]*2
        self.assertEqual(cvar(x,p,F(1,4)),F(20,3))
        self.assertEqual(cvar(x,p,F(3,4)),10)
        self.assertEqual(cvar([-2,1,7],[F(1,4),F(1,2),F(1,4)],F(1,2)),4)
    def test_mean_and_limit(self):
        for x in ([F(-2),F(1),F(7)],[F(0),F(10)],[F(3)]*3):
            p=[F(1,len(x))]*len(x)
            self.assertEqual(cvar(x,p,F(0)),sum(v*w for v,w in zip(x,p)))
            self.assertEqual(cvar(x,p,F(999,1000)),max(x))
    def test_monotone_and_bound(self):
        levels=[F(k,20) for k in range(20)]
        for a in range(-2,3):
            for b in range(-2,3):
                for c in range(-2,3):
                    x=[F(a),F(b),F(c)];p=[F(1,3)]*3
                    cs=[cvar(x,p,t) for t in levels]
                    for i in range(19):
                        self.assertLessEqual(cs[i],cs[i+1])
                        self.assertLessEqual(cs[i+1]-cs[i],(max(x)-min(x))*(levels[i+1]-levels[i])/(1-levels[i]))
    def test_affine_and_counterexample(self):
        x=[F(0),F(10)];p=[F(1,2)]*2
        self.assertEqual(cvar([2*v+3 for v in x],p,F(1,4)),2*cvar(x,p,F(1,4))+3)
        self.assertNotEqual(cvar([-v for v in x],p,F(1,2)),-cvar(x,p,F(1,2)))

if __name__=="__main__": unittest.main()
