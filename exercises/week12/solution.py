"""
Week 12 - Requests + Threading
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in tests/test_week12.py
imports directly from here.
"""


import threading
import requests


class APIError(Exception):
    """Raised when the API responds with a non-200 status code."""


def fetch_user_name(user_id: int) -> str:
    raise NotImplementedError


def fetch_many(user_ids: list[int]) -> dict[int, str]:
    """Fetch multiple user names concurrently using threading."""
    raise NotImplementedError
