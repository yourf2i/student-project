# LRU-кэш (Least Recently Used).
# Хранит не больше capacity элементов. Когда место кончилось,
# выкидывается тот элемент, которым дольше всего не пользовались.
#
# Как сделано:
#  - хэш-таблица: ключ -> узел списка (чтобы находить узел за O(1))
#  - двусвязный список: от head к tail идут от самых свежих к самым старым
#    Когда обращаемся к элементу, переносим его в начало списка.
#    Когда надо что-то выкинуть, убираем узел перед tail.

from structures.hash_table import HashTable


class _Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("capacity должен быть больше 0")
        self.capacity = capacity
        self.table = HashTable()
        # фиктивные узлы по краям, чтобы не проверять на None при вставке/удалении
        self.head = _Node(None, None)
        self.tail = _Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def __len__(self):
        return len(self.table)

    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_front(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        # если ключа нет, возвращаем None
        if not self.table.contains(key):
            return None
        node = self.table.get(key)
        # элемент использовали, значит он теперь самый свежий
        self._remove_node(node)
        self._add_to_front(node)
        return node.value

    def put(self, key, value):
        if self.table.contains(key):
            node = self.table.get(key)
            node.value = value
            self._remove_node(node)
            self._add_to_front(node)
            return

        if len(self.table) >= self.capacity:
            # место кончилось, выкидываем самый старый (он перед tail)
            oldest = self.tail.prev
            self._remove_node(oldest)
            self.table.remove(oldest.key)

        node = _Node(key, value)
        self._add_to_front(node)
        self.table.put(key, node)

    def keys_by_recent(self):
        # ключи от самого свежего к самому старому (нужно для тестов)
        result = []
        cur = self.head.next
        while cur is not self.tail:
            result.append(cur.key)
            cur = cur.next
        return result
