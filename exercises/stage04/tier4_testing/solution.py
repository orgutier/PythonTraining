"""
Data Structures -- Testing Without a Framework: Catch the Bug
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage04_tier4_testing.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage04/tier4_testing/ and import it as a submodule (e.g.
`from exercises.stage04.tier4_testing import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


def dedupe_correct(items):
    return list(dict.fromkeys(items))


def dedupe_buggy(items):
    return list(set(items))


def evens_correct(numbers):
    return [n for n in numbers if n % 2 == 0]


def evens_buggy(numbers):
    return [n for n in numbers if n % 2 == 1]


_check_log = []


def check(description: str, condition: bool) -> bool:
    """Append (description, condition) to _check_log; return condition. Must NEVER raise."""
    raise NotImplementedError


def run_all_checks() -> dict:
    """Call check() exactly 4 times (see README.md), then return {"total": ..., "passed": ..., "failed": [...]}."""
    raise NotImplementedError
