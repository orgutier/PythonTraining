# Challenge 23 — Rate-Limited HTTP Client

**Do this after:** Stage 12 (Requests + Threading)
**Correctness is pytest-tested:** `python tools/cli.py test challenge23` (or `pytest tests/test_challenge23.py`). The constraints below on *how* you write it are not something pytest can check -- grade those yourself.

## Problem

A rate limiter in isolation is a nice `threading.Lock` exercise, but the
real question interviewers ask is "now use it to actually throttle HTTP
calls made from multiple threads at once." This challenge builds both
halves together: a thread-safe token-bucket limiter, and an HTTP client
that waits on it before every request.

Implement:

```python
class TokenBucketLimiter:
    def __init__(self, capacity: int, refill_rate: float) -> None: ...
    def allow_request(self) -> bool:
        """Thread-safe: consume one token and return True, or return False if none is available right now. Refills continuously based on elapsed time (time.monotonic())."""

class RateLimitedClient:
    def __init__(self, session: "requests.Session", limiter: TokenBucketLimiter) -> None: ...
    def get_json(self, url: str) -> dict:
        """Block (poll allow_request() with a short time.sleep between tries) until a token is available, then session.get(url); raise_for_status(); return .json()."""

def fetch_all_concurrently(client: RateLimitedClient, urls: list) -> list:
    """Fetch every url via client.get_json, concurrently, using raw threading.Thread (not a pool). Return results in the SAME order as urls, regardless of which thread finishes first."""
```

The tests mock `requests.Session.get` -- never point this at a live
endpoint (see README's "Git hook integration" section).

## Constraints on HOW you write it

1. **`TokenBucketLimiter.allow_request` must be protected by a
   `threading.Lock`** covering the refill-and-consume check as one atomic
   step -- two threads calling it at the same moment must never both
   successfully consume the same last token.
2. **`RateLimitedClient.get_json` must poll in a loop** (`while not
   self.limiter.allow_request(): time.sleep(...)` , a short sleep like
   `0.001`), not fail/raise when no token is immediately available.
3. **`get_json` must call `r.raise_for_status()`** before `.json()` --
   an HTTP error response must raise, not be silently returned as if it
   were valid data.
4. **`fetch_all_concurrently` must use `threading.Thread` directly**
   (`.start()` every thread, *then* `.join()` every thread -- not
   `concurrent.futures.ThreadPoolExecutor`, which is Challenge 24's
   tool), and **must preserve `urls`' order in the result** even though
   the threads themselves finish in whatever order they finish in (write
   each result into a pre-sized list by index, not by appending as
   results arrive).
5. **A docstring on `allow_request`** listing edge cases: calling it
   immediately after construction (starts full, so the first `capacity`
   calls succeed), and calling it faster than the refill rate can keep up
   (returns `False` once the bucket is empty, doesn't go negative).
