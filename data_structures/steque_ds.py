# github repository: https://github.com/dev-xero/python-algorithms-exercise-1.3

"""steque_ds.py
   Python implementation of a steque data structure
"""

# ---------------------------------------------------------------------------------------------------------


from data_structures.linked_list_ds import Node


# ---------------------------------------------------------------------------------------------------------


class Steque:
    """A data structure that supports push, pop and enqueue"""
    def __init__(self):
        """Setup"""
        self._head: None | Node = None
        self._tail: None | Node = None
        self._size: int = 0

    def is_empty(self):
        """Returns true if the steque is empty"""
        return self._head is None

    @property
    def size(self):
        """Returns the size of the steque"""
        return self.size

    @property
    def head(self):
        """Returns the head of the steque"""
        return self._head

    def push(self, item: str) -> Node:
        """Pushes an item onto the steque"""
        new_node = Node(item)

        if self.is_empty():
            self._head = new_node
            self._tail = new_node
            self._size += 1

            return self._head

        new_node.next = self._head
        self._head = new_node
        self._size += 1

        return self._head

    def pop(self) -> Node:
        """Pops an item from the steque"""
        if not self._head:
            raise Exception("Cannot pop from an empty steque")

        new_head = self._head.next
        self._head = new_head
        self._size -= 1

        return self._head

    def enqueue(self, item: str) -> Node:
        """Enqueues an item onto the steque"""
        new_node = Node(item)

        if self.is_empty():
            self._head = new_node
            self._tail = new_node

            return new_node

        self._tail.next = new_node
        self._tail = new_node
        self._size += 1

        return new_node


# ---------------------------------------------------------------------------------------------------------


def main():
    """Testing"""
    test_steque = Steque()
    test_steque.enqueue("1")
    test_steque.enqueue("2")
    test_steque.push("0")

    test_steque.pop()

    head = test_steque.head
    print(head.next.item)


# ---------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    main()
