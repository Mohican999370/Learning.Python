__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'

input()
bars = list(map(int, input().split()))
towers = {}

for b in bars:
    towers[b] = towers.get(b, 0) + 1

print(max(towers.values()), len(towers))