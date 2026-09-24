class OrderError(Exception):
    pass


class OrderValidationError(OrderError):
    pass


class OrderProcessingError(OrderError):
    pass


def parse_order_quantity(raw: str) -> int:
    try:
        qty = int(raw)
    except ValueError as e:
        raise OrderValidationError(f"invalid quantity: {raw!r}") from e
    if qty <= 0:
        raise OrderValidationError(f"quantity must be positive: {qty}")
    return qty


def apply_bulk_discount(quantity: int, discount_pct_raw: str) -> float:
    try:
        pct = float(discount_pct_raw)
    except ValueError as e:
        raise OrderProcessingError(f"invalid discount: {discount_pct_raw!r}") from e
    if not (0 <= pct <= 100):
        raise OrderProcessingError(f"discount out of range: {pct}") from None
    return quantity * (1 - pct / 100)


def fulfill_order(quantity: int, stock: int) -> int:
    if quantity > stock:
        raise OrderProcessingError(f"insufficient stock: need {quantity}, have {stock}")
    return stock - quantity
