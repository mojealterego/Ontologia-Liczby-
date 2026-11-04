import unittest
from fractions import Fraction as F
from itertools import permutations

def cvar(p, x, h):
    assert len(p)==len(x) and sum(p)==1 and 0<h<=1
    remaining=h
    value=F(0)
    for loss,mass in sorted(zip(x,p),reverse=True):
        taken=min(mass,remaining)
        value+=taken*loss
        remaining-=taken
        if remaining==0:
            break
    return value/h

def aggregate(p,x,blocks):
    result=list(x)
    assert sorted(i for block in blocks for i in block)==list(range(len(p)))
    for block in blocks:
        mean=sum((p[i]*x[i] for i in block),F(0))/sum(p[i] for i in block)
        for i in block:
            result[i]=mean
    return result

class TestInformationHierarchy(unittest.TestCase):
    def test_tower(self):
        p=[F(1,4),F(1,4),F(1,2)]; x=[F(8),F(4),F(0)]
        medium=[[0,1],[2]]; coarse=[[0,1,2]]
        self.assertEqual(aggregate(p,aggregate(p,x,medium),coarse),aggregate(p,x,coarse))
        self.assertEqual(aggregate(p,aggregate(p,x,coarse),medium),aggregate(p,x,coarse))
        self.assertEqual([cvar(p,aggregate(p,x,b),F(1,2)) for b in [[[0],[1],[2]],medium,coarse]],[6,6,3])

    def test_examples(self):
        self.assertEqual(cvar([F(1,4),F(3,4)],[F(8),F(0)],F(1,2)),4)
        self.assertEqual(cvar([F(1,2)]*2,[F(0),F(2)],F(1,2)),2)

    def test_alpha_zero(self):
        p=[F(1,6),F(1,3),F(1,2)]; x=[F(-7),F(3),F(11)]
        self.assertEqual(cvar(p,x,F(1)),sum((a*b for a,b in zip(p,x)),F(0)))
        self.assertEqual(cvar(p,aggregate(p,x,[[0,1,2]]),F(1)),cvar(p,x,F(1)))

    def test_lipschitz(self):
        p=[F(1,2)]*2; x=[F(0),F(2)]; y=aggregate(p,x,[[0,1]])
        self.assertEqual(cvar(p,x,F(1,2))-cvar(p,y,F(1,2)),max(abs(a-b) for a,b in zip(x,y)))

    def test_refinement_exhaustive(self):
        p=[F(1,4),F(1,4),F(1,2)]
        for a in range(-2,3):
            for b in range(-2,3):
                for c in range(-2,3):
                    x=[F(a),F(b),F(c)]
                    for h in [F(1,4),F(1,2),F(3,4),F(1)]:
                        fine=cvar(p,x,h)
                        mid=cvar(p,aggregate(p,x,[[0,1],[2]]),h)
                        coarse=cvar(p,aggregate(p,x,[[0,1,2]]),h)
                        self.assertGreaterEqual(fine,mid)
                        self.assertGreaterEqual(mid,coarse)

    def test_permutation(self):
        p=[F(1,4),F(1,4),F(1,2)]; x=[F(8),F(4),F(0)]
        for perm in permutations(range(3)):
            self.assertEqual(cvar([p[i] for i in perm],[x[i] for i in perm],F(1,2)),6)

if __name__=="__main__":
    unittest.main()
