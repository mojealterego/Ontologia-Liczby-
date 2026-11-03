"""Exact arithmetic checks for Ontologia Liczby Tom I, supplement F28.2-H.

These tests validate finite rational examples, not universal theorems.
"""
import unittest
from fractions import Fraction as Q


def p_a(v):
    return (v[0], Q(0))


def p_b(v):
    avg = (v[0] + v[1]) / 2
    return (avg, avg)


def norm2(v):
    return sum((x * x for x in v), Q(0))


def sub(u, v):
    return tuple(a - b for a, b in zip(u, v))


def step(x):
    y = p_b(x)
    z = p_a(y)
    gap2 = norm2(sub(x, y)) + norm2(sub(y, z))
    return y, z, gap2


class AlternatingProjectionExactTests(unittest.TestCase):
    def test_first_projection(self):
        self.assertEqual(p_b((Q(2), Q(0))), (Q(1), Q(1)))

    def test_first_iteration(self):
        self.assertEqual(step((Q(2), Q(0)))[1], (Q(1), Q(0)))

    def test_second_iteration(self):
        self.assertEqual(step((Q(1), Q(0)))[1], (Q(1, 2), Q(0)))

    def test_first_gap(self):
        self.assertEqual(step((Q(2), Q(0)))[2], Q(3))

    def test_fejer_equality_on_lines(self):
        for t in range(-20, 21):
            x = (Q(t), Q(0))
            _, nxt, gap2 = step(x)
            self.assertEqual(norm2(nxt) + gap2, norm2(x))

    def test_exact_geometric_formula(self):
        x = (Q(2), Q(0))
        for k in range(16):
            self.assertEqual(x, (Q(2, 2**k), Q(0)))
            x = step(x)[1]

    def test_gap_formula(self):
        for k in range(12):
            x = (Q(2, 2**k), Q(0))
            self.assertEqual(step(x)[2], Q(3, 4**k))

    def test_telescope(self):
        x = (Q(2), Q(0))
        total = Q(0)
        for n in range(1, 14):
            _, x, gap2 = step(x)
            total += gap2
            self.assertEqual(total, Q(4) * (Q(1) - Q(1, 4**n)))
            self.assertLessEqual(total, Q(4))

    def test_min_gap_bound(self):
        for n in range(1, 14):
            gaps = [Q(3, 4**k) for k in range(n)]
            self.assertLessEqual(min(gaps), Q(4, n))

    def test_feasibility_certificate_squared(self):
        for t in range(-10, 11):
            x = (Q(t), Q(0))
            self.assertEqual(norm2(sub(x, p_b(x))), Q(t*t, 2))

    def test_linear_regular_error_bound(self):
        for t in range(-10, 11):
            x = (Q(t), Q(0))
            delta_squared = norm2(sub(x, p_b(x)))
            self.assertEqual(norm2(x), 2 * delta_squared)

    def test_rate_bound_and_exact_rate(self):
        for t in range(-10, 11):
            x = (Q(t), Q(0))
            x_next = step(x)[1]
            self.assertEqual(norm2(x_next), Q(1, 4) * norm2(x))
            self.assertLessEqual(norm2(x_next), Q(1, 2) * norm2(x))

    def test_noncommutativity(self):
        u = (Q(1), Q(0))
        self.assertNotEqual(p_a(p_b(u)), p_b(p_a(u)))

    def test_projector_idempotence(self):
        for a in range(-3, 4):
            for b in range(-3, 4):
                x = (Q(a), Q(b))
                self.assertEqual(p_a(p_a(x)), p_a(x))
                self.assertEqual(p_b(p_b(x)), p_b(x))

    def test_nonexpansiveness(self):
        points = [(Q(a), Q(b)) for a in range(-2, 3) for b in range(-2, 3)]
        for x in points:
            for y in points:
                self.assertLessEqual(norm2(sub(p_a(x), p_a(y))), norm2(sub(x, y)))
                self.assertLessEqual(norm2(sub(p_b(x), p_b(y))), norm2(sub(x, y)))

    def test_fixed_point_only_intersection_for_lines(self):
        for a in range(-3, 4):
            for b in range(-3, 4):
                x = (Q(a), Q(b))
                if step(x)[1] == x:
                    self.assertEqual(x, (Q(0), Q(0)))

    def test_tangent_sets_no_uniform_error_bound(self):
        for n in range(2, 60):
            t = Q(1, n)
            dist_to_intersection = t
            upper_bound_delta = t * t
            self.assertGreater(dist_to_intersection, upper_bound_delta)
            self.assertGreater(dist_to_intersection / upper_bound_delta, n - 1)

    def test_interval_projection_example(self):
        def interval_projection(t):
            return min(max(t, Q(0)), Q(1))
        self.assertEqual(interval_projection(Q(3)), Q(1))
        self.assertEqual(interval_projection(interval_projection(Q(3))), Q(1))

    def test_t7_only_after_first_step(self):
        x = (Q(2), Q(5))
        _, next_x, _ = step(x)
        self.assertEqual(next_x[1], Q(0))
        self.assertEqual(norm2(sub(next_x, p_b(next_x))), next_x[0]**2 / 2)


if __name__ == "__main__":
    unittest.main()
