__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__spec__ = 'http://codeforces.com/problemset/problem/1/A'
__version__ = '1.0'

import math

(n, m, a) = (int(i) for i in input().split())

result = math.ceil(n * 1.0 / a) * math.ceil(m * 1.0 / a)
print('%i' % result)