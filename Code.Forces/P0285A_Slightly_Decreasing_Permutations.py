__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'


def main() -> int:
    (n, k) = map(int, input().split())
    head = [i for i in range(k + 1, 0, -1)]
    tail = [i for i in range(k + 2, n + 1, 1)]

    print(' '.join(str(i) for i in head + tail))

    return 0


if __name__ == '__main__':
    main()