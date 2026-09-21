from unittest.mock import Mock, patch
import pytest
import requests
from challenges.challenge24.solution import (
    RetryingJobSubmitter,
    SafeCounter,
    submit_all_with_pool,
    submit_all_and_count_successes,
)


def _fake_response(json_data):
    response = Mock()
    response.json.return_value = json_data
    response.raise_for_status.return_value = None
    return response


def test_submit_job_succeeds_first_try():
    session = Mock()
    session.post.return_value = _fake_response({"ok": True})
    submitter = RetryingJobSubmitter(session)
    assert submitter.submit_job("https://example.test", {"a": 1}) == {"ok": True}


def test_submit_job_retries_then_succeeds(monkeypatch):
    monkeypatch.setattr("time.sleep", lambda seconds: None)
    session = Mock()
    call_count = {"n": 0}

    def flaky_post(url, json):
        call_count["n"] += 1
        if call_count["n"] < 2:
            raise requests.exceptions.ConnectionError("boom")
        return _fake_response({"ok": True})

    session.post.side_effect = flaky_post
    submitter = RetryingJobSubmitter(session, max_attempts=3)
    assert submitter.submit_job("https://example.test", {}) == {"ok": True}
    assert call_count["n"] == 2


def test_submit_job_raises_after_exhausting_attempts(monkeypatch):
    monkeypatch.setattr("time.sleep", lambda seconds: None)
    session = Mock()
    session.post.side_effect = requests.exceptions.ConnectionError("boom")
    submitter = RetryingJobSubmitter(session, max_attempts=2)
    with pytest.raises(requests.exceptions.ConnectionError):
        submitter.submit_job("https://example.test", {})


def test_submit_all_with_pool_preserves_order():
    session = Mock()
    session.post.side_effect = lambda url, json: _fake_response({"payload": json})
    submitter = RetryingJobSubmitter(session)
    jobs = [("https://example.test", {"i": i}) for i in range(5)]
    results = submit_all_with_pool(submitter, jobs)
    assert [r["payload"]["i"] for r in results] == list(range(5))


def test_safe_counter_exact_under_concurrency():
    session = Mock()
    session.post.side_effect = lambda url, json: _fake_response({"ok": True})
    submitter = RetryingJobSubmitter(session)
    counter = SafeCounter()
    jobs = [("https://example.test", {"i": i}) for i in range(50)]
    submit_all_and_count_successes(submitter, jobs, counter, max_workers=8)
    assert counter.value == 50
