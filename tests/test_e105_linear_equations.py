"""Exact arithmetic and case-splitting tests for E1-05."""
import unittest
from fractions import Fraction as F

def solve(a, b, domain=None):
    """Solve ax+b=0 on Q, or filter through an optional predicate."""
    a, b = F(a), F(b)
    if a == 0:
        return "all" if b == 0 else "none"
    x = -b / a
    return x if domain is None or domain(x) else "none"

def param_case(t):
    """(t**2-4)x=t+2, including singular parameters."""
    t = F(t)
    return solve(t*t - 4, -t - 2)

class LinearEquations(unittest.TestCase):
    def test_unique_solutions(self):
        for a in range(-9, 10):
            if not a:
                continue
            for b in range(-9, 10):
                x = solve(a, b)
                self.assertEqual(F(a)*x+F(b), 0)

    def test_degenerate_cases(self):
        self.assertEqual(solve(0, 0), "all")
        self.assertEqual(solve(0, 1), "none")

    def test_equivalent_additions(self):
        for x in range(-10, 11):
            for h in range(-4, 5):
                self.assertEqual(3*x-7 == 11, 3*x-7+h == 11+h)

    def test_equivalent_nonzero_multiplication(self):
        for x in range(-10, 11):
            for g in [-7, -2, 1, 3, 11]:
                self.assertEqual(x == 1, g*x == g)

    def test_invalid_multiplication_counterexample(self):
        self.assertEqual({x for x in range(-2, 4) if x == 1}, {1})
        self.assertEqual({x for x in range(-2, 4) if x*x == x}, {0, 1})

    def test_parameter_cases(self):
        self.assertEqual(param_case(-2), "all")
        self.assertEqual(param_case(2), "none")
        for t in [-10, -3, -1, 0, 1, 3, 7]:
            self.assertEqual(param_case(t), F(1, t-2))

    def test_domain_filter(self):
        self.assertEqual(solve(2, -3, lambda x: x.denominator == 1), "none")
        self.assertEqual(solve(2, -4, lambda x: x.denominator == 1), F(2))

    def test_residual_error_identity(self):
        for a in [-7, -1, F(1,100), F(1,500), 2, 11]:
            for b in [-5, 0, 3]:
                root = solve(a,b)
                for guess in [-4, 0, 2, 99]:
                    residual = F(a)*guess+F(b)
                    self.assertEqual(abs(F(guess)-root), abs(residual)/abs(F(a)))

    def test_absolute_value_branches(self):
        for a in [-5, -1, 2, 7]:
            for b in [-4, 0, 3]:
                for c in [1, 2, 5]:
                    roots = {F(c-b,a), F(-c-b,a)}
                    self.assertEqual(len(roots), 2)
                    for x in roots:
                        self.assertEqual(abs(F(a)*x+b), c)

    def test_fraction_examples(self):
        self.assertEqual(solve(F(5,6), -10), 12)
        self.assertEqual(solve(F(1,4), -F(7,4)), 7)
        self.assertEqual(solve(F(3,10), -F(7,5)), F(14,3))

    def test_integer_model(self):
        self.assertEqual(solve(14, -95, lambda x: x.denominator == 1 and x >= 0), "none")
        self.assertEqual(solve(12, -48, lambda x: x.denominator == 1 and x >= 0), 4)

if __name__ == "__main__":
    unittest.main()
