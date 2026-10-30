"""Referencyjna, dokładna arytmetyka mnożenia pisemnego F13.3.

Przeznaczenie: odtwarzalny dowód lokalnych inwariantów, nie produkcyjny
silnik kryptograficzny. Implementacja nie jest stałoczasowa.
"""
from __future__ import annotations

from dataclasses import dataclass


def _base(base: int) -> int:
    if type(base) is not int:
        raise TypeError("Podstawa musi być liczbą całkowitą")
    if base < 2:
        raise ValueError("Podstawa musi być >= 2")
    return base


def _nat(value: int) -> int:
    if type(value) is not int:
        raise TypeError("Operand musi być liczbą całkowitą")
    if value < 0:
        raise ValueError("Operand musi być nieujemny")
    return value


def digits_lsb(value: int, base: int) -> tuple[int, ...]:
    """Cyfry od najmniej znaczącej; zero reprezentowane jedną cyfrą."""
    _nat(value)
    _base(base)
    if value == 0:
        return (0,)
    result: list[int] = []
    while value:
        value, digit = divmod(value, base)
        result.append(digit)
    return tuple(result)


@dataclass(frozen=True)
class ProductTrace:
    """Znormalizowane cyfry, surowy splot i przeniesienia c_0..c_m."""
    base: int
    digits: tuple[int, ...]
    coefficients: tuple[int, ...]
    carries: tuple[int, ...]

    def reconstructed(self) -> int:
        return sum(digit * self.base**i for i, digit in enumerate(self.digits))

    @property
    def value(self) -> int:
        return self.reconstructed()


def schoolbook_product(x: int, y: int, base: int = 10) -> ProductTrace:
    """Klasyczny splot cyfr z normalizacją dodatnich przeniesień.

    Złożoność O(mn) iloczynów cyfr, O(m+n) dodatkowej pamięci.
    """
    _nat(x)
    _nat(y)
    _base(base)
    a = digits_lsb(x, base)
    b = digits_lsb(y, base)
    raw = [0] * (len(a) + len(b))
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            raw[i + j] += ai * bj
    digits: list[int] = []
    carries: list[int] = [0]
    carry = 0
    for coefficient in raw:
        carry, digit = divmod(coefficient + carry, base)
        digits.append(digit)
        carries.append(carry)
    if carry != 0:
        raise ArithmeticError("Błąd niezmiennika końcowego przeniesienia")
    while len(digits) > 1 and digits[-1] == 0:
        digits.pop()
        raw.pop()
        carries.pop()
    return ProductTrace(base=base,digits=tuple(digits),coefficients=tuple(raw),carries=tuple(carries))


def signed_product(x: int, y: int, base: int = 10) -> int:
    if type(x) is not int or type(y) is not int:
        raise TypeError("Operand musi być liczbą całkowitą")
    sign = -1 if (x < 0) != (y < 0) else 1
    return sign * schoolbook_product(abs(x), abs(y), base).value


def fixed_word_product(x: int, y: int, base: int, width: int) -> tuple[int, bool]:
    """Iloczyn w rejestrze bez znaku o szerokości width cyfr; (reszta, overflow)."""
    _nat(x)
    _nat(y)
    _base(base)
    if type(width) is not int:
        raise TypeError("width musi być liczbą całkowitą")
    if width < 1:
        raise ValueError("width musi być >=1")
    modulus = base ** width
    if x >= modulus or y >= modulus:
        raise ValueError("Operand nie mieści się w słowie")
    prod = schoolbook_product(x,y,base).value
    return prod % modulus, prod >= modulus
