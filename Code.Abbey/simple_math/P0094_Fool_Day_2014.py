__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'


def fool_input() -> int:
    numbers = [int(word) for word in input().split()]
    return sum(number * number for number in numbers)


def main() -> int:
    n = int(input())
    results = [str(fool_input()) for _ in range(n)]

    print(' '.join(results))
    return 0


if __name__ == '__main__':
    exit(main())