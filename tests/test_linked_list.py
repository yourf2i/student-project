import pytest

from structures.linked_list import LinkedList


def test_empty_list():
    lst = LinkedList()
    assert len(lst) == 0
    assert lst.to_list() == []


def test_append():
    lst = LinkedList()
    lst.append(1)
    lst.append(2)
    lst.append(3)
    assert lst.to_list() == [1, 2, 3]
    assert len(lst) == 3


def test_prepend():
    lst = LinkedList()
    lst.prepend(1)
    lst.prepend(2)
    assert lst.to_list() == [2, 1]


def test_insert_in_middle():
    lst = LinkedList()
    lst.append(1)
    lst.append(3)
    lst.insert(1, 2)
    assert lst.to_list() == [1, 2, 3]


def test_insert_at_start_and_end():
    lst = LinkedList()
    lst.insert(0, "b")
    lst.insert(0, "a")
    lst.insert(2, "c")
    assert lst.to_list() == ["a", "b", "c"]


def test_insert_bad_index():
    lst = LinkedList()
    with pytest.raises(IndexError):
        lst.insert(5, 1)
    with pytest.raises(IndexError):
        lst.insert(-1, 1)


def test_get():
    lst = LinkedList()
    for x in [10, 20, 30]:
        lst.append(x)
    assert lst.get(0) == 10
    assert lst.get(2) == 30
    with pytest.raises(IndexError):
        lst.get(3)


def test_find():
    lst = LinkedList()
    for x in [5, 6, 7]:
        lst.append(x)
    assert lst.find(6) == 1
    assert lst.find(100) == -1


def test_remove_head_middle_tail():
    lst = LinkedList()
    for x in [1, 2, 3, 4]:
        lst.append(x)
    assert lst.remove(1) is True   # голова
    assert lst.remove(3) is True   # середина
    assert lst.remove(4) is True   # хвост
    assert lst.to_list() == [2]
    assert len(lst) == 1


def test_remove_missing():
    lst = LinkedList()
    lst.append(1)
    assert lst.remove(99) is False
    assert len(lst) == 1


def test_remove_only_first_occurrence():
    lst = LinkedList()
    for x in [1, 2, 1]:
        lst.append(x)
    lst.remove(1)
    assert lst.to_list() == [2, 1]


def test_reverse():
    lst = LinkedList()
    for x in [1, 2, 3]:
        lst.append(x)
    lst.reverse()
    assert lst.to_list() == [3, 2, 1]


def test_reverse_empty():
    lst = LinkedList()
    lst.reverse()
    assert lst.to_list() == []
