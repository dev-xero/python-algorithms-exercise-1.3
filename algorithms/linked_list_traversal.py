# github repository: https://github.com/dev-xero/python-algorithms-exercise-1.3

"""linked_list_traversal.py
   Python algorithm to locate a key in a linked-list
"""

# ---------------------------------------------------------------------------------------------------------


from data_structures.linked_list_ds import Node


# ---------------------------------------------------------------------------------------------------------


def traverse_and_search(key: str, start: Node) -> Node | None:
    """Traverses a linked list to locate a key, returns None if absent"""
    current = start

    while current.next is not None:
        if current.item == key:
            return current

        current = current.next

    return None


# ---------------------------------------------------------------------------------------------------------


def main():
    """Testing"""
    head = Node("first")  # first -> second -> third -> fourth -> fifth -> sixth
    head.next = Node("second")
    head.next.next = Node("third")
    head.next.next.next = Node("fourth")
    head.next.next.next.next = Node("fifth")
    head.next.next.next.next.next = Node("sixth")

    print(traverse_and_search("fifth", head).item)  # exists


# ---------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    main()
