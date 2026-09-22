"""
Functions -- Functools Toolbox
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage03_exercise06.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage03/exercise06/ and import it as a submodule (e.g.
`from exercises.stage03.exercise06 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


import functools


def cached_fibonacci(n: int) -> int:
    """Recursive Fibonacci, decorated with functools.lru_cache(maxsize=None)."""
    raise NotImplementedError


def cached_is_prime(n: int) -> bool:
    """Primality check, decorated with functools.lru_cache(maxsize=None)."""
    raise NotImplementedError


def cached_factorial(n: int) -> int:
    """Recursive factorial, decorated with functools.lru_cache(maxsize=None)."""
    raise NotImplementedError


def add(a: int, b: int) -> int:
    raise NotImplementedError


def multiply(a: int, b: int) -> int:
    raise NotImplementedError


def format_currency(amount: float, symbol: str) -> str:
    """f"{symbol}{amount:.2f}"."""
    raise NotImplementedError


def make_adder(n: int):
    """functools.partial(add, n)."""
    raise NotImplementedError


def make_multiplier_via_partial(n: int):
    """functools.partial(multiply, n)."""
    raise NotImplementedError


def make_usd_formatter():
    """functools.partial(format_currency, symbol="$")."""
    raise NotImplementedError
