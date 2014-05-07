__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__spec__ = 'http://codeforces.com/problemset/problem/231/A'
__version__ = '1.0'

n = int(input())
result = 0

for i in range(n):
    if (input().count('1') >= 2):
        result += 1

print(result)