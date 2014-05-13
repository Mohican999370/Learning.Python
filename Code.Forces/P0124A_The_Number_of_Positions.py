__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'

(n, a, b) = map(int, input().split())
print(min(b, n - a - 1) + 1)