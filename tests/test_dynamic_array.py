import pytest

from structures.dynamic_array import DynamicArray


def test_empty():
    arr = DynamicArray()
    assert len(arr) == 0
    assert arr.to_list() == []


def test_append_and_get():
    arr = DynamicArray()
    arr.append(10)
    arr.append(20)
    assert arr.get(0) == 10
    assert arr[1] == 20
    assert len(arr) == 2


def test_grow_when_full():
    # начальный capacity = 4, кладём больше, чтобы сработало расширение
    arr = DynamicArray()
    for i in range(20):
        arr.append(i)
    assert len(arr) == 20
    assert arr.to_list() == list(range(20))
    assert arr.capacity >= 20


def test_set():
    arr = DynamicArray()
    arr.append(1)
    arr.set(0, 99)
    arr[0] = 100
    assert arr.get(0) == 100


def test_get_bad_index():
    arr = DynamicArray()
    arr.append(1)
    with pytest.raises(IndexError):
        arr.get(1)
    with pytest.raises(IndexError):
        arr.get(-1)


def test_insert_middle():
    arr = DynamicArray()
    for x in [1, 2, 4]:
        arr.append(x)
    arr.insert(2, 3)
    assert arr.to_list() == [1, 2, 3, 4]


def test_insert_start_and_end():
    arr = DynamicArray()
    arr.insert(0, 2)
    arr.insert(0, 1)
    arr.insert(2, 3)
    assert arr.to_list() == [1, 2, 3]


def test_insert_triggers_grow():
    arr = DynamicArray()
    for i in range(4):
        arr.append(i)
    arr.insert(1, 100)
    assert arr.to_list() == [0, 100, 1, 2, 3]


def test_insert_bad_index():
    arr = DynamicArray()
    with pytest.raises(IndexError):
        arr.insert(1, 5)


def test_remove_at():
    arr = DynamicArray()
    for x in [1, 2, 3, 4]:
        arr.append(x)
    assert arr.remove_at(1) == 2
    assert arr.to_list() == [1, 3, 4]
    assert len(arr) == 3


def test_remove_at_bad_index():
    arr = DynamicArray()
    with pytest.raises(IndexError):
        arr.remove_at(0)


def test_pop():
    arr = DynamicArray()
    arr.append(1)
    arr.append(2)
    assert arr.pop() == 2
    assert arr.pop() == 1
    with pytest.raises(IndexError):
        arr.pop()


def test_iteration():
    arr = DynamicArray()
    for x in [3, 2, 1]:
        arr.append(x)
    assert [x for x in arr] == [3, 2, 1]
