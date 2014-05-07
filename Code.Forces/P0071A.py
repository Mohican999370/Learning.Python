__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__spec__ = 'http://codeforces.com/problemset/problem/71/A'
__version__ = '1.0'

n = int(input())

for i in range(n):
    word = input()
    length = len(word)

    if (length <= 10):
        print(word)
    else:
        print(word[0], length - 2, word[-1], sep='')