__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'


def sum_digit(string: str) -> int:
    return sum(int(char) for char in string)


def is_lucky_ticket(n: int, ticket: str) -> bool:
    if (ticket.count('4') + ticket.count('7')) != n:
        return False

    return sum_digit(ticket[:n // 2]) == sum_digit(ticket[n // 2:])


def main() -> int:
    n = int(input())
    ticket = input()

    print('YES' if is_lucky_ticket(n, ticket) else 'NO')
    return 0


if __name__ == '__main__':
    exit(main())