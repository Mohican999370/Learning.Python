__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = 'http://codeforces.com/problemset/problem/149/A'
__version__ = '1.0'

k = int(input())
a = list(int(i) for i in input().split())
a = sorted(a, reverse=True)
grow = 0
i = 0

while grow < k and i < len(a):
    grow += a[i]
    i += 1

if (grow < k):
    print(-1)
else:
    print(i)