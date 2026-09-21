"""
Challenge 24 - Bounded Job Queue with Retry and ThreadPoolExecutor
Interview-style challenge. Correctness is pytest-tested (see
tests/test_challenge24.py / `python tools/cli.py test challenge24`); see
README.md in this folder for the full problem statement and the constraints
your solution must follow (requests.post()/response.raise_for_status() with a manual retry/backoff loop, concurrent.futures.ThreadPoolExecutor, and a threading.Lock-protected counter proving exact correctness under real concurrency).

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module, matching the convention used by
exercises/weekNN/solution.py.
"""


import time
import threading
import concurrent.futures
import requests


class RetryingJobSubmitter:
    def __init__(self, session, max_attempts: int = 3) -> None:
        raise NotImplementedError

    def submit_job(self, url: str, payload: dict) -> dict:
        """post + raise_for_status + json, retried with exponential backoff up to max_attempts."""
        raise NotImplementedError


class SafeCounter:
    def __init__(self) -> None:
        raise NotImplementedError

    def increment(self) -> None:
        """Thread-safe += 1."""
        raise NotImplementedError

    @property
    def value(self) -> int:
        raise NotImplementedError


def submit_all_with_pool(submitter: RetryingJobSubmitter, jobs: list, max_workers: int = 4) -> list:
    """ThreadPoolExecutor(max_workers).map over jobs; results in order."""
    raise NotImplementedError


def submit_all_and_count_successes(submitter: RetryingJobSubmitter, jobs: list, counter: SafeCounter, max_workers: int = 4) -> list:
    """Like submit_all_with_pool, but counter.increment() once per success."""
    raise NotImplementedError
