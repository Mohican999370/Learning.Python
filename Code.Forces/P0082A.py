__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = 'http://codeforces.com/problemset/problem/82/A'
__version__ = '1.0'

import math

n = int(input())
x = 1
cans = 5
oldCans = 0

while cans < n:
    oldCans = cans
    x *= 2
    cans += 5 * x

n -= oldCans
result = math.ceil(n * 1.0 / x)

print(["", "Sheldon", "Leonard", "Penny", "Rajesh", "Howard"][result])