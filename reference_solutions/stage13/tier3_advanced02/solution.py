from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()


@app.get("/ping")
def ping():
    return {"pong": True}


@app.post("/echo2")
def echo2(payload: dict):
    return payload


def client_get_json(app, path: str) -> dict:
    return TestClient(app).get(path).json()


def client_post_json(app, path: str, payload: dict) -> dict:
    return TestClient(app).post(path, json=payload).json()


def client_status_code(app, path: str) -> int:
    return TestClient(app).get(path).status_code
