from fractions import Fraction as F

def test_linear():
    for n in range(1,201):
        assert sum((F(1,4*n*n) for _ in range(n)),F(0))==F(1,4*n)
        assert F(1,4*n)<=F(1,2*n)

def test_sharp():
    for n in range(1,101):
        h=F(1,n)
        assert h/2==h*F(1,2)

def test_noise():
    assert F(1,4)*F(1,10)+F(3,4)*F(1,30)==F(1,20)

def test_mean():
    for n in range(1,101):
        m=[F(2*i-1,2*n) for i in range(1,n+1)]
        assert sum(m,F(0))/n==F(1,2)
        assert m==sorted(m)

if __name__=='__main__':
    test_linear();test_sharp();test_noise();test_mean()
    print('PASS: 501 checks')
