# Data Structures

Six exercises, two per tier. Every one is a small, realistic scenario combining several of that tier's specific tools at once -- from building a race-results ledger with tuples/zip/sort, through dataclass/namedtuple equality and set algebra, to the deque/defaultdict/Counter toolbox and, finally, exactly why __hash__ matters.

## Exercises

Each exercise below lives in its own folder with its own `solution.py` (the entry point) and `README.md` (the problem statement), and is independently testable with `python tools/cli.py test stage04_<name>` (e.g. `python tools/cli.py test stage04_tier1_basic01`). Work through them in order.

- **`tier1_basic01/`** -- list, tuple, append(), sort()/sorted(), zip(), enumerate(), len()
- **`tier1_basic02/`** -- dict, set, dict comprehension, list comprehension, zip(), len()
- **`tier2_mid01/`** -- dataclasses.dataclass, __eq__, collections module (namedtuple), dataclasses module, records
- **`tier2_mid02/`** -- set operations: union, intersection, difference
- **`tier3_advanced01/`** -- collections.defaultdict(), collections.Counter() x2, collections.deque() x2
- **`tier3_advanced02/`** -- __hash__, hashability -- automatic (frozen dataclass) and manual (__eq__ + __hash__ pair)
- **`tier4_testing/`** -- manual, framework-free verification -- your own check() helper, no assert, no pytest
