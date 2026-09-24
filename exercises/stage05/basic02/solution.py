"""
Files, Exceptions, Regex -- Support Ticket Intake
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage05_basic02.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage05/basic02/ and import it as a submodule (e.g.
`from exercises.stage05.basic02 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


import re


def extract_ticket_ids(text: str) -> list[str]:
    r"""re.findall(r"TICKET-\d+", text)."""
    raise NotImplementedError


def contains_urgent_flag(text: str) -> bool:
    r"""re.search(r"URGENT", text) is not None."""
    raise NotImplementedError


def clean_ticket_text(text: str) -> str:
    r"""re.sub(r"\s+", " ", text).strip()."""
    raise NotImplementedError


def looks_like_ticket_id(text: str) -> bool:
    r"""re.match(r"TICKET-\d+$", text) is not None -- the WHOLE text must be one ticket id."""
    raise NotImplementedError


def parse_priority(raw: str) -> int:
    """int(raw); on ValueError, raise a plain Exception with a clearer message."""
    raise NotImplementedError


_parse_attempts = 0


def parse_priority_with_default(raw: str, default: int = 0) -> int:
    """int(raw), or default on ValueError; always count the attempt in finally."""
    raise NotImplementedError


def get_parse_attempts() -> int:
    """Return _parse_attempts."""
    raise NotImplementedError
