# Context Managers

Implement three class-based context managers and three generator-based ones:

- `Timer` -- `__enter__` records `self._start = time.time()` and returns `self`; `__exit__` sets `self.elapsed = time.time() - self._start` and returns `False` (never suppress).
- `SuppressErrors` -- `__init__(self, exc_type)` stores it; `__enter__` returns `None`; `__exit__(self, exc_type, exc_val, exc_tb)` returns `True` (suppress) only if an exception occurred **and** it's an instance of the stored type, else `False`.
- `FileLineCounter` -- `__init__(self, path)` stores it; `__enter__` opens the file and returns the file object; `__exit__` closes it and returns `False`. This is what `with open(...) as f:` does under the hood.

- `temporary_value(obj, attr, value)` (`@contextlib.contextmanager`) -- save `getattr(obj, attr)`, `setattr(obj, attr, value)`, `yield`, then in a `finally:` restore the original value -- even if the with-block raised.
- `suppress_and_log(log: list, *exc_types)` -- `try: yield` `except exc_types as e: log.append(str(e))` (swallows a matching exception, recording it instead of propagating).
- `timing_block(results: list)` -- record `time.time()` before `yield`; in a `finally:`, `results.append(time.time() - start)`.

See the Study Reference presentation, Topic 5, for the theory.
