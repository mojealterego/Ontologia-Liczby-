"""Finite exact-arithmetic checks of F17.3 D19--D24, T59--T71.

These checks are not formal proofs. All rational computations use Fraction;
no floating point tolerance is used for mathematical assertions.
"""
from __future__ import annotations

import itertools
import re
import unittest
from fractions import Fraction as Q
from pathlib import Path


def energy(u):
    return sum((y - x) ** 2 for x, y in zip(u, u[1:]))


def laplace(u, n):
    return 2 * u[n] - u[n - 1] - u[n + 1]


def green(N, n, k):
    return Q(min(n, k) * (N - max(n, k)), N)


def affine(N, A, B):
    return [A + Q(n * (B - A), N) for n in range(N + 1)]


def poisson(N, A, B, source):
    baseline = affine(N, A, B)
    return [baseline[n] + sum(green(N, n, k) * source[k - 1]
                              for k in range(1, N)) for n in range(N + 1)]


class DirichletGreenTests(unittest.TestCase):
    def test_01_cauchy_schwarz_interval_exhaustive(self):
        for N in range(1, 5):
            for values in itertools.product(range(-2, 3), repeat=N + 1):
                self.assertLessEqual((values[-1] - values[0]) ** 2, N * energy(values))

    def test_02_dirichlet_equality_characterization(self):
        for N in range(1, 7):
            for A, B in itertools.product(range(-3, 4), repeat=2):
                u = affine(N, Q(A), Q(B))
                self.assertEqual(energy(u), Q((B - A) ** 2, N))

    def test_03_harmonicity_and_maximum(self):
        for N in range(1, 9):
            for A, B in itertools.product([-4, 0, 5], repeat=2):
                u = affine(N, Q(A), Q(B))
                self.assertTrue(all(laplace(u, n) == 0 for n in range(1, N)))
                self.assertTrue(all(min(A, B) <= x <= max(A, B) for x in u))

    def test_04_green_kernel_delta_and_symmetry(self):
        for N in range(2, 13):
            for k in range(1, N):
                g = [green(N, n, k) for n in range(N + 1)]
                self.assertEqual(g[0], 0)
                self.assertEqual(g[-1], 0)
                for n in range(1, N):
                    self.assertEqual(laplace(g, n), int(n == k))
                    self.assertEqual(g[n], green(N, k, n))
                    self.assertGreaterEqual(g[n], 0)

    def test_05_poisson_inverse_exact(self):
        for N in range(1, 9):
            for A, B in [(Q(0), Q(0)), (Q(1, 3), Q(7, 4))]:
                for s in range(4):
                    f = [Q(((k * 3 + s) % 7) - 3, k + 1) for k in range(1, N)]
                    u = poisson(N, A, B, f)
                    self.assertEqual(u[0], A)
                    self.assertEqual(u[-1], B)
                    self.assertEqual([laplace(u, n) for n in range(1, N)], f)

    def test_06_discrete_green_identity(self):
        for N in range(1, 7):
            for t in range(15):
                u = [Q((i * i + t * 2 + i * t) % 11 - 5, i + 1) for i in range(N + 1)]
                v = [Q((3 * i + t * i + 1) % 13 - 6, i + 2) for i in range(N + 1)]
                lhs = sum((u[n + 1] - u[n]) * (v[n + 1] - v[n]) for n in range(N))
                rhs = sum(v[n] * laplace(u, n) for n in range(1, N))
                rhs += v[-1] * (u[-1] - u[-2]) - v[0] * (u[1] - u[0])
                self.assertEqual(lhs, rhs)

    def test_07_energy_orthogonal_decomposition(self):
        for N in range(1, 9):
            A, B = Q(3, 2), Q(-5, 3)
            baseline = affine(N, A, B)
            deviation = [Q(0)] + [Q((j * j + 2) % 7 - 3, j + 2) for j in range(1, N)] + [Q(0)]
            u = [x + y for x, y in zip(baseline, deviation)]
            self.assertEqual(energy(u), energy(baseline) + energy(deviation))

    def test_08_pointwise_poincare(self):
        for N in range(2, 11):
            for t in range(10):
                v = [Q(0)] + [Q((j * t + j * j + 1) % 13 - 6, j + 1) for j in range(1, N)] + [Q(0)]
                E = energy(v)
                for j in range(1, N):
                    self.assertLessEqual(v[j] ** 2, Q(j * (N - j), N) * E)
                self.assertLessEqual(sum(x*x for x in v[1:-1]), Q(N*N - 1, 6) * E)

    def test_09_sharp_pointwise_constant(self):
        for N in range(2, 9):
            for j in range(1, N):
                increments = [Q(N-j, N) if n < j else Q(-j, N) for n in range(N)]
                v = [Q(0)]
                for d in increments:
                    v.append(v[-1] + d)
                self.assertEqual(v[-1], 0)
                self.assertEqual(v[j] ** 2, Q(j*(N-j), N) * energy(v))

    def test_10_weighted_minimizer(self):
        for weights in [[Q(1), Q(3)], [Q(2), Q(5), Q(7)], [Q(1, 3), Q(2), Q(9, 2), Q(4)]]:
            A, B = Q(-2), Q(5)
            R = sum(1 / w for w in weights)
            increments = [(B - A) / (w * R) for w in weights]
            self.assertEqual(sum(increments), B - A)
            weighted_energy = sum(w * d*d for w, d in zip(weights, increments))
            self.assertEqual(weighted_energy, (B-A)**2 / R)
            for j in range(len(weights)):
                perturbed = increments.copy()
                if j + 1 < len(weights):
                    perturbed[j] += Q(1, 7)
                    perturbed[j+1] -= Q(1, 7)
                    self.assertGreater(sum(w*d*d for w, d in zip(weights, perturbed)), weighted_energy)

    def test_11_positive_source_comparison(self):
        for N in range(2, 9):
            f = [Q(k % 3) for k in range(1, N)]
            u = poisson(N, Q(-1), Q(3), f)
            baseline = affine(N, Q(-1), Q(3))
            self.assertTrue(all(x >= y for x, y in zip(u, baseline)))
            if any(f):
                self.assertTrue(all(u[j] > baseline[j] for j in range(1, N)))

    def test_12_examples_and_counterexamples(self):
        self.assertEqual(poisson(2, Q(0), Q(0), [Q(2)]), [Q(0), Q(1), Q(0)])
        self.assertEqual(poisson(3, Q(0), Q(0), [Q(1), Q(-1)]), [Q(0), Q(1, 3), Q(-1, 3), Q(0)])
        self.assertEqual(green(4, 1, 3), Q(1, 4))
        self.assertEqual(green(4, 2, 2), Q(1))
        self.assertEqual(energy([Q(0), Q(2), Q(1), Q(3)]), 9)
        self.assertEqual(energy([Q(0), Q(1), Q(1), Q(0)]), 2)

    def test_13_strict_convexity(self):
        for N in range(2, 8):
            u = [Q(0)] + [Q(j*j) for j in range(1, N)] + [Q(0)]
            v = [Q(0)] + [Q(-j) for j in range(1, N)] + [Q(0)]
            midpoint = [(x + y) / 2 for x, y in zip(u, v)]
            self.assertLess(energy(midpoint), (energy(u) + energy(v)) / 2)

    def test_14_document_numbering(self):
        path = Path(__file__).resolve().parent.parent / "manuscript" / "tom-01" / "F17" / "F17.3_UZUPELNIENIE_GEOMETRIA_DYSKRETNA.md"
        if not path.exists():
            self.skipTest("Source absent from local test directory; repo path is checked in CI")
        content = path.read_text(encoding="utf-8")
        for prefix, pattern, last in [
            ("D", r"\*\*Definicja D(\d+)", 24),
            ("T", r"\*\*(?:Twierdzenie|Wniosek) T(\d+)", 71),
            ("K", r"\*\*(?:Kontrprzykład )?K(\d+)\b", 33),
            ("Z", r"\*\*(?:Zadanie )?Z(\d+)\b", 74),
        ]:
            nums = list(map(int, re.findall(pattern, content)))
            self.assertEqual(nums, list(range(1, last + 1)), prefix)


if __name__ == "__main__":
    unittest.main()
