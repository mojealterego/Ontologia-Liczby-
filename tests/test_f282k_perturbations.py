import unittest
from fractions import Fraction as F

class PerturbationsF282K(unittest.TestCase):
    def test_geometric_partial_sum(self):
        for n in range(1,20):
            self.assertEqual(sum((F(1,2)**(k+1) for k in range(n)),F(0)),1-F(1,2)**n)
    def test_geometric_tail(self):
        for n in range(12): self.assertEqual(F(1,2)**n, 2*F(1,2)**(n+1))
    def test_z3(self):
        for k in range(1,12): self.assertEqual(F(1,2)**(k-1),2*F(1,2)**k)
    def test_z5(self):
        self.assertEqual(F(1,2)**2*4+F(1,2)*F(1,2)+F(1,4),F(3,2))
    def test_z12(self):
        for n in range(1,15):
            lhs=sum(((-F(1,2))**k/F(2) for k in range(n)),F(0))
            self.assertEqual(lhs,(1-(-F(1,2))**n)/3)
    def test_nonexpansive_projection(self):
        def proj(x): return max(F(0),min(F(1),x))
        for a in range(-5,6):
            for b in range(-5,6): self.assertLessEqual(abs(proj(F(a,2))-proj(F(b,2))),F(abs(a-b),2))

if __name__=="__main__": unittest.main()
