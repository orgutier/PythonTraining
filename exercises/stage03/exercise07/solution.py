"""
Functions -- Signature Styles
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage03_exercise07.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage03/exercise07/ and import it as a submodule (e.g.
`from exercises.stage03.exercise07 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


def compute_area(length, width, *, unit="m") -> str:
    """f"{length*width}{unit}^2" -- unit is keyword-only."""
    raise NotImplementedError


def divide(a, b, /, *, precision=2) -> float:
    """round(a / b, precision) -- a, b positional-only; precision keyword-only."""
    raise NotImplementedError


def connect(host, port, /, *, timeout=30, retries=3) -> dict:
    """{"host":..., "port":..., "timeout":..., "retries":...} -- host/port positional-only, timeout/retries keyword-only."""
    raise NotImplementedError


def scale_point(x, y, /, factor=1.0) -> tuple:
    """(x*factor, y*factor) -- x, y positional-only; factor is a normal parameter."""
    raise NotImplementedError
