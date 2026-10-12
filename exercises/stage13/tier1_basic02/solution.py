"""
Local API Endpoints -- Running the App
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage13_tier1_basic02.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage13/tier1_basic02/ and import it as a submodule (e.g.
`from exercises.stage13.tier1_basic02 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/health")
def health():
    """{"status": "ok"}."""
    raise NotImplementedError


@app.post("/notes")
def create_note(payload: dict):
    """Return payload unchanged."""
    raise NotImplementedError


def run_server(app, host: str = "127.0.0.1", port: int = 8000) -> None:
    """uvicorn.run(app, host=host, port=port)."""
    raise NotImplementedError
