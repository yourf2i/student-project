# Быстрая сортировка.
# Выбираем опорный элемент (pivot), всё что меньше него кидаем влево,
# всё остальное вправо. Потом то же самое делаем для левой и правой части.
# В среднем O(n log n).
# Сортируем прямо в самом массиве, новый не создаём.


def partition(arr, low, high):
    # берём pivot из середины и прячем в конец
    # (так на уже отсортированном массиве работает лучше, чем брать крайний)
    mid = (low + high) // 2
    arr[mid], arr[high] = arr[high], arr[mid]
    pivot = arr[high]

    i = low  # сюда будем ставить элементы меньше pivot
    for j in range(low, high):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    # ставим pivot на его итоговое место
    arr[i], arr[high] = arr[high], arr[i]
    return i


def quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        p = partition(arr, low, high)
        quick_sort(arr, low, p - 1)
        quick_sort(arr, p + 1, high)
    return arr
