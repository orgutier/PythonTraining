# Context Managers as a Protocol

Implement three unrelated classes that all work in a `with` statement -- **none of them inherit from any special base class**. `with` works purely by looking for `__enter__`/`__exit__` *at runtime*: this is a **protocol** (structural, duck-typed), not explicit inheritance (unlike, say, Java's `Closeable` interface, which a class must formally implement):

- `ResourceGuard` -- `__enter__` sets `self.active = True` and returns `self`; `__exit__(self, exc_type, exc_val, exc_tb)` sets `self.active = False` and returns `False`.
- `Transaction` -- `__enter__` sets `self.committed = False` and `self.rolled_back = False`, returns `self`; `__exit__` sets `self.committed = True` if `exc_type is None` (the block finished cleanly), else sets `self.rolled_back = True` -- either way, returns `False` (never swallow the exception).
- `SuppressAll` -- `__enter__` returns `None`; `__exit__` **always** returns `True`, suppressing *any* exception raised inside the block, regardless of type.

See the Study Reference presentation, Topic 8, for the theory.
