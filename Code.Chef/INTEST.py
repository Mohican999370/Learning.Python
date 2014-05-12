__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = 'http://www.codechef.com/problems/INTEST'
__version__ = '1.0'

import sys

count = 0

n, k = map(int, sys.stdin.readline().split(" "))
array = map(int, sys.stdin.readlines())

for number in array:
    if number % 5 == 0:
        count += 1

print(count)