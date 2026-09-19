import threading
import time

from challenges.challenge04.solution import RateLimiter


def test_allows_up_to_capacity_then_blocks():
    # refill_rate=0.0 keeps this deterministic -- no time-based flakiness.
    limiter = RateLimiter(capacity=3, refill_rate=0.0)
    assert limiter.allow_request() is True
    assert limiter.allow_request() is True
    assert limiter.allow_request() is True
    assert limiter.allow_request() is False


def test_refills_over_elapsed_time():
    limiter = RateLimiter(capacity=1, refill_rate=5.0)  # 5 tokens/sec
    assert limiter.allow_request() is True
    assert limiter.allow_request() is False
    time.sleep(0.3)  # ~1.5 tokens worth of time, capped at capacity=1
    assert limiter.allow_request() is True


def test_never_exceeds_capacity_under_concurrent_access():
    limiter = RateLimiter(capacity=5, refill_rate=0.0)
    results: list[bool] = []
    results_lock = threading.Lock()

    def hammer():
        for _ in range(50):
            allowed = limiter.allow_request()
            with results_lock:
                results.append(allowed)

    threads = [threading.Thread(target=hammer) for _ in range(8)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    assert sum(results) == 5
    assert len(results) == 400
