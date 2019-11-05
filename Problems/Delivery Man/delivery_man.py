def delivery_man(A, B, X, Y, N):
    """
    Find the maximum tip andy and bob can make for N orders.
    :param A: Tips for Andy for an order.
    :param B: Tips for Bob for an order.
    :param X: The maximum # of orders Andy can take.
    :param Y: The maximum # of orders Bob can take.
    :param N: The Total # of Orders
    :return: The maximum tip Andy and Bob can make together.
    """
    # Array to store the min, max and diff for all orders.
    min_max_diff = [(min(a, b), max(a, b), (a - b)) for a, b in zip(A, B)]
    # We sort it by the abs(diff) between andy - bob's tips
    min_max_diff.sort(key=lambda x: abs(x[2]), reverse=True)
    # To hold the maximum tip made.
    max_tip = 0
    # For all the orders.
    for i in range(N):
        # If the diff in tips is 0, add either of Andy's or Bob's tips.
        if min_max_diff[i][2] == 0:
            max_tip += min_max_diff[i][1]
        # If diff > 0 => Andy had a higher tip.
        elif min_max_diff[i][2] > 0:
            # If Andy can take this order, add his tip.
            if X > 0:
                max_tip, X = max_tip + min_max_diff[i][1], X - 1
            # Else let Bob take the order and add his tip.
            else:
                max_tip, Y = max_tip + min_max_diff[i][0], Y - 1
        # If diff < 0 => Bob had a higher tip.
        else:
            # If Bob can take this order, add his tip.
            if Y > 0:
                max_tip, Y = max_tip + min_max_diff[i][1], Y - 1
            # Else let Andy take the order and add his tip.
            else:
                max_tip, X = max_tip + min_max_diff[i][0], X - 1
    # Return the Maximum tip they cna make together.
    return max_tip


def delivery_man_optimized(A, B, X, Y, N):
    """
    Find the maximum tip andy and bob can make for N orders.
    :param A: Tips for Andy for an order.
    :param B: Tips for Bob for an order.
    :param X: The maximum # of orders Andy can take.
    :param Y: The maximum # of orders Bob can take.
    :param N: The Total # of Orders
    :return: The maximum tip Andy and Bob can make together.
    """
    # Hold max tip.
    # a_tips, b_tips hold the diff between Andy and Bob's tips.
    max_tips, a_tips, b_tips = 0, [], []

    # For all the N orders,
    # choose the the one who has the maximum tip for that order.
    # Recording the diffs between the tips and decrement X, Y to record
    # 'over-utilization' of either Andy or Bob.
    for a, b, _ in zip(A, B, range(N)):
        if a > b:
            a_tips.append(a - b)
            max_tips += a
            X -= 1
        else:
            b_tips.append(b - a)
            max_tips += b
            Y -= 1

    # If Andy was over-utilized,
    # find the min diff in tips where he contributed and take Bob's
    # contribution there instead.
    # This works because when we subtract the diff, the min tip is taken for
    # order instead.
    if X < 0:
        a_tips.sort()
        for i in range(abs(X)):
            max_tips -= a_tips[i]

    # Same for Bob.
    if Y < 0:
        b_tips.sort()
        for i in range(abs(Y)):
            max_tips -= b_tips[i]

    # return the maximum tip.
    return max_tips


def delivery_man_optimized_1(A, B, X, Y, N):
    # Find the differences in tips, and reverse sort them.
    diff = sorted([a - b for a, b in zip(A, B)], reverse=True)
    # Consider the max tips = sum of any one of Andy's or Bob's tips.
    max_tips = sum(B)
    # Some of the tips could have been greater if the other one took the order.
    # Find where the diff was the maximum, and the other one would have made a
    # positive contribution.
    for i in range(X):
        if diff[i] > 0:
            max_tips += diff[i]
        else:
            break
    # return the maximum tip.
    return max_tips


def main():
    """
    Driver function.
    :return: None
    """
    # N = Total # of Orders, X, Y = # of orders Andy, Bob can take.
    N, X, Y = map(int, input().split())
    # Tips for Andy
    *A, = map(lambda x: int(x), input().split())
    # Tips for Bob
    *B, = map(lambda x: int(x), input().split())
    # Find the maximum tip Andy and Bob can make together.
    max_tip = delivery_man_optimized_1(A, B, X, Y, N)
    # Output result.
    print(max_tip)


if __name__ == '__main__':
    main()
