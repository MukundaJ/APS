def change(amount: int, coins: [int]) -> int:
    """
    Calculates the number of ways (different combinations of coin denominations)
    an amount can be made up.
    :param amount: The total amount to be made up.
    :param coins: The denominations of the coins available
    :return:
    """
    # DP array to hold the number of ways an amount i can be made up, where i is
    # the index of the array.
    # Base case, there is only 1 way to make an amount = 0,
    # i.e. select nothing.
    combinations = [1] + [0] * (amount - 1)

    # For all available denominations,
    for denomination in coins:
        # For all the amounts, upto the given amount,
        for amt in range(amount):
            # we check if this denomination can make up something <= amount ?
            # if yes, then the number of ways to make up (amt + denomination) =
            # number of ways to make up amt,
            # so we accumulate the total number of ways to make up any amount i.
            if amt + denomination <= amount:
                combinations[amt + denomination] += combinations[amt]

    # return the total number of ways to make up the amount.
    return combinations[amount]
