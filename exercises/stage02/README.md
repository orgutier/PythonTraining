# Control Flow

Six exercises, two per tier, plus no separate setup exercise (Stage 1 already covered that). Every one is a small scenario -- a grid scan, a bus manifest, a restock check, a round-robin scheduler -- that forces combining several of that tier's control-flow tools at once, not a single isolated demo.

## Exercises

Each exercise below lives in its own folder with its own `solution.py` (the entry point) and `README.md` (the problem statement), and is independently testable with `python tools/cli.py test stage02_<name>` (e.g. `python tools/cli.py test stage02_tier1_basic01`). Work through them in order.

- **`tier1_basic01/`** -- nested for + range(), if/elif/else, continue, pass, while + break
- **`tier1_basic02/`** -- while as the main loop, if/elif/else, break, continue, pass, nested for
- **`tier2_mid01/`** -- for...else, a short-circuit guard, a ternary, zip()
- **`tier2_mid02/`** -- while...else, a short-circuit guard, a ternary, zip() -- a different combination
- **`tier3_advanced01/`** -- a class implementing the iterator protocol (__iter__/__next__/StopIteration) by hand
- **`tier3_advanced02/`** -- itertools.chain + itertools.cycle + itertools.islice, combined
