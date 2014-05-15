__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'


def print_list(numbers: list) -> None:
    temp = [str(number) for number in numbers]
    print(len(temp), end=' ')
    print(' '.join(temp))


def main() -> int:
    n = int(input())
    numbers = [int(word) for word in input().split()]

    negatives = [i for i in numbers if i < 0]
    positives = [i for i in numbers if i > 0]
    zero = [0]

    group1 = [negatives[0]]
    group2 = negatives[1:] + positives

    if len(negatives) % 2 == 0:
        zero.append(group2[0])
        group2 = group2[1:]

    print_list(group1)
    print_list(group2)
    print_list(zero)

    return 0


if __name__ == '__main__':
    exit(main())