from LinkedList import LinkedList


class Stack:
    def __init__(self) -> None:
        self.__list = LinkedList()

    def size(self) -> int:
        return self.__list.size()

    def is_empty(self) -> bool:
        return self.__list.is_empty()

    def push(self, element):
        self.__list.add_first(element)

    def peek(self):
        return self.__list.peek_first()

    def pop(self):
        return self.__list.remove_first()

    def __iter__(self):
        """use with caution: empties the stack"""
        while not self.is_empty():
            yield self.pop()

    def __repr__(self) -> str:
        if self.is_empty():
            return "[Empty Stack]"

        nodes = []
        for node in self.__list:
            nodes.append(node.data)
        return "[ " + " <== ".join(map(str, nodes)) + " ]"
