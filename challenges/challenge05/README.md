# Challenge 05 — Pluggable Event Pipeline

**Do this after:** Week 03 (Functions)
**Correctness is pytest-tested:** `python tools/cli.py test challenge05` (or `pytest tests/test_challenge05.py`). The constraints below on *how* you write it are not something pytest can check -- grade those yourself.

## Problem

Plugin/handler registries built from closures and decorators are
everywhere in real Python codebases (web framework routes, CLI
subcommands, event buses). This challenge builds a tiny one, plus two
flavors of caching decorator, to pull together most of Week 3's function
toolkit in one place.

Implement:

```python
def make_pipeline():
    """Return (register, run): register(name) is a decorator that adds the decorated function as the handler for `name`; run(name, *args, **kwargs) calls that handler and returns its result, or raises KeyError if nothing is registered under `name`."""

def count_calls(func):
    """Decorator: wrapper.call_count tracks how many times func has been called."""

def memoize(func):
    """Decorator: cache func's results by its (args, kwargs), from scratch -- no functools.lru_cache here."""

def cached_expensive(n: int, *, precision: int = 2) -> float:
    """round(n ** 0.5, precision), decorated with functools.lru_cache(maxsize=None). precision is keyword-only."""
```

```python
register, run = make_pipeline()

@register("double")
def double(x):
    return x * 2

run("double", 5)     # -> 10
double.__name__       # -> "double"  (functools.wraps preserved it)
run("missing")        # -> raises KeyError
```

Each call to `make_pipeline()` must produce an **independent** registry --
registering a handler on one pipeline must not affect another.

## Constraints on HOW you write it

1. **`make_pipeline`'s handler storage must be a closure variable**
   (a local `dict` inside `make_pipeline`, captured by both `register` and
   `run`), not a module-level or class-level dict shared across calls to
   `make_pipeline()`.
2. **Every decorator here (`register`'s inner decorator, `count_calls`,
   `memoize`) must use `@functools.wraps(func)`** so the wrapped
   function's `__name__`/`__doc__` survive.
3. **`count_calls` must track its count in a closure variable updated with
   `nonlocal`**, not a mutable default argument or a function attribute
   incremented without `nonlocal` (that would raise `UnboundLocalError`).
4. **`memoize` must build the cache key from `(args, tuple(sorted(kwargs
   .items())))`** so it also works for keyword arguments, and must not use
   `functools.lru_cache` (that's what `cached_expensive` is for) --
   `memoize` is the "build it yourself" version.
5. **`cached_expensive`'s `precision` must be keyword-only** (`*` before
   it in the signature) and it must be decorated with
   `functools.lru_cache(maxsize=None)`.
6. **`run` must accept and forward arbitrary `*args`/`**kwargs`** to
   whatever handler is registered -- it has no idea what signature a
   given handler expects.
