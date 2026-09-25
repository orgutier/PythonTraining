# Generators, Scope & the Mutable-Default Trap

Implement:

- `batch_generator(items, batch_size)` -- a **generator function** (uses `yield`, not `return`) that yields successive slices of `items`, each of length `batch_size` (the last one may be shorter): `for i in range(0, len(items), batch_size): yield items[i:i + batch_size]`.
- `counter = 0` (module-level, already in the stub) and `increment_global()` -- uses `global counter`, increments it by `1`, and returns the new value.
- `make_local_shadow()` -- assigns a **local** variable also named `counter` set to `100` and returns it, **without** any `global` declaration. Because there's no `global`, this local assignment shadows the module-level `counter` inside this function only (LEGB: Python resolves the *assignment target* to a local name here) -- it must NOT change the module-level `counter`.
- `append_bad(item, target=[])` -- **deliberately buggy**: `target.append(item); return target`. Because the default `[]` is created once, at function-definition time, and reused on every call that doesn't pass its own `target`, repeated calls silently accumulate into the *same* list.
- `append_safe(item, target=None)` -- the fix: if `target is None: target = []`, then `target.append(item); return target`. A fresh list every time no `target` is supplied.

This exercise is specifically about the traps: reading `increment_global`/`make_local_shadow` side by side shows `global` vs. ordinary local shadowing, and `append_bad`/`append_safe` side by side shows the classic mutable-default-argument bug and its fix.

See the Study Reference presentation, Topic 3 (Advanced tier), for the theory.
