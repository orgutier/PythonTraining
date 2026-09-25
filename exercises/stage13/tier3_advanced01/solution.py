"""
Local API Endpoints -- Async Endpoints
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage13_tier3_advanced01.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage13/tier3_advanced01/ and import it as a submodule (e.g.
`from exercises.stage13.tier3_advanced01 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


from fastapi import FastAPI

app = FastAPI()


@app.get("/async-hello")
async def async_hello():
    """{"message": "hello async"}."""
    raise NotImplementedError


@app.get("/async-items/{item_id}")
async def async_get_item(item_id: int):
    """{"item_id": item_id}."""
    raise NotImplementedError


@app.post("/async-echo")
async def async_echo(payload: dict):
    """Return payload unchanged."""
    raise NotImplementedError
