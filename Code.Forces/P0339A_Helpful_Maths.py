__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = 'http://codeforces.com/problemset/problem/339/A'
__version__ = '1.0'

def arrange(expression: str) -> str:
    operands = sorted(expression.split(sep='+'))
    return '+'.join(operands)

print(arrange(input()))