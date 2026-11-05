from fractions import Fraction as F
from itertools import product
import unittest

def h(d,t):
    assert 0<t<=1 and sum(d.values())==1
    left=t;result=F(0)
    for x,p in sorted(d.items(),reverse=True):
        w=min(left,p);result+=x*w;left-=w
        if not left:break
    return result

def mix(a,b,e):
    return {x:p for x in set(a)|set(b) if (p:=(1-e)*a.get(x,0)+e*b.get(x,0))}

def w1(a,b):
    z=sorted(set(a)|set(b));delta=F(0);out=F(0)
    for x,y in zip(z,z[1:]):
        delta+=a.get(x,0)-b.get(x,0);out+=abs(delta)*(y-x)
    return out

class TestBK(unittest.TestCase):
    def test_transport_certificate(self):
        cases=0
        for p,q,e,t in product([F(1,4),F(1,2),F(3,4)], [F(1,4),F(3,4)], [F(0),F(1,5),F(1,2),F(1)], [F(1,5),F(1,2),F(1)]):
            a={F(0):p,F(4):1-p};b={F(-2):q,F(7):1-q};c=mix(a,b,e)
            bound=min(e*w1(a,b),F(9)*min(e,t))
            self.assertLessEqual(abs(h(c,t)-h(a,t)),bound);cases+=1
        self.assertEqual(cases,72)
    def test_sharpness(self):
        for e,t in product([F(1,10),F(1,4),F(1,2),F(1)],repeat=2):
            a={F(0):F(1)};b={F(8):F(1)}
            self.assertEqual(h(mix(a,b,e),t)-h(a,t),8*min(e,t))
    def test_mean(self):
        a={F(-2):F(1,2),F(4):F(1,2)};b={F(1):F(1)}
        for e in [F(0),F(1,3),F(1)]:
            self.assertEqual(h(mix(a,b,e),F(1)),F(1))
    def test_zero_transport(self):
        a={F(0):F(1,2),F(2):F(1,2)}
        self.assertEqual(w1(a,a),0)
        for e in [F(0),F(1,4),F(1)]:
            self.assertEqual(h(mix(a,a,e),F(1,2)),h(a,F(1,2)))

if __name__=='__main__':unittest.main()
