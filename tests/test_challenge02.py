from challenges.challenge02.solution import LRUCache


def test_basic_get_and_put():
    cache = LRUCache(2)
    cache.put("a", 1)
    cache.put("b", 2)
    assert cache.get("a") == 1
    assert cache.get("b") == 2


def test_get_on_missing_key_returns_negative_one():
    cache = LRUCache(2)
    assert cache.get("missing") == -1


def test_eviction_of_least_recently_used():
    cache = LRUCache(2)
    cache.put("a", 1)
    cache.put("b", 2)
    cache.get("a")          # "a" is now most-recently-used
    cache.put("c", 3)       # over capacity -> evicts "b" (least recently used)
    assert cache.get("b") == -1
    assert cache.get("a") == 1
    assert cache.get("c") == 3


def test_put_on_existing_key_updates_value_without_extra_eviction():
    cache = LRUCache(2)
    cache.put("a", 1)
    cache.put("b", 2)
    cache.put("a", 100)     # update, not a new entry
    assert cache.get("a") == 100
    assert cache.get("b") == 2  # still present -- capacity wasn't exceeded


def test_zero_capacity_stores_nothing():
    cache = LRUCache(0)
    cache.put("a", 1)
    assert cache.get("a") == -1


def test_eviction_order_with_three_keys():
    cache = LRUCache(3)
    cache.put("a", 1)
    cache.put("b", 2)
    cache.put("c", 3)
    cache.get("a")           # order (MRU->LRU): a, c, b
    cache.put("d", 4)        # evicts "b"
    assert cache.get("b") == -1
    assert cache.get("a") == 1
    assert cache.get("c") == 3
    assert cache.get("d") == 4
