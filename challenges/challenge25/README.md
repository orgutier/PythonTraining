# Challenge 25 — URL Shortener API with Dependency-Injected Auth

**Do this after:** Stage 13 (FastAPI)
**Correctness is pytest-tested:** `python tools/cli.py test challenge25` (or `pytest tests/test_challenge25.py`). The constraints below on *how* you write it are not something pytest can check -- grade those yourself.

## Problem

"Write me a URL shortener" is one of the most common "design + code it
live" interview exercises. This version adds an API-key check via
`Depends()`, a validated query parameter, and an `async def` route, so
the exercise covers the rest of Stage 13 alongside the routing and
Pydantic models the original problem is about.

Implement:

```python
app = FastAPI()

class ShortenRequest(BaseModel):
    url: HttpUrl

class ShortenResponse(BaseModel):
    code: str
    short_url: str

def get_api_key(x_api_key: str = Header(default="")) -> str:
    """Raise HTTPException(401) if the X-API-Key header is missing/empty; else return it."""

@app.post("/shorten")
def shorten(req: ShortenRequest, api_key: str = Depends(get_api_key)) -> ShortenResponse:
    """Create (or reuse, if this exact URL was already shortened) a short code."""

@app.get("/search")
def search(prefix: str = "", limit: int = Query(default=10, le=100)):
    """{"codes": every known code starting with prefix, capped at limit}."""

@app.get("/stats/{code}")
def stats(code: str):
    """{"code", "url", "clicks"}. 404 if code doesn't exist."""

@app.get("/{code}")
async def redirect(code: str):
    """{"redirect_to": the original url}, incrementing that code's click count. 404 if code doesn't exist."""
```

```python
client.post("/shorten", json={"url": "https://example.com"}, headers={"x-api-key": "k"})
# -> 200 {"code": "abc123", "short_url": "/abc123"}
client.post("/shorten", json={"url": "https://example.com"})
# -> 401 (no X-API-Key header)
client.get("/search?prefix=a&limit=5")
# -> {"codes": [...]}  -- at most 5 codes, limit capped at 100 even if a caller asks for more
```

## Constraints on HOW you write it

1. **`get_api_key` must read a `Header`**, not a query parameter or the
   request body -- `x_api_key: str = Header(default="")`, not a bare
   `= ""` default (a bare default makes FastAPI treat it as a *query*
   parameter, not a header).
2. **`shorten` must inject `get_api_key` via `Depends(get_api_key)`** --
   the route itself doesn't validate the header; it just declares that
   it needs a valid one, and trusts the dependency to enforce that.
3. **Submitting the same URL twice must return the same `code` both
   times** -- don't waste a fresh code on a URL you've already
   shortened.
4. **`redirect` must be `async def`**; the other three routes are plain
   `def` -- the point is seeing both in the same file, not that this one
   specifically needs to `await` anything.
5. **`search`'s `limit` must use `Query(default=10, le=100)`** so FastAPI
   itself rejects `limit=1000` with a 422, rather than your handler code
   clamping it manually.
6. **`ShortenRequest`/`ShortenResponse` must be real `pydantic.BaseModel`
   classes** -- `url: HttpUrl` specifically, so an invalid URL is
   rejected by Pydantic's own validation (a 422) before your handler
   code ever runs.
7. **Route registration order matters: `/search` must be defined before
   `/{code}`.** FastAPI matches routes in the order they're registered,
   and `/{code}` is a single-segment catch-all -- if it's registered
   first, a request to `/search` matches `/{code}` instead (treating
   `"search"` as a code) and never reaches your `search` function at
   all. `/stats/{code}` doesn't have this problem (it's two segments,
   `/{code}` only ever matches one), but keep it above `/{code}` anyway
   for readability.
