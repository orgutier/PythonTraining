"""
Functions -- Rate-Limited Logger Factory + Clamp
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage03_mid01.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage03/mid01/ and import it as a submodule (e.g.
`from exercises.stage03.mid01 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


def make_logger(*, prefix, max_entries=5):
    """Keyword-only prefix/max_entries. Return a log(message) closure over a capped entries list."""
    raise NotImplementedError


def clamp(value, lo, hi, /):
    """value/lo/hi positional-only. Clamp value into [lo, hi]."""
    raise NotImplementedError


def function_signature_info(fn) -> dict:
    """{"name": fn.__name__, "doc": fn.__doc__}."""
    raise NotImplementedError
