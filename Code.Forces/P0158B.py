__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__spec__ = 'http://codeforces.com/problemset/problem/158/B'
__version__ = '1.0'

n = int(input())
s = [int(i) for i in input().split()]
count = [0, 0, 0, 0, 0]

for i in s:
    count[i] += 1

# Group4, Group3 + Group1
result = count[4] + count[3]
count1 = 0 if count[1] <= count[3] else count[1] - count[3]

# Group2
result += count[2] // 2
count2 = 1 if count[2] % 2 else 0

if (count2 > 0):
    count1 += 2

result += count1 // 4

if (count1 % 4):
    result += 1

print(result)