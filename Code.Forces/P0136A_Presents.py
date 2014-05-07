__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = 'http://codeforces.com/problemset/problem/136/A'
__version__ = '1.0'

def gifts(n_friends: int, friends: list) -> list:
    friends.insert(0, 0)
    result = [0] * (n_friends + 1)

    for i in range(1, n_friends + 1):
        result[friends[i]] = i

    return result[1:]

n = int(input())
p = [int(i) for i in input().split()]

print(' '.join(map(str, gifts(n, p))))