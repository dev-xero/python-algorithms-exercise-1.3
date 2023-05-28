# github repository: https://github.com/dev-xero/python-algorithms-exercise-1.3

"""linked_list_max.py
   Python algorithm to return the max item in a linked-list
"""

# ---------------------------------------------------------------------------------------------------------


from data_structures.linked_list_ds import Node
from algorithms.traverse_and_print import traverse_and_print


# ---------------------------------------------------------------------------------------------------------


def linked_list_max(head: Node) -> int:
    """Returns the max item in a linked list, returns 0 if head is empty"""
    max_item: int = 0
    if head is None:
        raise Exception("Cannot find max from an empty linked list")

    current = head

    while current:
        if int(current.item) > max_item:
            max_item = int(current.item)

        current = current.next

    return max_item


# ---------------------------------------------------------------------------------------------------------


def main():
    """Testing"""
    head = Node("1")   # linked-list: 1 -> 2 -> 7 -> 4 -> 5
    head.next = Node("2")
    head.next.next = Node("7")
    head.next.next.next = Node("4")
    head.next.next.next.next = Node("5")

    traverse_and_print(head)
    print()
    print("max:", linked_list_max(head))


# ---------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    main()
