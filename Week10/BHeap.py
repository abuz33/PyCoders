from math import floor, log2, ceil
# binary-tree based ds: supports heap invariant
# to simplify thins we are not using hash-map support for log(n) complexity


class BHeap:
    def __init__(self) -> None:
        # python list is actually a dynamic array
        # so, no need to re-size with capacity
        self.__list = []

    def size(self) -> int:
        return len(self.__list)

    def is_empty(self) -> bool:
        return self.size() == 0

    def peek(self):
        self.__raise_heap_empty_error("can not peek")
        return self.__list[0]

    def poll(self):
        self.__raise_heap_empty_error("can not poll")

        if self.size() == 1:
            return self.__list.pop()

        item = self.__list[0]
        self.__list[0] = self.__list.pop()

        idx = 0
        while self.__has_left_child(idx):
            c_idx = self.__left_child_idx(idx)
            if self.__has_right_child(idx) and self.__right_child(idx) < self.__left_child(idx):
                c_idx = self.__right_child_idx(idx)
            if self.__list[idx] < self.__list[c_idx]:
                break
            else:
                self.__swap(idx, c_idx)
            idx = c_idx
        return item

    def add(self, element):
        self.__list.append(element)
        new_idx = len(self.__list) - 1
        while new_idx > 0 and self.__parent(new_idx) > self.__list[new_idx]:
            self.__swap(new_idx, self.__parent_idx(new_idx))
            new_idx = self.__parent_idx(new_idx)

    def __swap(self, idx_i, idx_j):
        self.__list[idx_i], self.__list[idx_j] = self.__list[idx_j], self.__list[idx_i]

    def __raise_heap_empty_error(self, msg: str):
        if self.is_empty():
            raise RuntimeError(f"Empty heap: {msg}")

    def __parent_idx(self, child_idx: int) -> int:
        return (child_idx - 1) // 2

    def __left_child_idx(self, parent_idx: int) -> int:
        return 2 * parent_idx + 1

    def __right_child_idx(self, parent_idx: int) -> int:
        return 2 * parent_idx + 2

    def __has_left_child(self, idx: int) -> bool:
        return self.__left_child_idx(idx) < self.size()

    def __has_right_child(self, idx: int) -> bool:
        return self.__right_child_idx(idx) < self.size()

    def __left_child(self, idx: int):
        return self.__list[self.__left_child_idx(idx)]

    def __right_child(self, idx: int):
        return self.__list[self.__right_child_idx(idx)]

    def __parent(self, idx: int):
        return self.__list[self.__parent_idx(idx)]

    def __iter__(self):
        """use with caution: empties the b-heap"""
        while not self.is_empty():
            yield self.poll()

    def __repr__(self) -> str:
        if self.is_empty():
            return "[Empty B-Heap]"

        nodes = []
        for node in self.__list:
            nodes.append(node)
        return "[ " + " <?== ".join(map(str, nodes)) + " ]"


binary_heap = BHeap()
binary_heap.add(1)
binary_heap.add(10)
binary_heap.add(9)
binary_heap.add(3)
binary_heap.add(13)

print(binary_heap)
