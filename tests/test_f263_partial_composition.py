"""Exact finite-model regression for F26.3; no external dependencies."""
from __future__ import annotations

import itertools
import math
import unittest
from fractions import Fraction


def partial_maps(source, target):
    """Enumerate all partial functions source -> target, including empty."""
    source, target = tuple(source), tuple(target)
    for assignment in itertools.product((None, *target), repeat=len(source)):
        yield {x: y for x, y in zip(source, assignment) if y is not None}


def compose(f, g):
    """g o f with exact domain restriction."""
    return {x: g[y] for x, y in f.items() if y in g}


def wp(f, subset):
    return {x for x, y in f.items() if y in subset}


def inverse_partial(f):
    if len(set(f.values())) != len(f):
        raise ValueError("not injective")
    return {y: x for x, y in f.items()}


def iterate(f, n, universe):
    if n < 0:
        raise ValueError("negative iterate")
    result = {x: x for x in universe}
    for _ in range(n):
        result = compose(result, f)
    return result


def order_of_permutation(p):
    if set(p) != set(p.values()):
        raise ValueError("not a permutation")
    seen, order = set(), 1
    for x in p:
        if x in seen:
            continue
        y, length = x, 0
        while y not in seen:
            seen.add(y)
            y = p[y]
            length += 1
        order = math.lcm(order, length)
    return order


def affine_interval(a, b, low, high):
    a, b, low, high = map(Fraction, (a, b, low, high))
    if a == 0 or low > high:
        raise ValueError("noninvertible or empty interval")
    return tuple(sorted((a * low + b, a * high + b)))


