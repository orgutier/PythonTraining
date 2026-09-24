# Data Structures

Six exercises, two per tier. Every one is a small, realistic scenario combining several of that tier's specific tools at once -- from building a race-results ledger with tuples/zip/sort, through dataclass/namedtuple equality and set algebra, to the deque/defaultdict/Counter toolbox and, finally, exactly why __hash__ matters.

## Exercises

Each exercise below lives in its own folder with its own `solution.py` (the entry point) and `README.md` (the problem statement), and is independently testable with `python tools/cli.py test stage04_<name>` (e.g. `python tools/cli.py test stage04_basic01`). Work through them in order.

- **`basic01/`** -- list, tuple, append(), sort()/sorted(), zip(), enumerate(), len()
- **`basic02/`** -- dict, set, dict comprehension, list comprehension, zip(), len()
- **`mid01/`** -- dataclasses.dataclass, __eq__, collections module (namedtuple), dataclasses module, records
- **`mid02/`** -- set operations: union, intersection, difference
- **`advanced01/`** -- collections.defaultdict(), collections.Counter() x2, collections.deque() x2
- **`advanced02/`** -- __hash__, hashability -- automatic (frozen dataclass) and manual (__eq__ + __hash__ pair)
