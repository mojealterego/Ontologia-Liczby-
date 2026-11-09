from fractions import Fraction as F
from itertools import product

def radius(c, a):
    values = [F(ci, ai) for ci, ai in zip(c, a) if ai]
    return min(values) if values else None

def test_exact_box_vertices():
    checked = 0
    for c in product(range(1, 6), repeat=2):
        for a in product(range(4), repeat=2):
            r = radius(c, a)
            for t in (F(0), F(1, 2), F(1), F(2), F(3), F(5)):
                robust = all(F(ci) > t * ai for ci, ai in zip(c, a))
                expected = r is None or t < r
                assert robust == expected, (c, a, t, r)
                checked += 1
    assert checked == 2400

if __name__ == "__main__":
    test_exact_box_vertices()
    print("PASS: 2400 exact rational instances")
