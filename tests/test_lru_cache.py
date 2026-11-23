import pytest

from structures.lru_cache import LRUCache


def test_bad_capacity():
    with pytest.raises(ValueError):
        LRUCache(0)


def test_put_and_get():
    c = LRUCache(2)
    c.put("a", 1)
    c.put("b", 2)
    assert c.get("a") == 1
    assert c.get("b") == 2


def test_get_missing():
    c = LRUCache(2)
    assert c.get("нет") is None


def test_evicts_oldest():
    c = LRUCache(2)
    c.put("a", 1)
    c.put("b", 2)
    c.put("c", 3)  # места нет, выкидывается "a"
    assert c.get("a") is None
    assert c.get("b") == 2
    assert c.get("c") == 3
    assert len(c) == 2


def test_get_makes_item_fresh():
    c = LRUCache(2)
    c.put("a", 1)
    c.put("b", 2)
    c.get("a")      # теперь "a" свежее, чем "b"
    c.put("c", 3)   # выкидывается "b"
    assert c.get("b") is None
    assert c.get("a") == 1
    assert c.get("c") == 3


def test_put_existing_updates_value_and_freshness():
    c = LRUCache(2)
    c.put("a", 1)
    c.put("b", 2)
    c.put("a", 100)  # обновили "a", она свежая
    c.put("c", 3)    # выкидывается "b"
    assert c.get("a") == 100
    assert c.get("b") is None
    assert len(c) == 2


def test_order_of_keys():
    c = LRUCache(3)
    c.put(1, "a")
    c.put(2, "b")
    c.put(3, "c")
    assert c.keys_by_recent() == [3, 2, 1]
    c.get(1)
    assert c.keys_by_recent() == [1, 3, 2]


def test_capacity_one():
    c = LRUCache(1)
    c.put("a", 1)
    c.put("b", 2)
    assert c.get("a") is None
    assert c.get("b") == 2


def test_stores_none_value():
    # значение None тоже должно храниться
    c = LRUCache(2)
    c.put("a", None)
    assert c.get("a") is None
    assert len(c) == 1


def test_many_operations():
    c = LRUCache(3)
    for i in range(10):
        c.put(i, i)
    # должны остаться последние три
    assert c.keys_by_recent() == [9, 8, 7]
    assert c.get(5) is None
    assert c.get(7) == 7
