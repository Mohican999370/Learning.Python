__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = 'http://codeforces.com/problemset/problem/379/A'
__version__ = '1.0'

def calculate_hour(candles: int, pieces: int) -> int:
    hour = 0
    went_outs = 0

    while candles > 0:
        hour += candles
        went_outs += candles
        candles = went_outs // pieces
        went_outs %= pieces

    return hour

(a, b) = map(int, input().split())
print(calculate_hour(a, b))