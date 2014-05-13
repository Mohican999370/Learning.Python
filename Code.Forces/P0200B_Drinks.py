__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = 'http://codeforces.com/problemset/problem/200/B'
__version__ = '1.0'


def main() -> int:
    n = int(input())
    oranges = [int(word) for word in input().split()]

    print(sum(oranges) / n)

    return 0


if __name__ == '__main__':
    main()