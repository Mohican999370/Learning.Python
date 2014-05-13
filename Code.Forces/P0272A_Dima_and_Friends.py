__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'


def main() -> int:
    n = int(input()) + 1
    fingers = [int(word) for word in input().split()]
    sum_fingers = sum(fingers)
    count = 0

    for i in range(sum_fingers + 1, sum_fingers + 6, 1):
        if i % n == 1:
            count += 1

    result = 5 - count
    print(result)

    return 0


if __name__ == '__main__':
    main()