__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'


def shortest_distance(distances: list, start: int, end: int) -> int:
    if start > end:
        start, end = end, start

    home = sum(distances[start:end])
    away = sum(distances[end:]) + sum(distances[:start])

    return min(home, away)


input()
d = [0] + [int(i) for i in input().split()]
(s, t) = map(int, input().split())

print(shortest_distance(d, s, t))