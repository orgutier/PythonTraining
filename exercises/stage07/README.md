# OOP II

Six exercises, two per tier: inheritance/super()/polymorphism contrasted with duck typing in Basic, abstract base classes contrasted with composition's runtime flexibility in Mid, and mixins plus a runtime_checkable Protocol in Advanced.

## Exercises

Each exercise below lives in its own folder with its own `solution.py` (the entry point) and `README.md` (the problem statement), and is independently testable with `python tools/cli.py test stage07_<name>` (e.g. `python tools/cli.py test stage07_tier1_basic01`). Work through them in order.

- **`tier1_basic01/`** -- class Child(Parent), super(), polymorphism, duck typing (side by side)
- **`tier1_basic02/`** -- super() (three-level chain), isinstance(), typing module, polymorphism
- **`tier2_mid01/`** -- abc module, ABC, @abstractmethod
- **`tier2_mid02/`** -- composition vs inheritance
- **`tier3_advanced01/`** -- mixins (multiple inheritance for composed-in behavior)
- **`tier3_advanced02/`** -- typing.Protocol, @runtime_checkable, isinstance() (structural)
- **`tier4_testing/`** -- manual, framework-free verification -- your own check() helper, no assert, no pytest
