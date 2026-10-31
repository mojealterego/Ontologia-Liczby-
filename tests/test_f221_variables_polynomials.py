"""F22.1: exact finite checks; not a formal proof of theorems."""
from fractions import Fraction
from itertools import product
import unittest


def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def add(p, q):
    return trim([(p[i] if i < len(p) else 0) + (q[i] if i < len(q) else 0)
                 for i in range(max(len(p), len(q)))])


def mul(p, q):
    out = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] += a * b
    return trim(out)


def ev(p, x):
    acc = 0
    for a in reversed(p):
        acc = acc * x + a
    return acc


def compose(p, q):
    acc = [0]
    for a in reversed(p):
        acc = add(mul(acc, q), [a])
    return acc


def derivative(p):
    return trim([i * p[i] for i in range(1, len(p))] or [0])


def div_monic(p, q):
    assert q[-1] == 1
    p = trim(p)
    quot = [0] * max(1, len(p) - len(q) + 1)
    while p != [0] and len(p) >= len(q):
        k = len(p) - len(q)
        c = p[-1]
        quot[k] = c
        for i, v in enumerate(q):
            p[i + k] -= c * v
        p = trim(p)
    return trim(quot), p


def lagrange(points):
    out = [Fraction(0)]
    for i, (x, y) in enumerate(points):
        basis = [Fraction(1)]
        den = Fraction(1)
        for j, (z, _) in enumerate(points):
            if i != j:
                basis = mul(basis, [-z, Fraction(1)])
                den *= x - z
        out = add(out, [a * y / den for a in basis])
    return out


