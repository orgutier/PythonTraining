# Inheritance Basics

Implement:

- `Animal.__init__(self, name: str)` -- store `self.name`.
- `Animal.speak(self) -> str` -- `raise NotImplementedError` (the base class defines the *interface*, not a default behavior -- every subclass must override this).
- `Dog(Animal)` -- `speak(self) -> str` returns `f"{self.name} says Woof!"`.
- `Cat(Animal)` -- `__init__(self, name, indoor=True)` calls `super().__init__(name)` then stores `self.indoor`; `speak(self) -> str` returns `f"{self.name} says Meow!"`.
- `describe_animal(animal) -> str` -- `return animal.speak()`. This function doesn't care whether `animal` is a `Dog`, a `Cat`, or anything else with a `.speak()` method -- that's **polymorphism**: the same call (`animal.speak()`) does the right thing for whatever type is actually passed in.

See the Study Reference presentation, Topic 7, for the theory.
