from unittest.mock import Mock, patch
import pytest
import requests
from challenges.challenge23.solution import (
    TokenBucketLimiter,
    RateLimitedClient,
    fetch_all_concurrently,
)


def test_token_bucket_starts_full():
    limiter = TokenBucketLimiter(capacity=3, refill_rate=1.0)
    assert limiter.allow_request() is True
    assert limiter.allow_request() is True
    assert limiter.allow_request() is True
    assert limiter.allow_request() is False


def test_token_bucket_refills_over_time():
    import time
    limiter = TokenBucketLimiter(capacity=1, refill_rate=100.0)
    assert limiter.allow_request() is True
    assert limiter.allow_request() is False
    time.sleep(0.02)
    assert limiter.allow_request() is True


def _fake_response(json_data):
    response = Mock()
    response.json.return_value = json_data
    response.raise_for_status.return_value = None
    return response


def test_get_json_waits_for_a_token_then_fetches():
    limiter = TokenBucketLimiter(capacity=1, refill_rate=1000.0)
    session = Mock()
    session.get.return_value = _fake_response({"ok": True})
    client = RateLimitedClient(session, limiter)
    assert client.get_json("https://example.test") == {"ok": True}


def test_get_json_raises_for_http_error():
    limiter = TokenBucketLimiter(capacity=1, refill_rate=1000.0)
    session = Mock()
    bad_response = Mock()
    bad_response.raise_for_status.side_effect = requests.HTTPError("500")
    session.get.return_value = bad_response
    client = RateLimitedClient(session, limiter)
    with pytest.raises(requests.HTTPError):
        client.get_json("https://example.test")


def test_fetch_all_concurrently_preserves_order():
    limiter = TokenBucketLimiter(capacity=10, refill_rate=1000.0)
    session = Mock()
    session.get.side_effect = lambda url: _fake_response({"url": url})
    client = RateLimitedClient(session, limiter)
    urls = [f"https://example.test/{i}" for i in range(5)]
    results = fetch_all_concurrently(client, urls)
    assert [r["url"] for r in results] == urls
