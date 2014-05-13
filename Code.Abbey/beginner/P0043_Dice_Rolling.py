__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'


def dice(value: float, N: int) -> int:
    return int(value * N) + 1


def main() -> int:
    n = int(input())
    results = [''] * n
    N = 6

    for i in range(n):
        value = float(input())
        results[i] = str(dice(value, N))

    print(' '.join(results))
    return 0


if __name__ == '__main__':
    exit(main())