# github repository: https://github.com/dev-xero/python-algorithms-exercise-1.3

"""josephus_problem.py
   A solution to the josephus problem
"""

# ---------------------------------------------------------------------------------------------------------


from data_structures.queue_ds import Queue


# ---------------------------------------------------------------------------------------------------------


def josephus(num: int, eliminate_every: int) -> Queue:
    """Algorithm showing the execution order when eliminating an item at a specific distance"""
    if eliminate_every >= num:
        raise Exception("Elimination step must be less than the number of people")

    execution_order = Queue()
    starting_arr = [num for num in range(num)]
    i = -1

    while execution_order.size < num:
        next_pos = (i + eliminate_every) % num
        next_num = starting_arr[next_pos]

        if next_num != -1:
            execution_order.enqueue(str(next_num))
            starting_arr[next_pos] = -1
            i = next_pos
            continue

        i = next_pos + eliminate_every - 1

    return execution_order


# ---------------------------------------------------------------------------------------------------------


def main():
    """Testing"""
    number_of_people = int(input("Number of people: "))
    eliminate_every = int(input("Eliminate every (num) person: "))
    ex_order = josephus(number_of_people, eliminate_every)

    while not ex_order.is_empty():
        print(ex_order.dequeue(), end=" ")


# ---------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    main()
