from math import gcd
from string import ascii_uppercase


def solve_cryptopangram(ciphers: [int]) -> str:
    """
    Decodes the given list of ciphers into the message.
    :param ciphers: A list of products (of two primes).
    :return: The decoded message.
    """
    # Find the index of the next dissimilar ciphers.
    idx = next(
        index for index, cipher in enumerate(ciphers) if cipher != ciphers[0])

    # Find the gcd of the first and the next dissimilar ciphers.
    _gcd = gcd(ciphers[0], ciphers[idx])

    # Record all prime factors encountered so far.
    # All ciphers upto idx can be expressed as a product of the two primes,
    # _gcd and (c[0] // _gcd).
    # As long as these two primes are in our initial primes list, we're good !
    # (i.e. we've recorded all the primes seen at least once)
    # We record 1 prime for each cipher as below, making sure to include _gcd
    # and (c[0] // _gcd) as promised above.
    primes = (idx + 1) % 2 * [_gcd] + (idx + 1) // 2 * [ciphers[0] // _gcd,
                                                        _gcd]

    for cipher in ciphers[idx:]:
        # Get the second prime for the next dissimilar cipher
        _gcd = cipher // _gcd
        primes.append(_gcd)

    # Create a decode dictionary.
    decode = dict(zip(sorted(set(primes)), ascii_uppercase))

    # Return decoded result.
    return "".join(decode[prime] for prime in primes)


def main() -> None:
    """
    Driver function.
    :return: None
    """
    # For each test case in the set, solve it.
    for test_num in range(1, int(input()) + 1):
        # N, L in the next line.
        N, L = map(int, input().split())

        # List of prime products / ciphers.
        *ciphers, = map(int, input().split())

        # Solve for result.
        result = solve_cryptopangram(ciphers)

        # Output result.
        print("Case #{}: {}".format(test_num, result))


if __name__ == '__main__':
    main()
