__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__spec__ = 'http://codeforces.com/problemset/problem/131/A'
__version__ = '1.0'

value = input()
last = value[1:]

if (len(last) <= 0 or last.isupper()):
    print(value.swapcase())
else:
    print(value)