def solve_robot_programming_strategy(ops: [str]) -> str:
    """
    Finds a winning strategy to defeat all other robots given their moves,
    if possible.
    :param ops: A list of strings representing the moves of each of the robot
    at the time denoted byt the string index.
    :return: The winning strategy (set of moves to make) if possible else
    'IMPOSSIBLE'.
    """
    # Var to hold the winning strategy and time step.
    strategy, time = '', 0

    # As long as there is an opponent left,
    while ops:
        # Get the set of unique moves that can be made by all the robots at the
        # time step.
        letters = set(s[time % len(s)] for s in ops)

        # If at any time-step, there are opponents making all the 3 different
        # moves possible, we would loose to at-least one of the opponents no
        # matter what.
        if len(letters) == 3:
            return 'IMPOSSIBLE'

        # If all the opponents make the same move at the given time-step,
        # We pick the move that defeats all of them as below.
        elif len(letters) == 1:
            if 'R' in letters:
                strategy += 'P'
            elif 'P' in letters:
                strategy += 'S'
            elif 'S' in letters:
                strategy += 'R'

        # Otherwise, there must be at most 3 unique moves that all the remaining
        # opponents make at that time-step, so we pick the move that cannot be
        # defeated by the other 2 moves as below.
        else:
            if 'R' not in letters:
                strategy += 'S'
            elif 'P' not in letters:
                strategy += 'R'
            elif 'S' not in letters:
                strategy += 'P'

        # A filter which decides which element to remove.
        def defeated(move):
            """
            A filter to decide which opponents we have already won against at
            the current time-step.
            :param move: Move made by the opponent at a particular time-step.
            :return: A boolean value indicating if we can win against that move
            at the time-step.
            """
            if move == 'R':
                return strategy[-1] == 'P'
            elif move == 'P':
                return strategy[-1] == 'S'
            elif move == 'S':
                return strategy[-1] == 'R'

        # Keep the moves of the opponents not defeated yet.
        ops = [move for move in ops if not defeated(move[time % len(move)])]
        # increment the time-step
        time += 1

    # Return the winning strategy
    return strategy


def main():
    """
    Driver function.
    :return: None
    """
    # For all test-cases,
    for t in range(1, int(input()) + 1):
        # Get the total number of opponents.
        A = int(input())
        # Get the moves of each opponent,
        # each row is a set of moves to be made by the opponent.
        moves = [input().strip() for _ in range(A)]
        # Find if it possible to devise a winning strategy.
        result = solve_robot_programming_strategy(moves)
        # Output the result.
        print('Case #{}: {}'.format(t, result))


if __name__ == '__main__':
    main()
