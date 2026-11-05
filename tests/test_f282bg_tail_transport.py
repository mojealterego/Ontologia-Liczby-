from fractions import Fraction as F
import unittest

def h(dist,t):
    remaining=t; total=F(0)
    for x,p in sorted(dist,reverse=True):
        take=min(p,remaining);total+=x*take;remaining-=take
        if not remaining:break
    return total

def w1(a,b):
    a=sorted(a);b=sorted(b);i=j=0;ra=a[0][1];rb=b[0][1];total=F(0)
    while i<len(a) and j<len(b):
        q=min(ra,rb);total+=q*abs(a[i][0]-b[j][0]);ra-=q;rb-=q
        if not ra:i+=1;ra=a[i][1] if i<len(a) else F(0)
        if not rb:j+=1;rb=b[j][1] if j<len(b) else F(0)
    return total

class TestBG(unittest.TestCase):
    def test_sharp(self):
        for t in [F(1,10),F(1,4),F(1,2),F(1)]:
            a=[(F(0),1-t),(F(7),t)] if t<1 else [(F(7),F(1))]
            b=[(F(0),F(1))]
            self.assertEqual(abs(h(a,t)-h(b,t)),w1(a,b))
    def test_examples(self):
        self.assertEqual(h([(F(0),F(3,4)),(F(8),F(1,4))],F(1,4)),2)
        self.assertEqual(h([(F(1),F(1,2)),(F(3),F(1,2))],F(3,4)),F(7,4))
        self.assertEqual(h([(F(-3),F(1))],F(1,2)),F(-3,2))
    def test_transport_exhaustive(self):
        xs=[-2,0,3]; weights=[F(1,4),F(1,2),F(3,4)]
        count=0
        for p in weights:
            for q in weights:
                a=[(F(xs[0]),p),(F(xs[2]),1-p)]
                b=[(F(xs[1]),q),(F(xs[2]),1-q)]
                for t in [F(1,4),F(1,2),F(3,4),F(1)]:
                    self.assertLessEqual(abs(h(a,t)-h(b,t)),w1(a,b));count+=1
        self.assertEqual(count,36)
    def test_concavity(self):
        d=[(F(-2),F(1,4)),(F(1),F(1,2)),(F(5),F(1,4))]
        for k in range(1,8):
            t=F(k,8)
            self.assertGreaterEqual(2*h(d,t),h(d,t-F(1,8))+h(d,t+F(1,8)))

if __name__=='__main__':unittest.main()
