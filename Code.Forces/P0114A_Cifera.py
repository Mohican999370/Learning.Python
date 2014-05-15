__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'

from math import log, pow


def main() -> int:
    k = int(input())
    l = int(input())

    if (l < k):
        print('NO')
    else:
        temp = int(log(l, k))
        temp_pow = int(pow(k, temp))

        if temp_pow == l:
            print('YES', temp - 1, sep='\n')
        elif temp_pow * k == l:
            print('YES', temp, sep='\n')
        else:
            print('NO')

    return 0


if __name__ == '__main__':
    exit(main())