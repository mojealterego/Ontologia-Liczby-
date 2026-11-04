import unittest
from fractions import Fraction as F

def cvar(p, x, alpha):
    h = 1-alpha
    assert 0 < h <= 1 and sum(p)==1 and all(v>0 for v in p)
    remaining=h
    total=F(0)
    for loss,prob in sorted(zip(x,p),reverse=True):
        take=min(remaining,prob)
        total+=take*loss
        remaining-=take
        if remaining==0: break
    return total/h

def aggregate(p,x,blocks):
    result=list(x)
    assert sorted(i for b in blocks for i in b)==list(range(len(x)))
    for block in blocks:
        weight=sum(p[i] for i in block)
        mean=sum(p[i]*x[i] for i in block)/weight
        for i in block: result[i]=mean
    return result

class Hierarchy(unittest.TestCase):
    def test_telescope(self):
        p=[F(1,4)]*4; x=list(map(F,[0,2,4,6])); a=F(1,2)
        P=aggregate(p,x,[[0,1],[2,3]])
        R=aggregate(p,x,[[0,1,2,3]])
        self.assertEqual(cvar(p,x,a)-cvar(p,R,a),(cvar(p,x,a)-cvar(p,P,a))+(cvar(p,P,a)-cvar(p,R,a)))
    def test_exact_example(self):
        p=[F(1,4)]*4; x=list(map(F,[0,2,4,6])); a=F(1,2)
        P=aggregate(p,x,[[0,1],[2,3]]); R=aggregate(p,x,[[0,1,2,3]])
        self.assertEqual((cvar(p,x,a),cvar(p,P,a),cvar(p,R,a)),(5,5,3))
    def test_expectation(self):
        p=[F(1,3)]*3; x=list(map(F,[1,4,9]))
        self.assertEqual(cvar(p,x,F(0)),cvar(p,aggregate(p,x,[[0,1,2]]),F(0)))
    def test_nonadditivity(self):
        p=[F(1,2)]*2; a=F(1,2)
        gap=lambda x:cvar(p,x,a)-cvar(p,aggregate(p,x,[[0,1]]),a)
        self.assertEqual((gap([F(0),F(2)]),gap([F(2),F(0)]),gap([F(2),F(2)])),(1,1,0))
    def test_monotone_grid(self):
        p=[F(1,4)]*4
        for n in range(256):
            x=[F((n//(4**i))%4) for i in range(4)]
            P=aggregate(p,x,[[0,1],[2,3]])
            R=aggregate(p,x,[[0,1,2,3]])
            for a in [F(0),F(1,4),F(1,2),F(3,4)]:
                self.assertGreaterEqual(cvar(p,x,a),cvar(p,P,a))
                self.assertGreaterEqual(cvar(p,P,a),cvar(p,R,a))
                self.assertLessEqual(cvar(p,P,a)-cvar(p,R,a),max(abs(u-v) for u,v in zip(P,R)))

if __name__=="__main__": unittest.main()
