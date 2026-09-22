"""
Local API Endpoints -- TestClient, Docs, and uvicorn.run
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage13_exercise05.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage13/exercise05/ and import it as a submodule (e.g.
`from exercises.stage13.exercise05 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


from fastapi import FastAPI
from fastapi.testclient import TestClient
import uvicorn

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


def get_health_status(app) -> dict:
    """TestClient(app).get("/health").json()."""
    raise NotImplementedError


def get_openapi_schema(app) -> dict:
    """TestClient(app).get("/openapi.json").json()."""
    raise NotImplementedError


def docs_page_status(app) -> int:
    """TestClient(app).get("/docs").status_code."""
    raise NotImplementedError


def run_server(app, host: str = "127.0.0.1", port: int = 8000) -> None:
    """uvicorn.run(app, host=host, port=port)."""
    raise NotImplementedError
