__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'

def is_regular_angle(angle: int) -> int:
    return 1 if (360 % (180 - angle)) == 0 else 0

n = int(input())
messages = ['NO', 'YES']

for _ in range(n):
    print(messages[is_regular_angle(int(input()))])