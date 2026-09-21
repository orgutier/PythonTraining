# Duck Typing and Composition

Implement:

- `Engine.start(self) -> str` -- `"Engine starting..."`.
- `Boat.__init__(self, engine)` -- store `self.engine = engine` (a `Boat` **has an** `Engine` -- **composition**, not inheritance: `Boat` doesn't extend `Engine`, it just holds one). `start(self) -> str` -- `self.engine.start()`.
- `Duck.quack(self) -> str` -- `"Quack!"`.
- `Person.quack(self) -> str` -- `"I'm quacking like a duck!"`. `Duck` and `Person` share **no** base class in common.
- `make_it_quack(obj) -> str` -- `obj.quack()`. This works for *any* object with a `.quack()` method, `Duck` or `Person` or anything else -- **duck typing**: "if it quacks like a duck, treat it like a duck," no shared inheritance required.
- `is_duck_instance(obj) -> bool` -- `isinstance(obj, Duck)`. Unlike `make_it_quack`, this one *does* care about the actual type -- contrast the two.

See the Study Reference presentation, Topic 7, for the theory.
