__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__spec__ = 'http://codeforces.com/problemset/problem/116/A'
__version__ = '1.0'

n = int(input())
passengers = 0
min_passengers = 0

for i in range(n):
    (a, b) = map(int, input().split())
    passengers = passengers - a + b
    min_passengers = max(min_passengers, passengers)

print(min_passengers)