# Дек (двусторонняя очередь): можно добавлять и забирать с обоих концов.
# Сделан на двусвязном списке: у каждого узла есть ссылки и вперёд, и назад.
# Благодаря этому все операции работают за O(1).


class DNode:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class Deque:
    def __init__(self):
        self.head = None  # левый конец
        self.tail = None  # правый конец
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        cur = self.head
        while cur is not None:
            yield cur.value
            cur = cur.next

    def is_empty(self):
        return self.size == 0

    def push_front(self, value):
        node = DNode(value)
        if self.head is None:
            # дек был пустой, узел и голова, и хвост
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.size += 1

    def push_back(self, value):
        node = DNode(value)
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.size += 1

    def pop_front(self):
        if self.head is None:
            raise IndexError("дек пустой")
        value = self.head.value
        self.head = self.head.next
        if self.head is None:
            # элементов не осталось
            self.tail = None
        else:
            self.head.prev = None
        self.size -= 1
        return value

    def pop_back(self):
        if self.tail is None:
            raise IndexError("дек пустой")
        value = self.tail.value
        self.tail = self.tail.prev
        if self.tail is None:
            self.head = None
        else:
            self.tail.next = None
        self.size -= 1
        return value

    def peek_front(self):
        # посмотреть первый элемент не удаляя его
        if self.head is None:
            raise IndexError("дек пустой")
        return self.head.value

    def peek_back(self):
        if self.tail is None:
            raise IndexError("дек пустой")
        return self.tail.value

    def to_list(self):
        return list(self)
