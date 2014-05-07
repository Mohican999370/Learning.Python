__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = 'http://codeforces.com/problemset/problem/236/A'
__version__ = '1.0'

def get_gender(name: str) -> int:
    """
    Get the gender of a person by his/her name
    Return:
        1: male
        0: female
    """
    characters = set()

    for ch in name:
        characters.add(ch)

    return len(characters) % 2

messages = ['CHAT WITH HER!', 'IGNORE HIM!']
print(messages[get_gender(input())])