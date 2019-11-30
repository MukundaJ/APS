def trap(height: [int]) -> int:
    """
    Calculates how much rain water can be trapped, with the given heights
    :param height: The heights of the bars / elevation map.
    :return: The total amount of rain water trapped.
    """

    # Edge case where nothing needs to be done.
    if not height: return 0

    # Vars to hold,
    # n -> size of the elevation map,
    n = len(height)

    # l, r -> to hold the left and right extremes of the elevation map,
    # lmax, rmax -> to hold the maximum height encountered when traversing from
    # the left and right and right directions.
    l, r, lmax, rmax = 0, n - 1, 0, 0

    # rain_water -> holds the total amount of rain water trapped.
    rain_water = 0

    # Loop till the left and right pointers don't meet
    while l < r:

        # The rain water to be trapped will always be restricted by whichever
        # current height on l or r is minimum.
        if height[l] < height[r]:

            # Update lmax if we can,
            # else we add to the amount of rain water trapped.
            if height[l] >= lmax:
                lmax = height[l]
            else:
                rain_water += lmax - height[l]

            # Move l forward
            l += 1

        else:
            # Update rmax if we can,
            # else we add to the amount of rain water trapped.
            if height[r] >= rmax:
                rmax = height[r]
            else:
                rain_water += rmax - height[r]

            # Move r backward
            r -= 1

    # return the total amount of rain water trapped.
    return rain_water
