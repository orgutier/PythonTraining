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
    store[req.id] = (req.station_name, req.t)
    return {"ok": True}


@app.post("/checkout")
async def check_out(req: CheckOutRequest, store: dict = Depends(get_check_ins), totals: dict = Depends(get_travel_totals)):
    """
    Check out rider req.id, folding their trip into the running average.

    Edge cases handled:
      - No matching check-in for req.id -> raises HTTPException(400).
      - A second rider taking the same (start, end) route later -> folds
        into the SAME running total/count, not a separate average.
    """
    if req.id not in store:
        raise HTTPException(status_code=400, detail="no check-in found")
    start_station, start_t = store.pop(req.id)
    key = (start_station, req.station_name)
    total_time, count = totals.get(key, (0, 0))
    totals[key] = (total_time + (req.t - start_t), count + 1)
    return {"ok": True}


@app.get("/average")
def average(start_station: str, end_station: str, totals: dict = Depends(get_travel_totals)):
    key = (start_station, end_station)
    if key not in totals:
        raise HTTPException(status_code=404, detail="no data")
    total_time, count = totals[key]
    return {"average": total_time / count}


def get_diagnostics() -> dict:
    client = TestClient(app)
    openapi = client.get("/openapi.json").json()
    docs_status = client.get("/docs").status_code
    return {"openapi_paths": sorted(openapi["paths"].keys()), "docs_status": docs_status}


def run_server(host: str = "127.0.0.1", port: int = 8000) -> None:
    uvicorn.run(app, host=host, port=port)
