__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'


def decode(value: int) -> str:
    if '{0:b}'.format(value).count('1') % 2 != 0:
        return ''

    if value >= 128:
        value -= 128

    return chr(value)


def decode_input() -> str:
    data = [int(word) for word in input().split()]
    decoded_data = [decode(item) for item in data]

    return ''.join(decoded_data)


def main() -> int:
    print(decode_input().strip())
    return 0


if __name__ == '__main__':
    exit(main())