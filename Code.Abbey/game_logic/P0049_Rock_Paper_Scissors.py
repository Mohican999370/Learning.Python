__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'

game_rules = {
    'RR': 0, 'RP': -1, 'RS': 1,
    'PP': 0, 'PR': 1, 'PS': -1,
    'SS': 0, 'SR': -1, 'SP': 1
}


def game_run() -> str:
    game_data = input().split()
    game_result = sum([game_rules[data] for data in game_data])

    return '1' if game_result > 0 else '2'


def main():
    n = int(input())
    results = [game_run() for _ in range(n)]

    print(' '.join(results))
    return 0


if __name__ == '__main__':
    exit(main())