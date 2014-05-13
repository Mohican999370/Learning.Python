__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'


def round_down(value: float) -> float:
    return int(value * 100) / 100


def next_year(balance: float, interest: int) -> float:
    return round_down(balance * (interest / 100 + 1))


def should_wait(money: int, require: int, interest: int) -> int:
    wait = 0

    while money < require:
        wait += 1
        money = next_year(money, interest)

    return wait


def main() -> int:
    n = int(input())
    results = [''] * n

    for i in range(n):
        (S, R, P) = map(int, input().split())
        results[i] = str(should_wait(S, R, P))

    print(' '.join(results))
    return 0


if __name__ == '__main__':
    exit(main())