def cultural_programme(entries: [int], exits: [int]) -> int:
    """
    Finds the maximum number of people occupying the hall over the course of the
    Cultural Programme.
    :param entries: A list denoting the entry times of people.
    :param exits: A list denoting the exit times of people.
    :return: The maximum number of people occupying the hall.
    """
    # Vars to hold,
    # people -> The number of people in the hall any time.
    # max_people -> The maximum number of people in the hall over the course of
    # the programme.
    people, max_people, entry_set = 0, 0, set(entries)
    # Have all the entry and exit times in a list, sorted by time.
    # For every record,
    for record in sorted(entries + exits):
        # If a person enters a room, increment people by 1.
        # else the person must have exited the room so we decrement people by 1.
        # This is from the fact that all times will be unique since only one
        # person can either enter or exit the hall at a time.
        people = people + 1 if record in entry_set else people - 1
        # Update max_people.
        max_people = max(max_people, people)
    # return the maximum number of people
    return max_people


def main():
    """
    Driver function.
    :return: None
    """
    # Get the number of entry and exit times.
    N = int(input())
    # Var to hold the entry and exit times.
    entries, exits = [0] * N, [0] * N
    # Get the input.
    for i in range(N): entries[i], exits[i] = map(int, input().split())
    # Get the maximum number of people in the
    result = cultural_programme(entries, exits)
    # Output the result.
    print(result)


if __name__ == '__main__':
    main()
