__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = 'http://codeforces.com/problemset/problem/344/A'
__version__ = '1.0'

def input_magnets() -> str:
    n = int(input())
    result = ''

    for _ in range(n):
        result += input()

    return result

def count_groups(magnets: str):
    return magnets.count('00') + magnets.count('11') + 1

print(count_groups(input_magnets()))