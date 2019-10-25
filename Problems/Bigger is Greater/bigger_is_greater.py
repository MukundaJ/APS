from itertools import permutations


def naive_solution(w: str):
    """
    Naive solution to find the next lexicographically greatest permutation of w.
    :param w: The string next lexicographically greater permutation is to be
    found.
    :return: The next lexicographically greater permutation if possible
    else 'no answer'
    """
    # Find all the possible permutations of
    sorted_perms = sorted(set(map(''.join, permutations(w))))
    idx = sorted_perms.index(w) + 1
    return sorted_perms[idx] if idx < len(sorted_perms) else 'no answer'


def optimal_solution(w: str):
    """
    The optimal solution to find the next lexicographically greater permutation
    of w.
    :param w: The string next lexicographically greater permutation is to be
    found.
    :return: The next lexicographically greater permutation if possible
    else 'no answer'
    """
    w = list(w)
    try:
        # Find the pivot, i.e. first decreasing element from the right of the
        # word.
        pivot = next(i for i in range(len(w) - 1, 0, -1) if w[i] > w[i - 1]) - 1
    except StopIteration:
        return 'no answer'

    # Find the rightmost element greater than the the element at pivot.
    successor = next(i for i in range(len(w) - 1, 0, -1) if w[i] > w[pivot])

    # Swap the pivot and the successor.
    w[pivot], w[successor] = w[successor], w[pivot]

    # Minimize the half of the string after the pivot, by sorting it,
    # Notice how we achieve a sorted half by simply reversing it,
    # since the suffix initially was weakly increasing in itself and remains
    # so after the pivot is swapped for first righmost element greater than it.
    w = ''.join(w[:pivot + 1] + w[pivot + 1:][::-1])

    return w


def biggerIsGreater(w: str):
    """
    Bigger is greater driver function to call different solutions.
    :param w: The string next lexicographically greater permutation is to be
    found.
    :return: The next lexicographically greater permutation if possible
    else 'no answer'
    """
    # return naive_solution(w)
    return optimal_solution(w)


def main():
    """
    Driver function.
    :return: None
    """
    for test_num in range(int(input())):
        word = input()
        result = biggerIsGreater(word)
        print(result)


if __name__ == '__main__':
    main()
