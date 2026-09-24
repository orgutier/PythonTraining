import datetime
import json


def aware_now_utc():
    return datetime.datetime.now(datetime.timezone.utc)


def is_timezone_aware(dt) -> bool:
    return dt.tzinfo is not None and dt.tzinfo.utcoffset(dt) is not None


def make_aware(dt, tz):
    return dt.replace(tzinfo=tz)


def datetime_default(obj):
    if isinstance(obj, datetime.datetime):
        return obj.isoformat()
    raise TypeError(f"not JSON serializable: {obj!r}")


def serialize_event(name: str, timestamp) -> str:
    return json.dumps({"name": name, "timestamp": timestamp}, default=datetime_default)
