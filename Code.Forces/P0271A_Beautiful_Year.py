__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = 'http://codeforces.com/problemset/problem/271/A'
__version__ = '1.0'

def is_beautiful_year(year: int) -> bool:
    year_string = "%d" % year
    year_digits = set()

    for digit in year_string:
        year_digits.add(digit)

    return len(year_digits) == len(year_string)

def find_next_beautiful_year(year: int) -> int:
    next_year = year + 1

    while (not is_beautiful_year(next_year)):
        next_year += 1

    return next_year

print(find_next_beautiful_year(int(input())))