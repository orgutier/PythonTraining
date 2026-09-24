"""
Local API Endpoints -- Testing Apps with TestClient
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage13_advanced02.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage13/advanced02/ and import it as a submodule (e.g.
`from exercises.stage13.advanced02 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


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
    """TestClient(app).get(path).json()."""
    raise NotImplementedError


def client_post_json(app, path: str, payload: dict) -> dict:
    """TestClient(app).post(path, json=payload).json()."""
    raise NotImplementedError


def client_status_code(app, path: str) -> int:
    """TestClient(app).get(path).status_code."""
    raise NotImplementedError
