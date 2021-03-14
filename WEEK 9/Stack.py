from LinkedList import LinkedList
# LIFO -> Last in First Out


class Stack:
    def __init__(self) -> None:
        self.__list = LinkedList()

    def size(self):
        return self.__list.size()

    def is_empty(self):
        return self.__list.is_empty()

    def push(self, element):
        return self.__list.add_first(element)

    def pop(self):
        return self.__list.remove_first()

    def peek(self):
        return self.__list.peek_first()
