# Generator-Based Context Managers

Implement three `@contextlib.contextmanager`-decorated generator functions -- the lighter-weight alternative to writing a full `__enter__`/`__exit__` class:

- `temporary_value(obj, attr, value)` -- save `getattr(obj, attr)`, `setattr(obj, attr, value)`, `yield`, then in a `finally:` restore the original value -- even if the `with`-block raised.
- `suppress_and_log(log: list, *exc_types)` -- `try: yield` `except exc_types as e: log.append(str(e))` (swallows a matching exception, recording it instead of letting it propagate).
- `timing_block(results: list)` -- record `time.time()` before `yield`; in a `finally:`, `results.append(time.time() - start)`.

Everything before the `yield` runs as `__enter__`; everything after (particularly inside a `finally:`) runs as `__exit__` -- a `try`/`finally` wrapped around a single `yield` is how `@contextlib.contextmanager` turns an ordinary generator function into a context manager, without writing a class at all.

See the Study Reference presentation, Topic 5 (Advanced tier), for the theory.
