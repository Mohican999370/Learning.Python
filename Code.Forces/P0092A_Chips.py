__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'

def count_chips(n: int, m: int) -> int:
    temp = n * (n + 1) // 2
    m %= temp

    for i in range(1, n + 1):
        if m >= i:
            m -= i
        else:
            return m

def main() -> int:
    (n, m) = map(int, input().split())
    print(count_chips(n, m))

    return 0


if __name__ == '__main__':
    exit(main())