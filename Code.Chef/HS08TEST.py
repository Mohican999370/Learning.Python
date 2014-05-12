__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = 'http://www.codechef.com/problems/HS08TEST'
__version__ = '1.0'

(x, y) = map(float, input().split())
balance = y

if int(x) % 5 == 0 and x + 0.5 < y:
    balance = y - x - 0.5

print("%.2f" % balance)