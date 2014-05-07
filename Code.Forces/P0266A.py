__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = 'http://codeforces.com/problemset/problem/266/A'
__version__ = '1.0'

import re

n = int(input())
stones = input()

repeats = [len(i) - 1 for i in re.findall('R{2,}|G{2,}|B{2,}', stones)]
print(sum(repeats))