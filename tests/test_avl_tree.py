import random

from structures.avl_tree import AVLTree


def test_empty():
    t = AVLTree()
    assert len(t) == 0
    assert t.in_order() == []
    assert t.height() == 0
    assert not t.contains(1)


def test_insert_and_contains():
    t = AVLTree()
    for x in [5, 3, 8]:
        t.insert(x)
    assert t.contains(5)
    assert t.contains(3)
    assert t.contains(8)
    assert not t.contains(4)
    assert len(t) == 3


def test_no_duplicates():
    t = AVLTree()
    t.insert(1)
    t.insert(1)
    assert len(t) == 1
    assert t.in_order() == [1]


def test_in_order_sorted():
    t = AVLTree()
    for x in [7, 2, 9, 1, 5, 8]:
        t.insert(x)
    assert t.in_order() == [1, 2, 5, 7, 8, 9]


def test_right_rotation():
    # вставка по убыванию -> нужен правый поворот
    t = AVLTree()
    for x in [3, 2, 1]:
        t.insert(x)
    assert t.root.key == 2
    assert t.height() == 2


def test_left_rotation():
    # вставка по возрастанию -> нужен левый поворот
    t = AVLTree()
    for x in [1, 2, 3]:
        t.insert(x)
    assert t.root.key == 2
    assert t.height() == 2


def test_left_right_rotation():
    t = AVLTree()
    for x in [3, 1, 2]:
        t.insert(x)
    assert t.root.key == 2
    assert t.is_balanced()


def test_right_left_rotation():
    t = AVLTree()
    for x in [1, 3, 2]:
        t.insert(x)
    assert t.root.key == 2
    assert t.is_balanced()


def test_sorted_insert_stays_balanced():
    # если бы дерево не балансировалось, при 1000 по возрастанию высота была бы 1000
    t = AVLTree()
    for x in range(1000):
        t.insert(x)
    assert t.is_balanced()
    assert t.height() <= 14  # для 1000 элементов около log2(1000) ~ 10, с запасом


def test_delete_leaf():
    t = AVLTree()
    for x in [2, 1, 3]:
        t.insert(x)
    assert t.delete(1) is True
    assert t.in_order() == [2, 3]
    assert len(t) == 2


def test_delete_node_with_one_child():
    t = AVLTree()
    for x in [2, 1, 3, 4]:
        t.insert(x)
    t.delete(3)
    assert t.in_order() == [1, 2, 4]
    assert t.is_balanced()


def test_delete_node_with_two_children():
    t = AVLTree()
    for x in [5, 3, 8, 2, 4, 7, 9]:
        t.insert(x)
    t.delete(5)  # это корень, у него два ребёнка
    assert t.in_order() == [2, 3, 4, 7, 8, 9]
    assert not t.contains(5)
    assert t.is_balanced()


def test_delete_missing():
    t = AVLTree()
    t.insert(1)
    assert t.delete(100) is False
    assert len(t) == 1


def test_delete_all():
    t = AVLTree()
    for x in range(10):
        t.insert(x)
    for x in range(10):
        assert t.delete(x) is True
    assert len(t) == 0
    assert t.root is None


def test_random_insert_delete():
    # сравниваем с обычным set: после каждой операции всё должно совпадать
    random.seed(42)
    t = AVLTree()
    s = set()
    for _ in range(500):
        x = random.randint(0, 100)
        if random.random() < 0.6:
            t.insert(x)
            s.add(x)
        else:
            t.delete(x)
            s.discard(x)
        assert t.in_order() == sorted(s)
        assert len(t) == len(s)
        assert t.is_balanced()
