"""
Data Structures -- League Membership Analyzer
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage04_tier2_mid02.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage04/tier2_mid02/ and import it as a submodule (e.g.
`from exercises.stage04.tier2_mid02 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


def both_conferences(east: set, west: set) -> set:
    """east & west -- intersection."""
    raise NotImplementedError


def all_players(east: set, west: set) -> set:
    """east | west -- union."""
    raise NotImplementedError


def east_only(east: set, west: set) -> set:
    """east - west -- difference."""
    raise NotImplementedError


def west_only(east: set, west: set) -> set:
    """west - east -- difference, other direction."""
    raise NotImplementedError


def symmetric_difference_manual(east: set, west: set) -> set:
    """(east - west) | (west - east) -- built from difference + union, not the `^` operator."""
    raise NotImplementedError
