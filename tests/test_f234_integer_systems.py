"""Dokładne kontrole F23.4. Nie zastępują formalnych dowodów twierdzeń."""
from __future__ import annotations

import itertools
import math
import unittest
from fractions import Fraction


def det(a):
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def matvec(a, x):
    return tuple(sum(a[i][j] * x[j] for j in range(2)) for i in range(2))


def smith_invariants(a):
    g = math.gcd(*(abs(z) for row in a for z in row))
    d = abs(det(a))
    if g == 0:
        return 0, 0
    return (g, d // g) if d else (g, 0)


def bezout(a, b):
    """Zwraca (s,t,g), sa+tb=g=gcd(a,b)>=0."""
    def eg(x, y):
        if y == 0:
            return (abs(x), 1 if x >= 0 else -1, 0)
        g, s, t = eg(y, x % y)
        return g, t, s - (x // y) * t
    g, s, t = eg(a, b)
    return s, t, g


def integer_solution(a, b):
    """Jedno rozwiązanie w Z² lub None, z pełną obsługą rzędu 0, 1 i 2."""
    delta = det(a)
    if delta:
        p = a[1][1] * b[0] - a[0][1] * b[1]
        q = -a[1][0] * b[0] + a[0][0] * b[1]
        if p % delta or q % delta:
            return None
        return p // delta, q // delta
    if all(z == 0 for row in a for z in row):
        return (0, 0) if b == (0, 0) else None
    row = next(row for row in a if row != (0, 0))
    g = math.gcd(*row)
    u, v = row[0] // g, row[1] // g
    factors = []
    for r in a:
        h = r[0] // u if u else r[1] // v
        if r != (h * u, h * v):
            raise ValueError("macierz nie ma rzędu jeden")
        factors.append(h)
    t = None
    for h, bi in zip(factors, b):
        if h == 0:
            if bi != 0:
                return None
        else:
            if bi % h:
                return None
            candidate = bi // h
            if t is not None and candidate != t:
                return None
            t = candidate
    assert t is not None
    s, q, gcd_uv = bezout(u, v)
    assert gcd_uv == 1
    return s * t, q * t


def rational_solution(a, b):
    d = det(a)
    if d == 0:
        raise ValueError("singular")
    return (Fraction(a[1][1] * b[0] - a[0][1] * b[1], d),
            Fraction(-a[1][0] * b[0] + a[0][0] * b[1], d))


class IntegerSystemTests(unittest.TestCase):
    def test_determinant(self):
        self.assertEqual(det(((2, 1), (0, 3))), 6)

    def test_unimodular(self):
        self.assertEqual(abs(det(((1, 1), (0, 1)))), 1)

    def test_smith_diag(self):
        self.assertEqual(smith_invariants(((2, 0), (0, 6))), (2, 6))

    def test_smith_rank_one(self):
        self.assertEqual(smith_invariants(((2, 2), (4, 4))), (2, 0))

    def test_smith_zero(self):
        self.assertEqual(smith_invariants(((0, 0), (0, 0))), (0, 0))

    def test_smith_gcd_one_not_unimodular(self):
        self.assertEqual(smith_invariants(((1, 0), (0, 2))), (1, 2))

    def test_smith_divisibility(self):
        for entries in itertools.product(range(-2, 3), repeat=4):
            a = (entries[:2], entries[2:])
            d1, d2 = smith_invariants(a)
            if d1 and d2:
                self.assertEqual(d2 % d1, 0)
                self.assertEqual(d1 * d2, abs(det(a)))

    def test_smith_independent_sympy(self):
        from sympy import Matrix, ZZ
        from sympy.matrices.normalforms import smith_normal_form
        for entries in itertools.product(range(-2, 3), repeat=4):
            a = (entries[:2], entries[2:])
            s = smith_normal_form(Matrix(a), domain=ZZ)
            self.assertEqual(tuple(abs(int(s[i, i])) for i in range(2)), smith_invariants(a))

    def test_bezout_signed(self):
        for a, b in itertools.product(range(-9, 10), repeat=2):
            s, t, g = bezout(a, b)
            self.assertEqual(s * a + t * b, g)
            self.assertEqual(g, math.gcd(a, b))

    def test_full_rank_round_trip(self):
        for entries in itertools.product(range(-2, 3), repeat=4):
            a = (entries[:2], entries[2:])
            if not det(a):
                continue
            for x in ((0, 0), (1, -1), (-2, 2), (3, 1)):
                b = matvec(a, x)
                self.assertEqual(integer_solution(a, b), x)

    def test_rank_one_round_trip(self):
        for row in ((2, 3), (-2, 4), (0, -3), (3, 0)):
            for h in (-2, -1, 0, 2):
                a = (row, (h * row[0], h * row[1]))
                for x in ((1, 2), (-3, 4), (0, 0)):
                    b = matvec(a, x)
                    witness = integer_solution(a, b)
                    self.assertIsNotNone(witness)
                    self.assertEqual(matvec(a, witness), b)

    def test_zero_matrix_consistent(self):
        self.assertEqual(integer_solution(((0, 0), (0, 0)), (0, 0)), (0, 0))

    def test_zero_matrix_inconsistent(self):
        self.assertIsNone(integer_solution(((0, 0), (0, 0)), (0, 1)))

    def test_rational_not_integer(self):
        a = ((2, 0), (0, 1))
        self.assertEqual(rational_solution(a, (1, 0)), (Fraction(1, 2), Fraction(0)))
        self.assertIsNone(integer_solution(a, (1, 0)))

    def test_modular_obstruction(self):
        a = ((2, 1), (0, 2))
        self.assertIsNone(integer_solution(a, (0, 1)))
        self.assertTrue(all(matvec(a, x)[1] % 2 == 0 for x in itertools.product(range(2), repeat=2)))

    def test_exercise_1(self):
        self.assertEqual(integer_solution(((2, 0), (0, 3)), (4, 9)), (2, 3))

    def test_exercise_2(self):
        self.assertIsNone(integer_solution(((2, 0), (0, 3)), (1, 9)))

    def test_exercise_3(self):
        self.assertIsNone(integer_solution(((2, 1), (0, 3)), (5, 6)))

    def test_exercise_4(self):
        self.assertEqual(integer_solution(((2, 1), (0, 3)), (6, 6)), (2, 2))

    def test_exercise_5(self):
        a = ((1, 1), (2, 2))
        x = integer_solution(a, (3, 6))
        self.assertEqual(matvec(a, x), (3, 6))

    def test_exercise_6(self):
        self.assertIsNone(integer_solution(((1, 1), (2, 2)), (3, 7)))

    def test_exercise_7(self):
        a = ((2, 2), (4, 4))
        x = integer_solution(a, (6, 12))
        self.assertEqual(matvec(a, x), (6, 12))

    def test_exercise_8(self):
        self.assertIsNone(integer_solution(((2, 2), (4, 4)), (3, 6)))

    def test_exercise_9(self):
        self.assertEqual(smith_invariants(((2, 0), (0, 6))), (2, 6))

    def test_exercise_10(self):
        self.assertEqual(integer_solution(((2, 1), (0, 2)), (1, 2)), (0, 1))

    def test_exercise_11(self):
        self.assertIsNone(integer_solution(((2, 1), (0, 2)), (0, 1)))

    def test_exercise_12(self):
        x = rational_solution(((3, 0), (0, 4)), (1, 2))
        self.assertEqual(x, (Fraction(1, 3), Fraction(1, 2)))
        self.assertEqual(math.lcm(*(z.denominator for z in x)), 6)

    def test_mod_2_rank_drop(self):
        a = ((2, 0), (0, 1))
        self.assertNotEqual(det(a), 0)
        self.assertEqual(a[0][0] % 2, 0)

    def test_random_full_rank_versus_rational(self):
        for entries in itertools.product(range(-2, 3), repeat=4):
            a = (entries[:2], entries[2:])
            if det(a) == 0:
                continue
            for b in ((1, 0), (0, 1), (1, 2)):
                q = rational_solution(a, b)
                z = integer_solution(a, b)
                self.assertEqual(z is not None, all(t.denominator == 1 for t in q))


if __name__ == "__main__":
    unittest.main()
