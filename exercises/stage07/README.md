# OOP II

Six exercises, two per tier: inheritance/super()/polymorphism contrasted with duck typing in Basic, abstract base classes contrasted with composition's runtime flexibility in Mid, and mixins plus a runtime_checkable Protocol in Advanced.

## Exercises

Each exercise below lives in its own folder with its own `solution.py` (the entry point) and `README.md` (the problem statement), and is independently testable with `python tools/cli.py test stage07_<name>` (e.g. `python tools/cli.py test stage07_basic01`). Work through them in order.

- **`basic01/`** -- class Child(Parent), super(), polymorphism, duck typing (side by side)
- **`basic02/`** -- super() (three-level chain), isinstance(), typing module, polymorphism
- **`mid01/`** -- abc module, ABC, @abstractmethod
- **`mid02/`** -- composition vs inheritance
- **`advanced01/`** -- mixins (multiple inheritance for composed-in behavior)
- **`advanced02/`** -- typing.Protocol, @runtime_checkable, isinstance() (structural)
