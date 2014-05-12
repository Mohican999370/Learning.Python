__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = 'http://codeforces.com/problemset/problem/330/A'
__version__ = '1.0'

(row, col) = map(int, input().split())
inputs = [''] * row
hasS = {
    'row': [0] * row,
    'col': [0] * col
}

for i in range(row):
    inputs[i] = input()

for i in range(row):
    for j in range(col):
        if (inputs[i][j] == 'S'):
            hasS['row'][i] = 1
            hasS['col'][j] = 1

rowcount = row - sum(hasS['row'])
colcount = col - sum(hasS['col'])

result = rowcount * col + colcount * row - rowcount * colcount
print(result)