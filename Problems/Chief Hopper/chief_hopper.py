def chiefHopper(arr: [int]) -> int:
    """
    Finds the minimum initial energy the bot will require to hop over all the
    buildings.
    :param arr: A list containing the height of all the buildings.
    :return: the minimum initial energy the bot will require to hop over all the
    buildings.
    """
    # For the minimum initial energy, the bot mush have 0 energy left at the end
    # of the last building.
    e = 0
    # Now we calculate backwards how much initial energy would be required.
    # if e < h, e = 2e - h
    for height in arr[::-1]: e = (e + height + 1) // 2
    return e


def main():
    """
    Driver function.
    :return: None
    """
    # Number of buildings.
    input()
    # Heights of each of the buildings.
    heights = list(map(int, input().strip().split()))
    # Get the minimum initial energy the bot requires.
    result = chiefHopper(heights)
    # Output the result.
    print(result)


if __name__ == '__main__':
    main()
