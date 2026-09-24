"""
Requests + Threading -- Requests Basics
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage12_basic01.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage12/basic01/ and import it as a submodule (e.g.
`from exercises.stage12.basic01 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


import requests


def fetch_json(url: str) -> dict:
    """requests.get(url).json()."""
    raise NotImplementedError


def fetch_status_code(url: str) -> int:
    """requests.get(url).status_code."""
    raise NotImplementedError


def post_data(url: str, payload: dict) -> dict:
    """requests.post(url, json=payload).json()."""
    raise NotImplementedError
