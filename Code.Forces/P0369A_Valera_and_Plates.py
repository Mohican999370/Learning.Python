__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'

(days, bowls, plates) = map(int, input().split())
temp = input()
type1, type2 = temp.count('1'), temp.count('2')

if bowls < type1:
    type1 -= bowls
    bowls = 0
else:
    bowls -= type1
    type1 = 0

dishes = bowls + plates

if dishes < type2:
    type2 -= dishes
else:
    type2 = 0

print(type1 + type2)