__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'

n = int(input())
data = [None] * n

for i in range(n):
    (a, b) = map(int, input().split())
    data[i] = sum(a, b)

results = [str(i) for i in data]
print(' '.join(results))