# github repository: https://github.com/dev-xero/python-algorithms-exercise-1.3

"""is_circular_shift_of.py
   Algorithm to check whether a string is a circular shift of another string
"""

# ---------------------------------------------------------------------------------------------------------


def is_circular_shift_of(a: str, b: str) -> bool:
    """Returns true if a string "b" is a circular rotation of another string "a" """
    return len(a) == len(b) and b in (a + a)


# ---------------------------------------------------------------------------------------------------------


def main():
    """Testing"""
    test_string_a = "AWARD"
    test_string_b = "WARDA"

    print(is_circular_shift_of(test_string_a, test_string_b))


# ---------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    main()
