from string import ascii_lowercase as charset


def another_kmp(counts: [int]) -> str:
    """
    Function that finds the lexicographically smallest string that can be made
    from the given character frequencies.
    :param counts: The frequency of each of the character.
    :return: The lexicographically smallest string S, minimizing sum(kmp(S)).
    """

    # Keep an array to hold the non-zero frequencies.
    used = [i for i in range(26) if counts[i]]

    # If all the frequencies are 0, return the empty string.
    if len(used) == 0:
        return ''

    # If only 1 character is used, return that character repeated as many times
    # as it's frequency.
    elif len(used) == 1:
        return ''.join(charset[i] * counts[i] for i in used)

    # For non-trivial cases,
    else:
        # Find the character that has the minimum frequency and is the smallest
        # lexicographically.
        min_freq_char = min(used, key=lambda x: (counts[x], x))

        # If there is only 1 of that character or,
        # the min_frequency character != lexicographically smallest character,
        if counts[min_freq_char] == 1 or min_freq_char != used[0]:
            # Make the first character as the min_frequency character and then
            # make the remaining string the smallest lexicographic string.
            counts[min_freq_char] -= 1
            return charset[min_freq_char] + \
                   ''.join(charset[i] * counts[i] for i in used)

        # If the min_frequency character is also the lexicographically smallest
        # character,
        else:
            # Start the string with as min_freq_char repeated twice
            # (We would have at-least 2 since we checked for it being earlier.)
            result = charset[min_freq_char] * 2
            counts[min_freq_char] -= 2

            # Then we interleave it with the remaining characters till the
            # min_frequency character is exhausted.
            remainder = ''.join(charset[i] * counts[i] for i in used
                                if i != min_freq_char)

            # Interleaving.
            i = 0
            while counts[min_freq_char] > 0:
                result += remainder[i] + charset[min_freq_char]
                counts[min_freq_char], i = counts[min_freq_char] - 1, i + 1

            # Append the remaining string once the min_frequency character is
            # exhausted.
            result += remainder[i:]

            # return the result.
            return result


def main():
    """
    Driver function.
    :return: None
    """
    # Get the counts of each alphabet.
    counts = [int(x) for x in input().split(' ')]
    # Find the lexicographically smallest string S minimizing sum(kmp(S)).
    result = another_kmp(counts)
    # Output the result.
    print(result)


if __name__ == '__main__':
    main()
