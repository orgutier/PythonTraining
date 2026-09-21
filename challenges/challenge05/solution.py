"""
Challenge 05 - Pluggable Event Pipeline
Interview-style challenge. Correctness is pytest-tested (see
tests/test_challenge05.py / `python tools/cli.py test challenge05`); see
README.md in this folder for the full problem statement and the constraints
your solution must follow (a closure-based registry, functools.wraps on every decorator, hand-rolled memoization (not lru_cache), and functools.lru_cache with a keyword-only parameter).

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module, matching the convention used by
exercises/weekNN/solution.py.
"""


import functools


def make_pipeline():
    """Return (register, run) -- see README for the exact contract."""
    raise NotImplementedError


def count_calls(func):
    """Decorator: wrapper.call_count tracks calls, via a closure + nonlocal. Use functools.wraps(func)."""
    raise NotImplementedError


def memoize(func):
    """Decorator: hand-rolled memoization keyed on (args, sorted kwargs). Use functools.wraps(func)."""
    raise NotImplementedError


def cached_expensive(n: int, *, precision: int = 2) -> float:
    """round(n ** 0.5, precision), decorated with functools.lru_cache(maxsize=None). precision is keyword-only."""
    raise NotImplementedError
