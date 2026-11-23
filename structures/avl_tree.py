# АВЛ-дерево: бинарное дерево поиска, которое само себя балансирует.
# Правило: у любого узла высоты левого и правого поддеревьев
# отличаются не больше чем на 1. Если разница стала 2, делаем повороты.
# Из-за этого высота дерева всегда около log(n), и поиск быстрый.


class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1  # высота листа = 1


class AVLTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    # ---------- вспомогательные штуки ----------

    def _height(self, node):
        if node is None:
            return 0
        return node.height

    def _update_height(self, node):
        node.height = 1 + max(self._height(node.left), self._height(node.right))

    def _balance(self, node):
        # баланс-фактор: положительный значит левое поддерево выше
        if node is None:
            return 0
        return self._height(node.left) - self._height(node.right)

    def _rotate_right(self, y):
        #       y            x
        #      / \          / \
        #     x   C   ->   A   y
        #    / \              / \
        #   A   B            B   C
        x = y.left
        y.left = x.right
        x.right = y
        self._update_height(y)
        self._update_height(x)
        return x  # x теперь корень этого поддерева

    def _rotate_left(self, x):
        # зеркальный случай для правого поворота
        y = x.right
        x.right = y.left
        y.left = x
        self._update_height(x)
        self._update_height(y)
        return y

    def _rebalance(self, node):
        self._update_height(node)
        balance = self._balance(node)

        if balance > 1:
            # слева слишком высоко
            if self._balance(node.left) < 0:
                # случай "лево-право": сначала поворачиваем левого ребёнка
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        if balance < -1:
            # справа слишком высоко
            if self._balance(node.right) > 0:
                # случай "право-лево"
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node  # всё и так нормально

    # ---------- вставка ----------

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            self.size += 1
            return AVLNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        else:
            # такой ключ уже есть, дубликаты не храним
            return node
        return self._rebalance(node)

    # ---------- поиск ----------

    def contains(self, key):
        cur = self.root
        while cur is not None:
            if key == cur.key:
                return True
            elif key < cur.key:
                cur = cur.left
            else:
                cur = cur.right
        return False

    # ---------- удаление ----------

    def delete(self, key):
        # возвращает True если ключ был и мы его удалили
        if not self.contains(key):
            return False
        self.root = self._delete(self.root, key)
        self.size -= 1
        return True

    def _delete(self, node, key):
        if node is None:
            return None
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            # нашли узел, который надо удалить
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            # у узла два ребёнка: берём самый маленький ключ из правого
            # поддерева, ставим его сюда и удаляем его оттуда
            smallest = node.right
            while smallest.left is not None:
                smallest = smallest.left
            node.key = smallest.key
            node.right = self._delete(node.right, smallest.key)
        return self._rebalance(node)

    # ---------- обход и проверки ----------

    def in_order(self):
        # обход слева-направо, для дерева поиска даёт отсортированный список
        result = []
        self._in_order(self.root, result)
        return result

    def _in_order(self, node, result):
        if node is None:
            return
        self._in_order(node.left, result)
        result.append(node.key)
        self._in_order(node.right, result)

    def height(self):
        return self._height(self.root)

    def is_balanced(self):
        # проверка для тестов: везде ли баланс в пределах [-1, 1]
        return self._check(self.root)

    def _check(self, node):
        if node is None:
            return True
        if abs(self._balance(node)) > 1:
            return False
        return self._check(node.left) and self._check(node.right)
