# Хэш-таблица (метод цепочек).
# Есть массив корзин (bucket). Номер корзины = hash(ключ) % количество корзин.
# Если в одну корзину попало несколько ключей (коллизия), они лежат в списке.
# Когда таблица заполнена больше чем на 75%, увеличиваем число корзин в 2 раза.


class HashTable:
    def __init__(self, capacity=8):
        self.capacity = capacity
        self.buckets = [[] for _ in range(capacity)]
        self.size = 0

    def __len__(self):
        return self.size

    def __contains__(self, key):
        return self.contains(key)

    def _index(self, key):
        return hash(key) % self.capacity

    def put(self, key, value):
        bucket = self.buckets[self._index(key)]
        for pair in bucket:
            if pair[0] == key:
                # ключ уже был, просто меняем значение
                pair[1] = value
                return
        bucket.append([key, value])
        self.size += 1
        if self.size / self.capacity > 0.75:
            self._resize()

    def get(self, key, default=None):
        bucket = self.buckets[self._index(key)]
        for pair in bucket:
            if pair[0] == key:
                return pair[1]
        return default

    def contains(self, key):
        bucket = self.buckets[self._index(key)]
        for pair in bucket:
            if pair[0] == key:
                return True
        return False

    def remove(self, key):
        # True если удалили, False если такого ключа не было
        bucket = self.buckets[self._index(key)]
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                bucket.pop(i)
                self.size -= 1
                return True
        return False

    def _resize(self):
        # номер корзины зависит от capacity, поэтому после увеличения
        # надо заново положить все пары
        old_buckets = self.buckets
        self.capacity = self.capacity * 2
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0
        for bucket in old_buckets:
            for key, value in bucket:
                self.put(key, value)

    def keys(self):
        result = []
        for bucket in self.buckets:
            for pair in bucket:
                result.append(pair[0])
        return result
