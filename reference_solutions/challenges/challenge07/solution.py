# get_min() is O(1): a second stack (_mins) tracks the minimum seen so
# far at each depth, pushed/popped in lockstep with the main stack, so
# the current minimum is always just _mins[-1] -- no scanning required.
class MinStack:
    """
    A stack supporting push/pop/top/get_min all in O(1) time, backed by
    a second "running minimum" stack kept in lockstep with the main one.

    Edge cases handled:
      - Emptying the stack (pop() down to nothing) and pushing again:
        _mins empties out along with _items, so the next push starts a
        fresh running minimum rather than reusing a stale one.
      - Duplicate minimum values (e.g. push -3 twice, then pop once):
        each push records the min *as of that push* in _mins, so popping
        one -3 correctly reveals the other -3 was still the min, instead
        of losing track of it.
      - A single-element stack: get_min() and top() both just read that
        one element, which naturally falls out of the same logic.
    """

    def __init__(self) -> None:
        self._items: list[int] = []
        self._mins: list[int] = []

    def push(self, val: int) -> None:
        self._items.append(val)
        if not self._mins or val < self._mins[-1]:
            self._mins.append(val)
        else:
            self._mins.append(self._mins[-1])

    def pop(self) -> None:
        self._items.pop()
        self._mins.pop()

    def top(self) -> int:
        return self._items[-1]

    def get_min(self) -> int:
        return self._mins[-1]
