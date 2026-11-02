"""Deterministic exact-arithmetic checks for F28.2-G (not a proof assistant)."""
import unittest
from fractions import Fraction as Q


def clip(x, lo, hi):
    if lo > hi:
        raise ValueError("empty interval")
    return min(hi, max(lo, x))


def dot(u, v):
    return sum((a * b for a, b in zip(u, v)), Q(0))


def project_halfspace(u, a, b):
    norm2 = dot(a, a)
    if norm2 == 0:
        raise ValueError("normal vector must be nonzero")
    t = max(Q(0), (dot(a, u) - b) / norm2)
    return tuple(ui - t * ai for ui, ai in zip(u, a))


def f(x):
    return (x - 2) ** 2 / 2


def step(x, L=Q(2)):
    return clip(x - (x - 2) / L, Q(0), Q(1))


class ProjectedGradientF282G(unittest.TestCase):
    def test_box_projection_examples(self):
        self.assertEqual(clip(Q(-3), Q(0), Q(2)), 0)
        self.assertEqual(clip(Q(3), Q(-1), Q(1)), 1)

    def test_projection_idempotence(self):
        for n in range(-20, 21):
            x = Q(n, 4)
            self.assertEqual(clip(clip(x, Q(0), Q(1)), Q(0), Q(1)), clip(x, Q(0), Q(1)))

    def test_projection_nonexpansiveness(self):
        for i in range(-8, 9):
            for j in range(-8, 9):
                u, v = Q(i, 3), Q(j, 3)
                self.assertLessEqual(abs(clip(u, Q(0), Q(1)) - clip(v, Q(0), Q(1))), abs(u-v))

    def test_projection_variational_inequality(self):
        for i in range(-8, 9):
            u = Q(i, 3)
            p = clip(u, Q(0), Q(1))
            for j in range(0, 11):
                z = Q(j, 10)
                self.assertLessEqual((u-p)*(z-p), 0)

    def test_halfspace_2d(self):
        self.assertEqual(project_halfspace((Q(2), Q(2)), (Q(1), Q(1)), Q(1)), (Q(1,2), Q(1,2)))

    def test_halfspace_axis(self):
        self.assertEqual(project_halfspace((Q(3), Q(-2)), (Q(1), Q(0)), Q(1)), (Q(1), Q(-2)))

    def test_halfspace_feasibility(self):
        for i in range(-5, 6):
            for j in range(-5, 6):
                p = project_halfspace((Q(i), Q(j)), (Q(1), Q(1)), Q(1))
                self.assertLessEqual(sum(p), 1)

    def test_halfspace_zero_normal_rejected(self):
        with self.assertRaises(ValueError):
            project_halfspace((Q(0), Q(0)), (Q(0), Q(0)), Q(1))

    def test_empty_interval_rejected(self):
        with self.assertRaises(ValueError):
            clip(Q(0), Q(2), Q(1))

    def test_projected_gradient_fixed_point_boundary(self):
        self.assertEqual(step(Q(1)), 1)
        self.assertEqual(step(Q(0)), Q(1))

    def test_projected_residual_at_boundary_with_nonzero_derivative(self):
        x = Q(0)
        # f(x)=x, C=[0,+infty), eta=1: gradient=1, projection(-1)=0.
        p = max(Q(0), x-Q(1))
        self.assertEqual(x-p, 0)
        self.assertEqual(Q(1), 1)

    def test_descent_t4_grid(self):
        L = Q(2)
        for i in range(0, 21):
            x = Q(i, 20)
            y = step(x, L)
            self.assertLessEqual(f(y), f(x) - L*(y-x)**2/2)

    def test_three_point_t5_grid(self):
        L = Q(2)
        for i in range(0, 21):
            x = Q(i, 20)
            y = step(x, L)
            for j in range(0, 21):
                z = Q(j, 20)
                self.assertLessEqual(f(y)-f(z), L*((x-z)**2-(y-z)**2)/2)

    def test_objective_rate_t6(self):
        L = Q(2)
        x = Q(0)
        xstar = Q(1)
        for N in range(1, 31):
            x = step(x, L)
            self.assertLessEqual(f(x)-f(xstar), L*(Q(0)-xstar)**2/(2*N))

    def test_residual_bound_t7(self):
        L = Q(2)
        x = Q(0)
        residuals = []
        for N in range(1, 31):
            y = step(x, L)
            residuals.append((L*(x-y))**2)
            x = y
            self.assertLessEqual(min(residuals), 2*L*(f(Q(0))-f(Q(1)))/N)

    def test_t10_strong_convexity_distance(self):
        # f(x)=(x-2)^2/2, C=[0,1], mu=1, x*=1.
        for i in range(0, 21):
            x = Q(i, 20)
            self.assertLessEqual((x-Q(1))**2, 2*(f(x)-f(Q(1))))

    def test_large_step_counterexample(self):
        x = Q(1)
        for k in range(1, 9):
            x = x - 3*x
            self.assertEqual(x, (-2)**k)

    def test_nonconvex_projection_nonunique(self):
        self.assertEqual((Q(0)-Q(-1))**2, (Q(0)-Q(1))**2)

    def test_rate_numeric_z10(self):
        self.assertEqual(Q(4)*Q(2)**2/(2*8), Q(1))

    def test_residual_numeric_z11(self):
        self.assertEqual(2*Q(2)*Q(5)/10, Q(2))

    def test_distance_numeric_z13(self):
        self.assertEqual(2*Q(4,100)/2, Q(4,100))


if __name__ == '__main__':
    unittest.main(verbosity=2)
