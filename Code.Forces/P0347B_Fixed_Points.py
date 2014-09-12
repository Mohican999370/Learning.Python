__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'


def main() -> int:
    n = int(input())
    numbers = [int(word) for word in input().split()]
    count_fixed = 0
    has_swap = False

    for i in range(n):
        if i == numbers[i]:
            count_fixed += 1
        elif numbers[numbers[i]] == i:
            has_swap = True

    if count_fixed == n:
        print(count_fixed)
    elif has_swap:
        print(count_fixed + 2)
    else:
        print(count_fixed + 1)

    return 0


if __name__ == '__main__':
    exit(main())