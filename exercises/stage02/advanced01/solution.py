"""
Control Flow -- Custom Iterator: CountdownTimer
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage02_advanced01.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage02/advanced01/ and import it as a submodule (e.g.
`from exercises.stage02.advanced01 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


class CountdownTimer:
    """Counts down from `start` to 0 inclusive; is its own iterator."""

    def __init__(self, start):
        raise NotImplementedError

    def __iter__(self):
        raise NotImplementedError

    def __next__(self):
        raise NotImplementedError
