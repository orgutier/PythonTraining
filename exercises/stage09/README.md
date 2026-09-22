# OS, JSON, Datetime, XML

Seven exercises tour the everyday stdlib modules from Topic 9 -- filesystem access two ways (os.path and pathlib), JSON round-tripping and custom encoding, naive vs. timezone-aware datetimes, and parsing/building XML with ElementTree -- each at least three times.

## Exercises

Each exercise below lives in its own folder with its own `solution.py` (the entry point) and `README.md` (the problem statement), and is independently testable with `python tools/cli.py test stage09_exerciseXX`. Work through them in order.

- **`exercise01/`** -- os.listdir, os.path x2, pathlib.Path x2
- **`exercise02/`** -- os.walk() x3, pathlib.Path glob
- **`exercise03/`** -- json.load/dump x2, json.loads/dumps
- **`exercise04/`** -- json.dumps(default=...) x3
- **`exercise05/`** -- datetime.now()/isoformat(), strftime, fromisoformat, arithmetic
- **`exercise06/`** -- datetime.now() x2 more, isoformat x1 more, timezone-aware vs naive
- **`exercise07/`** -- ElementTree.parse/findall x3, building XML
