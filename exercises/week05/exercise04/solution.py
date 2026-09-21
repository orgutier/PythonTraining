"""
Files, Exceptions, Regex -- Regex Basics
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_week05_exercise04.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/week05/exercise04/ and import it as a submodule (e.g.
`from exercises.week05.exercise04 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


import re

EMAIL_PATTERN = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")


def contains_digit(text: str) -> bool:
    """re.search(r"\d", text) is not None."""
    raise NotImplementedError


def find_all_numbers(text: str) -> list[str]:
    """re.findall(r"\d+", text)."""
    raise NotImplementedError


def starts_with_word(text: str, word: str) -> bool:
    """re.match(re.escape(word), text) is not None."""
    raise NotImplementedError


def normalize_whitespace(text: str) -> str:
    """re.sub(r"\s+", " ", text).strip()."""
    raise NotImplementedError


def extract_emails(text: str) -> list[str]:
    """EMAIL_PATTERN.findall(text)."""
    raise NotImplementedError
