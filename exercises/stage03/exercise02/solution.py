"""
Functions -- Args and Kwargs
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage03_exercise02.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage03/exercise02/ and import it as a submodule (e.g.
`from exercises.stage03.exercise02 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


def sum_all(*args: int) -> int:
    """Sum any number of positional int arguments."""
    raise NotImplementedError


def build_config(**kwargs) -> dict:
    """Return the keyword arguments as a plain dict."""
    raise NotImplementedError


def describe_call(*args, **kwargs) -> str:
    """f"args={args}, kwargs={kwargs}"."""
    raise NotImplementedError
