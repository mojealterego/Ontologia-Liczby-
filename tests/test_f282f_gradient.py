import unittest
from fractions import Fraction as F

class GradientF282F(unittest.TestCase):
    def test_quadratic_one_step(self):
        for x in range(-10,11):
            self.assertEqual(F(x)-F(x),0)
    def test_half_step(self):
        self.assertEqual(F(3)-F(3,2),F(3,2))
        self.assertEqual(F(3,2)**2/2,F(9,8))
    def test_rate_bound(self):
        self.assertEqual(F(3,4)**3*16,F(27,4))
    def test_divergent_step(self):
        x=F(1)
        for _ in range(8): x=x-3*x
        self.assertEqual(abs(x),256)
    def test_stationarity_average_bound(self):
        self.assertEqual(2*F(2,8),F(1,2))
    def test_distance_certificate(self):
        self.assertEqual(2*F(1,100)/2,F(1,100))

if __name__=="__main__": unittest.main()
