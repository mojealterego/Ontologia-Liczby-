"""Dokładne testy obliczeń i kontrprzykładów F20.2 (bez float)."""
from fractions import Fraction as F
from itertools import permutations, product
from pathlib import Path
import re
import unittest


def multiplier(p: F) -> F:
    return F(1) + F(p, 100)


def compose(p: F, q: F) -> F:
    if p <= -100 or q <= -100:
        raise ValueError("W grupie dopuszczalne są wyłącznie p,q > -100")
    return F(100) * (multiplier(p) * multiplier(q) - 1)


def inverse(p: F) -> F:
    if p <= -100:
        raise ValueError("Brak dodatniego mnożnika")
    return -F(100) * p / (F(100) + p)


def rate(x: F, y: F) -> F:
    if x <= 0 or y < 0:
        raise ValueError("x>0, y>=0")
    return F(100) * (y - x) / x


def aggregate(xs: tuple[F, ...], ys: tuple[F, ...]) -> F:
    if len(xs) != len(ys) or not xs or any(x <= 0 for x in xs) or any(y < 0 for y in ys):
        raise ValueError("Błędne wektory baz i wartości końcowych")
    return rate(sum(xs), sum(ys))


class PercentChanges(unittest.TestCase):
    def test_T1_exact_composition(self):
        for p, q in product(range(-95, 150, 5), repeat=2):
            self.assertEqual(compose(F(p), F(q)), F(p + q) + F(p*q, 100))

    def test_T2_group_associativity_and_identity(self):
        ps = [F(-90), F(-25), F(0), F(15), F(150)]
        for p, q, r in product(ps, repeat=3):
            self.assertEqual(compose(compose(p, q), r), compose(p, compose(q, r)))
            self.assertEqual(compose(p, q), compose(q, p))
            self.assertEqual(compose(p, 0), p)

    def test_T3_inverse(self):
        for p in [F(-99), F(-75), F(-1), F(0), F(20), F(25), F(300)]:
            self.assertEqual(compose(p, inverse(p)), 0)
            self.assertEqual(multiplier(inverse(p)), 1 / multiplier(p))
        with self.assertRaises(ValueError):
            inverse(F(-100))

    def test_T4_additivity_iff_zero_product(self):
        for p, q in product(range(-90, 110, 10), repeat=2):
            self.assertEqual(compose(F(p), F(q)) == p + q, p*q == 0)

    def test_T5_symmetric_change(self):
        for p in range(1, 100):
            self.assertEqual(compose(F(p), F(-p)), -F(p*p, 100))

    def test_T6_weighted_aggregate(self):
        xs = (F(100), F(900))
        ys = (F(150), F(810))
        self.assertEqual(aggregate(xs, ys), -4)
        self.assertEqual(aggregate(xs, ys), sum((x / sum(xs)) * rate(x, y) for x, y in zip(xs, ys)))
        for x1, x2, p1, p2 in product([1, 2, 7], [1, 5], [-90, 0, 20], [-40, 0, 80]):
            xs = (F(x1), F(x2))
            ys = (xs[0]*multiplier(F(p1)), xs[1]*multiplier(F(p2)))
            r = aggregate(xs, ys)
            self.assertTrue(min(p1, p2) <= r <= max(p1, p2))

    def test_T7_rebasing_indices(self):
        for s, t, u in product([F(1), F(2), F(7), F(11)], repeat=3):
            self.assertEqual(F(100)*u/s, (F(100)*t/s)*(F(100)*u/t)/100)

    def test_T8_percentage_points(self):
        a, b = F(12, 100), F(15, 100)
        d = 100*(b-a)
        self.assertEqual(d, 3)
        self.assertEqual(d/a, 25)

    def test_T9_permutation(self):
        ps = (F(10), F(-25), F(20))
        def total(seq):
            out = F(1)
            for p in seq:
                out *= multiplier(p)
            return out
        self.assertEqual({total(perm) for perm in permutations(ps)}, {F(99, 100)})

    def test_T10_stability_bound(self):
        for x, xp, y, yp in product(range(1, 7), range(1, 7), range(0, 7), range(0, 7)):
            m = min(x, xp)
            actual = abs(rate(F(x), F(y)) - rate(F(xp), F(yp)))
            bound = F(100) * (F(abs(y-yp), m) + F(yp*abs(x-xp), m*m))
            self.assertLessEqual(actual, bound)

    def test_T11_bernoulli(self):
        for n, r in product(range(0, 15), range(0, 51, 5)):
            self.assertGreaterEqual(multiplier(F(r))**n, 1 + F(n*r, 100))
            if n >= 2 and r > 0:
                self.assertGreater(multiplier(F(r))**n, 1 + F(n*r, 100))

    def test_K1_K2_K3(self):
        self.assertEqual(compose(F(10), F(10)), 21)
        self.assertEqual(compose(F(25), F(-25)), F(-25, 4))
        self.assertEqual(inverse(F(25)), -20)
        self.assertEqual(rate(F(12), F(15)), 25)

    def test_K4_K5_K6(self):
        self.assertNotEqual((F(50)+F(-10))/2, aggregate((F(100), F(900)), (F(150), F(810))))
        with self.assertRaises(ValueError):
            rate(F(0), F(5))
        a = lambda x: x+10
        b = lambda x: 2*x
        self.assertNotEqual(a(b(1)), b(a(1)))

    def test_Z1_Z2_Z3_Z4(self):
        self.assertEqual(F(800)*multiplier(F(15))*multiplier(F(-10)), 828)
        self.assertEqual(F(270)/multiplier(F(35)), 200)
        self.assertEqual(inverse(F(25)), -20)
        self.assertEqual(inverse(F(20)), -F(50, 3))

    def test_Z5_Z6_Z7_Z8(self):
        self.assertEqual(compose(F(30), F(-30)), -9)
        self.assertEqual(aggregate((F(100), F(900)), (F(150), F(810))), -4)
        self.assertEqual(rate(F(12), F(15)), 25)
        self.assertEqual(multiplier(F(10))*multiplier(F(20))*multiplier(F(-25)), F(99, 100))

    def test_Z9_Z10_Z11_Z12(self):
        self.assertEqual(rate(F(100), F(121)), 21)
        self.assertEqual(rate(F(110), F(121)), 10)
        self.assertEqual(rate(F(100), F(110))-rate(F(101), F(111)), F(10, 101))
        self.assertEqual(F(1000)*multiplier(F(5))**3, F(9261, 8))
        self.assertEqual(compose(F(-20), F(-20)), -36)
        self.assertEqual(inverse(F(-36)), F(225, 4))

    def test_numbering_and_structure(self):
        source = Path(__file__).resolve().parents[1] / "manuscript/tom-01/F20/F20.2_UZUPELNIENIE_ZMIANY_PROCENTOWE.md"
        content = source.read_text(encoding="utf-8")
        for prefix, count in (("D", 8), ("T", 11), ("K", 6), ("Z", 12)):
            got = [int(x) for x in re.findall(r"^\*\*" + prefix + r"(\d+)\b", content, re.M)]
            self.assertEqual(got, list(range(1, count + 1)), (prefix, got))
        self.assertIn("*Dowód.*", content)
        self.assertNotIn("TODO", content)


if __name__ == "__main__":
    unittest.main()
