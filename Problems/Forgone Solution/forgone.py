def forgone(N: str) -> (int, int):
    """
    Finds two number A and B that add upto N.
    :param N: The number to be made
    :return: A, B where A + B = N
    """
    # Copy N to A
    A = list(N)
    # make a list of 0's
    B = ['0'] * len(A)
    # For every number in N,
    # we decrement if we spot a 4 and convert the respective digit in B to 1
    for i in range(len(A)):
        if A[i] == '4': A[i], B[i] = '3', '1'

    # return the result.
    return ''.join(A), ''.join(B).lstrip('0')


def main():
    """
    Driver function
    :return: None
    """
    # For all the test cases,
    for t in range(1, int(input()) + 1):
        # get the number ot be made
        N = input().strip()
        # Find the numbers the that add up N and have no value 4.
        A, B = forgone(N)
        # output the result.
        print("Case #%d: %s %s" % (t, A, B))


if __name__ == '__main__':
    main()
