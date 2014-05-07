__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__spec__ = 'http://codeforces.com/problemset/problem/282/A'
__version__ = '1.0'

n = int(input())
result = 0

for _ in range(n):
    statement = input()

    if ('++' in statement):
        result += 1
    elif ('--' in statement):
        result -= 1

print(result)