__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = 'http://codeforces.com/problemset/problem/59/A'
__version__ = '1.0'

word = input()
uppercases = sum(char.upper() == char for char in word)

if (uppercases > len(word) // 2):
    print(word.upper())
else:
    print(word.lower())