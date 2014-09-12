__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'


def main() -> int:
    n = int(input())
    result = [str(n)] + [str(i) for i in range(1, n)]

    print(' '.join(result))
    return 0


if __name__ == '__main__':
    exit(main())