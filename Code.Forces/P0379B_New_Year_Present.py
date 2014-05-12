__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = 'http://codeforces.com/problemset/problem/379/B'
__version__ = '1.0'

n = int(input())
wallets = [int(i) for i in input().split()]

pos = 0
output = []

while pos < n:
    if wallets[pos] > 0:
        output.append('P')
        wallets[pos] -= 1

        if pos == n - 1 and wallets[pos] == 0 and wallets[pos - 1] == 0:
            break

        if (pos > 0 and wallets[pos - 1] > 0) or (pos == n - 1):
            pos -= 1
            output.append('L')
        else:
            pos += 1

            if (pos < n):
                output.append('R')
    else:
        if pos > 0 and wallets[pos - 1] > 0:
            pos -= 1
            output.append('L')
        else:
            pos += 1

            if (pos < n):
                output.append('R')

print(''.join(output))