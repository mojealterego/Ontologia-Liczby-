"""F28.1: dokładne testy certyfikatów ilorazu różnicowego.

Testy skończonych instancji nie zastępują dowodów twierdzeń ogólnych.
"""
import math
import unittest
from fractions import Fraction as F

import sympy as sp


def forward_quadratic(a, b, x, h):
    if h == 0:
        raise ValueError('h=0')
    f = lambda t: a*t*t + b*t
    return (f(x+h)-f(x))/h


def central_quadratic(a, b, x, h):
    if h == 0:
        raise ValueError('h=0')
    f = lambda t: a*t*t + b*t
    return (f(x+h)-f(x-h))/(2*h)


def central_poly(coeffs, x, h):
    if h == 0:
        raise ValueError('h=0')
    def f(t):
        return sum(c*t**i for i, c in enumerate(coeffs))
    return (f(x+h)-f(x-h))/(2*h)


def richardson_poly(coeffs, x, h):
    return (4*central_poly(coeffs, x, h/2)-central_poly(coeffs, x, h))/3


def reciprocal_forward(x, h):
    if x == 0 or h == 0 or x+h == 0:
        raise ValueError('niedozwolona dziedzina')
    return (F(1, 1)/(x+h)-F(1, 1)/x)/h


def hermite_perturbation(nodes, x, p, a):
    t = sp.symbols('t')
    H = (t-x)*sp.prod(t-s for s in set(nodes) if s != x)
    slope = sp.diff(H, t).subs(t, x)
    assert slope != 0
    return sp.expand(p+a*H/slope)


