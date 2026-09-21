# JSON Basics

Implement:

- `save_json(path: str, data) -> None` -- `with open(path, "w") as f: json.dump(data, f)`.
- `load_json(path: str)` -- `with open(path) as f: return json.load(f)`.
- `to_json_string(data) -> str` -- `json.dumps(data)` (the string version of `dump`, no file involved).
- `from_json_string(text: str)` -- `json.loads(text)` (the string version of `load`).

See the Study Reference presentation, Topic 9, for the theory.
