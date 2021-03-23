from __future__ import annotations


class BSTree:
    def __init__(self, data, left_child: BSTree | None, right_child: BSTree | None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child

    def add(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left_child is None:
                self.left_child = BSTree(data)
            else:
                self.left_child.add(data)
        else:
            if self.right_child is None:
                self.right_child = BSTree(data)
            else:
                self.right_child.add(data)

    def contains(self, data):
        if data == self.data:
            return True
        elif data < self.data:
            if self.left_child is None:
                return False
            else:
                return self.left_child.contains(data)
        else:
            if self.right_child is None:
                return False
            else:
                return self.right_child.contains(data)

    def print_in_order(self):
        if self.left_child is not None:
            self.left_child.print_in_order()
        print(self.data)
        if self.right_child is not None:
            self.right_child.print_in_order()

    def print_pre_order(self):
        print(self.data)
        if self.left_child is not None:
            self.left_child.print_pre_order()
        if self.right_child is not None:
            self.right_child.print_pre_order()

    def print_post_order(self):
        if self.left_child is not None:
            self.left_child.print_post_order()
        if self.right_child is not None:
            self.right_child.print_post_order()
        print(self.data)
