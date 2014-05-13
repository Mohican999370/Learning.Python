__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'


def main() -> int:
    n = int(input())
    numbers = [int(word) % 2 for word in input().split()]

    if (numbers[0] + numbers[1] + numbers[2]) > 1:
        print(numbers.index(0) + 1)
    else:
        print(numbers.index(1) + 1)

    return 0


if __name__ == '__main__':
    main()