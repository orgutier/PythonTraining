import json


def save_json(path: str, data) -> None:
    with open(path, "w") as f:
        json.dump(data, f)


def load_json(path: str):
    with open(path) as f:
        return json.load(f)


def to_json_string(data) -> str:
    return json.dumps(data)


def from_json_string(text: str):
    return json.loads(text)
