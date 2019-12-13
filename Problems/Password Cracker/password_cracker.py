from sys import setrecursionlimit

setrecursionlimit(10 ** 6)


def passwordCracker(passwords, loginAttempt, memo={}):
    """
    Checks if the loginAttempt is valid or not based on the problem definition,
    i.e. the loginAttempt can be made up from the given by concatenation.
    :param passwords: The passwords of all the users.
    :param loginAttempt: The loginAttempt to be validated.
    :param memo: A dictionary to hold the combinations for a password.
    :return:
    """
    # If we already have the answer return it.
    if loginAttempt in memo: return memo[loginAttempt]

    if loginAttempt == '':
        memo[loginAttempt] = []
        return memo[loginAttempt]

    # If the attempted password is already a valid password, return it.
    if loginAttempt in passwords:
        memo[loginAttempt] = [loginAttempt]
        return memo[loginAttempt]

    for password in passwords:
        _len = len(password)

        # We try to match the current loginAttempt to the current password,
        # If we find a match, we try again on the remainder of the loginAttempt
        if loginAttempt[:_len] == password:
            result = passwordCracker(passwords, loginAttempt[_len:], memo)

            # If we find a valid combination, return.
            if result != False:
                memo[loginAttempt] = [password] + result
                return memo[loginAttempt]

    # Otherwise no combination is possible for the given attempt.
    memo[loginAttempt] = False
    return memo[loginAttempt]
