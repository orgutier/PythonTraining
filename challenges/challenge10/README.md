# Challenge 10 — Underground System API

**Do this after:** Week 13 (FastAPI)
**Correctness is pytest-tested:** `python tools/cli.py test challenge10` (or `pytest tests/test_challenge10.py`). The constraints below on *how* you write it are not something pytest can check -- grade those yourself.

## Problem

LeetCode #1396 ("Design Underground System") asks you to track riders
checking in and out of a metro system and report average travel times
between stations. This challenge asks for the same system, but exposed
as a small FastAPI service instead of a plain class.

## Required endpoints

| Method & path | Behavior |
|---|---|
| `POST /checkin` | Body: `{"id": 1, "station_name": "Leyton", "t": 3}`. Records that rider `id` checked in at `station_name` at time `t`. |
| `POST /checkout` | Body: `{"id": 1, "station_name": "Paradise", "t": 8}`. Records that rider `id` (who must have an open check-in) checked out, completing a trip of duration `t - checkin_t` from their check-in station to this one. |
| `GET /average/{start_station}/{end_station}` | Returns `{"start_station": ..., "end_station": ..., "average_time": ...}` -- the average travel time across every completed trip from `start_station` to `end_station`. |

Storage is **in-memory only** -- plain Python dicts at module scope, same
as Challenge 05's URL shortener. No database, no file persistence.

## Constraints on HOW you write it

1. **Request and response bodies must be Pydantic `BaseModel` classes**,
   not raw dicts passed straight through -- define `CheckInRequest` and
   `CheckOutRequest` models (per Week 13's lesson on typed validation).
2. **`/checkout` for a rider with no open check-in must return a proper
   4xx error**, not a 500 or a silently-wrong result -- validate that the
   rider actually has a pending check-in before completing a trip.
3. **The same rider ID must be reusable for a new trip after they check
   out** -- checking in again after a completed checkout should work
   normally, not be rejected as "already checked in."
4. **`GET /average/...` for a station pair with zero completed trips
   must return a proper 4xx error**, not a division-by-zero crash or a
   fabricated `0`.
5. **A docstring (module-level or per-function) with a comprehensive
   list of the edge cases your implementation handles:** checkout
   without checkin, checkin without a matching checkout yet (no trip
   recorded until checkout happens), multiple completed trips between
   the same two stations (correctly averaged), and an average request
   for a route no one has ever traveled.

## Check your work

`python tools/cli.py test challenge10` runs `tests/test_challenge10.py`,
which uses FastAPI's `TestClient` (Week 13) to check in and out several
riders across multiple trips, verifies the averages, and confirms the
checkout-without-checkin and no-data-for-route cases both come back as
proper error responses instead of crashing the server.
