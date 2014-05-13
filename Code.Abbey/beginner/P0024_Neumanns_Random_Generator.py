__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'


def next_neumanns(number: int) -> int:
    number *= number
    number2 = str(number).zfill(8)
    number2 = number2[2:6]

    return int(number2)


def neumanns_count(number: int) -> int:
    next_numbers = [number]
    next_number = next_neumanns(number)
    count = 1

    while True:
        if next_number in next_numbers:
            return count
        else:
            next_numbers.append(next_number)
            next_number = next_neumanns(next_number)
            count += 1


def main() -> int:
    n = int(input())
    numbers = [int(word) for word in input().split()]
    results = [str(neumanns_count(i)) for i in numbers]

    print(' '.join(results))


if __name__ == '__main__':
    exit(main())