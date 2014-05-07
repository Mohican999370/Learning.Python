__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = 'http://codeforces.com/problemset/problem/148/A'
__version__ = '1.0'


def damage(length: int, step: int, damaged: list) -> None:
    for i in range(step, length + 1, step):
        damaged[i] = 1


def count_undamaged(k: int, l: int, m: int, n: int, d: int) -> int:
    damaged = [0] * (d + 1)

    damage(d, k, damaged)
    damage(d, l, damaged)
    damage(d, m, damaged)
    damage(d, n, damaged)

    return sum(damaged)


k, l, m, n, d = int(input()), int(input()), int(input()), int(input()), int(input())
print(count_undamaged(k, l, m, n, d))