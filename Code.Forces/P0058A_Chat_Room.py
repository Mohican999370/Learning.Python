__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = 'http://codeforces.com/problemset/problem/58/A'
__version__ = '1.0'

import re


def is_hello(s: str) -> bool:
    return re.match('.*h.*e.*l.*l.*o.*', s)


if (is_hello(input())):
    print('YES')
else:
    print('NO')