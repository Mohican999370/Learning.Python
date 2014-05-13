__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = 'http://codeforces.com/problemset/problem/381/A'
__version__ = '1.0'

n = int(input())
cards = [int(word) for word in input().split()]
left, right = 0, n - 1
scores = [0, 0]
turn = 0

for _ in range(n):
    if cards[left] > cards[right]:
        scores[turn] += cards[left]
        left += 1
    else:
        scores[turn] += cards[right]
        right -= 1

    turn = 1 - turn

print(' '.join([str(i) for i in scores]))