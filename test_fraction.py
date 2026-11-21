"""Tests for the Fraction class."""

import pytest

from fraction import Fraction


def test_initialization() -> None:
    fraction = Fraction(3, 4)
    assert fraction.numerator == 3
    assert fraction.denominator == 4


def test_fraction_is_reduced() -> None:
    assert Fraction(8, 12) == Fraction(2, 3)


def test_negative_and_zero_numerator() -> None:
    assert Fraction(-6, 8) == Fraction(-3, 4)
    assert Fraction(0, 5) == Fraction(0, 1)


@pytest.mark.parametrize(
    ("numerator", "denominator"),
    [(1.5, 2), (1, 2.5), ("1", 2), (1, "2"), (True, 2)],
)
def test_non_integer_values_raise_type_error(
    numerator: object, denominator: object
) -> None:
    with pytest.raises(TypeError):
        Fraction(numerator, denominator)


@pytest.mark.parametrize("denominator", [0, -1, -10])
def test_non_positive_denominator_raises_value_error(denominator: int) -> None:
    with pytest.raises(ValueError):
        Fraction(1, denominator)


def test_read_only_properties() -> None:
    fraction = Fraction(1, 2)
    with pytest.raises(AttributeError):
        fraction.numerator = 3
    with pytest.raises(AttributeError):
        fraction.denominator = 4


def test_arithmetic() -> None:
    first = Fraction(1, 2)
    second = Fraction(1, 3)
    assert first + second == Fraction(5, 6)
    assert first - second == Fraction(1, 6)
    assert first * second == Fraction(1, 6)
    assert first / second == Fraction(3, 2)


def test_division_by_negative_fraction() -> None:
    result = Fraction(1, 2) / Fraction(-3, 4)
    assert result == Fraction(-2, 3)
    assert result.denominator > 0


def test_division_by_zero_fraction_raises_error() -> None:
    with pytest.raises(ZeroDivisionError):
        Fraction(1, 2) / Fraction(0, 1)


def test_all_comparisons() -> None:
    small = Fraction(1, 4)
    middle = Fraction(1, 2)
    equivalent = Fraction(2, 4)
    large = Fraction(3, 4)
    assert middle == equivalent
    assert middle != large
    assert small < middle
    assert small <= middle
    assert middle <= equivalent
    assert large > middle
    assert large >= middle
    assert middle >= equivalent


def test_other_types_return_not_implemented() -> None:
    fraction = Fraction(1, 2)
    for method in (
        fraction.__eq__,
        fraction.__ne__,
        fraction.__lt__,
        fraction.__le__,
        fraction.__gt__,
        fraction.__ge__,
        fraction.__add__,
        fraction.__sub__,
        fraction.__mul__,
        fraction.__truediv__,
    ):
        assert method(1) is NotImplemented


def test_additional_special_methods() -> None:
    fraction = Fraction(2, 3)
    assert -fraction == Fraction(-2, 3)
    assert float(Fraction(1, 4)) == 0.25
    assert str(fraction) == "2/3"
    assert repr(fraction) == "Fraction(2, 3)"
