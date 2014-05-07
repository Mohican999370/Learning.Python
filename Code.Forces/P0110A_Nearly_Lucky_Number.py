__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = 'http://codeforces.com/problemset/problem/110/A'
__version__ = '1.0'

def is_lucky_number(number: str) -> int:
    for ch in number:
        if ch != '4' and ch != '7':
            return 0

    return 1

def is_nearly_lucky_number(number: str) -> int:
    lucky_digts = number.count('4') + number.count('7')
    return is_lucky_number("%i" % lucky_digts)

messages = ['NO', 'YES']
print(messages[is_nearly_lucky_number(input())])