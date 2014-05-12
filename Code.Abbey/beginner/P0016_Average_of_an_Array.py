__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = 'http://www.codeabbey.com/index/task_view/average-of-array'
__version__ = '1.0'

n = int(input())
results = [''] * n

for i in range(n):
    numbers = [int(word) for word in input().split()]
    results[i] = str(round(sum(numbers) * 1.0 / (len(numbers) - 1)))

print(' '.join(results))