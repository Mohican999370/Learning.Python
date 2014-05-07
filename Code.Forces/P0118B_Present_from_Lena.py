__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = 'http://codeforces.com/problemset/problem/118/B'
__version__ = '1.0'

number = '0123456789'
n = int(input())
spaces = n * 2
output = [None] * (n * 2 + 1)

for i in range(0, n + 1):
    value = ' ' * spaces + ' '.join(number[:i] + number[i::-1])
    spaces -= 2
    output[i] = output[n * 2 - i] = value

print('\n'.join(output))