__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'


def findab(x1: int, y1: int, x2: int, y2: int) -> tuple:
    a = (y1 - y2) // (x1 - x2)
    b = y1 - a * x1

    return (a, b)


def main() -> int:
    n = int(input())
    results = [''] * n

    for i in range(n):
        (x1, y1, x2, y2) = map(int, input().split())
        results[i] = '(%d %d)' % findab(x1, y1, x2, y2)

    print(' '.join(results))
    return 0


if __name__ == '__main__':
    exit(main())