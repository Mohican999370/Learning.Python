__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'


def swap(numbers: list, indexes: list, index1: int, index2: int) -> None:
    temp = numbers[index1]
    numbers[index1] = numbers[index2]
    numbers[index2] = temp

    temp = indexes[index1]
    indexes[index1] = indexes[index2]
    indexes[index2] = temp

    return


def bubble_sort(n: int, numbers: list) -> list:
    indexes = [i + 1 for i in range(n)]

    for i in range(n - 1):
        swaps = False

        for j in range(n - 1):
            if numbers[j] > numbers[j + 1]:
                swap(numbers, indexes, j, j + 1)
                swaps = True

        if not swaps:
            break

    return indexes


def main() -> int:
    n = int(input())
    numbers = [int(word) for word in input().split()]
    result = bubble_sort(n, numbers)
    result_string = [str(i) for i in result]

    print(' '.join(result_string))
    return 0


if __name__ == '__main__':
    exit(main())