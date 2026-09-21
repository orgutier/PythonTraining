# Custom JSON Encoding

`json.dumps` only knows how to serialize the handful of builtin types (`dict`, `list`, `str`, `int`/`float`, `bool`, `None`). For anything else, pass a `default=` function: it receives the unrecognized object and must return something JSON-serializable (or raise `TypeError`). Implement three:

- `point_default(obj)` -- if `obj` is a `Point` (already defined, with `.x`/`.y`), return `{"x": obj.x, "y": obj.y}`; else `raise TypeError(f"not JSON serializable: {obj!r}")`. `serialize_with_points(data) -> str` -- `json.dumps(data, default=point_default)`.
- `datetime_default(obj)` -- if `obj` is a `datetime.datetime`, return `obj.isoformat()`; else raise the same `TypeError`. `serialize_with_datetimes(data) -> str` -- `json.dumps(data, default=datetime_default)`.
- `set_default(obj)` -- if `obj` is a `set`, return `sorted(obj)` (JSON has no set type, only arrays); else raise. `serialize_with_sets(data) -> str` -- `json.dumps(data, default=set_default)`.

See the Study Reference presentation, Topic 9, for the theory.
