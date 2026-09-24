"""
OOP I -- Slotted Records
Implement the function(s)/class(es) below.

IMPORTANT: do not add an `if __name__ == "__main__":` block to this file.
It must stay a plain importable module -- the test suite in
tests/test_stage06_mid02.py imports directly from here. Need a helper
function or class of your own? Add another .py file next to this one inside
exercises/stage06/mid02/ and import it as a submodule (e.g.
`from exercises.stage06.mid02 import helpers`) -- solution.py just has to
stay the entry point these tests import from.
"""


class TemperatureSlots:
    __slots__ = ("celsius",)

    def __init__(self, celsius):
        raise NotImplementedError

    def fahrenheit(self) -> float:
        """celsius * 9 / 5 + 32."""
        raise NotImplementedError


class InventoryItemSlots:
    __slots__ = ("name", "price", "quantity")

    def __init__(self, name, price, quantity):
        raise NotImplementedError

    def total_value(self) -> float:
        """round(price * quantity, 2)."""
        raise NotImplementedError
