from re import search


def num_super_six_substrings_optimal(s: str) -> int:
    """
    Calculates the number of super six substrings of the given string s, as per
    the definition of super six substrings in the problem statement.
    :param s: The string to be whose super substrings are to be found.
    :return: The total number of super substrings of s.
    """
    # a -> holds the sum of digits modulo 3
    # count holds the count of the super 6 substrings
    a, n, x, count = [0] * 3, len(s), 0, 0
    # Iterate through s, and memorize every values of sum of all the
    # prefixes % 3 and update a.
    for i in range(n):
        digit = int(s[i])
        x = (x + digit) % 3
        if digit % 2 == 0: a[x] += 1
    x = 0
    # Finally we iterate through s again and
    # notice that is  s[i] == '0' only one string is valid starting at i
    # i.e. s[i] itself.
    # Otherwise, we find all the prefixes beginning at i, having the same
    # sum modulo % 3 value, for which we can use our precomputed array a.
    for i in range(n):
        if s[i] == '0':
            count += 1
        else:
            count += a[x]
        digit = int(s[i])
        x = (x + digit) % 3
        if digit % 2 == 0: a[x] -= 1
    return count


def num_super_six_substrings(s: str) -> int:
    """
    Calculates the number of super six substrings of the given string s, as per
    the definition of super six substrings in the problem statement.
    :param s: The string to be whose super substrings are to be found.
    :return: The total number of super substrings of s.
    """
    count = 0
    for subs in substrings(s):
        if is_divisible_by_6(int(subs)) and not has_leading_zero(subs):
            count += 1
    return count


def is_divisible_by_6(num: int) -> bool:
    """
    Checks if the given number is divisible by 6 or not.
    :param num: The number to be tested.
    :return: True if the number is divisible by 6.
    """
    # A number is divisible by 6 if it is divisible by both 2 and 3.
    return num % 2 == num % 3 == 0


def has_leading_zero(s: str):
    """
    Checks if the given string has a leading zero.
    :param s: The string to be tested
    :return: True if the string has a leading zero.
    """
    return search('^0.+$', s)


def substrings(s: str) -> [str]:
    """
    Generates all the substrings of the given string s.
    :param s: The string whose substrings are to be returned.
    :return: All the substrings of the string s.
    """
    return [s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]


def main():
    """
    Driver function.
    :return: None
    """
    # Take the input string.
    s = input()
    # Find the number of super six substrings.
    result = num_super_six_substrings_optimal(s)
    # Output the result.
    print(result)


if __name__ == '__main__':
    main()
