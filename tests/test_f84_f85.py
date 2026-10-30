"""Finite reproducible examples for F8.4/F8.5.

Not a formal proof of Gödel/Cohen, compactness or model-theoretic claims.
Run: python -m pytest -q tests/test_f84_f85.py
"""
from itertools import product
from fractions import Fraction


def partial_conditions(n):
    for values in product((None, 0, 1), repeat=n):
        yield {k: v for k, v in enumerate(values) if v is not None}


def test_forcing_conditions_common_extension_exactly_when_compatible():
    conditions = list(partial_conditions(4))
    assert len(conditions) == 81
    for a in conditions:
        for b in conditions:
            compatible = all(a[k] == b[k] for k in a.keys() & b.keys())
            union = {**a, **b}
            extends_both = all(union[k] == v for k, v in a.items()) and all(
                union[k] == v for k, v in b.items()
            )
            assert compatible == extends_both


def test_finite_powerset_cardinality():
    for n in range(16):
        assert 2**n > n
    assert 2**5 == 32


def test_interval_affine_mapping_is_bijection_on_rational_samples():
    a, b, c, d = map(Fraction, (1, 5, -3, 11))
    for k in range(1, 250):
        x = a + (b - a) * Fraction(k, 250)
        y = c + (d - c) * (x - a) / (b - a)
        assert c < y < d
        assert a + (b - a) * (y - c) / (d - c) == x


def test_finite_diagonal_is_outside_every_given_row():
    for n in range(1, 24):
        rows = [[(i + 3*j + j*j) % 2 for j in range(n)] for i in range(n)]
        diagonal = [1 - rows[i][i] for i in range(n)]
        assert all(diagonal != row for row in rows)


def test_explicit_compatible_and_incompatible_conditions():
    p, q, r = {(1, 0): 0}, {(1, 1): 1}, {(1, 0): 1}
    assert all(p[k] == q[k] for k in p.keys() & q.keys())
    assert not all(p[k] == r[k] for k in p.keys() & r.keys())


def test_two_element_groups_are_isomorphic():
    f = {0: 1, 1: -1}
    assert set(f.values()) == {-1, 1}
    for a, b in product(range(2), repeat=2):
        assert f[(a + b) % 2] == f[a] * f[b]


def test_von_neumann_and_zermelo_codings_differ_at_two():
    zero = frozenset()
    vn, ze = [zero], [zero]
    for _ in range(4):
        vn.append(frozenset(set(vn[-1]) | {vn[-1]}))
        ze.append(frozenset({ze[-1]}))
    assert len(set(vn)) == 5
    assert len(set(ze)) == 5
    assert vn[0] == ze[0]
    assert vn[2] != ze[2]


def test_additive_group_has_unique_identity():
    elements = range(2)
    identities = [
        e for e in elements
        if all((e + x) % 2 == x and (x + e) % 2 == x for x in elements)
    ]
    assert identities == [0]


def test_recurrence_examples():
    f, g = 3, 0
    for n in range(75):
        assert f == 3 + 2 * n
        assert g == n % 2
        f, g = f + 2, 1 - g
