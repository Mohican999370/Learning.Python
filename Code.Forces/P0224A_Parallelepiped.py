__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'

from math import sqrt


def main() -> int:
    (x, y, z) = map(int, input().split())
    a1 = int(sqrt((x * y) // z))
    a2 = x // a1
    a3 = y // a1

    print(4 * (a1 + a2 + a3))
    return 0


if __name__ == '__main__':
    exit(main())