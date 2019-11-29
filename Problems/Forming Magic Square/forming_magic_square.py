from itertools import permutations


def formingMagicSquare(s: [[int]], cache=True) -> int:
    """
    Finds the minimum cost required to transform s into a magic square.
    :pre-conditions: s is a matrix of order 3 (i.e. of shape 3x3).
    :param s: The matrix to be transformed into a magic square.
    :return: The minimum cost required to transform s into a magic square.
    """
    if is_magic_square(s): return 0
    if cache:
        # A list of all the known magic squares of order 3.
        known_magic_squares = [[[8, 1, 6], [3, 5, 7], [4, 9, 2]],
                               [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
                               [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
                               [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
                               [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
                               [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
                               [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
                               [[2, 7, 6], [9, 5, 1], [4, 3, 8]]]
    else:
        # Generate all the magic squares.
        known_magic_squares = magic_squares(3)

    # Var to hold the minimum cost required to transform s into a magic square.
    min_cost = float('inf')

    # For all known magic squares,
    for magic_sq in known_magic_squares:
        # Var to hold the total diff with current magic_sq
        cost = 0
        for row in range(len(magic_sq)):
            for col in range(len(magic_sq[row])):
                # For each element we add to the cost.
                cost += abs(s[row][col] - magic_sq[row][col])
        # Update min_cost if required.
        min_cost = min(min_cost, cost)

    # return the minimum cost required.
    return min_cost


def is_magic_square(s: [[int]]) -> bool:
    """
    Checks if the given matrix is a magic square or not.
    :pre-conditions: s is a square matrix with shape like NxN.
    :param s: The matrix to be checked.
    :return: A boolean value indicating if s is a magic square or not.
    """
    # Order of s.
    n = len(s)
    # The magic constant for a square of order n.
    m_const = n * (n ** 2 + 1) // 2

    # Checking the sum of the diagonals.
    l_diagonal, r_diagonal = 0, 0
    for i in range(n):
        l_diagonal, r_diagonal = l_diagonal + s[i][i], r_diagonal + s[i][~i]
    if not l_diagonal == r_diagonal == m_const: return False

    # Checking the sum of each row and each column.
    for i in range(n):
        row_sum, col_sum = 0, 0
        for j in range(n):
            row_sum, col_sum = row_sum + s[i][j], col_sum + s[j][i]
        if not row_sum == col_sum == m_const: return False

    # If all above conditions are met, s is said to be a magic square.
    return True


def magic_squares(n: int) -> [[[int]]]:
    """
    Finds all the magic squares of order n.
    :param n: The order of the square matrix (shape like n x n).
    :return: A list of all the magic squares of the given order.
    """
    # List to hold all the magic squares.
    _magic_squares = []

    # For all the permutations of the given numbers.
    for p in permutations(range(1, n ** 2 + 1)):
        # A square matrix of order n.
        sq = [p[i: i + n] for i in range(0, n ** 2, n)]
        # If it is a magic square add it to _magic_squares.
        if is_magic_square(sq): _magic_squares.append(sq)

    # return all the magic squares of the order 3.
    return _magic_squares


def main():
    """
    Driver function.
    :return: None
    """
    # Get the input square,
    s = [list(map(int, input().strip().split())) for _ in range(3)]
    # Find the minimum cost to make it a magic square.
    res = formingMagicSquare(s)
    # Output the result.
    print(res)


if __name__ == '__main__':
    main()
