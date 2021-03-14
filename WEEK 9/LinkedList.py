from __future__ import annotations


class ListNode:
    def __init__(self, data, next: ListNode = None, prev: ListNode = None) -> None:
        self.data = data
        self.next = next
        self.prev = prev

    def __repr__(self) -> None:
        return f"{self.data}"


# __ (2 UNDERSCORE) IN PYTHON MEANS THE ATT IS NOT ACCESIBLE
a = []


class LinkedList:
    def __init__(self, tail: ListNode = None, head: ListNode = None) -> None:
        self.tail = tail
        self.head = head
        self.__size = 0

    def size(self) -> int:
        return self.__size

    def is_empty(self) -> bool:
        """
        - returns `True` if the list is empty.
        - returns `False` if the list has element or elements
        """
        return self.size() == 0

    def add_last(self, value) -> None:
        if self.is_empty():
            # node = ListNode(data=value)
            # self.tail = node
            # self.head = node

            self.tail = self.head = ListNode(data=value)
        else:
            # nodu olustur
            node = ListNode(data=value, prev=self.tail)
            # kuyrugun nexti yap
            self.tail.next = node
            # node un previni eski kuyruk yap
            # node.prev = self.tail
            # node u kuyruk yap
            self.tail = node
        self.__size += 1

    def add_first(self, value) -> None:
        if self.is_empty():
            # node = ListNode(data=value)
            # self.tail = node
            # self.head = node

            self.tail = self.head = ListNode(data=value)
        else:
            # nodu olustur
            node = ListNode(data=value, next=self.head)
            # head in prev i yap
            self.head.prev = node
            # node un next ini eski head yap
            # node.prev = self.head
            # node u head yap
            self.head = node
        self.__size += 1

    def add_after(self, after_value, value):
        if self.is_empty():
            raise RuntimeError("Empty List: can not add after")

        for node in self:
            if node.data == after_value:
                # edge case data is the tail
                if node is self.tail:
                    return self.add_last(value)

                new_node = ListNode(value, prev=node, next=node.next)
                # new_node.next = node.next
                # new_node.prev = node
                node.next = new_node
                new_node.next.prev = new_node
                return
        else:
            print(f"{after_value} is not in the list")

    def add_before(self, before_value, value):
        if self.is_empty():
            raise RuntimeError("Empty List: can not add after")

        for node in self:
            if node.data == before_value:
                # edge case data is the tail
                if node is self.head:
                    return self.add_first(value)

                new_node = ListNode(value, prev=node.prev, next=node)
                # new_node.next = node.next
                # new_node.prev = node
                node.prev = new_node
                node.prev.next = new_node
                return
        else:
            print(f"{before_value} is not in the list")

    def add(self, value):
        self.add_last(value)

    def update(self, old_value, new_value):
        node, index = self.find_value(old_value)
        if index == -1:
            raise RuntimeError(f'{old_value} is not found')
        node.data = new_value

    def find_value(self, value) -> tuple[ListNode | None, int]:
        """
        Makes a linear search starting from the head of he list.
        - if `null` or (`None`) is provided as argument to be searched raises a Run time Error.
        - if the value  is not in the list returns `(None, -1)`
        - If found, `first elemend` is the `node` and the `second` is the index itself.
        """
        if value is None:
            raise RuntimeError("Can not find None")

        if self.is_empty():
            return None, -1
        i = 0
        for node in self:
            if node.data == value:
                return node, i
            i += 1

        return None, -1

    def remove_first(self):
        """
        - Removes the first element in the list
        """
        if self.is_empty():
            raise RuntimeError("Empty List : can not remove first")
        temp = self.head.data

        self.head = self.head.next
        self.__size -= 1
        if self.is_empty():
            self.tail = None
        else:
            self.head.prev = None

        return temp

    def remove_last(self):
        """
        - Removes the last element in the list
        """
        if self.is_empty():
            raise RuntimeError("Empty List : can not remove first")
        temp = self.tail.data

        self.tail = self.tail.prev
        self.__size -= 1
        if self.is_empty():
            self.head = None
        else:
            self.tail.next = None

        return temp

    def remove_node(self, node: ListNode):
        """
        - use wih caution: `node` can not be `None`
        """
        if node is self.head:
            return self.remove_first()
        elif node is self.tail:
            return self.remove_last()

        temp = node.data

        node.next.prev = node.prev
        node.prev.next = node.next
        node.next = node.prev = None
        node = None
        self.__size -= 1
        return temp

    def remove_at(self, index: int):
        """
        - Removes the element at the given index in the list
        """
        if index < 0 or index >= self.size():
            raise RuntimeError(f"index: {index} is Out of the list boundaries")

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

    def remove_value(self, value):
        """
        - Removes the value in the list
        """
        node, index = self.find_value(value)
        if index != -1:
            self.remove_node(node)
            return True
        return False

    def index_of(self, value):
        """
        - Returns the index of the `value`
        """
        node, index = self.find_value(value)
        return index

    def contains(self, value):
        """
        Checks if the element is in the list.
        - Returns `True`, if the element is in the list.
        - Returns `False` if the element is not in the list
        """
        node, index = self.find_value(value)
        return index != -1

    def peek_first(self):
        if self.is_empty():
            raise RuntimeError("Empty List: can not peek first")
        return self.head.data

    def peek_last(self):
        if self.is_empty():
            raise RuntimeError("Empty List: can not peek last")
        return self.tail.data

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self) -> str:
        elements = []
        for node in self:
            elements.append(str(node.data))

        return "[" + " <--> ".join(elements) + "]"


x = LinkedList()

x.add_last(15)
x.add_last(5)
x.add_first(35)

x.add_after(35, 45)
x.add_before(5, 45)

print(x)

x.update(15, 0)
print(x)

x.update(555, 0)
print(x)
