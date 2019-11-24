def stringSimilarity_brute_force(s) -> int:
    """
    Trivial implementation of the Z-function.
    :param s: The string whose similarity is to be found with it's suffixes.
    :return: The sum of string's similarity with all it's suffixes.
    """
    # Length of s.
    n = len(s)
    # Z-Array, where z[i] == len(longest_common_prefix(s, suffix(s, i))).
    z = [0] * n
    for i in range(1, n):
        # Keep incrementing z[i] till mismatch or end of string.
        while i + z[i] < n and s[z[i]] == s[i + z[i]]: z[i] += 1
    # return the sum(z) + n
    # where n accounts for when i = 0 i.e. s == suffix(s, i = 0)
    return sum(z) + n


def stringSimilarity(s) -> int:
    """
    Efficient implementation of the Z-function.
    :param s: The string whose similarity is to be found with it's suffixes.
    :return: The sum of string's similarity with all it's suffixes.
    """
    # Length of s.
    n = len(s)
    # l, r to hold the indices of the right-most segment match.
    # Z-Array, where z[i] == len(longest_common_prefix(s, suffix(s, i))).
    l, r, z = 0, 0, [0] * n
    for i in range(1, n):
        # if i < r, use an min(r - i + 1, z[i - l]) as an initial approximation.
        if i <= r: z[i] = min(r - i + 1, z[i - l])
        # if i > r, compute z[i] trivially.
        while i + z[i] < n and s[z[i]] == s[i + z[i]]: z[i] += 1
        # Update l, r to hold the indices of the right-most segment match.
        if i + z[i] - 1 > r: l, r = i, i + z[i] - 1
    # return the sum(z) + n
    # where n accounts for when i = 0 i.e. s == suffix(s, i = 0)
    return sum(z) + n


def main():
    """
    Driver function.
    :return: None
    """
    # For every test case
    for _ in range(1, int(input()) + 1):
        # Get the input string.
        s = input()
        # Find the sum of the string's similarity with all it's suffixes.
        result = stringSimilarity(s)
        # Output the result.
        print(result)


if __name__ == '__main__':
    main()
