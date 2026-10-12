import json
import os


def config_path(directory: str, name: str) -> str:
    return os.path.join(directory, name + ".json")


def config_exists(directory: str, name: str) -> bool:
    return os.path.exists(config_path(directory, name))


def save_config(directory: str, name: str, data: dict) -> None:
    with open(config_path(directory, name), "w") as f:
        json.dump(data, f)


def load_config(directory: str, name: str) -> dict:
    with open(config_path(directory, name)) as f:
        return json.load(f)


def list_config_names(directory: str) -> list[str]:
    return sorted(f[:-5] for f in os.listdir(directory) if f.endswith(".json"))
