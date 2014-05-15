__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'


def find_point(n: int, k: int, squares: list) -> int:
    if k > n:
        return -1

    squares = sorted(squares, reverse=True)
    return squares[k - 1]


def main() -> int:
    (n, k) = map(int, input().split())
    squares = [int(word) for word in input().split()]
    result = find_point(n, k, squares)

    if result < 0:
        print(result)
    else:
        print(result, result)

    return 0


if __name__ == '__main__':
    exit(main())