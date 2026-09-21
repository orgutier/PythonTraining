import pytest
from challenges.challenge11.solution import LRUCache


def test_basic_get_put_and_eviction():
    cache = LRUCache(2)
    cache.put("a", 1)
    cache.put("b", 2)
    assert cache.get("a") == 1
    cache.put("c", 3)
    assert cache.get("b") == -1
    assert cache.get("c") == 3


def test_capacity_one_every_put_evicts():
    cache = LRUCache(1)
    cache.put("a", 1)
    cache.put("b", 2)
    assert cache.get("a") == -1
    assert cache.get("b") == 2


def test_updating_existing_key_does_not_grow_size():
    cache = LRUCache(2)
    cache.put("a", 1)
    cache.put("a", 100)
    cache.put("b", 2)
    cache.put("c", 3)
    assert cache.get("a") == -1  # a was LRU after update+b+c, should be evicted


def test_hit_rate():
    cache = LRUCache(2)
    cache.put("a", 1)
    cache.get("a")
    cache.get("missing")
    assert cache.hit_rate == 0.5


def test_hit_rate_zero_before_any_get():
    cache = LRUCache(2)
    assert cache.hit_rate == 0.0


def test_capacity_descriptor_validates():
    cache = LRUCache(2)
    with pytest.raises(ValueError):
        cache.capacity = -1
    with pytest.raises(ValueError):
        LRUCache(0)


def test_capacity_can_be_increased_via_descriptor():
    cache = LRUCache(1)
    cache.put("a", 1)
    cache.capacity = 3
    cache.put("b", 2)
    cache.put("c", 3)
    assert cache.get("a") == 1  # still present -- capacity grew before b/c were added


def test_is_valid_capacity_static():
    assert LRUCache.is_valid_capacity(5) is True
    assert LRUCache.is_valid_capacity(True) is False
    assert LRUCache.is_valid_capacity(-1) is False


def test_with_initial_items_classmethod():
    cache = LRUCache.with_initial_items(2, {"a": 1, "b": 2})
    assert cache.get("a") == 1
    assert cache.get("b") == 2


def test_total_caches_created_shared_across_instances():
    before = LRUCache.total_caches_created
    LRUCache(1)
    LRUCache(1)
    assert LRUCache.total_caches_created == before + 2


def test_slots_rejects_new_attribute():
    cache = LRUCache(1)
    with pytest.raises(AttributeError):
        cache.some_new_attr = 1
