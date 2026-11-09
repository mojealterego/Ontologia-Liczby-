import unittest
from fractions import Fraction as F

def radius(edges, cost, K):
    ratios=[]
    for d in edges:
        gap=sum(a*b for a,b in zip(cost,d))
        assert gap>0
        support=max(sum(-a*b for a,b in zip(k,d)) for k in K)
        if support>0: ratios.append(gap/support)
    return min(ratios) if ratios else None

class AsymmetricSupportTests(unittest.TestCase):
    def test_one_dimensional(self):
        for c in range(1,20):
            self.assertIsNone(radius([(F(1),)],(F(c),),[(F(0),),(F(1),)]))
            self.assertEqual(radius([(F(1),)],(F(c),),[(F(-1),),(F(0),)]),F(c))
    def test_square(self):
        edges=[(F(1),F(0)),(F(0),F(1))]
        for a in range(1,13):
            for b in range(1,13):
                self.assertEqual(radius(edges,(F(a),F(b)),[(F(0),F(0)),(F(-1),F(0)),(F(0),F(-2)),(F(-1),F(-2))]),min(F(a),F(b,2)))
    def test_scaling(self):
        edges=[(F(1),F(0)),(F(0),F(1))]
        K=[(F(0),F(0)),(F(-1),F(0)),(F(0),F(-2))]
        for a in range(1,10):
            for b in range(1,10):
                r=radius(edges,(F(a),F(b)),K)
                self.assertEqual(radius(edges,(F(a),F(b)),[(2*x,2*y) for x,y in K]),r/2)
    def test_boundary(self):
        self.assertEqual(F(2)+F(2)*F(-1),0)
        self.assertLess(F(2)+F(3)*F(-1),0)

if __name__=="__main__": unittest.main()
