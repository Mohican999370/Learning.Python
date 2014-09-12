__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'


def find_last_day(n_page: int, reading_schedule: list) -> int:
    sum_schedule = sum(reading_schedule)
    n_page %= sum_schedule

    if n_page % sum_schedule == 0:
        i = 6

        while reading_schedule[i] == 0:
            i -= 1

        return i + 1
    else:
        for i in range(7):
            if n_page <= reading_schedule[i]:
                return i + 1
            else:
                n_page -= reading_schedule[i]

    return 0


def main() -> int:
    n = int(input())
    schedule = [int(word) for word in input().split()]

    print(find_last_day(n, schedule))
    return 0


if __name__ == '__main__':
    exit(main())