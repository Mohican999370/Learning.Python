__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = 'http://codeforces.com/problemset/problem/313/A'
__version__ = '1.0'


def maximize(state: str) -> int:
    intstate = int(state)

    if intstate >= 0:
        return intstate

    if intstate >= -10:
        return 0

    a = int(state[:-1])
    b = int(state[:-2] + state[-1])

    return max(a, b)

print(maximize(input()))