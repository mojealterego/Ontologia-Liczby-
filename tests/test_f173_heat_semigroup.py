"""Finite checks for F17.3 T81–T89; not a formal proof of general claims.

Only the Python standard library is used. Run with:
    python -m unittest discover -s tests -p 'test_f173_heat_semigroup.py' -v
"""
from __future__ import annotations

import math
import re
import unittest
from fractions import Fraction
from pathlib import Path


def adjacency(n: int) -> list[list[int]]:
    """Adjacency matrix for n internal vertices (N=n+1)."""
    if n < 1:
        raise ValueError("at least one interior vertex required")
    return [[int(abs(i - j) == 1) for j in range(n)] for i in range(n)]


def multiply(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def identity(n: int):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def heat_kernel(n: int, t: float, terms: int = 120):
    """Positive adjacency-series approximation, with no matrix packages."""
    a = adjacency(n)
    power = identity(n)
    total = [[0.0 for _ in range(n)] for _ in range(n)]
    coefficient = 1.0
    for j in range(terms):
        for r in range(n):
            for s in range(n):
                total[r][s] += coefficient * power[r][s]
        power = multiply(power, a)
        coefficient *= t / (j + 1)
    factor = math.exp(-2 * t)
    return [[factor * x for x in row] for row in total]


def apply(a, x):
    return [sum(v * y for v, y in zip(row, x)) for row in a]


def euler(n: int, h: Fraction):
    a = adjacency(n)
    return [[(Fraction(1) - 2 * h if i == j else Fraction(0)) + h * a[i][j]
             for j in range(n)] for i in range(n)]


class HeatSemigroupTests(unittest.TestCase):
    def test_01_adjacency_and_laplacian(self):
        for n in range(1, 12):
            a = adjacency(n)
            self.assertEqual(a, [list(x) for x in zip(*a)])
            self.assertTrue(all(sum(row) <= 2 for row in a))
            self.assertEqual([2 - sum(row) for row in a][0], 2 if n == 1 else 1)

    def test_02_kernel_nonnegative(self):
        for n in range(1, 8):
            for t in (0.0, 0.01, 0.25, 1.0, 3.0):
                p = heat_kernel(n, t)
                self.assertTrue(all(x >= 0 for row in p for x in row))

    def test_03_strict_positive_for_positive_time(self):
        for n in range(1, 8):
            for t in (0.1, 0.5, 1.5):
                self.assertTrue(all(x > 0 for row in heat_kernel(n, t) for x in row))

    def test_04_substochastic(self):
        for n in range(1, 10):
            for t in (0.05, 0.5, 2.0):
                p = heat_kernel(n, t)
                self.assertTrue(all(0 < sum(row) < 1 + 1e-12 for row in p))
                self.assertTrue(all(sum(row) < 1 - 1e-13 for row in p))

    def test_05_symmetry(self):
        for n in range(1, 9):
            p = heat_kernel(n, 0.75)
            for i in range(n):
                for j in range(n):
                    self.assertAlmostEqual(p[i][j], p[j][i], places=12)

    def test_06_semigroup(self):
        for n in range(1, 7):
            left = heat_kernel(n, 0.8)
            right = multiply(heat_kernel(n, 0.3), heat_kernel(n, 0.5))
            for i in range(n):
                for j in range(n):
                    self.assertAlmostEqual(left[i][j], right[i][j], places=11)

    def test_07_order_preservation(self):
        for n in range(1, 8):
            p = heat_kernel(n, 0.7)
            u = [-i for i in range(n)]
            v = [i + 1 for i in range(n)]
            self.assertTrue(all(x <= y + 1e-12 for x, y in zip(apply(p, u), apply(p, v))))

    def test_08_infinity_norm_contraction(self):
        for n in range(1, 9):
            p = heat_kernel(n, 0.6)
            v = [(-1) ** i * (i + 1) for i in range(n)]
            out = apply(p, v)
            self.assertLess(max(abs(x) for x in out), max(abs(x) for x in v))

    def test_09_euler_exact_step_and_negative_diagonal(self):
        for n in range(1, 9):
            for h in (Fraction(0), Fraction(1, 4), Fraction(1, 2)):
                b = euler(n, h)
                self.assertTrue(all(x >= 0 for row in b for x in row))
                self.assertTrue(all(sum(row) <= 1 for row in b))
            self.assertLess(euler(n, Fraction(3, 4))[0][0], 0)

    def test_10_euler_limit(self):
        n, t = 4, 0.8
        expected = heat_kernel(n, t)
        for m, tol in ((100, 0.025), (1000, 0.003)):
            b = euler(n, Fraction(4, 5 * m))
            power = identity(n)
            for _ in range(m):
                power = multiply(power, b)
            self.assertLess(max(abs(float(power[i][j]) - expected[i][j])
                                for i in range(n) for j in range(n)), tol)

    def test_11_two_vertex_kernel_formula(self):
        for t in (0, 0.2, 1.0, 3.0):
            p = heat_kernel(2, t)
            a = (math.exp(-t) + math.exp(-3 * t)) / 2
            b = (math.exp(-t) - math.exp(-3 * t)) / 2
            self.assertAlmostEqual(p[0][0], a, places=11)
            self.assertAlmostEqual(p[0][1], b, places=11)
            self.assertAlmostEqual(sum(p[0]), math.exp(-t), places=11)

    def test_12_heat_trace_and_determinant(self):
        for n in range(1, 9):
            for t in (0.1, 0.7, 1.2):
                p = heat_kernel(n, t)
                trace = sum(p[i][i] for i in range(n))
                eig_trace = sum(math.exp(-(2 - 2 * math.cos(math.pi * k / (n + 1))) * t)
                                for k in range(1, n + 1))
                self.assertAlmostEqual(trace, eig_trace, places=10)
            if n == 2:
                p = heat_kernel(n, 0.7)
                self.assertAlmostEqual(p[0][0] * p[1][1] - p[0][1] * p[1][0],
                                       math.exp(-4 * 0.7), places=11)

    def test_13_constant_forcing(self):
        # For N=3, (1,1) is an eigenvector with eigenvalue 1.
        for t in (0.1, 0.5, 2.0):
            p = heat_kernel(2, t)
            solution = [1 - x for x in apply(p, [1.0, 1.0])]
            for x in solution:
                self.assertAlmostEqual(x, 1 - math.exp(-t), places=11)

    def test_14_duhamel_scalar_forcing(self):
        # v'=-2v+exp(-t), v(0)=0; exact v=exp(-t)-exp(-2t).
        for t in (0.1, 0.7, 2.0):
            expected = math.exp(-t) - math.exp(-2 * t)
            # Trapezoidal quadrature independent of the closed-form expression.
            steps = 2000
            h = t / steps
            integral = sum((0.5 if j in (0, steps) else 1.0) *
                           math.exp(-2 * (t - j * h)) * math.exp(-j * h)
                           for j in range(steps + 1)) * h
            self.assertAlmostEqual(integral, expected, places=6)

    def test_15_numbering_and_append_only_source(self):
        path = Path(__file__).resolve().parent.parent / 'manuscript' / 'tom-01' / 'F17' / 'F17.3_UZUPELNIENIE_GEOMETRIA_DYSKRETNA.md'
        if not path.is_file():
            self.skipTest('full manuscript not available in this environment')
        content = path.read_text(encoding='utf-8')
        for prefix, end in (('D', 32), ('T', 89), ('K', 44), ('Z', 97)):
            found = [int(n) for n in re.findall(r'(?m)^\*\*(?:Definicja |Twierdzenie |Wniosek |Kontrprzykład |Zadanie )?' + prefix + r'(\d+)\b', content)]
            self.assertEqual(found, list(range(1, end + 1)), f'{prefix}: gaps or duplicates')
        self.assertIn('### 22. Dodatniość przepływu cieplnego', content)


if __name__ == '__main__':
    unittest.main()
