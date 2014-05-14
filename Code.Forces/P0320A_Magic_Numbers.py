__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'


def is_magic_number(number: str) -> bool:
    if (number[0] != '1') or ('444' in number):
        return False

    for char in number:
        if (char != '1') and (char != '4'):
            return False

    return True


def main() -> int:
    number = input()

    print('YES' if is_magic_number(number) else 'NO')
    return 0


if __name__ == '__main__':
    exit(main())