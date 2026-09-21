from unittest.mock import patch
import pytest
from fastapi.testclient import TestClient
from challenges.challenge26.solution import app, _check_ins, _travel_totals, get_diagnostics, run_server

client = TestClient(app)


@pytest.fixture(autouse=True)
def _reset_state():
    _check_ins.clear()
    _travel_totals.clear()
    yield
    _check_ins.clear()
    _travel_totals.clear()


def test_checkin_checkout_and_average():
    client.post("/checkin", json={"id": 1, "station_name": "A", "t": 3})
    client.post("/checkout", json={"id": 1, "station_name": "B", "t": 8})
    response = client.get("/average?start_station=A&end_station=B")
    assert response.json() == {"average": 5.0}


def test_average_folds_multiple_trips():
    client.post("/checkin", json={"id": 1, "station_name": "A", "t": 0})
    client.post("/checkout", json={"id": 1, "station_name": "B", "t": 10})
    client.post("/checkin", json={"id": 2, "station_name": "A", "t": 0})
    client.post("/checkout", json={"id": 2, "station_name": "B", "t": 20})
    response = client.get("/average?start_station=A&end_station=B")
    assert response.json() == {"average": 15.0}


def test_checkout_without_checkin_returns_400():
    response = client.post("/checkout", json={"id": 99, "station_name": "B", "t": 8})
    assert response.status_code == 400


def test_average_missing_query_params_is_422():
    assert client.get("/average?start_station=A").status_code == 422
    assert client.get("/average").status_code == 422


def test_average_unknown_route_is_404():
    assert client.get("/average?start_station=X&end_station=Y").status_code == 404


def test_get_diagnostics():
    diagnostics = get_diagnostics()
    assert "/average" in diagnostics["openapi_paths"]
    assert diagnostics["docs_status"] == 200


def test_run_server_calls_uvicorn_run_without_starting_a_server():
    with patch("uvicorn.run") as mock_run:
        run_server(host="0.0.0.0", port=9000)
    mock_run.assert_called_once_with(app, host="0.0.0.0", port=9000)
