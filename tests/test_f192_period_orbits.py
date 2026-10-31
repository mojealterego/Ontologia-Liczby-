"""F19.2: exact finite verification of residue orbits, repetends and examples.
These tests do not constitute a formal proof of the manuscript's theorems.
"""
from __future__ import annotations

from fractions import Fraction
from math import gcd, lcm
from pathlib import Path
import re
import unittest

SOURCE = Path(__file__).with_name("F19.2_UZUPELNIENIE_ORBITY_I_OKRESY.md")


def order(b: int, q: int) -> int:
    if q < 2 or gcd(b, q) != 1:
        raise ValueError("q >= 2 and coprimality required")
    r = b % q
    p = 1
    while r != 1:
        r = r * b % q
        p += 1
    return p


def orbit_digits(b: int, a: int, q: int):
    if not (b >= 2 and 0 < a < q and gcd(a, q) == gcd(b, q) == 1):
        raise ValueError("invalid reduced proper fraction")
    p = order(b, q)
    r = a
    states = []
    digits = []
    for _ in range(p):
        states.append(r)
        digit, r = divmod(b * r, q)
        digits.append(digit)
    assert r == a
    return states, digits


def block_value(b: int, digits: list[int]) -> int:
    v = 0
    for d in digits:
        v = b * v + d
    return v


def prime_divisors(n: int) -> list[int]:
    ps = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            ps.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        ps.append(n)
    return ps


class F192Tests(unittest.TestCase):
    def test_source_numbering(self):
        src = SOURCE.read_text(encoding="utf-8")
        for tag, count in (("D", 6), ("T", 10), ("K", 6), ("Z", 12)):
            found = [int(n) for n in re.findall(rf"\*\*{tag}(\d+)\b", src)]
            self.assertEqual(found, list(range(1, count + 1)))

    def test_orbit_is_unique_and_cyclic(self):
        for b in range(2, 15):
            for q in range(2, 65):
                if gcd(b, q) != 1:
                    continue
                p = order(b, q)
                for a in range(1, q):
                    if gcd(a, q) != 1:
                        continue
                    states, digits = orbit_digits(b, a, q)
                    self.assertEqual(len(set(states)), p)
                    self.assertEqual(len(digits), p)
                    self.assertEqual(states[0], a)

    def test_repetend_formula_exact(self):
        for b in range(2, 12):
            for q in range(2, 55):
                if gcd(b, q) != 1:
                    continue
                for a in range(1, q):
                    if gcd(a, q) != 1:
                        continue
                    _, digits = orbit_digits(b, a, q)
                    self.assertEqual(Fraction(block_value(b, digits), b ** len(digits) - 1), Fraction(a, q))

    def test_lagrange_divisibility(self):
        for b in range(2, 14):
            for q in range(2, 100):
                if gcd(b, q) == 1:
                    phi = sum(gcd(i, q) == 1 for i in range(1, q))
                    self.assertEqual(phi % order(b, q), 0)

    def test_certificate_prime_divisor_reduction(self):
        for b in range(2, 13):
            for q in range(2, 95):
                if gcd(b, q) == 1:
                    p = order(b, q)
                    self.assertEqual(pow(b, p, q), 1)
                    self.assertTrue(all(pow(b, p // ell, q) != 1 for ell in prime_divisors(p)))

    def test_rotation(self):
        for b in range(2, 11):
            for q in range(2, 40):
                if gcd(b, q) != 1:
                    continue
                a = 1
                _, digits = orbit_digits(b, a, q)
                p = len(digits)
                for h in range(p):
                    ah = a * pow(b, h, q) % q
                    _, rotated = orbit_digits(b, ah, q)
                    self.assertEqual(rotated, digits[h:] + digits[:h])

    def test_complement_when_minus_one(self):
        for b in range(2, 13):
            for q in range(3, 90):
                if gcd(b, q) != 1:
                    continue
                p = order(b, q)
                if p % 2 != 0 or pow(b, p // 2, q) != q - 1:
                    continue
                _, digits = orbit_digits(b, 1, q)
                h = p // 2
                self.assertEqual(digits[h:], [b - 1 - d for d in digits[:h]])
                self.assertEqual(block_value(b, digits[:h]) + block_value(b, digits[h:]), b ** h - 1)

    def test_digit_frequency(self):
        for b in range(2, 13):
            for q in range(2, 65):
                if gcd(b, q) != 1:
                    continue
                states, digits = orbit_digits(b, 1, q)
                for d in range(b):
                    self.assertEqual(digits.count(d), sum(d * q <= b * r < (d + 1) * q for r in states))

    def test_word_reconstruction(self):
        for b in range(2, 9):
            for p in range(1, 5):
                for B in range(1, min(b ** p - 1, 200)):
                    x = Fraction(B, b ** p - 1)
                    self.assertEqual(x.denominator, (b ** p - 1) // gcd(B, b ** p - 1))
                    self.assertEqual(p % order(b, x.denominator), 0) if x.denominator > 1 else self.assertEqual(x, 1)

    def test_orbit_partition(self):
        for b in range(2, 13):
            for q in range(2, 85):
                if gcd(b, q) != 1:
                    continue
                units = {a for a in range(1, q) if gcd(a, q) == 1}
                unseen = set(units)
                count = 0
                while unseen:
                    a = min(unseen)
                    states, _ = orbit_digits(b, a, q)
                    self.assertTrue(set(states) <= unseen)
                    unseen -= set(states)
                    count += 1
                self.assertEqual(count, len(units) // order(b, q))

    def test_one_seventh_rotations(self):
        self.assertEqual(orbit_digits(10, 1, 7)[1], [1, 4, 2, 8, 5, 7])
        self.assertEqual(orbit_digits(10, 2, 7)[1], [2, 8, 5, 7, 1, 4])
        self.assertEqual(orbit_digits(10, 3, 7)[1], [4, 2, 8, 5, 7, 1])

    def test_one_thirteenth_midys(self):
        self.assertEqual(orbit_digits(10, 1, 13)[1], [0, 7, 6, 9, 2, 3])
        self.assertEqual(pow(10, 3, 13), 12)
        self.assertEqual(76 + 923, 999)

    def test_one_eleventh_and_one_thirty_seventh(self):
        self.assertEqual(orbit_digits(10, 1, 11)[1], [0, 9])
        self.assertEqual(orbit_digits(10, 1, 37)[1], [0, 2, 7])

    def test_counterexamples(self):
        self.assertEqual(order(10, 13), 6)
        self.assertEqual(order(10, 21), 6)
        self.assertNotEqual(pow(10, 3, 21), 20)
        self.assertNotEqual(Fraction(9, 100), Fraction(1, 11))
        self.assertEqual(Fraction(33, 99), Fraction(1, 3))

    def test_invalid_inputs(self):
        for params in [(10, 1, 6), (10, 0, 7), (10, 7, 7), (1, 1, 7)]:
            with self.assertRaises(ValueError):
                orbit_digits(*params)


if __name__ == "__main__":
    unittest.main()
