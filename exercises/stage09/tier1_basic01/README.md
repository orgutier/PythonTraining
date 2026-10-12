# Config File Manager

A small JSON-backed config store, one file per named config, all living in one directory. Implement:

- `config_path(directory: str, name: str) -> str` -- `os.path.join(directory, name + ".json")`.
- `config_exists(directory: str, name: str) -> bool` -- `os.path.exists(config_path(directory, name))`.
- `save_config(directory: str, name: str, data: dict) -> None` -- `with open(config_path(directory, name), "w") as f: json.dump(data, f)`.
- `load_config(directory: str, name: str) -> dict` -- `with open(config_path(directory, name)) as f: return json.load(f)`.
- `list_config_names(directory: str) -> list[str]` -- `sorted(f[:-5] for f in os.listdir(directory) if f.endswith(".json"))` (strip the `.json` suffix off each matching filename).

See the Study Reference presentation, Topic 9 (Basic tier), for the theory.
