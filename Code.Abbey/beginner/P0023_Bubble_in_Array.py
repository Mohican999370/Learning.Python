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


def swap(numbers: list, index1: int, index2: int) -> None:
    temp = numbers[index1]
    numbers[index1] = numbers[index2]
    numbers[index2] = temp


def bubble_stats(numbers: list) -> tuple:
    n_swaps = 0
    n = len(numbers)

    for j in range(n - 1):
        if (numbers[j] > numbers[j + 1]):
            swap(numbers, j, j + 1)
            n_swaps += 1

    return (n_swaps, check_sum(numbers))


def main() -> int:
    numbers = [int(word) for word in input().split()][:-1]
    results = [str(i) for i in bubble_stats(numbers)]
    print(' '.join(results))
    return 0


if __name__ == '__main__':
    exit(main())