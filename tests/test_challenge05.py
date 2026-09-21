import uuid

from fastapi.testclient import TestClient

from challenges.challenge05.solution import app

client = TestClient(app)


def _unique_url() -> str:
    # A fresh URL per test avoids any dependency on shared in-memory state
    # being reset between tests (it isn't, by design -- see the app's
    # module-level storage).
    return f"https://example.com/{uuid.uuid4()}"


def test_shorten_then_redirect():
    url = _unique_url()
    response = client.post("/shorten", json={"url": url})
    assert response.status_code == 200
    body = response.json()
    code = body["code"]
    assert body["short_url"] == f"/{code}"

    redirect = client.get(f"/{code}", follow_redirects=False)
    assert redirect.status_code == 307
    assert redirect.headers["location"] == url


def test_stats_tracks_click_count():
    url = _unique_url()
    code = client.post("/shorten", json={"url": url}).json()["code"]

    client.get(f"/{code}", follow_redirects=False)
    client.get(f"/{code}", follow_redirects=False)

    stats = client.get(f"/stats/{code}")
    assert stats.status_code == 200
    data = stats.json()
    assert data["clicks"] == 2
    assert data["url"] == url


def test_shortening_the_same_url_twice_returns_the_same_code():
    url = _unique_url()
    first = client.post("/shorten", json={"url": url}).json()["code"]
    second = client.post("/shorten", json={"url": url}).json()["code"]
    assert first == second


def test_invalid_url_is_rejected_with_422():
    response = client.post("/shorten", json={"url": "not-a-url"})
    assert response.status_code == 422


def test_missing_url_field_is_rejected_with_422():
    response = client.post("/shorten", json={})
    assert response.status_code == 422


def test_unknown_code_returns_404_for_redirect_and_stats():
    unknown = "this-short-code-should-never-exist-abc123"
    assert client.get(f"/{unknown}", follow_redirects=False).status_code == 404
    assert client.get(f"/stats/{unknown}").status_code == 404


def test_never_clicked_code_reports_zero_clicks():
    url = _unique_url()
    code = client.post("/shorten", json={"url": url}).json()["code"]
    stats = client.get(f"/stats/{code}")
    assert stats.json()["clicks"] == 0
