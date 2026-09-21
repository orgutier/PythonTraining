"""
The Python Data Model -- Context Managers as a Protocol
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the aggregated test suite in
tests/test_week08.py imports directly from here. Need a helper function or
class of your own? Add another .py file next to this one inside
exercises/week08/exercise07/ and import it as a submodule (e.g.
`from exercises.week08.exercise07 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


class ResourceGuard:
    def __enter__(self):
        """Set self.active = True; return self."""
        raise NotImplementedError

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Set self.active = False; return False."""
        raise NotImplementedError


class Transaction:
    def __enter__(self):
        """Set self.committed = self.rolled_back = False; return self."""
        raise NotImplementedError

    def __exit__(self, exc_type, exc_val, exc_tb):
        """committed=True if exc_type is None, else rolled_back=True. Return False."""
        raise NotImplementedError


class SuppressAll:
    def __enter__(self):
        raise NotImplementedError

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Always return True -- suppress any exception."""
        raise NotImplementedError
