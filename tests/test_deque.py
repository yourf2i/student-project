import pytest

from structures.deque import Deque


def test_empty():
    d = Deque()
    assert d.is_empty()
    assert len(d) == 0


def test_push_back():
    d = Deque()
    d.push_back(1)
    d.push_back(2)
    d.push_back(3)
    assert d.to_list() == [1, 2, 3]


def test_push_front():
    d = Deque()
    d.push_front(1)
    d.push_front(2)
    d.push_front(3)
    assert d.to_list() == [3, 2, 1]


def test_mixed_push():
    d = Deque()
    d.push_back(2)
    d.push_front(1)
    d.push_back(3)
    assert d.to_list() == [1, 2, 3]
    assert len(d) == 3


def test_pop_front():
    d = Deque()
    for x in [1, 2, 3]:
        d.push_back(x)
    assert d.pop_front() == 1
    assert d.pop_front() == 2
    assert d.to_list() == [3]


def test_pop_back():
    d = Deque()
    for x in [1, 2, 3]:
        d.push_back(x)
    assert d.pop_back() == 3
    assert d.pop_back() == 2
    assert d.to_list() == [1]


def test_pop_until_empty_then_reuse():
    # проверяем, что после опустошения head и tail правильно сбросились
    d = Deque()
    d.push_back(1)
    d.pop_back()
    assert d.is_empty()
    d.push_front(5)
    assert d.to_list() == [5]
    assert d.peek_back() == 5
    d.pop_front()
    assert d.is_empty()


def test_pop_empty():
    d = Deque()
    with pytest.raises(IndexError):
        d.pop_front()
    with pytest.raises(IndexError):
        d.pop_back()


def test_peek():
    d = Deque()
    d.push_back(1)
    d.push_back(2)
    assert d.peek_front() == 1
    assert d.peek_back() == 2
    # peek ничего не удаляет
    assert len(d) == 2


def test_peek_empty():
    d = Deque()
    with pytest.raises(IndexError):
        d.peek_front()
    with pytest.raises(IndexError):
        d.peek_back()


def test_as_stack_and_queue():
    # как стек: кладём и берём с одного конца
    d = Deque()
    d.push_back(1)
    d.push_back(2)
    assert d.pop_back() == 2
    # как очередь: кладём в конец, берём из начала
    d.push_back(3)
    assert d.pop_front() == 1
    assert d.pop_front() == 3
