"""
Python Fundamentals -- Boolean Logic
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage01_exercise04.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage01/exercise04/ and import it as a submodule (e.g.
`from exercises.stage01.exercise04 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


def can_enter_venue(age, has_ticket: bool, is_vip: bool) -> bool:
    """True if age is known and >= 18, and (has_ticket or is_vip)."""
    raise NotImplementedError


def access_level(has_ticket: bool, is_vip: bool, is_staff: bool) -> str:
    """"backstage" if staff/vip, else "general" if has_ticket, else "denied"."""
    raise NotImplementedError


def is_valid_choice(choice, allowed: list[str]) -> bool:
    """True if choice is a non-empty str that appears in allowed."""
    raise NotImplementedError


def toggle_flag(flag: bool) -> bool:
    """Opposite of flag -- implement with `if flag is True: ... else: ...`, not `not`."""
    raise NotImplementedError
