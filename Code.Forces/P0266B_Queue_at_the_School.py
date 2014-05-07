__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = 'http://codeforces.com/problemset/problem/266/B'
__version__ = '1.0'

def get_status(length: int, time: int, queue_string: str) -> str:
    queue_list = list(queue_string)

    for _ in range(time):
        index = queue_string.find('BG')

        while (index >= 0):
            queue_list[index] = 'G'
            queue_list[index + 1] = 'B'
            index = queue_string.find('BG', index + 2)

        queue_string = ''.join(queue_list)

    return queue_string

(n, t) = map(int, input().split())
s = input()
print(get_status(n, t, s))