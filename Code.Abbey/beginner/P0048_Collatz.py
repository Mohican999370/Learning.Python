__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'


def collatz(number: int) -> int:
    count = 0

    while number != 1:
        number = number // 2 if number % 2 == 0 else number * 3 + 1
        count += 1

    return count


def main() -> int:
    input()
    numbers = [int(word) for word in input().split()]
    results = [str(collatz(i)) for i in numbers]

    print(' '.join(results))
    return 0


if __name__ == '__main__':
    exit(main())