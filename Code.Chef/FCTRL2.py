__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'

size = 101
array = [0] * size
array[0] = 1

for i in range(1, size):
    array[i] = i * array[i - 1]

t = int(input())

for _ in range(t):
    number = int(input())
    print(array[number])