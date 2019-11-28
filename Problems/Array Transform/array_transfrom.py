from collections import Counter


def solve_array_trm(n: int, k: int, nums: [int]) -> str:
    """
    Checks if it is possible to transform the array with the specified
    operation.
    :param n: The length of the list.
    :param k: The increment value for the operation.
    :param nums: The array to be transformed.
    :return: 'YES' if it is possible to transform the array with the specified
    operation else 'NO'.
    """
    # If there is just 1 or 2 (i.e. n == 1 or 2) element,
    # then 0 or 1 (i.e. n - 1 == 0 or 1) elements should be 0,
    # so the all unit length arrays satisfy the condition, and for 2 length
    # arrays, we can keep selecting one number to decrement to 0 trivially.
    # Otherwise,
    # We find the remainder on dividing each of the numbers by (k + 1),
    # essentially mapping them to a number space of [0, k].
    # We then count how many elements have the same remainder
    # (i.e. get mapped to the same number when transformed to a [0, k] space).
    # If n - 1 or more numbers have the same remainder / mapping, then it is
    # possible to transform the array.
    if n < 3 or max(Counter(x % (k + 1) for x in nums).values()) >= n - 1:
        return 'YES'
    return 'NO'


def main():
    """
    Driver function.
    :return: None
    """
    # For all test cases,
    for _ in range(int(input())):
        # Get n and k,
        # where n is the number of numbers given in the test-case
        # and k is the increment value.
        n, k = map(int, input().split())
        # Get list of the numbers to check.
        nums = list(map(int, input().split()))
        # Check if the operation is possible or not.
        res = solve_array_trm(n, k, nums)
        # Output the result.
        print(res)


if __name__ == '__main__':
    main()
