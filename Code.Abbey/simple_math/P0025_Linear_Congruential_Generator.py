__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'


def generate(A, C, M, X0, N) -> int:
    for _ in range(N):
        X0 = (A * X0 + C) % M

    return X0


def main() -> int:
    n = int(input())
    results = [''] * n

    for i in range(n):
        (A, C, M, X0, N) = map(int, input().split())
        results[i] = str(generate(A, C, M, X0, N))

    print(' '.join(results))
    return 0


if __name__ == '__main__':
    exit(main())