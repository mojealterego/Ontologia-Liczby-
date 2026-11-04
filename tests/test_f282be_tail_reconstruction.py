import unittest
from fractions import Fraction as F

def h(values, masses, t):
    assert len(values) == len(masses) and sum(masses) == 1 and 0 <= t <= 1
    remaining = t
    result = F(0)
    for x, p in sorted(zip(values, masses), reverse=True):
        take = min(remaining, p)
        result += x * take
        remaining -= take
        if remaining == 0:
            break
    return result

class TailReconstruction(unittest.TestCase):
    def test_two_atoms(self):
        self.assertEqual(h([F(3),F(1)],[F(1,4),F(3,4)],F(1,2)), F(1))
    def test_mean(self):
        self.assertEqual(h([F(4),F(-1)],[F(1,3),F(2,3)],F(1)), F(2,3))
    def test_translation(self):
        for i in range(11):
            t=F(i,10)
            self.assertEqual(h([F(5),F(3)],[F(1,4),F(3,4)],t),h([F(3),F(1)],[F(1,4),F(3,4)],t)+2*t)
    def test_rearrangement(self):
        for i in range(11):
            t=F(i,10)
            self.assertEqual(h([F(0),F(2)],[F(1,2),F(1,2)],t),h([F(2),F(0)],[F(1,2),F(1,2)],t))
    def test_monotonicity(self):
        for i in range(11):
            t=F(i,10)
            self.assertLessEqual(h([F(1),F(-1)],[F(1,2),F(1,2)],t),h([F(2),F(0)],[F(1,2),F(1,2)],t))
    def test_lipschitz(self):
        for i in range(11):
            t=F(i,10)
            a=h([F(3),F(1)],[F(1,4),F(3,4)],t)
            b=h([F(4),F(0)],[F(1,4),F(3,4)],t)
            self.assertLessEqual(abs(a-b),t)
if __name__ == "__main__":
    unittest.main()
