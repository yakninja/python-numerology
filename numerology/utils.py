import math


def count_digits(n):
    """
    Returns count of decimal digits in number
    :param n:
    :return:
    """
    return int(math.log10(n)) + 1


def sum_digits(n, max_digits=None):
    """
    Returns sum of decimal digits in number
    :param n: number
    :param max_digits: if set, runs the function recursively until result has max_digits or less digits
    :return:
    """
    r = 0
    while n:
        r, n = r + n % 10, n // 10

    if max_digits is not None and count_digits(r) > max_digits:
        return sum_digits(r, max_digits)

    return r
