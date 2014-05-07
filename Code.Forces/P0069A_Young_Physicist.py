__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = 'http://codeforces.com/problemset/problem/69/A'
__version__ = '1.0'


def input_forces() -> dict:
    n = int(input())
    result = {'x': [], 'y': [], 'z': []}

    for i in range(n):
        (x, y, z) = map(int, input().split())
        result['x'].append(x)
        result['y'].append(y)
        result['z'].append(z)

    return result


def is_in_equilibrium(forces: dict) -> bool:
    return sum(forces['x']) == 0 and \
           sum(forces['y']) == 0 and \
           sum(forces['z']) == 0


if (is_in_equilibrium(input_forces())):
    print('YES')
else:
    print('NO')