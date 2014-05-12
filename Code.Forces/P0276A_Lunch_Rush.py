__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = 'http://codeforces.com/problemset/problem/276/A'
__version__ = '1.0'


def joy(f: int, t: int, k: int) -> int:
    return f - (t - k) if t > k else f


(n, k) = map(int, input().split())
joys = [0] * n

for i in range(n):
    (f, t) = map(int, input().split())
    joys[i] = joy(f, t, k)

print(max(joys))