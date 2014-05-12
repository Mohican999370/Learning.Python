__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'

STRENGTH = 'strength'
BONUS = 'bonus'


def can_pass(strength: int, n_dragons: int, dragon_infos: list) -> bool:
    # sorts the dragons by their strength
    dragon_infos = sorted(dragon_infos, key=lambda k: k[STRENGTH])

    for i in range(n_dragons):
        if strength <= dragon_infos[i][STRENGTH]:
            return False
        else:
            strength += dragon_infos[i][BONUS]

    return True


def main() -> None:
    (s, n) = map(int, input().split())
    dragons = [None] * n

    for i in range(n):
        dragons[i] = {}
        (x, y) = map(int, input().split())
        dragons[i][STRENGTH] = x
        dragons[i][BONUS] = y

    print('YES' if can_pass(s, n, dragons) else 'NO')


if __name__ == "__main__":
    main()