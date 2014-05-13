__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'


def fibonacci(size: int) -> list:
    if size < 1:
        return []
    elif size < 2:
        return [0]
    else:
        fibo = [0] * size
        fibo[1] = 1

        for i in range(2, size):
            fibo[i] = fibo[i - 1] + fibo[i - 2]

        return fibo


def main() -> int:
    n = int(input())
    results = [''] * n
    fibo = fibonacci(1000)

    for i in range(n):
        results[i] = str(fibo.index(int(input())))

    print(' '.join(results))
    return 0


if __name__ == '__main__':
    exit(main())