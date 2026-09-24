# Order Total Calculator

Implement two order-pricing helpers:

- `compute_total(*item_prices, tax_rate=0.08, **surcharges) -> float` -- `item_prices` is any number of positional prices (via `*args`); `tax_rate` is a keyword argument with a default of `0.08`; `surcharges` collects any number of extra named fees (via `**kwargs`, e.g. `shipping=5`, `handling=2`). Return `round(subtotal + tax + sum(surcharges.values()), 2)`, where `subtotal = sum(item_prices)` and `tax = subtotal * tax_rate`.
- `apply_discount(price, pct=0.10) -> float` -- return `round(price * (1 - pct), 2)`. `pct` defaults to `0.10` (a 10% discount) but can be overridden.

Both functions need a `-> float` return type hint on their signature, and `compute_total` must genuinely accept a variable number of prices and surcharges -- don't hardcode a fixed parameter list.

See the Study Reference presentation, Topic 3 (Basic tier), for the theory.
