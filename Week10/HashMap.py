from __future__ import annotations
from functools import total_ordering
from LinkedList import LinkedList


@total_ordering
class HashPair:
    def __init__(self, key: str, value) -> None:
        self.key = key
        self.value = value

    def __eq__(self, other: HashPair) -> bool:
        return self.key == other.key

    def __lt__(self, other: HashPair) -> bool:
        return self.key < other.key

    def __repr__(self) -> str:
        return "{'" + str(self.key) + "' : '" + str(self.value) + "'}"


class HashMap:
    def __init__(self) -> None:
        self.__capacity = 16
        self.__size = 0
        self.__list = []
        for _ in range(0, self.__capacity):
            self.__list.append(LinkedList())

    def size(self) -> int:
        return self.__size

    def is_empty(self) -> bool:
        return self.size() == 0

    def __hash_index(self, data: str):
        return abs(hash(data)) % self.__capacity

    def add(self, key: str, value):
        idx = self.__hash_index(key)
        pair = HashPair(key, value)
        if not self.__list[idx].contains(pair):
            self.__list[idx].add(pair)
            self.__size += 1
        else:
            self.__list[idx].update(pair)

    def get(self, key: str):
        idx = self.__hash_index(key)
        for pair_node in self.__list[idx]:
            if pair_node.data.key == key:
                return pair_node.data.value
        raise RuntimeError(f"Key: {key} not found  in the map!")

    def delete(self, key: str) -> bool:
        idx = self.__hash_index(key)
        pair = HashPair(key, value=None)
        is_deleted = self.__list[idx].remove_value(pair)
        if is_deleted:
            self.__size -= 1
        return is_deleted

    def __iter__(self):
        for bucket in self.__list:
            for pair in bucket:
                yield pair

    def __repr__(self) -> str:
        if self.is_empty():
            return "{EMPTY MAP}"

        pairs = []
        for list in self.__list:
            for pair in list:
                pairs.append(f"\"{pair.data.key}\": \"{pair.data.value}\"")
        return "{ " + ", ".join(pairs) + " }"


x = HashMap()
x.add("abc", 123)
x.add("qwe", 234)
x.add("fgh", 567)
x.add("jkl", 789)

for i in x:
    print(i)
