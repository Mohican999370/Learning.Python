__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'


def pythagore_it(a: int, b: int, c: int) -> str:
    c2_must_be = a * a + b * b
    c2_actual = c * c

    if c2_actual < c2_must_be:
        return 'A'
    elif c2_actual > c2_must_be:
        return 'O'
    else:
        return 'R'


def pythagore_input() -> str:
    (a, b, c) = map(int, input().split())
    return pythagore_it(a, b, c)


def main() -> int:
    n = int(input())
    results = [pythagore_input() for _ in range(n)]

    print(' '.join(results))
    return 0

if __name__ == '__main__':
    exit(main())