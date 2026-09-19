# Challenge 04 — Rate Limiter (Token Bucket)

**Do this after:** Week 12 (Requests + Threading)
**Not pytest-tested.** Grade it yourself against the constraints below.

## Problem

Implement a thread-safe rate limiter using the token-bucket algorithm: a
bucket starts full with `capacity` tokens; every call to `allow_request()`
consumes one token if one is available (returns `True`) or is rejected if
the bucket is empty (returns `False`); tokens refill continuously over time
at `refill_rate` tokens per second, up to `capacity`.

This exact problem (in one form or another -- token bucket, leaky bucket,
sliding window) is a staple of backend/systems interviews at every company
that runs a public API, because it tests whether you can reason about
*state shared across concurrent callers* correctly, not just write
sequential code.

```python
limiter = RateLimiter(capacity=5, refill_rate=1.0)  # 5 tokens, refills 1/sec
limiter.allow_request()   # True  (4 tokens left)
# ... 4 more calls immediately ...
limiter.allow_request()   # False (bucket empty)
# wait 2 seconds ...
limiter.allow_request()   # True  (~2 tokens refilled)
```

## Required interface

```python
class RateLimiter:
    def __init__(self, capacity: int, refill_rate: float) -> None: ...
    def allow_request(self) -> bool:
        """Consume one token and return True, or return False if none available."""
```

## Constraints on HOW you write it

1. **Must be thread-safe.** Multiple threads will call `allow_request()`
   concurrently -- protect the bucket's shared state with a
   `threading.Lock` (per Week 12), acquired for the shortest critical
   section that's actually correct (don't hold the lock across anything
   that doesn't need it).
2. **Implement the token bucket algorithm from scratch.** No external
   rate-limiting library, and no `time.sleep()`-based busy-waiting to
   "simulate" refill -- compute the number of tokens to add based on the
   actual elapsed wall-clock time (`time.monotonic()`, not `time.time()`,
   since it can't go backwards) since the last refill.
3. **The class docstring must be a comprehensive specification**, covering:
   `capacity` (max tokens, and the starting token count), `refill_rate`
   (tokens added per second, and that it's a float so fractional rates are
   allowed), the exact behavior when the bucket is empty, the exact
   behavior under concurrent access from multiple threads (no two callers
   should ever be granted the same "last token"), and which clock source
   you used and why.
4. **Full type hints**, and a `__repr__` that shows the current token
   count (rounded to 2 decimal places) so the limiter's state is
   debuggable at a glance.

## Prove it's actually thread-safe

Write a short manual check (not a pytest test -- run it yourself, e.g. in a
`python -i` session or a scratch script) that starts several threads
hammering `allow_request()` at once on a limiter with a small capacity, and
confirms the total number of `True` results never exceeds what the bucket's
capacity and elapsed time should allow.
