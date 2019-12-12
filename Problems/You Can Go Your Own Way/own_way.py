def invert_path(P: str) -> str:
    """
    Inverts the given path P
    :param P: The path taken by Lydia.
    :return: The path to that does not overlap with P.
    """
    # Dictionary to invert the given moves,
    # East to South and South to East.
    _invert = {'E': 'S', 'S': 'E'}
    return ''.join(_invert[p] for p in P)


def main():
    """
    Driver function.
    :return: None
    """
    # For all the test cases
    for t in range(1, int(input()) + 1):
        # Get the path length
        N = int(input())
        # Get the path
        P = input()
        result = invert_path(P)
        # Output the result.
        print("Case #{}: {}".format(t, result))


if __name__ == '__main__':
    main()
