# Timezone-Aware vs. Naive Datetimes

Implement:

- `naive_now()` -- `datetime.datetime.now()` -- **naive**: no timezone information at all.
- `aware_now_utc()` -- `datetime.datetime.now(datetime.timezone.utc)` -- **aware**: explicitly anchored to UTC.
- `is_timezone_aware(dt) -> bool` -- `dt.tzinfo is not None and dt.tzinfo.utcoffset(dt) is not None` (the official recipe -- just checking `dt.tzinfo is not None` isn't quite enough in every edge case, though it's right for the objects these exercises produce).
- `to_utc_isoformat(dt) -> str` -- `dt.astimezone(datetime.timezone.utc).isoformat()` (only works on an *aware* `dt` -- converting a naive one raises, since there's no original timezone to convert *from*).
- `make_aware(dt, tz)` -- `dt.replace(tzinfo=tz)` (attaches a timezone to a naive datetime *without* shifting the clock time -- for that, you'd use `.astimezone()` instead).

Comparing or subtracting a naive and an aware `datetime` raises `TypeError` -- Python refuses to guess which timezone the naive one is in, which is exactly why mixing the two is a classic bug source in real code.

See the Study Reference presentation, Topic 9, for the theory.
