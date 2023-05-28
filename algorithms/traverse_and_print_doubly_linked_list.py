# https://github.com/dev-xero/python-algorithms-exercise-1.3

"""traverse_and_print_doubly_linked_list.py
   Python algorithm to traverse and print the contents of a doubly linked list
"""

# ---------------------------------------------------------------------------------------------------------


from data_structures.doubly_linked_lists_ds import DoubleNode


# ---------------------------------------------------------------------------------------------------------


def traverse_and_print(head: DoubleNode, order: str = "forward"):
    """Traverses and prints the contents of a doubly linked list in a specific order"""
    current = head

    if order == "reverse":
        while current:
            print(current.item, end=" ")
            current = current.prev

    else:
        while current:
            print(current.item, end=" ")
            current = current.next


# ---------------------------------------------------------------------------------------------------------


def main():
    """Testing"""
    head = DoubleNode("1")  # doubly linked list
    head.next = DoubleNode("2")
    head.next.prev = head
    head.next.next = DoubleNode("3")
    head.next.next.prev = head.next
    head.next.next.next = DoubleNode("4")
    head.next.next.next.prev = head.next.next

    traverse_and_print(head.next.next, "reverse")  # 3 -> 2 -> 1


# ---------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    main()
