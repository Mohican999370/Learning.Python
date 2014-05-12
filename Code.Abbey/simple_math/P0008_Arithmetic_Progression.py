__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = 'http://www.codeabbey.com/index/task_view/arithmetic-progression'
__version__ = '1.0'

count = int(input())
results = [''] * count

for i in range(count):
    (a, b, n) = map(int, input().split())
    result = n * a + n * (n - 1) * b // 2
    results[i] = str(result)

print(' '.join(results))