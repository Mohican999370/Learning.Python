__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'

import math


def f(coefficients: tuple, value: float) -> float:
    return coefficients[0] * value \
           + coefficients[1] * math.sqrt(value * value * value) \
           - coefficients[2] * math.exp(-value / 50) \
           - coefficients[3]


def binary_search(coefficients: tuple) -> float:
    left, right, mid = 0, 100, 50
    epsilon = 1

    while epsilon > 0.00000001:
        mid = (left + right) / 2
        result = f(coefficients, mid)
        epsilon = math.fabs(result)

        if result < 0:
            left = mid
        else:
            right = mid

    return mid


def input_coefficients() -> tuple:
    (a, c, b, d) = map(float, input().split())
    return (a, c, b, d)


def main() -> int:
    n = int(input())
    results = [''] * n

    for i in range(n):
        results[i] = str(binary_search(input_coefficients()))

    print(' '.join(results))
    return 0


if __name__ == '__main__':
    exit(main())