"""
Python Fundamentals -- Temperature and BMI
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage01_exercise02.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage01/exercise02/ and import it as a submodule (e.g.
`from exercises.stage01.exercise02 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert a Celsius temperature to Fahrenheit."""
    raise NotImplementedError


def bmi_calculator(weight_kg: float, height_m: float) -> float:
    """Return BMI = weight_kg / height_m ** 2, rounded to 2 decimals."""
    raise NotImplementedError


def validate_measurement(value) -> bool:
    """True if value is an int or float, but explicitly NOT a bool."""
    raise NotImplementedError
