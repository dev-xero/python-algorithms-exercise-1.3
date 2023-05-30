# https://github.com/dev-xero/python-algorithms-exercise-1.3

"""spiral_matrix.py
   Python algorithm to walk a matrix
"""

# ---------------------------------------------------------------------------------------------------------


def spiral_matrix(the_matrix: [[int]]) -> [int]:
    """Algorithm to return the path when traversing a matrix in a clock-wise spiral"""
    path: [int] = []

    rows = len(the_matrix)
    cols = len(the_matrix[0])

    direction = 0  # 0 -> right, 1 -> down, 2 -> left, 3 -> up

    top = 0
    right = cols - 1
    left = 0
    bottom = rows - 1

    while top <= bottom and left <= right:
        if direction == 0:
            for i in range(left, right + 1):
                path.append(the_matrix[top][i])

            top += 1
            direction = 1  # move down next

        if direction == 1:
            for i in range(top, bottom + 1):
                path.append(the_matrix[i][right])

            right -= 1
            direction = 2  # move left next

        if direction == 2:
            for i in range(right, left - 1, -1):
                path.append(the_matrix[bottom][i])

            bottom -= 1
            direction = 3  # move up next

        if direction == 3:
            for i in range(bottom, top - 1, -1):
                path.append(the_matrix[i][left])

            left += 1
            direction = 0

    return path


# ---------------------------------------------------------------------------------------------------------


def main():
    """Testing"""
    test_matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]

    print(spiral_matrix(test_matrix))


# ---------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    main()
