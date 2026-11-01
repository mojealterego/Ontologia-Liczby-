"""F22.2: finite algebraic certificates; not a formal proof assistant."""
import unittest
import sympy as s

X=s.symbols('X')

def reduced_and_exclusions(p,q):
    p,q=s.Poly(p,X,domain=s.QQ),s.Poly(q,X,domain=s.QQ)
    if q.is_zero: raise ZeroDivisionError('formal denominator zero')
    g=s.gcd(p,q).monic()
    return p.exquo(g),q.exquo(g),q

def solve_rational(p,q,r,t):
    """Solve p/q=r/t over reals; filter excluded roots exactly."""
    num=s.expand(p*t-r*q)
    cand=s.solveset(num,X,domain=s.S.Reals)
    dom=s.Complement(s.S.Reals,s.Union(s.solveset(q,X,domain=s.S.Reals),s.solveset(t,X,domain=s.S.Reals)))
    return s.Intersection(cand,dom)

class F222(unittest.TestCase):
    def test_cancel_retains_domain(self):
        p,q,orig=reduced_and_exclusions((X-2)*(X+3),X-2)
        self.assertEqual(p.as_expr(),X+3)
        self.assertEqual(q.as_expr(),1)
        self.assertEqual(orig.eval(2),0)
    def test_unique_reduced_form(self):
        a,b,_=reduced_and_exclusions(X**2-1,X**2-2*X+1)
        self.assertEqual((a.as_expr(),b.as_expr()),(X+1,X-1))
    def test_spurious_solution(self):
        self.assertEqual(solve_rational(X**2-4,X-2,4,1),s.S.EmptySet)
    def test_rational_equation(self):
        self.assertEqual(solve_rational(1,X-1,1,X+1),s.S.EmptySet)
    def test_two_roots(self):
        roots=s.solveset(2*X-(X**2-1),X,domain=s.S.Reals)
        self.assertEqual(roots,s.FiniteSet(1-s.sqrt(2),1+s.sqrt(2)))
    def test_order_removable(self):
        f=(X-1)**3*(X+2)/((X-1)**2*(X+4))
        self.assertEqual(s.limit(f,X,1),0)
    def test_pole(self):
        self.assertEqual(s.limit((X+1)/(X-3)**2,X,3),s.oo)
    def test_radical_equation(self):
        self.assertEqual(s.solveset(s.sqrt(X+5)-(X-1),X,domain=s.S.Reals),s.FiniteSet(4))
    def test_radical_domain(self):
        dom=s.solveset((X-1)/(X+2)>=0,X,domain=s.S.Reals)
        self.assertEqual(dom,s.Union(s.Interval.open(-s.oo,-2),s.Interval(1,s.oo)))
    def test_absolute(self):
        self.assertEqual(s.solveset(s.Abs(X-4)-3,X,domain=s.S.Reals),s.FiniteSet(1,7))
    def test_sign_intervals(self):
        f=(X-1)/(X+2)
        self.assertTrue(all(f.subs(X,t)>0 for t in [-5,2,10]))
        self.assertTrue(all(f.subs(X,t)<0 for t in [-1,0]))
    def test_denominator_guard(self):
        self.assertEqual(solve_rational(X-2,X-2,X+1,X+1),s.Complement(s.S.Reals,s.FiniteSet(-1,2)))
    def test_multiplication_adds_zero(self):
        self.assertEqual(s.solveset(X*(X-1),X,domain=s.S.Reals),s.FiniteSet(0,1))
    def test_sqrt_square_abs(self):
        for n in range(-20,21): self.assertEqual(s.sqrt(n*n),abs(n))
    def test_field_cancellation_counterexample(self):
        self.assertEqual((2*1)%6,(2*4)%6)
        self.assertNotEqual(1%6,4%6)
    def test_valuation_examples(self):
        p=s.Poly((X-1)**3*(X+2),X);q=s.Poly((X-1)**2*(X+4),X)
        self.assertEqual(s.limit((p.as_expr()/q.as_expr())/(X-1),X,1),s.Rational(3,5))
    def test_finite_exclusion(self):
        for n in range(-8,9):
            if n!=2:self.assertEqual(s.cancel((X-2)*(X+3)/(X-2)).subs(X,n),n+3)
    def test_cross_multiplication(self):
        for a in range(-6,7):
            if a not in (-1,1):
                lhs=s.Rational(1,a-1)+s.Rational(1,a+1)
                self.assertEqual(lhs==1, a*a-2*a-1==0)
    def test_finite_field_polynomial_zero_function(self):
        for n in range(5): self.assertEqual((n**5-n)%5,0)
    def test_zero_divisor_certificate(self):
        with self.assertRaises(ZeroDivisionError):reduced_and_exclusions(X,0)

if __name__=='__main__': unittest.main()
