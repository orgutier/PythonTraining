# functools Toolkit

Implement:

- `logged(fn)` -- a decorator whose `wrapper` is decorated with `@functools.wraps(fn)` (so it preserves `fn`'s `__name__`/`__doc__`) and simply forwards every call: `return fn(*args, **kwargs)`.
- `multiply(a, b)` -- a plain (undecorated) function, `"""Multiply two numbers."""`, returns `a * b`. It is deliberately **not** written as `@logged\ndef multiply(...)` in this file -- applying a still-unimplemented decorator with `@` syntax at import time would raise `NotImplementedError` immediately and crash the whole module. The tests instead call `logged(multiply)` themselves to check your decorator's behavior.
- `fib(n)` -- decorated with `@functools.lru_cache(maxsize=None)` (that decorator is already fully implemented by the standard library, so applying it at import time is safe), recursive Fibonacci (`n < 2` returns `n`, otherwise `fib(n - 1) + fib(n - 2)`).
- `add_ten` -- `functools.partial(lambda a, b: a + b, b=10)`, a callable that adds `10` to whatever single argument it's given.

Without `functools.wraps`, `logged(multiply).__name__` would be `"wrapper"` and its `__doc__` would be `None` -- the tests check exactly that this doesn't happen. Without `functools.lru_cache`, `fib(20)` would still be correct but `fib` wouldn't expose a `cache_info()` method.

See the Study Reference presentation, Topic 3 (Advanced tier), for the theory.
