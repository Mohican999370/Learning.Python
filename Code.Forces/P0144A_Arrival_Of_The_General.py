__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = 'http://codeforces.com/problemset/problem/144/A'
__version__ = '1.0'

def count_swap(soldiers: list) -> int:
    length = len(soldiers)
    max_height = max(soldiers)
    min_height = min(soldiers)
    max_solder_index = soldiers.index(max_height)
    mix_solder_index = length - 1 - soldiers[::-1].index(min_height)

    result = max_solder_index + (length - 1 - mix_solder_index)

    if (max_solder_index > mix_solder_index):
        result -= 1

    return result

n = int(input())
a = [int(i) for i in input().split()]
print(count_swap(a))