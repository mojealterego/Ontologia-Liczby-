"""Exact rational regression checks for F28.2-HI."""
from fractions import Fraction as Q
from itertools import product
import unittest

def value(vertices, c):
    return min(sum(x*y for x,y in zip(u,c)) for u in vertices)

def dot(a,b):
    return sum((x*y for x,y in zip(a,b)), Q(0))

class TestHI(unittest.TestCase):
    def test_lipschitz_supergradients_and_directional(self):
        count=0
        vertices=((Q(1),Q(0)),(Q(0),Q(1)))
        for a,b,p,q in product(range(-4,5),repeat=4):
            c=(Q(a),Q(b))
            e=(Q(p),Q(q))
            vc=value(vertices,c)
            vce=value(vertices,tuple(x+y for x,y in zip(c,e)))
            self.assertLessEqual(abs(vce-vc),max(abs(p),abs(q)))
            active=[u for u in vertices if dot(u,c)==vc]
            for u in active:
                self.assertLessEqual(vce,vc+dot(e,u))
            expected=min(dot(e,u) for u in active)
            for t in (Q(1,100),Q(1,1000)):
                if a!=b and abs(a-b)>t*abs(p-q) or a==b:
                    self.assertEqual((value(vertices,tuple(x+t*y for x,y in zip(c,e)))-vc)/t,expected)
            self.assertEqual(value(vertices,(c[0]+7,c[1]+7)),vc+7)
            count+=1
        self.assertEqual(count,6561)

    def test_stability_radius(self):
        vertices=((Q(1),Q(0)),(Q(0),Q(1)))
        for gap in range(1,20):
            c=(Q(0),Q(gap))
            rho=Q(gap,2)
            for e in ((rho/2,-rho/2),(-rho/2,rho/2)):
                self.assertEqual(value(vertices,tuple(x+y for x,y in zip(c,e))),dot(vertices[0],tuple(x+y for x,y in zip(c,e))))

if __name__=="__main__":
    unittest.main()
