"""Exact rational regression for F28.2-ER."""
from fractions import Fraction as F
from itertools import product

def energy(a):
    w = sum((v for x, v in a), F(0))
    mu = sum((x*v for x, v in a), F(0))/w
    return sum((v*(x-mu)**2 for x, v in a), F(0))

def test_transfer():
    checks = 0
    for n in range(3, 5):
        for vals in product((F(0), F(1), F(3)), repeat=n):
            for weights in product((F(1), F(2)), repeat=n):
                for cut in range(2, n):
                    A = list(zip(vals[:cut], weights[:cut]))
                    B = list(zip(vals[cut:], weights[cut:]))
                    for i, (z, v) in enumerate(A):
                        aa = A[:i] + A[i+1:]
                        bb = B + [(z, v)]
                        wa = sum((w for x, w in A), F(0))
                        wb = sum((w for x, w in B), F(0))
                        ma = sum((x*w for x, w in A), F(0))/wa
                        mb = sum((x*w for x, w in B), F(0))/wb
                        delta = energy(aa)+energy(bb)-energy(A)-energy(B)
                        rhs = wb*v/(wb+v)*(z-mb)**2-wa*v/(wa-v)*(z-ma)**2
                        assert delta == rhs
                        assert energy(A)+energy(B)-energy(aa)-energy(bb) == -delta
                        checks += 2
    assert checks == 13824

if __name__ == "__main__":
    test_transfer()
    print("PASS: 13824 exact rational assertions")
