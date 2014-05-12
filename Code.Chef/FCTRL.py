__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = 'http://www.codechef.com/problems/FCTRL'
__version__ = '1.0'

import sys

def fac_zeros(number: int) -> int:
    k = 5
    result = 0

    while number >= k:
        number = number // k
        result += number

    return result

n = int(input())
array = map(int, sys.stdin.readlines())

for i in array:
    print(fac_zeros(i))