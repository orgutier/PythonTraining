# Class-Based Context Managers

Implement three class-based context managers:

- `Timer` -- `__enter__` records `self._start = time.time()` and returns `self`; `__exit__` sets `self.elapsed = time.time() - self._start` and returns `False` (never suppress an exception).
- `SuppressErrors` -- `__init__(self, exc_type)` stores it; `__enter__` returns `None`; `__exit__(self, exc_type, exc_val, exc_tb)` returns `True` (suppress) only if an exception occurred **and** it's a subclass of the stored type, else `False` (let it propagate).
- `FileLineCounter` -- `__init__(self, path)` stores it; `__enter__` opens the file and returns the file object; `__exit__` closes it and returns `False`. This is roughly what `with open(...) as f:` does under the hood.

A class-based context manager's `__exit__` receives `(exc_type, exc_val, exc_tb)` describing any exception that happened inside the `with` block (all `None` if nothing went wrong) -- returning a truthy value from `__exit__` is what swallows that exception instead of letting it propagate.

See the Study Reference presentation, Topic 5 (Advanced tier), for the theory.
