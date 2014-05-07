__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = 'http://codeforces.com/problemset/problem/160/A'
__version__ = '1.0'

def take_coins(num_coins: int, coins: list) -> int:
    coins = sorted(coins, reverse=True)
    half_sum_coins = sum(coins) // 2
    my_sum_coins = 0
    i = 0

    while (my_sum_coins <= half_sum_coins):
        my_sum_coins += coins[i]
        i += 1

    return i

n, a = int(input()), list(int(i) for i in input().split())
print(take_coins(n, a))