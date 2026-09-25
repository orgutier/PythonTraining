# OS, JSON, Datetime, XML

Six exercises, two per tier: a config-file manager (os.path + JSON) and a library catalog (datetime + XML) in Basic; pathlib as the modern os.path alternative, and timezone-aware timestamps serialized via a custom JSON encoder, in Mid; recursive directory traversal with os.walk() in Advanced.

## Exercises

Each exercise below lives in its own folder with its own `solution.py` (the entry point) and `README.md` (the problem statement), and is independently testable with `python tools/cli.py test stage09_<name>` (e.g. `python tools/cli.py test stage09_tier1_basic01`). Work through them in order.

- **`tier1_basic01/`** -- os.listdir, os.path, json.load/dump
- **`tier1_basic02/`** -- datetime.now/isoformat, ElementTree.parse/findall
- **`tier2_mid01/`** -- pathlib.Path, pathlib as the modern os.path alternative
- **`tier2_mid02/`** -- json.dumps(default=...), timezone-aware vs naive datetimes
- **`tier3_advanced01/`** -- os.walk()
- **`tier3_advanced02/`** -- os.walk() (two more scenarios)
