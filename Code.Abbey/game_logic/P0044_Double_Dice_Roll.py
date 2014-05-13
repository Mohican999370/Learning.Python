__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'


def dice(number: int) -> int:
    return number % 6 + 1


def double_dice(number1: int, number2: int) -> int:
    return dice(number1) + dice(number2)


def double_dice_input() -> int:
    (number1, number2) = map(int, input().split())
    return double_dice(number1, number2)


def double_dice_input_to_string() -> str:
    return str(double_dice_input())


def main() -> int:
    n = int(input())
    results = [double_dice_input_to_string() for _ in range(n)]

    print(' '.join(results))
    return 0


if __name__ == '__main__':
    exit(main())