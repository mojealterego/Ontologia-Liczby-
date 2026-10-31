"""F21.2: exact rational verification of root certificates (no binary floats)."""
from __future__ import annotations

import math
import unittest
from fractions import Fraction
from itertools import product


def is_rational_square(q: Fraction) -> bool:
    if q < 0:
        return False
    p, s = q.numerator, q.denominator
    return math.isqrt(p) ** 2 == p and math.isqrt(s) ** 2 == s


def squarefree_parts(n: int) -> tuple[int, int]:
    if n < 1:
        raise ValueError("n must be positive")
    square, kernel = 1, 1
    p = 2
    remaining = n
    while p * p <= remaining:
        exponent = 0
        while remaining % p == 0:
            remaining //= p
            exponent += 1
        square *= p ** (exponent // 2)
        kernel *= p ** (exponent % 2)
        p += 1
    if remaining > 1:
        kernel *= remaining
    return kernel, square


def certified(a: Fraction, lower: Fraction, upper: Fraction) -> bool:
    return 0 <= lower <= upper and lower * lower <= a <= upper * upper


def bisect(a: Fraction, lower: Fraction, upper: Fraction, steps: int):
    if not certified(a, lower, upper):
        raise ValueError("invalid initial certificate")
    if steps < 0:
        raise ValueError("negative step count")
    for _ in range(steps):
        mid = (lower + upper) / 2
        if mid * mid <= a:
            lower = mid
        else:
            upper = mid
    return lower, upper


def newton(a: Fraction, x: Fraction) -> Fraction:
    if a <= 0 or x <= 0:
        raise ValueError("positive radicand and iterate required")
    return (x + a / x) / 2


def decimal_floor_root(a: Fraction, digits: int) -> int:
    if a < 0 or digits < 0:
        raise ValueError("nonnegative inputs required")
    h = 10 ** digits
    return math.isqrt(a.numerator * h * h // a.denominator)


def mul_quadratic(z: tuple[Fraction, Fraction], w: tuple[Fraction, Fraction], d: int):
    u, v = z
    r, s = w
    return u * r + d * v * s, u * s + v * r


def norm(z: tuple[Fraction, Fraction], d: int) -> Fraction:
    return z[0] * z[0] - d * z[1] * z[1]


class CertifiedRootTests(unittest.TestCase):
    def test_rational_square_criterion(self):
        for p in range(0, 45):
            for q in range(1, 31):
                a = Fraction(p, q)
                criterion = is_rational_square(a)
                n, d = a.numerator, a.denominator
                self.assertEqual(criterion, math.isqrt(n)**2 == n and math.isqrt(d)**2 == d)

    def test_reduced_fraction_necessity(self):
        self.assertTrue(is_rational_square(Fraction(2, 8)))
        self.assertEqual(Fraction(2, 8), Fraction(1, 4))

    def test_negative_rational_not_real_square(self):
        self.assertFalse(is_rational_square(Fraction(-1, 4)))

    def test_squarefree_decomposition(self):
        for n in range(1, 1500):
            s, t = squarefree_parts(n)
            self.assertEqual(s*t*t, n)
            self.assertTrue(all(s % (p*p) for p in range(2, math.isqrt(s)+1)))

    def test_isqrt_certificate(self):
        for n in range(0, 10000):
            k = math.isqrt(n)
            self.assertLessEqual(k*k, n)
            self.assertLess(n, (k+1)*(k+1))

    def test_certificate_rejects_negative_bound(self):
        self.assertFalse(certified(Fraction(2), Fraction(-1), Fraction(2)))

    def test_certificate_2(self):
        self.assertTrue(certified(Fraction(2), Fraction(7,5), Fraction(3,2)))

    def test_bisection_three_steps(self):
        self.assertEqual(bisect(Fraction(2), Fraction(1), Fraction(2), 3),
                         (Fraction(11,8), Fraction(3,2)))

    def test_bisection_width_and_invariant(self):
        for a in [Fraction(i,j) for i in range(0,16) for j in range(1,12)]:
            lo, hi = Fraction(0), max(Fraction(1), a)
            for steps in range(9):
                l, u = bisect(a, lo, hi, steps)
                self.assertTrue(certified(a, l, u))
                self.assertEqual(u-l, (hi-lo)/2**steps)

    def test_bisection_invalid_input(self):
        with self.assertRaises(ValueError):
            bisect(Fraction(2), Fraction(0), Fraction(1), 3)

    def test_newton_rational_example(self):
        self.assertEqual(newton(Fraction(2), Fraction(3,2)), Fraction(17,12))

    def test_newton_upper_certificate(self):
        for a in [Fraction(i,j) for i in range(1,30) for j in range(1,18)]:
            for x in [Fraction(k,2) for k in range(1,12)]:
                y = newton(a, x)
                self.assertGreaterEqual(y*y, a)
                self.assertTrue(certified(a, a/y, y))

    def test_newton_exact_residual(self):
        for a in [Fraction(i,j) for i in range(1,20) for j in range(1,13)]:
            for x in [Fraction(1), Fraction(3,2), Fraction(5,3)]:
                y = newton(a, x)
                self.assertEqual(y*y-a, (x*x-a)**2/(4*x*x))

    def test_newton_decreasing_from_upper(self):
        for a in [Fraction(2), Fraction(3,2), Fraction(17,10)]:
            x = max(Fraction(1), a)
            for _ in range(7):
                y = newton(a, x)
                self.assertLessEqual(y, x)
                self.assertGreaterEqual(y*y, a)
                x = y

    def test_newton_zero_rejected(self):
        with self.assertRaises(ValueError):
            newton(Fraction(2), Fraction(0))

    def test_decimal_floor(self):
        for a in [Fraction(0), Fraction(1,2), Fraction(2), Fraction(7,3), Fraction(49,64)]:
            for k in range(0,6):
                t = decimal_floor_root(a, k)
                h = 10**k
                self.assertLessEqual(Fraction(t*t, h*h), a)
                self.assertLess(a, Fraction((t+1)**2, h*h))

    def test_decimal_example(self):
        self.assertEqual(decimal_floor_root(Fraction(2), 3), 1414)

    def test_sqrt_holder_squared(self):
        # For x=sqrt(a), y=sqrt(b) chosen rationally, |x-y|^2 <= |x^2-y^2|.
        for x,y in product([Fraction(k,6) for k in range(0,25)], repeat=2):
            self.assertLessEqual((x-y)**2, abs(x*x-y*y))

    def test_lipschitz_away_from_zero_squared(self):
        # Delta=1, hence |x-y| <= |x^2-y^2|/2 for x,y>=1.
        for x,y in product([Fraction(k,6) for k in range(6,25)], repeat=2):
            self.assertLessEqual(2*abs(x-y), abs(x*x-y*y))

    def test_concavity_jensen_squared(self):
        for x,y in product([Fraction(k,7) for k in range(0,16)], repeat=2):
            for t in [Fraction(0), Fraction(1,4), Fraction(1,2), Fraction(3,4), Fraction(1)]:
                lhs_square = t*x*x+(1-t)*y*y
                rhs_square = (t*x+(1-t)*y)**2
                self.assertGreaterEqual(lhs_square, rhs_square)
                if t not in (0,1):
                    self.assertEqual(lhs_square==rhs_square, x==y)

    def test_norm_multiplicativity(self):
        d=2
        vals=[Fraction(-2),Fraction(-1,2),Fraction(0),Fraction(1),Fraction(3,2)]
        elements=list(product(vals, repeat=2))
        for z in elements:
            for w in elements:
                self.assertEqual(norm(mul_quadratic(z,w,d),d), norm(z,d)*norm(w,d))

    def test_inverse_quadratic(self):
        z=(Fraction(3),Fraction(2))
        self.assertEqual(norm(z,2),1)
        self.assertEqual(mul_quadratic(z,(Fraction(3),Fraction(-2)),2),(Fraction(1),Fraction(0)))

    def test_non_squarefree_failure(self):
        self.assertEqual(norm((Fraction(2),Fraction(1)),4),0)

    def test_tasks_selected(self):
        self.assertEqual(squarefree_parts(180),(5,6))
        self.assertEqual(math.isqrt(2026),45)
        self.assertEqual(Fraction(17,12)-Fraction(24,17),Fraction(1,204))
        self.assertLess(Fraction(1,7), Fraction(1,6))


if __name__ == '__main__':
    unittest.main()
