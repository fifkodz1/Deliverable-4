"""Tests for the Temperature class."""

import pytest

from temperature import Temperature


def test_default_unit() -> None:
    temperature = Temperature(25)

    assert temperature.value == 25.0
    assert temperature.unit == "C"


@pytest.mark.parametrize("unit", ["c", "f", "k", "C", "F", "K"])
def test_units_are_case_insensitive(unit: str) -> None:
    temperature = Temperature(25, unit)

    assert temperature.unit == unit.upper()


def test_value_and_unit_are_read_only() -> None:
    temperature = Temperature(25, "C")

    with pytest.raises(AttributeError):
        temperature.value = 30

    with pytest.raises(AttributeError):
        temperature.unit = "F"


@pytest.mark.parametrize("invalid_unit", ["X", "Celsius", "", "CF"])
def test_invalid_units_raise_value_error(invalid_unit: str) -> None:
    with pytest.raises(ValueError):
        Temperature(25, invalid_unit)


@pytest.mark.parametrize(
    ("value", "unit"),
    [
        (-273.1500001, "C"),
        (-459.6700001, "F"),
        (-0.0000001, "K"),
    ],
)
def test_temperature_below_absolute_zero_raises_value_error(
    value: float,
    unit: str,
) -> None:
    with pytest.raises(ValueError):
        Temperature(value, unit)


@pytest.mark.parametrize(
    ("celsius", "fahrenheit", "kelvin"),
    [
        (-273.15, -459.67, 0.0),
        (-40.0, -40.0, 233.15),
        (0.0, 32.0, 273.15),
        (37.0, 98.6, 310.15),
        (100.0, 212.0, 373.15),
    ],
)
def test_reference_point_conversions(
    celsius: float,
    fahrenheit: float,
    kelvin: float,
) -> None:
    from_celsius = Temperature(celsius, "C")
    from_fahrenheit = Temperature(fahrenheit, "F")
    from_kelvin = Temperature(kelvin, "K")

    assert from_celsius.to_fahrenheit() == pytest.approx(
        fahrenheit,
        rel=0.0,
        abs=1e-9,
    )
    assert from_celsius.to_kelvin() == pytest.approx(
        kelvin,
        rel=0.0,
        abs=1e-9,
    )

    assert from_fahrenheit.to_celsius() == pytest.approx(
        celsius,
        rel=0.0,
        abs=1e-9,
    )
    assert from_fahrenheit.to_kelvin() == pytest.approx(
        kelvin,
        rel=0.0,
        abs=1e-9,
    )

    assert from_kelvin.to_celsius() == pytest.approx(
        celsius,
        rel=0.0,
        abs=1e-9,
    )
    assert from_kelvin.to_fahrenheit() == pytest.approx(
        fahrenheit,
        rel=0.0,
        abs=1e-9,
    )


def test_convert_to_returns_new_temperature() -> None:
    original = Temperature(0, "C")
    converted = original.convert_to("f")

    assert converted == Temperature(32, "F")
    assert converted.unit == "F"
    assert converted is not original


@pytest.mark.parametrize("invalid_unit", ["X", "Celsius", ""])
def test_convert_to_rejects_invalid_units(invalid_unit: str) -> None:
    temperature = Temperature(25, "C")

    with pytest.raises(ValueError):
        temperature.convert_to(invalid_unit)


def test_round_trip_conversion() -> None:
    original = Temperature(37, "C")

    result = (
        original.convert_to("F")
        .convert_to("K")
        .convert_to("C")
    )

    assert result == original
    assert result.unit == "C"


def test_cross_unit_equality_and_inequality() -> None:
    assert Temperature(0, "C") == Temperature(32, "F")
    assert Temperature(0, "C") == Temperature(273.15, "K")
    assert Temperature(0, "C") != Temperature(100, "C")


def test_cross_unit_ordering() -> None:
    cold = Temperature(0, "C")
    hot = Temperature(212, "F")
    hot_kelvin = Temperature(373.15, "K")

    assert cold < hot
    assert cold <= hot
    assert hot > cold
    assert hot >= cold
    assert hot <= hot_kelvin
    assert hot >= hot_kelvin


def test_comparisons_with_other_types_return_not_implemented() -> None:
    temperature = Temperature(25, "C")

    assert temperature.__eq__(25) is NotImplemented
    assert temperature.__ne__(25) is NotImplemented
    assert temperature.__lt__(25) is NotImplemented
    assert temperature.__le__(25) is NotImplemented
    assert temperature.__gt__(25) is NotImplemented
    assert temperature.__ge__(25) is NotImplemented


def test_string_formatting() -> None:
    temperature = Temperature(25, "C")

    assert str(temperature) == "25.00 °C"
    assert repr(temperature) == "Temperature(25.0, 'C')"