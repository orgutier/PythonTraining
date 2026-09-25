"""
Data Structures -- Race Results Ledger
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage04_tier1_basic01.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage04/tier1_basic01/ and import it as a submodule (e.g.
`from exercises.stage04.tier1_basic01 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


def build_results(names: list[str], times: list[float]) -> list[tuple]:
    """[] then a for-loop over zip(names, times) .append()-ing each (name, time) tuple."""
    raise NotImplementedError


def rank_by_time(results: list[tuple]) -> list[tuple]:
    """sorted(results, key=lambda r: r[1]) -- fastest first, returns a NEW list."""
    raise NotImplementedError


def fastest_n(ranked_results: list[tuple], n: int) -> list[tuple]:
    """ranked_results[:n]."""
    raise NotImplementedError


def podium_labels(fastest: list[tuple]) -> list[str]:
    """[f"{i+1}. {name} ({time}s)" for i, (name, time) in enumerate(fastest)]."""
    raise NotImplementedError


def racer_count(names: list[str]) -> int:
    """len(names)."""
    raise NotImplementedError
