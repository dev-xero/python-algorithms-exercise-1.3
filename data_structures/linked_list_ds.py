# github repository: https://github.com/dev-xero/python-algorithms-exercise-1.3

"""linked_list_ds.py
   Python implementation of a linked list data structure
"""

# ---------------------------------------------------------------------------------------------------------


class Node:
    """Linked list implementation in Python"""
    def __init__(self, item=None):
        """Setup"""
        self.item: str | None = item
        self.next: Node | None = None


# ---------------------------------------------------------------------------------------------------------


def main():
    """Testing"""
    head = Node("1")  # linked list: 1 -> 2 -> 3 -> 4 -> 5
    head.next = Node("2")
    head.next.next = Node("3")
    head.next.next.next = Node("4")
    head.next.next.next.next = Node("5")

    print(head.next.next.item)  # 3


# ---------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    main()
