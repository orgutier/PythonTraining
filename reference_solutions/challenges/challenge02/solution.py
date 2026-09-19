class _Node:
    def __init__(self, key: str, value: int) -> None:
        self.key = key
        self.value = value
        self.prev: "_Node | None" = None
        self.next: "_Node | None" = None


# get() and put() are both O(1): the dict gives O(1) key -> node lookup,
# and the doubly linked list gives O(1) removal/insertion at either end
# without shifting any other element (unlike a list, which would need an
# O(n) scan and shift to move an item to the front).
class LRUCache:
    """
    Fixed-capacity least-recently-used cache backed by a dict (key -> node)
    plus a hand-built doubly linked list ordered most-recently-used (head)
    to least-recently-used (tail).

    Edge cases handled:
      - capacity <= 0: nothing is ever stored; get() always returns -1 and
        put() is a no-op.
      - get() on a key that was never inserted (or was evicted) -> -1,
        and it does not disturb the recency order.
      - put() on a key that already exists -> updates its value in place,
        moves it to most-recently-used, and does NOT count against
        capacity a second time (the cache's size doesn't change).
      - Eviction ties: when multiple keys are equally "old", the one that
        became least-recently-used first is evicted first, because the
        list's tail always holds the single actual least-recently-used
        entry -- there's no ambiguity by construction.
    """

    def __init__(self, capacity: int) -> None:
        self._capacity = max(capacity, 0)
        self._nodes: dict[str, _Node] = {}
        # Sentinel head/tail nodes remove all the "is this the first/last
        # real node" edge cases from insert/remove.
        self._head = _Node("", 0)
        self._tail = _Node("", 0)
        self._head.next = self._tail
        self._tail.prev = self._head

    def get(self, key: str) -> int:
        """Return the value for key, or -1 if not present. Counts as a use."""
        node = self._nodes.get(key)
        if node is None:
            return -1
        self._move_to_front(node)
        return node.value

    def put(self, key: str, value: int) -> None:
        """Insert or update key. Counts as a use. Evict the LRU key if over capacity."""
        if self._capacity == 0:
            return

        existing = self._nodes.get(key)
        if existing is not None:
            existing.value = value
            self._move_to_front(existing)
            return

        if len(self._nodes) >= self._capacity:
            lru = self._tail.prev
            assert lru is not None and lru is not self._head
            self._remove(lru)
            del self._nodes[lru.key]

        node = _Node(key, value)
        self._nodes[key] = node
        self._insert_at_front(node)

    def __repr__(self) -> str:
        items = []
        node = self._head.next
        while node is not None and node is not self._tail:
            items.append(f"{node.key}={node.value}")
            node = node.next
        return f"LRUCache(capacity={self._capacity}, mru_to_lru=[{', '.join(items)}])"

    def _remove(self, node: _Node) -> None:
        prev_node, next_node = node.prev, node.next
        assert prev_node is not None and next_node is not None
        prev_node.next = next_node
        next_node.prev = prev_node

    def _insert_at_front(self, node: _Node) -> None:
        first = self._head.next
        assert first is not None
        node.prev = self._head
        node.next = first
        self._head.next = node
        first.prev = node

    def _move_to_front(self, node: _Node) -> None:
        self._remove(node)
        self._insert_at_front(node)
