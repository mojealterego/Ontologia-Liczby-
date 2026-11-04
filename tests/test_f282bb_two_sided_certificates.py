"""Exact rational regression tests for F28.2-BB."""
import unittest
from fractions import Fraction as F
from itertools import product

def cvar(p, x, alpha):
    h = 1-alpha
    rem = h
    total = F(0)
    for i in sorted(range(len(x)), key=lambda j: x[j], reverse=True):
        take = min(rem, p[i])
        total += take*x[i]
        rem -= take
        if rem == 0:
            break
    return total/h

def bounds(p, x, blocks, alpha):
    m = list(x)
    u = list(x)
    for block in blocks:
        mass = sum((p[i] for i in block), F(0))
        avg = sum((p[i]*x[i] for i in block), F(0))/mass
        mx = max(x[i] for i in block)
        for i in block:
            m[i],u[i] = avg,mx
    return cvar(p,m,alpha),cvar(p,u,alpha)

class Certificates(unittest.TestCase):
    def test_exhaustive_three_scenarios(self):
        p = [F(1,3)]*3
        coarse = [[0,1,2]]
        fine = [[0],[1,2]]
        single = [[0],[1],[2]]
        for v in product(range(-2,3),repeat=3):
            x=list(map(F,v))
            for a in (F(0),F(1,3),F(2,3)):
                l0,u0=bounds(p,x,coarse,a)
                l1,u1=bounds(p,x,fine,a)
                l2,u2=bounds(p,x,single,a)
                exact=cvar(p,x,a)
                self.assertLessEqual(l0,l1)
                self.assertLessEqual(l1,exact)
                self.assertLessEqual(exact,u1)
                self.assertLessEqual(u1,u0)
                self.assertEqual((l2,u2),(exact,exact))
    def test_midpoint(self):
        p=[F(1,2)]*2
        x=[F(0),F(2)]
        l,u=bounds(p,x,[[0,1]],F(1,2))
        self.assertEqual((l,u),(F(1),F(2)))
        self.assertLessEqual(abs(cvar(p,x,F(1,2))-(l+u)/2),(u-l)/2)
    def test_constant(self):
        p=[F(1,4),F(3,4)]
        self.assertEqual(bounds(p,[F(5),F(5)],[[0,1]],F(3,4)),(F(5),F(5)))
if __name__=="__main__":
    unittest.main()
