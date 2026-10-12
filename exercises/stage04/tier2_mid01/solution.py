"""
Data Structures -- Player Records: Dataclass vs. namedtuple
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage04_tier2_mid01.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage04/tier2_mid01/ and import it as a submodule (e.g.
`from exercises.stage04.tier2_mid01 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


import collections
import dataclasses


@dataclasses.dataclass
class Player:
    name: str
    position: str


PlayerRecord = collections.namedtuple("PlayerRecord", ["name", "position"])


def convert_to_record(player: Player) -> PlayerRecord:
    """PlayerRecord(player.name, player.position)."""
    raise NotImplementedError


def players_are_equal(a: Player, b: Player) -> bool:
    """a == b -- relies on @dataclasses.dataclass's auto-generated __eq__ (field-based, not identity)."""
    raise NotImplementedError


def records_are_equal(a: PlayerRecord, b: PlayerRecord) -> bool:
    """a == b -- namedtuple's field-based equality, inherited from tuple."""
    raise NotImplementedError
