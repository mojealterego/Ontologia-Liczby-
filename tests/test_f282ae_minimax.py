import unittest
from fractions import Fraction as F

def value(weights, a, x, q=F(0)):
    assert F(0) <= q < 1
    return max(sum(w*(v-z) for w,v,z in zip(row,a,x))/(1-q) for row in weights)

class TestF282AE(unittest.TestCase):
    def test_balanced_optimum(self):
        w=[[F(4),F(1)],[F(1),F(4)]]
        self.assertEqual(value(w,[F(1)]*2,[F(1,2)]*2),F(5,2))
        self.assertEqual(value(w,[F(1)]*2,[F(1),F(0)]),F(4))
        for k in range(21):
            x=F(k,20)
            self.assertGreaterEqual(value(w,[F(1)]*2,[x,1-x]),F(5,2))
    def test_half_budget(self):
        w=[[F(4),F(1)],[F(1),F(4)]]
        self.assertEqual(value(w,[F(1)]*2,[F(1,4)]*2),F(15,4))
        for k in range(11):
            x=F(k,20)
            self.assertGreaterEqual(value(w,[F(1)]*2,[x,F(1,2)-x]),F(15,4))
    def test_single_phase(self):
        self.assertEqual(value([[F(6),F(2)]],[F(1),F(1)],[F(1),F(0)],F(1,2)),F(4))
    def test_monotonicity(self):
        w=[[F(4),F(1)],[F(1),F(4)]]
        for k in range(11):
            x=F(k,10)
            self.assertGreaterEqual(value(w,[F(1)]*2,[F(0),F(0)]),value(w,[F(1)]*2,[x,F(0)]))
    def test_exchange_dominance(self):
        w=[[F(6),F(2)],[F(3),F(1)]]
        before=value(w,[F(1),F(1)],[F(0),F(1)],F(1,3))
        after=value(w,[F(1),F(1)],[F(1,2),F(0)],F(1,3))
        self.assertLessEqual(after,before)
    def test_threshold(self):
        w=[[F(4),F(1)],[F(1),F(4)]]
        self.assertLessEqual(value(w,[F(1)]*2,[F(1,2)]*2),F(3))
    def test_zero_weights(self):
        self.assertEqual(value([[F(0),F(0)]],[F(1),F(1)],[F(0),F(0)]),F(0))

if __name__ == "__main__":
    unittest.main()
