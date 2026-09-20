from fastapi.testclient import TestClient

from challenges.challenge10.solution import app

client = TestClient(app)


def test_checkin_checkout_and_average():
    client.post("/checkin", json={"id": 1, "station_name": "Leyton", "t": 3})
    client.post("/checkout", json={"id": 1, "station_name": "Paradise", "t": 8})

    response = client.get("/average/Leyton/Paradise")
    assert response.status_code == 200
    assert response.json()["average_time"] == 5


def test_average_across_multiple_trips():
    client.post("/checkin", json={"id": 10, "station_name": "A", "t": 0})
    client.post("/checkout", json={"id": 10, "station_name": "B", "t": 10})
    client.post("/checkin", json={"id": 11, "station_name": "A", "t": 0})
    client.post("/checkout", json={"id": 11, "station_name": "B", "t": 20})

    response = client.get("/average/A/B")
    assert response.json()["average_time"] == 15


def test_checkout_without_checkin_is_rejected():
    response = client.post("/checkout", json={"id": 999, "station_name": "X", "t": 5})
    assert 400 <= response.status_code < 500


def test_average_for_unknown_route_is_rejected():
    response = client.get("/average/Nowhere/Nowhere2")
    assert 400 <= response.status_code < 500


def test_rider_can_check_in_again_after_checkout():
    client.post("/checkin", json={"id": 55, "station_name": "P", "t": 0})
    client.post("/checkout", json={"id": 55, "station_name": "Q", "t": 4})

    # Reusing the same rider id for a brand-new trip must work normally.
    second = client.post("/checkin", json={"id": 55, "station_name": "R", "t": 10})
    assert second.status_code == 200
    third = client.post("/checkout", json={"id": 55, "station_name": "S", "t": 16})
    assert third.status_code == 200

    response = client.get("/average/R/S")
    assert response.json()["average_time"] == 6
