import threading
import time


class RateLimiter:
    """
    Thread-safe token-bucket rate limiter.

    - capacity: the maximum number of tokens the bucket can hold, and also
      the number of tokens it starts full with.
    - refill_rate: tokens added per second (a float, so fractional rates
      like 0.5 tokens/sec are allowed). Refill is computed continuously
      from elapsed wall-clock time, not on a fixed tick.
    - Empty bucket: allow_request() returns False and consumes nothing;
      the caller is expected to retry later rather than block.
    - Concurrent access: a single threading.Lock guards every read and
      write of the token count and the last-refill timestamp, so two
      threads can never both be granted the bucket's last token -- each
      call to allow_request() refills-then-checks-then-consumes as one
      atomic critical section.
    - Clock source: time.monotonic(), because it is guaranteed never to go
      backwards (unlike time.time(), which can jump on a system clock
      adjustment) -- correctness here depends on elapsed time always being
      non-negative.
    """

    def __init__(self, capacity: int, refill_rate: float) -> None:
        self._capacity = capacity
        self._refill_rate = refill_rate
        self._tokens = float(capacity)
        self._last_refill = time.monotonic()
        self._lock = threading.Lock()

    def allow_request(self) -> bool:
        """Consume one token and return True, or return False if none available."""
        with self._lock:
            self._refill_locked()
            if self._tokens >= 1.0:
                self._tokens -= 1.0
                return True
            return False

    def _refill_locked(self) -> None:
        # Caller must already hold self._lock.
        now = time.monotonic()
        elapsed = now - self._last_refill
        if elapsed <= 0:
            return
        self._tokens = min(self._capacity, self._tokens + elapsed * self._refill_rate)
        self._last_refill = now

    def __repr__(self) -> str:
        with self._lock:
            self._refill_locked()
            return (
                f"RateLimiter(capacity={self._capacity}, "
                f"refill_rate={self._refill_rate}, tokens={self._tokens:.2f})"
            )
