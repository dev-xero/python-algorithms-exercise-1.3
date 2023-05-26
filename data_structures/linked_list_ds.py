# github repository: https://github.com/dev-xero/python-algorithms-exercise-1.3

"""linked_list_ds.py
   Python implementation of a linked list data structure
"""

# ---------------------------------------------------------------------------------------------------------


class Node:
    def __init__(self):
        """Setup"""
        self.item: str | None = None
        self.next: Node | None = None

# ---------------------------------------------------------------------------------------------------------


def main():
    """Testing"""
    first = Node()
    second = Node()
    third = Node()

    first.item = "first"
    second.item = "second"
    third.item = "third"

    first.next = second
    second.next = third

    print(first.next.next.item)


# ---------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    main()
