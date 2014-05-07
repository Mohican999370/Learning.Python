__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__spec__ = 'http://codeforces.com/problemset/problem/158/A'
__version__ = '1.0'

(n, k) = map(int, input().split())
a = [int(i) for i in input().split()]

result = k - 1

if a[result] <= 0:
    result -= 1
    while result >= 0 and a[result] <= 0:
        result -= 1
else:
    while result < len(a) - 1 and a[result + 1] == a[result]:
        result += 1

print(result + 1)