# Files, Exceptions, Regex

Six exercises, two per tier: file I/O and everyday try/except/finally/raise plus basic regex in Basic; custom exception hierarchies with raise ... from ... chaining, and compiled named-group regex, in Mid; both ways to write a context manager -- a class with __enter__/__exit__, and @contextlib.contextmanager -- in Advanced.

## Exercises

Each exercise below lives in its own folder with its own `solution.py` (the entry point) and `README.md` (the problem statement), and is independently testable with `python tools/cli.py test stage05_<name>` (e.g. `python tools/cli.py test stage05_basic01`). Work through them in order.

- **`basic01/`** -- open(), with, as
- **`basic02/`** -- try, except, finally, raise, Exception, re.search(), re.findall(), re.match(), re.sub()
- **`mid01/`** -- exception hierarchies, exception chaining (raise ... from ...)
- **`mid02/`** -- re.compile(), regex named groups
- **`advanced01/`** -- __enter__/__exit__
- **`advanced02/`** -- @contextlib.contextmanager
