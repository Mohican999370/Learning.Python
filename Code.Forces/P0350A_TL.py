__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'


def find_tl(corrects: list, wrongs: list) -> int:
    min_correct = min(corrects)
    max_correct = max(corrects)
    min_wrong = min(wrongs) - 1

    min_x = max(max_correct, 2 * min_correct)
    max_x = min_wrong

    return -1 if max_x < min_x else min_x


def main() -> int:
    (n, m) = map(int, input().split())
    corrects = [int(word) for word in input().split()]
    wrongs = [int(word) for word in input().split()]

    print(find_tl(corrects, wrongs))
    return 0


if __name__ == '__main__':
    exit(main())