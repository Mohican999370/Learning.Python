__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'


def count_cases(a: int, b: int) -> list:
    count = [0, 0, 0]

    for i in range(1, 7):
        if abs(a - i) < abs(b - i):
            count[0] += 1
        elif abs(a - i) == abs(b - i):
            count[1] += 1
        else:
            count[2] += 1

    return count


def main() -> int:
    (a, b) = map(int, input().split())

    print(' '.join([str(i) for i in count_cases(a, b)]))
    return 0


if __name__ == '__main__':
    exit(main())