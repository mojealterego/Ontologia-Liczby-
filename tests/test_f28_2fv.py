from fractions import Fraction

def iterate(y0, u):
    y = Fraction(y0)
    result = [y]
    for n, value in enumerate(u):
        y = Fraction(n+1, n+2)*y + value
        result.append(y)
    return result

checks = 0
for y0 in [Fraction(-7,3), Fraction(0), Fraction(11,5)]:
    for period in [[1], [1,-1], [1,0,-1,0], [1,-1,0]]:
        for length in range(1,90):
            u = [Fraction(period[j%len(period)]) for j in range(length)]
            actual = iterate(y0, u)
            for n, value in enumerate(actual):
                expected = (y0 + sum((j+2)*u[j] for j in range(n)))/Fraction(n+1)
                assert value == expected
                checks += 1
for n in range(1,100):
    assert iterate(0,[Fraction(1)]*n)[-1] == Fraction(n*(n+3),2*(n+1))
    checks += 1
print("PASS", checks, "exact rational checks")
