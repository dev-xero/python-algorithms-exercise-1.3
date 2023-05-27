# github repository: https://github.com/dev-xero/python-algorithms-exercise-1.3

"""traverse_and_print.py
   Python algorithm to traverse a linked list and print the items stored in the nodes
"""

# ---------------------------------------------------------------------------------------------------------


from data_structures.linked_list_ds import Node


# ---------------------------------------------------------------------------------------------------------


def traverse_and_print(start: Node) -> None:
    """Traverses and prints the items in the node of a linked list"""
    if not start or type(start) is not Node:
        raise Exception("A valid node must be specified")

    current = start

    while current:
        print(f"{current.item} ", end="")
        current = current.next


# ---------------------------------------------------------------------------------------------------------


def main():
    """Testing"""
    first: Node = Node()
    second: Node = Node()
    third: Node = Node()
    fourth: Node = Node()
    fifth: Node = Node()

    first.item = "first"
    second.item = "second"
    third.item = "third"
    fourth.item = "fourth"
    fifth.item = "fifth"

    first.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth

    traverse_and_print(first)


# ---------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    main()
