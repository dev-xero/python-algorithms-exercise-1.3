# Python algorithms exercise sub-1.3
🐍 Algorithms and data structures implemented while studying subchapter 1.3 written in Python

## Data Structures Implemented
1. Linked Lists (Singly)
2. Push Down Stack

## Algorithms Implemented
1. is_valid_parens()
2. is_circular_shift_of()

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
