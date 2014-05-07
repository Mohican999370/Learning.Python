__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = 'http://codeforces.com/problemset/problem/318/A'
__version__ = '1.0'


def find(maximum: int, pos: int) -> int:
    odds = maximum // 2 + 1 \
        if maximum % 2 != 0 \
        else maximum // 2

    if pos <= odds:
        return pos * 2 - 1
    else:
        return (pos - odds) * 2

(n, k) = map(int, input().split())
print(find(n, k))