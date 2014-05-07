__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'


n = int(input())
arrivals_count = {}

for _ in range(n):
    arrival = input()
    arrivals_count[arrival] = arrivals_count.get(arrival, 0) + 1

print(max(arrivals_count.values()))