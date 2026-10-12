"""
OOP I -- Testing Without a Framework: Catch the Bug
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage06_tier4_testing.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage06/tier4_testing/ and import it as a submodule (e.g.
`from exercises.stage06.tier4_testing import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def fahrenheit(self):
        return self.celsius * 9 / 5 + 32


class TemperatureBuggy:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def fahrenheit(self):
        return self.celsius * 9 / 5


class Counter:
    def __init__(self, start=0):
        self.value = start

    @classmethod
    def from_string(cls, text):
        return cls(int(text))


class CounterBuggy:
    def __init__(self, start=0):
        self.value = start

    @classmethod
    def from_string(cls, text):
        return cls(text)


_check_log = []


def check(description: str, condition: bool) -> bool:
    """Append (description, condition) to _check_log; return condition. Must NEVER raise."""
    raise NotImplementedError


def run_all_checks() -> dict:
    """Call check() exactly 4 times (see README.md), then return {"total": ..., "passed": ..., "failed": [...]}."""
    raise NotImplementedError
