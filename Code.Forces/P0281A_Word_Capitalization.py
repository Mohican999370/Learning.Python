__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = 'http://codeforces.com/problemset/problem/281/A'
__version__ = '1.0'

def capitalize(s: str) -> str:
    if (len(s) > 0):
        return s[:1].upper() + s[1:]
    else:
        return s

print(capitalize(input()))