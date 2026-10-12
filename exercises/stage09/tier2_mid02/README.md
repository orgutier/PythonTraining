# Timezone-Aware Timestamps in JSON

`datetime.datetime` isn't one of the handful of types `json.dumps` knows how to serialize natively -- and naive vs. timezone-aware matters even before you get that far. Implement:

- `aware_now_utc()` -- `datetime.datetime.now(datetime.timezone.utc)` -- **aware**: explicitly anchored to UTC.
- `is_timezone_aware(dt) -> bool` -- `dt.tzinfo is not None and dt.tzinfo.utcoffset(dt) is not None` (the official recipe -- just checking `dt.tzinfo is not None` isn't quite enough in every edge case, though it's right for the objects these exercises produce).
- `make_aware(dt, tz)` -- `dt.replace(tzinfo=tz)` (attaches a timezone to a naive datetime *without* shifting the clock time -- for that, you'd use `.astimezone()` instead).
- `datetime_default(obj)` -- if `obj` is a `datetime.datetime`, return `obj.isoformat()`; else `raise TypeError(f"not JSON serializable: {obj!r}")`. This is a `default=` function for `json.dumps`: it's called for any object `json.dumps` doesn't natively know how to handle, and must return something JSON-serializable (or raise).
- `serialize_event(name: str, timestamp) -> str` -- `json.dumps({"name": name, "timestamp": timestamp}, default=datetime_default)`.

Put together: build a naive `datetime`, make it timezone-aware with `make_aware`, then hand it to `serialize_event` -- `json.dumps` calls `datetime_default` under the hood to turn that aware datetime into an ISO string (complete with its `+00:00` UTC offset) in the JSON output.

See the Study Reference presentation, Topic 9 (Mid tier), for the theory.
