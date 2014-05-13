__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'


def array_count(n: int, data: list) -> list:
    result = [0] * (n + 1)

    for item in data:
        result[item] += 1

    return result[1:]


def main() -> int:
    (m, n) = map(int, input().split())
    data = [int(word) for word in input().split()]
    counts = array_count(n, data)

    print(' '.join([str(i) for i in counts]))
    return 0


if __name__ == '__main__':
    exit(main())