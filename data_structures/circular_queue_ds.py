# github repository: https://github.com/dev-xero/python-algorithms-exercise-1.3

"""circular_queue_ds.py
   Python implementation of a queue using a circular linked list
"""

# ---------------------------------------------------------------------------------------------------------


from data_structures.linked_list_ds import Node


# ---------------------------------------------------------------------------------------------------------


class CircularQueue:
    """A queue data structure implementation utilizing a circular linked list"""
    def __init__(self):
        """Setup"""
        self._first: Node | None = None
        self._last: Node | None = None
        self._size: int = 0

    def is_empty(self) -> None:
        """Returns true if the first item is None, false otherwise"""
        return self._first is None

    @property
    def size(self) -> int:
        """Returns the size of the queue"""
        return self._size

    def enqueue(self, item: str) -> None:
        """Enqueues an item"""
        new_node = Node(item)

        if self.is_empty():
            self._first = new_node
            new_node.next = self._first
            self._last = new_node

        else:
            new_node.next = self._first
            self._last.next = new_node
            self._last = new_node

        self._size += 1

    def dequeue(self) -> str:
        """Dequeues an item if the queue is not empty"""
        if self.is_empty():
            raise Exception("Cannot dequeue from an empty circular queue")

        old_first = self._first
        self._first = old_first.next
        self._last.next = self._first
        self._size -= 1

        return old_first.item


# ---------------------------------------------------------------------------------------------------------


def main():
    """Testing"""
    test_queue: CircularQueue = CircularQueue()

    test_queue.enqueue("1")
    test_queue.enqueue("2")
    test_queue.enqueue("3")
    test_queue.enqueue("4")
    test_queue.enqueue("5")

    print(test_queue.size)
    print(test_queue.dequeue())
    print(test_queue.dequeue())
    print(test_queue.dequeue())

    print(test_queue.size)


# ---------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    main()
