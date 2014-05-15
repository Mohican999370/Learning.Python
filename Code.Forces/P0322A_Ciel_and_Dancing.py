__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'


def main() -> int:
    (n, m) = map(int, input().split())

    print(n + m - 1)

    for i in range(1, m + 1):
        print('1 %d' % i)

    for i in range(2, n + 1):
        print('%d 1' % i)

    return 0


if __name__ == '__main__':
    exit(main())