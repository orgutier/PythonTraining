"""
Requests + Threading -- Raising on HTTP Errors
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage12_mid01.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage12/mid01/ and import it as a submodule (e.g.
`from exercises.stage12.mid01 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


import requests


def fetch_with_raise(url: str) -> dict:
    """requests.get(url), then r.raise_for_status(), then r.json()."""
    raise NotImplementedError


def url_is_healthy(url: str) -> bool:
    """True if requests.get(url).raise_for_status() doesn't raise, else False."""
    raise NotImplementedError
