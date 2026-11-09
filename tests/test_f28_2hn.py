import unittest
from fractions import Fraction as F
from itertools import product

def radius(c, edges, J):
    values = []
    for d in edges:
        margin = sum(a*b for a,b in zip(c,d))
        assert margin > 0
        den = sum(abs(d[i]) for i in J)
        if den: values.append(margin / den)
    return min(values) if values else None

class TestSelectiveRadius(unittest.TestCase):
    def test_square(self):
        for a,b in product(range(1,12), repeat=2):
            c=(F(a),F(b))
            edges=[(F(1),F(0)),(F(0),F(1))]
            self.assertEqual(radius(c,edges,{0}),F(a))
            self.assertEqual(radius(c,edges,{1}),F(b))
            self.assertEqual(radius(c,edges,{0,1}),F(min(a,b)))
    def test_diagonal(self):
        for a,b in product(range(1,12),repeat=2):
            c=(F(a),F(b))
            self.assertEqual(radius(c,[(F(1),F(1))],{0}),F(a+b))
            self.assertEqual(radius(c,[(F(1),F(1))],{0,1}),F(a+b,2))
    def test_invisible(self):
        self.assertIsNone(radius((F(2),F(5)),[(F(0),F(1))],{0}))
    def test_boundary(self):
        c=(F(4),F(6)); e=(F(-4),F(0))
        self.assertEqual(sum((c[i]+e[i])*([F(1),F(0)][i]) for i in range(2)),0)

if __name__=="__main__": unittest.main()
