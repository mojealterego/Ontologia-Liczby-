"""Exact rational regression tests for F28.2-HW (standard library only)."""
from fractions import Fraction as F
from itertools import product
import unittest

def reciprocal_radius(gaps, directions, scenarios):
    """For one-dimensional or coordinate-axis directions, exact rational data."""
    return max([F(0)] + [
        max([F(0)] + [-sum(k[i]*d[i] for i in range(len(d))) for k in scenarios]) / g
        for g,d in zip(gaps,directions)
    ])

def hausdorff_singletons(a,b):
    return max(abs(x-y) for x,y in zip(a,b)) if len(a)==1 else None

class StabilityTests(unittest.TestCase):
    def test_exact_lipschitz_single_edge(self):
        count=0
        for gap, a, b in product(range(1,8), range(-12,13), range(-12,13)):
            q1=reciprocal_radius([F(gap)],[(F(1),)],[(F(a),)])
            q2=reciprocal_radius([F(gap)],[(F(1),)],[(F(b),)])
            self.assertLessEqual(abs(q1-q2),F(abs(a-b),gap))
            count+=1
        self.assertEqual(count,4375)

    def test_monotone_scenario_enrichment(self):
        for a,b in product(range(-9,10),repeat=2):
            q1=reciprocal_radius([F(2),F(3)],[(F(1),F(0)),(F(0),F(1))],[(F(a),F(0))])
            q2=reciprocal_radius([F(2),F(3)],[(F(1),F(0)),(F(0),F(1))],[(F(a),F(0)),(F(0),F(b))])
            self.assertGreaterEqual(q2,q1)

    def test_orientation_and_infinity(self):
        self.assertEqual(reciprocal_radius([F(2)],[(F(1),)],[(F(-1),),(F(3),)]),F(1,2))
        self.assertEqual(reciprocal_radius([F(1)],[(F(1),)],[(F(2),)]),F(0))

    def test_certificate(self):
        q=reciprocal_radius([F(2)],[(F(1),)],[(F(-1),)])
        delta=F(1,4)
        C=F(1,2)
        self.assertEqual((1/(q+C*delta),1/(q-C*delta)),(F(8,5),F(8,3)))

if __name__=="__main__":
    unittest.main()
