def is_magic_square(l):
    m_const = 3 * (3 ** 2 + 1) / 2

    # Un-flatten, convert list of len = 9 to 3x3 array.
    s = [l[i:i + 3] for i in range(0, 9, 3)]

    # Check the sum of each row.
    # row_sum = all([sum(s[row])])

    pass


def formingMagicSquare(s):
    n = flatten(s)
    # Hard-coding solutions
    all_n = [
        [8, 1, 6, 3, 5, 7, 4, 9, 2],
        [6, 1, 8, 7, 5, 3, 2, 9, 4],
        [4, 9, 2, 3, 5, 7, 8, 1, 6],
        [2, 9, 4, 7, 5, 3, 6, 1, 8],
        [8, 3, 4, 1, 5, 9, 6, 7, 2],
        [4, 3, 8, 9, 5, 1, 2, 7, 6],
        [6, 7, 2, 1, 5, 9, 8, 3, 4],
        [2, 7, 6, 9, 5, 1, 4, 3, 8]
    ]
    for x in all_n:
        is_magic_square(x)
    allsum = []
    for l in all_n:
        allsum.append(sum([abs(n[i] - l[i]) for i in range(9)]))

    return min(allsum)


def flatten(s):
    return [s[i][j] for i in range(len(s)) for j in range(len(s[i]))]


def m_constant(n):
    return n * (n ** 2 + 1) / 2


def main():
    all_n = [
        [8, 1, 6, 3, 5, 7, 4, 9, 2],
        [6, 1, 8, 7, 5, 3, 2, 9, 4],
        [4, 9, 2, 3, 5, 7, 8, 1, 6],
        [2, 9, 4, 7, 5, 3, 6, 1, 8],
        [8, 3, 4, 1, 5, 9, 6, 7, 2],
        [4, 3, 8, 9, 5, 1, 2, 7, 6],
        [6, 7, 2, 1, 5, 9, 8, 3, 4],
        [2, 7, 6, 9, 5, 1, 4, 3, 8]
    ]
    for l in all_n:
        is_magic_square(l)


if __name__ == '__main__':
    main()
