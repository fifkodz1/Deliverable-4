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