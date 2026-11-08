"""Exact rational regression for F28.2-GV."""
import itertools
import unittest
from fractions import Fraction as Q

def d(k):
    return Q(1,k**5)-Q(1,(k+1)**5)

def allocations(r,N):
    for extras in itertools.product(range(N-r+1),repeat=r):
        if sum(extras)==N-r:
            yield tuple(x+1 for x in extras)

def thresholds(a,i,N):
    M=N-len(a)
    gains=sorted((a[j]*d(k) for j in range(len(a)) if j!=i for k in range(1,M+1)),reverse=True)[:M]
    return [gains[M-s-1]/d(s+1)-a[i] for s in range(M)]

def optimal_indices(a,i,N,t):
    costs=[(sum((a[j]+(t if j==i else 0))/Q(n[j]**5) for j in range(len(a))),n[i]-1) for n in allocations(len(a),N)]
    best=min(x[0] for x in costs)
    return {s for value,s in costs if value==best}

class ThresholdTests(unittest.TestCase):
    def test_exact_enumeration(self):
        count=0
        for r in (2,3):
            for N in range(r,r+4):
                for weights in itertools.product((Q(1,4),Q(1),Q(3,2)),repeat=r):
                    for i in range(r):
                        tau=thresholds(weights,i,N)
                        self.assertEqual(tau,sorted(tau))
                        samples={Q(0),Q(1,3),Q(1),Q(3),Q(10)}
                        samples.update(x for x in tau if x>=0)
                        samples.update((x+y)/2 for x,y in zip(tau,tau[1:]) if x>=0 and y>=0)
                        for t in samples:
                            predicted={s for s in range(N-r+1) if (s==0 or tau[s-1]<=t) and (s==N-r or t<=tau[s])}
                            self.assertEqual(predicted,optimal_indices(weights,i,N,t))
                            count+=1
        self.assertGreater(count,1000)
    def test_boundary_and_ties(self):
        self.assertEqual(thresholds((Q(1),Q(1),Q(1)),0,4),[Q(0)])
        self.assertEqual(optimal_indices((Q(1),Q(1),Q(1)),0,4,Q(0)),{0,1})
    def test_negative_threshold(self):
        self.assertEqual(thresholds((Q(2),Q(1)),0,3),[Q(-1)])
        self.assertEqual(optimal_indices((Q(2),Q(1)),0,3,Q(0)),{1})

if __name__=="__main__":
    unittest.main()
