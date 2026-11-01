"""F27.3 — exact rational checks; finite tests are not formal proofs."""
from fractions import Fraction as Q
from itertools import product
import unittest

# (exercise, numerator linear a*n+b, denominator linear c*n+d, printed limit)
SOURCE_EXERCISES = (
    (1, 3, 2, 2, 3, Q(3, 2)),
    (2, 3, 4, 4, 3, Q(4, 3)),
    (3, 4, 5, 5, 4, Q(5, 4)),
    (4, 1, 6, 6, 5, Q(6)),
    (5, 2, 7, 7, 1, Q(7, 2)),
    (6, 3, 2, 8, 2, Q(8, 3)),
    (7, 4, 3, 2, 3, Q(1, 2)),
    (8, 1, 4, 3, 4, Q(3)),
    (9, 2, 5, 4, 5, Q(2)),
    (10, 3, 6, 5, 1, Q(5, 3)),
    (11, 4, 7, 6, 2, Q(3, 2)),
    (12, 1, 2, 7, 3, Q(7)),
    (13, 2, 3, 8, 4, Q(4)),
    (14, 3, 4, 2, 5, Q(2, 3)),
    (15, 4, 5, 3, 1, Q(3, 4)),
    (16, 1, 6, 4, 2, Q(4)),
    (17, 2, 7, 5, 3, Q(5, 2)),
    (18, 3, 2, 6, 4, Q(2)),
    (19, 4, 3, 7, 5, Q(7, 4)),
    (20, 8, 1, 1, 4, Q(8)),
    (21, 2, 5, 2, 2, Q(1)),
    (22, 3, 6, 3, 3, Q(1)),
    (23, 4, 7, 4, 4, Q(1)),
    (24, 1, 2, 5, 5, Q(5)),
)


def linear_ratio_limit(a: int, b: int, c: int, d: int) -> Q:
    if c == 0:
        raise ValueError('leading denominator coefficient must be nonzero')
    return Q(a, c)


def linear_ratio_error(a: int, b: int, c: int, d: int, n: int) -> Q:
    if c == 0 or c*n + d == 0:
        raise ZeroDivisionError
    return abs(Q(a*n+b, c*n+d)-Q(a, c))


def exact_linear_ratio_error(a: int, b: int, c: int, d: int, n: int) -> Q:
    if c == 0 or c*n + d == 0:
        raise ZeroDivisionError
    return Q(abs(b*c-a*d), abs(c)*abs(c*n+d))


def strict_threshold_for_reciprocal(eps: Q) -> int:
    if eps <= 0:
        raise ValueError('epsilon must be positive')
    x = 1 / eps
    return x.numerator // x.denominator


def geometric_sum(c: Q, q: Q, n: int) -> Q:
    if not 0 < q < 1 or n < 0:
        raise ValueError
    return c * (1 - q**(n+1)) / (1 - q)


def geometric_tail(c: Q, q: Q, n: int) -> Q:
    if not 0 < q < 1 or n < 0:
        raise ValueError
    return c * q**(n+1) / (1 - q)


def telescoping_sum(n: int) -> Q:
    if n < 1:
        raise ValueError
    return sum((Q(1, k*(k+1)) for k in range(1, n+1)), Q(0))


def interval_certificate(n: int):
    if n < 0:
        raise ValueError
    d = Q(1, n+1)
    return Q(1)-d, Q(1)+d


