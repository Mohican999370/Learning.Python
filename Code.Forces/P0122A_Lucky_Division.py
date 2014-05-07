__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = 'http://codeforces.com/problemset/problem/122/A'
__version__ = '1.0'

def is_almost_lucky_number(number: int) -> bool:
    lucky_numbers_under_1000 = [4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777]

    for lucky_number in lucky_numbers_under_1000:
        if number % lucky_number == 0:
            return True
        elif number < lucky_number:
            break

    return False

n = int(input())

if (is_almost_lucky_number(n)):
    print('YES')
else:
    print('NO')