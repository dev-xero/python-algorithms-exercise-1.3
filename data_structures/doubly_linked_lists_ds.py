# github repository: https://github.com/dev-xero/python-algorithms-exercise-1.3

"""doubly_linked_lists_ds.py
   Python implementation of a doubly linked list
"""

# ---------------------------------------------------------------------------------------------------------


class DoublyLinkedList:
    """Python implementation of a doubly linked list"""
    class Node:
        """Node definition for doubly linked lists"""
        def __init__(self, item: str = None):
            self.item = item
            self.next = None
            self.prev = None

    def __init__(self):
        """Setup"""
        self.head = None
        self.tail = None

    def prepend(self, item: str) -> Node:
        """Prepend an item to the linked list before head"""
        new_node = self.Node(item)

        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        return self.head


# ---------------------------------------------------------------------------------------------------------


def main():
    """Testing"""
    head = DoublyLinkedList()  # doubly linked list
    head.prepend("4")
    head.prepend("3")
    head.prepend("2")
    a = head.prepend("1")

    print(a.next.next.next.item)

# ---------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    main()
