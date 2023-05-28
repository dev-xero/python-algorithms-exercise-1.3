# github repository: https://github.com/dev-xero/python-algorithms-exercise-1.3

"""linked_list_remove_after.py
   Python algorithm to remove a node after a specified node in a linked-list if it exists
"""

# ---------------------------------------------------------------------------------------------------------


from data_structures.linked_list_ds import Node
from algorithms.traverse_and_print import traverse_and_print


# ---------------------------------------------------------------------------------------------------------


def remove_node_after(head: Node, key: Node) -> Node:
    """Traverses the linked list and returns the removed node if present"""
    current = head
    removed_node: Node | None = None

    if not head or not key:
        raise Exception("Needs both key and a starting node")

    while current.next:
        if current == key:
            node_after_current: Node | None = current.next
            current.next = node_after_current.next
            node_after_current.next = None

            removed_node = node_after_current
            return removed_node

        else:
            current = current.next

    return removed_node

# ---------------------------------------------------------------------------------------------------------


def main():
    """Testing"""
    head = Node("1")  # 1 -> 2 -> 3 -> 4 -> 5
    head.next = Node("2")
    head.next.next = Node("3")
    head.next.next.next = Node("4")
    head.next.next.next.next = Node("5")

    print("removed:", remove_node_after(head, head.next.next).item)

    traverse_and_print(head)


# ---------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    main()
