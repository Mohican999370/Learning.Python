__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'


def main() -> int:
    n = int(input())

    for i in range(n, n * 2):
        print(i, end=' ')

    return 0


if __name__ == '__main__':
    exit(main())