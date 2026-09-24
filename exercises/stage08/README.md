# The Python Data Model

Six exercises, two per tier: the everyday trio (__repr__/__str__/__eq__) in Basic, a card-deck-style collection protocol plus callables in Mid, and operator overloading's __radd__/__hash__ pairing plus three context-manager classes with no shared base class in Advanced.

## Exercises

Each exercise below lives in its own folder with its own `solution.py` (the entry point) and `README.md` (the problem statement), and is independently testable with `python tools/cli.py test stage08_<name>` (e.g. `python tools/cli.py test stage08_basic01`). Work through them in order.

- **`basic01/`** -- __repr__, __str__, __eq__
- **`basic02/`** -- __repr__, __str__, __eq__ (a second scenario)
- **`mid01/`** -- __len__, __getitem__, __iter__, __contains__, __add__, operator overloading, protocols
- **`mid02/`** -- __contains__, __iter__, __bool__ (reinforced), __call__
- **`advanced01/`** -- __repr__/__eq__ (reinforced), __add__, __radd__, __hash__
- **`advanced02/`** -- __enter__, __exit__
