__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = 'http://www.codeabbey.com/index/task_view/median-of-three'
__version__ = '1.0'

n = int(input())
results = [''] * n


def swap(a: list, index1: int, index2: int) -> None:
    temp = a[index1]
    a[index1] = a[index2]
    a[index2] = temp

    return


def sort(a: list) -> None:
    if a[0] > a[2]:
        swap(a, 0, 2)

    if a[1] < a[0]:
        swap(a, 0, 1)
    elif a[1] > a[2]:
        swap(a, 1, 2)

    return


for i in range(n):
    numbers = [int(word) for word in input().split()]
    sort(numbers)
    results[i] = str(numbers[1])

print(' '.join(results))