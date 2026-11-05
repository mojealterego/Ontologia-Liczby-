"""Exact rational regression for F28.2-EC."""
from fractions import Fraction
from itertools import combinations, product
import unittest

def cost(xs, ws, a, b):
    w = sum(ws[a:b], Fraction())
    s = sum((ws[i]*xs[i] for i in range(a,b)), Fraction())
    q = sum((ws[i]*xs[i]*xs[i] for i in range(a,b)), Fraction())
    return q - s*s/w

def dp(xs, ws, k):
    n = len(xs)
    prev = [None]*(n+1)
    prev[0] = Fraction()
    choices = []
    for r in range(1,k+1):
        cur = [None]*(n+1)
        arg = [None]*(n+1)
        for j in range(r,n+1):
            vals = [(prev[t]+cost(xs,ws,t,j),t)
                    for t in range(r-1,j) if prev[t] is not None]
            cur[j],arg[j] = min(vals)
        choices.append(arg)
        prev = cur
    return prev[n], choices

class QuantizationMonge(unittest.TestCase):
    def test_monge_and_monotone_argmins(self):
        count = 0
        for n in range(2,7):
            for xs0 in combinations(range(7),n):
                xs = tuple(map(Fraction,xs0))
                ws = tuple(Fraction((i%3)+1) for i in range(n))
                for a in range(n):
                    for b in range(a,n):
                        for c in range(b,n):
                            for d in range(c,n):
                                self.assertLessEqual(cost(xs,ws,a,c+1)+cost(xs,ws,b,d+1),
                                                     cost(xs,ws,a,d+1)+cost(xs,ws,b,c+1))
                                count += 1
                for k in range(1,n+1):
                    _,args = dp(xs,ws,k)
                    for r,row in enumerate(args,1):
                        valid = [row[j] for j in range(r,n+1)]
                        self.assertEqual(valid,sorted(valid))
        self.assertGreater(count,1000)

    def test_dp_against_exhaustive(self):
        for n in range(2,7):
            for xs0 in combinations(range(7),n):
                xs = tuple(map(Fraction,xs0))
                ws = tuple(Fraction(1) for _ in xs)
                for k in range(1,n+1):
                    optimum,_ = dp(xs,ws,k)
                    brute = min(sum((cost(xs,ws,a,b) for a,b in zip((0,)+cuts,cuts+(n,))),Fraction())
                                for cuts in combinations(range(1,n),k-1))
                    self.assertEqual(optimum,brute)

    def test_counterexample(self):
        xs = tuple(map(Fraction,(0,10,0)))
        ws = (Fraction(1),)*3
        self.assertGreater(cost(xs,ws,0,2)+cost(xs,ws,1,3),
                           cost(xs,ws,0,3)+cost(xs,ws,1,2))

if __name__ == "__main__":
    unittest.main()
