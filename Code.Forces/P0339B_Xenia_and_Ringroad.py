__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = 'http://codeforces.com/problemset/problem/339/B'
__version__ = '1.0'

(n, m) = map(int, input().split())
a = [int(i) for i in input().split()]

indexes = [j for j in range(m - 1) if a[j + 1] < a[j]]

if len(indexes) > 0:
    print(len(indexes) * n + max(a[indexes[-1]+1:]) - 1)
else:
    print(a[-1] - 1)