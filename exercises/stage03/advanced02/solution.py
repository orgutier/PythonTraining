"""
Functions -- Generators, Scope & the Mutable-Default Trap
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage03_advanced02.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage03/advanced02/ and import it as a submodule (e.g.
`from exercises.stage03.advanced02 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


counter = 0


def batch_generator(items, batch_size):
    """Generator: yield successive batch_size-length slices of items."""
    raise NotImplementedError


def increment_global() -> int:
    """global counter; increment it by 1 and return the new value."""
    raise NotImplementedError


def make_local_shadow() -> int:
    """Assign a LOCAL counter = 100 (no `global`) and return it; must NOT touch the module-level counter."""
    raise NotImplementedError


def append_bad(item, target=[]):
    """Deliberately buggy: target.append(item); return target. Demonstrates the mutable-default-argument trap."""
    raise NotImplementedError


def append_safe(item, target=None):
    """Fixed version: if target is None: target = []; then append/return. A fresh list per call."""
    raise NotImplementedError
