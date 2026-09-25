"""
OOP II -- Testing Without a Framework: Catch the Bug
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage07_tier4_testing.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage07/tier4_testing/ and import it as a submodule (e.g.
`from exercises.stage07.tier4_testing import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


class Shape:
    def area(self):
        raise NotImplementedError


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


class SquareBuggy(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * 2


class Duck:
    def quack(self):
        return "Quack!"


def make_it_quack_correct(obj):
    return obj.quack()


def make_it_quack_buggy(obj):
    return obj.quack


_check_log = []


def check(description: str, condition: bool) -> bool:
    """Append (description, condition) to _check_log; return condition. Must NEVER raise."""
    raise NotImplementedError


def run_all_checks() -> dict:
    """Call check() exactly 4 times (see README.md), then return {"total": ..., "passed": ..., "failed": [...]}."""
    raise NotImplementedError
