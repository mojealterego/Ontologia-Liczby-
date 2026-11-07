from fractions import Fraction as F

def phi(a,k,j):
    p=F(1)
    for i in range(j,k):
        p*=a[i]
    return p

def run():
    checks=0
    for n in range(1,9):
        for r in (F(0),F(1,2),F(2,3),F(1)):
            a=[r]*n
            for z0 in (F(-3),F(0),F(5)):
                for pattern in (0,1,2):
                    v=[F((i%3)-1,i+2) if pattern==0 else (F(1,i+2) if pattern==1 else F(0)) for i in range(n)]
                    z=z0
                    for k in range(1,n+1):
                        z=a[k-1]*z+v[k-1]
                        formula=phi(a,k,0)*z0+sum((phi(a,k,j+1)*v[j] for j in range(k)),F(0))
                        assert z==formula
                        checks+=1
    for k in range(1,40):
        a=[F(i+1,i+2) for i in range(k)]
        assert phi(a,k,0)==F(1,k+1);checks+=1
        assert sum((phi(a,k,j+1) for j in range(k)),F(0))==F(k*(k+3),2*(k+1));checks+=1
        assert sum((F(1,2)**(k-1-j)*F(1,3)**j for j in range(k)),F(0))==6*(F(1,2)**k-F(1,3)**k);checks+=1
    print("PASS",checks,"exact rational assertions")

if __name__=="__main__":
    run()
