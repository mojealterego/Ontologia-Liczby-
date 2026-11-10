from fractions import Fraction as F
import unittest

def radius(gaps, scenarios):
    """Exact radius for finite K; None means infinity."""
    candidates=[]
    for gap, d in gaps:
        loss=max((-sum(k[i]*d[i] for i in range(len(d))) for k in scenarios))
        if loss>0:
            candidates.append(gap/loss)
    return min(candidates) if candidates else None

class TestHV(unittest.TestCase):
    def test_interval(self):
        self.assertEqual(radius([(F(6),(F(2),))],[(F(-2),),(F(4),)]),F(3,2))
    def test_box(self):
        edges=[(F(2),(F(1),F(0))),(F(3),(F(0),F(1)))]
        scenarios=[(F(-1),F(-2)),(F(0),F(0))]
        self.assertEqual(radius(edges,scenarios),F(3,2))
    def test_no_destructive_direction(self):
        self.assertIsNone(radius([(F(1),(F(1),))],[(F(1),),(F(2),)]))
    def test_convex_hull_invariance_grid(self):
        for a in range(-8,9):
            for b in range(-8,9):
                for gap in range(1,8):
                    ends=[(F(a),),(F(b),)]
                    mid=[(F(a+b,2),)]
                    self.assertEqual(radius([(F(gap),(F(1),))],ends),
                                     radius([(F(gap),(F(1),))],ends+mid))
if __name__=="__main__":
    unittest.main()
