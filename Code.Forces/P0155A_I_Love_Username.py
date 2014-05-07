__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = 'http://codeforces.com/problemset/problem/155/A'
__version__ = '1.0'

n = int(input())
scores = [int(i) for i in input().split()]
min = max = scores[0]
amazing = 0

for i in range(1, n):
    if scores[i] > max:
        max = scores[i]
        amazing += 1
    elif scores[i] < min:
        min = scores[i]
        amazing += 1

print(amazing)