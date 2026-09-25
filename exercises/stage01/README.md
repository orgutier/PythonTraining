# Python Fundamentals

Seven small exercises, each in its own folder: tier0_hello_world (Setup), then two apiece for the Basic, Mid, and Advanced tiers. Every one is plain top-level code -- no function to implement -- since Stage 1 hasn't introduced `def` yet. Each is a small, self-contained scenario (never just "print this value") that forces you to actually combine that tier's tools, not just demonstrate one in isolation.

## Exercises

Each exercise below lives in its own folder with its own `solution.py` (the entry point) and `README.md` (the problem statement), and is independently testable with `python tools/cli.py test stage01_<name>` (e.g. `python tools/cli.py test stage01_tier0_hello_world`). Work through them in order.

- **`tier0_hello_world/`** -- print(), variable assignment, string concatenation -- confirms your environment and this repo's test runner both work
- **`tier1_basic01/`** -- explicit int()/float() casting, arithmetic operators, isinstance(), no f-strings yet
- **`tier1_basic02/`** -- // and % chained together, explicit bool-from-string casting (avoiding the bool(str) trap)
- **`tier2_mid01/`** -- operator precedence, chained comparisons, the walrus operator, f-strings, augmented assignment
- **`tier2_mid02/`** -- more precedence/walrus/chained-comparison/augmented-assignment practice, a different scenario
- **`tier3_advanced01/`** -- Decimal built from string (not float), math.isclose() vs ==, the classic 0.1+0.2 case
- **`tier3_advanced02/`** -- arbitrary-precision integers, small-int caching, string interning (and its limits)
