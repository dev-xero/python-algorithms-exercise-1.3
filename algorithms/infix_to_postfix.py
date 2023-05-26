# github repository: https://github.com/dev-xero/python-algorithms-exercise-1.3

"""is_valid_parens.py
   Python algorithm to convert a fully parenthesized infix expression to postfix notation
"""

# ---------------------------------------------------------------------------------------------------------


from data_structures.stack_ds import Stack
from algorithms.infix_expression import to_infix


# ---------------------------------------------------------------------------------------------------------


def to_postfix(expression: str) -> str:
    """Returns the postfix equivalent of a fully parenthesized infix expression"""
    infix_expression = to_infix(expression)  # convert to a valid infix
    expression_array = infix_expression.split(" ")

    stack: Stack = Stack()
    operators = ["+", "-", "*", "/"]

    for char in expression_array:
        if char == ")":
            right_operand = stack.pop()
            operator = stack.pop()
            left_operand = stack.pop()

            res = f"{left_operand} {right_operand} {operator} "

            stack.push(res)

        if char in operators or char.isnumeric():
            stack.push(char)

    return stack.pop()


# ---------------------------------------------------------------------------------------------------------


def main():
    """Testing"""
    infix_expression = str(input("Enter infix expression: "))  # ( ( 1 + 2 ) * 3 ) - 4 ) works
    postfix_expression = to_postfix(infix_expression)

    print(postfix_expression)


# ---------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    main()
