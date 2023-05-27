# github repository: https://github.com/dev-xero/python-algorithms-exercise-1.3

"""reverse_linked_list.py
   Python algorithm to reverse a singly linked list
"""

# ---------------------------------------------------------------------------------------------------------


from data_structures.linked_list_ds import Node
from algorithms.traverse_and_print import traverse_and_print


# ---------------------------------------------------------------------------------------------------------


def reverse_linked_list(head: Node) -> None | Node:
    current = head
    previous = None

    while current is not None:
        next_node = current.next

        current.next = previous
        previous = current

        current = next_node

    return previous


# ---------------------------------------------------------------------------------------------------------


def main():
    """Testing"""
    head: Node = Node("1")  # linked list: 1 -> 2 -> 3 -> 4 -> 5
    head.next = Node("2")
    head.next.next = Node("3")
    head.next.next.next = Node("4")
    head.next.next.next.next = Node("5")

    traverse_and_print(head)
    reverse_linked_list(head)
    traverse_and_print(head)


# ---------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    main()
