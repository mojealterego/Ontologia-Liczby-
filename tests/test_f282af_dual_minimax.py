import unittest
from fractions import Fraction as F

def primal(b, A, x):
    return max(b[i] - sum(A[i][j]*x[j] for j in range(len(x))) for i in range(len(b)))

def dual(b, p, lam, mu, H, u):
    return sum(p[i]*b[i] for i in range(len(b))) - lam*H - sum(mu[j]*u[j] for j in range(len(u)))

def feasible_dual(A, p, lam, mu, c):
    return sum(p)==1 and all(v>=0 for v in p+[lam]+mu) and all(lam*c[j]+mu[j]>=sum(p[i]*A[i][j] for i in range(len(p))) for j in range(len(c)))

class DualMinimaxTests(unittest.TestCase):
    def test_symmetric_exact(self):
        b=[F(1),F(1)]; A=[[F(1),F(0)],[F(0),F(1)]]
        p=[F(1,2)]*2; lam=F(1,2); mu=[F(0)]*2
        for h in [F(0),F(1,2),F(1),F(3,2),F(2)]:
            x=[h/2]*2
            self.assertTrue(feasible_dual(A,p,lam,mu,[F(1)]*2))
            self.assertEqual(primal(b,A,x),dual(b,p,lam,mu,h,[F(1)]*2))
    def test_saturation(self):
        b=[F(1)]*2; A=[[F(1),F(0)],[F(0),F(1)]]
        self.assertEqual(primal(b,A,[F(1),F(1)]),F(0))
        self.assertEqual(dual(b,[F(1,2)]*2,F(0),[F(1,2)]*2,F(3),[F(1)]*2),F(0))
    def test_single_phase_budget(self):
        self.assertEqual(primal([F(3)],[[F(2)]],[F(1)]),F(1))
        self.assertEqual(dual([F(3)],[F(1)],F(2),[F(0)],F(1),[F(2)]),F(1))
    def test_single_phase_cap(self):
        self.assertEqual(dual([F(3)],[F(1)],F(0),[F(2)],F(4),[F(1)]),F(1))
    def test_approx_gap(self):
        b=[F(1)]*2; A=[[F(1),F(0)],[F(0),F(1)]]
        self.assertEqual(primal(b,A,[F(3,5),F(2,5)])-F(1,2),F(1,10))
    def test_weak_duality_grid(self):
        b=[F(1)]*2; A=[[F(1),F(0)],[F(0),F(1)]]
        p=[F(1,2)]*2; lam=F(1,2); mu=[F(0)]*2
        for a in range(11):
            for z in range(11-a):
                x=[F(a,10),F(z,10)]
                self.assertGreaterEqual(primal(b,A,x),dual(b,p,lam,mu,F(1),[F(1)]*2))
if __name__ == "__main__":
    unittest.main()
