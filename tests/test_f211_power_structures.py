"""F21.1: exact finite regression checks; general proofs remain in manuscript."""
import math
import unittest
from fractions import Fraction as F


def mul(a, b, mod=None):
    c = (a[0]*b[0]+a[1]*b[2], a[0]*b[1]+a[1]*b[3],
         a[2]*b[0]+a[3]*b[2], a[2]*b[1]+a[3]*b[3])
    return tuple(x % mod for x in c) if mod else c


def power(a, n, mod=None):
    if n < 0:
        raise ValueError('only nonnegative matrix powers here')
    out = (1, 0, 0, 1)
    while n:
        if n & 1:
            out = mul(out, a, mod)
        a = mul(a, a, mod)
        n //= 2
    return out


def order_mod(a, n):
    if n < 2 or math.gcd(a, n) != 1:
        raise ValueError('unit residue required')
    x = 1
    for t in range(1, n + 1):
        x = (x*a) % n
        if x == 1:
            return t
    raise AssertionError('finite unit group guarantees an order')


def valuations(q):
    q = F(q)
    if q <= 0:
        raise ValueError('positive rational required')
    ans = {}
    for sign, val in ((1, q.numerator), (-1, q.denominator)):
        p = 2
        while p*p <= val:
            while val % p == 0:
                ans[p] = ans.get(p, 0) + sign
                val //= p
            p += 1
        if val > 1:
            ans[val] = ans.get(val, 0) + sign
    return {p: e for p, e in ans.items() if e}


def rational_power_certificate(a, m, n):
    if a <= 0 or n <= 0 or m == 0 or math.gcd(abs(m), n) != 1:
        raise ValueError('reduced nonzero rational exponent and positive base required')
    v = valuations(a)
    if any(e % n for e in v.values()):
        return None
    b = F(1)
    for p, e in v.items():
        b *= F(p) ** (e // n)
    result = b ** m
    assert result ** n == F(a) ** m
    return result


def negative_base_rational_power(a, m, n):
    if a >= 0 or n <= 0 or math.gcd(abs(m), n) != 1 or n % 2 == 0:
        raise ValueError('negative base requires reduced odd denominator')
    root = next((k for k in range(1, abs(a) + 1) if k ** n == abs(a)), None)
    if root is None:
        raise ValueError('test helper only handles integral roots')
    return F(-root) ** m


class PowerStructures(unittest.TestCase):
    def test_power_zero_identity(self): self.assertEqual(power((0, 0, 0, 0), 0), (1, 0, 0, 1))
    def test_monoid_exponent_additivity(self):
        a = (1, 2, 0, 1)
        for m in range(7):
            for n in range(7):
                self.assertEqual(power(a, m+n), mul(power(a, m), power(a, n)))
    def test_noncommuting_pair(self):
        a, b = (1, 1, 0, 1), (1, 0, 1, 1)
        self.assertNotEqual(mul(a, b), mul(b, a))
        self.assertNotEqual(power(mul(a, b), 2), mul(power(a, 2), power(b, 2)))
    def test_commuting_pair(self):
        a, b = (1, 2, 0, 1), (1, 3, 0, 1)
        for n in range(10):
            self.assertEqual(power(mul(a, b), n), mul(power(a, n), power(b, n)))
    def test_conjugation(self):
        u, ui, d = (1, 1, 0, 1), (1, -1, 0, 1), (2, 0, 0, 3)
        for n in range(7):
            self.assertEqual(power(mul(mul(u, d), ui), n), mul(mul(u, power(d, n)), ui))
    def test_conjugation_numeric(self):
        self.assertEqual(mul(mul((1, 1, 0, 1), (8, 0, 0, 27)), (1, -1, 0, 1)), (8, 19, 0, 27))
    def test_orders(self): self.assertEqual((order_mod(2, 7), order_mod(3, 10)), (3, 4))
    def test_modular_reduction(self):
        for n in range(2, 36):
            for a in range(1, n):
                if math.gcd(a, n) == 1:
                    t = order_mod(a, n)
                    for k in (0, 1, 2, 17, 100, 2026):
                        self.assertEqual(pow(a, k, n), pow(a, k % t, n))
    def test_modular_examples(self): self.assertEqual((pow(2, 100, 7), pow(3, 2026, 10)), (2, 9))
    def test_order_rejects_nonunit(self):
        with self.assertRaises(ValueError): order_mod(2, 10)
    def test_val_positive(self): self.assertEqual(valuations(F(18, 25)), {2: 1, 3: 2, 5: -2})
    def test_val_perfect_root(self): self.assertEqual(valuations(F(64, 729)), {2: 6, 3: -6})
    def test_rational_root_exact(self): self.assertEqual(rational_power_certificate(F(81, 16), 3, 4), F(27, 8))
    def test_rational_root_sixth(self): self.assertEqual(rational_power_certificate(F(64, 729), 5, 6), F(32, 243))
    def test_rational_root_irrational(self): self.assertIsNone(rational_power_certificate(F(18, 25), 1, 2))
    def test_rational_root_negative_exponent(self): self.assertEqual(rational_power_certificate(F(64, 729), -5, 6), F(243, 32))
    def test_rational_root_rejects_nonreduced(self):
        with self.assertRaises(ValueError): rational_power_certificate(F(16), 2, 4)
    def test_negative_base_odd_root(self):
        self.assertEqual(negative_base_rational_power(-32, 2, 5), F(4))
        self.assertEqual(negative_base_rational_power(-32, 3, 5), F(-8))
    def test_negative_base_even_root_rejected(self):
        with self.assertRaises(ValueError): negative_base_rational_power(-16, 1, 2)
    def test_negative_base_power_composition_failure(self):
        left = rational_power_certificate(negative_base_rational_power(-8, 2, 3), 3, 2)
        self.assertEqual(left, F(8))
        self.assertNotEqual(left, negative_base_rational_power(-8, 1, 1))
    def test_quadratic_commutation_equivalence_gl2_f2(self):
        mats = [(a,b,c,d) for a in range(2) for b in range(2)
                for c in range(2) for d in range(2) if (a*d-b*c) % 2]
        self.assertEqual(len(mats), 6)
        for a in mats:
            for b in mats:
                commute = mul(a,b,2) == mul(b,a,2)
                quadratic = power(mul(a,b,2),2,2) == mul(power(a,2,2),power(b,2,2),2)
                self.assertEqual(commute,quadratic)
    def test_frobenius_mod3(self):
        for x in range(3):
            for y in range(3):
                self.assertEqual(pow(x+y, 3, 3), (pow(x, 3, 3)+pow(y, 3, 3)) % 3)
    def test_noncommutative_frobenius_failure(self):
        x, y = (0, 1, 0, 0), (0, 0, 1, 0)
        self.assertEqual(power(x, 2, 2), (0, 0, 0, 0))
        self.assertEqual(power(y, 2, 2), (0, 0, 0, 0))
        self.assertEqual(power(tuple((a+b) % 2 for a, b in zip(x, y)), 2, 2), (1, 0, 0, 1))
    def test_integer_power_uniqueness(self):
        for a in (F(2), F(3, 2), F(5, 7)):
            for m in range(-6, 7):
                for n in range(-6, 7):
                    self.assertEqual(a ** (m+n), a ** m * a ** n)


if __name__ == '__main__':
    unittest.main()
