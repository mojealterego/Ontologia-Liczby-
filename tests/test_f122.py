"""Property checks for Tom I F12.2; exact digit arithmetic, not a proof assistant."""
import unittest
from itertools import product


def subtract(a: int, b: int, base: int, n: int):
    if not (base >= 2 and n >= 1 and 0 <= a < base**n and 0 <= b < base**n):
        raise ValueError('Inputs must fit the declared base and width')
    borrow = 0
    result = 0
    certificate = []
    for i in range(n):
        ai = (a // base**i) % base
        di = (b // base**i) % base
        t = ai - di - borrow
        next_borrow = int(t < 0)
        ri = t + base * next_borrow
        certificate.append((ai, di, borrow, ri, next_borrow))
        result += ri * base**i
        borrow = next_borrow
    return result, borrow, certificate


def verify(a: int, b: int, base: int, n: int, result: int, final_borrow: int, cert):
    if len(cert) != n or final_borrow not in (0, 1):
        return False
    if not (0 <= a < base**n and 0 <= b < base**n and 0 <= result < base**n):
        return False
    prev = 0
    for i, (ai, di, cin, ri, cout) in enumerate(cert):
        if (ai != (a // base**i) % base or di != (b // base**i) % base
                or cin != prev or not 0 <= ri < base or cout not in (0, 1)
                or ai - di - cin != ri - base * cout
                or ri != (result // base**i) % base):
            return False
        prev = cout
    return prev == final_borrow


class F122Tests(unittest.TestCase):
    def test_exhaustive_bases(self):
        for base, n in ((2, 6), (3, 4), (10, 2)):
            limit = base**n
            for a in range(limit):
                for b in range(limit):
                    r, c, cert = subtract(a, b, base, n)
                    self.assertEqual(a-b, r-c*limit)
                    self.assertEqual(c, int(a < b))
                    self.assertTrue(verify(a, b, base, n, r, c, cert))

    def test_prefix_invariant(self):
        for base, n in ((2, 5), (3, 3), (10, 2)):
            for a, b in product(range(base**n), repeat=2):
                r, c, cert = subtract(a, b, base, n)
                for k in range(n+1):
                    radix = base**k
                    prefix_r = r % radix
                    prefix_a = a % radix
                    prefix_b = b % radix
                    incoming = 0 if k == 0 else cert[k-1][4]
                    self.assertEqual(prefix_a-prefix_b, prefix_r-incoming*radix)

    def test_modular_prefix(self):
        for base in (2, 3, 8, 10):
            n = 4
            for a, b in ((0,1), (1,0), (base**n-1, 1), (123%base**n, 57%base**n)):
                r, _, _ = subtract(a, b, base, n)
                for k in range(1,n+1):
                    self.assertEqual(r % base**k, (a-b) % base**k)

    def test_complement(self):
        for base, n in ((2,5), (3,4), (10,2)):
            radix=base**n
            for a, b in product(range(radix), repeat=2):
                r,c,_=subtract(a,b,base,n)
                complement=radix-1-b
                s=a+complement+1
                self.assertEqual((s%radix, s//radix), (r, 1-c))

    def test_propagation_equal_digits(self):
        for base in (2,3,8,10):
            a = base**4
            b = 1
            r,c,cert=subtract(a,b,base,5)
            self.assertEqual((r,c), (a-1,0))
            self.assertTrue(all(cert[j][3]==base-1 and cert[j][4]==1 for j in range(4)))

    def test_examples_decimal(self):
        for a,b,expected in ((1000,1,999),(502,178,324),(10000,9999,1),
                             (700,256,444),(2002,1999,3),(300,175,125),
                             (402,178,224),(1002,478,524),(4000,2001,1999)):
            n=len(str(max(a,b)))
            self.assertEqual(subtract(a,b,10,n)[:2], (expected,0))

    def test_examples_binary_ternary_octal(self):
        self.assertEqual(subtract(10,3,2,4)[:2],(7,0))
        self.assertEqual(subtract(9,1,3,3)[:2],(8,0))
        self.assertEqual(subtract(0o1000,0o157,8,4)[:2],(0o621,0))

    def test_negative_borrow(self):
        self.assertEqual(subtract(15,16,2,5)[:2],(31,1))
        self.assertEqual(subtract(125,307,10,3)[:2],(818,1))
        self.assertEqual(subtract(0,1,10,3)[:2],(999,1))

    def test_certificate_rejects_modified_digit(self):
        r,c,cert=subtract(502,178,10,3)
        bad=[list(row) for row in cert]
        bad[1][3]=3
        self.assertFalse(verify(502,178,10,3,334,c,bad))
        self.assertTrue(verify(502,178,10,3,r,c,cert))

    def test_certificate_rejects_modified_borrow(self):
        r,c,cert=subtract(1002,478,10,4)
        bad=[list(row) for row in cert]
        bad[1][4]=0
        self.assertFalse(verify(1002,478,10,4,r,c,bad))

    def test_out_of_range_rejected(self):
        for values in ((1000,1,10,3),(-1,1,10,3),(1,1,1,3),(1,1,10,0)):
            with self.assertRaises(ValueError):
                subtract(*values)

    def test_inverse_and_counterexample(self):
        self.assertEqual(324+178,502)
        self.assertNotEqual(334+178,502)
        self.assertEqual(334%10,324%10)
        self.assertEqual(0o621,401)


if __name__ == '__main__':
    unittest.main()
