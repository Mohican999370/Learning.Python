__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'


def main() -> int:
    game_data = input().split()
    dictionary = {}

    for data in game_data:
        dictionary[data] = dictionary.get(data, 0) + 1

    results = [key for key in dictionary.keys() if dictionary[key] > 1]
    results = sorted(results)
    print(' '.join(results))

    return 0


if __name__ == '__main__':
    exit(main())