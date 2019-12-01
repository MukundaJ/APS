def chop_waffle(waffle: [str], r: int, c: int, h: int, v: int) -> bool:
    """
    Checks if it is possible to cut up the waffle with the given number of
    horizontal and vertical cuts.
    :param waffle: The waffle that is to be cut up represented as a list of
    strings.
    :param r: The number of rows in the waffle.
    :param c: The number of columns in the waffle.
    :param h: The number of horizontal cuts to be made.
    :param v: The number of vertical cuts to be made.
    :return: A boolean value indicating if it is possible or not.
    """
    # Counting the total number of chips in the waffle.
    chips = sum(1 for i in range(r) for j in range(c) if waffle[i][j] == '@')

    # If there are no chips, we cna divide into how many ever parts having equal
    # number of chips (i.e. 0).
    if chips == 0: return True
    # with h horizontal cuts and v vertical cuts, there would be a total of
    # ((h + 1) * (v + 1)) parts in total, if cannot divide the chips perfectly,
    # return IMPOSSIBLE
    if chips % ((h + 1) * (v + 1)) != 0: return False

    # Vars to hold,
    # h_cuts -> array to hold where the horizontal cuts should be made,
    # avg -> the avg number of chips that should be in each cut.
    # pos -> position in the h_cuts array.
    h_cuts, v_cuts = [0] * (h + 2), [0] * (v + 2)
    h_avg, v_avg = chips // (h + 1), chips // (v + 1)
    h_pos, v_pos, h_curr, v_curr = 1, 1, 0, 0

    # Count the chips, and make a cut where the chips count == avg, and save it.
    for i in range(r):
        for j in range(c):
            if waffle[i][j] == '@': h_curr += 1

        # If the total number of chips in any one cut is greater than the avg,
        # It's not possible to distribute it equally.
        if h_curr > h_avg: return False

        # Mark a horizontal cut.
        if h_curr == h_avg:
            h_cuts[h_pos] = i + 1
            h_curr, h_pos = 0, h_pos + 1

    # We do the same for the vertical cuts.
    for i in range(c):
        for j in range(r):
            if waffle[j][i] == '@': v_curr += 1

        # If the total number of chips in any one cut is greater than the avg,
        # It's not possible to distribute it equally.
        if v_avg > v_avg: return False

        # Mark a vertical cut.
        if v_curr == v_avg:
            v_cuts[v_pos] = i + 1
            v_curr, v_pos = 0, v_pos + 1

    # avg number of chips per part of the waffle.
    avg = chips / ((h + 1) * (v + 1))

    # count the number of chips in each part.
    for i in range(h + 1):
        for j in range(v + 1):
            # total to hold total chips in each part
            total = 0
            # for each part of the waffle,
            for k in range(h_cuts[i], h_cuts[i + 1]):
                for l in range(v_cuts[j], v_cuts[j + 1]):
                    if waffle[k][l] == '@': total += 1
            # If the total != avg,
            if total != avg: return False

    # If it satisfies all the conditions, it is possible.
    return True


def main():
    """
    Driver function.
    :return: None
    """
    # For every test case,
    for t in range(1, int(input()) + 1):
        # Get the number or rows (r), columns (c), horizontal cuts (h),
        # vertical cuts (v)
        r, c, h, v = map(int, input().split())
        # Get the waffle input.
        waffle = [input().strip() for _ in range(r)]
        # Check if the waffle can be cut up or not.
        result = 'POSSIBLE' if chop_waffle(waffle, r, c, h, v) else 'IMPOSSIBLE'
        # Output the result.
        print('Case #{}: {}'.format(t, result))


if __name__ == '__main__':
    main()
