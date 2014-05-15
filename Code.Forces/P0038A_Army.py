__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'


def count_years(rank_years: list, a: int, b: int) -> int:
    return sum(rank_years[a - 1:b - 1])


def main() -> int:
    n = int(input())
    rank_years = [int(word) for word in input().split()]
    (a, b) = map(int, input().split())

    print(count_years(rank_years, a, b))
    return 0


if __name__ == '__main__':
    exit(main())