from fractions import Fraction as F
from itertools import product
import unittest

def dot(a,b): return sum((x*y for x,y in zip(a,b)),F(0))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def norm1(v): return sum(map(abs,v),F(0))
def radius(vertices,x,c):
    return min(dot(c,sub(v,x))/norm1(sub(v,x)) for v in vertices if v!=x)

class TestEdgeCertificate(unittest.TestCase):
    def test_box_exact(self):
        checked=0
        for a,b in product(range(1,12),repeat=2):
            c=(F(a),F(b)); x=(F(0),F(0))
            vertices=[(F(i),F(j)) for i,j in product(range(2),repeat=2)]
            neighbors=[(F(1),F(0)),(F(0),F(1))]
            self.assertEqual(radius(vertices,x,c),radius(neighbors+[x],x,c));checked+=1
        self.assertEqual(checked,121)
    def test_scaled_triangle(self):
        checked=0
        for p,q,a,b in product(range(1,5),repeat=4):
            x=(F(0),F(0)); v=(F(p),F(0));w=(F(0),F(q));c=(F(a),F(b))
            self.assertEqual(radius([x,v,w],x,c),min(F(a),F(b)));checked+=1
        self.assertEqual(checked,256)
    def test_boundary(self):
        self.assertEqual(radius([(F(0),),(F(1),)],(F(0),),(F(2),)),F(2))
    def test_nonneighbor_ratio(self):
        self.assertEqual(radius([(F(0),F(0)),(F(1),F(0)),(F(0),F(1)),(F(1),F(1))],(F(0),F(0)),(F(2),F(3))),F(2))
if __name__=='__main__': unittest.main()
