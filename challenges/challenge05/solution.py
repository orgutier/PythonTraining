"""
Challenge 05 - URL Shortener API
Interview-style challenge. Correctness is pytest-tested (see
tests/test_challenge05.py / `python tools/cli.py test challenge05`); see README.md in this folder
for the full problem statement (POST /shorten, GET /{code}, GET /stats/{code})
and the constraints your solution must follow (Pydantic request/response
models, proper 4xx on invalid input, idempotent shortening, collision-free
codes, and a documented list of edge cases).

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module, matching the convention used by
exercises/weekNN/solution.py.
"""
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class ShortenRequest(BaseModel):
    """Fill in: the incoming {"url": ...} body, with URL validation."""


class ShortenResponse(BaseModel):
    """Fill in: the outgoing {"code", "short_url"} body."""


@app.post("/shorten")
def shorten(request: ShortenRequest) -> ShortenResponse:
    raise NotImplementedError


@app.get("/{code}")
def redirect(code: str):
    raise NotImplementedError


@app.get("/stats/{code}")
def stats(code: str) -> dict:
    raise NotImplementedError
