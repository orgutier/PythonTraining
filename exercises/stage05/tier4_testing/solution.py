"""
Files, Exceptions, Regex -- Testing Without a Framework: Catch the Bug
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage05_tier4_testing.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage05/tier4_testing/ and import it as a submodule (e.g.
`from exercises.stage05.tier4_testing import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


import re


def safe_divide_correct(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None


def safe_divide_buggy(a, b):
    return a / b


def looks_like_email_correct(text):
    return re.match(r"^[\w.+-]+@[\w-]+\.[\w.-]+$", text) is not None


def looks_like_email_buggy(text):
    return re.match(r"[\w.+-]+@[\w-]+\.[\w.-]+", text) is not None


_check_log = []


def check(description: str, condition: bool) -> bool:
    """Append (description, condition) to _check_log; return condition. Must NEVER raise."""
    raise NotImplementedError


def run_all_checks() -> dict:
    """Call check() exactly 4 times (see README.md), then return {"total": ..., "passed": ..., "failed": [...]}."""
    raise NotImplementedError
