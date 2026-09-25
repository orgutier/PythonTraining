# Functions

Six exercises, two per tier. Every one is function-based -- Stage 3's whole subject is writing functions, so (unlike Stage 1/2) there's no reason to dodge `def` here. Each exercise is a small, realistic scenario combining several of that tier's specific tools at once.

## Exercises

Each exercise below lives in its own folder with its own `solution.py` (the entry point) and `README.md` (the problem statement), and is independently testable with `python tools/cli.py test stage03_<name>` (e.g. `python tools/cli.py test stage03_tier1_basic01`). Work through them in order.

- **`tier1_basic01/`** -- def, return, ->, default args, *args, **kwargs
- **`tier1_basic02/`** -- basic recursion, lambda, return type hints
- **`tier2_mid01/`** -- closures, keyword-only args, positional-only params, docstrings & introspection
- **`tier2_mid02/`** -- a simple decorator, closures, keyword-only args (a different scenario)
- **`tier3_advanced01/`** -- functools.wraps, functools.lru_cache, functools.partial
- **`tier3_advanced02/`** -- yield / generator functions, global + LEGB scoping, the mutable-default-argument bug
