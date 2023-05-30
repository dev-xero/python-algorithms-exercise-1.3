# github repository: https://github.com/dev-xero/python-algorithms-exercise-1.3

"""deque_ds.py
   Python implementation of a deque data structure
"""

# ---------------------------------------------------------------------------------------------------------


from data_structures.linked_list_ds import Node


# ---------------------------------------------------------------------------------------------------------


class Deque:
    """A double-ended queue"""
    def __init__(self):
        """Setup"""
        self._head: None | Node = None
        self._tail: None | Node = None
        self._size: int = 0

    def is_empty(self) -> bool:
        """Returns true if head is none"""
        return self._head is None

    @property
    def size(self) -> int:
        """Returns the size of the deque"""
        return self._size

    def push_left(self, item: str) -> Node:
        """Pushes an item in front of the deque"""
        new_node = Node(item)

        if self.is_empty():
            self._head = new_node
            self._tail = new_node
            self._size += 1

            return new_node

        new_node.next = self._head
        self._head = new_node
        self._size += 1

        return new_node

    def push_right(self, item: str) -> Node:
        """Pushes an item to the back of the deque"""
        new_node = Node(item)

        if self.is_empty():
            self._head = new_node
            self._tail = new_node
            self._size += 1

            return new_node

        self._tail.next = new_node
        self._tail = new_node
        self._size += 1

        return new_node

    def pop_left(self) -> Node:
        """Pops an item from the front of the deque and returns it"""
        if self.is_empty():
            raise Exception("Cannot pop from the front of an empty deque")

        old_head = self._head
        self._head = self._head.next
        self._size -= 1

        return old_head

    def pop_right(self) -> Node:
        """Pops an item from the back of the deque and returns it"""
        if self.is_empty():
            raise Exception("Cannot pop from the back of an empty deque")

        curr = self._head

        while True:
            if curr.next == self._tail:
                old_tail = curr.next
                self._tail = curr
                curr.next = None
                self._size -= 1

                return old_tail

            curr = curr.next


# ---------------------------------------------------------------------------------------------------------


def main():
    """Testing"""
    test_deque = Deque()

    test_deque.push_left("2")
    test_deque.push_left("1")
    test_deque.push_left("0")

    test_deque.push_right("3")
    test_deque.pop_left()
    test_deque.pop_right()

    test_deque.push_right("4")


# ---------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    main()
