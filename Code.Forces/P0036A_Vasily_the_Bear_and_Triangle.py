__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'


def main() -> int:
    (x0, y0) = map(int, input().split())

    if x0 * y0 > 0:
        b = x0 + y0

        if b > 0:
            print('0 %d %d 0' % (b, b))
        else:
            print('%d 0 0 %d' % (b, b))
    else:
        b = y0 - x0

        if b < 0:
            print('0 %d %d 0' % (b, -b))
        else:
            print('%d 0 0 %d' % (-b, b))

    return 0


if __name__ == '__main__':
    exit(main())