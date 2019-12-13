def next_palindrome(K: str) -> str:
    """
    Finds the next palindrome number greater than K
    :param K: The number whose next greater palindrome is to be found.
    :return: The next greater palindrome after K.
    """
    # Edge cases.
    if not K or len(K) < 1: return ''
    # n -> length of K
    n = len(K)
    # If the given number is all 9's the next greater palindrome, will be the
    # number + 2, Ex - 9 -> 11, 99 -> 101, 999 -> 1001 and so on ...
    if K == '9' * n: return str(int(K) + 2)

    num = list(K)

    # Make num a palindrome by simple matching.
    for i in range(n // 2):
        num[~i] = num[i]

    # If this palindrome number is greater than K, we are done.
    if num > list(K): return ''.join(num)

    # Otherwise, we get the 2 mid points of the string.
    i = n // 2 + (0 if n % 2 else -1)
    j = n // 2

    # Now we start exploring from the center to the edges.
    while True:
        # If any of the number travelling leftward is 9,
        # make it zero and the corresponding mirror index zero too.
        if num[i] == '9':
            num[i] = num[j] = '0'
            i, j = i - 1, j + 1
        # Other-wise, we just add one to the leftward number, making it greater,
        # set its corresponding palindromic index to the same value.
        else:
            num[i] = num[j] = str(int(num[i]) + 1)
            return ''.join(num)


def main():
    """
    Driver function.
    :return: None
    """
    # For all the test cases,
    for _ in range(int(input())):
        # Get the number whose next palindrome is to be found.
        K = input().strip()
        # Find the next palindrome greater than it.
        result = next_palindrome(K)
        # Output the result.
        print(result)


if __name__ == '__main__':
    main()
