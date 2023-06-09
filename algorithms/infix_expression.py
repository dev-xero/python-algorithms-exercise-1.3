# github repository: https://github.com/dev-xero/python-algorithms-exercise-1.3

"""infix_expression.py
   Python algorithm to fully parenthesize an infix expression string
"""

# ---------------------------------------------------------------------------------------------------------


from data_structures.stack_ds import Stack


# ---------------------------------------------------------------------------------------------------------


def to_infix(expression: str) -> str:
    """Properly parenthesizes a non-infix expression"""
    stack = Stack()
    operators = ["+", "-", "/", "*"]

    expression_array = expression.split(" ")

    for char in expression_array:
        if char == ")":
            right_operand = stack.pop()
            operator = stack.pop()
            left_operand = stack.pop()

            res = f"({left_operand}{operator}{right_operand})"

            stack.push(res)

        elif char in operators:
            stack.push(char)

        else:
            stack.push(char)

    return " ".join(stack.pop())


# ---------------------------------------------------------------------------------------------------------


def main():
    """Testing"""
    expression = str(input("Enter the expression: "))  # 1 + 2 ) * 3 - 4 ) * 5 - 6 ) ) ) works
    infix_expression = to_infix(expression)

    print(infix_expression)


# ---------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    main()
