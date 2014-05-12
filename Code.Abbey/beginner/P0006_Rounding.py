__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = 'http://www.codeabbey.com/index/task_view/rounding'
__version__ = '1.0'

n = int(input())
results = [''] * n

for i in range(n):
    (a, b) = map(int, input().split())
    results[i] = str(round(a / b))

print(' '.join(results))