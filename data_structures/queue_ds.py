# github repository: https://github.com/dev-xero/python-algorithms-exercise-1.3

"""queue_ds.py
   Python implementation of a queue data structure
"""

# ---------------------------------------------------------------------------------------------------------


from data_structures.linked_list_ds import Node


# ---------------------------------------------------------------------------------------------------------


class Queue:
    def __init__(self):
        self._first: Node | None = None
        self._last: Node | None = None
        self._size: int = 0

    def is_empty(self) -> None:
        return self._first is None

    @property
    def size(self) -> int:
        return self._size

    def enqueue(self, item: str) -> None:
        new_node = Node()
        new_node.item = item

        if self.is_empty():
            self._first = new_node
            self._last = new_node

        else:
            self._last.next = new_node
            self._last = new_node

        self._size += 1

    def dequeue(self) -> str:
        if self.is_empty():
            raise IndexError("Cannot dequeue from an empty queue")

        first = self._first
        self._first = first.next
        self._size -= 1

        return first.item


# ---------------------------------------------------------------------------------------------------------


def main():
    """Testing"""
    test_queue = Queue()

    test_queue.enqueue("this")
    test_queue.enqueue("is")
    test_queue.enqueue("a")
    test_queue.enqueue("queue")

    print(test_queue.dequeue())
    print(test_queue.dequeue())
    print(test_queue.dequeue())
    print(test_queue.size)

# ---------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    main()
