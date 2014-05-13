__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = 'http://codeforces.com/problemset/problem/337/A'
__version__ = '1.0'

def min_differences(n_children: int, n_presents: int, present_pieces: list) -> int:
    present_pieces = sorted(present_pieces)
    diffs = [present_pieces[j + n - 1] - present_pieces[j] for j in range(m - n + 1)]

    return min(diffs)

(n, m) = map(int, input().split())
f = [int(i) for i in input().split()]
print(min_differences(n, m, f))