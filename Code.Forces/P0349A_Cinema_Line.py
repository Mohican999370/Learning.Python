__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = 'http://codeforces.com/problemset/problem/349/A'
__version__ = '1.0'


def can_sell(client_moneys: list) -> bool:
    current = {
        25: 0,
        50: 0,
        100: 0 # This is not necessary
    }

    for money in client_moneys:
        if money == 25:
            current[25] += 1
        elif money == 50:
            if current[25] < 1:
                return False
            else:
                current[25] -= 1
                current[50] += 1
        elif money == 100:
            if current[25] < 1:
                return False
            elif current[50] > 0:
                current[25] -= 1
                current[50] -= 1
            elif current[25] < 3:
                return False
            else:
                current[25] -= 3

            current[100] += 1

    return True


input()
moneys = [int(i) for i in input().split()]
print('YES' if can_sell(moneys) else 'NO')