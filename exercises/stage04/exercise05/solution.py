"""
Data Structures -- Dataclasses
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage04_exercise05.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage04/exercise05/ and import it as a submodule (e.g.
`from exercises.stage04.exercise05 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


import dataclasses


@dataclasses.dataclass
class Point:
    x: int
    y: int

    def distance_from_origin(self) -> float:
        """(x**2 + y**2) ** 0.5."""
        raise NotImplementedError


@dataclasses.dataclass(frozen=True)
class FrozenPoint:
    x: int
    y: int

    def distance_from_origin(self) -> float:
        """(x**2 + y**2) ** 0.5."""
        raise NotImplementedError


@dataclasses.dataclass
class TaggedItem:
    name: str
    tags: list = dataclasses.field(default_factory=list)

    def add_tag(self, tag: str) -> None:
        """self.tags.append(tag)."""
        raise NotImplementedError
