from functools import reduce
from operator import mul


def beadOrnaments(b):
    """
    Finds the number of ways 'labeled' beads of len(b) diff colors can be
    arranged.
    :param b: A list representing how many beads of each colors are to be
    arranged.
    :return: The total number of ways the beads can be arranged.
    """
    # The number of ways to arrange n labeled nodes in a tree is given by
    # caley's formula as n^(n-2).
    # We then account for the number of ways to arrange these trees among each
    # given as b(0) * b(1) * ... * b(n) * (b(0) + b(1) + ... + b(n))^(n -2).
    # adding the number of ways to arrange labeled nodes using caley's formula,
    # we have b(0)^(b(0) - 1) * b(1)^(b(1) - 1) * ... * b(n)^(b(n) - 1) *
    # (b(0) + b(1) + ... + b(n))^(n -2).
    return int(reduce(mul, map(lambda x: x ** (x - 1), b)) *
               (sum(b) ** (len(b) - 2)) % (10 ** 9 + 7))
