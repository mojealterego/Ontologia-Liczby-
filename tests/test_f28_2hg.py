from fractions import Fraction as F
from itertools import product
import unittest

def greedy(d,l,h,s):
    u=list(l); remaining=s-sum(l)
    for j in sorted(range(len(d)),key=lambda j:(d[j],j)):
        delta=min(remaining,h[j]-l[j]);u[j]+=delta;remaining-=delta
    assert remaining==0
    return sum(x*y for x,y in zip(d,u))

def brute(d,l,h,s):
    # Rational grid vertices: all but at most one coordinate at a bound.
    values=[]
    for k in range(len(d)):
        other=[j for j in range(len(d)) if j!=k]
        for bits in product((0,1),repeat=len(other)):
            u=[None]*len(d)
            for j,b in zip(other,bits):u[j]=(l[j],h[j])[b]
            u[k]=s-sum(u[j] for j in other)
            if l[k]<=u[k]<=h[k]:values.append(sum(d[j]*u[j] for j in range(len(d))))
    return min(values)

class ExactRegression(unittest.TestCase):
    def test_all(self):
        count=0
        for d in product((-2,0,1,3),repeat=3):
            for s2 in range(7):
                s=F(s2,2)
                l=(F(0),)*3;h=(F(1),)*3
                self.assertEqual(greedy(d,l,h,s),brute(d,l,h,s))
                count+=1
        print('EXACT_CASES',count)
    def test_kink(self):
        d=(F(1),F(3));l=(F(0),F(0));h=(F(1),F(1))
        self.assertEqual(greedy(d,l,h,F(3,2)),F(5,2))

if __name__=='__main__':unittest.main()
