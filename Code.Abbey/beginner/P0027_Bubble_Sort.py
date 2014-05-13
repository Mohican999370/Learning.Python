__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'


def swap(numbers: list, index1: int, index2: int) -> None:
    temp = numbers[index1]
    numbers[index1] = numbers[index2]
    numbers[index2] = temp


def bubble_stats(n: int, numbers: list) -> tuple:
    n_passes = 0
    n_swaps = 0

    for i in range(n - 1):
        n_passes += 1
        current_swaps = 0

        for j in range(n - 1):
            if (numbers[j] > numbers[j + 1]):
                swap(numbers, j, j + 1)
                current_swaps += 1

        if current_swaps <= 0:
            return (n_passes, n_swaps)
        else:
            n_swaps += current_swaps


def main() -> int:
    n = int(input())
    numbers = [int(word) for word in input().split()]
    results = [str(i) for i in bubble_stats(n, numbers)]
    print(' '.join(results))
    return 0


if __name__ == '__main__':
    exit(main())