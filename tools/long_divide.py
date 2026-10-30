"""F14.1: exact base-B Euclidean long division with checkable certificates.

No floating point operations. Not intended for constant-time cryptography.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Sequence


def _positive_int(value: int, name: str, minimum: int = 1) -> int:
    if type(value) is not int or value < minimum:
        raise ValueError(f"{name} must be an integer >= {minimum}")
    return value


@dataclass(frozen=True)
class DivisionCertificate:
    base: int
    divisor: int
    digits: tuple[int, ...]
    quotient_digits: tuple[int, ...]
    remainders: tuple[int, ...]  # includes r_0 = 0

    @property
    def quotient(self) -> int:
        value = 0
        for digit in self.quotient_digits:
            value = self.base * value + digit
        return value

    @property
    def remainder(self) -> int:
        return self.remainders[-1]

    @property
    def dividend(self) -> int:
        value = 0
        for digit in self.digits:
            value = self.base * value + digit
        return value

    def verify(self) -> bool:
        B, d = self.base, self.divisor
        if type(B) is not int or B < 2 or type(d) is not int or d < 1:
            return False
        if len(self.digits) != len(self.quotient_digits) or len(self.remainders) != len(self.digits) + 1:
            return False
        if self.remainders[0] != 0:
            return False
        for k, (x, q) in enumerate(zip(self.digits, self.quotient_digits)):
            old, new = self.remainders[k:k+2]
            if any(type(v) is not int for v in (x, q, old, new)):
                return False
            if not (0 <= x < B and 0 <= q < B and 0 <= old < d and 0 <= new < d):
                return False
            if B * old + x != d * q + new:
                return False
        return self.dividend == d * self.quotient + self.remainder


def divide_digits(digits: Sequence[int], base: int, divisor: int) -> DivisionCertificate:
    B = _positive_int(base, "base", 2)
    d = _positive_int(divisor, "divisor")
    input_digits = tuple(digits)
    for digit in input_digits:
        if type(digit) is not int or not 0 <= digit < B:
            raise ValueError("each digit must be an integer in [0, base)")
    r = 0
    quotients = []
    remainders = [0]
    for x in input_digits:
        q, r = divmod(B * r + x, d)
        quotients.append(q)
        remainders.append(r)
    certificate = DivisionCertificate(B, d, input_digits, tuple(quotients), tuple(remainders))
    assert certificate.verify()
    return certificate


def euclidean_signed(a: int, b: int) -> tuple[int, int]:
    if type(a) is not int or type(b) is not int or b == 0:
        raise ValueError("integer dividend and nonzero integer divisor required")
    d = abs(b)
    q0, r0 = divmod(abs(a), d)
    sigma = 1 if b > 0 else -1
    if a >= 0:
        return sigma * q0, r0
    if r0 == 0:
        return -sigma * q0, 0
    return -sigma * (q0 + 1), d - r0


def fractional_expansion(numerator: int, denominator: int, base: int = 10) -> tuple[tuple[int, ...], int, int]:
    """Return digits through first repeated remainder or termination, preperiod, period.

    period=0 denotes a terminating expansion; trailing zeros are omitted.
    """
    B = _positive_int(base, "base", 2)
    d = _positive_int(denominator, "denominator")
    if type(numerator) is not int or not 0 <= numerator < d:
        raise ValueError("numerator must be in [0, denominator)")
    r = numerator
    digits: list[int] = []
    seen: dict[int, int] = {}
    while r:
        if r in seen:
            return tuple(digits), seen[r], len(digits) - seen[r]
        seen[r] = len(digits)
        q, r = divmod(B * r, d)
        digits.append(q)
    return tuple(digits), len(digits), 0