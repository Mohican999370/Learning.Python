__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'


def main() -> int:
    (n, k, l, c, d, p, nl, np) = map(int, input().split())
    drink_for_toast = k * l // nl
    limes_for_toast = c * d
    salt_for_toast = p // np
    toasts_per_friend = min(drink_for_toast, limes_for_toast, salt_for_toast) // n

    print(toasts_per_friend)
    return 0


if __name__ == '__main__':
    main()