"""Temperature class for working with Celsius, Fahrenheit, and Kelvin."""


class Temperature:
    """Represent a temperature value and its unit."""

    TOLERANCE = 1e-9
    VALID_UNITS = {"C", "F", "K"}

    def __init__(self, value: float, unit: str = "C") -> None:
        """Create a temperature with a value and unit."""
        self._value = float(value)
        self._unit = unit.upper()

    @property
    def value(self) -> float:
        """Return the temperature value."""
        return self._value

    @property
    def unit(self) -> str:
        """Return the temperature unit."""
        return self._unit