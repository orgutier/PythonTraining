# Rectangle Properties

Implement `Rectangle`:

- `__init__(self, width: float, height: float)` -- set both *through the properties* below (`self.width = width`, `self.height = height`), so construction validates them the same way a later assignment would.
- `width` / `height` (`@property` + `@width.setter` / `@height.setter`) -- getters return `self._width`/`self._height`; setters `raise ValueError` for any value `<= 0`, else store it.
- `area` (`@property`, read-only, no setter) -- `self.width * self.height`.
- `perimeter` (`@property`, read-only) -- `2 * (self.width + self.height)`.
- `is_square` (`@property`, read-only) -- `self.width == self.height`.

`area`/`perimeter`/`is_square` are *computed* properties -- there's nothing to set, they're derived fresh from `width`/`height` on every access, which is exactly why they're read-only (no setter defined at all).

See the Study Reference presentation, Topic 6, for the theory.
