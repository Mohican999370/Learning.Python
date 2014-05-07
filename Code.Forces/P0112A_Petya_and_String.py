__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = 'http://codeforces.com/problemset/problem/112/A'
__version__ = '1.0'

string1, string2 = input(), input()


def stricmp(s1: str, s2: str) -> int:
    """
    Compares two strings case-insensitively
    """
    try:
        s1 = s1.lower()
        s2 = s2.lower()

        if s1 < s2:
            return -1
        elif s1 > s2:
            return 1
        else:
            return 0
    except AttributeError:
        print('Please input strings only')
        return None


print(stricmp(string1, string2))