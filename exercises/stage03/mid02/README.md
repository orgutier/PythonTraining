# Call-Counting Decorator + Validated Config

Implement:

- `count_calls(fn)` -- a **decorator**. Return a `wrapper(*args, **kwargs)` that calls `fn(*args, **kwargs)` and returns its result, while tracking how many times it's been called as `wrapper.calls` (start it at `0` right after defining `wrapper`, increment it on every call).
- `greet(name)` -- a plain (undecorated) function returning `"Hello, " + name`. It is deliberately **not** written as `@count_calls\ndef greet(...)` in this file -- applying a still-unimplemented decorator with `@` syntax at import time would raise `NotImplementedError` immediately and crash the whole module before you'd even get to run a single test. The tests instead call `count_calls(greet)` themselves to check your decorator's behavior, exactly as you'd call it by hand anywhere else.
- `make_validator(*, min_value, max_value=100)` -- `min_value` and `max_value` are **keyword-only**. Return a one-argument `validate(n)` **closure** that returns `True` iff `min_value <= n <= max_value`.

`count_calls` is the simplest possible decorator shape: wrap, track state on the wrapper itself, still forward every call through to the original function and its return value.

See the Study Reference presentation, Topic 3 (Mid tier), for the theory.
