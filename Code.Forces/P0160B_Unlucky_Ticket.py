__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'


def is_definitely_unlucky(n: int, ticket: str) -> bool:
    digits = list(ticket)

    left = sorted(digits[:n])
    right = sorted(digits[n:])

    if left[0] == right[0]:
        return False

    condition = left[0] < right[0]

    for i in range(1, n):
        if (left[i] == right[i]) or (left[i] < right[i]) != condition:
            return False

    return True


def main() -> int:
    n = int(input())
    ticket = input()

    print('YES' if is_definitely_unlucky(n, ticket) else 'NO')
    return 0


if __name__ == '__main__':
    exit(main())