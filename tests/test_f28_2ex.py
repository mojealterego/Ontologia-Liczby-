from fractions import Fraction as F
from itertools import product

def between(ws, xs):
    W=sum(ws); mu=sum(w*x for w,x in zip(ws,xs))/W
    return sum(w*(x-mu)**2 for w,x in zip(ws,xs))

def verify():
    count=0
    for n in range(2,5):
        for ww in product((1,2),repeat=n):
            ws=tuple(map(F,ww))
            for xx in product((-2,0,1,3),repeat=n):
                xs=tuple(map(F,xx)); W=sum(ws); a=min(xs); b=max(xs)
                mu=sum(w*x for w,x in zip(ws,xs))/W
                H=between(ws,xs)
                assert H == sum(ws[i]*ws[j]*(xs[i]-xs[j])**2 for i in range(n) for j in range(i+1,n))/W
                assert H <= W*(b-a)**2/4
                assert H <= W*(b-mu)*(mu-a)
                assert W*(b-mu)*(mu-a)-H == sum(w*(x-a)*(b-x) for w,x in zip(ws,xs))
                assert (H==W*(b-mu)*(mu-a)) == all(x==a or x==b for x in xs)
                count+=5
    return count
if __name__=='__main__': print('PASS',verify())
