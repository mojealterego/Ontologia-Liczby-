"""F27.1: exact-rational checks of discrete-iteration certificates.

These are finite verification experiments, not machine proofs of theorems.
"""
from __future__ import annotations

import unittest
from fractions import Fraction as Q
from itertools import product
from pathlib import Path


def trajectory(q: Q, b: Q, x0: Q, errors: list[Q]) -> list[Q]:
    x = x0
    out = [x]
    for e in errors:
        x = q * x + b + e
        out.append(x)
    return out


def certificate(q: Q, b: Q, x0: Q, errors: list[Q]) -> Q:
    assert q != 1
    n = len(errors)
    L = b / (1 - q)
    return q**n * (x0 - L) + sum(
        (q**(n - 1 - k) * e for k, e in enumerate(errors)), Q(0)
    )


def geometric_bound(rho: Q, initial: Q, errors: list[Q]) -> Q:
    assert 0 <= rho < 1
    n = len(errors)
    return rho**n * abs(initial) + sum(
        (rho**(n - 1 - k) * abs(e) for k, e in enumerate(errors)), Q(0)
    )


def cesaro(seq: list[Q]) -> Q:
    if not seq:
        raise ValueError("nonempty sequence required")
    return sum(seq, Q(0)) / len(seq)


class TestF271(unittest.TestCase):
    def test_T2_empty_error_list(self):
        self.assertEqual(certificate(Q(1, 2), Q(1), Q(0), []), Q(-2))

    def test_T2_exact_enumeration(self):
        for q, b, x0 in product([Q(-1, 2), Q(0), Q(1, 3), Q(3, 4)], [Q(-2), Q(0), Q(3)], [Q(-3), Q(0), Q(2)]):
            for n in range(5):
                errors = [Q((k % 3) - 1, 7) for k in range(n)]
                L = b / (1 - q)
                self.assertEqual(trajectory(q, b, x0, errors)[-1] - L, certificate(q, b, x0, errors))

    def test_T2_signed_errors(self):
        self.assertEqual(certificate(Q(-1, 2), Q(3), Q(0), [Q(1), Q(-2)]), Q(-3))

    def test_T2_bound(self):
        for q in [Q(-3, 4), Q(-1, 3), Q(0), Q(1, 2)]:
            for n in range(1, 9):
                errors = [Q((-1)**k * (k + 1), 50) for k in range(n)]
                self.assertLessEqual(abs(certificate(q, Q(2), Q(-3), errors)), geometric_bound(abs(q), Q(-3) - Q(2) / (1 - q), errors))

    def test_T3_geometric_sum(self):
        for rho in [Q(0), Q(1, 3), Q(3, 4)]:
            for n in range(0, 15):
                self.assertEqual(sum((rho**k for k in range(n)), Q(0)), (1-rho**n)/(1-rho))

    def test_T3_constant_error(self):
        for n in range(1, 15):
            seq = trajectory(Q(1, 2), Q(0), Q(0), [Q(1, 100)] * n)
            self.assertEqual(seq[-1], Q(1, 50) * (1-Q(1, 2)**n))

    def test_T3_alternating_error_no_limit(self):
        seq = trajectory(Q(0), Q(0), Q(0), [Q((-1)**k, 10) for k in range(12)])
        self.assertEqual(seq[1::2], [Q(1, 10)] * 6)
        self.assertEqual(seq[2::2], [Q(-1, 10)] * 6)

    def test_T4_errors_tend_to_zero_example(self):
        seq = trajectory(Q(1, 2), Q(0), Q(0), [Q(1, k+1) for k in range(100)])
        self.assertLess(abs(seq[-1]), Q(1, 20))

    def test_T5_invariant_closed_ball(self):
        for q in [Q(-3, 4), Q(-1, 2), Q(0), Q(3, 4)]:
            for x in [Q(-1, 10), Q(-1, 20), Q(0), Q(1, 20), Q(1, 10)]:
                for e in [Q(-1, 40), Q(0), Q(1, 40)]:
                    self.assertLessEqual(abs(q*x+e), Q(1, 10))

    def test_T5_bound_is_sharp(self):
        self.assertGreater(Q(3, 4)*Q(1, 10)+Q(1, 39), Q(1, 10))

    def test_T6_residual_identity(self):
        for q in [Q(-3, 4), Q(0), Q(1, 4), Q(5, 4)]:
            for x in [Q(-5), Q(0), Q(1, 7), Q(5)]:
                b = Q(3)
                L = b/(1-q)
                self.assertEqual(abs(x-L), abs(x-(q*x+b))/abs(1-q))

    def test_T6_perturbed_step_not_residual(self):
        q,b,x,e = Q(1, 2),Q(1),Q(0),Q(1)
        L=b/(1-q)
        self.assertNotEqual(abs(x-L), abs((q*x+b+e)-x)/abs(1-q))

    def test_T7_contraction_bound(self):
        for rho in [Q(0), Q(1, 4), Q(2, 3)]:
            x0 = Q(7)
            x = x0
            for n in range(0, 10):
                self.assertLessEqual(abs(x), rho**n/(1-rho)*abs(rho*x0-x0))
                x *= rho

    def test_T7_aposteriori_bound(self):
        rho = Q(2, 5)
        x0 = Q(7)
        for n in range(1, 12):
            xn = x0*rho**n
            previous = x0*rho**(n-1)
            self.assertLessEqual(abs(xn), rho/(1-rho)*abs(xn-previous))

    def test_T7_incomplete_space(self):
        x = Q(1, 2)
        for _ in range(20):
            x /= 2
            self.assertGreater(x, 0)
            self.assertLess(x, 1)

    def test_T8_increment_certificate(self):
        rho, C = Q(1, 2), Q(5)
        for n in range(0, 15):
            partial = sum((C*rho**k for k in range(n)), Q(0))
            limit = C/(1-rho)
            self.assertEqual(limit-partial, C*rho**n/(1-rho))

    def test_T8_harmonic_not_geometric(self):
        for n in [20, 50, 100]:
            self.assertGreater(Q(1, n+1), Q(10)*(Q(1, 2)**n))

    def test_T9_variable_coefficients(self):
        x=Q(8)
        for n in range(3):
            x = Q((-1)**n, 4)*x
        self.assertEqual(abs(x), Q(1, 8))

    def test_T9_variable_bound(self):
        x=Q(3)
        rho=Q(1, 2)
        for n in range(1, 25):
            q=Q((-1)**n, n+3)
            e=Q((-1)**n, n+5)
            x=q*x+e
            self.assertLessEqual(abs(x), Q(3)*rho**n+sum((rho**(n-1-k)*Q(1,k+6) for k in range(n)), Q(0)))

    def test_T10_cesaro_exact(self):
        for n in range(1, 20):
            seq=[Q(2)+Q(1,2)**k for k in range(n)]
            self.assertEqual(cesaro(seq)-Q(2), (1-Q(1,2)**n)/(Q(n)*(1-Q(1,2))))

    def test_T10_nonempty_precondition(self):
        with self.assertRaises(ValueError):
            cesaro([])

    def test_K3_harmonic_growth(self):
        s=Q(0)
        for k in range(1, 1025):
            s+=Q(1,k)
        self.assertGreater(s,Q(7))

    def test_K5_no_uniform_modulus(self):
        for proposed_N in [0,1,5,50]:
            M=proposed_N+1
            self.assertEqual(Q(0) if proposed_N<M else Q(1), Q(0))
            self.assertEqual(Q(1) if M<M else Q(0), Q(0))

    def test_K6_square_indicator(self):
        seq=[int(__import__('math').isqrt(k)**2==k) for k in range(1,1001)]
        self.assertEqual(sum(seq),31)
        self.assertIn(0,seq[900:])
        self.assertIn(1,seq[900:])

    def test_Z1(self):
        self.assertEqual(abs(trajectory(Q(1,3),Q(2),Q(0),[Q(0)]*5)[-1]-Q(3)),Q(1,81))

    def test_Z2(self):
        self.assertEqual(abs(trajectory(Q(-1,2),Q(3),Q(0),[Q(0)]*4)[-1]-Q(2)),Q(1,8))

    def test_Z3(self):
        self.assertEqual(geometric_bound(Q(1,2),Q(0),[Q(1,100)]*7),Q(1,50)*(1-Q(1,2)**7))

    def test_Z4(self):
        self.assertEqual((1-Q(3,4))*Q(1,10),Q(1,40))

    def test_Z5(self):
        self.assertEqual(Q(5)-(Q(5,4)+Q(3)),Q(3,4))

    def test_Z6(self):
        self.assertEqual(Q(2)*Q(1,3)**4/(1-Q(1,3)),Q(1,27))

    def test_Z7(self):
        self.assertEqual(Q(5)*Q(1,2)**6/(1-Q(1,2)),Q(5,32))

    def test_Z8(self):
        self.assertEqual(Q(8)*Q(1,4)**3,Q(1,8))

    def test_Z9(self):
        self.assertEqual(cesaro([Q(1,2)**k for k in range(10)]),(1-Q(1,2)**10)/5)

    def test_Z10(self):
        self.assertEqual(trajectory(Q(0),Q(0),Q(0),[Q((-1)**k,10) for k in range(4)])[1:], [Q(1,10),Q(-1,10),Q(1,10),Q(-1,10)])

    def test_Z11(self):
        for numerator in range(1,11):
            eps=Q(numerator,100)
            n=0
            while Q(4,2**n)>=eps:
                n+=1
            self.assertLess(Q(4,2**n),eps)
            if n>0:self.assertGreaterEqual(Q(4,2**(n-1)),eps)

    def test_source_structure(self):
        source=Path(__file__).resolve().parents[1]/'manuscript/tom-01/F27/F27.1_UZUPELNIENIE_CERTYFIKATY_ITERACJI.md'
        content=source.read_text(encoding='utf-8')
        for prefix,count in [('**D',8),('**T',10),('**K',6),('**Z',12)]:
            self.assertEqual(sum(f'{prefix}{i} ' in content or f'{prefix}{i} (' in content or f'{prefix}{i}.' in content for i in range(1,count+1)),count)
        self.assertIn('585/1222',content)


if __name__=='__main__':
    unittest.main()
