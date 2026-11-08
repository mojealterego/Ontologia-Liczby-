from fractions import Fraction as Q
from itertools import product
import unittest

def allocations(r,N):
    return [v for v in product(range(1,N+1),repeat=r) if sum(v)==N]

def cost(a,n):
    return sum((x/Q(k**5) for x,k in zip(a,n)),Q(0))

def optimal(a):
    vals=[(cost(a,n),n) for n in allocations(len(a),sum_budget)]
    best=min(x for x,_ in vals)
    return [n for x,n in vals if x==best]

class ParametricAllocationTests(unittest.TestCase):
    def test_monotonicity_and_concavity(self):
        global sum_budget
        cases=0
        for r in (2,3):
            for N in range(r+1,r+5):
                sum_budget=N
                for weights in product((Q(1),Q(2),Q(3)),repeat=r):
                    for i in range(r):
                        previous=None
                        slopes=[]
                        for t in (Q(0),Q(1,4),Q(1,2),Q(1),Q(2),Q(4),Q(8)):
                            a=list(weights);a[i]+=t
                            ns=optimal(a)
                            lo=min(n[i] for n in ns)
                            hi=max(n[i] for n in ns)
                            if previous is not None:
                                self.assertLessEqual(previous,lo)
                            previous=hi
                            slopes.append(min(Q(1,n[i]**5) for n in ns))
                            cases+=1
                        self.assertEqual(slopes,sorted(slopes,reverse=True))
        print("exact parametric checks:",cases)

    def test_thresholds(self):
        sum_budget_local=3
        self.assertEqual(cost((Q(1),Q(2)),(1,2)),Q(17,16))
        self.assertEqual(cost((Q(1),Q(2)),(2,1)),Q(65,32))
        self.assertEqual(Q(65,32)-Q(17,16),Q(31,32))
        self.assertEqual((Q(31,32))/(Q(1)-Q(1,32)),Q(1))
        self.assertEqual((cost((Q(1),Q(3,2)),(2,1))-cost((Q(1),Q(3,2)),(1,2)))/(Q(1)-Q(1,32)),Q(1,2))

if __name__=="__main__":
    unittest.main()
