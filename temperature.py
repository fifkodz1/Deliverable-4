"""Temperature class for working with Celsius, Fahrenheit, and Kelvin."""


class Temperature:
    """Represent a temperature value and its unit."""

    TOLERANCE = 1e-9
    VALID_UNITS = {"C", "F", "K"}

    def __init__(self, value: float, unit: str = "C") -> None:
        """Create and validate a temperature value and unit."""
        if not isinstance(unit, str):
            raise ValueError("Temperature unit must be a string.")

        normalized_unit = unit.upper()

        if normalized_unit not in self.VALID_UNITS:
            raise ValueError("Unit must be 'C', 'F', or 'K'.")

        numeric_value = float(value)

        absolute_zero = {
            "C": -273.15,
            "F": -459.67,
            "K": 0.0,
        }

        if numeric_value < absolute_zero[normalized_unit]:
            raise ValueError("Temperature cannot be below absolute zero.")

        self._value = numeric_value
        self._unit = normalized_unit

    @property
    def value(self) -> float:
        """Return the temperature value."""
        return self._value

    @property
    def unit(self) -> str:
        """Return the temperature unit."""
        return self._unit

    def to_celsius(self) -> float:
        """Return the temperature converted to Celsius."""
        if self._unit == "C":
            return self._value
        if self._unit == "F":
            return (self._value - 32) * 5 / 9
        return self._value - 273.15

    def to_fahrenheit(self) -> float:
        """Return the temperature converted to Fahrenheit."""
        if self._unit == "F":
            return self._value
        if self._unit == "C":
            return self._value * 9 / 5 + 32
        return (self._value - 273.15) * 9 / 5 + 32

    def to_kelvin(self) -> float:
        """Return the temperature converted to Kelvin."""
        if self._unit == "K":
            return self._value
        if self._unit == "C":
            return self._value + 273.15
        return (self._value - 32) * 5 / 9 + 273.15  

    def convert_to(self, target_unit: str) -> "Temperature":
        """Return a new Temperature converted to the target unit."""
        if not isinstance(target_unit, str):
            raise ValueError("Target unit must be a string.")

        normalized_unit = target_unit.upper()

        if normalized_unit not in self.VALID_UNITS:
            raise ValueError("Target unit must be 'C', 'F', or 'K'.")

        if normalized_unit == "C":
            converted_value = self.to_celsius()
        elif normalized_unit == "F":
            converted_value = self.to_fahrenheit()
        else:
            converted_value = self.to_kelvin()

        return Temperature(converted_value, normalized_unit)

    def __repr__(self) -> str:
        """Return an unambiguous representation of the temperature."""
        return f"Temperature({self._value!r}, '{self._unit}')"

    def __str__(self) -> str:
        """Return a human-readable representation of the temperature."""
        return f"{self._value:.2f} °{self._unit}"

    def __eq__(self, other: object):
        """Return whether two temperatures are equal."""
        if not isinstance(other, Temperature):
            return NotImplemented

        difference = abs(self.to_celsius() - other.to_celsius())
        return difference <= self.TOLERANCE

    def __ne__(self, other: object):
        """Return whether two temperatures are different."""
        if not isinstance(other, Temperature):
            return NotImplemented

        return not self == other

    def __lt__(self, other: object):
        """Return whether this temperature is lower than another."""
        if not isinstance(other, Temperature):
            return NotImplemented

        return self.to_celsius() < other.to_celsius() - self.TOLERANCE

    def __le__(self, other: object):
        """Return whether this temperature is lower than or equal to another."""
        if not isinstance(other, Temperature):
            return NotImplemented

        return self.to_celsius() <= other.to_celsius() + self.TOLERANCE

    def __gt__(self, other: object):
        """Return whether this temperature is greater than another."""
        if not isinstance(other, Temperature):
            return NotImplemented

        return self.to_celsius() > other.to_celsius() + self.TOLERANCE

    def __ge__(self, other: object):
        """Return whether this temperature is greater than or equal to another."""
        if not isinstance(other, Temperature):
            return NotImplemented

        return self.to_celsius() >= other.to_celsius() - self.TOLERANCE