class F221Tests(unittest.TestCase):
    def test_ev_hom_add(self):
        for p in ([0], [1, 2], [3, -4, 2]):
            for q in ([2], [0, 1], [-2, 0, 1]):
                for x in range(-3, 4):
                    self.assertEqual(ev(add(p, q), x), ev(p, x) + ev(q, x))

    def test_ev_hom_mul(self):
        for p in ([1, 2], [3, -1, 2]):
            for q in ([2, 1], [1, 0, 1]):
                for x in range(-4, 5):
                    self.assertEqual(ev(mul(p, q), x), ev(p, x) * ev(q, x))

    def test_factor_kernel(self):
        for a in range(-4, 5):
            for q in ([0], [1], [1, -2], [2, 3, 1]):
                f = mul([-a, 1], q)
                self.assertEqual(ev(f, a), 0)
                quot, rem = div_monic(f, [-a, 1])
                self.assertEqual(rem, [0])
                self.assertEqual(quot, trim(q))

    def test_division_remainder_evaluation(self):
        for a in range(-3, 4):
            for f in ([1], [1, 2], [-2, 3, 4], [3, -2, 0, 1]):
                q, r = div_monic(f, [-a, 1])
                self.assertEqual(r, [ev(f, a)])
                self.assertEqual(add(mul(q, [-a, 1]), r), trim(f))

    def test_root_bound_small_integer_polynomials(self):
        for coeff in product(range(-2, 3), repeat=3):
            f = trim(coeff)
            if f == [0]:
                continue
            roots = [x for x in range(-8, 9) if ev(f, x) == 0]
            self.assertLessEqual(len(roots), len(f) - 1)

    def test_identity_principle_finite_check(self):
        for p in ([0], [1, 2], [2, -1, 1]):
            for q in ([0], [1, 2], [2, -1, 1]):
                equal_values = all(ev(p, x) == ev(q, x) for x in range(-3, 4))
                self.assertEqual(equal_values, p == q)

    def test_finite_field_function_kernel(self):
        for p in product(range(2), repeat=5):
            f = trim(p)
            zero_fun = all(ev(f, a) % 2 == 0 for a in range(2))
            _, r = div_monic(f, [0, -1, 1])
            self.assertEqual(zero_fun, all(c % 2 == 0 for c in r))

    def test_finite_field_counterexample(self):
        f = [0, -1, 1]
        self.assertNotEqual(trim(f), [0])
        self.assertEqual([ev(f, x) % 2 for x in range(2)], [0, 0])

    def test_lagrange_interpolation(self):
        for xs in ((-1, 0, 1), (0, 2, 5), (-3, 2, 7)):
            for ys in ((1, 2, 4), (0, 0, 0), (-2, 1, 3)):
                pts = [(Fraction(x), Fraction(y)) for x, y in zip(xs, ys)]
                p = lagrange(pts)
                self.assertLess(len(p), 4)
                self.assertEqual([ev(p, x) for x in xs], list(ys))

    def test_interpolation_examples(self):
        self.assertEqual(lagrange([(Fraction(0), Fraction(1)), (Fraction(1), Fraction(3))]), [1, 2])
        self.assertEqual(lagrange([(Fraction(-1), Fraction(2)), (Fraction(0), Fraction(1)), (Fraction(1), Fraction(2))]), [1, 0, 1])

    def test_composition_homomorphism(self):
        p, q, g = [2, 3, 1], [-1, 0, 2], [1, 2]
        self.assertEqual(compose(add(p, q), g), add(compose(p, g), compose(q, g)))
        self.assertEqual(compose(mul(p, q), g), mul(compose(p, g), compose(q, g)))

    def test_degree_composition(self):
        for m in range(1, 5):
            for n in range(1, 5):
                p = [1] + [0] * (m - 1) + [2]
                q = [3] + [0] * (n - 1) + [4]
                self.assertEqual(len(compose(p, q)) - 1, m * n)

    def test_formal_chain_rule(self):
        for f in ([0], [1, 2], [2, 0, 3], [1, -2, 3, 1]):
            for g in ([1], [2, 1], [1, 0, 2]):
                self.assertEqual(derivative(compose(f, g)), mul(compose(derivative(f), g), derivative(g)))

    def test_derivative_char_five(self):
        self.assertEqual([x % 5 for x in derivative([0, 0, 0, 0, 0, 1])], [0, 0, 0, 0, 0])

    def test_equation_multiplication_extra_roots(self):
        orig = {x for x in range(-4, 5) if x - 1 == 0}
        after = {x for x in range(-4, 5) if x * (x - 1) == 0}
        self.assertEqual(orig, {1})
        self.assertEqual(after, {0, 1})

    def test_exact_zero_locus_union(self):
        for c in range(-2, 3):
            for d in range(-2, 3):
                left = {x for x in range(-4, 5) if (x - c) * (x - d) == 0}
                right = {x for x in range(-4, 5) if x == c or x == d}
                self.assertEqual(left, right)

    def test_zero_divisor_counterexample(self):
        self.assertEqual((2 * 3) % 6, 0)
        self.assertNotEqual(2 % 6, 0)
        self.assertNotEqual(3 % 6, 0)

    def test_four_roots_mod_eight(self):
        self.assertEqual([x for x in range(8) if (x * x - 1) % 8 == 0], [1, 3, 5, 7])

    def test_capture_avoidance_counterexample(self):
        # In the 2-element ordered model: forall z (y < z) differs from forall y (y < y).
        universe = (0, 1)
        for y in universe:
            corrected = all(y < z for z in universe)
            captured = all(z < z for z in universe)
            self.assertEqual(captured, False)
            self.assertEqual(corrected, False)
        # Semantic distinction on a model with a non-reflexive relation: R(x,y) := x != y.
        # exists y R(x,y) is true for each x, whereas naive x:=y -> exists y R(y,y) is false.
        for y in universe:
            self.assertTrue(any(y != z for z in universe))
        self.assertFalse(any(z != z for z in universe))

    def test_12_task_answers(self):
        self.assertEqual(ev([0, 0, 1, -1], 0), 0)
        self.assertEqual(mul([-2, 1], [4, 2, 1]), [-8, 0, 0, 1])
        self.assertEqual(len(compose([1, 0, 1], [0, -1, 0, 1])) - 1, 6)
        self.assertEqual(derivative([0, 1, 1]), [1, 2])
        self.assertEqual(derivative([0, 0, 0, 1]), [0, 0, 3])


if __name__ == '__main__':
    unittest.main()
