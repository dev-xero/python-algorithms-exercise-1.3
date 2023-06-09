# github repository: https://github.com/dev-xero/python-algorithms-exercise-1.3

"""traverse_and_print.py
   Python algorithm to traverse a linked list and print the items stored in the nodes
"""

# ---------------------------------------------------------------------------------------------------------


from data_structures.linked_list_ds import Node


# ---------------------------------------------------------------------------------------------------------


def traverse_and_print(head: Node) -> None:
    """Traverses and prints the items in the node of a linked list"""
    if not head or type(head) is not Node:
        raise Exception("A valid node must be specified")

    current = head

    while current:
        print(f"{current.item} ", end="")
        current = current.next


# ---------------------------------------------------------------------------------------------------------


def main():
    """Testing"""
    head = Node("first")  # linked list: first -> second -> third -> fourth -> fifth
    head.next = Node("second")
    head.next.next = Node("third")
    head.next.next.next = Node("fourth")
    head.next.next.next.next = Node("fifth")

    traverse_and_print(head)


# ---------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    main()
