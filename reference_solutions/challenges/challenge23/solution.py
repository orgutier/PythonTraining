import time
import threading
import requests


class TokenBucketLimiter:
    def __init__(self, capacity: int, refill_rate: float) -> None:
        self._capacity = capacity
        self._tokens = float(capacity)
        self._refill_rate = refill_rate
        self._last_refill = time.monotonic()
        self._lock = threading.Lock()

    def allow_request(self) -> bool:
        """
        Consume one token if available (thread-safe).

        Edge cases handled:
          - Called immediately after construction -> starts full, so the
            first `capacity` calls all succeed.
          - Called faster than refill_rate can keep up -> returns False
            once the bucket is empty; tokens never go negative.
        """
        with self._lock:
            now = time.monotonic()
            elapsed = now - self._last_refill
            self._tokens = min(self._capacity, self._tokens + elapsed * self._refill_rate)
            self._last_refill = now
            if self._tokens >= 1:
                self._tokens -= 1
                return True
            return False


class RateLimitedClient:
    def __init__(self, session, limiter: TokenBucketLimiter) -> None:
        self.session = session
        self.limiter = limiter

    def get_json(self, url: str) -> dict:
        while not self.limiter.allow_request():
            time.sleep(0.001)
        r = self.session.get(url)
        r.raise_for_status()
        return r.json()


def fetch_all_concurrently(client: RateLimitedClient, urls: list) -> list:
    results = [None] * len(urls)

    def worker(index, url):
        results[index] = client.get_json(url)

    threads = [threading.Thread(target=worker, args=(i, url)) for i, url in enumerate(urls)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return results
