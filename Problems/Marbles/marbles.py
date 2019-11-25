from functools import reduce
from operator import mul


def marbles(n: int, k: int) -> int:
    """
    Calculates the number of possibilities of selecting n marbles, where there
    is at least 1 marble for each color k.
    :param n: The number of marbles to be selected.
    :param k: The number of colors of marbles available.
    :return: The number of possibilities of selecting the marbles given the
    constraints in the problem.
    """
    # return (n-1) Choose (k - 1)
    # which is the number of possibilities with the given constraints.
    return n_choose_k(n - 1, k - 1)


def n_choose_k(n: int, k: int) -> int:
    """
    Calculates n Choose k,
    where Choose is defined as nCk = n! / ((k!) * (n - k)!).
    This is further reduced to
    nCk = prod(range(n, n - k - 1)) / prod(range(1, k))
    :param n: The number of possible options to choose from.
    :param k: The number of choices to make.
    :return: nCk
    """
    # Edge case, no possible way to choose.
    if k > n or k < 0 or n < 0: return 0
    # We choose the min of k or n - k
    # since nCk == nC(n - k).
    k = min(k, n - k)
    # The numerator represents the product
    # n * (n - 1) * (n - 2) * ... * (n - k - 1)
    numerator = reduce(mul, range(n, n - k, -1), 1)
    # The denominator represents the product
    # 1 * 2 * ... * k
    denominator = reduce(mul, range(1, k + 1), 1)
    # return the result as an integer.
    return numerator // denominator


def main():
    """
    Driver function.
    :return: None
    """
    # For all the test cases.
    for _ in range(int(input())):
        # n -> number of marbles to be chosen,
        # k -> number of colors.
        n, k = map(int, input().split())
        # Find the number of possibilities.
        result = marbles(n, k)
        # Print the result.
        print(result)


if __name__ == '__main__':
    main()
