from functools import reduce
from collections import Counter
from operator import mul


def brute_force(factors: [int]):
    """
    Finds the number of distinct factors of the product of the factors.
    :param factors: The numbers whose product makes up the entire number.
    :return: The numbers whose product makes up the entire number.
    """
    # Find the number by multiplying factors.
    product = reduce(mul, factors)
    # Find the distinct factors by simply counting upto the number.
    factors = [i for i in range(1, product + 1) if not product % i]
    # Return the number of distinct factors seen.
    return len(factors)


def brute_force_optimized(factors: [int]):
    """
    Finds the number of distinct factors of the product of the factors.
    :param factors: The numbers whose product makes up the entire number.
    :return: The numbers whose product makes up the entire number.
    """
    # Find the number by multiplying factors.
    product = reduce(mul, factors)
    # Find the distinct factors by counting only upto the number // 2.
    # This finds all the factors of the number excluding the number itself.
    factors = [i for i in range(1, product // 2 + 1) if not product % i]
    # Return the number of factors
    return len(factors) + 1


def brute_force_further_optimized(factors: [int]):
    """
    Finds the number of distinct factors of the product of the factors.
    :param factors: The numbers whose product makes up the entire number.
    :return: The numbers whose product makes up the entire number.
    """
    # Find the number by multiplying factors.
    product = reduce(mul, factors)

    # Find the distinct factors by counting only upto the number ** 0.5 which is
    # a smaller search space compared to number // 2.
    # We use the fact that if i is a factor, n // i is also a factor.
    factors = reduce(list.__add__, ([i, product // i]
                                    for i in range(1, int(product ** 0.5) + 1)
                                    if not product % i))

    # We could simply
    # return len(set(factors))
    # but we know why we may have a duplicate in the first place.

    # If the number is a perfect square, we would have counted it's root twice
    # instead of just once, as we add both [i, product // i] to factors.
    # Ex- factors for 25 = [1, 5, 5, 25].
    is_perfect_square = product ** 0.5 // 1 == product ** 0.5

    # Return the number of factors, accounting for a duplicate in case the
    # number is a perfect square.
    return len(factors) - 1 if is_perfect_square else len(factors)


def _prime_factors(num: int):
    """
    Finds the prime factors of a the number num passed to it.
    :param num: The number whose prime factorization is ot be found.
    :return: The prime factorization of num.
    """
    # Array to hold the prime factors.
    __factors = []

    # Take care of all the even composite numbers.
    while not num % 2:
        __factors.append(2)
        num //= 2

    # Take care of all the odd composite numbers.
    for i in range(3, int(num ** 0.5) + 1, 2):
        while not num % i:
            __factors.append(i)
            num //= i

    # In case num is a prime number, add it to the list of factors.
    if num > 2:
        __factors.append(num)

    # Return the factors
    return __factors


def optimal_solution(factors: [int]):
    """
    Finds the number of distinct factors of the product of the factors.
    :param factors: The numbers whose product makes up the entire number.
    :return: The numbers whose product makes up the entire number.
    """
    # Find all the prime factors of each of the numbers in the factors list.
    # We can find the prime factors of the number individually, since it would
    # be equivalent to finding the prime factorization of the number formed by
    # multiplying the them.
    prime_factors = reduce(list.__add__, (_prime_factors(f) for f in factors))

    # Number of distinct factors of a num = p^x * q^y * r^z * ...
    # is = (x + 1) * (y + 1) * (z + 1) * ...
    num_factors = reduce(mul, (x + 1 for x in Counter(prime_factors).values()))

    # Return the number of distinct factors.
    return num_factors


def solve_number_of_factors(factors: [int]):
    """
    Calls different solutions to find the number of distinct factors of the
    product of the factors.
    :param factors: The numbers whose product makes up the entire number.
    :return: The numbers whose product makes up the entire number.
    """
    # return brute_force(factors)
    # return brute_force_optimized(factors)
    # return brute_force_further_optimized(factors)
    return optimal_solution(factors)


def main():
    """
    Driver function.
    :return: None
    """
    # For each test case,
    for num_test in range(1, 1 + int(input())):
        # Get the length of the list,
        _len = int(input())
        # Get the factors,
        *factors, = map(int, input().split())
        # Find the number of factors,
        result = solve_number_of_factors(factors)
        # Output the result.
        print(result)


if __name__ == '__main__':
    main()
