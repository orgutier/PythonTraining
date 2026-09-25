# Mixins

Implement two **mixins** -- small classes meant to be combined with others via multiple inheritance, each adding one focused piece of reusable behavior, never instantiated on their own:

- `LoggingMixin.log(self, message: str) -> str` -- `f"[{self.__class__.__name__}] {message}"`.
- `SerializableMixin.to_dict(self) -> dict` -- `dict(self.__dict__)`.
- `Widget(LoggingMixin, SerializableMixin)` -- `__init__(self, name)` stores `self.name`. `Widget` gets both `.log()` and `.to_dict()` for free by combining the two mixins -- no shared "is-a" hierarchy needed beyond the mixins themselves, just behavior composed in through multiple inheritance.

Note `self.__class__.__name__` inside `LoggingMixin.log` -- because it reads the *actual* class of whatever instance calls it (`"Widget"`), not `"LoggingMixin"`, the same mixin code produces a correctly-labeled message no matter which class mixes it in.

See the Study Reference presentation, Topic 7 (Advanced tier), for the theory.
