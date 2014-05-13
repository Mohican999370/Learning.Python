__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'


def josephus(n, k):
    r = 0
    i = 1

    while i <= n:
        r = (r + k) % i
        i += 1

    return r + 1


def main() -> int:
    (n, k) = map(int, input().split())

    print(josephus(n, k))
    return 0


if __name__ == '__main__':
    exit(main())