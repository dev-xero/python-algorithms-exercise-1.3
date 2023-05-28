# github repository: https://github.com/dev-xero/python-algorithms-exercise-1.3

"""doubly_linked_lists_ds.py
   Python implementation of a doubly linked list
"""

# ---------------------------------------------------------------------------------------------------------


class DoubleNode:
    """Node definition for doubly linked lists"""
    def __init__(self, item: str = None):
        self.item = item
        self.next = None
        self.prev = None


# ---------------------------------------------------------------------------------------------------------


class DoublyLinkedList:
    """Python implementation of a doubly linked list"""
    def __init__(self):
        """Setup"""
        self.head: None | DoubleNode = None
        self.tail: None | DoubleNode = None

    def prepend(self, item: str) -> DoubleNode:
        """Prepends a node to the start of the list"""
        new_node = DoubleNode(item)

        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        return self.head

    def append(self, item: str) -> DoubleNode:
        """Appends a node at the end of the linked list"""
        new_node = DoubleNode(item)

        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.next = None
            new_node.prev = self.tail

            self.tail.next = new_node
            self.tail = new_node

        return self.tail

    def prepend_before(self, node: DoubleNode, item: str) -> DoubleNode:
        """Prepends a node before another node in the linked list if it exists"""
        if node is None:
            raise Exception("Cannot prepend before an empty node")

        current = node

        while current:
            if current == node:
                new_node = DoubleNode(item)

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

    def append_after(self, node: DoubleNode, item: str) -> DoubleNode:
        """Appends a node after another node in the linked list if present"""
        if node is None:
            raise Exception("Cannot append after an empty node")

        current = node

        while current:
            if current == node:
                new_node = DoubleNode(item)
                new_node.prev = current

                if current.next:
                    current.next.prev = new_node
                    new_node.next = current.next

                else:
                    self.tail = new_node

                current.next = new_node

                return new_node

            current = current.next


# ---------------------------------------------------------------------------------------------------------

def main():
    """Testing"""
    from algorithms.traverse_and_print_doubly_linked_list import traverse_and_print

    head = DoublyLinkedList()  # doubly linked list
    head.prepend("5")
    head.prepend("3")
    head.prepend("2")
    head.prepend("1")

    last = head.append("9")
    fourth = last.prev

    head.prepend_before(last, "8")
    head.prepend_before(fourth, "4")

    head.append_after(last, "10")
    head.append_after(fourth, "6")
    head.append_after(fourth, "7")

    traverse_and_print(last.next, "reverse")


# ---------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    main()
