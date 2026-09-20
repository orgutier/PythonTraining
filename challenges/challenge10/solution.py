"""
Challenge 10 - Underground System API
Interview-style challenge (LeetCode #1396, adapted to FastAPI). Correctness
is pytest-tested (see tests/test_challenge10.py / `python tools/cli.py
test challenge10`); see README.md in this folder for the full problem
statement (POST /checkin, POST /checkout, GET /average/{start}/{end})
and the constraints your solution must follow (Pydantic request models,
proper 4xx on invalid checkout/average requests, and a documented list
of edge cases).

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module, matching the convention used by
exercises/weekNN/solution.py.
"""
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class CheckInRequest(BaseModel):
    """Fill in: the incoming {"id", "station_name", "t"} check-in body."""


class CheckOutRequest(BaseModel):
    """Fill in: the incoming {"id", "station_name", "t"} check-out body."""


@app.post("/checkin")
def checkin(request: CheckInRequest) -> dict:
    raise NotImplementedError


@app.post("/checkout")
def checkout(request: CheckOutRequest) -> dict:
    raise NotImplementedError


@app.get("/average/{start_station}/{end_station}")
def average(start_station: str, end_station: str) -> dict:
    raise NotImplementedError
