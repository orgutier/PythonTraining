# Challenge 14 — Shape Library with Protocols and Composition

**Do this after:** Week 07 (OOP II)
**Correctness is pytest-tested:** `python tools/cli.py test challenge14` (or `pytest tests/test_challenge14.py`). The constraints below on *how* you write it are not something pytest can check -- grade those yourself.

## Problem

A companion to Challenge 13: this one deliberately avoids a base-class
inheritance chain, to give the *other* half of Week 7's ideas -- structural
typing (`typing.Protocol`) and composition -- somewhere concrete to live.
`Circle` and `Rectangle` share **no** common base class at all; they're
related only by having matching methods.

Implement:

```python
@runtime_checkable
class Drawable(Protocol):
    def area(self) -> float: ...
    def perimeter(self) -> float: ...

class Circle:
    def __init__(self, radius: float) -> None: ...
    def area(self) -> float: ...
    def perimeter(self) -> float: ...

class Rectangle:
    def __init__(self, width: float, height: float) -> None: ...
    def area(self) -> float: ...
    def perimeter(self) -> float: ...

class CompositeShape:
    """Holds a list of Drawable-shaped objects -- composition, not inheritance."""
    def __init__(self, shapes: list) -> None: ...
    def area(self) -> float:
        """Sum of every held shape's area()."""
    def perimeter(self) -> float:
        """Sum of every held shape's perimeter()."""

def total_area(shapes: list) -> float:
    """Sum area() across every item in shapes that structurally IS a Drawable; non-conforming items are skipped, not errors."""

def largest_by_area(shapes: list):
    """The single shape (from a non-empty list of Drawables) with the largest area()."""
```

```python
c = Circle(2)
r = Rectangle(3, 4)
composite = CompositeShape([c, r])
composite.area()          # -> Circle's area + Rectangle's area
total_area([c, r, "not a shape", 42])   # -> same total, the non-shapes are skipped
largest_by_area([c, r])    # -> whichever of c/r has the bigger area()
isinstance(c, Drawable)    # -> True, even though Circle never mentions Drawable
```

## Constraints on HOW you write it

1. **`Circle` and `Rectangle` must not inherit from `Drawable` (or from
   each other, or from any shared base class).** They satisfy `Drawable`
   purely by having matching `area()`/`perimeter()` methods -- structural
   typing, not explicit inheritance.
2. **`Drawable` must be `@runtime_checkable`**, so `isinstance(x,
   Drawable)` actually works at runtime (a plain `Protocol` without this
   decorator only helps a static type checker, not `isinstance`).
3. **`CompositeShape` must hold its shapes as data** (`self.shapes =
   shapes`), computing `area()`/`perimeter()` by delegating to each held
   shape -- **composition**. It must not inherit from `Circle`,
   `Rectangle`, or any base shape class.
4. **`total_area` must use `isinstance(item, Drawable)`** to filter, not
   `hasattr(item, "area")` -- the whole point is exercising the
   `runtime_checkable` `Protocol`, not falling back to plain duck typing.
5. **`largest_by_area` must work uniformly across `Circle`, `Rectangle`,
   *and* `CompositeShape`** in the same list, calling nothing but
   `.area()` on each -- no `isinstance`/`type()` branching inside it. That
   uniform handling *is* polymorphism.
6. **A docstring on `total_area`** listing edge cases: an empty `shapes`
   list (`0.0`), and a list containing only non-`Drawable` items (also
   `0.0`, not an error).
