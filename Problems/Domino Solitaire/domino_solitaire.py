"""
https://www.codechef.com/problems/DOMSOL
"""


def domino_solitaire_dp(N: int, grid: [[int]]) -> int:
    """
    Calculates the maximum score that can be made by placing the 1x2 tiles
    horizontally or vertically such that no two of them overlap.
    The score is calculated as the difference between the numbers covered by the
    tile.
    :param grid: The 2xN grid in which the tiles are to be placed.
    :param N: The number of columns in the grid.
    :return: The maximum score by placing the tiles as specified.
    """
    # Array to hold maximum score made upto column i in the grid, where i is
    # represents by the column number (from 0 upto N).
    score = [0] * N
    # For only 1 column, we can only place one tile i.e. vertically.
    score[0] = abs(grid[0][0] - grid[1][0])
    # For columns 0 & 1, we can place two tiles either both vertically or
    # both horizontally only (since no overlap is allowed),
    # we calculate the max score as follows,
    # First term represents placing two tiles horizontally,
    # The second one represents placing two tiles vertically,
    score[1] = max(score[0] + abs(grid[0][1] - grid[1][1]),
                   abs(grid[0][0] - grid[0][1]) + abs(grid[1][0] - grid[1][1]))
    # We calculate the upto score for the following columns by using these base
    # results.
    for i in range(2, N):
        # First term represents that everything upto col i - 1 is occupied,
        # So we only place a single vertical tile at column i.
        # Second term represents the case where everything upto column i - 2 is
        # occupied so we can place 2 horizontal tiles at each row covering
        # columns i - 1 and i.
        score[i] = max(score[i - 1] + abs(grid[0][i] - grid[1][i]),
                       score[i - 2] + abs(grid[0][i] - grid[0][i - 1]) +
                       abs(grid[1][i] - grid[1][i - 1]))

    # return the maximum score when all the columns are used.
    return score[N - 1]


def domino_solitaire_space_optimized(N: int, grid: [[int]]) -> int:
    """
    Calculates the maximum score that can be made by placing the 1x2 tiles
    horizontally or vertically such that no two of them overlap.
    The score is calculated as the difference between the numbers covered by the
    tile.
    :param grid: The 2xN grid in which the tiles are to be placed.
    :param N: The number of columns in the grid.
    :return: The maximum score by placing the tiles as specified.
    """
    # prev -> score when there are i - 1 columns,
    # max_score -> max_score upto i columns,
    # initially i = 1,
    # => prev = 0 (cannot place any tile if there is no grid)
    # => max_score = score of tile placed vertically on column 1.
    prev, max_score = 0, abs(grid[0][0] - grid[1][0])

    # We calculate the maximum score that can be made upto column N.
    for i in range(1, N):
        # Placing a tile vertically if everything upto column i - 1 is occupied.
        vertical = max_score + abs(grid[0][i] - grid[1][i])
        # Placing 2 tiles horizontally in the case where everything upto
        # column i - 2 is occupied so we can place 2 horizontal tiles at each
        # row covering columns i - 1 and i.
        horizontal = prev + abs(grid[0][i] - grid[0][i - 1]) + \
                     abs(grid[1][i] - grid[1][i - 1])
        # Update the previous score to follow upto the (i - 1)th column.
        prev = max_score
        # Update the maximum score when using everything including column i.
        max_score = max(horizontal, vertical)

    # return the maximum score that can be made when using all the columns.
    return max_score


def main():
    """
    Driver function.
    :return: None
    """
    # Get the number of rows columns in the 2xN grid.
    N = int(input())
    # Get the grid with 2 rows.
    grid = [[int(x) for x in input().split()] for _ in range(2)]
    # Get the maximum score that can be made by placing the tile with the given
    # configurations.
    result = domino_solitaire_space_optimized(N, grid)
    # Output the result.
    print(result)


if __name__ == '__main__':
    main()
