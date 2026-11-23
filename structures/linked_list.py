# Односвязный список.
# Каждый элемент (узел) хранит значение и ссылку на следующий узел.
# Последний узел ссылается на None.


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None  # первый узел
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        cur = self.head
        while cur is not None:
            yield cur.value
            cur = cur.next

    def append(self, value):
        # добавить в конец: надо дойти до последнего узла, поэтому O(n)
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = new_node
        self.size += 1

    def prepend(self, value):
        # добавить в начало: O(1), просто новый узел становится головой
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def insert(self, index, value):
        # вставить значение так, чтобы оно оказалось на позиции index
        if index < 0 or index > self.size:
            raise IndexError("индекс вне списка")
        if index == 0:
            self.prepend(value)
            return
        # идём к узлу, который стоит ПЕРЕД нужной позицией
        cur = self.head
        for _ in range(index - 1):
            cur = cur.next
        new_node = Node(value)
        new_node.next = cur.next
        cur.next = new_node
        self.size += 1

    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("индекс вне списка")
        cur = self.head
        for _ in range(index):
            cur = cur.next
        return cur.value

    def find(self, value):
        # возвращает индекс первого найденного значения или -1
        cur = self.head
        i = 0
        while cur is not None:
            if cur.value == value:
                return i
            cur = cur.next
            i += 1
        return -1

    def remove(self, value):
        # удаляет первое вхождение, возвращает True если что-то удалили
        prev = None
        cur = self.head
        while cur is not None:
            if cur.value == value:
                if prev is None:
                    # удаляем голову
                    self.head = cur.next
                else:
                    # перекидываем ссылку через удаляемый узел
                    prev.next = cur.next
                self.size -= 1
                return True
            prev = cur
            cur = cur.next
        return False

    def reverse(self):
        # разворачиваем ссылки на противоположные
        prev = None
        cur = self.head
        while cur is not None:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev

    def to_list(self):
        return list(self)
