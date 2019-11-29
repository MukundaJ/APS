def solve_trouble(arr: [int], _len: int):
    """
    Checks if the array arr will be correctly sorted the proposed Trouble Sort
    algorithm.
    :param arr: The list to be sorted using trouble sort.
    :param _len: The length of the list.
    :return: 'OK' if arr would be sorted correctly sorted,
                else the index where the first error occurs.
    """
    # Array to hold the sorted even and odd position elements interleaved.
    interleaved = [None] * _len
    interleaved[::2] = sorted(arr[::2])
    interleaved[1::2] = sorted(arr[1::2])

    # Find the first error by checking where interleaved[x] > interleaved[x + 1]
    try:
        return next(idx for idx in range(_len - 1)
                    if interleaved[idx] > interleaved[idx + 1])

    # If no such index is found, the array is correctly sorted.
    except StopIteration:
        return 'OK'


def main():
    """
    Driver function.
    :return: None
    """
    # For every test case,
    for test_num in range(1, int(input()) + 1):
        # Get the length of the list,
        list_len = int(input())
        # Get teh factors.
        *arr, = map(int, input().split())
        # Solve if trouble sort works for the given input.
        result = solve_trouble(arr, list_len)
        # Output the result.
        print('Case #{}: {}'.format(test_num, result))


if __name__ == '__main__':
    main()
