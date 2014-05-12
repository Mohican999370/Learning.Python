__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = 'http://codeforces.com/problemset/problem/214/A'
__version__ = '1.0'

(n, m) = map(int, input().split())
count = 0

for a in range(32):
    b = n - a * a

    if b >= 0 and (m - b * b) == a:
        count += 1

print(count)