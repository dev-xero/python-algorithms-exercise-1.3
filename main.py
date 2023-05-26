# github repository: https://github.com/dev-xero/python-algorithms-exercise-1.3

"""main.py
   Python implementation of the exercises found in subchapter 1.3
"""

# ---------------------------------------------------------------------------------------------------------


from algorithms.is_valid_parens import is_valid_parens


# ---------------------------------------------------------------------------------------------------------


def main():
    """Testing"""
    balanced_parens_string = "(({[()]})[])"
    print(is_valid_parens(balanced_parens_string))  # the string is balanced


# ---------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    main()
