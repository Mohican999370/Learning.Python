__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = 'http://codeforces.com/problemset/problem/401/A'
__version__ = '1.0'

import math

(n, x) = map(int, input().split())
sum_found = sum([int(i) for i in input().split()])
sum_need = abs(sum_found)

print(math.ceil(sum_need / x))