class DifferenceQuotients(unittest.TestCase):
    def test_forward_quadratic_exact(self):
        for a in range(-3, 4):
            for b in range(-2, 3):
                for x in range(-2, 3):
                    for h in [F(-2, 3), F(1, 7), F(3, 4)]:
                        self.assertEqual(forward_quadratic(F(a), F(b), F(x), h), 2*a*x+b+a*h)

    def test_central_quadratic_exact(self):
        for a in range(-3, 4):
            for b in range(-2, 3):
                for x in range(-2, 3):
                    for h in [F(-1, 3), F(1, 5)]:
                        self.assertEqual(central_quadratic(F(a), F(b), F(x), h), 2*a*x+b)

    def test_zero_step_rejected_forward(self):
        with self.assertRaises(ValueError): forward_quadratic(F(1), F(0), F(1), F(0))

    def test_zero_step_rejected_central(self):
        with self.assertRaises(ValueError): central_poly([F(0), F(1)], F(0), F(0))

    def test_forward_cubic_exact(self):
        for x in range(-3, 4):
            for h in [F(1, 4), F(-1, 4)]:
                f=lambda t:t**3
                self.assertEqual((f(x+h)-f(x))/h, 3*x*x+3*x*h+h*h)

    def test_central_cubic_exact(self):
        for x in range(-3, 4):
            for h in [F(1, 2), F(-1, 3)]:
                self.assertEqual(central_poly([0,0,0,1],F(x),h),3*x*x+h*h)

    def test_richardson_cubic_exact(self):
        for x in range(-4, 5):
            for h in [F(1, 2), F(-2, 3)]:
                self.assertEqual(richardson_poly([0,0,0,1],F(x),h),3*x*x)

    def test_richardson_quartic_exact(self):
        for x in range(-3, 4):
            self.assertEqual(richardson_poly([0,0,0,0,1],F(x),F(1,5)),4*x**3)

    def test_richardson_quintic_bound(self):
        # f=t^5: f^(5)=120, błąd rzeczywisty = 4 h^4 / 3? obliczany symbolicznie
        x=F(1,3)
        for h in [F(1,2),F(1,5),F(-1,7)]:
            d=5*x**4
            err=abs(richardson_poly([0,0,0,0,0,1],x,h)-d)
            self.assertLessEqual(err,120*h**4/F(288))

    def test_central_cubic_bound_sharp(self):
        for h in [F(1,3),F(-2,7)]:
            self.assertEqual(abs(central_poly([0,0,0,1],F(0),h)),6*h*h/6)

    def test_forward_quadratic_bound_sharp(self):
        for a in [F(1),F(-2),F(7,3)]:
            for h in [F(1,11),F(-3,4)]:
                err=abs(forward_quadratic(a,F(0),F(0),h))
                self.assertEqual(err,abs(2*a)*abs(h)/2)

    def test_reciprocal_forward(self):
        for x in [F(-4),F(-1),F(1),F(2),F(5,2)]:
            for h in [F(1,5),F(-1,7)]:
                if x+h:
                    self.assertEqual(reciprocal_forward(x,h),-1/(x*(x+h)))

    def test_reciprocal_error_identity(self):
        for x in [F(-3),F(1),F(2)]:
            for h in [F(1,8),F(-1,8)]:
                e=abs(reciprocal_forward(x,h)+1/x**2)
                self.assertEqual(e,abs(h)/(abs(x)**2*abs(x+h)))

    def test_reciprocal_certified_bound(self):
        for x in [F(-3),F(1),F(2)]:
            for h in [x/F(2),-x/F(2),x/F(10)]:
                self.assertLessEqual(abs(reciprocal_forward(x,h)+1/x**2),2*abs(h)/abs(x)**3)

    def test_reciprocal_pole_rejected(self):
        for x,h in [(F(0),F(1)),(F(1),F(-1)),(F(1),F(0))]:
            with self.assertRaises(ValueError): reciprocal_forward(x,h)

    def test_convex_secants(self):
        for u in range(-3,2):
            for v in range(u+1,4):
                for w in range(v+1,6):
                    f=lambda z:F(z*z)
                    l=(f(v)-f(u))/(v-u)
                    m=(f(w)-f(u))/(w-u)
                    r=(f(w)-f(v))/(w-v)
                    self.assertLessEqual(l,m)
                    self.assertLessEqual(m,r)

    def test_nonconvex_reverse_possible(self):
        f=lambda z:-z*z
        self.assertGreater((f(1)-f(0)),(f(3)-f(0))/3)

    def test_hermite_nodes_including_x(self):
        t=sp.symbols('t'); p=t**2+2*t+3
        for nodes in [[0],[0,1],[-1,0,1],[0,2,3,5]]:
            for a in [-9,0,7]:
                g=hermite_perturbation(nodes,0,p,a)
                for s in nodes: self.assertEqual(sp.expand(g-p).subs(t,s),0)
                self.assertEqual(sp.diff(g,t).subs(t,0),2+a)

    def test_hermite_nodes_excluding_x(self):
        t=sp.symbols('t'); p=t**2
        g=hermite_perturbation([1,2,4],0,p,sp.Rational(5,2))
        for s in [1,2,4]: self.assertEqual(g.subs(t,s),p.subs(t,s))
        self.assertEqual(sp.diff(g,t).subs(t,0),sp.Rational(5,2))

    def test_hermite_empty_nodes(self):
        t=sp.symbols('t')
        g=hermite_perturbation([],3,t**2,7)
        self.assertEqual(sp.diff(g,t).subs(t,3),13)

    def test_symmetry_absolute_value_failure(self):
        h=F(1,10)
        self.assertEqual((abs(h)-abs(-h))/(2*h),0)
        self.assertEqual((abs(h)-0)/h,1)
        self.assertEqual((abs(-h)-0)/(-h),-1)

    def test_small_values_large_derivatives(self):
        delta=F(1,100)
        for k in [1,10,1000]:
            self.assertLessEqual(abs(float(delta)*math.sin(k*0.2)),float(delta))
            self.assertEqual(delta*k,F(k,100))

    def test_perturbed_central_measurement_bound(self):
        delta=F(1,10000); h=F(1,20)
        true=lambda t:t**3
        measured_plus=true(h)+delta
        measured_minus=true(-h)-delta
        observed=(measured_plus-measured_minus)/(2*h)
        self.assertLessEqual(abs(observed),F(6)*h*h/6+delta/h)

    def test_perturbed_central_worst_case(self):
        delta=F(1,10000); h=F(1,20)
        # f=0, pomiary o przeciwnych błędach
        self.assertEqual((delta-(-delta))/(2*h),delta/h)

    def test_optimal_h(self):
        M3=6.; delta=2e-6
        h=(3*delta/M3)**(1/3)
        self.assertAlmostEqual(h,.01)
        b=lambda x:M3*x*x/6+delta/x
        self.assertLess(b(h),b(h*.9))
        self.assertLess(b(h),b(h*1.1))

    def test_optimal_h_degenerate_not_claimed(self):
        # M3=0: funkcja celu maleje do zera wraz z rosnącym h,
        # wzór z dzieleniem przez M3 nie ma zastosowania.
        delta=F(1,100)
        self.assertLess(delta/F(2),delta/F(1))

    def test_Z1_Z2(self):
        self.assertEqual(forward_quadratic(F(3),F(-2),F(2),F(1,10)),F(103,10))
        self.assertEqual(central_quadratic(F(3),F(-2),F(2),F(1,10)),10)

    def test_Z3_Z4_Z5(self):
        self.assertEqual(F(8,200),F(1,25))
        self.assertEqual(F(12,600),F(1,50))
        self.assertEqual(F(120,288*16),F(5,192))

    def test_Z6_Z7_Z8(self):
        self.assertEqual(reciprocal_forward(F(2),F(1,4)),F(-2,9))
        self.assertEqual(abs(reciprocal_forward(F(2),F(1,4))+F(1,4)),F(1,36))
        self.assertEqual(richardson_poly([0,0,0,1],F(1),F(1,2)),3)
        self.assertEqual(central_poly([0,0,0,0,1],F(0),F(1,3)),0)

    def test_Z9_Z10(self):
        self.assertTrue(F(1)<=F(7,3)<=F(3))
        t=sp.symbols('t'); g=-6*t*t+7*t
        self.assertEqual([g.subs(t,s) for s in [0,1]],[0,1])
        self.assertEqual(sp.diff(g,t).subs(t,0),7)

    def test_Z11_Z12(self):
        self.assertEqual(F(6)*F(1,100)**2/6+F(2,1000000)/F(1,100),F(3,10000))
        self.assertEqual(F(1,800)+F(1,500),F(13,4000))

    def test_polynomial_symbolic_identity_T5(self):
        t,x,h=sp.symbols('t x h', nonzero=True)
        f=t**5
        c=lambda hh:sp.expand((f.subs(t,x+hh)-f.subs(t,x-hh))/(2*hh))
        r=sp.expand((4*c(h/2)-c(h))/3)
        self.assertEqual(sp.simplify(r-5*x**4),-h**4/4)

    def test_quintic_bound_T5(self):
        # dla t^5 dokładny błąd R wynosi h^4/4 <= 120*h^4/288=5h^4/12
        for h in [F(1,2),F(1,3)]:
            self.assertLessEqual(h**4/F(4),F(120)*h**4/F(288))


if __name__=='__main__':
    unittest.main()