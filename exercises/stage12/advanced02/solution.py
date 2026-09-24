"""
Requests + Threading -- ThreadPoolExecutor
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage12_advanced02.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage12/advanced02/ and import it as a submodule (e.g.
`from exercises.stage12.advanced02 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


import concurrent.futures
import requests


def fetch_all_concurrently(urls: list) -> list:
    """ThreadPoolExecutor(max_workers=4).map(lambda u: requests.get(u).json(), urls)."""
    raise NotImplementedError


def run_tasks_with_pool(funcs: list) -> list:
    """ThreadPoolExecutor().map(lambda f: f(), funcs)."""
    raise NotImplementedError


def compute_squares_concurrently(numbers: list) -> list:
    """ThreadPoolExecutor().map(lambda x: x ** 2, numbers)."""
    raise NotImplementedError
