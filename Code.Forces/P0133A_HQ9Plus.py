__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = 'http://codeforces.com/problemset/problem/133/A'
__version__ = '1.0'


def has_output(ins: str) -> str:
    for i in ins:
        if i == 'H' or i == 'Q' or i == '9':
            return 'YES'
    return 'NO'


instructions = input()
print(has_output(instructions))