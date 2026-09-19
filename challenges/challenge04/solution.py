"""
Challenge 04 - Rate Limiter (Token Bucket)
Interview-style challenge. Correctness is pytest-tested (see
tests/test_challenge04.py / `python tools/cli.py test challenge04`); see README.md in this folder
for the full problem statement and the constraints your solution must follow
(thread safety with threading.Lock, a from-scratch token bucket driven by
time.monotonic(), a comprehensive docstring, and a debuggable __repr__).

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module, matching the convention used by
exercises/weekNN/solution.py.
"""
import threading


class RateLimiter:
    """
    Thread-safe token-bucket rate limiter. Fill in this docstring as part
    of the challenge: document capacity, refill_rate, empty-bucket
    behavior, concurrent-access behavior, and your clock source choice.
    """

    def __init__(self, capacity: int, refill_rate: float) -> None:
        raise NotImplementedError

    def allow_request(self) -> bool:
        """Consume one token and return True, or return False if none available."""
        raise NotImplementedError

    def __repr__(self) -> str:
        raise NotImplementedError
