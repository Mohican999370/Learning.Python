__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'

from fractions import gcd


def main() -> int:
    (x, y, a, b) = map(int, input().split())
    lcm = x * y // gcd(x, y)

    print(b // lcm - (a - 1) // lcm)
    return 0


if __name__ == '__main__':
    exit(main())