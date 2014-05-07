__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = 'http://codeforces.com/problemset/problem/141/A'
__version__ = '1.0'

from string import ascii_uppercase


def is_permutation(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False

    for letter in ascii_uppercase:
        if s1.count(letter) != s2.count(letter):
            return False

    return True


names = input() + input()
pile = input()

if (is_permutation(names, pile)):
    print('YES')
else:
    print('NO')