from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# In-memory storage only, per the challenge's constraints -- state resets
# when the process restarts.
# _open_checkins: rider id -> (station_name, t)
_open_checkins: dict[int, tuple[str, int]] = {}
# _trips: (start_station, end_station) -> list of completed trip durations
_trips: dict[tuple[str, str], list[int]] = {}


class CheckInRequest(BaseModel):
    id: int
    station_name: str
    t: int


class CheckOutRequest(BaseModel):
    id: int
    station_name: str
    t: int


@app.post("/checkin")
def checkin(request: CheckInRequest) -> dict:
    """
    Record a check-in. A rider can check in again immediately after a
    completed checkout -- _open_checkins only ever holds a rider's
    CURRENT open trip, if any, so reusing an id across separate trips
    works normally.
    """
    _open_checkins[request.id] = (request.station_name, request.t)
    return {"status": "checked in"}


@app.post("/checkout")
def checkout(request: CheckOutRequest) -> dict:
    """
    Complete a trip. Raises 400 if this rider has no open check-in --
    checking out without checking in first is invalid, not silently
    ignored or crashing with a KeyError.
    """
    if request.id not in _open_checkins:
        raise HTTPException(status_code=400, detail="No open check-in for this rider")

    start_station, start_t = _open_checkins.pop(request.id)
    duration = request.t - start_t
    route = (start_station, request.station_name)
    _trips.setdefault(route, []).append(duration)
    return {"status": "checked out", "duration": duration}


@app.get("/average/{start_station}/{end_station}")
def average(start_station: str, end_station: str) -> dict:
    """
    Average travel time across every completed trip between two
    stations. Raises 404 if no trips have been completed for that exact
    route -- never returns a fabricated 0 for a route with no data.
    """
    route = (start_station, end_station)
    durations = _trips.get(route)
    if not durations:
        raise HTTPException(status_code=404, detail="No completed trips for this route")

    return {
        "start_station": start_station,
        "end_station": end_station,
        "average_time": sum(durations) / len(durations),
    }
