__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = 'http://codeforces.com/problemset/problem/119/A'
__version__ = '1.0'


def greatest_common_divisor(a: int, b: int) -> int:
    if b == 0:
        return a
    else:
        return greatest_common_divisor(b, a % b)


def the_winner_is(a: int, b: int, n: int) -> int:
    if n == 0:
        return 1

    n -= greatest_common_divisor(a, n)

    if n == 0:
        return 0

    n -= greatest_common_divisor(b, n)

    return the_winner_is(a, b, n)


(a, b, n) = map(int, input().split())
print(the_winner_is(a, b, n))