from structures.hash_table import HashTable


def test_empty():
    h = HashTable()
    assert len(h) == 0
    assert h.get("a") is None


def test_put_and_get():
    h = HashTable()
    h.put("a", 1)
    h.put("b", 2)
    assert h.get("a") == 1
    assert h.get("b") == 2
    assert len(h) == 2


def test_get_default():
    h = HashTable()
    assert h.get("нет", 0) == 0


def test_overwrite():
    h = HashTable()
    h.put("a", 1)
    h.put("a", 2)
    assert h.get("a") == 2
    assert len(h) == 1


def test_contains():
    h = HashTable()
    h.put(1, "x")
    assert h.contains(1)
    assert 1 in h
    assert 2 not in h


def test_remove():
    h = HashTable()
    h.put("a", 1)
    assert h.remove("a") is True
    assert h.get("a") is None
    assert len(h) == 0
    assert h.remove("a") is False


class BadKey:
    # у всех объектов этого класса одинаковый хэш,
    # поэтому они всегда попадают в одну корзину (коллизия)
    def __init__(self, name):
        self.name = name

    def __hash__(self):
        return 1

    def __eq__(self, other):
        return self.name == other.name


def test_collisions():
    h = HashTable()
    h.put(BadKey("a"), 1)
    h.put(BadKey("b"), 2)
    h.put(BadKey("c"), 3)
    assert h.get(BadKey("a")) == 1
    assert h.get(BadKey("b")) == 2
    assert h.get(BadKey("c")) == 3
    assert len(h) == 3


def test_remove_in_collision_bucket():
    h = HashTable()
    h.put(BadKey("a"), 1)
    h.put(BadKey("b"), 2)
    h.remove(BadKey("a"))
    assert h.get(BadKey("a")) is None
    assert h.get(BadKey("b")) == 2


def test_resize_keeps_data():
    h = HashTable(capacity=2)
    for i in range(100):
        h.put(i, i * i)
    assert len(h) == 100
    assert h.capacity > 2
    for i in range(100):
        assert h.get(i) == i * i


def test_keys():
    h = HashTable()
    for k in ["a", "b", "c"]:
        h.put(k, 0)
    assert sorted(h.keys()) == ["a", "b", "c"]


def test_different_key_types():
    h = HashTable()
    h.put(1, "int")
    h.put("1", "str")
    h.put((1, 2), "tuple")
    assert h.get(1) == "int"
    assert h.get("1") == "str"
    assert h.get((1, 2)) == "tuple"
