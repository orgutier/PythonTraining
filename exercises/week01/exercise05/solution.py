"""
Python Fundamentals -- CLI Interaction
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the aggregated test suite in
tests/test_week01.py imports directly from here. Need a helper function or
class of your own? Add another .py file next to this one inside
exercises/week01/exercise05/ and import it as a submodule (e.g.
`from exercises.week01.exercise05 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


def ask_name() -> str:
    """Prompt "What is your name? " and return the typed string."""
    raise NotImplementedError


def ask_age() -> int:
    """Prompt "How old are you? " and return the typed answer as an int."""
    raise NotImplementedError


def ask_yes_no(prompt: str) -> bool:
    """Prompt with `prompt`; True if the (lowercased, stripped) answer is "y" or "yes"."""
    raise NotImplementedError


def greet(name: str) -> None:
    """print(f"Hello, {name}!")."""
    raise NotImplementedError


def greeting_flow() -> str:
    """ask_name(), greet() it, then return the name."""
    raise NotImplementedError
