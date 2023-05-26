# github repository: https://github.com/dev-xero/python-algorithms-exercise-1.3

"""is_valid_parens.py
   Python algorithm to check whether a string of parentheses is balanced and nested
"""

# ---------------------------------------------------------------------------------------------------------


from data_structures.stack_ds import Stack


# ---------------------------------------------------------------------------------------------------------


def is_valid_parens(string: str) -> bool:
    """Returns true if the string contains balanced parentheses"""
    parens_map: dict[str, str] = {
        "(" : ")",
        "{" : "}",
        "[" : "]"
    }
    opening_parens_stack = Stack()

    for paren in string:
        if paren in parens_map.keys():
            opening_parens_stack.push(paren)

        else:
            if paren == parens_map.get(opening_parens_stack.peek().item):
                opening_parens_stack.pop()

    return opening_parens_stack.is_empty()


# ---------------------------------------------------------------------------------------------------------


def main():
    """Testing"""
    test_string = "[()]{}{[()()]()}"
    print(is_valid_parens(test_string))


# ---------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    main()
