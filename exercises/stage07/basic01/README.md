# Animal Sounds: Inheritance and Duck Typing

Two different mechanisms for "the same call does the right thing for different types" -- inheritance-based, and duck-typed. Implement:

- `Animal.__init__(self, name: str)` -- store `self.name`.
- `Animal.speak(self) -> str` -- `raise NotImplementedError` (the base class defines the *interface*, not a default behavior -- every subclass must override this).
- `Dog(Animal)` -- `speak(self) -> str` returns `f"{self.name} says Woof!"`.
- `Cat(Animal)` -- `__init__(self, name, indoor=True)` calls `super().__init__(name)` then stores `self.indoor`; `speak(self) -> str` returns `f"{self.name} says Meow!"`.
- `describe_animal(animal) -> str` -- `return animal.speak()`. Works for any `Animal` subclass -- **polymorphism** through a shared base class.

Now the duck-typed version, with **no shared base class at all**:

- `Duck.quack(self) -> str` -- `"Quack!"`.
- `Person.quack(self) -> str` -- `"I'm quacking like a duck!"`. `Duck` and `Person` share nothing in common.
- `make_it_quack(obj) -> str` -- `obj.quack()`. This works for *any* object with a `.quack()` method -- **duck typing**: "if it quacks like a duck, treat it like a duck," no inheritance required. Compare it with `describe_animal` above: both get "the right behavior for the type passed in", but one relies on a shared `Animal` base class and the other relies on nothing but a matching method name.

See the Study Reference presentation, Topic 7 (Basic tier), for the theory.
