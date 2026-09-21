# Decorators

Implement three decorators, each preserving the wrapped function's `__name__`/`__doc__` with `functools.wraps`:

- `log_calls(func)` -- wraps `func` so `wrapper.calls` counts how many times it's been called (start it at `0`, increment inside the wrapper, still call and return `func(*args, **kwargs)`).
- `count_calls(func)` -- same idea, but track the count in a closure variable (`nonlocal`) instead of an attribute, exposed as a zero-arg `wrapper.call_count()` method you attach after defining `wrapper`.
- `uppercase_result(func)` -- call `func`, and if the result is a `str`, return it `.upper()`-ed; otherwise return it unchanged.

Every wrapper must be decorated with `@functools.wraps(func)` so `wrapper.__name__`/`wrapper.__doc__` still report the *original* function's name and docstring, not `"wrapper"`.

See the Study Reference presentation, Topic 3, for the theory.
