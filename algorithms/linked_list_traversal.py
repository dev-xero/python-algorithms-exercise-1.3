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
    first = Node()
    second = Node()
    third = Node()
    fourth = Node()
    fifth = Node()
    sixth = Node()

    first.item = "first"
    second.item = "second"
    third.item = "third"
    fourth.item = "fourth"
    fifth.item = "fifth"
    sixth.item = "sixth"

    first.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    fifth.next = sixth

    print(traverse_and_search("fifth", first))


# ---------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    main()
