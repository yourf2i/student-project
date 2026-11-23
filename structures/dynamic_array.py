# Динамический массив (как list в питоне, только самодельный).
# Внутри лежит обычный список фиксированной длины (capacity).
# Когда место кончается, делаем новый в 2 раза больше и копируем туда всё.


class DynamicArray:
    def __init__(self):
        self.capacity = 4  # сколько всего места
        self.size = 0      # сколько элементов реально лежит
        self.data = [None] * self.capacity

    def __len__(self):
        return self.size

    def __getitem__(self, index):
        return self.get(index)

    def __setitem__(self, index, value):
        self.set(index, value)

    def __iter__(self):
        for i in range(self.size):
            yield self.data[i]

    def _check_index(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("индекс вне массива")

    def _grow(self):
        # увеличиваем место в 2 раза
        self.capacity = self.capacity * 2
        new_data = [None] * self.capacity
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.data = new_data

    def append(self, value):
        if self.size == self.capacity:
            self._grow()
        self.data[self.size] = value
        self.size += 1

    def get(self, index):
        self._check_index(index)
        return self.data[index]

    def set(self, index, value):
        self._check_index(index)
        self.data[index] = value

    def insert(self, index, value):
        # вставка в середину: сдвигаем всё что правее на одну клетку вправо
        if index < 0 or index > self.size:
            raise IndexError("индекс вне массива")
        if self.size == self.capacity:
            self._grow()
        i = self.size
        while i > index:
            self.data[i] = self.data[i - 1]
            i -= 1
        self.data[index] = value
        self.size += 1

    def remove_at(self, index):
        # удаляем элемент и сдвигаем всё что правее на одну клетку влево
        self._check_index(index)
        value = self.data[index]
        for i in range(index, self.size - 1):
            self.data[i] = self.data[i + 1]
        self.data[self.size - 1] = None
        self.size -= 1
        return value

    def pop(self):
        # убрать последний элемент
        if self.size == 0:
            raise IndexError("массив пустой")
        return self.remove_at(self.size - 1)

    def to_list(self):
        return list(self)
