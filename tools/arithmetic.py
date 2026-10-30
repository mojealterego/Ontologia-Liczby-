"""Deterministic arithmetic reference implementations for F12.2/F12.3.

Inputs are mathematical integers; every public function validates its contract.
A subtraction trace records the prefix invariant, not a proof of its universality.
"""
from __future__ import annotations

from math import gcd


def base_digits(number: int, base: int, width: int | None = None) -> list[int]:
    """Little-endian, unsigned representation. Optional exact width pads with zeros."""
    if isinstance(number, bool) or not isinstance(number,int) or number<0:
        raise ValueError('number must be a nonnegative integer')
    if isinstance(base,bool) or not isinstance(base,int) or base<2:
        raise ValueError('base must be an integer >= 2')
    if width is not None and (isinstance(width,bool) or not isinstance(width,int) or width<1):
        raise ValueError('width must be an integer >= 1')
    digits=[]
    n=number
    while n:
        n,r=divmod(n,base)
        digits.append(r)
    if not digits: digits=[0]
    if width is not None:
        if len(digits)>width: raise ValueError('number does not fit in width')
        digits.extend([0]*(width-len(digits)))
    return digits


def digits_value(digits: list[int], base: int) -> int:
    if isinstance(base,bool) or not isinstance(base,int) or base<2: raise ValueError('base >= 2 required')
    if not digits: raise ValueError('at least one digit required')
    if any(isinstance(d,bool) or not isinstance(d,int) or d<0 or d>=base for d in digits):
        raise ValueError('each digit must lie in [0, base)')
    return sum(d*(base**i) for i,d in enumerate(digits))


def borrow_subtract(a_digits: list[int], b_digits: list[int], base: int):
    """Unsigned column subtraction modulo base**width.

    Returns (digits_little_endian, final_borrow, trace); exact relation is
    A-B = value(digits)-final_borrow*base**width.
    """
    digits_value(a_digits,base)
    digits_value(b_digits,base)
    if len(a_digits)!=len(b_digits): raise ValueError('operand widths must match')
    borrow=0
    out=[]
    trace=[]
    for i,(a,b) in enumerate(zip(a_digits,b_digits)):
        difference=a-b-borrow
        next_borrow=int(difference<0)
        digit=difference+base*next_borrow
        assert 0<=digit<base
        out.append(digit)
        trace.append({'position':i,'borrow_in':borrow,'borrow_out':next_borrow,'digit':digit})
        borrow=next_borrow
    return out,borrow,trace


def signed_from_twos(raw: int, bits: int) -> int:
    if isinstance(bits,bool) or not isinstance(bits,int) or bits<2:raise ValueError('bits >= 2 required')
    if isinstance(raw,bool) or not isinstance(raw,int) or not 0<=raw<1<<bits:
        raise ValueError('raw must fit unsigned word')
    return raw if raw < 1<<(bits-1) else raw-(1<<bits)


def signed_overflow_subtract(a: int,b: int,bits: int) -> tuple[int,bool]:
    if isinstance(bits,bool) or not isinstance(bits,int) or bits<2:raise ValueError('bits >= 2 required')
    lower,upper=-(1<<(bits-1)),(1<<(bits-1))-1
    if any(isinstance(x,bool) or not isinstance(x,int) or x<lower or x>upper for x in (a,b)):
        raise ValueError('signed input does not fit word')
    raw=(a-b)%(1<<bits)
    value=signed_from_twos(raw,bits)
    overflow=(a<0)!=(b<0) and (value<0)!=(a<0)
    return value,overflow


def solve_congruence(a: int,b: int,m: int)->list[int]:
    """All residue representatives x in [0,m) satisfying a*x == b (mod m)."""
    if any(isinstance(x,bool) or not isinstance(x,int) for x in (a,b,m)) or m<1:
        raise ValueError('a,b integers and m positive integer required')
    d=gcd(a,m)
    if b%d: return []
    reduced_mod=m//d
    # When reduced_mod is 1, all x modulo m solve the equation.
    first=0 if reduced_mod==1 else (pow((a//d)%reduced_mod,-1,reduced_mod)*(b//d))%reduced_mod
    return sorted(first+j*reduced_mod for j in range(d))


def solve_integer_linear(a: int,b: int,c: int) -> int|None:
    """Solve a*x+b=c in Z; a=0 has zero or infinitely many solutions."""
    if any(isinstance(v,bool) or not isinstance(v,int) for v in (a,b,c)):
        raise ValueError('integer inputs required')
    if a==0:raise ValueError('a=0: either no solution or infinitely many; no unique x')
    delta=c-b
    return delta//a if delta%a==0 else None


def complement_subtract(a: int,b: int,base: int,width: int)->tuple[int,int]:
    """Base complement subtraction. Return (low_digits_as_number, final_carry)."""
    if isinstance(base,bool) or not isinstance(base,int) or base<2:raise ValueError('base >= 2')
    if isinstance(width,bool) or not isinstance(width,int) or width<1:raise ValueError('width >= 1')
    limit=base**width
    if any(isinstance(v,bool) or not isinstance(v,int) or not 0<=v<limit for v in (a,b)):
        raise ValueError('operands must fit unsigned width')
    full=a+(limit-1-b)+1
    return full%limit,int(full>=limit)


def solve_diophantine(a: int,b: int,c: int)->tuple[int,int,int,int]|None:
    """Find particular integer solution and full parametrization ax+by=c.

    The returned tuple (x0,y0,dx,dy) denotes x=x0+t*dx, y=y0+t*dy.
    """
    if any(isinstance(v,bool) or not isinstance(v,int) for v in (a,b,c)):
        raise ValueError('integer inputs required')
    if a==0 and b==0:raise ValueError('degenerate 0*x+0*y=c needs separate treatment')
    d=gcd(a,b)
    if c%d:return None
    old_r,r=abs(a),abs(b)
    old_s,s=1,0
    old_t,t=0,1
    while r:
        q=old_r//r
        old_r,r=r,old_r-q*r
        old_s,s=s,old_s-q*s
        old_t,t=t,old_t-q*t
    assert old_r==d
    multiplier=c//d
    x=old_s*(1 if a>=0 else -1)*multiplier
    y=old_t*(1 if b>=0 else -1)*multiplier
    assert a*x+b*y==c
    return x,y,b//d,-a//d