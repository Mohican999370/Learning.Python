__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'


def sum_digits(number: int) -> int:
    result = 0

    while number != 0:
        result += number % 10
        number //= 10

    return result


def sum_digits_expression(number1: int, number2: int, number3: int) -> int:
    return sum_digits(number1 * number2 + number3)


def main() -> int:
    n = int(input())
    results = [''] * n

    for i in range(n):
        (a, b, c) = map(int, input().split())
        results[i] = str(sum_digits_expression(a, b, c))

    print(' '.join(results))

    return 0


if __name__ == '__main__':
    exit(main())