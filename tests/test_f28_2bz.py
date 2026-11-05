from fractions import Fraction as F

def H_two(t):
    return 2*t if t <= F(1,2) else F(1)

def H_uniform(t):
    return t-t*t/2

def slope(f,s,t):
    return (f(t)-f(s))/(t-s)

def test_piecewise():
    for i in range(1,20):
        t=F(i,40); h=F(1,80)
        assert slope(H_two,t,t+h) <= slope(H_two,t-h,t)
    assert slope(H_two,F(39,80),F(1,2)) == 2
    assert slope(H_two,F(1,2),F(41,80)) == 0

def test_uniform():
    for i in range(1,99):
        t=F(i,100); h=F(1,200)
        assert slope(H_uniform,t,t+h)==1-t-h/2
        assert slope(H_uniform,t-h,t)==1-t+h/2
        assert slope(H_uniform,t,t+h)<=1-t<=slope(H_uniform,t-h,t)

def test_noise():
    eps=F(1,100)
    for i in range(2,98):
        t=F(i,100); h=F(1,100)
        e1,e2,e3=eps,-eps,eps
        lo=((H_uniform(t+h)+e3)-(H_uniform(t)+e2))/h-2*eps/h
        hi=((H_uniform(t)+e2)-(H_uniform(t-h)+e1))/h+2*eps/h
        assert lo <= 1-t <= hi

if __name__ == "__main__":
    test_piecewise();test_uniform();test_noise()
    print("PASS: 411 exact rational assertions")
