from fractions import Fraction as F
import unittest

class PhaseTests(unittest.TestCase):
    def cert(self, q, r):
        m = len(q)
        Q = F(1)
        for a in q:
            Q *= a
        C = []
        for i in range(m):
            b, w = F(0), F(1)
            for k in range(m):
                b += w * r[(i-k) % m]
                w *= q[(i-k) % m]
            C.append(b / (1-Q))
        return C

    def test_two_phases(self):
        self.assertEqual(self.cert([F(1,2),F(1,3)],[F(1,10),F(1,20)]),[F(3,20),F(1,10)])

    def test_uncertainty(self):
        self.assertEqual(self.cert([F(1,2),F(1,3)],[F(11,100),F(6,100)]),[F(21,125),F(29,250)])

    def test_exact_recurrence(self):
        for a in range(5):
            for b in range(5):
                for u in range(4):
                    for v in range(4):
                        q = [F(a,5), F(b,5)]
                        r = [F(u,10), F(v,10)]
                        c = self.cert(q,r)
                        self.assertEqual(c[0],q[0]*c[1]+r[0])
                        self.assertEqual(c[1],q[1]*c[0]+r[1])

    def test_zero(self):
        self.assertEqual(self.cert([F(1,2),F(1,3)],[F(0),F(0)]),[F(0),F(0)])

    def test_single(self):
        self.assertEqual(self.cert([F(1,4)],[F(3,8)]),[F(1,2)])

if __name__ == "__main__":
    unittest.main()
