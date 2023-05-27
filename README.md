# Python algorithms exercise sub-1.3
🐍 Algorithms and data structures implemented while studying subchapter 1.3 written in Python

## Data Structures Implemented
1. Linked Lists (Singly)
2. Push Down Stack
3. Queue

## Algorithms Implemented
1. is_valid_parens()
2. is_circular_shift_of()
3. to_infix()
4. to_postfix()
5. eval_postfix()
6. traverse_and_search()
7. linked_list_remove_after()
8. traverse_and_print()
9. reverse_linked_list()
10. recursive_reverse_linked_list()

## Code Examples
Some code examples of the algorithms and data structures implemented.  

### 1. Linked List Node
```python3
    class Node:
    """Linked list implementation in Python"""
    def __init__(self):
        """Setup"""
        self.item: str | None = None
        self.next: Node | None = None
```

### 2. is_valid_parens()
```python3
    balanced_parens_string = "(({[()]})[])"
    print(is_valid_parens(balanced_parens_string))  # the string is balanced
```

### 3. recursive_reverse_linked_list()
```python3
    def recursive_reverse_linked_list(head: Node) -> Node | None:
        """Recursively reverses a linked list"""
        if head is None or head.next is None:
            return head

        reversed_list = recursive_reverse_linked_list(head.next)

        head.next.next = head
        head.next = None

        return reversed_list
```
