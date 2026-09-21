import json
import datetime


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def point_default(obj):
    if isinstance(obj, Point):
        return {"x": obj.x, "y": obj.y}
    raise TypeError(f"not JSON serializable: {obj!r}")


def serialize_with_points(data) -> str:
    return json.dumps(data, default=point_default)


def datetime_default(obj):
    if isinstance(obj, datetime.datetime):
        return obj.isoformat()
    raise TypeError(f"not JSON serializable: {obj!r}")


def serialize_with_datetimes(data) -> str:
    return json.dumps(data, default=datetime_default)


def set_default(obj):
    if isinstance(obj, set):
        return sorted(obj)
    raise TypeError(f"not JSON serializable: {obj!r}")


def serialize_with_sets(data) -> str:
    return json.dumps(data, default=set_default)
