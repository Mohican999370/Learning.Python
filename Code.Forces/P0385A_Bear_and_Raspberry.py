__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = 'http://codeforces.com/problemset/problem/385/A'
__version__ = '1.0'


def max_raspberry(n_days: int, lend_price: int, honey_prices: list) -> int:
    money = max(honey_prices[i] - honey_prices[i + 1] for i in range(n_days - 1))

    if money < lend_price:
        return 0

    return money - lend_price

(n, c) = map(int, input().split())
x = [int(i) for i in input().split()]
print(max_raspberry(n, c, x))