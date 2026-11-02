"""Checks for MSC 97D40 III-G: bounded rewards and confidence radii."""
import math
import unittest

class TaskSelection(unittest.TestCase):
    def test_radius_decreases(self):
        for m in range(1,9):
            for delta in (.01,.05,.1,.5):
                radius=lambda n:math.sqrt(math.log(2*m/delta)/(2*n))
                for n in range(1,60):
                    self.assertGreater(radius(n),radius(n+1))
    def test_regret_bound_algebra(self):
        for m in range(2,6):
            for delta in (.05,.1):
                for n in range(1,50):
                    radius=math.sqrt(math.log(2*m/delta)/(2*n))
                    self.assertAlmostEqual(2*radius,math.sqrt(2*math.log(2*m/delta)/n))
    def test_union_budget(self):
        for m in range(1,100):
            for delta in (.01,.1,.5):
                self.assertAlmostEqual(m*(delta/m),delta)
    def test_empirical_mean_bounded(self):
        for values in ((0,0,0),(0,1,1),(1,1,1),(.1,.7,.4)):
            avg=sum(values)/len(values)
            self.assertLessEqual(avg,1)
            self.assertGreaterEqual(avg,0)
    def test_regret(self):
        means=[.7,.5]
        self.assertAlmostEqual(max(means)-means[1],.2)
        self.assertEqual(max(means)-means[0],0)
    def test_example_values(self):
        self.assertAlmostEqual(math.sqrt(math.log(40)/200),.13581015157406195)
        self.assertAlmostEqual(math.sqrt(2*math.log(40)/200),.19206455826398416)
    def test_budget(self):
        self.assertEqual(4*25,100)

if __name__=="__main__":
    unittest.main()
