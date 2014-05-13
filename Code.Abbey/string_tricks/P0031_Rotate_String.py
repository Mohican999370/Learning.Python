__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'


def rotate_string(value: str, where: int) -> str:
    return value[where:] + value[:where]


def main() -> int:
    n = int(input())
    results = [''] * n

    for i in range(n):
        inputs = input().split()
        results[i] = rotate_string(inputs[1], int(inputs[0]))

    print(' '.join(results))
    return 0


if __name__ == '__main__':
    exit(main())