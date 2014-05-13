__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'


def bit_count(number: int) -> int:
    if number < 0:
        number = 4294967296 + number

    a = '{0:b}'.format(number).zfill(32)
    b = str(a)

    return b.count('1')


def main() -> int:
    n = int(input())
    numbers = [int(word) for word in input().split()]
    results = [str(bit_count(number)) for number in numbers]

    print(' '.join(results))
    return 0


if __name__ == '__main__':
    exit(main())