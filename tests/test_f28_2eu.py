"""Exact rational regression for F28.2-EU. Run: python -m unittest tests/test_f28_2eu.py"""
from fractions import Fraction as F
from itertools import product
import unittest


def stats(indices, xs, ws):
    if not indices:
        raise ValueError("empty block")
    w = sum((ws[i] for i in indices), F(0))
    m = sum((ws[i] * xs[i] for i in indices), F(0))
    q = sum((ws[i] * xs[i] ** 2 for i in indices), F(0))
    return w, m, q


def energy(indices, xs, ws):
    w, m, q = stats(indices, xs, ws)
    return q - m * m / w


def delta_formula(a, b, u, v, xs, ws):
    aw, am, _ = stats(a, xs, ws)
    bw, bm, _ = stats(b, xs, ws)
    uw = sum((ws[i] for i in u), F(0))
    vw = sum((ws[i] for i in v), F(0))
    um = sum((ws[i] * xs[i] for i in u), F(0))
    vm = sum((ws[i] * xs[i] for i in v), F(0))
    if aw - uw + vw <= 0 or bw - vw + uw <= 0:
        raise ValueError("empty result")
    return am * am / aw + bm * bm / bw - (am - um + vm) ** 2 / (aw - uw + vw) - (bm - vm + um) ** 2 / (bw - vw + uw)


class BatchTransfer(unittest.TestCase):
    def test_exhaustive(self):
        checks = 0
        for vals in product((-1, 0, 2), repeat=4):
            xs = tuple(map(F, vals))
            for weights in product((1, 2), repeat=4):
                ws = tuple(map(F, weights))
                a, b = (0, 1), (2, 3)
                for masku in range(4):
                    for maskv in range(4):
                        u = tuple(a[i] for i in range(2) if masku & (1 << i))
                        v = tuple(b[i] for i in range(2) if maskv & (1 << i))
                        ap = tuple(i for i in a if i not in u) + v
                        bp = tuple(i for i in b if i not in v) + u
                        if not ap or not bp:
                            continue
                        old = energy(a, xs, ws) + energy(b, xs, ws)
                        new = energy(ap, xs, ws) + energy(bp, xs, ws)
                        d = delta_formula(a, b, u, v, xs, ws)
                        self.assertEqual(new - old, d)
                        self.assertEqual(delta_formula(ap, bp, v, u, xs, ws), -d)
                        ys = tuple(3 * x + 7 for x in xs)
                        self.assertEqual(delta_formula(a, b, u, v, ys, ws), 9 * d)
                        checks += 3
        print("F28.2-EU exact assertions:", checks)

    def test_examples(self):
        xs = tuple(map(F, (0, 10, 4, 6)))
        ws = (F(1),) * 4
        self.assertEqual(delta_formula((0, 1), (2, 3), (1,), (2,), xs, ws), -36)
        xs2 = tuple(map(F, (0, 2, 8, 10)))
        self.assertEqual(delta_formula((0, 1), (2, 3), (), (2,), xs2, ws), F(92, 3))
        self.assertEqual(delta_formula((0, 1), (2, 3), (1,), (2,), xs2, ws), 60)


if __name__ == "__main__":
    unittest.main()
