# INF201 Deliverable 4

Object-oriented Python implementation of `Temperature` and `Fraction` classes, including automated test suites and a Jupyter notebook presenting the results.

## Authors

- Filip Alan Jackowski
- Khalid Rashed

## Project contents

- `temperature.py` — implementation of the Temperature class
- `test_temperature.py` — pytest suite for Temperature
- `fraction.py` — implementation of the Fraction class
- `test_fraction.py` — pytest suite for Fraction
- `deliverable_4.ipynb` — executed project notebook
- `deliverable_4.pdf` — PDF export of the notebook
- `requirements.txt` — project dependencies
- `git_log.txt` — project commit history

## Features

### Temperature

- Celsius, Fahrenheit, and Kelvin support
- Case-insensitive units
- Absolute-zero validation
- Read-only properties
- Unit conversions
- String representations
- Cross-unit equality and ordering comparisons

### Fraction

- Automatic fraction reduction
- Strictly positive denominators
- Read-only properties
- Arithmetic operations
- String representations
- Equality and ordering comparisons

## Setup

Create and activate a virtual environment, then install the dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
