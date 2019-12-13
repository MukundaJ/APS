def reachingPoints(sx: int, sy: int, tx: int, ty: int) -> bool:
    """
    Finds if we can reach tx, ty form sx, sy using only the transformations
    given in the problem.
    :param sx: The source x coordinate.
    :param sy: The source y coordinate.
    :param tx: The destination x coordinate.
    :param ty: The destination y coordinate.
    :return: A boolean value indicating if such a transform is possible.
    """
    # No transformation possible, since we can only increase sx and sy.
    if tx < sx or ty < sy: return False
    # If the source and destination are the same return true.
    if tx == sx and ty == sy: return True
    # ty must be of the form sy + n * tx
    if tx == sx: return (ty - sy) % tx == 0
    # tx must be of the form sx + n * ty
    if ty == sy: return (tx - sx) % ty == 0

    # The greater one could only have been made by addition from the the other
    # co-ordinate.
    if tx > ty:
        return reachingPoints(sx, sy, tx % ty, ty)
    else:
        return reachingPoints(sx, sy, tx, ty % tx)