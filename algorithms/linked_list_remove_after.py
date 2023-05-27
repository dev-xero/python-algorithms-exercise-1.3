# github repository: https://github.com/dev-xero/python-algorithms-exercise-1.3

"""linked_list_remove_after.py
   Python algorithm to remove a node after a specified node in a linked-list if it exists
"""

# ---------------------------------------------------------------------------------------------------------


from data_structures.linked_list_ds import Node
from algorithms.traverse_and_print import traverse_and_print


# ---------------------------------------------------------------------------------------------------------


def remove_node_after(start: Node, key: Node) -> Node:
    """Traverses the linked list and returns the removed node if present"""
    current = start
    removed_node: Node | None = None

    if not start or not key:
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
    node_one = Node()
    node_two = Node()
    node_three = Node()
    node_four = Node()
    node_five = Node()

    node_one.item = "1"
    node_two.item = "2"
    node_three.item = "3"
    node_four.item = "4"
    node_five.item = "5"

    node_one.next = node_two
    node_two.next = node_three
    node_three.next = node_four
    node_four.next = node_five

    print("removed: ", remove_node_after(node_one, node_three).item)

    traverse_and_print(node_one)


# ---------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    main()
