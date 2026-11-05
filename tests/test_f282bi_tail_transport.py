from fractions import Fraction as F
import unittest

def quantile_segments(d):
    s=F(0);out=[]
    for x,p in sorted(d.items()):
        out.append((s,s+p,x));s+=p
    assert s==1
    return out

def tail_transport(a,b,t):
    qa=quantile_segments(a);qb=quantile_segments(b)
    cuts=sorted({F(0),F(1),F(1)-t}|{v for lo,hi,x in qa for v in (lo,hi)}|{v for lo,hi,x in qb for v in (lo,hi)})
    T=R=F(0)
    for lo,hi in zip(cuts,cuts[1:]):
        mid=(lo+hi)/2
        x=next(x for l,r,x in qa if l<=mid<r)
        y=next(x for l,r,x in qb if l<=mid<r)
        if lo>=1-t:T+=(hi-lo)*abs(x-y)
        else:R+=(hi-lo)*abs(x-y)
    return T,R

def h(d,t):
    return sum((hi-max(lo,1-t))*x for lo,hi,x in quantile_segments(d) if hi>1-t)

class TailTransport(unittest.TestCase):
    def test_zero_tail(self):
        a={F(0):F(1,2),F(2):F(1,2)}
        b={F(1):F(1,2),F(2):F(1,2)}
        self.assertEqual(tail_transport(a,b,F(1,2)),(0,F(1,2)))
    def test_sharp(self):
        for t in [F(1,5),F(1,2),F(1)]:
            a={F(0):1-t,F(8):t} if t<1 else {F(8):F(1)}
            b={F(0):F(1)}
            T,R=tail_transport(a,b,t)
            self.assertEqual(T,t*8);self.assertEqual(R,0)
            self.assertEqual(abs(h(a,t)-h(b,t)),T)
    def test_exhaustive(self):
        for p in [F(1,4),F(1,2),F(3,4)]:
            for q in [F(1,4),F(1,2),F(3,4)]:
                a={F(-2):p,F(3):1-p};b={F(0):q,F(5):1-q}
                for t in [F(1,4),F(1,2),F(3,4),F(1)]:
                    T,R=tail_transport(a,b,t)
                    self.assertGreaterEqual(T,abs(h(a,t)-h(b,t)))
                    self.assertGreaterEqual(R,0)
                    self.assertEqual(T+R,tail_transport(a,b,F(1))[0])
    def test_mean_counterexample(self):
        a={F(0):F(1,2),F(2):F(1,2)};b={F(1):F(1)}
        self.assertEqual(h(a,F(1)),h(b,F(1)))
        self.assertEqual(tail_transport(a,b,F(1))[0],1)
if __name__=='__main__':unittest.main()
