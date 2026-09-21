"""
OOP II -- Inheritance Basics
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_week07_exercise01.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/week07/exercise01/ and import it as a submodule (e.g.
`from exercises.week07.exercise01 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


class Animal:
    def __init__(self, name: str):
        raise NotImplementedError

    def speak(self) -> str:
        """Base class defines the interface; subclasses must override."""
        raise NotImplementedError


class Dog(Animal):
    def speak(self) -> str:
        """f"{self.name} says Woof!"."""
        raise NotImplementedError


class Cat(Animal):
    def __init__(self, name: str, indoor: bool = True):
        """super().__init__(name), then store self.indoor."""
        raise NotImplementedError

    def speak(self) -> str:
        """f"{self.name} says Meow!"."""
        raise NotImplementedError


def describe_animal(animal) -> str:
    """animal.speak() -- works for any Animal subclass (polymorphism)."""
    raise NotImplementedError
