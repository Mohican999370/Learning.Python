__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = 'http://codeforces.com/problemset/problem/96/A'
__version__ = '1.0'


def is_dangerous(situation: str) -> str:
    if '1111111' in situation \
            or '0000000' in situation:
        return 'YES'
    return 'NO'

print(is_dangerous(input()))