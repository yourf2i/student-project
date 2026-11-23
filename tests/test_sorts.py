import random

import pytest

from sorts.bubble_sort import bubble_sort
from sorts.quick_sort import quick_sort

# прогоняем одни и те же тесты для обеих сортировок
SORTS = [bubble_sort, quick_sort]


@pytest.mark.parametrize("sort", SORTS)
def test_empty(sort):
    assert sort([]) == []


@pytest.mark.parametrize("sort", SORTS)
def test_one_element(sort):
    assert sort([1]) == [1]


@pytest.mark.parametrize("sort", SORTS)
def test_already_sorted(sort):
    assert sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


@pytest.mark.parametrize("sort", SORTS)
def test_reversed(sort):
    assert sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


@pytest.mark.parametrize("sort", SORTS)
def test_duplicates(sort):
    assert sort([3, 1, 2, 3, 1, 2]) == [1, 1, 2, 2, 3, 3]


@pytest.mark.parametrize("sort", SORTS)
def test_negative_numbers(sort):
    assert sort([0, -5, 3, -1, 2]) == [-5, -1, 0, 2, 3]


@pytest.mark.parametrize("sort", SORTS)
def test_strings(sort):
    assert sort(["b", "c", "a"]) == ["a", "b", "c"]


@pytest.mark.parametrize("sort", SORTS)
def test_sorts_in_place(sort):
    arr = [3, 2, 1]
    sort(arr)
    assert arr == [1, 2, 3]


@pytest.mark.parametrize("sort", SORTS)
def test_random_arrays_like_builtin_sorted(sort):
    # сравниваем с встроенной sorted на случайных данных
    random.seed(1)
    for _ in range(50):
        n = random.randint(0, 60)
        arr = [random.randint(-50, 50) for _ in range(n)]
        expected = sorted(arr)
        assert sort(arr) == expected
