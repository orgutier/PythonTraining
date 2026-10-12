"""
Challenge 23 - Rate-Limited HTTP Client
Interview-style challenge. Correctness is pytest-tested (see
tests/test_challenge23.py / `python tools/cli.py test challenge23`); see
README.md in this folder for the full problem statement and the constraints
your solution must follow (threading.Lock protecting a token bucket, requests.Session()/raise_for_status()/response.json(), and raw threading.Thread/.start()/.join() for concurrent fetches).

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module, matching the convention used by
exercises/stageNN/solution.py.
"""


import time
import threading
import requests


class TokenBucketLimiter:
    def __init__(self, capacity: int, refill_rate: float) -> None:
        raise NotImplementedError

    def allow_request(self) -> bool:
        """Thread-safe token consumption with continuous refill. See README."""
        raise NotImplementedError


class RateLimitedClient:
    def __init__(self, session, limiter: TokenBucketLimiter) -> None:
        raise NotImplementedError

    def get_json(self, url: str) -> dict:
        """Poll limiter.allow_request() until True, then session.get(url), raise_for_status(), .json()."""
        raise NotImplementedError


def fetch_all_concurrently(client: RateLimitedClient, urls: list) -> list:
    """threading.Thread per url (not a pool); results in urls' original order."""
    raise NotImplementedError
