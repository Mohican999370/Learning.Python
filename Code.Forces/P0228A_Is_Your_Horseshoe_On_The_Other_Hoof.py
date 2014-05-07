__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = 'http://codeforces.com/problemset/problem/228/A'
__version__ = '1.0'

def must_buy(shoes: list) -> int:
    distincts = set()

    for shoe in shoes:
        distincts.add(shoe)

    return len(shoes) - len(distincts)

horseshoes = [int(i) for i in input().split()]
print(must_buy(horseshoes))