# github repository: https://github.com/dev-xero/python-algorithms-exercise-1.3

"""eval_postfix.py
   Python algorithm to evaluate a valid postfix expression
"""

# ---------------------------------------------------------------------------------------------------------


from data_structures.stack_ds import Stack


# ---------------------------------------------------------------------------------------------------------


def eval_postfix(postfix_expression: str) -> int:
    postfix_expression_array = postfix_expression.split(" ")
    stack: Stack = Stack()
    operators = ["+", "-", "*", "/"]

    for char in postfix_expression_array:
        if char in operators:
            right_operand = int(stack.pop())
            operator = char
            left_operand = int(stack.pop())

            res = 0

            if operator == "+":
                res = left_operand + right_operand

            elif operator == "-":
                res = left_operand - right_operand

            elif operator == "*":
                res = left_operand * right_operand

            elif operator == "/":
                res = left_operand / right_operand

            stack.push(str(res))

        elif char in operators or char.isnumeric():
            stack.push(char)

    return int(stack.pop())


# ---------------------------------------------------------------------------------------------------------


def main():
    """Testing"""
    test_postfix = str(input("Enter postfix expression: "))  # 5 2 + 4 3 - * works
    print(eval_postfix(test_postfix))


# ---------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    main()
