"""
OOP II -- Composition and Swappable Engines
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage07_tier2_mid02.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage07/tier2_mid02/ and import it as a submodule (e.g.
`from exercises.stage07.tier2_mid02 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


class GasEngine:
    def start(self) -> str:
        """"Gas engine roaring to life..."."""
        raise NotImplementedError


class ElectricEngine:
    def start(self) -> str:
        """"Electric engine humming..."."""
        raise NotImplementedError


class Boat:
    def __init__(self, engine):
        """Store self.engine = engine (composition: Boat HAS an engine, doesn't extend one)."""
        raise NotImplementedError

    def start(self) -> str:
        """self.engine.start() -- delegates to whichever engine it holds."""
        raise NotImplementedError


def swap_engine(boat, new_engine) -> None:
    """boat.engine = new_engine -- swap behavior at runtime, no class hierarchy involved."""
    raise NotImplementedError
