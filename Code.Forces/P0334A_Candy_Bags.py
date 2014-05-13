__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = 'http://codeforces.com/problemset/problem/334/A'
__version__ = '1.0'

n = int(input())
n2 = n * n + 1
ndiv2 = n // 2

for i in range(1, n + 1):
    first = list(range(ndiv2 * (i - 1) + 1, ndiv2 * i + 1))
    last = [n2 - k for k in first]
    candies = first + last
    print(' '.join(map(str, candies)))