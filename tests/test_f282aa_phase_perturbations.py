import unittest
from fractions import Fraction as F

def certificates(q, delta):
    m = len(q)
    Q = F(1)
    for x in q:
        Q *= x
    assert Q < 1
    result = []
    for i in range(m):
        b, prod = F(0), F(1)
        for k in range(m):
            j = (i-k) % m
            b += prod * delta[j]
            prod *= q[j]
        result.append(b / (1-Q))
    return result

class PhasePerturbation(unittest.TestCase):
    def test_one_phase(self):
        self.assertEqual(certificates([F(1,2)], [F(3)]), [F(6)])
    def test_two_phases(self):
        self.assertEqual(certificates([F(1,2),F(1,3)], [F(2),F(3)]), [F(21,5),F(22,5)])
    def test_sharpness_and_recurrence(self):
        for a in range(4):
            for b in range(4):
                for c in range(4):
                    q = [F(a,5),F(b,5),F(c,5)]
                    delta = [F(1),F(2),F(3)]
                    z = certificates(q,delta)
                    for i in range(3):
                        self.assertEqual(z[i], q[i]*z[(i-1)%3]+delta[i])
    def test_uniform(self):
        q = [F(1,4),F(2,5),F(3,5)]
        d = [F(1,100)]*3
        self.assertTrue(all(x<=F(1,40) for x in certificates(q,d)))
    def test_no_uniform_q_counterexample(self):
        for n in range(2,30):
            self.assertEqual(certificates([F(n-1,n)],[F(1,n)]),[F(1)])
    def test_measurement(self):
        self.assertEqual(certificates([F(3,4)],[F(1,10)+F(1,50)]),[F(12,25)])

if __name__ == "__main__":
    unittest.main()
