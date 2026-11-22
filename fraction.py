"""Fraction class for representing and calculating fractions."""

from math import gcd


class Fraction:
    """Represent a reduced fraction with a positive denominator."""

    def __init__(self, numerator: int, denominator: int) -> None:
        """Create and reduce a fraction."""
        if type(numerator) is not int or type(denominator) is not int:
            raise TypeError("Numerator and denominator must be integers.")
        if denominator <= 0:
            raise ValueError("Denominator must be strictly positive.")

        common_divisor = gcd(numerator, denominator)
        self._numerator = numerator // common_divisor
        self._denominator = denominator // common_divisor

    @property
    def numerator(self) -> int:
        """Return the numerator."""
        return self._numerator

    @property
    def denominator(self) -> int:
        """Return the denominator."""
        return self._denominator

    def __repr__(self) -> str:
        return f"Fraction({self._numerator}, {self._denominator})"

    def __str__(self) -> str:
        return f"{self._numerator}/{self._denominator}"

    def __float__(self) -> float:
        return self._numerator / self._denominator

    def __neg__(self) -> "Fraction":
        return Fraction(-self._numerator, self._denominator)

    def __add__(self, other: object):
        if not isinstance(other, Fraction):
            return NotImplemented
        numerator = (
            self._numerator * other._denominator
            + other._numerator * self._denominator
        )
        return Fraction(numerator, self._denominator * other._denominator)

    def __sub__(self, other: object):
        if not isinstance(other, Fraction):
            return NotImplemented
        numerator = (
            self._numerator * other._denominator
            - other._numerator * self._denominator
        )
        return Fraction(numerator, self._denominator * other._denominator)

    def __mul__(self, other: object):
        if not isinstance(other, Fraction):
            return NotImplemented
        return Fraction(
            self._numerator * other._numerator,
            self._denominator * other._denominator,
        )

    def __truediv__(self, other: object):
        if not isinstance(other, Fraction):
            return NotImplemented
        if other._numerator == 0:
            raise ZeroDivisionError("Cannot divide by a zero fraction.")

        numerator = self._numerator * other._denominator
        denominator = self._denominator * other._numerator
        if denominator < 0:
            numerator = -numerator
            denominator = -denominator
        return Fraction(numerator, denominator)

    def __eq__(self, other: object):
        if not isinstance(other, Fraction):
            return NotImplemented
        return (
            self._numerator == other._numerator
            and self._denominator == other._denominator
        )

    def __ne__(self, other: object):
        if not isinstance(other, Fraction):
            return NotImplemented
        return not self == other

    def __lt__(self, other: object):
        if not isinstance(other, Fraction):
            return NotImplemented
        return (
            self._numerator * other._denominator
            < other._numerator * self._denominator
        )

    def __le__(self, other: object):
        if not isinstance(other, Fraction):
            return NotImplemented
        return (
            self._numerator * other._denominator
            <= other._numerator * self._denominator
        )

    def __gt__(self, other: object):
        if not isinstance(other, Fraction):
            return NotImplemented
        return (
            self._numerator * other._denominator
            > other._numerator * self._denominator
        )

    def __ge__(self, other: object):
        if not isinstance(other, Fraction):
            return NotImplemented
        return (
            self._numerator * other._denominator
            >= other._numerator * self._denominator
        )