class F263ExactTests(unittest.TestCase):
    def test_z1_positive_domain(self):
        self.assertEqual({x for x in range(-8, 9) if x != 0 and Fraction(1, x) >= 0}, set(range(1, 9)))

    def test_z2_log_square_domain(self):
        self.assertEqual({x for x in range(-5, 6) if x*x > 0}, set(range(-5, 0)) | set(range(1, 6)))

    def test_z3_wp_affine(self):
        xs = [Fraction(i, 2) for i in range(-4, 5)]
        f = {x: 2*x + 1 for x in xs}
        self.assertEqual(wp(f, {Fraction(i, 2) for i in range(0, 7)}), {x for x in xs if Fraction(-1, 2) <= x <= 1})

    def test_z4_relative_complement(self):
        f = {x: x*x for x in range(-2, 3)}
        self.assertEqual(wp(f, set(range(1, 10))), {-2, -1, 1, 2})
        self.assertEqual(set(f) - wp(f, set(range(1, 10))), {0})

    def test_z5_inverse(self):
        f = {-2: -1, 0: 1, 3: 4}
        self.assertEqual(inverse_partial(f), {-1: -2, 1: 0, 4: 3})

    def test_z6_collision_rejected(self):
        with self.assertRaises(ValueError):
            inverse_partial({-1: 1, 1: 1})

    def test_z7_reverse_composition(self):
        f, g = {1: "a", 2: "b"}, {"a": "Y", "b": "X"}
        self.assertEqual(inverse_partial(compose(f, g)), compose(inverse_partial(g), inverse_partial(f)))

    def test_z8_partial_identity(self):
        e = {0: 0, 2: 2}
        self.assertEqual(compose(e, e), e)
        self.assertNotIn(1, e)

    def test_z9_iterated_domains(self):
        f = {0: 1, 1: 2, 2: 3}
        self.assertEqual([set(iterate(f, n, range(4))) for n in range(1, 5)], [{0, 1, 2}, {0, 1}, {0}, set()])

    def test_z10_permutation_order(self):
        self.assertEqual(order_of_permutation({0: 2, 2: 1, 1: 0, 3: 4, 4: 3}), 6)

    def test_z11_affine_interval(self):
        self.assertEqual(affine_interval(-3, 2, -1, 2), (Fraction(-4), Fraction(5)))
        for y in (Fraction(-4), Fraction(1, 2), Fraction(5)):
            x = (2-y)/3
            self.assertEqual(-3*x+2, y)

    def test_z12_quadratic_branch(self):
        self.assertEqual(Fraction(1, 4)**2 + 1, Fraction(17, 16))
        self.assertEqual(Fraction(1, 4)**2, Fraction(1, 16))

    def test_t1_domain_composition_exhaustive(self):
        for f in partial_maps(range(2), range(2)):
            for g in partial_maps(range(2), range(2)):
                self.assertEqual(set(compose(f, g)), wp(f, set(g)))

    def test_t2_associativity_exhaustive(self):
        maps = list(partial_maps(range(2), range(2)))
        for f, g, h in itertools.product(maps, repeat=3):
            self.assertEqual(compose(compose(f, g), h), compose(f, compose(g, h)))

    def test_t3_wp_chain_exhaustive(self):
        maps = list(partial_maps(range(2), range(2)))
        subsets = [set(), {0}, {1}, {0, 1}]
        for f, g, subset in itertools.product(maps, maps, subsets):
            self.assertEqual(wp(compose(f, g), subset), wp(f, wp(g, subset)))

    def test_t4_wp_complement_exhaustive(self):
        for f in partial_maps(range(3), range(2)):
            for s in (set(), {0}, {1}, {0, 1}):
                self.assertEqual(wp(f, {0, 1} - s), set(f) - wp(f, s))

    def test_t5_inverse_partial_exhaustive(self):
        for f in partial_maps(range(3), range(3)):
            if len(set(f.values())) == len(f):
                inv = inverse_partial(f)
                self.assertEqual(compose(f, inv), {x: x for x in f})
                self.assertEqual(compose(inv, f), {y: y for y in f.values()})
            else:
                with self.assertRaises(ValueError):
                    inverse_partial(f)

    def test_t6_inverse_composition_exhaustive(self):
        maps = [f for f in partial_maps(range(2), range(2)) if len(set(f.values())) == len(f)]
        for f, g in itertools.product(maps, repeat=2):
            self.assertEqual(inverse_partial(compose(f, g)), compose(inverse_partial(g), inverse_partial(f)))

    def test_t7_idempotent_injective(self):
        for f in partial_maps(range(3), range(3)):
            if len(set(f.values())) == len(f) and compose(f, f) == f:
                self.assertEqual(f, {x: x for x in f})

    def test_t7_noninjective_counterexample(self):
        e = {0: 0, 1: 0}
        self.assertEqual(compose(e, e), e)
        self.assertNotEqual(e, {x: x for x in e})

    def test_t8_iterate_domain_monotonic_exhaustive(self):
        for f in partial_maps(range(3), range(3)):
            previous = set(range(3))
            for n in range(1, 6):
                current = set(iterate(f, n, range(3)))
                self.assertTrue(current <= previous)
                previous = current

    def test_t9_permutation_lcm_exhaustive(self):
        for n in range(0, 6):
            for values in itertools.permutations(range(n)):
                p = dict(zip(range(n), values))
                order = order_of_permutation(p)
                self.assertEqual(iterate(p, order, range(n)), {x: x for x in range(n)})
                for k in range(1, order):
                    self.assertNotEqual(iterate(p, k, range(n)), {x: x for x in range(n)})

    def test_t10_affine_fraction_grid(self):
        for a, b, low, high in itertools.product(range(-3, 4), range(-2, 3), range(-2, 3), range(-2, 3)):
            if a == 0 or low > high:
                continue
            left, right = affine_interval(a, b, low, high)
            for x in (Fraction(low), Fraction(low+high, 2), Fraction(high)):
                y = a*x+b
                self.assertTrue(left <= y <= right)
                self.assertEqual((y-b)/a, x)

    def test_t10_exact_error_constant(self):
        for a in (-7, -3, -1, 1, 2, 9):
            for y, z in itertools.product(range(-3, 4), repeat=2):
                self.assertEqual(abs(Fraction(y-z, a)), Fraction(abs(y-z), abs(a)))

    def test_t11_sqrt_holder_integer_squares(self):
        for u, v in itertools.product(range(12), repeat=2):
            self.assertLessEqual(abs(u-v)**2, abs(u*u-v*v))

    def test_t11_local_lipschitz_on_squares(self):
        for u, v in itertools.product(range(1, 12), repeat=2):
            self.assertLessEqual(2*abs(u-v), abs(u*u-v*v))

    def test_t12_composition_lipschitz(self):
        for a, b in itertools.product(range(-5, 6), repeat=2):
            for x, y in itertools.product(range(-4, 5), repeat=2):
                self.assertLessEqual(abs(a*b*(x-y)), abs(a)*abs(b)*abs(x-y))

    def test_t12_inverse_lower_bound(self):
        for a in (-5, -2, -1, 1, 3, 7):
            for x, y in itertools.product(range(-4, 5), repeat=2):
                self.assertEqual(abs(Fraction(a*x-a*y, a)), abs(x-y))

    def test_partial_map_empty(self):
        self.assertEqual(compose({}, {}), {})
        self.assertEqual(inverse_partial({}), {})
        self.assertEqual(order_of_permutation({}), 1)

    def test_invalid_permutation(self):
        with self.assertRaises(ValueError):
            order_of_permutation({0: 0, 1: 0})

    def test_negative_iterate_rejected(self):
        with self.assertRaises(ValueError):
            iterate({0: 0}, -1, [0])


if __name__ == "__main__":
    unittest.main()
