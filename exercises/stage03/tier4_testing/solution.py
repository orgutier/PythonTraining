"""
Functions -- Testing Without a Framework: Catch the Bug
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage03_tier4_testing.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage03/tier4_testing/ and import it as a submodule (e.g.
`from exercises.stage03.tier4_testing import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


def factorial_correct(n):
    if n <= 1:
        return 1
    return n * factorial_correct(n - 1)


def factorial_buggy(n):
    if n <= 1:
        return 1
    return n + factorial_buggy(n - 1)


def apply_discount_correct(price, pct=0.1):
    return round(price * (1 - pct), 2)


def apply_discount_buggy(price, pct=0.1):
    return round(price * (1 + pct), 2)


_check_log = []


def check(description: str, condition: bool) -> bool:
    """Append (description, condition) to _check_log; return condition. Must NEVER raise."""
    raise NotImplementedError


def run_all_checks() -> dict:
    """Call check() exactly 4 times (see README.md), then return {"total": ..., "passed": ..., "failed": [...]}."""
    raise NotImplementedError
