# github repository: https://github.com/dev-xero/python-algorithms-exercise-1.3

"""remove_all_from_linked_list.py
   Python algorithm to remove all occurrences of a key if present
"""

# ---------------------------------------------------------------------------------------------------------


from data_structures.linked_list_ds import Node
from algorithms.traverse_and_print import traverse_and_print


# ---------------------------------------------------------------------------------------------------------


def remove_all_from_linked_list(key: str, head: Node) -> Node:
    if head is None:
        raise Exception("Cannot remove from an empty linked list")

    while head is not None and head.item == key:
        head = head.next

    current = head
    previous = None

    while current:
        if current.item == key:
            if previous is not None:
                previous.next = current.next

            current = current.next

        else:
            previous = current
            current = current.next

    return head


# ---------------------------------------------------------------------------------------------------------


def main():
    """Testing"""
    head = Node("1")  # linked list: 1 -> 2 -> 1 -> 3 -> 1
    head.next = Node("2")
    head.next.next = Node("1")
    head.next.next.next = Node("3")
    head.next.next.next.next = Node("1")

    new_head = remove_all_from_linked_list("1", head)

    traverse_and_print(new_head)


# ---------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    main()
