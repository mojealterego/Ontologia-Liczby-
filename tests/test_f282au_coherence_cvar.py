import unittest
from fractions import Fraction as F
from itertools import product

def cvar(p, x, alpha):
    h = 1-alpha
    assert 0 < h <= 1 and sum(p) == 1 and len(p)==len(x)
    remaining=h
    total=F(0)
    for loss, prob in sorted(zip(x,p),reverse=True):
        take=min(remaining,prob)
        total+=take*loss
        remaining-=take
        if remaining==0: break
    assert remaining==0
    return total/h

class CoherenceTests(unittest.TestCase):
    def setUp(self):
        self.p=[F(1,2),F(1,2)]
        self.a=F(1,2)
    def test_translation(self):
        for x in product(range(-2,3),repeat=2):
            self.assertEqual(cvar(self.p,[z+3 for z in x],self.a),cvar(self.p,x,self.a)+3)
    def test_homogeneity(self):
        for x in product(range(-2,3),repeat=2):
            for k in [0,1,2,3]:
                self.assertEqual(cvar(self.p,[k*z for z in x],self.a),k*cvar(self.p,x,self.a))
    def test_monotonicity(self):
        for x in product(range(-1,2),repeat=2):
            for d in product(range(3),repeat=2):
                y=[a+b for a,b in zip(x,d)]
                self.assertLessEqual(cvar(self.p,x,self.a),cvar(self.p,y,self.a))
    def test_subadditivity(self):
        vals=list(product(range(-2,3),repeat=2))
        for x in vals:
            for y in vals:
                self.assertLessEqual(cvar(self.p,[a+b for a,b in zip(x,y)],self.a),cvar(self.p,x,self.a)+cvar(self.p,y,self.a))
    def test_stability(self):
        for x in product(range(-2,3),repeat=2):
            for y in product(range(-2,3),repeat=2):
                self.assertLessEqual(abs(cvar(self.p,x,self.a)-cvar(self.p,y,self.a)),max(abs(a-b) for a,b in zip(x,y)))
    def test_counterexamples(self):
        self.assertEqual(cvar(self.p,[2,0],self.a)+cvar(self.p,[0,2],self.a)-cvar(self.p,[2,2],self.a),2)
        self.assertNotEqual(cvar(self.p,[-2,0],self.a),-cvar(self.p,[2,0],self.a))
if __name__ == '__main__': unittest.main()
