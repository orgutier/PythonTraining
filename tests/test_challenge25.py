import pytest
from fastapi.testclient import TestClient
from challenges.challenge25.solution import app, _store

client = TestClient(app)


@pytest.fixture(autouse=True)
def _reset_store():
    _store.clear()
    yield
    _store.clear()


def test_shorten_requires_api_key():
    response = client.post("/shorten", json={"url": "https://example.com"})
    assert response.status_code == 401


def test_shorten_with_api_key_succeeds():
    response = client.post(
        "/shorten", json={"url": "https://example.com"}, headers={"x-api-key": "k"}
    )
    assert response.status_code == 200
    assert "code" in response.json()


def test_shorten_same_url_twice_returns_same_code():
    headers = {"x-api-key": "k"}
    first = client.post("/shorten", json={"url": "https://example.com/a"}, headers=headers).json()
    second = client.post("/shorten", json={"url": "https://example.com/a"}, headers=headers).json()
    assert first["code"] == second["code"]


def test_shorten_invalid_url_rejected():
    response = client.post(
        "/shorten", json={"url": "not a url"}, headers={"x-api-key": "k"}
    )
    assert response.status_code == 422


def test_redirect_increments_clicks_and_404_for_unknown():
    headers = {"x-api-key": "k"}
    code = client.post("/shorten", json={"url": "https://example.com/b"}, headers=headers).json()["code"]
    r1 = client.get(f"/{code}")
    assert r1.status_code == 200
    assert r1.json()["redirect_to"] == "https://example.com/b"

    stats = client.get(f"/stats/{code}").json()
    assert stats["clicks"] == 1

    assert client.get("/nonexistent").status_code == 404


def test_search_limit_is_capped_by_query_validation():
    assert client.get("/search?limit=1000").status_code == 422


def test_search_returns_matching_prefix():
    headers = {"x-api-key": "k"}
    client.post("/shorten", json={"url": "https://example.com/c"}, headers=headers)
    result = client.get("/search?prefix=&limit=50").json()
    assert len(result["codes"]) >= 1
