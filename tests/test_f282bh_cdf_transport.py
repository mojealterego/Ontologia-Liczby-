from fractions import Fraction as F
import unittest

def w1_cdf(a,b):
    z=sorted(set(a)|set(b));delta=F(0);out=F(0)
    for j in range(len(z)-1):
        delta+=a.get(z[j],F(0))-b.get(z[j],F(0))
        out+=abs(delta)*(z[j+1]-z[j])
    return out

def h(d,t):
    rest=t;total=F(0)
    for x,p in sorted(d.items(),reverse=True):
        q=min(rest,p);total+=x*q;rest-=q
        if rest==0:break
    return total

class TransportCDF(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(w1_cdf({F(0):F(1,2),F(2):F(1,2)},{F(1):F(1)}),1)
        self.assertEqual(w1_cdf({F(0):F(3,4),F(4):F(1,4)},{F(0):F(1)}),1)
    def test_grid(self):
        a={F(0):F(1,2),F(4):F(1,2)}
        b={F(1):F(1,2),F(3):F(1,2)}
        self.assertEqual(w1_cdf(a,b),1)
    def test_bound_grid(self):
        for p in [F(1,5),F(1,2),F(4,5)]:
            a={F(0):p,F(4):1-p};b={F(1):p,F(3):1-p}
            for t in [F(1,5),F(1,2),F(4,5),F(1)]:
                self.assertLessEqual(abs(h(a,t)-h(b,t)),w1_cdf(a,b))
    def test_shift(self):
        for p in [F(1,4),F(1,2),F(3,4)]:
            a={F(0):p,F(3):1-p}
            for c in [-4,-1,2,5]:
                b={x+c:v for x,v in a.items()}
                self.assertEqual(w1_cdf(a,b),abs(c))
                for t in [F(1,4),F(1,2),F(1)]:
                    self.assertEqual(h(b,t)-h(a,t),t*c)
if __name__=='__main__':unittest.main()
