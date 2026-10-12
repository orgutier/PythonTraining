"""
Local API Endpoints -- Basic Routes
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage13_tier1_basic01.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage13/tier1_basic01/ and import it as a submodule (e.g.
`from exercises.stage13.tier1_basic01 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    """{"message": "hello"}."""
    raise NotImplementedError


@app.get("/items/{item_id}")
def read_item(item_id: int):
    """{"item_id": item_id} -- item_id is a path parameter."""
    raise NotImplementedError


@app.get("/search")
def search(q: str = ""):
    """{"q": q} -- q is a query parameter."""
    raise NotImplementedError


@app.post("/echo")
def echo(payload: dict):
    """Return payload unchanged."""
    raise NotImplementedError
