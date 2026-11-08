from fractions import Fraction as Q
from itertools import product
import unittest

def allocations(r,N):
    if r==1:
        yield (N,)
    else:
        for k in range(1,N-r+2):
            for tail in allocations(r-1,N-k):
                yield (k,)+tail

def cost(a,n):
    return sum((x/Q(k**5) for x,k in zip(a,n)),Q(0))

def active(a,N):
    aa=list(allocations(len(a),N))
    v=min(cost(a,n) for n in aa)
    return [n for n in aa if cost(a,n)==v],v

class GRTests(unittest.TestCase):
    def test_two_region(self):
        a=(Q(1),Q(1)); opts,val=active(a,3)
        self.assertEqual(val,Q(33,32))
        self.assertEqual(len(opts),2)
        self.assertEqual(min(sum(v/Q(k**5) for v,k in zip((Q(2),Q(-1)),n)) for n in opts),Q(-15,16))
    def test_directional_exact(self):
        count=0
        for r in (2,3):
            for N in range(r+1,r+5):
                for aa in product((Q(1),Q(2),Q(3)),repeat=r):
                    opts,val=active(aa,N)
                    for vv in product((Q(-1),Q(0),Q(1)),repeat=r):
                        t=Q(1,100000)
                        slope=min(sum(v/Q(k**5) for v,k in zip(vv,n)) for n in opts)
                        _,new=active(tuple(a+t*v for a,v in zip(aa,vv)),N)
                        self.assertEqual((new-val)/t,slope)
                        count+=1
        print("directional cases:",count)
    def test_lipschitz(self):
        for N in range(3,8):
            for aa in product((Q(1),Q(2)),repeat=2):
                for bb in product((Q(1),Q(3)),repeat=2):
                    fa=active(aa,N)[1]; fb=active(bb,N)[1]
                    self.assertLessEqual(abs(fa-fb),sum(abs(a-b) for a,b in zip(aa,bb)))
if __name__=="__main__": unittest.main()
