class _Node:
    __slots__ = ("key", "value", "prev", "next")

    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class PositiveInt:
    def __set_name__(self, owner, name):
        self._name = "_" + name

    def __get__(self, obj, objtype=None):
        return getattr(obj, self._name)

    def __set__(self, obj, value):
        if not (isinstance(value, int) and not isinstance(value, bool) and value > 0):
            raise ValueError(f"{self._name[1:]} must be a positive int, got {value!r}")
        setattr(obj, self._name, value)


class LRUCache:
    __slots__ = ("_capacity", "_map", "_head", "_tail", "_hits", "_misses")

    capacity = PositiveInt()
    total_caches_created = 0

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self._map = {}
        self._head = _Node()
        self._tail = _Node()
        self._head.next = self._tail
        self._tail.prev = self._head
        self._hits = 0
        self._misses = 0
        LRUCache.total_caches_created += 1

    @staticmethod
    def is_valid_capacity(value) -> bool:
        return isinstance(value, int) and not isinstance(value, bool) and value > 0

    @property
    def hit_rate(self) -> float:
        total = self._hits + self._misses
        return self._hits / total if total else 0.0

    @classmethod
    def with_initial_items(cls, capacity: int, items: dict) -> "LRUCache":
        cache = cls(capacity)
        for key, value in items.items():
            cache.put(key, value)
        return cache

    def _insert_at_front(self, node):
        node.prev = self._head
        node.next = self._head.next
        self._head.next.prev = node
        self._head.next = node

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _move_to_front(self, node):
        self._remove(node)
        self._insert_at_front(node)

    def _evict_lru(self):
        lru = self._tail.prev
        if lru is self._head:
            return
        self._remove(lru)
        del self._map[lru.key]

    def get(self, key) -> int:
        if key not in self._map:
            self._misses += 1
            return -1
        self._hits += 1
        node = self._map[key]
        self._move_to_front(node)
        return node.value

    def put(self, key, value) -> None:
        if key in self._map:
            node = self._map[key]
            node.value = value
            self._move_to_front(node)
            return
        if len(self._map) >= self.capacity:
            self._evict_lru()
        node = _Node(key, value)
        self._map[key] = node
        self._insert_at_front(node)
