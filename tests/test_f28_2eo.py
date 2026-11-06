"""Regression: exact weighted ANOVA for nested partitions (F28.2-EO)."""
from fractions import Fraction as F
from itertools import product

def energy(x, w, blocks):
    total = F(0)
    for b in blocks:
        mass = sum((w[i] for i in b), F(0))
        mean = sum((w[i] * x[i] for i in b), F(0)) / mass
        total += sum((w[i] * (x[i] - mean)**2 for i in b), F(0))
    return total

def partitions(seq):
    if not seq:
        yield ()
        return
    first, *rest = seq
    for p in partitions(rest):
        yield ((first,),) + p
        for j in range(len(p)):
            q = list(p)
            q[j] = (first,) + q[j]
            yield tuple(q)

def refines(p, q):
    return all(any(set(a) <= set(b) for b in q) for a in p)

def between(x, w, p, q):
    result = F(0)
    for b in q:
        mass_b = sum((w[i] for i in b), F(0))
        mean_b = sum((w[i]*x[i] for i in b), F(0))/mass_b
        for a in p:
            if set(a) <= set(b):
                mass_a = sum((w[i] for i in a), F(0))
                mean_a = sum((w[i]*x[i] for i in a), F(0))/mass_a
                result += mass_a*(mean_a-mean_b)**2
    return result

def test_exact_nested_decomposition():
    checks = 0
    for n in range(2, 5):
        ps = list(partitions(tuple(range(n))))
        for x0 in product((0, 1, 3), repeat=n):
            x = tuple(map(F, x0))
            for w0 in product((1, 2), repeat=n):
                w = tuple(map(F, w0))
                costs = [energy(x, w, p) for p in ps]
                for i, p in enumerate(ps):
                    for j, q in enumerate(ps):
                        if refines(p, q):
                            gain = costs[j]-costs[i]
                            assert gain >= 0
                            assert gain == between(x, w, p, q)
                            checks += 2
    return checks

if __name__ == "__main__":
    print("PASS exact assertions:", test_exact_nested_decomposition())
