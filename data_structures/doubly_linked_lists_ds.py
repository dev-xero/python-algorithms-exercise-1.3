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
        self.head: None | DoublyLinkedList.Node = None
        self.tail: None | DoublyLinkedList.Node = None

    def prepend(self, item: str) -> Node:
        """Prepends an item to the start of the list"""
        new_node = self.Node(item)

        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        return self.head

    def append(self, item: str) -> Node:
        """Appends an item at the end of the linked list"""
        new_node = self.Node(item)

        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.next = None
            new_node.prev = self.tail

            self.tail.next = new_node
            self.tail = new_node

        return self.tail

    def prepend_before(self, node: Node, item: str) -> Node:
        """Prepends an item before a node in the linked list if it exists"""
        if node is None:
            raise Exception("Cannot prepend before an empty node")

        current = node

        while current:
            if current == node:
                new_node = self.Node(item)

                new_node.prev = current.prev
                new_node.next = current

                if current.prev:
                    current.prev.next = new_node

                else:
                    self.head = new_node

                current.prev = new_node

                return new_node

            current = current.prev

        return current


# ---------------------------------------------------------------------------------------------------------


def main():
    """Testing"""
    head = DoublyLinkedList()  # doubly linked list
    head.prepend("4")
    head.prepend("3")
    head.prepend("2")
    head.prepend("1")

    last = head.append("5")
    second = last.prev.prev.prev

    head.prepend_before(last, "4.5")
    head.prepend_before(second, "1.5")

    current = head.head

    while current:
        print(current.item, end=" ")
        current = current.next


# ---------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    main()
