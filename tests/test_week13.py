from fastapi.testclient import TestClient
from exercises.week13.solution import app

client = TestClient(app)


def test_say_hello():
    response = client.get("/hello/World")
    assert response.json() == {"message": "Hello, World!"}


def test_add():
    response = client.get("/add", params={"a": 2, "b": 3})
    assert response.json() == {"result": 5}
