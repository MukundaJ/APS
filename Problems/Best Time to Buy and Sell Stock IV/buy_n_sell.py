def maxProfit(k: int, prices: [int]) -> int:
    """
    Calculates the maximum profit that can be made with at most k transactions.
    :param k: The maximum number of transactions allowed.
    :param prices: The array holding the stock price at time i.
    :return: The maximum profit that can be made with at most k transactions.
    """
    # The total prices
    n = len(prices)
    # If the number of transactions is greater than n // 2,
    # we can make all the possible transactions.
    if k >= n // 2:
        # var to hold the profit initially profit = 0
        profit = 0
        # For all the prices,
        for i in range(1, n):
            # The transaction is profitable if we can buy at a lesser price
            # than sell.
            if prices[i - 1] < prices[i]:
                # Make the transaction is profitable and add to profit.
                profit += prices[i] - prices[i - 1]
        # return the maximum profit.
        return profit
    # Array to hold
    # 1. profit when making at most i transactions.
    # 2. minimum cost to be able to buy a stock at time i.
    profits, costs = [0] * (k + 1), [float('inf')] * (k + 1)
    # For all the prices at time i,
    for p in prices:
        # For all the k transactions,
        for i in range(1, k + 1):
            # Minimize the cost,
            # currentPrice - previous profit represents how much we actually pay
            # out of pocket (since some of the cost is covered by the profit
            # we made earlier).
            costs[i] = min(costs[i], p - profits[i - 1])
            # Maximize the profit,
            # currentPrice - cost[i] = max profit that we can making at most i
            # transactions.
            profits[i] = max(profits[i], p - costs[i])
    # Return maximum profit that can be made by at most k transactions.
    return profits[k]


def main():
    """
    Driver function.
    :return: None
    """
    t1 = [2, 4, 1], 2
    print(maxProfit(t1[1], t1[0]))
    t2 = [3, 2, 6, 5, 0, 3], 2
    print(maxProfit(t2[1], t2[0]))


if __name__ == '__main__':
    main()
