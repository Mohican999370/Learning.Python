__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'

n = int(input())
data = [0] * n

for i in range(n):
    (a, b, c) = map(int, input().split())
    data[i] = min(a, b, c)

results = [str(i) for i in data]
print(' '.join(results))