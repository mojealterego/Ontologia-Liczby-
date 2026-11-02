"""Exact rational checks for Tom I F28.2-C (no floating point tolerance)."""
import unittest
from fractions import Fraction as Q

def clamp(t, lo, hi):
    return min(hi, max(lo, t))

def primal(a, y, lam, x):
    return a * (x-y)**2 / 2 + lam * abs(x)

def dual(a, y, u):
    return y*u - u*u/(2*a)

def optimum(a, y, lam):
    u = clamp(a*y, -lam, lam)
    return y-u/a, u

def gap_parts(a, y, lam, x, u):
    return a*(x-y+u/a)**2/2, lam*abs(x)-u*x

class DualityChecks(unittest.TestCase):
    def setUp(self):
        self.cases = [(Q(a), Q(y, 2), Q(lam, 2))
                      for a in (1, 2, 3, 5)
                      for y in range(-8, 9)
                      for lam in range(0, 9)]

    def test_primal_dual_optima(self):
        for a,y,lam in self.cases:
            x,u = optimum(a,y,lam)
            self.assertEqual(primal(a,y,lam,x),dual(a,y,u))
            self.assertEqual(primal(a,y,lam,x),a*y*y/2 - max(a*abs(y)-lam, Q(0))**2/(2*a))

    def test_gap_identity_and_weak_duality(self):
        for a,y,lam in self.cases:
            for x in (Q(-3),Q(0),Q(1,2),Q(4)):
                for u in (-lam, Q(0), lam):
                    p,c = gap_parts(a,y,lam,x,u)
                    self.assertGreaterEqual(p,0)
                    self.assertGreaterEqual(c,0)
                    self.assertEqual(primal(a,y,lam,x)-dual(a,y,u),p+c)

    def test_error_bounds(self):
        for a,y,lam in self.cases:
            xs,us=optimum(a,y,lam)
            for x in (Q(-3),Q(0),Q(2)):
                for u in (-lam,Q(0),lam):
                    g=primal(a,y,lam,x)-dual(a,y,u)
                    self.assertLessEqual(a*(x-xs)**2/2,g)
                    self.assertLessEqual((u-us)**2/(2*a),g)

    def test_zero_gap_and_counterexamples(self):
        a,y,lam=Q(1),Q(3),Q(1)
        self.assertEqual(optimum(a,y,lam),(Q(2),Q(1)))
        self.assertEqual(dual(a,y,Q(2)),Q(4))  # infeasible: not a bound
        self.assertEqual(gap_parts(Q(1),Q(0),Q(1),Q(1),Q(-1)),(Q(0),Q(2)))
        self.assertEqual(gap_parts(a,y,lam,Q(4),Q(1)),(Q(2),Q(0)))
        self.assertEqual(primal(a,y,lam,Q(2))-dual(a,y,Q(0)),Q(5,2))

    def test_sensitivity(self):
        for a in (Q(1),Q(2),Q(5)):
            for lam in (Q(0),Q(1,2),Q(3)):
                for y1 in [Q(-3),Q(-1,2),Q(0),Q(1),Q(4)]:
                    for y2 in [Q(-2),Q(0),Q(2)]:
                        x1,u1=optimum(a,y1,lam)
                        x2,u2=optimum(a,y2,lam)
                        self.assertLessEqual(abs(x1-x2),abs(y1-y2))
                        self.assertLessEqual(abs(u1-u2),a*abs(y1-y2))

    def test_interval_certificate(self):
        a,y,lam=Q(1),Q(3),Q(1)
        l,r=Q(0),Q(1)
        u=Q(1)
        z=clamp(y-u/a,l,r)
        d=a*(z-y)**2/2+u*z
        self.assertEqual(z,Q(1))
        self.assertEqual(d,primal(a,y,lam,z))
        for x in [Q(0),Q(1,4),Q(1,2),Q(1)]:
            self.assertLessEqual(d,primal(a,y,lam,x))

    def test_exercises(self):
        expected=[(1,3,1,Q(2),Q(1),Q(5,2)),
                  (2,3,2,Q(2),Q(2),Q(5)),
                  (2,Q(1,2),2,Q(0),Q(1),Q(1,4)),
                  (3,-2,3,Q(-1),Q(-3),Q(9,2))]
        for a,y,lam,x,u,v in expected:
            a,y,lam=Q(a),Q(y),Q(lam)
            self.assertEqual(optimum(a,y,lam),(x,u))
            self.assertEqual(primal(a,y,lam,x),v)
            self.assertEqual(dual(a,y,u),v)

if __name__ == '__main__':
    unittest.main()
