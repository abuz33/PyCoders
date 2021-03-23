from __future__ import annotations
from typing import Tuple


class ListNode:
    def __init__(self, data, next: ListNode | None = None, prev: ListNode | None = None):
        self.data = data
        self.next = next
        self.prev = prev

    def __repr__(self) -> str:
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = self.tail = None
        self.__size = 0

    def size(self) -> int:
        return self.__size

    def is_empty(self) -> bool:
        return self.size() == 0

    def __add_initial(self, element):
        """ use with causion: check `is_empty()` before use"""
        self.head = self.tail = ListNode(data=element)

    def add_last(self, element):
        self.__raise_null_element_error(element)

        if self.is_empty():
            self.__add_initial(element)
        else:
            self.tail.next = ListNode(
                data=element, next=None, prev=self.tail)
            self.tail = self.tail.next
        self.__size += 1

    def add_first(self, element):
        self.__raise_null_element_error(element)

        if self.is_empty():
            self.__add_initial(element)
        else:
            self.head.prev = ListNode(
                data=element, next=self.head, prev=None)
            self.head = self.head.prev
        self.__size += 1

    def add_after(self, after_element, element):
        self.__raise_list_empty_error("can not add after")

        for node in self:
            if node.data == after_element:
                if node is self.tail:
                    return self.add_last(element)
                new_node = ListNode(element, prev=node, next=node.next)
                node.next.prev = new_node
                node.next = new_node
                return
        raise RuntimeError(f"Value: {after_element} not found  in the list!")

    def add_before(self, before_element, element):
        self.__raise_list_empty_error("can not add before")

        for node in self:
            if node.data == before_element:
                if node is self.head:
                    return self.add_first(element)
                new_node = ListNode(element, prev=node.prev, next=node)
                node.prev.next = new_node
                node.prev = new_node
                return
        raise RuntimeError(f"Value: {before_element} not found  in the list!")

    def add(self, element):
        self.add_last(element)

    def update(self, element):
        idx, node = self.find_value(element)
        if idx == -1:
            raise RuntimeError(f"Value: {element} not found  in the list!")
        node.data = element

    def __raise_null_element_error(self, element):
        if element is None:
            raise RuntimeError("null values not supported!")

    def __raise_list_empty_error(self, msg: str):
        if self.is_empty():
            raise RuntimeError(f"Empty list: {msg}")

    def peek_first(self):
        self.__raise_list_empty_error("can not peek first")

        return self.head.data

    def peek_last(self):
        self.__raise_list_empty_error("can not peek last")

        return self.tail.data

    def remove_first(self):
        self.__raise_list_empty_error("can not remove first")

        data = self.head.data
        self.head = self.head.next
        self.__size -= 1

        if (self.is_empty()):
            self.tail = None
        else:
            self.head.prev = None

        return data

    def remove_last(self):
        self.__raise_list_empty_error("can not remove last")

        data = self.tail.data
        self.tail = self.tail.prev
        self.__size -= 1

        if (self.is_empty()):
            self.head = None
        else:
            self.tail.next = None

        return data

    def remove_node(self, node: ListNode):
        """use with causion: `node` can not be `None`"""
        if node.prev is None:
            return self.remove_first()
        if node.next is None:
            return self.remove_last()

        data = node.data
        node.next.prev = node.prev
        node.prev.next = node.next

        node.data = node.next = node.prev = None
        node = None
        self.__size -= 1

        return data

    def remove_at(self, index: int):
        if index < 0 or index >= self.size():
            raise RuntimeError(f"index: {index} is out of list bounds!")

        node = None
        if index < self.size() / 2:
            node = self.head
            for _ in range(0, index):
                node = node.next
        else:
            node = self.tail
            for _ in range(index, self.size() - 1):
                node = node.prev

        return self.remove_node(node)

    def find_value(self, element) -> Tuple[int, ListNode | None]:
        """
        Makes a linear search starting from the `head` of the list.

        - If `null` or (`None`) is provided as argument to be searched,
        raises a `RuntimeError`

        - If the value is not in the list returns `(-1, None)`

        - If found, `first element` is the `index` and the `second` is the `node` itself.
        """
        self.__raise_null_element_error(element)

        if self.is_empty():
            return -1, None

        index = 0
        for node in self:
            if node.data == element:
                return index, node
            index += 1

        return -1, None

    def remove_value(self, element) -> bool:
        index, node = self.find_value(element)

        if index != -1:
            self.remove_node(node)
            return True

        return False

    def index_of(self, element) -> int:
        return self.find_value(element)[0]

    def contains(self, element) -> bool:
        return self.index_of(element) != -1

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self) -> str:
        if self.is_empty():
            return "[None]"

        nodes = []
        for node in self:
            nodes.append(node.data)
        nodes.append("NONE")
        return "[ " + " <--> ".join(map(str, nodes)) + " ]"
