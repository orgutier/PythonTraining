"""
Functions -- Lambdas and Higher-Order Functions
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_week03_exercise03.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/week03/exercise03/ and import it as a submodule (e.g.
`from exercises.week03.exercise03 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


def make_multiplier(factor: int):
    """Return a one-arg callable that multiplies its input by factor (a lambda)."""
    raise NotImplementedError


def sort_by_length(words: list[str]) -> list[str]:
    """Words sorted shortest to longest, via sorted(..., key=lambda ...)."""
    raise NotImplementedError


def top_scorer(records: list[dict]) -> dict:
    """The record with the highest "score", via max(..., key=lambda ...)."""
    raise NotImplementedError
