from collections import defaultdict


def alien_rhyme(words):
    """
    Finds the largest grouping of pairs of words that match.
    :param words: The list of words to be made into suffix based pairs.
    :return: The maximum number of words that can be paired in teh given way.
    """
    # dicts to hold
    # count -> the count of each suffix
    # _words -> maps the suffix to a list of words.
    count, _words = defaultdict(int), defaultdict(set)
    # Fro all thw words
    for word in words:
        # get all the suffixes
        for suffix in suffixes(word):
            count[suffix] += 1
            _words[suffix].add(word)
    # Only the suffixes that are common to atleast two words.
    useful_suff = [suffix for suffix, _count in count.items() if _count > 1]
    # We sort this based ont the length of the suffixes in descending order to
    # have the largest suffix first.
    useful_suff.sort(key=len, reverse=True)
    # res -> the number of words paired
    # unavailable -> set of words already used.
    res, unavailable = 0, set()
    # For all the useful suffixes.
    for suff in useful_suff:
        # Get the words that belong to that suffix and are available.
        available = list(_words[suff] - unavailable)
        # If more than 1 word match, select the first two
        # make them unavailable and repeat.
        if len(available) > 1:
            res += 2
            unavailable |= set(available[:2])
    # return maximum number of words that can be paired in teh given way.
    return res


def suffixes(word):
    """
    finds all the suffixes of a given word.
    :param word: The word whose suffixes are to be found
    :return: A list of all the suffixes of a given word.
    """
    return [word[i:] for i in range(len(word))]


def main():
    """
    Driver function.
    :return: None
    """
    # The number of test cases.
    num_tests = int(input())
    # For all tets cases,
    for test_num in range(1, num_tests + 1):
        # get all the words
        words = [input().strip() for _ in range(int(input()))]
        # find the maximum number of words that can be paired in the given sway.
        result = alien_rhyme(words)
        # Output the result
        print('Case #{}: {}'.format(test_num, result))


if __name__ == '__main__':
    main()
