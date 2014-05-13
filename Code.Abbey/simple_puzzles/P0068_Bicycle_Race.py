__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'


def s1(s: int, v1: int, v2: int) -> float:
    return s * v1 / (v1 + v2)


def main() -> int:
    n = int(input())
    results = [''] * n

    for i in range(n):
        (s, v1, v2) = map(int, input().split())
        results[i] = str(s1(s, v1, v2))

    print(' '.join(results))
    return 0


if __name__ == '__main__':
    exit(main())