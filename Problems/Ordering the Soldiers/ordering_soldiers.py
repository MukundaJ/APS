def order_soldiers(n: int, w: [int]) -> [int]:
    """
    Finds the initial ordering the soldiers arrived in given the how much each
    soldier has to move to the left to get the final ordering.
    :param n: The number of soldiers.
    :param w: The number of people each soldier has to move to the left before
    no superior is to the left of him.
    :return: The initial arrangement of the soldiers
    """

    # Array to hold the arrangement after the soldiers move the required steps.
    final_pos = []

    # Simulate the moving of a soldier to their final position,
    # the index of the array is the rank of the soldier, and the value is the
    # position where the soldier was initially.
    for i in range(n): final_pos.insert(i - w[i], i)

    # Array to store the initial order the soldier arrived in.
    initial_order = [_ for _ in range(n)]

    # After moving, the soldiers are now in increasing order of rank,
    # and we know where they were initially from the values in final_pos.
    for i in range(n): initial_order[final_pos[i]] = i + 1

    # return the initial order the soldiers were in.
    return initial_order


def order_soldiers_one_pass(n: int, w: [int]) -> [int]:
    """
    Finds the initial ordering the soldiers arrived in given the how much each
    soldier has to move to the left to get the final ordering.
    :param n: The number of soldiers.
    :param w: The number of people each soldier has to move to the left before
    no superior is to the left of him.
    :return: The initial arrangement of the soldiers
    """
    # Array holding the the final ranking position.
    ranks = [i for i in range(1, n + 1)]
    # The initial order would then be,
    # rank at (end of ranks array - steps moved to left).
    for i in range(n - 1, -1, -1): w[i] = ranks.pop(i - w[i])
    # return the initial order the soldiers were in.
    return w


def main():
    """
    Driver function.
    :return: None
    """
    # For all test cases,
    for _ in range(int(input().strip())):
        # Get the number of soldiers.
        n = int(input().strip())
        # Get how much each soldier has to move to the left.
        w = list(map(int, input().strip().split()))
        # Get the initial ordering of the soldiers.
        result = order_soldiers_one_pass(n, w)
        # Output the result.
        print(*result)


if __name__ == '__main__':
    main()
