# Rate-Limited Logger Factory + Clamp

Implement:

- `make_logger(*, prefix, max_entries=5)` -- `prefix` and `max_entries` are **keyword-only** (they come after the bare `*`). Return a one-argument `log(message)` **closure** that: appends `prefix + ": " + message` to an internal list, and if the list now has more than `max_entries` items, drops the *oldest* one (`entries.pop(0)`). Each call to `log(...)` returns a copy of the current list (`list(entries)`), so you can observe it growing (and the oldest entry rolling off once it's over capacity).
- `clamp(value, lo, hi, /) -> int|float` -- `value`, `lo`, `hi` are all **positional-only** (before the `/`). Return `lo` if `value < lo`, `hi` if `value > hi`, otherwise `value` unchanged.
- `function_signature_info(fn) -> dict` -- introspect any function and return `{"name": fn.__name__, "doc": fn.__doc__}`.

`make_logger`'s inner `log` function is a genuine closure: it must keep reading and mutating the *same* `entries` list across calls, defined once per `make_logger(...)` call (a fresh list each time `make_logger` itself is called).

See the Study Reference presentation, Topic 3 (Mid tier), for the theory.