class TestF273(unittest.TestCase):
    def test_source_24_exercises_distinct(self):
        self.assertEqual(len(SOURCE_EXERCISES), 24)
        self.assertEqual({x[0] for x in SOURCE_EXERCISES}, set(range(1,25)))

    def test_errata_exact_count(self):
        wrong = [row[0] for row in SOURCE_EXERCISES if Q(row[1], row[3]) != row[5]]
        self.assertEqual(wrong, list(range(2,20))+[24])
        self.assertEqual(len(wrong), 19)

    def test_source_correct_exercises(self):
        good = [row[0] for row in SOURCE_EXERCISES if Q(row[1], row[3]) == row[5]]
        self.assertEqual(good, [1,20,21,22,23])

    def test_source_exact_limits(self):
        for number, a,b,c,d,printed in SOURCE_EXERCISES:
            with self.subTest(number=number):
                self.assertEqual(linear_ratio_limit(a,b,c,d), Q(a,c))

    def test_source_error_identity_all_24(self):
        for _,a,b,c,d,_ in SOURCE_EXERCISES:
            for n in (1,2,3,7,25,1000):
                self.assertEqual(linear_ratio_error(a,b,c,d,n),
                                 exact_linear_ratio_error(a,b,c,d,n))

    def test_source_convergence_certified(self):
        for _,a,b,c,d,_ in SOURCE_EXERCISES:
            for eps in (Q(1,10), Q(1,100), Q(1,1000)):
                n=0
                while exact_linear_ratio_error(a,b,c,d,n) >= eps:
                    n += 1
                self.assertLess(exact_linear_ratio_error(a,b,c,d,n),eps)
                for j in range(n,n+50):
                    self.assertLess(exact_linear_ratio_error(a,b,c,d,j),eps)

    def test_invalid_denominator(self):
        with self.assertRaises(ZeroDivisionError):
            exact_linear_ratio_error(1,2,1,-2,2)

    def test_invalid_leading_denominator(self):
        with self.assertRaises(ValueError):
            linear_ratio_limit(1,2,0,3)

    def test_reciprocal_strict_threshold(self):
        for eps in (Q(1,100), Q(1,5), Q(3,4), Q(5,2)):
            n = strict_threshold_for_reciprocal(eps)
            self.assertLess(Q(1,n+1),eps)
            if n:
                self.assertGreaterEqual(Q(1,n),eps)

    def test_reciprocal_invalid(self):
        for eps in (Q(0), Q(-1)):
            with self.assertRaises(ValueError):
                strict_threshold_for_reciprocal(eps)

    def test_finite_modification_convergence(self):
        a = lambda n: Q(1,n+1)
        b = lambda n: Q(99) if n < 200 else a(n)
        self.assertEqual([a(n) for n in range(200,220)],
                         [b(n) for n in range(200,220)])

    def test_finite_modification_attainment_changes(self):
        a = lambda n: Q(1,n+1)
        b = lambda n: Q(0) if n == 3 else a(n)
        self.assertNotIn(Q(0), [a(n) for n in range(100)])
        self.assertIn(Q(0), [b(n) for n in range(100)])

    def test_monotone_supremum(self):
        vals=[Q(1)-Q(1,n+1) for n in range(1000)]
        self.assertEqual(vals, sorted(vals))
        self.assertTrue(all(v < 1 for v in vals))

    def test_monotone_tail_error(self):
        for n in range(1,60):
            self.assertEqual(max(Q(1)- (Q(1)-Q(1,k+1)) for k in range(n,n+60)),
                             Q(1,n+1))

    def test_oscillating_tail_error(self):
        for n in range(0,50):
            vals=[abs(Q((-1)**k,k+1)) for k in range(n,n+40)]
            self.assertEqual(max(vals),Q(1,n+1))

    def test_geometric_identity_exhaustive(self):
        for c in (Q(1),Q(3,2),Q(5)):
            for q in (Q(1,2),Q(1,3),Q(3,4)):
                for n in range(0,15):
                    finite=sum((c*q**k for k in range(n+1)),Q(0))
                    self.assertEqual(finite,geometric_sum(c,q,n))
                    self.assertEqual(finite+geometric_tail(c,q,n),c/(1-q))

    def test_geometric_positive_nonattainment(self):
        for q in (Q(1,2),Q(1,4),Q(9,10)):
            for n in range(20):
                self.assertGreater(geometric_tail(Q(1),q,n),0)

    def test_geometric_invalid_q(self):
        for q in (Q(-1),Q(0),Q(1),Q(2)):
            with self.assertRaises(ValueError):
                geometric_tail(Q(1),q,4)

    def test_dominated_geometric_tail(self):
        for n in range(0,20):
            q=Q(1,4)
            partial=sum(((-q)**k for k in range(n+1)),Q(0))
            exact=Q(1)/(1+q)-partial
            self.assertLessEqual(abs(exact),geometric_tail(Q(1),q,n))

    def test_telescoping_all(self):
        for n in range(1,150):
            self.assertEqual(telescoping_sum(n),Q(1)-Q(1,n+1))

    def test_telescoping_nonattainment(self):
        for n in range(1,150):
            self.assertGreater(Q(1)-telescoping_sum(n),0)

    def test_alternating_leibniz(self):
        # Use geometric alternating terms: exact limit and exact remainder.
        for q in (Q(1,2),Q(1,3),Q(1,4)):
            for n in range(20):
                partial=sum(((-q)**k for k in range(n+1)),Q(0))
                residual=Q(1)/(1+q)-partial
                self.assertGreater((-1)**(n+1)*residual,0)
                self.assertLessEqual(abs(residual),q**(n+1))

    def test_interval_nested(self):
        for n in range(1,100):
            l0,u0=interval_certificate(n-1)
            l1,u1=interval_certificate(n)
            self.assertLessEqual(l0,l1)
            self.assertLessEqual(u1,u0)
            self.assertLessEqual(l1,Q(1))
            self.assertLessEqual(Q(1),u1)

    def test_interval_diameter(self):
        for n in range(100):
            l,u=interval_certificate(n)
            self.assertEqual(u-l,Q(2,n+1))

    def test_interval_invalid(self):
        with self.assertRaises(ValueError):
            interval_certificate(-1)

    def test_two_parity_limits(self):
        for n in (10,100,1000):
            even=Q(1)+Q(1,n+1)
            odd=Q(2)-Q(1,n+1)
            self.assertLess(abs(even-1),Q(1,n))
            self.assertLess(abs(odd-2),Q(1,n))

    def test_two_parity_nonconvergence(self):
        self.assertGreater(Q(2)-Q(1),Q(1,2))

    def test_double_limit_m_fixed(self):
        for m in (1,2,100):
            self.assertLess(Q(m,m+1000*m),Q(1,1000))

    def test_double_limit_n_fixed(self):
        for n in (1,2,100):
            self.assertLess(Q(1)-Q(1000*n,1000*n+n),Q(1,1000))

    def test_z1(self):
        self.assertEqual(strict_threshold_for_reciprocal(Q(1,100)),100)

    def test_z2(self):
        self.assertEqual(Q(1,100),Q(1)- (Q(1)-Q(1,100)))

    def test_z3(self):
        self.assertEqual(max(abs(Q((-1)**n,n+1)) for n in range(9,100)),Q(1,10))

    def test_z4(self):
        self.assertEqual(geometric_sum(Q(1),Q(1,3),4),Q(3,2)-Q(1,162))

    def test_z5(self):
        self.assertEqual(telescoping_sum(19),Q(19,20))

    def test_z6(self):
        # Finite paired tails of the harmonic alternating series have the
        # prescribed sign and are bounded by the first omitted term.
        for pairs in range(1, 60):
            residual = sum((Q((-1)**(k+1), k) for k in range(101, 101+2*pairs)), Q(0))
            self.assertGreater(residual, 0)
            self.assertLessEqual(residual, Q(1,101))

    def test_z7(self):
        self.assertEqual(Q(4,5)-Q(13,16),-Q(1,80))
        self.assertEqual(geometric_tail(Q(1),Q(1,4),2),Q(1,48))

    def test_z8(self):
        self.assertEqual(interval_certificate(49),(Q(49,50),Q(51,50)))

    def test_z9(self):
        for n in (10,100,1000):
            even = Q(1)+Q(1,n+1)
            odd = Q(2)-Q(1,n+1)
            self.assertLess(abs(even-Q(1)), Q(1,n))
            self.assertLess(abs(odd-Q(2)), Q(1,n))
            self.assertGreater(odd-even, Q(1,2))

    def test_z10(self):
        self.assertNotIn(Q(1),{Q(1)-Q(1,n+1) for n in range(500)})

    def test_z11(self):
        for fixed in (1,3,17):
            self.assertLess(Q(fixed, fixed+1000*fixed),Q(1,1000))
            self.assertLess(Q(1)-Q(1000*fixed, 1001*fixed),Q(1,1000))

    def test_z12(self):
        self.assertEqual(linear_ratio_limit(3,4,4,3),Q(3,4))
        self.assertEqual(exact_linear_ratio_error(3,4,4,3,43),Q(7,4*(4*43+3)))
        self.assertGreaterEqual(exact_linear_ratio_error(3,4,4,3,43),Q(1,100))
        self.assertLess(exact_linear_ratio_error(3,4,4,3,44),Q(1,100))


if __name__ == '__main__':
    unittest.main()
