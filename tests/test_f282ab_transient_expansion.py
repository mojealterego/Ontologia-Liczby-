from fractions import Fraction as F
import unittest

def certificate(L, r, phase):
    m = len(L)
    if not m or len(r) != m: raise ValueError("invalid phases")
    Q = F(1)
    for x in L:
        if x < 0: raise ValueError("negative Lipschitz constant")
        Q *= x
    if Q >= 1: raise ValueError("full cycle must contract")
    s = F(0)
    for k in range(m):
        w = F(1)
        for j in range(k+1, m):
            w *= L[(phase+j) % m]
        s += r[(phase+k) % m] * w
    return s / (1-Q)

class TestF282AB(unittest.TestCase):
    def test_example_z1(self):
        L=[F(2),F(1,4)]; r=[F(1,10),F(1,20)]
        self.assertEqual(certificate(L,r,0),F(3,20))
        self.assertEqual(certificate(L,r,1),F(2,5))
    def test_one_phase(self):
        self.assertEqual(certificate([F(3,5)],[F(2,5)],0),1)
    def test_zero_residual(self):
        self.assertEqual(certificate([F(3),F(1,6)],[F(0),F(0)],1),0)
    def test_noncontraction_rejected(self):
        with self.assertRaises(ValueError):
            certificate([F(2),F(1,2)],[F(1),F(1)],0)
    def test_sharpness_exact_grid(self):
        for a in [F(1,2),F(1),F(2),F(3)]:
            for b in [F(1,12),F(1,8),F(1,6)]:
                if a*b >= 1: continue
                for u in [F(0),F(1,10),F(2,3)]:
                    for v in [F(0),F(1,7),F(1,2)]:
                        y0=(b*u+v)/(1-a*b)
                        y1=a*y0+u
                        self.assertEqual(y0,certificate([a,b],[u,v],0))
                        self.assertEqual(y1,certificate([a,b],[u,v],1))
    def test_counterexample_k4(self):
        for n in range(2,40):
            L=[F(n),F(1,2*n)]
            y0=F(1,n); y1=F(1)
            r=[abs(y1-L[0]*y0),abs(y0-L[1]*y1)]
            self.assertEqual(r,[F(0),F(1,2*n)])
            self.assertEqual(certificate(L,r,1),1)

if __name__ == "__main__":
    unittest.main()
