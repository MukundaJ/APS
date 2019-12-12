from sys import stdin


def bytelandian_convert(amount: int) -> int:
    """
    Finds the maximum amount of american dollars we cna buy by changing the
    bytelandian gold coin as specified.
    :param amount: The value of bytelandian gold coin we have.
    :return: The maximum number of american dollars we can make.
    """
    # memo to hold the results.
    memo = {0: 0, 1: 1}

    def _helper(amt: int) -> int:
        """
        Helper function to perform a dfs like search by getting the max at each
        amount, by keeping on reducing it to the base amounts we have.
        :param amt: The value of bytelandian gold coin we have.
        :return: The maximum number of american dollars we can make.
        """
        # If we already have the max we can make using that amount, return it
        if amt in memo:
            return memo[amt]
        # Other wise find the max amount we can make for it using the given
        # number of ways.
        else:
            memo[amt] = max(amt,
                            _helper(amt // 2) + _helper(amt // 3) + _helper(
                                amt // 4))
            return memo[amt]

    # return the result.
    return _helper(amount)


def main():
    """
    Driver function.
    :return: None
    """
    for case in stdin:
        amount = int(case)
        result = bytelandian_convert(amount)
        print(result)


if __name__ == '__main__':
    main()
