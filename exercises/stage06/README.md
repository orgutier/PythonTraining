# OOP I

Six exercises, two per tier: validated properties and classmethod alternate constructors in Basic, __slots__ across four small classes in Mid, and a hand-rolled descriptor (what @property is built on) in Advanced.

## Exercises

Each exercise below lives in its own folder with its own `solution.py` (the entry point) and `README.md` (the problem statement), and is independently testable with `python tools/cli.py test stage06_<name>` (e.g. `python tools/cli.py test stage06_tier1_basic01`). Work through them in order.

- **`tier1_basic01/`** -- class, self, __init__, @property, @x.setter, @staticmethod, encapsulation
- **`tier1_basic02/`** -- instance vs class attributes, @classmethod, cls, @staticmethod, @property (read-only)
- **`tier2_mid01/`** -- __slots__
- **`tier2_mid02/`** -- __slots__ (two more classes)
- **`tier3_advanced01/`** -- __get__/__set__, descriptors
- **`tier3_advanced02/`** -- __get__/__set__, descriptors (type-checking variant)
- **`tier4_testing/`** -- manual, framework-free verification -- your own check() helper, no assert, no pytest
