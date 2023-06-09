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

    def remove_head(self) -> DoubleNode:
        """Removes the head from a linked-list and sets the next node as the head"""
        next_node = self.head.next
        next_node.prev = None
        self.head = next_node

        return next_node

    def remove_tail(self) -> None:
        """Removes the tail from a linked list and sets the previous node as the new tail"""
        new_last = self.tail.prev
        new_last.next = None
        self.tail = new_last

        return self.tail

    def remove_node(self, node: DoubleNode) -> DoubleNode:
        """Removes a node from a doubly linked list if it exists"""
        if type(node) is not DoubleNode:
            raise Exception("Node to remove must be a valid double node")

        curr_node = node
        prev_node = node.prev or None
        next_node = node.next or None

        while curr_node.next:
            if curr_node == node:
                if not curr_node.prev:
                    new_head = curr_node.next
                    new_head.prev = None
                    self.head = new_head

                    return self.head

                if not curr_node.next:
                    new_tail = curr_node.prev
                    new_tail.next = None
                    self.tail = new_tail

                    return self.head

                prev_node.next = next_node
                next_node.prev = prev_node

                curr_node.next = None
                curr_node.prev = None

                return self.head


# ---------------------------------------------------------------------------------------------------------

def main():
    """Testing"""
    from algorithms.traverse_and_print_doubly_linked_list import traverse_and_print

    linked_list = DoublyLinkedList()  # doubly linked list
    linked_list.prepend("5")
    linked_list.prepend("3")
    linked_list.prepend("2")
    linked_list.prepend("1")

    last = linked_list.append("9")
    fourth = last.prev  # node.item = 5

    linked_list.prepend_before(last, "8")
    linked_list.prepend_before(fourth, "4")

    linked_list.append_after(last, "10")
    linked_list.append_after(fourth, "6")
    linked_list.append_after(fourth, "7")

    linked_list.remove_head()
    linked_list.remove_tail()
    linked_list.remove_tail()

    head = linked_list.remove_node(fourth)  # removes 5

    traverse_and_print(head, "forward")


# ---------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    main()
