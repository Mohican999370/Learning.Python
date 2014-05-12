__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = 'http://codeforces.com/problemset/problem/352/A'
__version__ = '1.0'

input()
temp = input()
n0, n5 = temp.count('0'), temp.count('5')

n5 = n5 // 9 * 9

if n0 <= 0:
    print(-1)
elif n5 > 0:
    print('5' * n5 + '0' * n0)
else:
    print(0)