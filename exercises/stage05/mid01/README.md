# Order Validation Pipeline

Implement a small order-processing pipeline with a two-level custom exception hierarchy:

```python
class OrderError(Exception): pass
class OrderValidationError(OrderError): pass  # bad input
class OrderProcessingError(OrderError): pass  # bad business state
```

Implement:

- `parse_order_quantity(raw: str) -> int` -- `try: qty = int(raw)` `except ValueError as e: raise OrderValidationError(f"invalid quantity: {raw!r}") from e` (chained -- there's a real underlying `ValueError` to point to). Then, separately, if `qty <= 0`: `raise OrderValidationError(f"quantity must be positive: {qty}")` (no `from` here -- this isn't wrapping another exception, it's a fresh validation failure). Otherwise return `qty`.
- `apply_bulk_discount(quantity: int, discount_pct_raw: str) -> float` -- `try: pct = float(discount_pct_raw)` `except ValueError as e: raise OrderProcessingError(f"invalid discount: {discount_pct_raw!r}") from e`. Then if `not (0 <= pct <= 100)`: `raise OrderProcessingError(f"discount out of range: {pct}") from None` -- `from None` **explicitly suppresses** chaining (there's no underlying exception here, just an out-of-range value). Otherwise return `quantity * (1 - pct / 100)`.
- `fulfill_order(quantity: int, stock: int) -> int` -- if `quantity > stock`: `raise OrderProcessingError(f"insufficient stock: need {quantity}, have {stock}")`; otherwise return `stock - quantity`.

The chained exception is available afterward as `exc.__cause__` (`None` when `from None` was used) -- that's what the tests check, along with `OrderValidationError`/`OrderProcessingError` both being `OrderError` subclasses.

See the Study Reference presentation, Topic 5 (Mid tier), for the theory.
