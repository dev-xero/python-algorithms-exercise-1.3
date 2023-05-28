# github repository: https://github.com/dev-xero/python-algorithms-exercise-1.3

"""is_circular_shift_of.py
   Algorithm to check whether a string is a circular shift of another string
"""

# ---------------------------------------------------------------------------------------------------------


def is_circular_shift_of(a: str, b: str) -> bool:
    """Returns true if a string "a" is a circular rotation of another string "b" """
    return len(a) == len(b) and a in (b + b)


# ---------------------------------------------------------------------------------------------------------


def main():
    """Testing"""
    test_base_string = str(input("Enter base string: "))
    tst_shifted_string = str(input("Enter shifted string: "))

    print(is_circular_shift_of(tst_shifted_string, test_base_string))


# ---------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    main()
