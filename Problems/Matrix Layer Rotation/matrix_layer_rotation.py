def matrixRotation(matrix, r):
    """
    Rotates the matrix in-place layer wise in the anticlockwise direction
    r times.
    :param matrix: The matrix to be rotated.
    :param r: The number of times the matrix is to be rotated.
    :return: None
    """

    # Edge cases, where nothing is to be done.
    if matrix is None or len(matrix) < 1 or len(matrix[0]) < 1: return

    # using left, right, top and bottom,
    # we can denote the vertices of a 'layer'/ring as
    # (top, left), (top, right), (bottom, left), (bottom, right).
    # After each iteration in the loop they would move on to the next/inner
    # 'layer'/ring of the matrix
    left, right, top, bottom = 0, len(matrix[0]) - 1, 0, len(matrix) - 1

    # Till all the inner layers are processed.
    while left < right and top < bottom:

        # Rotate each layer r % (layer_len) times.
        # where layer_len is a number denoting how many times this layer can be
        # rotated before landing up in exactly the same configuration.
        for _ in range(r % (2 * (right - left + bottom - top))):

            # The element to become the top right element.
            prev = matrix[top + 1][right]

            # Shift the elements of the top edge of the 'layer'/ring leftwards.
            for i in range(right, left - 1, -1):
                matrix[top][i], prev = prev, matrix[top][i]

            # Shift the elements of the left edge of the 'layer'/ring downwards.
            for i in range(top + 1, bottom + 1):
                matrix[i][left], prev = prev, matrix[i][left]

            # Shift the elements of the bottom edge of the 'layer'/ring
            # rightwards.
            for i in range(left + 1, right + 1):
                matrix[bottom][i], prev = prev, matrix[bottom][i]

            # Shift the elements of the right edge of the 'layer'/ring upwards.
            for i in range(bottom - 1, top - 1, -1):
                matrix[i][right], prev = prev, matrix[i][right]

        # Update left, right, top, bottom to point to the next/inner
        # 'layer'/ring of the matrix.
        left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1


def print_matrix(matrix):
    """
    Prints the matrix.
    :param matrix: The matrix to be printed.
    :return: None.
    """
    [print(*row) for row in matrix]


def main():
    """
    Driver function.
    :return: None
    """
    # m, n, r represent the rows, columns, rotation of the matrix respectively.
    m, n, r = map(int, input().split())
    # List to hold the given matrix.
    matrix = [list(map(int, input().split())) for _ in range(m)]
    # Rotate the matrix layer wise r times.
    matrixRotation(matrix, r)
    # Output the result.
    print_matrix(matrix)


if __name__ == '__main__':
    main()
