# Challenge 26 — Underground System API with Live Diagnostics

**Do this after:** Week 13 (FastAPI)
**Correctness is pytest-tested:** `python tools/cli.py test challenge26` (or `pytest tests/test_challenge26.py`). The constraints below on *how* you write it are not something pytest can check -- grade those yourself.

## Problem

Design Underground System (LeetCode #1396) tracks riders checking in and
out of a transit system, and reports the average travel time between any
two stations. This version injects its storage via `Depends()` instead of
touching module globals directly inside the routes, and adds a small
diagnostics utility built from `TestClient`/`uvicorn.run` -- the parts of
Week 13 the URL shortener challenge didn't need.

Implement:

```python
app = FastAPI()

class CheckInRequest(BaseModel):
    id: int
    station_name: str
    t: int

class CheckOutRequest(BaseModel):
    id: int
    station_name: str
    t: int

def get_check_ins() -> dict: ...   # returns the shared _check_ins dict
def get_travel_totals() -> dict: ...  # returns the shared _travel_totals dict

@app.post("/checkin")
async def check_in(req: CheckInRequest, store: dict = Depends(get_check_ins)):
    """Record that rider req.id checked in at req.station_name at time req.t."""

@app.post("/checkout")
async def check_out(req: CheckOutRequest, store: dict = Depends(get_check_ins), totals: dict = Depends(get_travel_totals)):
    """Look up the rider's check-in (400 if there isn't one), compute the travel time, fold it into totals for (start_station, req.station_name), and forget the check-in."""

@app.get("/average")
def average(start_station: str, end_station: str, totals: dict = Depends(get_travel_totals)):
    """The average travel time for that (start, end) pair. 404 if there's no data for it yet."""

def get_diagnostics() -> dict:
    """{"openapi_paths": sorted list of every path in app's OpenAPI schema, "docs_status": the /docs page's status code} -- built with TestClient(app), not a running server."""

def run_server(host: str = "127.0.0.1", port: int = 8000) -> None:
    """uvicorn.run(app, host=host, port=port)."""
```

```python
client.post("/checkin", json={"id": 1, "station_name": "A", "t": 3})
client.post("/checkout", json={"id": 1, "station_name": "B", "t": 8})
client.get("/average?start_station=A&end_station=B")   # -> {"average": 5.0}
```

## Constraints on HOW you write it

1. **`check_in` and `check_out` must both be `async def`**, and **both
   must receive their storage via `Depends(get_check_ins)`/`Depends
   (get_travel_totals)`** -- never reach for the module-level
   `_check_ins`/`_travel_totals` dict by name from inside a route
   function. The dependency functions are where those names are
   allowed to appear.
2. **`start_station`/`end_station` on `/average` must be required query
   parameters** (no default value) -- omitting either from the URL must
   produce a 422 from FastAPI itself, not a `KeyError` from your handler.
3. **`check_out` must raise `HTTPException(400)`** if `req.id` has no
   matching check-in -- not silently ignore the request or crash with an
   unhandled `KeyError`.
4. **`get_diagnostics` must build its own `TestClient(app)`** and read
   `/openapi.json` and `/docs` through it -- it must not require an
   actual server to be running.
5. **`run_server` must call `uvicorn.run(app, host=host, port=port)`** --
   tests mock `uvicorn.run` so this never actually starts listening on a
   port during the test suite.
6. **A docstring on `check_out`** listing edge cases: checking out a
   rider who never checked in (400), and a second rider taking the exact
   same route later (folds into the *same* running average, not a
   separate one).
