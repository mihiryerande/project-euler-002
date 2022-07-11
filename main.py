# Problem 2:
#     Even Fibonacci Numbers
#
# Description:
#     Each new term in the Fibonacci sequence is generated by adding the previous two terms.
#     By starting with 1 and 2, the first 10 terms will be:
#         1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
#     By considering the terms in the Fibonacci sequence whose values do not exceed four million,
#       find the sum of the even-valued terms.

from math import floor, sqrt

PHI = (1 + sqrt(5)) / 2


def fib(i: int) -> int:
    """
    Return the i'th Fibonacci number, where...
      * F_0 = 0
      * F_1 = 1
      * F_{i+2} = F_{i+1} + F_i (for i > 1)

    Args:
        i (int): Index of Fibonacci number in sequence

    Returns:
        (int): i'th Fibonacci number
    """
    return floor(PHI ** i / sqrt(5) + 0.5)


def main(n: int) -> int:
    """
    Returns the sum of all even Fibonacci numbers less than `n`.

    Args:
        n (int): Natural number

    Returns:
        (int): Sum of all even Fibonacci numbers less than `n`

    Raises:
        AssertError: if incorrect params are given
    """
    assert type(n) == int and n > 0

    s = 0
    i = 0
    next_fib = 0
    while next_fib < n:
        s += next_fib
        # Step forward three times to skip to next even Fib
        i += 3
        next_fib = fib(i)
    return s


if __name__ == '__main__':
    num = int(input('Enter a natural number: '))
    ans = main(num)
    print('Sum of Even Fibonacci numbers below {}:\n{}'.format(num, ans))
