"""
Challenge 26 - Underground System API with Live Diagnostics
Interview-style challenge. Correctness is pytest-tested (see
tests/test_challenge26.py / `python tools/cli.py test challenge26`); see
README.md in this folder for the full problem statement and the constraints
your solution must follow (two async def routes sharing state via Depends(), a required (non-defaulted) query parameter pair, and TestClient()/uvicorn.run() used to introspect the app itself).

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module, matching the convention used by
exercises/weekNN/solution.py.
"""


from fastapi import FastAPI, Depends, HTTPException
from fastapi.testclient import TestClient
from pydantic import BaseModel
import uvicorn

app = FastAPI()

_check_ins = {}
_travel_totals = {}


class CheckInRequest(BaseModel):
    id: int
    station_name: str
    t: int


class CheckOutRequest(BaseModel):
    id: int
    station_name: str
    t: int


def get_check_ins() -> dict:
    return _check_ins


def get_travel_totals() -> dict:
    return _travel_totals


@app.post("/checkin")
async def check_in(req: CheckInRequest, store: dict = Depends(get_check_ins)):
    """Record req.id's check-in (station_name, t)."""
    raise NotImplementedError


@app.post("/checkout")
async def check_out(req: CheckOutRequest, store: dict = Depends(get_check_ins), totals: dict = Depends(get_travel_totals)):
    """Fold this trip's time into totals; 400 if no check-in for req.id."""
    raise NotImplementedError


@app.get("/average")
def average(start_station: str, end_station: str, totals: dict = Depends(get_travel_totals)):
    """{"average": ...}; 404 if no data for this (start, end) pair."""
    raise NotImplementedError


def get_diagnostics() -> dict:
    """{"openapi_paths": [...], "docs_status": ...} via a fresh TestClient(app)."""
    raise NotImplementedError


def run_server(host: str = "127.0.0.1", port: int = 8000) -> None:
    """uvicorn.run(app, host=host, port=port)."""
    raise NotImplementedError
