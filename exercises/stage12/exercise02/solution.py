"""
Requests + Threading -- Sessions and Retry/Backoff
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage12_exercise02.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage12/exercise02/ and import it as a submodule (e.g.
`from exercises.stage12.exercise02 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


import time
import requests


def make_default_session():
    """requests.Session()."""
    raise NotImplementedError


def create_session_with_headers(headers: dict):
    """A requests.Session() with .headers.update(headers) applied."""
    raise NotImplementedError


def fetch_multiple_with_session(urls: list) -> list:
    """with requests.Session() as session: [session.get(u).json() for u in urls]."""
    raise NotImplementedError


def fetch_with_retry(url: str, max_attempts: int) -> dict:
    """Retry requests.get(url) up to max_attempts times with exponential backoff."""
    raise NotImplementedError
