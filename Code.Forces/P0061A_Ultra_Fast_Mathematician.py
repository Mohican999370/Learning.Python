__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = 'http://codeforces.com/problemset/problem/61/A'
__version__ = '1.0'

def calculate(s1: str, s2: str) -> str:
    result = ['0'] * len(s1)

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            result[i] = '1'

    return ''.join(result)

first, second = input(), input()
print(calculate(first, second))