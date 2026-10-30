"""Reprodukowalne kontrole przykładów F15.1; nie zastępują dowodów ogólnych."""
from itertools import product
from math import gcd, lcm
from pathlib import Path
import re
import unittest

SOURCE = Path(__file__).resolve().parents[1] / 'F15.1_UZUPELNIENIE_IDEALY_I_WARTOSCIOWANIA.md'


def valuation(p, n):
    assert abs(n) > 0 and p > 1
    n = abs(n)
    exponent = 0
    while n % p == 0:
        exponent += 1
        n //= p
    return exponent


def is_prime(n):
    return n > 1 and all(n % d != 0 for d in range(2, int(n**.5) + 1))


def bezout(a, b):
    old_r, r, old_s, s, old_t, t = a, b, 1, 0, 0, 1
    while r:
        q = old_r // r
        old_r, r = r, old_r - q*r
        old_s, s = s, old_s-q*s
        old_t, t = t, old_t-q*t
    sign = 1 if old_r >= 0 else -1
    return old_r*sign, old_s*sign, old_t*sign


class TestF151(unittest.TestCase):
    def test_structure(self):
        s = SOURCE.read_text(encoding='utf-8')
        self.assertEqual(len(re.findall(r'\*\*Twierdzenie T\d+', s)), 12)
        self.assertEqual(len(re.findall(r'\*\*Zadanie \d+', s)), 12)
        self.assertEqual(len(re.findall(r'\*\*Kontrprzykład K\d+', s)), 6)
        self.assertGreater(len(s), 12000)

    def test_divisibility_zero_and_associates(self):
        div = lambda a, b: (b == 0 if a == 0 else b % a == 0)
        for a, b in product(range(-15, 16), repeat=2):
            if div(a, b) and div(b, a):
                self.assertEqual(abs(a), abs(b))
            self.assertTrue(div(a, a))
        self.assertTrue(div(0, 0))
        self.assertFalse(div(0, 7))

    def test_gcd_bezout(self):
        for a, b in product(range(-45, 46), repeat=2):
            g, u, v = bezout(a, b)
            self.assertEqual(g, gcd(a, b))
            self.assertEqual(a*u+b*v, g)

    def test_lcm_product(self):
        for a, b in product(range(-50, 51), repeat=2):
            if a and b:
                self.assertEqual(gcd(a, b)*lcm(a, b), abs(a*b))
                self.assertEqual(lcm(a, b) % abs(a), 0)
                self.assertEqual(lcm(a, b) % abs(b), 0)

    def test_lattice_distributivity(self):
        for a, b, c in product(range(1, 17), repeat=3):
            self.assertEqual(gcd(a, lcm(b,c)), lcm(gcd(a,b), gcd(a,c)))

    def test_prime_and_irreducible(self):
        for n in range(2, 250):
            irreducible = not any(n == a*b for a in range(2, n) for b in range(2, n//a+1))
            self.assertEqual(irreducible, is_prime(n))

    def test_valuation_products(self):
        for p in (2,3,5,7,11):
            for a, b in product(range(1, 40), repeat=2):
                self.assertEqual(valuation(p,a*b), valuation(p,a)+valuation(p,b))

    def test_divisibility_valuation(self):
        primes = [p for p in range(2, 120) if is_prime(p)]
        for a,b in product(range(1,70),repeat=2):
            self.assertEqual(b % a == 0, all(valuation(p,a)<=valuation(p,b) for p in primes))

    def test_gcd_add_multiple(self):
        for a,b,k in product(range(-12,13),range(-12,13),range(-6,7)):
            self.assertEqual(gcd(a,b),gcd(a,b+k*a))

    def test_crt_coprime(self):
        for m,n in product(range(1,15), repeat=2):
            if gcd(m,n) == 1:
                for r,s in product(range(-2,3),repeat=2):
                    matches=[x for x in range(m*n) if x % m == r % m and x % n == s % n]
                    self.assertEqual(len(matches),1)

    def test_block_digits(self):
        for base, block, mod in ((10,3,37),(10,1,9),(10,1,11),(2,3,7)):
            scale=base**block
            for number in range(0,2000,37):
                parts=[];x=number
                if x==0:parts=[0]
                while x:
                    parts.append(x%scale);x//=scale
                if scale % mod==1:
                    self.assertEqual(number%mod,sum(parts)%mod)
                if scale % mod==mod-1:
                    self.assertEqual(number%mod,sum(((-1)**j)*p for j,p in enumerate(parts))%mod)

    def test_solved_exercises(self):
        self.assertEqual(gcd(18,30),6)
        self.assertEqual(lcm(18,30),90)
        self.assertEqual(gcd(14,21),7)
        self.assertEqual(lcm(14,21),42)
        self.assertEqual(gcd(72,120),24)
        self.assertEqual(lcm(72,120),360)
        self.assertEqual(gcd(12,lcm(18,40)),12)
        self.assertEqual(lcm(gcd(12,18),gcd(12,40)),12)
        self.assertEqual((valuation(2,360),valuation(3,360),valuation(5,360)),(3,2,1))
        self.assertEqual(valuation(2,360*72),6)
        self.assertEqual(198*2+126*(-3),18)
        self.assertEqual([x for x in range(15) if x%3==2 and x%5==3],[8])
        self.assertEqual(123456%37,24)


if __name__ == '__main__':
    unittest.main()