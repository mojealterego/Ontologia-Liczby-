"""MSC 97D40 III-E: exact finite checks of reliability and threshold bounds."""
import itertools
import math
import unittest

class MeasurementReliability(unittest.TestCase):
    def test_mse_bias_variance(self):
        # A two-point estimator theta + bias +/- sqrt(variance)
        # has exact expectation theta+bias and exact MSE variance+bias**2.
        for variance in range(10):
            for bias in range(-5, 6):
                theta = 7.0
                values = [theta + bias - math.sqrt(variance),
                          theta + bias + math.sqrt(variance)]
                expectation = sum(values) / 2
                actual_variance = sum((x - expectation)**2 for x in values) / 2
                actual_mse = sum((x - theta)**2 for x in values) / 2
                self.assertAlmostEqual(expectation-theta, bias)
                self.assertAlmostEqual(actual_variance, variance)
                self.assertAlmostEqual(actual_mse, variance + bias*bias)
        self.assertEqual(4+3*3, 13)
    def test_equicorrelation_bounds(self):
        for n in range(2,15):
            for k in range(-100,101):
                rho=k/100
                admissible=(-1/(n-1)<=rho<=1)
                eigmin=min(1-rho,1+(n-1)*rho)
                self.assertEqual(admissible,eigmin>=-1e-12)
    def test_variance_mean(self):
        for n in range(2,12):
            for sigma2 in (1,4,9):
                for rho in (0,1,-1/(n-1)):
                    direct=(n*sigma2+n*(n-1)*rho*sigma2)/(n*n)
                    formula=sigma2*(1+(n-1)*rho)/n
                    self.assertAlmostEqual(direct,formula)
                    self.assertGreaterEqual(formula,-1e-12)
    def test_chebyshev_sample_bound(self):
        for sigma2 in (1,4,9):
            for h in (1,2,3):
                for alpha in (.01,.05,.1):
                    n=math.ceil(sigma2/(alpha*h*h))
                    self.assertLessEqual(sigma2/(n*h*h),alpha+1e-12)
    def test_threshold_stability(self):
        for theta,t,e in itertools.product(range(-8,9),range(-8,9),range(4)):
            if theta<t-e:
                for error in range(-e,e+1):
                    self.assertLess(theta+error,t)
            if theta>=t+e:
                for error in range(-e,e+1):
                    self.assertGreaterEqual(theta+error,t)
    def test_threshold_from_observation(self):
        for observed,t,e in itertools.product(range(-6,7),range(-6,7),range(4)):
            if abs(observed-t)>e:
                for theta in range(observed-e,observed+e+1):
                    self.assertEqual(observed>t,theta>t)
    def test_positive_scale(self):
        for y,t,a,b in itertools.product(range(-3,4),range(-3,4),(1,2,3),(-2,0,2)):
            self.assertEqual(y>=t,a*y+b>=a*t+b)
    def test_negative_scale_counterexample(self):
        self.assertNotEqual(1>=0,-1>=0)

if __name__=="__main__":
    unittest.main()
