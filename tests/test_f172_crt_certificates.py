"""Deterministic exhaustive tests for Tom I F17.2 CRT certificate supplement.
No third-party dependencies; all computations use exact Python integers.
"""
import math
import unittest


def egcd(a: int, b: int) -> tuple[int, int, int]:
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r:
        q, rem = divmod(old_r, r)
        old_r, r = r, rem
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t
    if old_r < 0:
        return -old_r, -old_s, -old_t
    return old_r, old_s, old_t


def crt(a: int, m: int, b: int, n: int) -> tuple[int, int] | None:
    if m < 1 or n < 1:
        raise ValueError("moduli must be positive")
    d, u, _ = egcd(m, n)
    if (b - a) % d:
        return None
    period = math.lcm(m, n)
    x = (a + m * u * ((b - a) // d)) % period
    return x, period


def projectors(m: int, n: int) -> tuple[int, int]:
    if m < 2 or n < 2 or math.gcd(m, n) != 1:
        raise ValueError("projectors require coprime moduli >=2")
    _, u, _ = egcd(n, m)
    _, v, _ = egcd(m, n)
    return (n * u) % (m * n), (m * v) % (m * n)


class TestF172Certificates(unittest.TestCase):
    def test_bezout_certificates(self):
        for a in range(-35, 36):
            for b in range(-35, 36):
                if not (a or b):
                    continue
                d, u, v = egcd(a, b)
                self.assertEqual(d, math.gcd(a, b))
                self.assertEqual(a * u + b * v, d)
                self.assertEqual(a % d, 0)
                self.assertEqual(b % d, 0)

    def test_generalized_crt_exhaustive(self):
        for m in range(1, 21):
            for n in range(1, 21):
                for a in range(-10, 11):
                    for b in range(-10, 11):
                        result = crt(a, m, b, n)
                        expected = (b - a) % math.gcd(m, n) == 0
                        self.assertEqual(result is not None, expected)
                        if result is not None:
                            x, period = result
                            self.assertEqual(period, math.lcm(m, n))
                            self.assertTrue(0 <= x < period)
                            self.assertEqual((x - a) % m, 0)
                            self.assertEqual((x - b) % n, 0)

    def test_crt_uniqueness(self):
        for m in range(1, 13):
            for n in range(1, 13):
                for a in range(-3, 4):
                    for b in range(-3, 4):
                        result = crt(a, m, b, n)
                        brute = [x for x in range(math.lcm(m, n)) if (x - a) % m == 0 and (x - b) % n == 0]
                        self.assertEqual(brute, [] if result is None else [result[0]])

    def test_projector_identities(self):
        for m in range(2, 31):
            for n in range(2, 31):
                if math.gcd(m, n) != 1:
                    continue
                e_m, e_n = projectors(m, n)
                M = m * n
                self.assertEqual(e_m % m, 1)
                self.assertEqual(e_m % n, 0)
                self.assertEqual(e_n % m, 0)
                self.assertEqual(e_n % n, 1)
                self.assertEqual((e_m * e_m - e_m) % M, 0)
                self.assertEqual((e_n * e_n - e_n) % M, 0)
                self.assertEqual((e_m * e_n) % M, 0)
                self.assertEqual((e_m + e_n - 1) % M, 0)

    def test_reconstruction(self):
        for m in range(2, 14):
            for n in range(2, 14):
                if math.gcd(m, n) != 1:
                    continue
                e_m, e_n = projectors(m, n)
                for a in range(m):
                    for b in range(n):
                        x = (a * e_m + b * e_n) % (m * n)
                        self.assertEqual(x % m, a)
                        self.assertEqual(x % n, b)

    def test_nilpotents_and_squarefree(self):
        for m in range(2, 100):
            squarefree = all(m % (p * p) for p in range(2, math.isqrt(m) + 1))
            has_nonzero_nilpotent = any(
                any(pow(a, k, m) == 0 for k in range(1, 8))
                for a in range(1, m)
            )
            self.assertEqual(has_nonzero_nilpotent, not squarefree)

    def test_four_idempotents_for_distinct_primes(self):
        primes = [2, 3, 5, 7, 11, 13]
        for p in primes:
            for q in primes:
                if p == q:
                    continue
                M = p * q
                ids = [a for a in range(M) if (a * a - a) % M == 0]
                self.assertEqual(len(ids), 4)

    def test_worked_examples(self):
        self.assertEqual(projectors(4, 9), (9, 28))
        self.assertEqual(crt(3, 4, 5, 9), (23, 36))
        self.assertEqual(crt(5, 6, 1, 8), (17, 24))
        self.assertIsNone(crt(2, 6, 3, 8))
        self.assertEqual(sorted(x for x in range(15) if x * x % 15 == 1), [1, 4, 11, 14])
        self.assertEqual(sorted(x for x in range(15) if x * x % 15 == x), [0, 1, 6, 10])
        self.assertEqual(crt(-1, 7, 2, 9), (20, 63))

    def test_invalid_moduli(self):
        for m, n in [(0, 5), (-2, 5), (3, 0), (2, -3)]:
            with self.assertRaises(ValueError):
                crt(1, m, 2, n)
        for m, n in [(1, 7), (4, 6), (0, 3)]:
            with self.assertRaises(ValueError):
                projectors(m, n)


if __name__ == "__main__":
    unittest.main()
