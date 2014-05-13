__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'


def smooth(n: int, data: list) -> list:
    result = [0] * n
    result[0] = data[0]
    result[n - 1] = data[n - 1]

    for i in range(1, n - 1):
        result[i] = (data[i] + data[i - 1] + data[i + 1]) / 3

    return result


def main() -> int:
    n = int(input())
    data = [float(i) for i in input().split()]
    result = [str(i) for i in smooth(n, data)]

    print(' '.join(result))
    return 0


if __name__ == '__main__':
    exit(main())