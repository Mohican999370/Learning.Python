__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'


def check_sum(array: list) -> int:
    result = 0

    for number in array:
        result = (result + number) * 113 % 10000007

    return result


def main() -> int:
    input()
    numbers = [int(word) for word in input().split()]
    print(check_sum(numbers))

    return 0


if __name__ == '__main__':
    exit(main())