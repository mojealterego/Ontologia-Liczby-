import unittest
from fractions import Fraction as F
from itertools import product

def segments(values,weights):
    assert len(values)==len(weights) and all(w>0 for w in weights) and sum(weights)==1
    d={}
    for x,w in zip(values,weights): d[x]=d.get(x,F(0))+w
    out=[];left=F(0)
    for x,w in sorted(d.items()):
        out.append((left,left+w,x));left+=w
    return out

def cvar(values,weights,alpha):
    assert 0<=alpha<1
    return sum((max(F(0),b-max(a,alpha))*x for a,b,x in segments(values,weights)),F(0))/(1-alpha)

def w1(x,p,y,q):
    a=segments(x,p);b=segments(y,q)
    cuts=sorted({F(0),F(1)}|{v for z in a+b for v in z[:2]})
    return sum((v-u)*abs(next(z for l,r,z in a if l<=u<r)-next(z for l,r,z in b if l<=u<r)) for u,v in zip(cuts,cuts[1:]))

class TransportTests(unittest.TestCase):
    def test_sharpness(self):
        for alpha in [F(0),F(1,4),F(1,2),F(3,4),F(9,10)]:
            x=[7] if alpha==0 else [0,7]
            p=[F(1)] if alpha==0 else [alpha,1-alpha]
            self.assertEqual(cvar(x,p,alpha),w1([0],[F(1)],x,p)/(1-alpha))
    def test_exhaustive_lipschitz(self):
        cases=[([x,y],[F(1,3),F(2,3)]) for x,y in product(range(4),repeat=2)]
        for (x,p),(y,q) in product(cases,repeat=2):
            d=w1(x,p,y,q)
            for a in [F(0),F(1,4),F(1,2),F(3,4),F(9,10)]:
                self.assertLessEqual(abs(cvar(x,p,a)-cvar(y,q,a)),d/(1-a))
    def test_translation(self):
        for a in [F(0),F(1,2),F(3,4)]:
            self.assertEqual(cvar([2,5],[F(1,3),F(2,3)],a)+4,cvar([6,9],[F(1,3),F(2,3)],a))
    def test_counterexample(self):
        self.assertGreater(cvar([0,10],[F(9,10),F(1,10)],F(9,10)),cvar([2],[F(1)],F(9,10)))

if __name__=="__main__": unittest.main()
