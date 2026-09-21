"""
Challenge 25 - URL Shortener API with Dependency-Injected Auth
Interview-style challenge. Correctness is pytest-tested (see
tests/test_challenge25.py / `python tools/cli.py test challenge25`); see
README.md in this folder for the full problem statement and the constraints
your solution must follow (Depends() for a header-based auth check, Pydantic request/response models, an async def route, and Query() validation on a query parameter).

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module, matching the convention used by
exercises/weekNN/solution.py.
"""


from fastapi import FastAPI, Depends, HTTPException, Query, Header
from pydantic import BaseModel, HttpUrl

app = FastAPI()

_store = {}


class ShortenRequest(BaseModel):
    url: HttpUrl


class ShortenResponse(BaseModel):
    code: str
    short_url: str


def get_api_key(x_api_key: str = Header(default="")) -> str:
    """Raise HTTPException(401) if empty; else return x_api_key."""
    raise NotImplementedError


@app.post("/shorten")
def shorten(req: ShortenRequest, api_key: str = Depends(get_api_key)) -> ShortenResponse:
    """Create or reuse a code for req.url."""
    raise NotImplementedError


@app.get("/search")
def search(prefix: str = "", limit: int = Query(default=10, le=100)):
    """{"codes": [...]} -- codes starting with prefix, capped at limit."""
    raise NotImplementedError


@app.get("/stats/{code}")
def stats(code: str):
    """{"code", "url", "clicks"}; 404 if unknown."""
    raise NotImplementedError


@app.get("/{code}")
async def redirect(code: str):
    """{"redirect_to": ...}; 404 if unknown. Increments clicks."""
    raise NotImplementedError
