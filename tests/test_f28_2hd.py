"""F28.2-HD: exact rational dual-vs-primal regression."""
from fractions import Fraction as Q
from itertools import product
import unittest

def primal(a,d,rho):
    lo=[-min(rho,x) for x in a]
    hi=[rho for _ in a]
    vals=[]
    for free in range(len(a)):
        fixed=[j for j in range(len(a)) if j!=free]
        for ends in product((0,1),repeat=len(fixed)):
            u=[Q(0)]*len(a)
            for j,e in zip(fixed,ends):
                u[j]=hi[j] if e else lo[j]
            u[free]=-sum(u)
            if lo[free]<=u[free]<=hi[free]:
                vals.append(sum(x*y for x,y in zip(d,u)))
    return min(vals)

def dual(a,d,rho):
    lo=[-min(rho,x) for x in a]
    hi=[rho for _ in a]
    return max(sum(min((x-l)*low,(x-l)*high) for x,low,high in zip(d,lo,hi)) for l in d)

class DualCertificate(unittest.TestCase):
    def test_exhaustive(self):
        checks=0
        for r in (2,3):
            for a0 in product((Q(1,2),Q(1),Q(2)),repeat=r):
                for d0 in product((Q(-1),Q(0),Q(1)),repeat=r):
                    for rho in (Q(0),Q(1,4),Q(1),Q(2)):
                        self.assertEqual(primal(a0,d0,rho),dual(a0,d0,rho))
                        checks+=1
        print("PASS",checks,"exact rational instances")
    def test_real_allocation(self):
        a=(Q(1),Q(2))
        d=(Q(-31,32),Q(31,32))
        self.assertEqual(primal(a,d,Q(1,4)),Q(-31,64))
        self.assertEqual(dual(a,d,Q(1,2)),Q(-31,32))
if __name__=="__main__":
    unittest.main()
