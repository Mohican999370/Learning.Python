__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'


def is_triangle(a: int, b: int, c: int) -> bool:
    if a + b > c \
            and a + c > b \
            and b + c > a \
            and abs(a - b) < c \
            and abs(b - c) < a \
            and abs(a - c) < b:
        return True

    return False


def main() -> int:
    n = int(input())
    results = [''] * n

    for i in range(n):
        (a, b, c) = map(int, input().split())
        results[i] = '1' if is_triangle(a, b, c) else '0'

    print(' '.join(results))
    return 0


if __name__ == '__main__':
    exit(main())