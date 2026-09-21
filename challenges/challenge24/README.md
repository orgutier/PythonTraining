# Challenge 24 — Bounded Job Queue with Retry and ThreadPoolExecutor

**Do this after:** Week 12 (Requests + Threading)
**Correctness is pytest-tested:** `python tools/cli.py test challenge24` (or `pytest tests/test_challenge24.py`). The constraints below on *how* you write it are not something pytest can check -- grade those yourself.

## Problem

A companion to Challenge 23: `concurrent.futures.ThreadPoolExecutor` is
the higher-level alternative to managing `threading.Thread` objects by
hand, and it's what most real code actually reaches for. This challenge
pairs it with retry/backoff (posting jobs that sometimes fail
transiently) and a shared counter that has to stay exactly correct no
matter how the pool schedules its workers.

Implement:

```python
class RetryingJobSubmitter:
    def __init__(self, session: "requests.Session", max_attempts: int = 3) -> None: ...
    def submit_job(self, url: str, payload: dict) -> dict:
        """session.post(url, json=payload); raise_for_status(); .json(). On requests.exceptions.RequestException, retry with exponential backoff (time.sleep(0.01 * 2**attempt)) up to max_attempts total; re-raise after the last failed attempt."""

class SafeCounter:
    def __init__(self) -> None: ...
    def increment(self) -> None:
        """Thread-safe += 1."""
    @property
    def value(self) -> int: ...

def submit_all_with_pool(submitter: RetryingJobSubmitter, jobs: list, max_workers: int = 4) -> list:
    """[(url, payload), ...] in jobs, submitted concurrently via ThreadPoolExecutor.map, results in order."""

def submit_all_and_count_successes(submitter: RetryingJobSubmitter, jobs: list, counter: SafeCounter, max_workers: int = 4) -> list:
    """Same as submit_all_with_pool, but also counter.increment() once per successful submit_job call (from inside the pool's own worker threads)."""
```

The tests mock `requests.Session.post` -- never point this at a live
endpoint.

## Constraints on HOW you write it

1. **`submit_job` must retry only on `requests.exceptions
   .RequestException`**, sleeping `0.01 * 2 ** attempt` between
   attempts (exponential backoff), and **must re-raise** once
   `max_attempts` is exhausted -- not swallow the failure and return
   `None`.
2. **`submit_all_with_pool` must use `concurrent.futures
   .ThreadPoolExecutor(max_workers=max_workers)` and its `.map(...)`**
   -- not raw `threading.Thread` (that's Challenge 23's approach) and not
   `.submit()` + manually collecting `Future`s (`.map` already preserves
   order for you).
3. **`SafeCounter.increment` must be protected by a `threading.Lock`** --
   the whole point of `submit_all_and_count_successes` is proving the
   final count is *exactly* right (equal to the number of jobs) even
   though many threads increment it "simultaneously."
4. **A docstring on `submit_job`** listing edge cases: a job that
   succeeds on the first attempt (no sleep at all), and a job that fails
   every single attempt (the *original* exception type from the last
   attempt propagates, not some wrapped/generic one).
