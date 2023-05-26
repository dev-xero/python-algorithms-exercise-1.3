# github repository: https://github.com/dev-xero/python-algorithms-exercise-1.3

"""stack_ds.py
   Python implementation of a stack data structure
"""

# ---------------------------------------------------------------------------------------------------------


from data_structures.linked_list_ds import Node


# ---------------------------------------------------------------------------------------------------------


class Stack:
    """Stack implementation in Python"""
    def __init__(self):
        """Setup"""
        self._first: Node | None = None
        self._size: int = 0

    def is_empty(self) -> bool:
        """Returns true if the first item is None"""
        return self._first is None

    @property
    def size(self) -> int:
        """Returns the size of the stack"""
        return self._size

    def push(self, item: str) -> None:
        """Pushes an item onto the stack"""
        old_first = self._first
        first = Node()

        first.item = item
        first.next = old_first

        self._first = first
        self._size += 1

    def pop(self) -> str:
        """Pops an item from the stack and returns it"""
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack")

        old_first = self._first
        self._first = old_first.next

        self._size -= 1
        return old_first.item


# ---------------------------------------------------------------------------------------------------------


def main():
    """Testing"""
    test_stack = Stack()

    print(test_stack.is_empty())
    test_stack.push("this")
    test_stack.push("is")
    test_stack.push("a")
    test_stack.push("stack")

    print(test_stack.size)
    print(test_stack.pop())
    print(test_stack.pop())
    print(test_stack.pop())

    print(test_stack.size)
    print(test_stack.pop())
    print(test_stack.pop())


# ---------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    main()
