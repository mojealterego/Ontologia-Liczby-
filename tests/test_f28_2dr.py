from fractions import Fraction as F
from itertools import combinations_with_replacement

def cost(values, cuts):
    n = len(values)
    assert cuts[0] == 0 and cuts[-1] == n
    total = F(0)
    for a, b in zip(cuts, cuts[1:]):
        mean = sum(values[a:b], F(0)) / (b - a)
        total += sum(((v - mean) ** 2 for v in values[a:b]), F(0)) / n
    return total

count = 0
for n in range(2, 9):
    for values in combinations_with_replacement(range(4), n):
        vals = tuple(map(F, values))
        for split in range(1, n):
            w = cost(vals, (0, split, n))
            h = F(max(split, n - split), n)
            assert F(0) <= w <= h * (vals[-1] - vals[0]) ** 2 / 4
            count += 2
assert cost((F(0), F(2)), (0, 2)) == 1
assert cost((F(0), F(2)), (0, 1, 2)) == 0
print("PASS", count + 2, "exact rational assertions")
