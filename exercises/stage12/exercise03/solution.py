"""
Requests + Threading -- Threading Basics
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage12_exercise03.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage12/exercise03/ and import it as a submodule (e.g.
`from exercises.stage12.exercise03 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


import threading


def run_in_background(func, *args) -> threading.Thread:
    """threading.Thread(target=func, args=args), started, then returned."""
    raise NotImplementedError


def wait_for_all(threads: list) -> None:
    """t.join() for every thread in threads."""
    raise NotImplementedError


def run_and_wait(funcs: list) -> None:
    """Start every func as its own thread, THEN join all of them."""
    raise NotImplementedError
