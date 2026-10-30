"""Kontrole F12.2/F12.3: reprezentacja i rozwiązania równań (nie zastępują dowodów)."""
import itertools
import random
import unittest
from tools.arithmetic import (
    base_digits, borrow_subtract, digits_value, solve_congruence,
    complement_subtract, solve_diophantine,
    solve_integer_linear, signed_from_twos, signed_overflow_subtract,
)


class SubtractionTests(unittest.TestCase):
    def test_all_single_digit_bases(self):
        for base in range(2, 21):
            for a in range(base):
                for b in range(base):
                    digits, borrow, trace = borrow_subtract([a], [b], base)
                    self.assertEqual(digits_value(digits, base) - borrow * base, a-b)
                    self.assertEqual(trace[-1]['borrow_out'], borrow)

    def test_exhaustive_3_digit_binary(self):
        for a, b in itertools.product(range(8), repeat=2):
            digits, borrow, _ = borrow_subtract(base_digits(a, 2, 3), base_digits(b, 2, 3), 2)
            self.assertEqual(digits_value(digits, 2) - borrow*8, a-b)

    def test_exhaustive_two_digit_decimal(self):
        for a, b in itertools.product(range(100), repeat=2):
            digits, borrow, _ = borrow_subtract(base_digits(a, 10, 2), base_digits(b, 10, 2), 10)
            self.assertEqual(digits_value(digits, 10) - borrow*100, a-b)

    def test_decimal_zero_chain(self):
        digits, borrow, _ = borrow_subtract(base_digits(100000, 10, 6), base_digits(1, 10, 6), 10)
        self.assertEqual((digits_value(digits, 10), borrow), (99999, 0))

    def test_existing_examples(self):
        for base, a, b in [(10, 402, 178), (10, 1002, 478), (8, 512, 111), (10, 2000, 1357)]:
            width = max(1, len(base_digits(a,base)),len(base_digits(b,base)))
            digits, borrow, _ = borrow_subtract(base_digits(a,base,width), base_digits(b,base,width),base)
            self.assertEqual(digits_value(digits,base)-borrow*(base**width),a-b)

    def test_random_invariants_all_prefixes(self):
        rng=random.Random(20261030)
        for _ in range(2500):
            base=rng.randint(2,36);width=rng.randint(1,8);a=rng.randrange(base**width);b=rng.randrange(base**width)
            aa,bb=base_digits(a,base,width),base_digits(b,base,width)
            digits, borrow, trace=borrow_subtract(aa,bb,base)
            for i, step in enumerate(trace,1):
                prefix_a=digits_value(aa[:i],base);prefix_b=digits_value(bb[:i],base)
                prefix_c=digits_value(digits[:i],base)
                self.assertEqual(prefix_a-prefix_b,prefix_c-step['borrow_out']*base**i)
            self.assertEqual(digits_value(digits,base)-borrow*(base**width),a-b)

    def test_complement_matches_borrow(self):
        for base in range(2,18):
            for width in (1,2,3):
                limit=base**width
                vals=range(limit) if limit<100 else (0,1,limit//2,limit-1)
                for a in vals:
                    for b in vals:
                        result, carry=complement_subtract(a,b,base,width)
                        digits,borrow,_=borrow_subtract(base_digits(a,base,width),base_digits(b,base,width),base)
                        self.assertEqual(result,digits_value(digits,base))
                        self.assertEqual(carry,1-borrow)

    def test_invalid_digit_rejected(self):
        with self.assertRaises(ValueError):borrow_subtract([2],[0],2)
        with self.assertRaises(ValueError):borrow_subtract([0],[0],1)
        with self.assertRaises(ValueError):borrow_subtract([0],[0,0],10)

    def test_signed_twos(self):
        self.assertEqual([signed_from_twos(i,4) for i in range(16)],list(range(8))+list(range(-8,0)))

    def test_signed_overflow(self):
        self.assertEqual(signed_overflow_subtract(7,-1,4),( -8, True ))
        self.assertEqual(signed_overflow_subtract(-8,1,4),(7,True))
        self.assertEqual(signed_overflow_subtract(3,-2,4),(5,False))
        self.assertEqual(signed_overflow_subtract(-3,-2,4),(-1,False))


class InverseEquationTests(unittest.TestCase):
    def test_congruence_by_bruteforce(self):
        for m in range(1,40):
            for a in range(-12,13):
                for b in range(-12,13):
                    self.assertEqual(solve_congruence(a,b,m),[x for x in range(m) if (a*x-b)%m==0])

    def test_congruence_edge(self):
        self.assertEqual(solve_congruence(0,0,5),[0,1,2,3,4])
        self.assertEqual(solve_congruence(6,5,9),[])
        self.assertEqual(solve_congruence(6,3,9),[2,5,8])

    def test_diophantine_parametrization(self):
        for a in range(-10,11):
            for b in range(-10,11):
                if a==b==0:continue
                for c in (-24,-1,0,1,21,35):
                    sol=solve_diophantine(a,b,c)
                    from math import gcd
                    if c%gcd(a,b):self.assertIsNone(sol)
                    else:
                        x,y,dx,dy=sol
                        for t in range(-5,6):
                            self.assertEqual(a*(x+t*dx)+b*(y+t*dy),c)
        self.assertIsNone(solve_diophantine(14,21,1))
        x,y,dx,dy=solve_diophantine(14,21,35)
        self.assertEqual((dx,dy),(3,-2))

    def test_linear_integer_equation(self):
        self.assertEqual(solve_integer_linear(3,5,17),4)
        self.assertIsNone(solve_integer_linear(3,5,16))
        self.assertEqual(solve_integer_linear(-2,7,1),3)
        with self.assertRaises(ValueError):solve_integer_linear(0,7,7)


if __name__ == '__main__': unittest.main()