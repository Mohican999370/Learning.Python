__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'


def count_stealing_ways(n: int, cookie_bags: list) -> int:
    sum_cookies = sum(cookie_bags)
    temp = sum_cookies % 2

    return sum(1 for bag in cookie_bags if bag % 2 == temp)


def main() -> int:
    n = int(input())
    cookie_bags = [int(word) for word in input().split()]

    print(count_stealing_ways(n, cookie_bags))
    return 0


if __name__ == '__main__':
    exit(main())