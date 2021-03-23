from __future__ import annotations
from BHeap import BHeap
from functools import total_ordering


@total_ordering
class ComparableNode:
    def __init__(self, data, order_value, prioritized=False) -> None:
        self.data = data
        self.__order_value = order_value
        self.__prioritized = prioritized

    def __lt__(self, other: ComparableNode) -> bool:
        if self.__prioritized and not other.__prioritized:
            return True
        elif other.__prioritized and not self.__prioritized:
            return False
        return self.__order_value < other.__order_value

    def __repr__(self) -> str:
        return str(self.data)

    def trace(self) -> str:
        return f"data: {self.data}, prioritized: {self.__prioritized}, order: {self.__order_value}"


class PQueue:
    def __init__(self) -> None:
        self.__list = BHeap()
        # this serves as the single differentiator between prioritized elements
        self.__priority_counter = 0

    def size(self) -> int:
        return self.__list.size()

    def is_empty(self) -> bool:
        return self.__list.is_empty()

    def peek(self) -> ComparableNode:
        return self.__list.peek()

    def poll(self) -> ComparableNode:
        return self.__list.poll()

    def add(self, data):
        self.__priority_counter += 1
        self.__list.add(ComparableNode(
            data, order_value=self.__priority_counter))

    def add_prioritized(self, data):
        self.__priority_counter += 1
        self.__list.add(ComparableNode(
            data, order_value=self.__priority_counter, prioritized=True))

    def __iter__(self):
        """use with caution: empties/consumes the p-queue"""
        for item in self.__list:
            yield item

    def __repr__(self) -> str:
        if self.is_empty():
            return "[Empty P-Queue]"
        return str(self.__list)
