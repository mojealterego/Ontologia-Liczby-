"""E1-02: executable properties for divisibility, primality, gcd/lcm and Euclid."""
import math
import unittest

def prime(n: int) -> bool:
    if n < 2:
        return False
    return all(n % d for d in range(2, math.isqrt(n) + 1))

def factorization(n: int) -> dict[int, int]:
    if n < 1:
        raise ValueError("Only positive integers are supported")
    out: dict[int, int] = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out

def euclid_trace(a: int, b: int) -> tuple[int, list[tuple[int, int, int, int]]]:
    if a < 0 or b < 0:
        raise ValueError("Expected nonnegative integers")
    trace = []
    while b:
        q, r = divmod(a, b)
        trace.append((a, b, q, r))
        a, b = b, r
    return a, trace

class DivisibilityE102(unittest.TestCase):
    def test_euclid_and_trace(self):
        for a in range(0, 150):
            for b in range(1, 70):
                g, trace = euclid_trace(a, b)
                self.assertEqual(g, math.gcd(a, b))
                for x, y, q, r in trace:
                    self.assertEqual(x, q * y + r)
                    self.assertTrue(0 <= r < y)
                    self.assertEqual(math.gcd(x, y), math.gcd(y, r))

    def test_factorization_roundtrip(self):
        for n in range(1, 1500):
            factors = factorization(n)
            self.assertEqual(math.prod(p**e for p, e in factors.items()), n)
            self.assertTrue(all(prime(p) and e > 0 for p, e in factors.items()))

    def test_prime_trial_division(self):
        for n in range(2, 500):
            trial = not any(n % d == 0 for d in range(2, math.isqrt(n) + 1))
            self.assertEqual(prime(n), trial)

    def test_gcd_lcm_product(self):
        for a in range(1, 101):
            for b in range(1, 101):
                g = math.gcd(a, b)
                l = math.lcm(a, b)
                self.assertEqual(g * l, a * b)
                self.assertEqual(a % g, 0)
                self.assertEqual(b % g, 0)
                self.assertEqual(l % a, 0)
                self.assertEqual(l % b, 0)

    def test_min_max_prime_exponents(self):
        for a in range(1, 120):
            for b in range(1, 120):
                fa, fb = factorization(a), factorization(b)
                primes = set(fa) | set(fb)
                g = math.prod(p**min(fa.get(p, 0), fb.get(p, 0)) for p in primes)
                l = math.prod(p**max(fa.get(p, 0), fb.get(p, 0)) for p in primes)
                self.assertEqual((g, l), (math.gcd(a, b), math.lcm(a, b)))

    def test_divisibility_rules(self):
        for n in range(0, 10000):
            digits = [int(d) for d in str(n)]
            self.assertEqual(n % 3 == 0, sum(digits) % 3 == 0)
            self.assertEqual(n % 9 == 0, sum(digits) % 9 == 0)
            alternating = sum((-1)**i * int(d) for i, d in enumerate(reversed(str(n))))
            self.assertEqual(n % 11 == 0, alternating % 11 == 0)
            self.assertEqual(n % 2 == 0, n % 10 in (0, 2, 4, 6, 8))
            self.assertEqual(n % 5 == 0, n % 10 in (0, 5))

    def test_relative_primes(self):
        for n in range(1, 1000):
            self.assertEqual(math.gcd(n, n+1), 1)

    def test_examples(self):
        self.assertEqual(math.gcd(252, 198), 18)
        self.assertEqual(math.gcd(1071, 462), 21)
        self.assertEqual(math.gcd(414, 662), 2)
        self.assertEqual(8*414 - 5*662, 2)
        self.assertEqual(math.lcm(18, 24, 30), 360)
        self.assertEqual(math.lcm(12, 20), 60)
        self.assertEqual(math.lcm(6, 8, 15), 120)
        self.assertEqual(factorization(360), {2: 3, 3: 2, 5: 1})
        self.assertTrue(prime(97))
        self.assertTrue(prime(149))
        self.assertFalse(prime(221))
        self.assertEqual(60 % 7, 4)
        self.assertEqual(149 % 11, 6)

if __name__ == "__main__":
    unittest.main()
