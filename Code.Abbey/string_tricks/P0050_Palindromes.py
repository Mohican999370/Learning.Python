__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'


def is_palindrome(value: str) -> bool:
    value = value.upper() \
        .replace(' ', '') \
        .replace('-', '') \
        .replace(',', '')

    reversed_string = ''.join(reversed(value))
    return reversed_string == value


def main() -> int:
    n = int(input())
    results = [''] * n

    for i in range(n):
        results[i] = 'Y' if is_palindrome(input()) else 'N'

    print(' '.join(results))
    return 0


if __name__ == '__main__':
    exit(main())