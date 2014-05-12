__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = 'http://www.codeabbey.com/index/task_view/min-of-two'
__version__ = '1.0'

n = int(input())
data = [0] * n

for i in range(n):
    (a, b) = map(int, input().split())
    data[i] = min(a, b)

results = [str(i) for i in data]
print(' '.join(results))