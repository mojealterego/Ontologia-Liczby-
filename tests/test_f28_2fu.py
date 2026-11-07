from fractions import Fraction
import unittest

def iterate(u, y0, n):
    y = Fraction(y0)
    values = [y]
    for k in range(n):
        y = Fraction(k + 1, k + 2) * y + u[k % len(u)]
        values.append(y)
    return values

class PeriodicForcingTests(unittest.TestCase):
    def test_exact_formula(self):
        for period in ((0,), (1,), (1,-1), (2,-1,-1), (1,-1,2,-2)):
            u = tuple(map(Fraction, period))
            for y0 in (-3, 0, 4):
                vals = iterate(u, y0, 100)
                for n in range(1,101):
                    rhs = (Fraction(y0) + sum((j+2)*u[j%len(u)] for j in range(n)))/(n+1)
                    self.assertEqual(vals[n], rhs)

    def test_zero_mean_cycle(self):
        for period in ((1,-1), (2,-1,-1), (1,-1,2,-2)):
            u = tuple(map(Fraction, period))
            s = [Fraction(0)]
            for a in u[:-1]:
                s.append(s[-1]+a)
            avg = sum(s)/len(s)
            z = [v-avg for v in s]
            self.assertEqual(sum(z), 0)
            for r in range(len(u)):
                self.assertEqual(z[(r+1)%len(u)]-z[r],u[r])
            vals = iterate(u, 3, 1200)
            for n in range(1,1201):
                self.assertLessEqual(abs(vals[n]-z[n%len(u)]),Fraction(30,n+1))

    def test_constant_closed_form(self):
        for c in (-2,0,3):
            vals = iterate((Fraction(c),),5,100)
            for n in range(1,101):
                self.assertEqual(vals[n],Fraction(10+c*n*(n+3),2*(n+1)))

if __name__ == '__main__':
    unittest.main()
