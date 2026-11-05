from fractions import Fraction as F
from itertools import combinations_with_replacement

def test_median_cell_bounds():
    checks = 0
    for n in range(2, 9):
        for values in combinations_with_replacement(range(5), n):
            q = list(map(F, values))
            for k in range(1, n + 1):
                if n % k:
                    continue
                width = n // k
                cs = [q[i * width + width // 2] for i in range(k)]
                err = sum((abs(q[j] - cs[j // width]) for j in range(n)), F(0)) / n
                d = sum((q[(i + 1) * width - 1] - q[i * width] for i in range(k)), F(0))
                assert err <= F(width, 2 * n) * d
                assert err <= F(1, 2 * k) * (q[-1] - q[0])
                checks += 2
                for i in range(k):
                    c = cs[i]
                    cost = sum((abs(q[j] - c) for j in range(i * width, (i + 1) * width)), F(0))
                    for z in range(5):
                        assert cost <= sum((abs(q[j] - z) for j in range(i * width, (i + 1) * width)), F(0))
                        checks += 1
    print("PASS", checks, "exact assertions")

if __name__ == "__main__":
    test_median_cell_bounds()
