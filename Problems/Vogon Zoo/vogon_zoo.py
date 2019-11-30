def vogon_zoo(blood_types, K):
    """
    Finds the maximum number of Kubudu dragons that can be placed in the same
    cage given the blood type threshold.
    :param blood_types: The blood types of the dragons.
    :param K: The threshold value of difference between blood types.
    :return: The maximum number of Kubudu dragons that can be placed in the same
    cage.
    """
    # Sort the blood types in ascending order,
    blood_types.sort()
    # Vars to hold,
    # total -> the total number of Kubudu dragons that can be placed in the same
    # cage.
    # curr -> the blood type of the last Kubudu dragon placed in the same cage.
    total, curr = 1, blood_types[0]
    # For the blood types in sorted order,
    # We simply keep count if are able to place another dragon in the same cage.
    # This would be the maximum number of dragons we can put in the cage, since
    # starting from a blood type any higher than the least one can only reduce
    # our total.
    for blood_type in blood_types:
        if blood_type >= curr + K: total, curr = total + 1, blood_type
    # Return the total number of dragons that can be put in the same cage.
    return total


def main():
    """
    Driver function.
    :return: None
    """
    # Vars to hold,
    # N -> Number of Kubudu dragons,
    # K -> Threshold difference required between blood types.
    N, K = map(int, input().split())
    # Get all the blood types.
    blood_types = list(map(int, input().split()))
    # Find the maximum number of dragons that can be put in a cage together.
    result = vogon_zoo(blood_types, K)
    # Output the result.
    print(result)


if __name__ == '__main__':
    main()
