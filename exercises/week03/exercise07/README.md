# Signature Styles

Implement four functions using Python's `/` and `*` signature markers:

- `compute_area(length, width, *, unit="m") -> str` -- return `f"{length * width}{unit}^2"`. `unit` is **keyword-only** (it comes after the bare `*`): `compute_area(2, 3, "cm")` must raise `TypeError`; `compute_area(2, 3, unit="cm")` must work.
- `divide(a, b, /, *, precision=2) -> float` -- return `round(a / b, precision)`. `a`/`b` are **positional-only** (before the `/`); `precision` is keyword-only.
- `connect(host, port, /, *, timeout=30, retries=3) -> dict` -- return `{"host": host, "port": port, "timeout": timeout, "retries": retries}`. Same pattern, two positional-only and two keyword-only parameters.
- `scale_point(x, y, /, factor=1.0) -> tuple` -- return `(x * factor, y * factor)`. `x`/`y` are positional-only; `factor` is a normal parameter (callable either positionally or by keyword) -- not everything after `/` has to also be after `*`.

See the Study Reference presentation, Topic 3, for the theory.
