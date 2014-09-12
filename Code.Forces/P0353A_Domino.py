__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'


def main() -> int:
    n = int(input())
    has_even_odd_domino = False
    sum_uppers, sum_lowers = 0, 0

    for _ in range(n):
        (upper, lower) = map(int, input().split())
        sum_uppers += upper
        sum_lowers += lower

        if (upper + lower) % 2 != 0:
            has_even_odd_domino = True

    if (sum_lowers % 2 == 0) and (sum_uppers % 2 == 0):
        print(0)
    elif (sum_lowers % 2 != 0) and (sum_uppers % 2 != 0):
        if has_even_odd_domino:
            print(1)
        else:
            print(-1)
    else:
        print(-1)

    return 0


if __name__ == '__main__':
    exit(main())